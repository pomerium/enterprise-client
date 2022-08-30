# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/pomerium/pomerium/pkg/grpc/user/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5github.com/pomerium/pomerium/pkg/grpc/user/user.proto\x12\x04user\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"$\n\x05\x43laim\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"\xd2\x01\n\x04User\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12&\n\x06\x63laims\x18\t \x03(\x0b\x32\x16.user.User.ClaimsEntry\x12\x1d\n\x15\x64\x65vice_credential_ids\x18\n \x03(\t\x1aI\n\x0b\x43laimsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\"\x93\x02\n\x0eServiceAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x0cnamespace_id\x18\x08 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\t \x01(\tH\x01\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12.\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tissued_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x61\x63\x63\x65ssed_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\n\r_namespace_idB\x0e\n\x0c_descriptionB,Z*github.com/pomerium/pomerium/pkg/grpc/userb\x06proto3')



_CLAIM = DESCRIPTOR.message_types_by_name['Claim']
_USER = DESCRIPTOR.message_types_by_name['User']
_USER_CLAIMSENTRY = _USER.nested_types_by_name['ClaimsEntry']
_SERVICEACCOUNT = DESCRIPTOR.message_types_by_name['ServiceAccount']
Claim = _reflection.GeneratedProtocolMessageType('Claim', (_message.Message,), {
  'DESCRIPTOR' : _CLAIM,
  '__module__' : 'github.com.pomerium.pomerium.pkg.grpc.user.user_pb2'
  # @@protoc_insertion_point(class_scope:user.Claim)
  })
_sym_db.RegisterMessage(Claim)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {

  'ClaimsEntry' : _reflection.GeneratedProtocolMessageType('ClaimsEntry', (_message.Message,), {
    'DESCRIPTOR' : _USER_CLAIMSENTRY,
    '__module__' : 'github.com.pomerium.pomerium.pkg.grpc.user.user_pb2'
    # @@protoc_insertion_point(class_scope:user.User.ClaimsEntry)
    })
  ,
  'DESCRIPTOR' : _USER,
  '__module__' : 'github.com.pomerium.pomerium.pkg.grpc.user.user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)
_sym_db.RegisterMessage(User.ClaimsEntry)

ServiceAccount = _reflection.GeneratedProtocolMessageType('ServiceAccount', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNT,
  '__module__' : 'github.com.pomerium.pomerium.pkg.grpc.user.user_pb2'
  # @@protoc_insertion_point(class_scope:user.ServiceAccount)
  })
_sym_db.RegisterMessage(ServiceAccount)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/pomerium/pomerium/pkg/grpc/user'
  _USER_CLAIMSENTRY._options = None
  _USER_CLAIMSENTRY._serialized_options = b'8\001'
  _CLAIM._serialized_start=126
  _CLAIM._serialized_end=162
  _USER._serialized_start=165
  _USER._serialized_end=375
  _USER_CLAIMSENTRY._serialized_start=302
  _USER_CLAIMSENTRY._serialized_end=375
  _SERVICEACCOUNT._serialized_start=378
  _SERVICEACCOUNT._serialized_end=653
# @@protoc_insertion_point(module_scope)
