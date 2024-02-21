# hbase-driver

Native Hbase driver in Python. (No thrift)

### Introduction

- written in pure Python
- native HBase protocol support (HBase 2.X+)
- Support both admin operations and regionserver calls.

### Installation (pip)

```
pip3 install hbase-driver
```

### Get Started

```python
from hbasedriver.client import Client
from hbasedriver.operations import Put, Get, Scan
from hbasedriver.exceptions.RemoteException import TableExistsException

# lets say your hbase instance runs on 127.0.0.1 (zk quorum address)
client = Client(["127.0.0.1"])
try:
    client.create_table("", "mytable", ['cf1', 'cf2'])
except TableExistsException:
    pass
table = client.get_table("", "mytable")
table.put(Put(b'row1').add_column(b'cf1', b'qf', b'666'))
table.put(Put(b'row1').add_column(b'cf2', b'qf', b'777'))
result = table.get(Get(b"row1").add_column(b'cf1', b'qf'))
print(result)

scan_result = table.scan(Scan(b"row1").add_family(b'cf1'))
for row in scan_result:
    print(row)
```

### Implemented

- Create, Disable, Delete table
- Put
- Get
- DELETE
- Scan

### TODOs

- Filters
- More params in the operations. 
