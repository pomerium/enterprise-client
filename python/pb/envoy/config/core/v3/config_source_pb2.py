# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/config_source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.core.v3 import extension_pb2 as envoy_dot_config_dot_core_dot_v3_dot_extension__pb2
from envoy.config.core.v3 import grpc_service_pb2 as envoy_dot_config_dot_core_dot_v3_dot_grpc__service__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from xds.core.v3 import authority_pb2 as xds_dot_core_dot_v3_dot_authority__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(envoy/config/core/v3/config_source.proto\x12\x14\x65nvoy.config.core.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a$envoy/config/core/v3/extension.proto\x1a\'envoy/config/core/v3/grpc_service.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bxds/core/v3/authority.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xdc\x05\n\x0f\x41piConfigSource\x12I\n\x08\x61pi_type\x18\x01 \x01(\x0e\x32-.envoy.config.core.v3.ApiConfigSource.ApiTypeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12I\n\x15transport_api_version\x18\x08 \x01(\x0e\x32 .envoy.config.core.v3.ApiVersionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x15\n\rcluster_names\x18\x02 \x03(\t\x12\x38\n\rgrpc_services\x18\x04 \x03(\x0b\x32!.envoy.config.core.v3.GrpcService\x12\x30\n\rrefresh_delay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x0frequest_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02*\x00\x12\x44\n\x13rate_limit_settings\x18\x06 \x01(\x0b\x32\'.envoy.config.core.v3.RateLimitSettings\x12&\n\x1eset_node_on_first_message_only\x18\x07 \x01(\x08\x12\x45\n\x11\x63onfig_validators\x18\t \x03(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfig\"\x92\x01\n\x07\x41piType\x12\x33\n%DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE\x10\x00\x1a\x08\x08\x01\xa8\xf7\xb4\x8b\x02\x01\x12\x08\n\x04REST\x10\x01\x12\x08\n\x04GRPC\x10\x02\x12\x0e\n\nDELTA_GRPC\x10\x03\x12\x13\n\x0f\x41GGREGATED_GRPC\x10\x05\x12\x19\n\x15\x41GGREGATED_DELTA_GRPC\x10\x06:(\x9a\xc5\x88\x1e#\n!envoy.api.v2.core.ApiConfigSource\"I\n\x16\x41ggregatedConfigSource:/\x9a\xc5\x88\x1e*\n(envoy.api.v2.core.AggregatedConfigSource\"\x88\x01\n\x10SelfConfigSource\x12I\n\x15transport_api_version\x18\x01 \x01(\x0e\x32 .envoy.config.core.v3.ApiVersionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01:)\x9a\xc5\x88\x1e$\n\"envoy.api.v2.core.SelfConfigSource\"\xb2\x01\n\x11RateLimitSettings\x12\x30\n\nmax_tokens\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12?\n\tfill_rate\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0e\xfa\x42\x0b\x12\t!\x00\x00\x00\x00\x00\x00\x00\x00:*\x9a\xc5\x88\x1e%\n#envoy.api.v2.core.RateLimitSettings\"l\n\x10PathConfigSource\x12\x15\n\x04path\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x41\n\x11watched_directory\x18\x02 \x01(\x0b\x32&.envoy.config.core.v3.WatchedDirectory\"\xa2\x04\n\x0c\x43onfigSource\x12+\n\x0b\x61uthorities\x18\x07 \x03(\x0b\x32\x16.xds.core.v3.Authority\x12\x1b\n\x04path\x18\x01 \x01(\tB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0H\x00\x12\x44\n\x12path_config_source\x18\x08 \x01(\x0b\x32&.envoy.config.core.v3.PathConfigSourceH\x00\x12\x42\n\x11\x61pi_config_source\x18\x02 \x01(\x0b\x32%.envoy.config.core.v3.ApiConfigSourceH\x00\x12;\n\x03\x61\x64s\x18\x03 \x01(\x0b\x32,.envoy.config.core.v3.AggregatedConfigSourceH\x00\x12\x36\n\x04self\x18\x05 \x01(\x0b\x32&.envoy.config.core.v3.SelfConfigSourceH\x00\x12\x38\n\x15initial_fetch_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12H\n\x14resource_api_version\x18\x06 \x01(\x0e\x32 .envoy.config.core.v3.ApiVersionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.api.v2.core.ConfigSourceB\x1e\n\x17\x63onfig_source_specifier\x12\x03\xf8\x42\x01\"\xd5\x01\n\x15\x45xtensionConfigSource\x12\x43\n\rconfig_source\x18\x01 \x01(\x0b\x32\".envoy.config.core.v3.ConfigSourceB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\x12,\n\x0e\x64\x65\x66\x61ult_config\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12,\n$apply_default_config_without_warming\x18\x03 \x01(\x08\x12\x1b\n\ttype_urls\x18\x04 \x03(\tB\x08\xfa\x42\x05\x92\x01\x02\x08\x01*@\n\nApiVersion\x12\x15\n\x04\x41UTO\x10\x00\x1a\x0b\x08\x01\x8a\xf4\x9b\xb3\x05\x03\x33.0\x12\x13\n\x02V2\x10\x01\x1a\x0b\x08\x01\x8a\xf4\x9b\xb3\x05\x03\x33.0\x12\x06\n\x02V3\x10\x02\x42\x85\x01\n\"io.envoyproxy.envoy.config.core.v3B\x11\x43onfigSourceProtoP\x01ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_APIVERSION = DESCRIPTOR.enum_types_by_name['ApiVersion']
ApiVersion = enum_type_wrapper.EnumTypeWrapper(_APIVERSION)
AUTO = 0
V2 = 1
V3 = 2


_APICONFIGSOURCE = DESCRIPTOR.message_types_by_name['ApiConfigSource']
_AGGREGATEDCONFIGSOURCE = DESCRIPTOR.message_types_by_name['AggregatedConfigSource']
_SELFCONFIGSOURCE = DESCRIPTOR.message_types_by_name['SelfConfigSource']
_RATELIMITSETTINGS = DESCRIPTOR.message_types_by_name['RateLimitSettings']
_PATHCONFIGSOURCE = DESCRIPTOR.message_types_by_name['PathConfigSource']
_CONFIGSOURCE = DESCRIPTOR.message_types_by_name['ConfigSource']
_EXTENSIONCONFIGSOURCE = DESCRIPTOR.message_types_by_name['ExtensionConfigSource']
_APICONFIGSOURCE_APITYPE = _APICONFIGSOURCE.enum_types_by_name['ApiType']
ApiConfigSource = _reflection.GeneratedProtocolMessageType('ApiConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _APICONFIGSOURCE,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.ApiConfigSource)
  })
_sym_db.RegisterMessage(ApiConfigSource)

AggregatedConfigSource = _reflection.GeneratedProtocolMessageType('AggregatedConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEDCONFIGSOURCE,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.AggregatedConfigSource)
  })
_sym_db.RegisterMessage(AggregatedConfigSource)

SelfConfigSource = _reflection.GeneratedProtocolMessageType('SelfConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _SELFCONFIGSOURCE,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.SelfConfigSource)
  })
_sym_db.RegisterMessage(SelfConfigSource)

RateLimitSettings = _reflection.GeneratedProtocolMessageType('RateLimitSettings', (_message.Message,), {
  'DESCRIPTOR' : _RATELIMITSETTINGS,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.RateLimitSettings)
  })
_sym_db.RegisterMessage(RateLimitSettings)

PathConfigSource = _reflection.GeneratedProtocolMessageType('PathConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _PATHCONFIGSOURCE,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.PathConfigSource)
  })
_sym_db.RegisterMessage(PathConfigSource)

ConfigSource = _reflection.GeneratedProtocolMessageType('ConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGSOURCE,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.ConfigSource)
  })
_sym_db.RegisterMessage(ConfigSource)

ExtensionConfigSource = _reflection.GeneratedProtocolMessageType('ExtensionConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONCONFIGSOURCE,
  '__module__' : 'envoy.config.core.v3.config_source_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.ExtensionConfigSource)
  })
_sym_db.RegisterMessage(ExtensionConfigSource)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"io.envoyproxy.envoy.config.core.v3B\021ConfigSourceProtoP\001ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\272\200\310\321\006\002\020\002'
  _APIVERSION.values_by_name["AUTO"]._options = None
  _APIVERSION.values_by_name["AUTO"]._serialized_options = b'\010\001\212\364\233\263\005\0033.0'
  _APIVERSION.values_by_name["V2"]._options = None
  _APIVERSION.values_by_name["V2"]._serialized_options = b'\010\001\212\364\233\263\005\0033.0'
  _APICONFIGSOURCE_APITYPE.values_by_name["DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE"]._options = None
  _APICONFIGSOURCE_APITYPE.values_by_name["DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE"]._serialized_options = b'\010\001\250\367\264\213\002\001'
  _APICONFIGSOURCE.fields_by_name['api_type']._options = None
  _APICONFIGSOURCE.fields_by_name['api_type']._serialized_options = b'\372B\005\202\001\002\020\001'
  _APICONFIGSOURCE.fields_by_name['transport_api_version']._options = None
  _APICONFIGSOURCE.fields_by_name['transport_api_version']._serialized_options = b'\372B\005\202\001\002\020\001'
  _APICONFIGSOURCE.fields_by_name['request_timeout']._options = None
  _APICONFIGSOURCE.fields_by_name['request_timeout']._serialized_options = b'\372B\005\252\001\002*\000'
  _APICONFIGSOURCE._options = None
  _APICONFIGSOURCE._serialized_options = b'\232\305\210\036#\n!envoy.api.v2.core.ApiConfigSource'
  _AGGREGATEDCONFIGSOURCE._options = None
  _AGGREGATEDCONFIGSOURCE._serialized_options = b'\232\305\210\036*\n(envoy.api.v2.core.AggregatedConfigSource'
  _SELFCONFIGSOURCE.fields_by_name['transport_api_version']._options = None
  _SELFCONFIGSOURCE.fields_by_name['transport_api_version']._serialized_options = b'\372B\005\202\001\002\020\001'
  _SELFCONFIGSOURCE._options = None
  _SELFCONFIGSOURCE._serialized_options = b'\232\305\210\036$\n\"envoy.api.v2.core.SelfConfigSource'
  _RATELIMITSETTINGS.fields_by_name['fill_rate']._options = None
  _RATELIMITSETTINGS.fields_by_name['fill_rate']._serialized_options = b'\372B\013\022\t!\000\000\000\000\000\000\000\000'
  _RATELIMITSETTINGS._options = None
  _RATELIMITSETTINGS._serialized_options = b'\232\305\210\036%\n#envoy.api.v2.core.RateLimitSettings'
  _PATHCONFIGSOURCE.fields_by_name['path']._options = None
  _PATHCONFIGSOURCE.fields_by_name['path']._serialized_options = b'\372B\004r\002\020\001'
  _CONFIGSOURCE.oneofs_by_name['config_source_specifier']._options = None
  _CONFIGSOURCE.oneofs_by_name['config_source_specifier']._serialized_options = b'\370B\001'
  _CONFIGSOURCE.fields_by_name['path']._options = None
  _CONFIGSOURCE.fields_by_name['path']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CONFIGSOURCE.fields_by_name['resource_api_version']._options = None
  _CONFIGSOURCE.fields_by_name['resource_api_version']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CONFIGSOURCE._options = None
  _CONFIGSOURCE._serialized_options = b'\232\305\210\036 \n\036envoy.api.v2.core.ConfigSource'
  _EXTENSIONCONFIGSOURCE.fields_by_name['config_source']._options = None
  _EXTENSIONCONFIGSOURCE.fields_by_name['config_source']._serialized_options = b'\372B\005\242\001\002\010\001'
  _EXTENSIONCONFIGSOURCE.fields_by_name['type_urls']._options = None
  _EXTENSIONCONFIGSOURCE.fields_by_name['type_urls']._serialized_options = b'\372B\005\222\001\002\010\001'
  _APIVERSION._serialized_start=2431
  _APIVERSION._serialized_end=2495
  _APICONFIGSOURCE._serialized_start=427
  _APICONFIGSOURCE._serialized_end=1159
  _APICONFIGSOURCE_APITYPE._serialized_start=971
  _APICONFIGSOURCE_APITYPE._serialized_end=1117
  _AGGREGATEDCONFIGSOURCE._serialized_start=1161
  _AGGREGATEDCONFIGSOURCE._serialized_end=1234
  _SELFCONFIGSOURCE._serialized_start=1237
  _SELFCONFIGSOURCE._serialized_end=1373
  _RATELIMITSETTINGS._serialized_start=1376
  _RATELIMITSETTINGS._serialized_end=1554
  _PATHCONFIGSOURCE._serialized_start=1556
  _PATHCONFIGSOURCE._serialized_end=1664
  _CONFIGSOURCE._serialized_start=1667
  _CONFIGSOURCE._serialized_end=2213
  _EXTENSIONCONFIGSOURCE._serialized_start=2216
  _EXTENSIONCONFIGSOURCE._serialized_end=2429
# @@protoc_insertion_point(module_scope)
