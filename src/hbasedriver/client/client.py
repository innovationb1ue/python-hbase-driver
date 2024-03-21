import time

from hbasedriver import zk
from hbasedriver.client.table import Table
from hbasedriver.master import MasterConnection
from hbasedriver.meta_server import MetaRsConnection
from hbasedriver.protobuf_py.Client_pb2 import ScanRequest, Column, ScanResponse


class Client:
    """
    Client class only contains Admin operations .

    Table and data manipulation actions are in class Table.
    Get Table instance by Client.get_table(ns, tb)

    """

    def __init__(self, zk_quorum: list):
        self.zk_quorum = zk_quorum
        self.master_host, self.master_port = zk.locate_master(zk_quorum)
        self.meta_host, self.meta_port = zk.locate_meta_region(zk_quorum)

        self.master_conn = MasterConnection().connect(self.master_host, self.master_port)
        self.meta_conn = MetaRsConnection().connect(self.meta_host, self.meta_port)

    def refresh_master(self):
        self.master_host, self.master_port = zk.locate_meta_region(self.zk_quorum)

    def create_table(self, ns: bytes, tb: bytes, columns, split_keys=None):
        self.master_conn.create_table(ns, tb, columns, split_keys)
        # check regions online
        self.check_regions_online(ns, tb, split_keys)

    def check_regions_online(self, ns: bytes, tb: bytes, split_keys: list):
        # Construct a ScanRequest to check if regions are online for each split key
        online_regions = 0
        while online_regions != len(split_keys):
            for split_key in split_keys:
                rq = ScanRequest()
                if ns is None or len(ns) == 0:
                    rq.scan.start_row = tb + b"," + split_key + b','
                else:
                    rq.scan.start_row = ns + b':' + tb + b"," + split_key + b','
                rq.scan.column.append(Column(family="info".encode("utf-8")))
                rq.number_of_rows = 1
                rq.region.type = 1
                rq.region.value = "hbase:meta,,1".encode('utf-8')

                # Send the scan request to the meta region server
                scan_resp: ScanResponse = self.meta_conn.send_request(rq, "Scan")

                if not scan_resp.results:
                    break
                for cell in scan_resp.results[0].cell:
                    if cell.qualifier == b'state' and cell.value == b'OPEN':
                        online_regions += 1

            if online_regions != len(split_keys):
                time.sleep(3)

    def delete_table(self, ns: bytes, tb: bytes):
        self.master_conn.delete_table(ns, tb)

    def disable_table(self, ns: bytes, tb: bytes):
        self.master_conn.disable_table(ns, tb)

    def get_table(self, ns, tb):
        return Table(self.zk_quorum, ns, tb, self.meta_conn)
