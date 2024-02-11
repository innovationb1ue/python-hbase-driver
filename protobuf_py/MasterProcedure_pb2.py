# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MasterProcedure.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HBase_pb2 as HBase__pb2
import RPC_pb2 as RPC__pb2
import Snapshot_pb2 as Snapshot__pb2
import Replication_pb2 as Replication__pb2
import RegionServerStatus_pb2 as RegionServerStatus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15MasterProcedure.proto\x12\x08hbase.pb\x1a\x0bHBase.proto\x1a\tRPC.proto\x1a\x0eSnapshot.proto\x1a\x11Replication.proto\x1a\x18RegionServerStatus.proto\"\x9c\x01\n\x14\x43reateTableStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12+\n\x0ctable_schema\x18\x02 \x02(\x0b\x32\x15.hbase.pb.TableSchema\x12)\n\x0bregion_info\x18\x03 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\"\x93\x02\n\x14ModifyTableStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\x36\n\x17unmodified_table_schema\x18\x02 \x01(\x0b\x32\x15.hbase.pb.TableSchema\x12\x34\n\x15modified_table_schema\x18\x03 \x02(\x0b\x32\x15.hbase.pb.TableSchema\x12&\n\x1e\x64\x65lete_column_family_in_modify\x18\x04 \x02(\x08\x12\x1f\n\x17should_check_descriptor\x18\x05 \x01(\x08\x12\x16\n\x0ereopen_regions\x18\x06 \x01(\x08\"\xe0\x01\n\x16TruncateTableStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\x17\n\x0fpreserve_splits\x18\x02 \x02(\x08\x12\'\n\ntable_name\x18\x03 \x01(\x0b\x32\x13.hbase.pb.TableName\x12+\n\x0ctable_schema\x18\x04 \x01(\x0b\x32\x15.hbase.pb.TableSchema\x12)\n\x0bregion_info\x18\x05 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\"\x98\x01\n\x14\x44\x65leteTableStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\'\n\ntable_name\x18\x02 \x02(\x0b\x32\x13.hbase.pb.TableName\x12)\n\x0bregion_info\x18\x03 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\"W\n\x18\x43reateNamespaceStateData\x12;\n\x14namespace_descriptor\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.NamespaceDescriptor\"\x9f\x01\n\x18ModifyNamespaceStateData\x12;\n\x14namespace_descriptor\x18\x01 \x02(\x0b\x32\x1d.hbase.pb.NamespaceDescriptor\x12\x46\n\x1funmodified_namespace_descriptor\x18\x02 \x01(\x0b\x32\x1d.hbase.pb.NamespaceDescriptor\"o\n\x18\x44\x65leteNamespaceStateData\x12\x16\n\x0enamespace_name\x18\x01 \x02(\t\x12;\n\x14namespace_descriptor\x18\x02 \x01(\x0b\x32\x1d.hbase.pb.NamespaceDescriptor\"\x91\x01\n\x14\x45nableTableStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\'\n\ntable_name\x18\x02 \x02(\x0b\x32\x13.hbase.pb.TableName\x12\"\n\x16skip_table_state_check\x18\x03 \x02(\x08\x42\x02\x18\x01\"\x8e\x01\n\x15\x44isableTableStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\'\n\ntable_name\x18\x02 \x02(\x0b\x32\x13.hbase.pb.TableName\x12\x1e\n\x16skip_table_state_check\x18\x03 \x02(\x08\"u\n\x1fRestoreParentToChildRegionsPair\x12\x1a\n\x12parent_region_name\x18\x01 \x02(\t\x12\x1a\n\x12\x63hild1_region_name\x18\x02 \x02(\t\x12\x1a\n\x12\x63hild2_region_name\x18\x03 \x02(\t\"\xcd\x02\n\x16\x43loneSnapshotStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12/\n\x08snapshot\x18\x02 \x02(\x0b\x32\x1d.hbase.pb.SnapshotDescription\x12+\n\x0ctable_schema\x18\x03 \x02(\x0b\x32\x15.hbase.pb.TableSchema\x12)\n\x0bregion_info\x18\x04 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12T\n!parent_to_child_regions_pair_list\x18\x05 \x03(\x0b\x32).hbase.pb.RestoreParentToChildRegionsPair\x12\x13\n\x0brestore_acl\x18\x06 \x01(\x08\x12\x11\n\tcustomSFT\x18\x07 \x01(\t\"\xba\x03\n\x18RestoreSnapshotStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12/\n\x08snapshot\x18\x02 \x02(\x0b\x32\x1d.hbase.pb.SnapshotDescription\x12\x34\n\x15modified_table_schema\x18\x03 \x02(\x0b\x32\x15.hbase.pb.TableSchema\x12\x35\n\x17region_info_for_restore\x18\x04 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x34\n\x16region_info_for_remove\x18\x05 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x31\n\x13region_info_for_add\x18\x06 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12T\n!parent_to_child_regions_pair_list\x18\x07 \x03(\x0b\x32).hbase.pb.RestoreParentToChildRegionsPair\x12\x13\n\x0brestore_acl\x18\x08 \x01(\x08\"\xb5\x01\n\x1f\x44ispatchMergingRegionsStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\'\n\ntable_name\x18\x02 \x02(\x0b\x32\x13.hbase.pb.TableName\x12)\n\x0bregion_info\x18\x03 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x10\n\x08\x66orcible\x18\x04 \x01(\x08\"\xac\x01\n\x19SplitTableRegionStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12\x30\n\x12parent_region_info\x18\x02 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\x12/\n\x11\x63hild_region_info\x18\x03 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\"\xc0\x01\n\x1aMergeTableRegionsStateData\x12,\n\tuser_info\x18\x01 \x02(\x0b\x32\x19.hbase.pb.UserInformation\x12)\n\x0bregion_info\x18\x02 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x30\n\x12merged_region_info\x18\x03 \x01(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x17\n\x08\x66orcible\x18\x04 \x01(\x08:\x05\x66\x61lse\"\xe1\x01\n\x14ServerCrashStateData\x12)\n\x0bserver_name\x18\x01 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12\x37\n\x19regions_on_crashed_server\x18\x03 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12.\n\x10regions_assigned\x18\x04 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x15\n\rcarrying_meta\x18\x05 \x01(\x08\x12\x1e\n\x10should_split_wal\x18\x06 \x01(\x08:\x04true\"\x7f\n\x14RecoverMetaStateData\x12\x30\n\x12\x66\x61iled_meta_server\x18\x01 \x01(\x0b\x32\x14.hbase.pb.ServerName\x12\x1e\n\x10should_split_wal\x18\x02 \x01(\x08:\x04true\x12\x15\n\nreplica_id\x18\x03 \x01(\x05:\x01\x30\"\xda\x01\n\x15\x41ssignRegionStateData\x12\x39\n\x10transition_state\x18\x01 \x02(\x0e\x32\x1f.hbase.pb.RegionTransitionState\x12)\n\x0bregion_info\x18\x02 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x1d\n\x0e\x66orce_new_plan\x18\x03 \x01(\x08:\x05\x66\x61lse\x12+\n\rtarget_server\x18\x04 \x01(\x0b\x32\x14.hbase.pb.ServerName\x12\x0f\n\x07\x61ttempt\x18\x05 \x01(\x05\"\xaf\x02\n\x17UnassignRegionStateData\x12\x39\n\x10transition_state\x18\x01 \x02(\x0e\x32\x1f.hbase.pb.RegionTransitionState\x12)\n\x0bregion_info\x18\x02 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\x12\x30\n\x12\x64\x65stination_server\x18\x03 \x01(\x0b\x32\x14.hbase.pb.ServerName\x12,\n\x0ehosting_server\x18\x05 \x01(\x0b\x32\x14.hbase.pb.ServerName\x12\x14\n\x05\x66orce\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\'\n\x18remove_after_unassigning\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x0f\n\x07\x61ttempt\x18\x07 \x01(\x05\"\x9f\x01\n\x13MoveRegionStateData\x12)\n\x0bregion_info\x18\x01 \x01(\x0b\x32\x14.hbase.pb.RegionInfo\x12+\n\rsource_server\x18\x02 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12\x30\n\x12\x64\x65stination_server\x18\x03 \x01(\x0b\x32\x14.hbase.pb.ServerName\">\n\x11GCRegionStateData\x12)\n\x0bregion_info\x18\x01 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\"\x9a\x01\n\x18GCMergedRegionsStateData\x12&\n\x08parent_a\x18\x01 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\x12&\n\x08parent_b\x18\x02 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\x12*\n\x0cmerged_child\x18\x03 \x02(\x0b\x32\x14.hbase.pb.RegionInfo:\x02\x18\x01\"u\n GCMultipleMergedRegionsStateData\x12%\n\x07parents\x18\x01 \x03(\x0b\x32\x14.hbase.pb.RegionInfo\x12*\n\x0cmerged_child\x18\x02 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\",\n\x19PeerModificationStateData\x12\x0f\n\x07peer_id\x18\x01 \x02(\t\"\x82\x01\n\x14RefreshPeerStateData\x12\x0f\n\x07peer_id\x18\x01 \x02(\t\x12,\n\x04type\x18\x02 \x02(\x0e\x32\x1e.hbase.pb.PeerModificationType\x12+\n\rtarget_server\x18\x03 \x02(\x0b\x32\x14.hbase.pb.ServerName\"\x82\x01\n\x14RefreshPeerParameter\x12\x0f\n\x07peer_id\x18\x01 \x02(\t\x12,\n\x04type\x18\x02 \x02(\x0e\x32\x1e.hbase.pb.PeerModificationType\x12+\n\rtarget_server\x18\x03 \x02(\x0b\x32\x14.hbase.pb.ServerName\")\n\x16PeerProcedureStateData\x12\x0f\n\x07peer_id\x18\x01 \x02(\t\"S\n\x10\x41\x64\x64PeerStateData\x12.\n\x0bpeer_config\x18\x01 \x02(\x0b\x32\x19.hbase.pb.ReplicationPeer\x12\x0f\n\x07\x65nabled\x18\x02 \x02(\x08\"\x90\x01\n\x19UpdatePeerConfigStateData\x12.\n\x0bpeer_config\x18\x01 \x02(\x0b\x32\x19.hbase.pb.ReplicationPeer\x12\x32\n\x0fold_peer_config\x18\x02 \x01(\x0b\x32\x19.hbase.pb.ReplicationPeer\x12\x0f\n\x07\x65nabled\x18\x03 \x02(\x08\"E\n\x13RemovePeerStateData\x12.\n\x0bpeer_config\x18\x01 \x01(\x0b\x32\x19.hbase.pb.ReplicationPeer\"\x15\n\x13\x45nablePeerStateData\"\x16\n\x14\x44isablePeerStateData\"\x86\x01\n\x1bReopenTableRegionsStateData\x12\'\n\ntable_name\x18\x01 \x02(\x0b\x32\x13.hbase.pb.TableName\x12(\n\x06region\x18\x02 \x03(\x0b\x32\x18.hbase.pb.RegionLocation\x12\x14\n\x0cregion_names\x18\x03 \x03(\x0c\"\x13\n\x11InitMetaStateData\"\x96\x01\n\x1eRegionStateTransitionStateData\x12,\n\x04type\x18\x01 \x02(\x0e\x32\x1e.hbase.pb.RegionTransitionType\x12.\n\x10\x61ssign_candidate\x18\x02 \x01(\x0b\x32\x14.hbase.pb.ServerName\x12\x16\n\x0e\x66orce_new_plan\x18\x03 \x02(\x08\"\x89\x02\n\"RegionRemoteProcedureBaseStateData\x12$\n\x06region\x18\x01 \x02(\x0b\x32\x14.hbase.pb.RegionInfo\x12+\n\rtarget_server\x18\x02 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12\x37\n\x05state\x18\x03 \x01(\x0e\x32(.hbase.pb.RegionRemoteProcedureBaseState\x12G\n\x0ftransition_code\x18\x04 \x01(\x0e\x32..hbase.pb.RegionStateTransition.TransitionCode\x12\x0e\n\x06seq_id\x18\x05 \x01(\x03\"\x1e\n\x1cOpenRegionProcedureStateData\"O\n\x1d\x43loseRegionProcedureStateData\x12.\n\x10\x61ssign_candidate\x18\x01 \x01(\x0b\x32\x14.hbase.pb.ServerName\":\n\x1aSwitchRpcThrottleStateData\x12\x1c\n\x14rpc_throttle_enabled\x18\x01 \x02(\x08\"m\n SwitchRpcThrottleRemoteStateData\x12+\n\rtarget_server\x18\x01 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12\x1c\n\x14rpc_throttle_enabled\x18\x02 \x02(\x08\"%\n\x11SplitWALParameter\x12\x10\n\x08wal_path\x18\x01 \x02(\t\"t\n\x0cSplitWALData\x12\x10\n\x08wal_path\x18\x01 \x02(\t\x12,\n\x0e\x63rashed_server\x18\x02 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12$\n\x06worker\x18\x03 \x01(\x0b\x32\x14.hbase.pb.ServerName\"z\n\x12SplitWALRemoteData\x12\x10\n\x08wal_path\x18\x01 \x02(\t\x12,\n\x0e\x63rashed_server\x18\x02 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12$\n\x06worker\x18\x03 \x02(\x0b\x32\x14.hbase.pb.ServerName\"O\n\x1f\x43laimReplicationQueuesStateData\x12,\n\x0e\x63rashed_server\x18\x01 \x02(\x0b\x32\x14.hbase.pb.ServerName\"\x90\x01\n$ClaimReplicationQueueRemoteStateData\x12,\n\x0e\x63rashed_server\x18\x01 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12\r\n\x05queue\x18\x02 \x02(\t\x12+\n\rtarget_server\x18\x03 \x02(\x0b\x32\x14.hbase.pb.ServerName\"c\n$ClaimReplicationQueueRemoteParameter\x12,\n\x0e\x63rashed_server\x18\x01 \x02(\x0b\x32\x14.hbase.pb.ServerName\x12\r\n\x05queue\x18\x02 \x02(\t\"\x7f\n\x1eModifyTableDescriptorStateData\x12\'\n\ntable_name\x18\x01 \x02(\x0b\x32\x13.hbase.pb.TableName\x12\x34\n\x15modified_table_schema\x18\x02 \x01(\x0b\x32\x15.hbase.pb.TableSchema\"[\n\x1fModifyStoreFileTrackerStateData\x12\'\n\ntable_name\x18\x01 \x02(\x0b\x32\x13.hbase.pb.TableName\x12\x0f\n\x07\x64st_sft\x18\x02 \x02(\t\"=\n+ModifyColumnFamilyStoreFileTrackerStateData\x12\x0e\n\x06\x66\x61mily\x18\x01 \x02(\x0c*\xd8\x01\n\x10\x43reateTableState\x12\x1e\n\x1a\x43REATE_TABLE_PRE_OPERATION\x10\x01\x12 \n\x1c\x43REATE_TABLE_WRITE_FS_LAYOUT\x10\x02\x12\x1c\n\x18\x43REATE_TABLE_ADD_TO_META\x10\x03\x12\x1f\n\x1b\x43REATE_TABLE_ASSIGN_REGIONS\x10\x04\x12\"\n\x1e\x43REATE_TABLE_UPDATE_DESC_CACHE\x10\x05\x12\x1f\n\x1b\x43REATE_TABLE_POST_OPERATION\x10\x06*\xd5\x02\n\x10ModifyTableState\x12\x18\n\x14MODIFY_TABLE_PREPARE\x10\x01\x12\x1e\n\x1aMODIFY_TABLE_PRE_OPERATION\x10\x02\x12(\n$MODIFY_TABLE_UPDATE_TABLE_DESCRIPTOR\x10\x03\x12&\n\"MODIFY_TABLE_REMOVE_REPLICA_COLUMN\x10\x04\x12!\n\x1dMODIFY_TABLE_DELETE_FS_LAYOUT\x10\x05\x12\x1f\n\x1bMODIFY_TABLE_POST_OPERATION\x10\x06\x12#\n\x1fMODIFY_TABLE_REOPEN_ALL_REGIONS\x10\x07\x12&\n\"MODIFY_TABLE_CLOSE_EXCESS_REPLICAS\x10\x08\x12$\n MODIFY_TABLE_ASSIGN_NEW_REPLICAS\x10\t*\x8a\x02\n\x12TruncateTableState\x12 \n\x1cTRUNCATE_TABLE_PRE_OPERATION\x10\x01\x12#\n\x1fTRUNCATE_TABLE_REMOVE_FROM_META\x10\x02\x12\"\n\x1eTRUNCATE_TABLE_CLEAR_FS_LAYOUT\x10\x03\x12#\n\x1fTRUNCATE_TABLE_CREATE_FS_LAYOUT\x10\x04\x12\x1e\n\x1aTRUNCATE_TABLE_ADD_TO_META\x10\x05\x12!\n\x1dTRUNCATE_TABLE_ASSIGN_REGIONS\x10\x06\x12!\n\x1dTRUNCATE_TABLE_POST_OPERATION\x10\x07*\xdf\x01\n\x10\x44\x65leteTableState\x12\x1e\n\x1a\x44\x45LETE_TABLE_PRE_OPERATION\x10\x01\x12!\n\x1d\x44\x45LETE_TABLE_REMOVE_FROM_META\x10\x02\x12 \n\x1c\x44\x45LETE_TABLE_CLEAR_FS_LAYOUT\x10\x03\x12\"\n\x1e\x44\x45LETE_TABLE_UPDATE_DESC_CACHE\x10\x04\x12!\n\x1d\x44\x45LETE_TABLE_UNASSIGN_REGIONS\x10\x05\x12\x1f\n\x1b\x44\x45LETE_TABLE_POST_OPERATION\x10\x06*\xd0\x01\n\x14\x43reateNamespaceState\x12\x1c\n\x18\x43REATE_NAMESPACE_PREPARE\x10\x01\x12%\n!CREATE_NAMESPACE_CREATE_DIRECTORY\x10\x02\x12)\n%CREATE_NAMESPACE_INSERT_INTO_NS_TABLE\x10\x03\x12\x1e\n\x1a\x43REATE_NAMESPACE_UPDATE_ZK\x10\x04\x12(\n$CREATE_NAMESPACE_SET_NAMESPACE_QUOTA\x10\x05*z\n\x14ModifyNamespaceState\x12\x1c\n\x18MODIFY_NAMESPACE_PREPARE\x10\x01\x12$\n MODIFY_NAMESPACE_UPDATE_NS_TABLE\x10\x02\x12\x1e\n\x1aMODIFY_NAMESPACE_UPDATE_ZK\x10\x03*\xda\x01\n\x14\x44\x65leteNamespaceState\x12\x1c\n\x18\x44\x45LETE_NAMESPACE_PREPARE\x10\x01\x12)\n%DELETE_NAMESPACE_DELETE_FROM_NS_TABLE\x10\x02\x12#\n\x1f\x44\x45LETE_NAMESPACE_REMOVE_FROM_ZK\x10\x03\x12\'\n#DELETE_NAMESPACE_DELETE_DIRECTORIES\x10\x04\x12+\n\'DELETE_NAMESPACE_REMOVE_NAMESPACE_QUOTA\x10\x05*\xe8\x01\n\x10\x45nableTableState\x12\x18\n\x14\x45NABLE_TABLE_PREPARE\x10\x01\x12\x1e\n\x1a\x45NABLE_TABLE_PRE_OPERATION\x10\x02\x12)\n%ENABLE_TABLE_SET_ENABLING_TABLE_STATE\x10\x03\x12$\n ENABLE_TABLE_MARK_REGIONS_ONLINE\x10\x04\x12(\n$ENABLE_TABLE_SET_ENABLED_TABLE_STATE\x10\x05\x12\x1f\n\x1b\x45NABLE_TABLE_POST_OPERATION\x10\x06*\x9d\x02\n\x11\x44isableTableState\x12\x19\n\x15\x44ISABLE_TABLE_PREPARE\x10\x01\x12\x1f\n\x1b\x44ISABLE_TABLE_PRE_OPERATION\x10\x02\x12+\n\'DISABLE_TABLE_SET_DISABLING_TABLE_STATE\x10\x03\x12&\n\"DISABLE_TABLE_MARK_REGIONS_OFFLINE\x10\x04\x12*\n&DISABLE_TABLE_SET_DISABLED_TABLE_STATE\x10\x05\x12 \n\x1c\x44ISABLE_TABLE_POST_OPERATION\x10\x06\x12)\n%DISABLE_TABLE_ADD_REPLICATION_BARRIER\x10\x07*\x86\x02\n\x12\x43loneSnapshotState\x12 \n\x1c\x43LONE_SNAPSHOT_PRE_OPERATION\x10\x01\x12\"\n\x1e\x43LONE_SNAPSHOT_WRITE_FS_LAYOUT\x10\x02\x12\x1e\n\x1a\x43LONE_SNAPSHOT_ADD_TO_META\x10\x03\x12!\n\x1d\x43LONE_SNAPSHOT_ASSIGN_REGIONS\x10\x04\x12$\n CLONE_SNAPSHOT_UPDATE_DESC_CACHE\x10\x05\x12!\n\x1d\x43LONE_SNAPSHOT_POST_OPERATION\x10\x06\x12\x1e\n\x1a\x43LONE_SNAPHOST_RESTORE_ACL\x10\x07*\xd2\x01\n\x14RestoreSnapshotState\x12\"\n\x1eRESTORE_SNAPSHOT_PRE_OPERATION\x10\x01\x12,\n(RESTORE_SNAPSHOT_UPDATE_TABLE_DESCRIPTOR\x10\x02\x12$\n RESTORE_SNAPSHOT_WRITE_FS_LAYOUT\x10\x03\x12 \n\x1cRESTORE_SNAPSHOT_UPDATE_META\x10\x04\x12 \n\x1cRESTORE_SNAPSHOT_RESTORE_ACL\x10\x05*\xfe\x01\n\x1b\x44ispatchMergingRegionsState\x12$\n DISPATCH_MERGING_REGIONS_PREPARE\x10\x01\x12*\n&DISPATCH_MERGING_REGIONS_PRE_OPERATION\x10\x02\x12\x33\n/DISPATCH_MERGING_REGIONS_MOVE_REGION_TO_SAME_RS\x10\x03\x12+\n\'DISPATCH_MERGING_REGIONS_DO_MERGE_IN_RS\x10\x04\x12+\n\'DISPATCH_MERGING_REGIONS_POST_OPERATION\x10\x05*\xf3\x03\n\x15SplitTableRegionState\x12\x1e\n\x1aSPLIT_TABLE_REGION_PREPARE\x10\x01\x12$\n SPLIT_TABLE_REGION_PRE_OPERATION\x10\x02\x12*\n&SPLIT_TABLE_REGION_CLOSE_PARENT_REGION\x10\x03\x12.\n*SPLIT_TABLE_REGION_CREATE_DAUGHTER_REGIONS\x10\x04\x12\x31\n-SPLIT_TABLE_REGION_WRITE_MAX_SEQUENCE_ID_FILE\x10\x05\x12\x30\n,SPLIT_TABLE_REGION_PRE_OPERATION_BEFORE_META\x10\x06\x12\"\n\x1eSPLIT_TABLE_REGION_UPDATE_META\x10\x07\x12/\n+SPLIT_TABLE_REGION_PRE_OPERATION_AFTER_META\x10\x08\x12)\n%SPLIT_TABLE_REGION_OPEN_CHILD_REGIONS\x10\t\x12%\n!SPLIT_TABLE_REGION_POST_OPERATION\x10\n\x12,\n(SPLIT_TABLE_REGIONS_CHECK_CLOSED_REGIONS\x10\x0b*\xa6\x04\n\x16MergeTableRegionsState\x12\x1f\n\x1bMERGE_TABLE_REGIONS_PREPARE\x10\x01\x12%\n!MERGE_TABLE_REGIONS_PRE_OPERATION\x10\x02\x12+\n\'MERGE_TABLE_REGIONS_PRE_MERGE_OPERATION\x10\x03\x12%\n!MERGE_TABLE_REGIONS_CLOSE_REGIONS\x10\x04\x12,\n(MERGE_TABLE_REGIONS_CREATE_MERGED_REGION\x10\x05\x12\x32\n.MERGE_TABLE_REGIONS_WRITE_MAX_SEQUENCE_ID_FILE\x10\x06\x12\x32\n.MERGE_TABLE_REGIONS_PRE_MERGE_COMMIT_OPERATION\x10\x07\x12#\n\x1fMERGE_TABLE_REGIONS_UPDATE_META\x10\x08\x12\x33\n/MERGE_TABLE_REGIONS_POST_MERGE_COMMIT_OPERATION\x10\t\x12*\n&MERGE_TABLE_REGIONS_OPEN_MERGED_REGION\x10\n\x12&\n\"MERGE_TABLE_REGIONS_POST_OPERATION\x10\x0b\x12,\n(MERGE_TABLE_REGIONS_CHECK_CLOSED_REGIONS\x10\x0c*\xe1\x03\n\x10ServerCrashState\x12\x16\n\x12SERVER_CRASH_START\x10\x01\x12!\n\x19SERVER_CRASH_PROCESS_META\x10\x02\x1a\x02\x08\x01\x12\x1c\n\x18SERVER_CRASH_GET_REGIONS\x10\x03\x12\"\n\x1aSERVER_CRASH_NO_SPLIT_LOGS\x10\x04\x1a\x02\x08\x01\x12\x1b\n\x17SERVER_CRASH_SPLIT_LOGS\x10\x05\x12\x17\n\x13SERVER_CRASH_ASSIGN\x10\x08\x12\x1f\n\x1bSERVER_CRASH_WAIT_ON_ASSIGN\x10\t\x12 \n\x1cSERVER_CRASH_SPLIT_META_LOGS\x10\n\x12\x1c\n\x18SERVER_CRASH_ASSIGN_META\x10\x0b\x12+\n\'SERVER_CRASH_DELETE_SPLIT_META_WALS_DIR\x10\x0c\x12&\n\"SERVER_CRASH_DELETE_SPLIT_WALS_DIR\x10\r\x12)\n%SERVER_CRASH_CLAIM_REPLICATION_QUEUES\x10\x0e\x12 \n\x18SERVER_CRASH_HANDLE_RIT2\x10\x14\x1a\x02\x08\x01\x12\x17\n\x13SERVER_CRASH_FINISH\x10\x64*j\n\x10RecoverMetaState\x12\x18\n\x14RECOVER_META_PREPARE\x10\x00\x12\x1b\n\x17RECOVER_META_SPLIT_LOGS\x10\x01\x12\x1f\n\x1bRECOVER_META_ASSIGN_REGIONS\x10\x02*r\n\x15RegionTransitionState\x12\x1b\n\x17REGION_TRANSITION_QUEUE\x10\x01\x12\x1e\n\x1aREGION_TRANSITION_DISPATCH\x10\x02\x12\x1c\n\x18REGION_TRANSITION_FINISH\x10\x03*\\\n\x0fMoveRegionState\x12\x17\n\x13MOVE_REGION_PREPARE\x10\x00\x12\x18\n\x14MOVE_REGION_UNASSIGN\x10\x01\x12\x16\n\x12MOVE_REGION_ASSIGN\x10\x02*[\n\rGCRegionState\x12\x15\n\x11GC_REGION_PREPARE\x10\x01\x12\x15\n\x11GC_REGION_ARCHIVE\x10\x02\x12\x1c\n\x18GC_REGION_PURGE_METADATA\x10\x03*o\n\x14GCMergedRegionsState\x12\x1d\n\x19GC_MERGED_REGIONS_PREPARE\x10\x01\x12\x1b\n\x17GC_MERGED_REGIONS_PURGE\x10\x02\x12\x1b\n\x17GC_REGION_EDIT_METADATA\x10\x03*\x9c\x02\n\x15PeerModificationState\x12\x19\n\x15PRE_PEER_MODIFICATION\x10\x01\x12\x17\n\x13UPDATE_PEER_STORAGE\x10\x02\x12\x16\n\x12REFRESH_PEER_ON_RS\x10\x03\x12\x1e\n\x1aSERIAL_PEER_REOPEN_REGIONS\x10\x04\x12)\n%SERIAL_PEER_UPDATE_LAST_PUSHED_SEQ_ID\x10\x05\x12 \n\x1cSERIAL_PEER_SET_PEER_ENABLED\x10\x06\x12.\n*SERIAL_PEER_ENABLE_PEER_REFRESH_PEER_ON_RS\x10\x07\x12\x1a\n\x16POST_PEER_MODIFICATION\x10\x08*p\n\x14PeerModificationType\x12\x0c\n\x08\x41\x44\x44_PEER\x10\x01\x12\x0f\n\x0bREMOVE_PEER\x10\x02\x12\x0f\n\x0b\x45NABLE_PEER\x10\x03\x12\x10\n\x0c\x44ISABLE_PEER\x10\x04\x12\x16\n\x12UPDATE_PEER_CONFIG\x10\x05*\x93\x01\n\x17ReopenTableRegionsState\x12$\n REOPEN_TABLE_REGIONS_GET_REGIONS\x10\x01\x12\'\n#REOPEN_TABLE_REGIONS_REOPEN_REGIONS\x10\x02\x12)\n%REOPEN_TABLE_REGIONS_CONFIRM_REOPENED\x10\x03*I\n\rInitMetaState\x12\x1d\n\x19INIT_META_WRITE_FS_LAYOUT\x10\x01\x12\x19\n\x15INIT_META_ASSIGN_META\x10\x02*\xeb\x01\n\x1aRegionStateTransitionState\x12\x30\n,REGION_STATE_TRANSITION_GET_ASSIGN_CANDIDATE\x10\x01\x12 \n\x1cREGION_STATE_TRANSITION_OPEN\x10\x02\x12*\n&REGION_STATE_TRANSITION_CONFIRM_OPENED\x10\x03\x12!\n\x1dREGION_STATE_TRANSITION_CLOSE\x10\x04\x12*\n&REGION_STATE_TRANSITION_CONFIRM_CLOSED\x10\x05*F\n\x14RegionTransitionType\x12\n\n\x06\x41SSIGN\x10\x01\x12\x0c\n\x08UNASSIGN\x10\x02\x12\x08\n\x04MOVE\x10\x03\x12\n\n\x06REOPEN\x10\x04*\xc7\x01\n\x1eRegionRemoteProcedureBaseState\x12$\n REGION_REMOTE_PROCEDURE_DISPATCH\x10\x01\x12*\n&REGION_REMOTE_PROCEDURE_REPORT_SUCCEED\x10\x02\x12)\n%REGION_REMOTE_PROCEDURE_DISPATCH_FAIL\x10\x03\x12(\n$REGION_REMOTE_PROCEDURE_SERVER_CRASH\x10\x04*}\n\x16SwitchRpcThrottleState\x12&\n\"UPDATE_SWITCH_RPC_THROTTLE_STORAGE\x10\x01\x12\x1d\n\x19SWITCH_RPC_THROTTLE_ON_RS\x10\x02\x12\x1c\n\x18POST_SWITCH_RPC_THROTTLE\x10\x03*c\n\rSplitWALState\x12\x1c\n\x18\x41\x43QUIRE_SPLIT_WAL_WORKER\x10\x01\x12\x1a\n\x16\x44ISPATCH_WAL_TO_WORKER\x10\x02\x12\x18\n\x14RELEASE_SPLIT_WORKER\x10\x03*i\n\x1b\x43laimReplicationQueuesState\x12%\n!CLAIM_REPLICATION_QUEUES_DISPATCH\x10\x01\x12#\n\x1f\x43LAIM_REPLICATION_QUEUES_FINISH\x10\x02*e\n\x1aModifyTableDescriptorState\x12#\n\x1fMODIFY_TABLE_DESCRIPTOR_PREPARE\x10\x01\x12\"\n\x1eMODIFY_TABLE_DESCRIPTOR_UPDATE\x10\x02*\xb5\x01\n\x1bModifyStoreFileTrackerState\x12\x37\n3MODIFY_STORE_FILE_TRACKER_FINISH_PREVIOUS_MIGRATION\x10\x01\x12-\n)MODIFY_STORE_FILE_TRACKER_START_MIGRATION\x10\x02\x12.\n*MODIFY_STORE_FILE_TRACKER_FINISH_MIGRATION\x10\x03\x42R\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\x15MasterProcedureProtosH\x01\x88\x01\x01\xa0\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MasterProcedure_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1org.apache.hadoop.hbase.shaded.protobuf.generatedB\025MasterProcedureProtosH\001\210\001\001\240\001\001'
  _globals['_SERVERCRASHSTATE'].values_by_name["SERVER_CRASH_PROCESS_META"]._options = None
  _globals['_SERVERCRASHSTATE'].values_by_name["SERVER_CRASH_PROCESS_META"]._serialized_options = b'\010\001'
  _globals['_SERVERCRASHSTATE'].values_by_name["SERVER_CRASH_NO_SPLIT_LOGS"]._options = None
  _globals['_SERVERCRASHSTATE'].values_by_name["SERVER_CRASH_NO_SPLIT_LOGS"]._serialized_options = b'\010\001'
  _globals['_SERVERCRASHSTATE'].values_by_name["SERVER_CRASH_HANDLE_RIT2"]._options = None
  _globals['_SERVERCRASHSTATE'].values_by_name["SERVER_CRASH_HANDLE_RIT2"]._serialized_options = b'\010\001'
  _globals['_ENABLETABLESTATEDATA'].fields_by_name['skip_table_state_check']._options = None
  _globals['_ENABLETABLESTATEDATA'].fields_by_name['skip_table_state_check']._serialized_options = b'\030\001'
  _globals['_GCMERGEDREGIONSSTATEDATA']._options = None
  _globals['_GCMERGEDREGIONSSTATEDATA']._serialized_options = b'\030\001'
  _globals['_CREATETABLESTATE']._serialized_start=6900
  _globals['_CREATETABLESTATE']._serialized_end=7116
  _globals['_MODIFYTABLESTATE']._serialized_start=7119
  _globals['_MODIFYTABLESTATE']._serialized_end=7460
  _globals['_TRUNCATETABLESTATE']._serialized_start=7463
  _globals['_TRUNCATETABLESTATE']._serialized_end=7729
  _globals['_DELETETABLESTATE']._serialized_start=7732
  _globals['_DELETETABLESTATE']._serialized_end=7955
  _globals['_CREATENAMESPACESTATE']._serialized_start=7958
  _globals['_CREATENAMESPACESTATE']._serialized_end=8166
  _globals['_MODIFYNAMESPACESTATE']._serialized_start=8168
  _globals['_MODIFYNAMESPACESTATE']._serialized_end=8290
  _globals['_DELETENAMESPACESTATE']._serialized_start=8293
  _globals['_DELETENAMESPACESTATE']._serialized_end=8511
  _globals['_ENABLETABLESTATE']._serialized_start=8514
  _globals['_ENABLETABLESTATE']._serialized_end=8746
  _globals['_DISABLETABLESTATE']._serialized_start=8749
  _globals['_DISABLETABLESTATE']._serialized_end=9034
  _globals['_CLONESNAPSHOTSTATE']._serialized_start=9037
  _globals['_CLONESNAPSHOTSTATE']._serialized_end=9299
  _globals['_RESTORESNAPSHOTSTATE']._serialized_start=9302
  _globals['_RESTORESNAPSHOTSTATE']._serialized_end=9512
  _globals['_DISPATCHMERGINGREGIONSSTATE']._serialized_start=9515
  _globals['_DISPATCHMERGINGREGIONSSTATE']._serialized_end=9769
  _globals['_SPLITTABLEREGIONSTATE']._serialized_start=9772
  _globals['_SPLITTABLEREGIONSTATE']._serialized_end=10271
  _globals['_MERGETABLEREGIONSSTATE']._serialized_start=10274
  _globals['_MERGETABLEREGIONSSTATE']._serialized_end=10824
  _globals['_SERVERCRASHSTATE']._serialized_start=10827
  _globals['_SERVERCRASHSTATE']._serialized_end=11308
  _globals['_RECOVERMETASTATE']._serialized_start=11310
  _globals['_RECOVERMETASTATE']._serialized_end=11416
  _globals['_REGIONTRANSITIONSTATE']._serialized_start=11418
  _globals['_REGIONTRANSITIONSTATE']._serialized_end=11532
  _globals['_MOVEREGIONSTATE']._serialized_start=11534
  _globals['_MOVEREGIONSTATE']._serialized_end=11626
  _globals['_GCREGIONSTATE']._serialized_start=11628
  _globals['_GCREGIONSTATE']._serialized_end=11719
  _globals['_GCMERGEDREGIONSSTATE']._serialized_start=11721
  _globals['_GCMERGEDREGIONSSTATE']._serialized_end=11832
  _globals['_PEERMODIFICATIONSTATE']._serialized_start=11835
  _globals['_PEERMODIFICATIONSTATE']._serialized_end=12119
  _globals['_PEERMODIFICATIONTYPE']._serialized_start=12121
  _globals['_PEERMODIFICATIONTYPE']._serialized_end=12233
  _globals['_REOPENTABLEREGIONSSTATE']._serialized_start=12236
  _globals['_REOPENTABLEREGIONSSTATE']._serialized_end=12383
  _globals['_INITMETASTATE']._serialized_start=12385
  _globals['_INITMETASTATE']._serialized_end=12458
  _globals['_REGIONSTATETRANSITIONSTATE']._serialized_start=12461
  _globals['_REGIONSTATETRANSITIONSTATE']._serialized_end=12696
  _globals['_REGIONTRANSITIONTYPE']._serialized_start=12698
  _globals['_REGIONTRANSITIONTYPE']._serialized_end=12768
  _globals['_REGIONREMOTEPROCEDUREBASESTATE']._serialized_start=12771
  _globals['_REGIONREMOTEPROCEDUREBASESTATE']._serialized_end=12970
  _globals['_SWITCHRPCTHROTTLESTATE']._serialized_start=12972
  _globals['_SWITCHRPCTHROTTLESTATE']._serialized_end=13097
  _globals['_SPLITWALSTATE']._serialized_start=13099
  _globals['_SPLITWALSTATE']._serialized_end=13198
  _globals['_CLAIMREPLICATIONQUEUESSTATE']._serialized_start=13200
  _globals['_CLAIMREPLICATIONQUEUESSTATE']._serialized_end=13305
  _globals['_MODIFYTABLEDESCRIPTORSTATE']._serialized_start=13307
  _globals['_MODIFYTABLEDESCRIPTORSTATE']._serialized_end=13408
  _globals['_MODIFYSTOREFILETRACKERSTATE']._serialized_start=13411
  _globals['_MODIFYSTOREFILETRACKERSTATE']._serialized_end=13592
  _globals['_CREATETABLESTATEDATA']._serialized_start=121
  _globals['_CREATETABLESTATEDATA']._serialized_end=277
  _globals['_MODIFYTABLESTATEDATA']._serialized_start=280
  _globals['_MODIFYTABLESTATEDATA']._serialized_end=555
  _globals['_TRUNCATETABLESTATEDATA']._serialized_start=558
  _globals['_TRUNCATETABLESTATEDATA']._serialized_end=782
  _globals['_DELETETABLESTATEDATA']._serialized_start=785
  _globals['_DELETETABLESTATEDATA']._serialized_end=937
  _globals['_CREATENAMESPACESTATEDATA']._serialized_start=939
  _globals['_CREATENAMESPACESTATEDATA']._serialized_end=1026
  _globals['_MODIFYNAMESPACESTATEDATA']._serialized_start=1029
  _globals['_MODIFYNAMESPACESTATEDATA']._serialized_end=1188
  _globals['_DELETENAMESPACESTATEDATA']._serialized_start=1190
  _globals['_DELETENAMESPACESTATEDATA']._serialized_end=1301
  _globals['_ENABLETABLESTATEDATA']._serialized_start=1304
  _globals['_ENABLETABLESTATEDATA']._serialized_end=1449
  _globals['_DISABLETABLESTATEDATA']._serialized_start=1452
  _globals['_DISABLETABLESTATEDATA']._serialized_end=1594
  _globals['_RESTOREPARENTTOCHILDREGIONSPAIR']._serialized_start=1596
  _globals['_RESTOREPARENTTOCHILDREGIONSPAIR']._serialized_end=1713
  _globals['_CLONESNAPSHOTSTATEDATA']._serialized_start=1716
  _globals['_CLONESNAPSHOTSTATEDATA']._serialized_end=2049
  _globals['_RESTORESNAPSHOTSTATEDATA']._serialized_start=2052
  _globals['_RESTORESNAPSHOTSTATEDATA']._serialized_end=2494
  _globals['_DISPATCHMERGINGREGIONSSTATEDATA']._serialized_start=2497
  _globals['_DISPATCHMERGINGREGIONSSTATEDATA']._serialized_end=2678
  _globals['_SPLITTABLEREGIONSTATEDATA']._serialized_start=2681
  _globals['_SPLITTABLEREGIONSTATEDATA']._serialized_end=2853
  _globals['_MERGETABLEREGIONSSTATEDATA']._serialized_start=2856
  _globals['_MERGETABLEREGIONSSTATEDATA']._serialized_end=3048
  _globals['_SERVERCRASHSTATEDATA']._serialized_start=3051
  _globals['_SERVERCRASHSTATEDATA']._serialized_end=3276
  _globals['_RECOVERMETASTATEDATA']._serialized_start=3278
  _globals['_RECOVERMETASTATEDATA']._serialized_end=3405
  _globals['_ASSIGNREGIONSTATEDATA']._serialized_start=3408
  _globals['_ASSIGNREGIONSTATEDATA']._serialized_end=3626
  _globals['_UNASSIGNREGIONSTATEDATA']._serialized_start=3629
  _globals['_UNASSIGNREGIONSTATEDATA']._serialized_end=3932
  _globals['_MOVEREGIONSTATEDATA']._serialized_start=3935
  _globals['_MOVEREGIONSTATEDATA']._serialized_end=4094
  _globals['_GCREGIONSTATEDATA']._serialized_start=4096
  _globals['_GCREGIONSTATEDATA']._serialized_end=4158
  _globals['_GCMERGEDREGIONSSTATEDATA']._serialized_start=4161
  _globals['_GCMERGEDREGIONSSTATEDATA']._serialized_end=4315
  _globals['_GCMULTIPLEMERGEDREGIONSSTATEDATA']._serialized_start=4317
  _globals['_GCMULTIPLEMERGEDREGIONSSTATEDATA']._serialized_end=4434
  _globals['_PEERMODIFICATIONSTATEDATA']._serialized_start=4436
  _globals['_PEERMODIFICATIONSTATEDATA']._serialized_end=4480
  _globals['_REFRESHPEERSTATEDATA']._serialized_start=4483
  _globals['_REFRESHPEERSTATEDATA']._serialized_end=4613
  _globals['_REFRESHPEERPARAMETER']._serialized_start=4616
  _globals['_REFRESHPEERPARAMETER']._serialized_end=4746
  _globals['_PEERPROCEDURESTATEDATA']._serialized_start=4748
  _globals['_PEERPROCEDURESTATEDATA']._serialized_end=4789
  _globals['_ADDPEERSTATEDATA']._serialized_start=4791
  _globals['_ADDPEERSTATEDATA']._serialized_end=4874
  _globals['_UPDATEPEERCONFIGSTATEDATA']._serialized_start=4877
  _globals['_UPDATEPEERCONFIGSTATEDATA']._serialized_end=5021
  _globals['_REMOVEPEERSTATEDATA']._serialized_start=5023
  _globals['_REMOVEPEERSTATEDATA']._serialized_end=5092
  _globals['_ENABLEPEERSTATEDATA']._serialized_start=5094
  _globals['_ENABLEPEERSTATEDATA']._serialized_end=5115
  _globals['_DISABLEPEERSTATEDATA']._serialized_start=5117
  _globals['_DISABLEPEERSTATEDATA']._serialized_end=5139
  _globals['_REOPENTABLEREGIONSSTATEDATA']._serialized_start=5142
  _globals['_REOPENTABLEREGIONSSTATEDATA']._serialized_end=5276
  _globals['_INITMETASTATEDATA']._serialized_start=5278
  _globals['_INITMETASTATEDATA']._serialized_end=5297
  _globals['_REGIONSTATETRANSITIONSTATEDATA']._serialized_start=5300
  _globals['_REGIONSTATETRANSITIONSTATEDATA']._serialized_end=5450
  _globals['_REGIONREMOTEPROCEDUREBASESTATEDATA']._serialized_start=5453
  _globals['_REGIONREMOTEPROCEDUREBASESTATEDATA']._serialized_end=5718
  _globals['_OPENREGIONPROCEDURESTATEDATA']._serialized_start=5720
  _globals['_OPENREGIONPROCEDURESTATEDATA']._serialized_end=5750
  _globals['_CLOSEREGIONPROCEDURESTATEDATA']._serialized_start=5752
  _globals['_CLOSEREGIONPROCEDURESTATEDATA']._serialized_end=5831
  _globals['_SWITCHRPCTHROTTLESTATEDATA']._serialized_start=5833
  _globals['_SWITCHRPCTHROTTLESTATEDATA']._serialized_end=5891
  _globals['_SWITCHRPCTHROTTLEREMOTESTATEDATA']._serialized_start=5893
  _globals['_SWITCHRPCTHROTTLEREMOTESTATEDATA']._serialized_end=6002
  _globals['_SPLITWALPARAMETER']._serialized_start=6004
  _globals['_SPLITWALPARAMETER']._serialized_end=6041
  _globals['_SPLITWALDATA']._serialized_start=6043
  _globals['_SPLITWALDATA']._serialized_end=6159
  _globals['_SPLITWALREMOTEDATA']._serialized_start=6161
  _globals['_SPLITWALREMOTEDATA']._serialized_end=6283
  _globals['_CLAIMREPLICATIONQUEUESSTATEDATA']._serialized_start=6285
  _globals['_CLAIMREPLICATIONQUEUESSTATEDATA']._serialized_end=6364
  _globals['_CLAIMREPLICATIONQUEUEREMOTESTATEDATA']._serialized_start=6367
  _globals['_CLAIMREPLICATIONQUEUEREMOTESTATEDATA']._serialized_end=6511
  _globals['_CLAIMREPLICATIONQUEUEREMOTEPARAMETER']._serialized_start=6513
  _globals['_CLAIMREPLICATIONQUEUEREMOTEPARAMETER']._serialized_end=6612
  _globals['_MODIFYTABLEDESCRIPTORSTATEDATA']._serialized_start=6614
  _globals['_MODIFYTABLEDESCRIPTORSTATEDATA']._serialized_end=6741
  _globals['_MODIFYSTOREFILETRACKERSTATEDATA']._serialized_start=6743
  _globals['_MODIFYSTOREFILETRACKERSTATEDATA']._serialized_end=6834
  _globals['_MODIFYCOLUMNFAMILYSTOREFILETRACKERSTATEDATA']._serialized_start=6836
  _globals['_MODIFYCOLUMNFAMILYSTOREFILETRACKERSTATEDATA']._serialized_end=6897
# @@protoc_insertion_point(module_scope)
