# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: namespaces.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10namespaces.proto\x12\x12pomerium.dashboard\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf4\x01\n\tNamespace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tparent_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0broute_count\x18\x07 \x01(\x03\x12\x14\n\x0cpolicy_count\x18\x08 \x01(\x03\"$\n\x16\x44\x65leteNamespaceRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x19\n\x17\x44\x65leteNamespaceResponse\"!\n\x13GetNamespaceRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x14GetNamespaceResponse\x12\x30\n\tnamespace\x18\x01 \x01(\x0b\x32\x1d.pomerium.dashboard.Namespace\"\x17\n\x15ListNamespacesRequest\"K\n\x16ListNamespacesResponse\x12\x31\n\nnamespaces\x18\x01 \x03(\x0b\x32\x1d.pomerium.dashboard.Namespace\"G\n\x13SetNamespaceRequest\x12\x30\n\tnamespace\x18\x01 \x01(\x0b\x32\x1d.pomerium.dashboard.Namespace\"H\n\x14SetNamespaceResponse\x12\x30\n\tnamespace\x18\x01 \x01(\x0b\x32\x1d.pomerium.dashboard.Namespace\"\xe8\x01\n\x13NamespacePermission\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t\x12\x16\n\x0enamespace_name\x18\x08 \x01(\t\x12\x14\n\x0csubject_type\x18\x05 \x01(\t\x12\x12\n\nsubject_id\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\"\x91\x01\n\x18NamespacePermissionGroup\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x13\n\x0bgroup_email\x18\x03 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t\x12\x16\n\x0enamespace_name\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\"\xa0\x01\n\x17NamespacePermissionUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12\x11\n\tgroup_ids\x18\x04 \x03(\t\x12\x14\n\x0cnamespace_id\x18\x05 \x01(\t\x12\x16\n\x0enamespace_name\x18\x07 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\".\n DeleteNamespacePermissionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"#\n!DeleteNamespacePermissionResponse\"+\n\x1dGetNamespacePermissionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"g\n\x1eGetNamespacePermissionResponse\x12\x45\n\x14namespace_permission\x18\x01 \x01(\x0b\x32\'.pomerium.dashboard.NamespacePermission\"!\n\x1fListNamespacePermissionsRequest\"j\n ListNamespacePermissionsResponse\x12\x46\n\x15namespace_permissions\x18\x01 \x03(\x0b\x32\'.pomerium.dashboard.NamespacePermission\"<\n$ListNamespacePermissionGroupsRequest\x12\x14\n\x0cnamespace_id\x18\x01 \x01(\t\"e\n%ListNamespacePermissionGroupsResponse\x12<\n\x06groups\x18\x01 \x03(\x0b\x32,.pomerium.dashboard.NamespacePermissionGroup\";\n#ListNamespacePermissionUsersRequest\x12\x14\n\x0cnamespace_id\x18\x01 \x01(\t\"b\n$ListNamespacePermissionUsersResponse\x12:\n\x05users\x18\x01 \x03(\x0b\x32+.pomerium.dashboard.NamespacePermissionUser\"f\n\x1dSetNamespacePermissionRequest\x12\x45\n\x14namespace_permission\x18\x01 \x01(\x0b\x32\'.pomerium.dashboard.NamespacePermission\"g\n\x1eSetNamespacePermissionResponse\x12\x45\n\x14namespace_permission\x18\x01 \x01(\x0b\x32\'.pomerium.dashboard.NamespacePermission2\xad\x03\n\x10NamespaceService\x12j\n\x0f\x44\x65leteNamespace\x12*.pomerium.dashboard.DeleteNamespaceRequest\x1a+.pomerium.dashboard.DeleteNamespaceResponse\x12\x61\n\x0cGetNamespace\x12\'.pomerium.dashboard.GetNamespaceRequest\x1a(.pomerium.dashboard.GetNamespaceResponse\x12g\n\x0eListNamespaces\x12).pomerium.dashboard.ListNamespacesRequest\x1a*.pomerium.dashboard.ListNamespacesResponse\x12\x61\n\x0cSetNamespace\x12\'.pomerium.dashboard.SetNamespaceRequest\x1a(.pomerium.dashboard.SetNamespaceResponse2\xdc\x06\n\x1aNamespacePermissionService\x12\x88\x01\n\x19\x44\x65leteNamespacePermission\x12\x34.pomerium.dashboard.DeleteNamespacePermissionRequest\x1a\x35.pomerium.dashboard.DeleteNamespacePermissionResponse\x12\x7f\n\x16GetNamespacePermission\x12\x31.pomerium.dashboard.GetNamespacePermissionRequest\x1a\x32.pomerium.dashboard.GetNamespacePermissionResponse\x12\x85\x01\n\x18ListNamespacePermissions\x12\x33.pomerium.dashboard.ListNamespacePermissionsRequest\x1a\x34.pomerium.dashboard.ListNamespacePermissionsResponse\x12\x94\x01\n\x1dListNamespacePermissionGroups\x12\x38.pomerium.dashboard.ListNamespacePermissionGroupsRequest\x1a\x39.pomerium.dashboard.ListNamespacePermissionGroupsResponse\x12\x91\x01\n\x1cListNamespacePermissionUsers\x12\x37.pomerium.dashboard.ListNamespacePermissionUsersRequest\x1a\x38.pomerium.dashboard.ListNamespacePermissionUsersResponse\x12\x7f\n\x16SetNamespacePermission\x12\x31.pomerium.dashboard.SetNamespacePermissionRequest\x1a\x32.pomerium.dashboard.SetNamespacePermissionResponseB-Z+github.com/pomerium/pomerium-console/pkg/pbb\x06proto3')



_NAMESPACE = DESCRIPTOR.message_types_by_name['Namespace']
_DELETENAMESPACEREQUEST = DESCRIPTOR.message_types_by_name['DeleteNamespaceRequest']
_DELETENAMESPACERESPONSE = DESCRIPTOR.message_types_by_name['DeleteNamespaceResponse']
_GETNAMESPACEREQUEST = DESCRIPTOR.message_types_by_name['GetNamespaceRequest']
_GETNAMESPACERESPONSE = DESCRIPTOR.message_types_by_name['GetNamespaceResponse']
_LISTNAMESPACESREQUEST = DESCRIPTOR.message_types_by_name['ListNamespacesRequest']
_LISTNAMESPACESRESPONSE = DESCRIPTOR.message_types_by_name['ListNamespacesResponse']
_SETNAMESPACEREQUEST = DESCRIPTOR.message_types_by_name['SetNamespaceRequest']
_SETNAMESPACERESPONSE = DESCRIPTOR.message_types_by_name['SetNamespaceResponse']
_NAMESPACEPERMISSION = DESCRIPTOR.message_types_by_name['NamespacePermission']
_NAMESPACEPERMISSIONGROUP = DESCRIPTOR.message_types_by_name['NamespacePermissionGroup']
_NAMESPACEPERMISSIONUSER = DESCRIPTOR.message_types_by_name['NamespacePermissionUser']
_DELETENAMESPACEPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteNamespacePermissionRequest']
_DELETENAMESPACEPERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteNamespacePermissionResponse']
_GETNAMESPACEPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['GetNamespacePermissionRequest']
_GETNAMESPACEPERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['GetNamespacePermissionResponse']
_LISTNAMESPACEPERMISSIONSREQUEST = DESCRIPTOR.message_types_by_name['ListNamespacePermissionsRequest']
_LISTNAMESPACEPERMISSIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListNamespacePermissionsResponse']
_LISTNAMESPACEPERMISSIONGROUPSREQUEST = DESCRIPTOR.message_types_by_name['ListNamespacePermissionGroupsRequest']
_LISTNAMESPACEPERMISSIONGROUPSRESPONSE = DESCRIPTOR.message_types_by_name['ListNamespacePermissionGroupsResponse']
_LISTNAMESPACEPERMISSIONUSERSREQUEST = DESCRIPTOR.message_types_by_name['ListNamespacePermissionUsersRequest']
_LISTNAMESPACEPERMISSIONUSERSRESPONSE = DESCRIPTOR.message_types_by_name['ListNamespacePermissionUsersResponse']
_SETNAMESPACEPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['SetNamespacePermissionRequest']
_SETNAMESPACEPERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['SetNamespacePermissionResponse']
Namespace = _reflection.GeneratedProtocolMessageType('Namespace', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.Namespace)
  })
_sym_db.RegisterMessage(Namespace)

DeleteNamespaceRequest = _reflection.GeneratedProtocolMessageType('DeleteNamespaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETENAMESPACEREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.DeleteNamespaceRequest)
  })
_sym_db.RegisterMessage(DeleteNamespaceRequest)

DeleteNamespaceResponse = _reflection.GeneratedProtocolMessageType('DeleteNamespaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETENAMESPACERESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.DeleteNamespaceResponse)
  })
_sym_db.RegisterMessage(DeleteNamespaceResponse)

GetNamespaceRequest = _reflection.GeneratedProtocolMessageType('GetNamespaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNAMESPACEREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.GetNamespaceRequest)
  })
_sym_db.RegisterMessage(GetNamespaceRequest)

GetNamespaceResponse = _reflection.GeneratedProtocolMessageType('GetNamespaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNAMESPACERESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.GetNamespaceResponse)
  })
_sym_db.RegisterMessage(GetNamespaceResponse)

ListNamespacesRequest = _reflection.GeneratedProtocolMessageType('ListNamespacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACESREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacesRequest)
  })
_sym_db.RegisterMessage(ListNamespacesRequest)

ListNamespacesResponse = _reflection.GeneratedProtocolMessageType('ListNamespacesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACESRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacesResponse)
  })
_sym_db.RegisterMessage(ListNamespacesResponse)

SetNamespaceRequest = _reflection.GeneratedProtocolMessageType('SetNamespaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETNAMESPACEREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.SetNamespaceRequest)
  })
_sym_db.RegisterMessage(SetNamespaceRequest)

SetNamespaceResponse = _reflection.GeneratedProtocolMessageType('SetNamespaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETNAMESPACERESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.SetNamespaceResponse)
  })
_sym_db.RegisterMessage(SetNamespaceResponse)

NamespacePermission = _reflection.GeneratedProtocolMessageType('NamespacePermission', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEPERMISSION,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.NamespacePermission)
  })
_sym_db.RegisterMessage(NamespacePermission)

NamespacePermissionGroup = _reflection.GeneratedProtocolMessageType('NamespacePermissionGroup', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEPERMISSIONGROUP,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.NamespacePermissionGroup)
  })
_sym_db.RegisterMessage(NamespacePermissionGroup)

NamespacePermissionUser = _reflection.GeneratedProtocolMessageType('NamespacePermissionUser', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEPERMISSIONUSER,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.NamespacePermissionUser)
  })
_sym_db.RegisterMessage(NamespacePermissionUser)

DeleteNamespacePermissionRequest = _reflection.GeneratedProtocolMessageType('DeleteNamespacePermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETENAMESPACEPERMISSIONREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.DeleteNamespacePermissionRequest)
  })
_sym_db.RegisterMessage(DeleteNamespacePermissionRequest)

DeleteNamespacePermissionResponse = _reflection.GeneratedProtocolMessageType('DeleteNamespacePermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETENAMESPACEPERMISSIONRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.DeleteNamespacePermissionResponse)
  })
_sym_db.RegisterMessage(DeleteNamespacePermissionResponse)

GetNamespacePermissionRequest = _reflection.GeneratedProtocolMessageType('GetNamespacePermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNAMESPACEPERMISSIONREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.GetNamespacePermissionRequest)
  })
_sym_db.RegisterMessage(GetNamespacePermissionRequest)

GetNamespacePermissionResponse = _reflection.GeneratedProtocolMessageType('GetNamespacePermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNAMESPACEPERMISSIONRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.GetNamespacePermissionResponse)
  })
_sym_db.RegisterMessage(GetNamespacePermissionResponse)

ListNamespacePermissionsRequest = _reflection.GeneratedProtocolMessageType('ListNamespacePermissionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACEPERMISSIONSREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacePermissionsRequest)
  })
_sym_db.RegisterMessage(ListNamespacePermissionsRequest)

ListNamespacePermissionsResponse = _reflection.GeneratedProtocolMessageType('ListNamespacePermissionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACEPERMISSIONSRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacePermissionsResponse)
  })
_sym_db.RegisterMessage(ListNamespacePermissionsResponse)

ListNamespacePermissionGroupsRequest = _reflection.GeneratedProtocolMessageType('ListNamespacePermissionGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACEPERMISSIONGROUPSREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacePermissionGroupsRequest)
  })
_sym_db.RegisterMessage(ListNamespacePermissionGroupsRequest)

ListNamespacePermissionGroupsResponse = _reflection.GeneratedProtocolMessageType('ListNamespacePermissionGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACEPERMISSIONGROUPSRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacePermissionGroupsResponse)
  })
_sym_db.RegisterMessage(ListNamespacePermissionGroupsResponse)

ListNamespacePermissionUsersRequest = _reflection.GeneratedProtocolMessageType('ListNamespacePermissionUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACEPERMISSIONUSERSREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacePermissionUsersRequest)
  })
_sym_db.RegisterMessage(ListNamespacePermissionUsersRequest)

ListNamespacePermissionUsersResponse = _reflection.GeneratedProtocolMessageType('ListNamespacePermissionUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNAMESPACEPERMISSIONUSERSRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListNamespacePermissionUsersResponse)
  })
_sym_db.RegisterMessage(ListNamespacePermissionUsersResponse)

SetNamespacePermissionRequest = _reflection.GeneratedProtocolMessageType('SetNamespacePermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETNAMESPACEPERMISSIONREQUEST,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.SetNamespacePermissionRequest)
  })
_sym_db.RegisterMessage(SetNamespacePermissionRequest)

SetNamespacePermissionResponse = _reflection.GeneratedProtocolMessageType('SetNamespacePermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETNAMESPACEPERMISSIONRESPONSE,
  '__module__' : 'namespaces_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.SetNamespacePermissionResponse)
  })
_sym_db.RegisterMessage(SetNamespacePermissionResponse)

_NAMESPACESERVICE = DESCRIPTOR.services_by_name['NamespaceService']
_NAMESPACEPERMISSIONSERVICE = DESCRIPTOR.services_by_name['NamespacePermissionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/pomerium/pomerium-console/pkg/pb'
  _NAMESPACE._serialized_start=74
  _NAMESPACE._serialized_end=318
  _DELETENAMESPACEREQUEST._serialized_start=320
  _DELETENAMESPACEREQUEST._serialized_end=356
  _DELETENAMESPACERESPONSE._serialized_start=358
  _DELETENAMESPACERESPONSE._serialized_end=383
  _GETNAMESPACEREQUEST._serialized_start=385
  _GETNAMESPACEREQUEST._serialized_end=418
  _GETNAMESPACERESPONSE._serialized_start=420
  _GETNAMESPACERESPONSE._serialized_end=492
  _LISTNAMESPACESREQUEST._serialized_start=494
  _LISTNAMESPACESREQUEST._serialized_end=517
  _LISTNAMESPACESRESPONSE._serialized_start=519
  _LISTNAMESPACESRESPONSE._serialized_end=594
  _SETNAMESPACEREQUEST._serialized_start=596
  _SETNAMESPACEREQUEST._serialized_end=667
  _SETNAMESPACERESPONSE._serialized_start=669
  _SETNAMESPACERESPONSE._serialized_end=741
  _NAMESPACEPERMISSION._serialized_start=744
  _NAMESPACEPERMISSION._serialized_end=976
  _NAMESPACEPERMISSIONGROUP._serialized_start=979
  _NAMESPACEPERMISSIONGROUP._serialized_end=1124
  _NAMESPACEPERMISSIONUSER._serialized_start=1127
  _NAMESPACEPERMISSIONUSER._serialized_end=1287
  _DELETENAMESPACEPERMISSIONREQUEST._serialized_start=1289
  _DELETENAMESPACEPERMISSIONREQUEST._serialized_end=1335
  _DELETENAMESPACEPERMISSIONRESPONSE._serialized_start=1337
  _DELETENAMESPACEPERMISSIONRESPONSE._serialized_end=1372
  _GETNAMESPACEPERMISSIONREQUEST._serialized_start=1374
  _GETNAMESPACEPERMISSIONREQUEST._serialized_end=1417
  _GETNAMESPACEPERMISSIONRESPONSE._serialized_start=1419
  _GETNAMESPACEPERMISSIONRESPONSE._serialized_end=1522
  _LISTNAMESPACEPERMISSIONSREQUEST._serialized_start=1524
  _LISTNAMESPACEPERMISSIONSREQUEST._serialized_end=1557
  _LISTNAMESPACEPERMISSIONSRESPONSE._serialized_start=1559
  _LISTNAMESPACEPERMISSIONSRESPONSE._serialized_end=1665
  _LISTNAMESPACEPERMISSIONGROUPSREQUEST._serialized_start=1667
  _LISTNAMESPACEPERMISSIONGROUPSREQUEST._serialized_end=1727
  _LISTNAMESPACEPERMISSIONGROUPSRESPONSE._serialized_start=1729
  _LISTNAMESPACEPERMISSIONGROUPSRESPONSE._serialized_end=1830
  _LISTNAMESPACEPERMISSIONUSERSREQUEST._serialized_start=1832
  _LISTNAMESPACEPERMISSIONUSERSREQUEST._serialized_end=1891
  _LISTNAMESPACEPERMISSIONUSERSRESPONSE._serialized_start=1893
  _LISTNAMESPACEPERMISSIONUSERSRESPONSE._serialized_end=1991
  _SETNAMESPACEPERMISSIONREQUEST._serialized_start=1993
  _SETNAMESPACEPERMISSIONREQUEST._serialized_end=2095
  _SETNAMESPACEPERMISSIONRESPONSE._serialized_start=2097
  _SETNAMESPACEPERMISSIONRESPONSE._serialized_end=2200
  _NAMESPACESERVICE._serialized_start=2203
  _NAMESPACESERVICE._serialized_end=2632
  _NAMESPACEPERMISSIONSERVICE._serialized_start=2635
  _NAMESPACEPERMISSIONSERVICE._serialized_end=3495
# @@protoc_insertion_point(module_scope)
