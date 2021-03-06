# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/string.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.matcher import regex_pb2 as envoy_dot_type_dot_matcher_dot_regex__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/string.proto',
  package='envoy.type.matcher',
  syntax='proto3',
  serialized_options=b'\n io.envoyproxy.envoy.type.matcherB\013StringProtoP\001Z9github.com/envoyproxy/go-control-plane/envoy/type/matcher\272\200\310\321\006\002\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x65nvoy/type/matcher/string.proto\x12\x12\x65nvoy.type.matcher\x1a\x1e\x65nvoy/type/matcher/regex.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xe6\x01\n\rStringMatcher\x12\x0f\n\x05\x65xact\x18\x01 \x01(\tH\x00\x12\x19\n\x06prefix\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00\x12\x19\n\x06suffix\x18\x03 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00\x12!\n\x05regex\x18\x04 \x01(\tB\x10\x18\x01\xfa\x42\x05r\x03(\x80\x08\xb8\xee\xf2\xd2\x05\x01H\x00\x12@\n\nsafe_regex\x18\x05 \x01(\x0b\x32 .envoy.type.matcher.RegexMatcherB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00\x12\x13\n\x0bignore_case\x18\x06 \x01(\x08\x42\x14\n\rmatch_pattern\x12\x03\xf8\x42\x01\"R\n\x11ListStringMatcher\x12=\n\x08patterns\x18\x01 \x03(\x0b\x32!.envoy.type.matcher.StringMatcherB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x42t\n io.envoyproxy.envoy.type.matcherB\x0bStringProtoP\x01Z9github.com/envoyproxy/go-control-plane/envoy/type/matcher\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_matcher_dot_regex__pb2.DESCRIPTOR,envoy_dot_annotations_dot_deprecation__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_STRINGMATCHER = _descriptor.Descriptor(
  name='StringMatcher',
  full_name='envoy.type.matcher.StringMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exact', full_name='envoy.type.matcher.StringMatcher.exact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='envoy.type.matcher.StringMatcher.prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='suffix', full_name='envoy.type.matcher.StringMatcher.suffix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regex', full_name='envoy.type.matcher.StringMatcher.regex', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001\372B\005r\003(\200\010\270\356\362\322\005\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='safe_regex', full_name='envoy.type.matcher.StringMatcher.safe_regex', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ignore_case', full_name='envoy.type.matcher.StringMatcher.ignore_case', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='match_pattern', full_name='envoy.type.matcher.StringMatcher.match_pattern',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=181,
  serialized_end=411,
)


_LISTSTRINGMATCHER = _descriptor.Descriptor(
  name='ListStringMatcher',
  full_name='envoy.type.matcher.ListStringMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='patterns', full_name='envoy.type.matcher.ListStringMatcher.patterns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=413,
  serialized_end=495,
)

_STRINGMATCHER.fields_by_name['safe_regex'].message_type = envoy_dot_type_dot_matcher_dot_regex__pb2._REGEXMATCHER
_STRINGMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _STRINGMATCHER.fields_by_name['exact'])
_STRINGMATCHER.fields_by_name['exact'].containing_oneof = _STRINGMATCHER.oneofs_by_name['match_pattern']
_STRINGMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _STRINGMATCHER.fields_by_name['prefix'])
_STRINGMATCHER.fields_by_name['prefix'].containing_oneof = _STRINGMATCHER.oneofs_by_name['match_pattern']
_STRINGMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _STRINGMATCHER.fields_by_name['suffix'])
_STRINGMATCHER.fields_by_name['suffix'].containing_oneof = _STRINGMATCHER.oneofs_by_name['match_pattern']
_STRINGMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _STRINGMATCHER.fields_by_name['regex'])
_STRINGMATCHER.fields_by_name['regex'].containing_oneof = _STRINGMATCHER.oneofs_by_name['match_pattern']
_STRINGMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _STRINGMATCHER.fields_by_name['safe_regex'])
_STRINGMATCHER.fields_by_name['safe_regex'].containing_oneof = _STRINGMATCHER.oneofs_by_name['match_pattern']
_LISTSTRINGMATCHER.fields_by_name['patterns'].message_type = _STRINGMATCHER
DESCRIPTOR.message_types_by_name['StringMatcher'] = _STRINGMATCHER
DESCRIPTOR.message_types_by_name['ListStringMatcher'] = _LISTSTRINGMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringMatcher = _reflection.GeneratedProtocolMessageType('StringMatcher', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMATCHER,
  '__module__' : 'envoy.type.matcher.string_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.StringMatcher)
  })
_sym_db.RegisterMessage(StringMatcher)

ListStringMatcher = _reflection.GeneratedProtocolMessageType('ListStringMatcher', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTRINGMATCHER,
  '__module__' : 'envoy.type.matcher.string_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.ListStringMatcher)
  })
_sym_db.RegisterMessage(ListStringMatcher)


DESCRIPTOR._options = None
_STRINGMATCHER.oneofs_by_name['match_pattern']._options = None
_STRINGMATCHER.fields_by_name['prefix']._options = None
_STRINGMATCHER.fields_by_name['suffix']._options = None
_STRINGMATCHER.fields_by_name['regex']._options = None
_STRINGMATCHER.fields_by_name['safe_regex']._options = None
_LISTSTRINGMATCHER.fields_by_name['patterns']._options = None
# @@protoc_insertion_point(module_scope)
