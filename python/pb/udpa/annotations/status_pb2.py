# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udpa/annotations/status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dudpa/annotations/status.proto\x12\x10udpa.annotations\x1a google/protobuf/descriptor.proto\"t\n\x10StatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\x12\x46\n\x16package_version_status\x18\x02 \x01(\x0e\x32&.udpa.annotations.PackageVersionStatus*]\n\x14PackageVersionStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46ROZEN\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12 \n\x1cNEXT_MAJOR_VERSION_CANDIDATE\x10\x03:X\n\x0b\x66ile_status\x12\x1c.google.protobuf.FileOptions\x18\x87\x80\x99j \x01(\x0b\x32\".udpa.annotations.StatusAnnotationb\x06proto3')

_PACKAGEVERSIONSTATUS = DESCRIPTOR.enum_types_by_name['PackageVersionStatus']
PackageVersionStatus = enum_type_wrapper.EnumTypeWrapper(_PACKAGEVERSIONSTATUS)
UNKNOWN = 0
FROZEN = 1
ACTIVE = 2
NEXT_MAJOR_VERSION_CANDIDATE = 3

FILE_STATUS_FIELD_NUMBER = 222707719
file_status = DESCRIPTOR.extensions_by_name['file_status']

_STATUSANNOTATION = DESCRIPTOR.message_types_by_name['StatusAnnotation']
StatusAnnotation = _reflection.GeneratedProtocolMessageType('StatusAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _STATUSANNOTATION,
  '__module__' : 'udpa.annotations.status_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.StatusAnnotation)
  })
_sym_db.RegisterMessage(StatusAnnotation)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(file_status)

  DESCRIPTOR._options = None
  _PACKAGEVERSIONSTATUS._serialized_start=203
  _PACKAGEVERSIONSTATUS._serialized_end=296
  _STATUSANNOTATION._serialized_start=85
  _STATUSANNOTATION._serialized_end=201
# @@protoc_insertion_point(module_scope)
