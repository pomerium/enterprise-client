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
import xds.core.v3.cidr_pb2
import xds.type.matcher.v3.matcher_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class IPMatcher(google.protobuf.message.Message):
    """[#protodoc-title: IP matcher]

    Matches a specific IP address against a set of possibly overlapping subnets using a trie.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class IPRangeMatcher(google.protobuf.message.Message):
        """Specifies an optional list of IP address ranges and a match action."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        RANGES_FIELD_NUMBER: builtins.int
        ON_MATCH_FIELD_NUMBER: builtins.int
        EXCLUSIVE_FIELD_NUMBER: builtins.int
        @property
        def ranges(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[xds.core.v3.cidr_pb2.CidrRange]:
            """A non-empty set of CIDR ranges."""
            pass
        @property
        def on_match(self) -> xds.type.matcher.v3.matcher_pb2.Matcher.OnMatch:
            """Match action to apply when the IP address is within one of the CIDR ranges."""
            pass
        exclusive: builtins.bool = ...
        """Indicates whether this match option should be considered if there is a
        more specific matcher. Exclusive matchers are not selected whenever a
        more specific matcher exists (e.g. matcher with a longer prefix) even
        when the more specific matcher fails its nested match condition.
        Non-exclusive matchers are considered if the more specific matcher
        exists but its nested match condition does not entirely match.
        Non-exclusive matchers are selected in the order of their specificity
        first (longest prefix first), then the order of declaration next.

        For example, consider two range matchers: an exclusive matcher *X* on
        ``0.0.0.0/0`` and a matcher *Y* on ``192.0.0.0/2`` with a nested match
        condition *Z*. For the input IP ``192.168.0.1`` matcher *Y* is the most
        specific. If its nested match condition *Z* does not accept the input,
        then the less specific matcher *X* does not apply either despite the
        input being within the range, because matcher *X* is exclusive.

        The opposite is true if matcher *X* is not marked as exclusive. In that
        case matcher *X* always matches whenever matcher "*Y* rejects the input.
        """

        def __init__(self,
            *,
            ranges : typing.Optional[typing.Iterable[xds.core.v3.cidr_pb2.CidrRange]] = ...,
            on_match : typing.Optional[xds.type.matcher.v3.matcher_pb2.Matcher.OnMatch] = ...,
            exclusive : builtins.bool = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"on_match",b"on_match"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"exclusive",b"exclusive",u"on_match",b"on_match",u"ranges",b"ranges"]) -> None: ...

    RANGE_MATCHERS_FIELD_NUMBER: builtins.int
    @property
    def range_matchers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IPMatcher.IPRangeMatcher]:
        """Match IP address by CIDR ranges."""
        pass
    def __init__(self,
        *,
        range_matchers : typing.Optional[typing.Iterable[global___IPMatcher.IPRangeMatcher]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"range_matchers",b"range_matchers"]) -> None: ...
global___IPMatcher = IPMatcher
