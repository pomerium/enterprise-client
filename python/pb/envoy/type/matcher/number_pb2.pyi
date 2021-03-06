"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import envoy.type.range_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DoubleMatcher(google.protobuf.message.Message):
    """[#protodoc-title: Number matcher]

    Specifies the way to match a double value.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RANGE_FIELD_NUMBER: builtins.int
    EXACT_FIELD_NUMBER: builtins.int
    @property
    def range(self) -> envoy.type.range_pb2.DoubleRange:
        """If specified, the input double value must be in the range specified here.
        Note: The range is using half-open interval semantics [start, end).
        """
        pass
    exact: builtins.float = ...
    """If specified, the input double value must be equal to the value specified here."""

    def __init__(self,
        *,
        range : typing.Optional[envoy.type.range_pb2.DoubleRange] = ...,
        exact : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"exact",b"exact",u"match_pattern",b"match_pattern",u"range",b"range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"exact",b"exact",u"match_pattern",b"match_pattern",u"range",b"range"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"match_pattern",b"match_pattern"]) -> typing.Optional[typing_extensions.Literal["range","exact"]]: ...
global___DoubleMatcher = DoubleMatcher
