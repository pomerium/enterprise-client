# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xds/core/v3/authority.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xds/core/v3/authority.proto',
  package='xds.core.v3',
  syntax='proto3',
  serialized_options=b'\n\026com.github.xds.core.v3B\016AuthorityProtoP\001Z\"github.com/cncf/xds/go/xds/core/v3\322\306\244\341\006\002\010\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bxds/core/v3/authority.proto\x12\x0bxds.core.v3\x1a\x1fxds/annotations/v3/status.proto\x1a\x17validate/validate.proto\"\"\n\tAuthority\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x42V\n\x16\x63om.github.xds.core.v3B\x0e\x41uthorityProtoP\x01Z\"github.com/cncf/xds/go/xds/core/v3\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x62\x06proto3'
  ,
  dependencies=[xds_dot_annotations_dot_v3_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_AUTHORITY = _descriptor.Descriptor(
  name='Authority',
  full_name='xds.core.v3.Authority',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xds.core.v3.Authority.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['Authority'] = _AUTHORITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Authority = _reflection.GeneratedProtocolMessageType('Authority', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORITY,
  '__module__' : 'xds.core.v3.authority_pb2'
  # @@protoc_insertion_point(class_scope:xds.core.v3.Authority)
  })
_sym_db.RegisterMessage(Authority)


DESCRIPTOR._options = None
_AUTHORITY.fields_by_name['name']._options = None
# @@protoc_insertion_point(module_scope)
