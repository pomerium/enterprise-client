"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MetadataKey(google.protobuf.message.Message):
    """[#protodoc-title: Metadata]

    MetadataKey provides a general interface using `key` and `path` to retrieve value from
    :ref:`Metadata <envoy_v3_api_msg_config.core.v3.Metadata>`.

    For example, for the following Metadata:

    .. code-block:: yaml

       filter_metadata:
         envoy.xxx:
           prop:
             foo: bar
             xyz:
               hello: envoy

    The following MetadataKey will retrieve a string value "bar" from the Metadata.

    .. code-block:: yaml

       key: envoy.xxx
       path:
       - key: prop
       - key: foo
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PathSegment(google.protobuf.message.Message):
        """Specifies the segment in a path to retrieve value from Metadata.
        Currently it is only supported to specify the key, i.e. field name, as one segment of a path.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        """If specified, use the key to retrieve the value in a Struct."""

        def __init__(self,
            *,
            key : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"key",b"key",u"segment",b"segment"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"segment",b"segment"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"segment",b"segment"]) -> typing.Optional[typing_extensions.Literal["key"]]: ...

    KEY_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    key: typing.Text = ...
    """The key name of Metadata to retrieve the Struct from the metadata.
    Typically, it represents a builtin subsystem or custom extension.
    """

    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MetadataKey.PathSegment]:
        """The path to retrieve the Value from the Struct. It can be a prefix or a full path,
        e.g. ``[prop, xyz]`` for a struct or ``[prop, foo]`` for a string in the example,
        which depends on the particular scenario.

        Note: Due to that only the key type segment is supported, the path can not specify a list
        unless the list is the last segment.
        """
        pass
    def __init__(self,
        *,
        key : typing.Text = ...,
        path : typing.Optional[typing.Iterable[global___MetadataKey.PathSegment]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"path",b"path"]) -> None: ...
global___MetadataKey = MetadataKey

class MetadataKind(google.protobuf.message.Message):
    """Describes what kind of metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Request(google.protobuf.message.Message):
        """Represents dynamic metadata associated with the request."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    class Route(google.protobuf.message.Message):
        """Represents metadata from :ref:`the route<envoy_v3_api_field_config.route.v3.Route.metadata>`."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    class Cluster(google.protobuf.message.Message):
        """Represents metadata from :ref:`the upstream cluster<envoy_v3_api_field_config.cluster.v3.Cluster.metadata>`."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    class Host(google.protobuf.message.Message):
        """Represents metadata from :ref:`the upstream
        host<envoy_v3_api_field_config.endpoint.v3.LbEndpoint.metadata>`.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    REQUEST_FIELD_NUMBER: builtins.int
    ROUTE_FIELD_NUMBER: builtins.int
    CLUSTER_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    @property
    def request(self) -> global___MetadataKind.Request:
        """Request kind of metadata."""
        pass
    @property
    def route(self) -> global___MetadataKind.Route:
        """Route kind of metadata."""
        pass
    @property
    def cluster(self) -> global___MetadataKind.Cluster:
        """Cluster kind of metadata."""
        pass
    @property
    def host(self) -> global___MetadataKind.Host:
        """Host kind of metadata."""
        pass
    def __init__(self,
        *,
        request : typing.Optional[global___MetadataKind.Request] = ...,
        route : typing.Optional[global___MetadataKind.Route] = ...,
        cluster : typing.Optional[global___MetadataKind.Cluster] = ...,
        host : typing.Optional[global___MetadataKind.Host] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cluster",b"cluster",u"host",b"host",u"kind",b"kind",u"request",b"request",u"route",b"route"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cluster",b"cluster",u"host",b"host",u"kind",b"kind",u"request",b"request",u"route",b"route"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"kind",b"kind"]) -> typing.Optional[typing_extensions.Literal["request","route","cluster","host"]]: ...
global___MetadataKind = MetadataKind
