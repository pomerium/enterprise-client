# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/struct.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.matcher import value_pb2 as envoy_dot_type_dot_matcher_dot_value__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/struct.proto',
  package='envoy.type.matcher',
  syntax='proto3',
  serialized_options=b'\n io.envoyproxy.envoy.type.matcherB\013StructProtoP\001Z9github.com/envoyproxy/go-control-plane/envoy/type/matcher\272\200\310\321\006\002\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x65nvoy/type/matcher/struct.proto\x12\x12\x65nvoy.type.matcher\x1a\x1e\x65nvoy/type/matcher/value.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xc8\x01\n\rStructMatcher\x12\x45\n\x04path\x18\x02 \x03(\x0b\x32-.envoy.type.matcher.StructMatcher.PathSegmentB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x12\x39\n\x05value\x18\x03 \x01(\x0b\x32 .envoy.type.matcher.ValueMatcherB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x1a\x35\n\x0bPathSegment\x12\x16\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00\x42\x0e\n\x07segment\x12\x03\xf8\x42\x01\x42t\n io.envoyproxy.envoy.type.matcherB\x0bStructProtoP\x01Z9github.com/envoyproxy/go-control-plane/envoy/type/matcher\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_matcher_dot_value__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_STRUCTMATCHER_PATHSEGMENT = _descriptor.Descriptor(
  name='PathSegment',
  full_name='envoy.type.matcher.StructMatcher.PathSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.matcher.StructMatcher.PathSegment.key', index=0,
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
    _descriptor.OneofDescriptor(
      name='segment', full_name='envoy.type.matcher.StructMatcher.PathSegment.segment',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=291,
  serialized_end=344,
)

_STRUCTMATCHER = _descriptor.Descriptor(
  name='StructMatcher',
  full_name='envoy.type.matcher.StructMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.type.matcher.StructMatcher.path', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.type.matcher.StructMatcher.value', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STRUCTMATCHER_PATHSEGMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=344,
)

_STRUCTMATCHER_PATHSEGMENT.containing_type = _STRUCTMATCHER
_STRUCTMATCHER_PATHSEGMENT.oneofs_by_name['segment'].fields.append(
  _STRUCTMATCHER_PATHSEGMENT.fields_by_name['key'])
_STRUCTMATCHER_PATHSEGMENT.fields_by_name['key'].containing_oneof = _STRUCTMATCHER_PATHSEGMENT.oneofs_by_name['segment']
_STRUCTMATCHER.fields_by_name['path'].message_type = _STRUCTMATCHER_PATHSEGMENT
_STRUCTMATCHER.fields_by_name['value'].message_type = envoy_dot_type_dot_matcher_dot_value__pb2._VALUEMATCHER
DESCRIPTOR.message_types_by_name['StructMatcher'] = _STRUCTMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StructMatcher = _reflection.GeneratedProtocolMessageType('StructMatcher', (_message.Message,), {

  'PathSegment' : _reflection.GeneratedProtocolMessageType('PathSegment', (_message.Message,), {
    'DESCRIPTOR' : _STRUCTMATCHER_PATHSEGMENT,
    '__module__' : 'envoy.type.matcher.struct_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.matcher.StructMatcher.PathSegment)
    })
  ,
  'DESCRIPTOR' : _STRUCTMATCHER,
  '__module__' : 'envoy.type.matcher.struct_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.StructMatcher)
  })
_sym_db.RegisterMessage(StructMatcher)
_sym_db.RegisterMessage(StructMatcher.PathSegment)


DESCRIPTOR._options = None
_STRUCTMATCHER_PATHSEGMENT.oneofs_by_name['segment']._options = None
_STRUCTMATCHER_PATHSEGMENT.fields_by_name['key']._options = None
_STRUCTMATCHER.fields_by_name['path']._options = None
_STRUCTMATCHER.fields_by_name['value']._options = None
# @@protoc_insertion_point(module_scope)
