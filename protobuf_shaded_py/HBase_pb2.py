# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HBase.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bHBase.proto\x12\x02pb\"1\n\tTableName\x12\x11\n\tnamespace\x18\x01 \x02(\x0c\x12\x11\n\tqualifier\x18\x02 \x02(\x0c\"\xb4\x01\n\x0bTableSchema\x12!\n\ntable_name\x18\x01 \x01(\x0b\x32\r.pb.TableName\x12&\n\nattributes\x18\x02 \x03(\x0b\x32\x12.pb.BytesBytesPair\x12/\n\x0f\x63olumn_families\x18\x03 \x03(\x0b\x32\x16.pb.ColumnFamilySchema\x12)\n\rconfiguration\x18\x04 \x03(\x0b\x32\x12.pb.NameStringPair\"r\n\nTableState\x12#\n\x05state\x18\x01 \x02(\x0e\x32\x14.pb.TableState.State\"?\n\x05State\x12\x0b\n\x07\x45NABLED\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\r\n\tDISABLING\x10\x02\x12\x0c\n\x08\x45NABLING\x10\x03\"u\n\x12\x43olumnFamilySchema\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12&\n\nattributes\x18\x02 \x03(\x0b\x32\x12.pb.BytesBytesPair\x12)\n\rconfiguration\x18\x03 \x03(\x0b\x32\x12.pb.NameStringPair\"\x9d\x01\n\nRegionInfo\x12\x11\n\tregion_id\x18\x01 \x02(\x04\x12!\n\ntable_name\x18\x02 \x02(\x0b\x32\r.pb.TableName\x12\x11\n\tstart_key\x18\x03 \x01(\x0c\x12\x0f\n\x07\x65nd_key\x18\x04 \x01(\x0c\x12\x0f\n\x07offline\x18\x05 \x01(\x08\x12\r\n\x05split\x18\x06 \x01(\x08\x12\x15\n\nreplica_id\x18\x07 \x01(\x05:\x01\x30\"4\n\x0c\x46\x61voredNodes\x12$\n\x0c\x66\x61vored_node\x18\x01 \x03(\x0b\x32\x0e.pb.ServerName\"\x98\x01\n\x0fRegionSpecifier\x12\x35\n\x04type\x18\x01 \x02(\x0e\x32\'.pb.RegionSpecifier.RegionSpecifierType\x12\r\n\x05value\x18\x02 \x02(\x0c\"?\n\x13RegionSpecifierType\x12\x0f\n\x0bREGION_NAME\x10\x01\x12\x17\n\x13\x45NCODED_REGION_NAME\x10\x02\"%\n\tTimeRange\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x04\x12\n\n\x02to\x18\x02 \x01(\x04\",\n\x10TimeRangeTracker\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x04\x12\n\n\x02to\x18\x02 \x01(\x04\"Q\n\x15\x43olumnFamilyTimeRange\x12\x15\n\rcolumn_family\x18\x01 \x02(\x0c\x12!\n\ntime_range\x18\x02 \x02(\x0b\x32\r.pb.TimeRange\"A\n\nServerName\x12\x11\n\thost_name\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x12\n\nstart_code\x18\x03 \x01(\x04\"\x1b\n\x0b\x43oprocessor\x12\x0c\n\x04name\x18\x01 \x02(\t\"-\n\x0eNameStringPair\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\",\n\rNameBytesPair\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"/\n\x0e\x42ytesBytesPair\x12\r\n\x05\x66irst\x18\x01 \x02(\x0c\x12\x0e\n\x06second\x18\x02 \x02(\x0c\",\n\rNameInt64Pair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\"\x80\x01\n\x14ProcedureDescription\x12\x11\n\tsignature\x18\x01 \x02(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x18\n\rcreation_time\x18\x03 \x01(\x03:\x01\x30\x12)\n\rconfiguration\x18\x04 \x03(\x0b\x32\x12.pb.NameStringPair\"\n\n\x08\x45mptyMsg\"\x1b\n\x07LongMsg\x12\x10\n\x08long_msg\x18\x01 \x02(\x03\"\x1f\n\tDoubleMsg\x12\x12\n\ndouble_msg\x18\x01 \x02(\x01\"\'\n\rBigDecimalMsg\x12\x16\n\x0e\x62igdecimal_msg\x18\x01 \x02(\x0c\"5\n\x04UUID\x12\x16\n\x0eleast_sig_bits\x18\x01 \x02(\x04\x12\x15\n\rmost_sig_bits\x18\x02 \x02(\x04\"N\n\x13NamespaceDescriptor\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12)\n\rconfiguration\x18\x02 \x03(\x0b\x32\x12.pb.NameStringPair\"\x9d\x01\n\x0bVersionInfo\x12\x0f\n\x07version\x18\x01 \x02(\t\x12\x0b\n\x03url\x18\x02 \x02(\t\x12\x10\n\x08revision\x18\x03 \x02(\t\x12\x0c\n\x04user\x18\x04 \x02(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x02(\t\x12\x14\n\x0csrc_checksum\x18\x06 \x02(\t\x12\x15\n\rversion_major\x18\x07 \x01(\r\x12\x15\n\rversion_minor\x18\x08 \x01(\r\"K\n\x10RegionServerInfo\x12\x10\n\x08infoPort\x18\x01 \x01(\x05\x12%\n\x0cversion_info\x18\x02 \x01(\x0b\x32\x0f.pb.VersionInfo\"c\n\x16RegionExceptionMessage\x12#\n\x06region\x18\x01 \x02(\x0b\x32\x13.pb.RegionSpecifier\x12$\n\texception\x18\x02 \x02(\x0b\x32\x11.pb.NameBytesPair\"\x8a\x01\n\x12\x43\x61\x63heEvictionStats\x12\x16\n\x0e\x65victed_blocks\x18\x01 \x01(\x03\x12\x15\n\rbytes_evicted\x18\x02 \x01(\x03\x12\x16\n\x0emax_cache_size\x18\x03 \x01(\x03\x12-\n\texception\x18\x04 \x03(\x0b\x32\x1a.pb.RegionExceptionMessage\"k\n\x0eRegionLocation\x12#\n\x0bregion_info\x18\x01 \x02(\x0b\x32\x0e.pb.RegionInfo\x12#\n\x0bserver_name\x18\x02 \x01(\x0b\x32\x0e.pb.ServerName\x12\x0f\n\x07seq_num\x18\x03 \x02(\x03\"9\n\nLogRequest\x12\x16\n\x0elog_class_name\x18\x01 \x02(\t\x12\x13\n\x0blog_message\x18\x02 \x02(\x0c\"7\n\x08LogEntry\x12\x16\n\x0elog_class_name\x18\x01 \x02(\t\x12\x13\n\x0blog_message\x18\x02 \x02(\x0c*r\n\x0b\x43ompareType\x12\x08\n\x04LESS\x10\x00\x12\x11\n\rLESS_OR_EQUAL\x10\x01\x12\t\n\x05\x45QUAL\x10\x02\x12\r\n\tNOT_EQUAL\x10\x03\x12\x14\n\x10GREATER_OR_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\t\n\x05NO_OP\x10\x06*n\n\x08TimeUnit\x12\x0f\n\x0bNANOSECONDS\x10\x01\x12\x10\n\x0cMICROSECONDS\x10\x02\x12\x10\n\x0cMILLISECONDS\x10\x03\x12\x0b\n\x07SECONDS\x10\x04\x12\x0b\n\x07MINUTES\x10\x05\x12\t\n\x05HOURS\x10\x06\x12\x08\n\x04\x44\x41YS\x10\x07\x42\x45\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\x0bHBaseProtosH\x01\xa0\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HBase_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\013HBaseProtosH\001\240\001\001'
  _globals['_COMPARETYPE']._serialized_start=2394
  _globals['_COMPARETYPE']._serialized_end=2508
  _globals['_TIMEUNIT']._serialized_start=2510
  _globals['_TIMEUNIT']._serialized_end=2620
  _globals['_TABLENAME']._serialized_start=19
  _globals['_TABLENAME']._serialized_end=68
  _globals['_TABLESCHEMA']._serialized_start=71
  _globals['_TABLESCHEMA']._serialized_end=251
  _globals['_TABLESTATE']._serialized_start=253
  _globals['_TABLESTATE']._serialized_end=367
  _globals['_TABLESTATE_STATE']._serialized_start=304
  _globals['_TABLESTATE_STATE']._serialized_end=367
  _globals['_COLUMNFAMILYSCHEMA']._serialized_start=369
  _globals['_COLUMNFAMILYSCHEMA']._serialized_end=486
  _globals['_REGIONINFO']._serialized_start=489
  _globals['_REGIONINFO']._serialized_end=646
  _globals['_FAVOREDNODES']._serialized_start=648
  _globals['_FAVOREDNODES']._serialized_end=700
  _globals['_REGIONSPECIFIER']._serialized_start=703
  _globals['_REGIONSPECIFIER']._serialized_end=855
  _globals['_REGIONSPECIFIER_REGIONSPECIFIERTYPE']._serialized_start=792
  _globals['_REGIONSPECIFIER_REGIONSPECIFIERTYPE']._serialized_end=855
  _globals['_TIMERANGE']._serialized_start=857
  _globals['_TIMERANGE']._serialized_end=894
  _globals['_TIMERANGETRACKER']._serialized_start=896
  _globals['_TIMERANGETRACKER']._serialized_end=940
  _globals['_COLUMNFAMILYTIMERANGE']._serialized_start=942
  _globals['_COLUMNFAMILYTIMERANGE']._serialized_end=1023
  _globals['_SERVERNAME']._serialized_start=1025
  _globals['_SERVERNAME']._serialized_end=1090
  _globals['_COPROCESSOR']._serialized_start=1092
  _globals['_COPROCESSOR']._serialized_end=1119
  _globals['_NAMESTRINGPAIR']._serialized_start=1121
  _globals['_NAMESTRINGPAIR']._serialized_end=1166
  _globals['_NAMEBYTESPAIR']._serialized_start=1168
  _globals['_NAMEBYTESPAIR']._serialized_end=1212
  _globals['_BYTESBYTESPAIR']._serialized_start=1214
  _globals['_BYTESBYTESPAIR']._serialized_end=1261
  _globals['_NAMEINT64PAIR']._serialized_start=1263
  _globals['_NAMEINT64PAIR']._serialized_end=1307
  _globals['_PROCEDUREDESCRIPTION']._serialized_start=1310
  _globals['_PROCEDUREDESCRIPTION']._serialized_end=1438
  _globals['_EMPTYMSG']._serialized_start=1440
  _globals['_EMPTYMSG']._serialized_end=1450
  _globals['_LONGMSG']._serialized_start=1452
  _globals['_LONGMSG']._serialized_end=1479
  _globals['_DOUBLEMSG']._serialized_start=1481
  _globals['_DOUBLEMSG']._serialized_end=1512
  _globals['_BIGDECIMALMSG']._serialized_start=1514
  _globals['_BIGDECIMALMSG']._serialized_end=1553
  _globals['_UUID']._serialized_start=1555
  _globals['_UUID']._serialized_end=1608
  _globals['_NAMESPACEDESCRIPTOR']._serialized_start=1610
  _globals['_NAMESPACEDESCRIPTOR']._serialized_end=1688
  _globals['_VERSIONINFO']._serialized_start=1691
  _globals['_VERSIONINFO']._serialized_end=1848
  _globals['_REGIONSERVERINFO']._serialized_start=1850
  _globals['_REGIONSERVERINFO']._serialized_end=1925
  _globals['_REGIONEXCEPTIONMESSAGE']._serialized_start=1927
  _globals['_REGIONEXCEPTIONMESSAGE']._serialized_end=2026
  _globals['_CACHEEVICTIONSTATS']._serialized_start=2029
  _globals['_CACHEEVICTIONSTATS']._serialized_end=2167
  _globals['_REGIONLOCATION']._serialized_start=2169
  _globals['_REGIONLOCATION']._serialized_end=2276
  _globals['_LOGREQUEST']._serialized_start=2278
  _globals['_LOGREQUEST']._serialized_end=2335
  _globals['_LOGENTRY']._serialized_start=2337
  _globals['_LOGENTRY']._serialized_end=2392
# @@protoc_insertion_point(module_scope)
