# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Comparator.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x43omparator.proto\x12\x08hbase.pb\"9\n\nComparator\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1d\n\x15serialized_comparator\x18\x02 \x01(\x0c\"$\n\x13\x42yteArrayComparable\x12\r\n\x05value\x18\x01 \x01(\x0c\"E\n\x10\x42inaryComparator\x12\x31\n\ncomparable\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.ByteArrayComparable\"C\n\x0eLongComparator\x12\x31\n\ncomparable\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.ByteArrayComparable\"K\n\x16\x42inaryPrefixComparator\x12\x31\n\ncomparable\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.ByteArrayComparable\"\xa0\x01\n\rBitComparator\x12\x31\n\ncomparable\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.ByteArrayComparable\x12\x35\n\nbitwise_op\x18\x02 \x02(\x0e\x32!.hbase.pb.BitComparator.BitwiseOp\"%\n\tBitwiseOp\x12\x07\n\x03\x41ND\x10\x01\x12\x06\n\x02OR\x10\x02\x12\x07\n\x03XOR\x10\x03\"\x10\n\x0eNullComparator\"`\n\x15RegexStringComparator\x12\x0f\n\x07pattern\x18\x01 \x02(\t\x12\x15\n\rpattern_flags\x18\x02 \x02(\x05\x12\x0f\n\x07\x63harset\x18\x03 \x02(\t\x12\x0e\n\x06\x65ngine\x18\x04 \x01(\t\"%\n\x13SubstringComparator\x12\x0e\n\x06substr\x18\x01 \x02(\t\"I\n\x14\x42igDecimalComparator\x12\x31\n\ncomparable\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.ByteArrayComparable\":\n\x19\x42inaryComponentComparator\x12\r\n\x05value\x18\x01 \x02(\x0c\x12\x0e\n\x06offset\x18\x02 \x02(\rBM\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\x10\x43omparatorProtosH\x01\x88\x01\x01\xa0\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Comparator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\020ComparatorProtosH\001\210\001\001\240\001\001'
  _globals['_COMPARATOR']._serialized_start=30
  _globals['_COMPARATOR']._serialized_end=87
  _globals['_BYTEARRAYCOMPARABLE']._serialized_start=89
  _globals['_BYTEARRAYCOMPARABLE']._serialized_end=125
  _globals['_BINARYCOMPARATOR']._serialized_start=127
  _globals['_BINARYCOMPARATOR']._serialized_end=196
  _globals['_LONGCOMPARATOR']._serialized_start=198
  _globals['_LONGCOMPARATOR']._serialized_end=265
  _globals['_BINARYPREFIXCOMPARATOR']._serialized_start=267
  _globals['_BINARYPREFIXCOMPARATOR']._serialized_end=342
  _globals['_BITCOMPARATOR']._serialized_start=345
  _globals['_BITCOMPARATOR']._serialized_end=505
  _globals['_BITCOMPARATOR_BITWISEOP']._serialized_start=468
  _globals['_BITCOMPARATOR_BITWISEOP']._serialized_end=505
  _globals['_NULLCOMPARATOR']._serialized_start=507
  _globals['_NULLCOMPARATOR']._serialized_end=523
  _globals['_REGEXSTRINGCOMPARATOR']._serialized_start=525
  _globals['_REGEXSTRINGCOMPARATOR']._serialized_end=621
  _globals['_SUBSTRINGCOMPARATOR']._serialized_start=623
  _globals['_SUBSTRINGCOMPARATOR']._serialized_end=660
  _globals['_BIGDECIMALCOMPARATOR']._serialized_start=662
  _globals['_BIGDECIMALCOMPARATOR']._serialized_end=735
  _globals['_BINARYCOMPONENTCOMPARATOR']._serialized_start=737
  _globals['_BINARYCOMPONENTCOMPARATOR']._serialized_end=795
# @@protoc_insertion_point(module_scope)
