from collections import defaultdict

from hbasedriver.protobuf_py.Client_pb2 import ScanRequest, ScanResponse


class Scan:
    MAX_ROWKEY_LENGTH = 32767

    def __init__(self, start_row: bytes = b'', end_row: bytes = b''):
        self.start_row = start_row
        self.start_row_inclusive = True
        self.end_row = end_row
        self.end_row_inclusive = True
        self.min_stamp: int = 0
        self.max_stamp: int = 0x7fffffffffffffff
        self.family_map: dict[bytes, list] = defaultdict(list)
        self.limit: int = 20

    # Get all columns from the specified family.
    def add_family(self, family: bytes):
        self.family_map[family] = []
        return self

    def set_limit(self, limit):
        """
        set the maximum of rows we want for this scan.
        :param limit:
        :return:
        """
        self.limit = limit

    def add_column(self, family: bytes, qualifier: bytes):
        self.family_map[family].append(qualifier)
        return self

    def set_time_range(self, min_stamp, max_stamp):
        self.min_stamp = min_stamp
        self.max_stamp = max_stamp

    def with_start_row(self, start_row: bytes, inclusive=True):
        if len(start_row) > Scan.MAX_ROWKEY_LENGTH:
            raise ValueError("rowkey length must be smaller than {}".format(Scan.MAX_ROWKEY_LENGTH))
        self.start_row = start_row
        self.start_row_inclusive = inclusive
        return self

    def with_end_row(self, end_row: bytes, inclusive=True):
        if len(end_row) > Scan.MAX_ROWKEY_LENGTH:
            raise ValueError("rowkey length must be smaller than {}".format(Scan.MAX_ROWKEY_LENGTH))
        self.end_row = end_row
        self.end_row_inclusive = inclusive


class ScanResultIterator:
    def __init__(self, scanner_id: int, scan: Scan, rs_conn):
        self.scanner_id = scanner_id
        self.rs_conn = rs_conn
        self.scan = scan

    def __next__(self):
        rq2 = ScanRequest()
        rq2.scanner_id = self.scanner_id
        rq2.number_of_rows = self.scan.limit
        resp2: ScanResponse = self.rs_conn.send_request(rq2, "Scan")
        # todo: build object mapping to rows here.
        return resp2.results
