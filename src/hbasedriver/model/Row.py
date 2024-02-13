import logging
from collections import defaultdict

logger = logging.getLogger("Row")


class Row:
    """
    Represent a row of data in hbase, with the unique rowkey.
    """

    def __init__(self, rowkey: bytes, kv: dict):
        self.rowkey = rowkey
        self.kv = kv

    # get the value of target column, return None if not exist.
    def get(self, cf, qf):
        tmp = self.kv.get(bytes(cf, 'utf-8'))
        if tmp:
            return tmp.get(bytes(qf, 'utf-8'))
        else:
            return None

    @staticmethod
    def from_result(result):
        # provide no cells, we return None here.
        if len(result.cell) == 0:
            return None
        kv = defaultdict(dict)
        for c in result.cell:
            kv[c.family][c.qualifier] = c.value
        return Row(result.cell[0].row, kv)

    @staticmethod
    def from_cell(cell):
        return Row(cell.row, {cell.family: {cell.qualifier: cell.value}})
