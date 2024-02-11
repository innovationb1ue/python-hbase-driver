import random
import socket
from abc import abstractmethod
from io import StringIO
from struct import pack, unpack

from google.protobuf import message

from RPC_pb2 import ConnectionHeader, RequestHeader, ResponseHeader
from src.response import response_types
from util.varint import to_varint, decoder


class Connection:
    def __init__(self, service_name):
        assert service_name in ["ClientService", "MasterService"]
        self.service_name = service_name

    @abstractmethod
    def connect(self, host, port=16000, timeout=3, user="pythonHbaseDriver"):
        self.conn = socket.create_connection((host, port), timeout=timeout)
        ch = ConnectionHeader()
        ch.user_info.effective_user = user
        ch.service_name = self.service_name
        serialized = ch.SerializeToString()
        # 6 bytes : 'HBas' + RPC_VERSION(0) + AUTH_CODE(80) +
        msg = b"HBas\x00\x50" + pack(">I", len(serialized)) + serialized
        self.conn.send(msg)

    def send_request(self, req: message.Message, method_name: str):
        rpc_serialized = req.SerializeToString()
        # todo: save id and check result later
        call_id = random.randint(1, 999)
        serialized_header = self._get_call_header_bytes(method_name, call_id)
        rpc_length_bytes = to_varint(len(rpc_serialized)).encode('utf-8')
        total_size = 4 + 1 + len(serialized_header) + len(rpc_length_bytes) + len(rpc_serialized)

        # Total length doesn't include the initial 4 bytes (for the total_length uint32)
        # size(4bytes) + header size(1byte)
        to_send = pack(">IB", total_size - 4, len(serialized_header))
        to_send += serialized_header + rpc_length_bytes + rpc_serialized

        self.conn.send(to_send)

        return self.receive_rpc(call_id, req, method_name)

    def _get_call_header_bytes(self, method_name, call_id: int):
        header = RequestHeader()
        header.call_id = call_id
        header.method_name = method_name
        header.request_param = True
        serialized_header: bytes = header.SerializeToString()
        return serialized_header

    # Receives exactly n bytes from the socket. Will block until n bytes are
    # received. If a socket is closed (RegionServer died) then raise an
    # exception that goes all the way back to the main client
    def _recv_n(self, sock: socket.socket, n):
        res = b''
        partial_len = 0
        while partial_len < n:
            packet = sock.recv(n - partial_len)
            if not packet:
                raise socket.error()
            partial_len += len(packet)
            res += packet
        return res

    def receive_rpc(self, call_id, rq: message.Message, rq_type: str, data=None):
        # Total message length is going to be the first four bytes
        # (little-endian uint32)
        try:
            msg_length = self._recv_n(self.conn, 4)
            if msg_length is None:
                raise
            msg_length = unpack(">I", msg_length)[0]
            # The message is then going to be however many bytes the first four
            # bytes specified. We don't want to overread or underread as that'll
            # cause havoc.
            full_data = self._recv_n(self.conn, msg_length)
        except socket.error:
            raise Exception("cant read enough data when receiving response. ")
        # Pass in the full data as well as your current position to the
        # decoder. It'll then return two variables:
        #       - next_pos: The number of bytes of data specified by the varint
        #       - pos: The starting location of the data to read.
        next_pos, pos = decoder(full_data, 0)
        header = ResponseHeader()
        header.ParseFromString(full_data[pos: pos + next_pos])
        pos += next_pos
        if header.call_id != call_id:
            # call_ids don't match? Looks like a different thread nabbed our
            # response.
            raise Exception("call id is wrong. ")

        rpc = response_types[rq_type]()
        rpc.ParseFromString(full_data[pos: pos + next_pos])
        # The rpc is fully built!
        return rpc
