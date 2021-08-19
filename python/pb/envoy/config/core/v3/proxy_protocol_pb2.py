# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/proxy_protocol.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/core/v3/proxy_protocol.proto',
  package='envoy.config.core.v3',
  syntax='proto3',
  serialized_options=b'\n\"io.envoyproxy.envoy.config.core.v3B\022ProxyProtocolProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)envoy/config/core/v3/proxy_protocol.proto\x12\x14\x65nvoy.config.core.v3\x1a\x1dudpa/annotations/status.proto\"t\n\x13ProxyProtocolConfig\x12\x42\n\x07version\x18\x01 \x01(\x0e\x32\x31.envoy.config.core.v3.ProxyProtocolConfig.Version\"\x19\n\x07Version\x12\x06\n\x02V1\x10\x00\x12\x06\n\x02V2\x10\x01\x42\x42\n\"io.envoyproxy.envoy.config.core.v3B\x12ProxyProtocolProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,])



_PROXYPROTOCOLCONFIG_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='envoy.config.core.v3.ProxyProtocolConfig.Version',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=189,
  serialized_end=214,
)
_sym_db.RegisterEnumDescriptor(_PROXYPROTOCOLCONFIG_VERSION)


_PROXYPROTOCOLCONFIG = _descriptor.Descriptor(
  name='ProxyProtocolConfig',
  full_name='envoy.config.core.v3.ProxyProtocolConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='envoy.config.core.v3.ProxyProtocolConfig.version', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROXYPROTOCOLCONFIG_VERSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=214,
)

_PROXYPROTOCOLCONFIG.fields_by_name['version'].enum_type = _PROXYPROTOCOLCONFIG_VERSION
_PROXYPROTOCOLCONFIG_VERSION.containing_type = _PROXYPROTOCOLCONFIG
DESCRIPTOR.message_types_by_name['ProxyProtocolConfig'] = _PROXYPROTOCOLCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProxyProtocolConfig = _reflection.GeneratedProtocolMessageType('ProxyProtocolConfig', (_message.Message,), {
  'DESCRIPTOR' : _PROXYPROTOCOLCONFIG,
  '__module__' : 'envoy.config.core.v3.proxy_protocol_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.ProxyProtocolConfig)
  })
_sym_db.RegisterMessage(ProxyProtocolConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
