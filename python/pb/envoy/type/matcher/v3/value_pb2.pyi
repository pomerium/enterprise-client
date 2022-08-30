"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import envoy.type.matcher.v3.number_pb2
import envoy.type.matcher.v3.string_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ValueMatcher(google.protobuf.message.Message):
    """[#protodoc-title: Value matcher]

    Specifies the way to match a ProtobufWkt::Value. Primitive values and ListValue are supported.
    StructValue is not supported and is always not matched.
    [#next-free-field: 7]
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class NullMatch(google.protobuf.message.Message):
        """NullMatch is an empty message to specify a null value."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    NULL_MATCH_FIELD_NUMBER: builtins.int
    DOUBLE_MATCH_FIELD_NUMBER: builtins.int
    STRING_MATCH_FIELD_NUMBER: builtins.int
    BOOL_MATCH_FIELD_NUMBER: builtins.int
    PRESENT_MATCH_FIELD_NUMBER: builtins.int
    LIST_MATCH_FIELD_NUMBER: builtins.int
    @property
    def null_match(self) -> global___ValueMatcher.NullMatch:
        """If specified, a match occurs if and only if the target value is a NullValue."""
    @property
    def double_match(self) -> envoy.type.matcher.v3.number_pb2.DoubleMatcher:
        """If specified, a match occurs if and only if the target value is a double value and is
        matched to this field.
        """
    @property
    def string_match(self) -> envoy.type.matcher.v3.string_pb2.StringMatcher:
        """If specified, a match occurs if and only if the target value is a string value and is
        matched to this field.
        """
    bool_match: builtins.bool
    """If specified, a match occurs if and only if the target value is a bool value and is equal
    to this field.
    """
    present_match: builtins.bool
    """If specified, value match will be performed based on whether the path is referring to a
    valid primitive value in the metadata. If the path is referring to a non-primitive value,
    the result is always not matched.
    """
    @property
    def list_match(self) -> global___ListMatcher:
        """If specified, a match occurs if and only if the target value is a list value and
        is matched to this field.
        """
    def __init__(
        self,
        *,
        null_match: global___ValueMatcher.NullMatch | None = ...,
        double_match: envoy.type.matcher.v3.number_pb2.DoubleMatcher | None = ...,
        string_match: envoy.type.matcher.v3.string_pb2.StringMatcher | None = ...,
        bool_match: builtins.bool = ...,
        present_match: builtins.bool = ...,
        list_match: global___ListMatcher | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool_match", b"bool_match", "double_match", b"double_match", "list_match", b"list_match", "match_pattern", b"match_pattern", "null_match", b"null_match", "present_match", b"present_match", "string_match", b"string_match"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool_match", b"bool_match", "double_match", b"double_match", "list_match", b"list_match", "match_pattern", b"match_pattern", "null_match", b"null_match", "present_match", b"present_match", "string_match", b"string_match"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["match_pattern", b"match_pattern"]) -> typing_extensions.Literal["null_match", "double_match", "string_match", "bool_match", "present_match", "list_match"] | None: ...

global___ValueMatcher = ValueMatcher

class ListMatcher(google.protobuf.message.Message):
    """Specifies the way to match a list value."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ONE_OF_FIELD_NUMBER: builtins.int
    @property
    def one_of(self) -> global___ValueMatcher:
        """If specified, at least one of the values in the list must match the value specified."""
    def __init__(
        self,
        *,
        one_of: global___ValueMatcher | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["match_pattern", b"match_pattern", "one_of", b"one_of"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["match_pattern", b"match_pattern", "one_of", b"one_of"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["match_pattern", b"match_pattern"]) -> typing_extensions.Literal["one_of"] | None: ...

global___ListMatcher = ListMatcher
