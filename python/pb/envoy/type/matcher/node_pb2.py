# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/node.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.matcher import string_pb2 as envoy_dot_type_dot_matcher_dot_string__pb2
from envoy.type.matcher import struct_pb2 as envoy_dot_type_dot_matcher_dot_struct__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/node.proto',
  package='envoy.type.matcher',
  syntax='proto3',
  serialized_options=b'\n io.envoyproxy.envoy.type.matcherB\tNodeProtoP\001Z9github.com/envoyproxy/go-control-plane/envoy/type/matcher\272\200\310\321\006\002\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x65nvoy/type/matcher/node.proto\x12\x12\x65nvoy.type.matcher\x1a\x1f\x65nvoy/type/matcher/string.proto\x1a\x1f\x65nvoy/type/matcher/struct.proto\x1a\x1dudpa/annotations/status.proto\"|\n\x0bNodeMatcher\x12\x32\n\x07node_id\x18\x01 \x01(\x0b\x32!.envoy.type.matcher.StringMatcher\x12\x39\n\x0enode_metadatas\x18\x02 \x03(\x0b\x32!.envoy.type.matcher.StructMatcherBr\n io.envoyproxy.envoy.type.matcherB\tNodeProtoP\x01Z9github.com/envoyproxy/go-control-plane/envoy/type/matcher\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_matcher_dot_string__pb2.DESCRIPTOR,envoy_dot_type_dot_matcher_dot_struct__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,])




_NODEMATCHER = _descriptor.Descriptor(
  name='NodeMatcher',
  full_name='envoy.type.matcher.NodeMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='envoy.type.matcher.NodeMatcher.node_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_metadatas', full_name='envoy.type.matcher.NodeMatcher.node_metadatas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=150,
  serialized_end=274,
)

_NODEMATCHER.fields_by_name['node_id'].message_type = envoy_dot_type_dot_matcher_dot_string__pb2._STRINGMATCHER
_NODEMATCHER.fields_by_name['node_metadatas'].message_type = envoy_dot_type_dot_matcher_dot_struct__pb2._STRUCTMATCHER
DESCRIPTOR.message_types_by_name['NodeMatcher'] = _NODEMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeMatcher = _reflection.GeneratedProtocolMessageType('NodeMatcher', (_message.Message,), {
  'DESCRIPTOR' : _NODEMATCHER,
  '__module__' : 'envoy.type.matcher.node_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.NodeMatcher)
  })
_sym_db.RegisterMessage(NodeMatcher)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
