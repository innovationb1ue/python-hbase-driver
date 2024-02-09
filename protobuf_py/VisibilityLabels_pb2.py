# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VisibilityLabels.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Client_pb2 as Client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16VisibilityLabels.proto\x12\x02pb\x1a\x0c\x43lient.proto\"@\n\x17VisibilityLabelsRequest\x12%\n\x08visLabel\x18\x01 \x03(\x0b\x32\x13.pb.VisibilityLabel\"1\n\x0fVisibilityLabel\x12\r\n\x05label\x18\x01 \x02(\x0c\x12\x0f\n\x07ordinal\x18\x02 \x01(\r\"B\n\x18VisibilityLabelsResponse\x12&\n\x06result\x18\x01 \x03(\x0b\x32\x16.pb.RegionActionResult\"-\n\x0fSetAuthsRequest\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12\x0c\n\x04\x61uth\x18\x02 \x03(\x0c\"0\n\x12UserAuthorizations\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12\x0c\n\x04\x61uth\x18\x02 \x03(\r\"D\n\x17MultiUserAuthorizations\x12)\n\tuserAuths\x18\x01 \x03(\x0b\x32\x16.pb.UserAuthorizations\"\x1f\n\x0fGetAuthsRequest\x12\x0c\n\x04user\x18\x01 \x02(\x0c\".\n\x10GetAuthsResponse\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12\x0c\n\x04\x61uth\x18\x02 \x03(\x0c\"\"\n\x11ListLabelsRequest\x12\r\n\x05regex\x18\x01 \x01(\t\"#\n\x12ListLabelsResponse\x12\r\n\x05label\x18\x01 \x03(\x0c\x32\xd5\x02\n\x17VisibilityLabelsService\x12\x46\n\taddLabels\x12\x1b.pb.VisibilityLabelsRequest\x1a\x1c.pb.VisibilityLabelsResponse\x12=\n\x08setAuths\x12\x13.pb.SetAuthsRequest\x1a\x1c.pb.VisibilityLabelsResponse\x12?\n\nclearAuths\x12\x13.pb.SetAuthsRequest\x1a\x1c.pb.VisibilityLabelsResponse\x12\x35\n\x08getAuths\x12\x13.pb.GetAuthsRequest\x1a\x14.pb.GetAuthsResponse\x12;\n\nlistLabels\x12\x15.pb.ListLabelsRequest\x1a\x16.pb.ListLabelsResponseBL\n*org.apache.hadoop.hbase.protobuf.generatedB\x16VisibilityLabelsProtosH\x01\x88\x01\x01\xa0\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'VisibilityLabels_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*org.apache.hadoop.hbase.protobuf.generatedB\026VisibilityLabelsProtosH\001\210\001\001\240\001\001'
  _globals['_VISIBILITYLABELSREQUEST']._serialized_start=44
  _globals['_VISIBILITYLABELSREQUEST']._serialized_end=108
  _globals['_VISIBILITYLABEL']._serialized_start=110
  _globals['_VISIBILITYLABEL']._serialized_end=159
  _globals['_VISIBILITYLABELSRESPONSE']._serialized_start=161
  _globals['_VISIBILITYLABELSRESPONSE']._serialized_end=227
  _globals['_SETAUTHSREQUEST']._serialized_start=229
  _globals['_SETAUTHSREQUEST']._serialized_end=274
  _globals['_USERAUTHORIZATIONS']._serialized_start=276
  _globals['_USERAUTHORIZATIONS']._serialized_end=324
  _globals['_MULTIUSERAUTHORIZATIONS']._serialized_start=326
  _globals['_MULTIUSERAUTHORIZATIONS']._serialized_end=394
  _globals['_GETAUTHSREQUEST']._serialized_start=396
  _globals['_GETAUTHSREQUEST']._serialized_end=427
  _globals['_GETAUTHSRESPONSE']._serialized_start=429
  _globals['_GETAUTHSRESPONSE']._serialized_end=475
  _globals['_LISTLABELSREQUEST']._serialized_start=477
  _globals['_LISTLABELSREQUEST']._serialized_end=511
  _globals['_LISTLABELSRESPONSE']._serialized_start=513
  _globals['_LISTLABELSRESPONSE']._serialized_end=548
  _globals['_VISIBILITYLABELSSERVICE']._serialized_start=551
  _globals['_VISIBILITYLABELSSERVICE']._serialized_end=892
# @@protoc_insertion_point(module_scope)
