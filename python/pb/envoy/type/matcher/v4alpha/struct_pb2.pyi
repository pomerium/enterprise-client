"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import envoy.type.matcher.v4alpha.value_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class StructMatcher(google.protobuf.message.Message):
    """[#protodoc-title: Struct matcher]

    StructMatcher provides a general interface to check if a given value is matched in
    google.protobuf.Struct. It uses `path` to retrieve the value
    from the struct and then check if it's matched to the specified value.

    For example, for the following Struct:

    .. code-block:: yaml

           fields:
             a:
               struct_value:
                 fields:
                   b:
                     struct_value:
                       fields:
                         c:
                           string_value: pro
                   t:
                     list_value:
                       values:
                         - string_value: m
                         - string_value: n

    The following MetadataMatcher is matched as the path [a, b, c] will retrieve a string value "pro"
    from the Metadata which is matched to the specified prefix match.

    .. code-block:: yaml

       path:
       - key: a
       - key: b
       - key: c
       value:
         string_match:
           prefix: pr

    The following StructMatcher is matched as the code will match one of the string values in the
    list at the path [a, t].

    .. code-block:: yaml

       path:
       - key: a
       - key: t
       value:
         list_match:
           one_of:
             string_match:
               exact: m

    An example use of StructMatcher is to match metadata in envoy.v*.core.Node.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PathSegment(google.protobuf.message.Message):
        """Specifies the segment in a path to retrieve value from Struct."""
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

    PATH_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StructMatcher.PathSegment]:
        """The path to retrieve the Value from the Struct."""
        pass
    @property
    def value(self) -> envoy.type.matcher.v4alpha.value_pb2.ValueMatcher:
        """The StructMatcher is matched if the value retrieved by path is matched to this value."""
        pass
    def __init__(self,
        *,
        path : typing.Optional[typing.Iterable[global___StructMatcher.PathSegment]] = ...,
        value : typing.Optional[envoy.type.matcher.v4alpha.value_pb2.ValueMatcher] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"path",b"path",u"value",b"value"]) -> None: ...
global___StructMatcher = StructMatcher
