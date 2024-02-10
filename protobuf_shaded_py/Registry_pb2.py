# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Registry.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HBase_pb2 as HBase__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eRegistry.proto\x12\x02pb\x1a\x0bHBase.proto\"\x15\n\x13GetClusterIdRequest\"*\n\x14GetClusterIdResponse\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\x18\n\x16GetActiveMasterRequest\">\n\x17GetActiveMasterResponse\x12#\n\x0bserver_name\x18\x01 \x01(\x0b\x32\x0e.pb.ServerName\"\x17\n\x11GetMastersRequest:\x02\x18\x01\"U\n\x17GetMastersResponseEntry\x12#\n\x0bserver_name\x18\x01 \x02(\x0b\x32\x0e.pb.ServerName\x12\x11\n\tis_active\x18\x02 \x02(\x08:\x02\x18\x01\"M\n\x12GetMastersResponse\x12\x33\n\x0emaster_servers\x18\x01 \x03(\x0b\x32\x1b.pb.GetMastersResponseEntry:\x02\x18\x01\"\x1f\n\x1dGetMetaRegionLocationsRequest\"L\n\x1eGetMetaRegionLocationsResponse\x12*\n\x0emeta_locations\x18\x01 \x03(\x0b\x32\x12.pb.RegionLocation\"\x1a\n\x18GetBootstrapNodesRequest\"@\n\x19GetBootstrapNodesResponse\x12#\n\x0bserver_name\x18\x01 \x03(\x0b\x32\x0e.pb.ServerName2\x97\x03\n\x11\x43lientMetaService\x12\x41\n\x0cGetClusterId\x12\x17.pb.GetClusterIdRequest\x1a\x18.pb.GetClusterIdResponse\x12J\n\x0fGetActiveMaster\x12\x1a.pb.GetActiveMasterRequest\x1a\x1b.pb.GetActiveMasterResponse\x12@\n\nGetMasters\x12\x15.pb.GetMastersRequest\x1a\x16.pb.GetMastersResponse\"\x03\x88\x02\x01\x12_\n\x16GetMetaRegionLocations\x12!.pb.GetMetaRegionLocationsRequest\x1a\".pb.GetMetaRegionLocationsResponse\x12P\n\x11GetBootstrapNodes\x12\x1c.pb.GetBootstrapNodesRequest\x1a\x1d.pb.GetBootstrapNodesResponseBK\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\x0eRegistryProtosH\x01\x88\x01\x01\xa0\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Registry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\016RegistryProtosH\001\210\001\001\240\001\001'
  _globals['_GETMASTERSREQUEST']._options = None
  _globals['_GETMASTERSREQUEST']._serialized_options = b'\030\001'
  _globals['_GETMASTERSRESPONSEENTRY']._options = None
  _globals['_GETMASTERSRESPONSEENTRY']._serialized_options = b'\030\001'
  _globals['_GETMASTERSRESPONSE']._options = None
  _globals['_GETMASTERSRESPONSE']._serialized_options = b'\030\001'
  _globals['_CLIENTMETASERVICE'].methods_by_name['GetMasters']._options = None
  _globals['_CLIENTMETASERVICE'].methods_by_name['GetMasters']._serialized_options = b'\210\002\001'
  _globals['_GETCLUSTERIDREQUEST']._serialized_start=35
  _globals['_GETCLUSTERIDREQUEST']._serialized_end=56
  _globals['_GETCLUSTERIDRESPONSE']._serialized_start=58
  _globals['_GETCLUSTERIDRESPONSE']._serialized_end=100
  _globals['_GETACTIVEMASTERREQUEST']._serialized_start=102
  _globals['_GETACTIVEMASTERREQUEST']._serialized_end=126
  _globals['_GETACTIVEMASTERRESPONSE']._serialized_start=128
  _globals['_GETACTIVEMASTERRESPONSE']._serialized_end=190
  _globals['_GETMASTERSREQUEST']._serialized_start=192
  _globals['_GETMASTERSREQUEST']._serialized_end=215
  _globals['_GETMASTERSRESPONSEENTRY']._serialized_start=217
  _globals['_GETMASTERSRESPONSEENTRY']._serialized_end=302
  _globals['_GETMASTERSRESPONSE']._serialized_start=304
  _globals['_GETMASTERSRESPONSE']._serialized_end=381
  _globals['_GETMETAREGIONLOCATIONSREQUEST']._serialized_start=383
  _globals['_GETMETAREGIONLOCATIONSREQUEST']._serialized_end=414
  _globals['_GETMETAREGIONLOCATIONSRESPONSE']._serialized_start=416
  _globals['_GETMETAREGIONLOCATIONSRESPONSE']._serialized_end=492
  _globals['_GETBOOTSTRAPNODESREQUEST']._serialized_start=494
  _globals['_GETBOOTSTRAPNODESREQUEST']._serialized_end=520
  _globals['_GETBOOTSTRAPNODESRESPONSE']._serialized_start=522
  _globals['_GETBOOTSTRAPNODESRESPONSE']._serialized_end=586
  _globals['_CLIENTMETASERVICE']._serialized_start=589
  _globals['_CLIENTMETASERVICE']._serialized_end=996
# @@protoc_insertion_point(module_scope)
