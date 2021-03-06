"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import envoy.config.core.v3.grpc_service_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions
import xds.core.v3.authority_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ApiVersion(_ApiVersion, metaclass=_ApiVersionEnumTypeWrapper):
    """[#protodoc-title: Configuration sources]

    xDS API and non-xDS services version. This is used to describe both resource and transport
    protocol versions (in distinct configuration fields).
    """
    pass
class _ApiVersion:
    V = typing.NewType('V', builtins.int)
class _ApiVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ApiVersion.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    AUTO = ApiVersion.V(0)
    """When not specified, we assume v2, to ease migration to Envoy's stable API
    versioning. If a client does not support v2 (e.g. due to deprecation), this
    is an invalid value.
    """

    V2 = ApiVersion.V(1)
    """Use xDS v2 API."""

    V3 = ApiVersion.V(2)
    """Use xDS v3 API."""


AUTO = ApiVersion.V(0)
"""When not specified, we assume v2, to ease migration to Envoy's stable API
versioning. If a client does not support v2 (e.g. due to deprecation), this
is an invalid value.
"""

V2 = ApiVersion.V(1)
"""Use xDS v2 API."""

V3 = ApiVersion.V(2)
"""Use xDS v3 API."""

global___ApiVersion = ApiVersion


class ApiConfigSource(google.protobuf.message.Message):
    """API configuration source. This identifies the API type and cluster that Envoy
    will use to fetch an xDS API.
    [#next-free-field: 9]
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ApiType(_ApiType, metaclass=_ApiTypeEnumTypeWrapper):
        """APIs may be fetched via either REST or gRPC."""
        pass
    class _ApiType:
        V = typing.NewType('V', builtins.int)
    class _ApiTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ApiType.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE = ApiConfigSource.ApiType.V(0)
        """Ideally this would be 'reserved 0' but one can't reserve the default
        value. Instead we throw an exception if this is ever used.
        """

        REST = ApiConfigSource.ApiType.V(1)
        """REST-JSON v2 API. The `canonical JSON encoding
        <https://developers.google.com/protocol-buffers/docs/proto3#json>`_ for
        the v2 protos is used.
        """

        GRPC = ApiConfigSource.ApiType.V(2)
        """SotW gRPC service."""

        DELTA_GRPC = ApiConfigSource.ApiType.V(3)
        """Using the delta xDS gRPC service, i.e. DeltaDiscovery{Request,Response}
        rather than Discovery{Request,Response}. Rather than sending Envoy the entire state
        with every update, the xDS server only sends what has changed since the last update.
        """

        AGGREGATED_GRPC = ApiConfigSource.ApiType.V(5)
        """SotW xDS gRPC with ADS. All resources which resolve to this configuration source will be
        multiplexed on a single connection to an ADS endpoint.
        [#not-implemented-hide:]
        """

        AGGREGATED_DELTA_GRPC = ApiConfigSource.ApiType.V(6)
        """Delta xDS gRPC with ADS. All resources which resolve to this configuration source will be
        multiplexed on a single connection to an ADS endpoint.
        [#not-implemented-hide:]
        """


    DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE = ApiConfigSource.ApiType.V(0)
    """Ideally this would be 'reserved 0' but one can't reserve the default
    value. Instead we throw an exception if this is ever used.
    """

    REST = ApiConfigSource.ApiType.V(1)
    """REST-JSON v2 API. The `canonical JSON encoding
    <https://developers.google.com/protocol-buffers/docs/proto3#json>`_ for
    the v2 protos is used.
    """

    GRPC = ApiConfigSource.ApiType.V(2)
    """SotW gRPC service."""

    DELTA_GRPC = ApiConfigSource.ApiType.V(3)
    """Using the delta xDS gRPC service, i.e. DeltaDiscovery{Request,Response}
    rather than Discovery{Request,Response}. Rather than sending Envoy the entire state
    with every update, the xDS server only sends what has changed since the last update.
    """

    AGGREGATED_GRPC = ApiConfigSource.ApiType.V(5)
    """SotW xDS gRPC with ADS. All resources which resolve to this configuration source will be
    multiplexed on a single connection to an ADS endpoint.
    [#not-implemented-hide:]
    """

    AGGREGATED_DELTA_GRPC = ApiConfigSource.ApiType.V(6)
    """Delta xDS gRPC with ADS. All resources which resolve to this configuration source will be
    multiplexed on a single connection to an ADS endpoint.
    [#not-implemented-hide:]
    """


    API_TYPE_FIELD_NUMBER: builtins.int
    TRANSPORT_API_VERSION_FIELD_NUMBER: builtins.int
    CLUSTER_NAMES_FIELD_NUMBER: builtins.int
    GRPC_SERVICES_FIELD_NUMBER: builtins.int
    REFRESH_DELAY_FIELD_NUMBER: builtins.int
    REQUEST_TIMEOUT_FIELD_NUMBER: builtins.int
    RATE_LIMIT_SETTINGS_FIELD_NUMBER: builtins.int
    SET_NODE_ON_FIRST_MESSAGE_ONLY_FIELD_NUMBER: builtins.int
    api_type: global___ApiConfigSource.ApiType.V = ...
    """API type (gRPC, REST, delta gRPC)"""

    transport_api_version: global___ApiVersion.V = ...
    """API version for xDS transport protocol. This describes the xDS gRPC/REST
    endpoint and version of [Delta]DiscoveryRequest/Response used on the wire.
    """

    @property
    def cluster_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Cluster names should be used only with REST. If > 1
        cluster is defined, clusters will be cycled through if any kind of failure
        occurs.

        .. note::

         The cluster with name ``cluster_name`` must be statically defined and its
         type must not be ``EDS``.
        """
        pass
    @property
    def grpc_services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[envoy.config.core.v3.grpc_service_pb2.GrpcService]:
        """Multiple gRPC services be provided for GRPC. If > 1 cluster is defined,
        services will be cycled through if any kind of failure occurs.
        """
        pass
    @property
    def refresh_delay(self) -> google.protobuf.duration_pb2.Duration:
        """For REST APIs, the delay between successive polls."""
        pass
    @property
    def request_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """For REST APIs, the request timeout. If not set, a default value of 1s will be used."""
        pass
    @property
    def rate_limit_settings(self) -> global___RateLimitSettings:
        """For GRPC APIs, the rate limit settings. If present, discovery requests made by Envoy will be
        rate limited.
        """
        pass
    set_node_on_first_message_only: builtins.bool = ...
    """Skip the node identifier in subsequent discovery requests for streaming gRPC config types."""

    def __init__(self,
        *,
        api_type : global___ApiConfigSource.ApiType.V = ...,
        transport_api_version : global___ApiVersion.V = ...,
        cluster_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        grpc_services : typing.Optional[typing.Iterable[envoy.config.core.v3.grpc_service_pb2.GrpcService]] = ...,
        refresh_delay : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        request_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        rate_limit_settings : typing.Optional[global___RateLimitSettings] = ...,
        set_node_on_first_message_only : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"rate_limit_settings",b"rate_limit_settings",u"refresh_delay",b"refresh_delay",u"request_timeout",b"request_timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"api_type",b"api_type",u"cluster_names",b"cluster_names",u"grpc_services",b"grpc_services",u"rate_limit_settings",b"rate_limit_settings",u"refresh_delay",b"refresh_delay",u"request_timeout",b"request_timeout",u"set_node_on_first_message_only",b"set_node_on_first_message_only",u"transport_api_version",b"transport_api_version"]) -> None: ...
global___ApiConfigSource = ApiConfigSource

class AggregatedConfigSource(google.protobuf.message.Message):
    """Aggregated Discovery Service (ADS) options. This is currently empty, but when
    set in :ref:`ConfigSource <envoy_v3_api_msg_config.core.v3.ConfigSource>` can be used to
    specify that ADS is to be used.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___AggregatedConfigSource = AggregatedConfigSource

class SelfConfigSource(google.protobuf.message.Message):
    """[#not-implemented-hide:]
    Self-referencing config source options. This is currently empty, but when
    set in :ref:`ConfigSource <envoy_v3_api_msg_config.core.v3.ConfigSource>` can be used to
    specify that other data can be obtained from the same server.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSPORT_API_VERSION_FIELD_NUMBER: builtins.int
    transport_api_version: global___ApiVersion.V = ...
    """API version for xDS transport protocol. This describes the xDS gRPC/REST
    endpoint and version of [Delta]DiscoveryRequest/Response used on the wire.
    """

    def __init__(self,
        *,
        transport_api_version : global___ApiVersion.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"transport_api_version",b"transport_api_version"]) -> None: ...
global___SelfConfigSource = SelfConfigSource

class RateLimitSettings(google.protobuf.message.Message):
    """Rate Limit settings to be applied for discovery requests made by Envoy."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_TOKENS_FIELD_NUMBER: builtins.int
    FILL_RATE_FIELD_NUMBER: builtins.int
    @property
    def max_tokens(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """Maximum number of tokens to be used for rate limiting discovery request calls. If not set, a
        default value of 100 will be used.
        """
        pass
    @property
    def fill_rate(self) -> google.protobuf.wrappers_pb2.DoubleValue:
        """Rate at which tokens will be filled per second. If not set, a default fill rate of 10 tokens
        per second will be used.
        """
        pass
    def __init__(self,
        *,
        max_tokens : typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        fill_rate : typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"fill_rate",b"fill_rate",u"max_tokens",b"max_tokens"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fill_rate",b"fill_rate",u"max_tokens",b"max_tokens"]) -> None: ...
global___RateLimitSettings = RateLimitSettings

class ConfigSource(google.protobuf.message.Message):
    """Configuration for :ref:`listeners <config_listeners>`, :ref:`clusters
    <config_cluster_manager>`, :ref:`routes
    <envoy_v3_api_msg_config.route.v3.RouteConfiguration>`, :ref:`endpoints
    <arch_overview_service_discovery>` etc. may either be sourced from the
    filesystem or from an xDS API source. Filesystem configs are watched with
    inotify for updates.
    [#next-free-field: 8]
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AUTHORITIES_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    API_CONFIG_SOURCE_FIELD_NUMBER: builtins.int
    ADS_FIELD_NUMBER: builtins.int
    SELF_FIELD_NUMBER: builtins.int
    INITIAL_FETCH_TIMEOUT_FIELD_NUMBER: builtins.int
    RESOURCE_API_VERSION_FIELD_NUMBER: builtins.int
    @property
    def authorities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[xds.core.v3.authority_pb2.Authority]:
        """Authorities that this config source may be used for. An authority specified in a xdstp:// URL
        is resolved to a *ConfigSource* prior to configuration fetch. This field provides the
        association between authority name and configuration source.
        [#not-implemented-hide:]
        """
        pass
    path: typing.Text = ...
    """Path on the filesystem to source and watch for configuration updates.
    When sourcing configuration for :ref:`secret <envoy_v3_api_msg_extensions.transport_sockets.tls.v3.Secret>`,
    the certificate and key files are also watched for updates.

    .. note::

     The path to the source must exist at config load time.

    .. note::

      Envoy will only watch the file path for *moves.* This is because in general only moves
      are atomic. The same method of swapping files as is demonstrated in the
      :ref:`runtime documentation <config_runtime_symbolic_link_swap>` can be used here also.
    """

    @property
    def api_config_source(self) -> global___ApiConfigSource:
        """API configuration source."""
        pass
    @property
    def ads(self) -> global___AggregatedConfigSource:
        """When set, ADS will be used to fetch resources. The ADS API configuration
        source in the bootstrap configuration is used.
        """
        pass
    @property
    def self(self) -> global___SelfConfigSource:
        """[#not-implemented-hide:]
        When set, the client will access the resources from the same server it got the
        ConfigSource from, although not necessarily from the same stream. This is similar to the
        :ref:`ads<envoy_v3_api_field.ConfigSource.ads>` field, except that the client may use a
        different stream to the same server. As a result, this field can be used for things
        like LRS that cannot be sent on an ADS stream. It can also be used to link from (e.g.)
        LDS to RDS on the same server without requiring the management server to know its name
        or required credentials.
        [#next-major-version: In xDS v3, consider replacing the ads field with this one, since
        this field can implicitly mean to use the same stream in the case where the ConfigSource
        is provided via ADS and the specified data can also be obtained via ADS.]
        """
        pass
    @property
    def initial_fetch_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """When this timeout is specified, Envoy will wait no longer than the specified time for first
        config response on this xDS subscription during the :ref:`initialization process
        <arch_overview_initialization>`. After reaching the timeout, Envoy will move to the next
        initialization phase, even if the first config is not delivered yet. The timer is activated
        when the xDS API subscription starts, and is disarmed on first config update or on error. 0
        means no timeout - Envoy will wait indefinitely for the first xDS config (unless another
        timeout applies). The default is 15s.
        """
        pass
    resource_api_version: global___ApiVersion.V = ...
    """API version for xDS resources. This implies the type URLs that the client
    will request for resources and the resource type that the client will in
    turn expect to be delivered.
    """

    def __init__(self_,
        *,
        authorities : typing.Optional[typing.Iterable[xds.core.v3.authority_pb2.Authority]] = ...,
        path : typing.Text = ...,
        api_config_source : typing.Optional[global___ApiConfigSource] = ...,
        ads : typing.Optional[global___AggregatedConfigSource] = ...,
        self : typing.Optional[global___SelfConfigSource] = ...,
        initial_fetch_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        resource_api_version : global___ApiVersion.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"ads",b"ads",u"api_config_source",b"api_config_source",u"config_source_specifier",b"config_source_specifier",u"initial_fetch_timeout",b"initial_fetch_timeout",u"path",b"path",u"self",b"self"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"ads",b"ads",u"api_config_source",b"api_config_source",u"authorities",b"authorities",u"config_source_specifier",b"config_source_specifier",u"initial_fetch_timeout",b"initial_fetch_timeout",u"path",b"path",u"resource_api_version",b"resource_api_version",u"self",b"self"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"config_source_specifier",b"config_source_specifier"]) -> typing.Optional[typing_extensions.Literal["path","api_config_source","ads","self"]]: ...
global___ConfigSource = ConfigSource
