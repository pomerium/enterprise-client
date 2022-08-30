"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import xds.core.v3.extension_pb2
import xds.type.matcher.v3.string_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Matcher(google.protobuf.message.Message):
    """[#protodoc-title: Unified Matcher API]

    A matcher, which may traverse a matching tree in order to result in a match action.
    During matching, the tree will be traversed until a match is found, or if no match
    is found the action specified by the most specific on_no_match will be evaluated.
    As an on_no_match might result in another matching tree being evaluated, this process
    might repeat several times until the final OnMatch (or no match) is decided.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class OnMatch(google.protobuf.message.Message):
        """What to do if a match is successful."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MATCHER_FIELD_NUMBER: builtins.int
        ACTION_FIELD_NUMBER: builtins.int
        @property
        def matcher(self) -> global___Matcher:
            """Nested matcher to evaluate.
            If the nested matcher does not match and does not specify
            on_no_match, then this matcher is considered not to have
            matched, even if a predicate at this level or above returned
            true.
            """
        @property
        def action(self) -> xds.core.v3.extension_pb2.TypedExtensionConfig:
            """Protocol-specific action to take."""
        def __init__(
            self,
            *,
            matcher: global___Matcher | None = ...,
            action: xds.core.v3.extension_pb2.TypedExtensionConfig | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["action", b"action", "matcher", b"matcher", "on_match", b"on_match"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "matcher", b"matcher", "on_match", b"on_match"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["on_match", b"on_match"]) -> typing_extensions.Literal["matcher", "action"] | None: ...

    class MatcherList(google.protobuf.message.Message):
        """A linear list of field matchers.
        The field matchers are evaluated in order, and the first match
        wins.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class Predicate(google.protobuf.message.Message):
            """Predicate to determine if a match is successful."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            class SinglePredicate(google.protobuf.message.Message):
                """Predicate for a single input field."""

                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                INPUT_FIELD_NUMBER: builtins.int
                VALUE_MATCH_FIELD_NUMBER: builtins.int
                CUSTOM_MATCH_FIELD_NUMBER: builtins.int
                @property
                def input(self) -> xds.core.v3.extension_pb2.TypedExtensionConfig:
                    """Protocol-specific specification of input field to match on.
                    [#extension-category: envoy.matching.common_inputs]
                    """
                @property
                def value_match(self) -> xds.type.matcher.v3.string_pb2.StringMatcher:
                    """Built-in string matcher."""
                @property
                def custom_match(self) -> xds.core.v3.extension_pb2.TypedExtensionConfig:
                    """Extension for custom matching logic.
                    [#extension-category: envoy.matching.input_matchers]
                    """
                def __init__(
                    self,
                    *,
                    input: xds.core.v3.extension_pb2.TypedExtensionConfig | None = ...,
                    value_match: xds.type.matcher.v3.string_pb2.StringMatcher | None = ...,
                    custom_match: xds.core.v3.extension_pb2.TypedExtensionConfig | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal["custom_match", b"custom_match", "input", b"input", "matcher", b"matcher", "value_match", b"value_match"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal["custom_match", b"custom_match", "input", b"input", "matcher", b"matcher", "value_match", b"value_match"]) -> None: ...
                def WhichOneof(self, oneof_group: typing_extensions.Literal["matcher", b"matcher"]) -> typing_extensions.Literal["value_match", "custom_match"] | None: ...

            class PredicateList(google.protobuf.message.Message):
                """A list of two or more matchers. Used to allow using a list within a oneof."""

                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                PREDICATE_FIELD_NUMBER: builtins.int
                @property
                def predicate(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Matcher.MatcherList.Predicate]: ...
                def __init__(
                    self,
                    *,
                    predicate: collections.abc.Iterable[global___Matcher.MatcherList.Predicate] | None = ...,
                ) -> None: ...
                def ClearField(self, field_name: typing_extensions.Literal["predicate", b"predicate"]) -> None: ...

            SINGLE_PREDICATE_FIELD_NUMBER: builtins.int
            OR_MATCHER_FIELD_NUMBER: builtins.int
            AND_MATCHER_FIELD_NUMBER: builtins.int
            NOT_MATCHER_FIELD_NUMBER: builtins.int
            @property
            def single_predicate(self) -> global___Matcher.MatcherList.Predicate.SinglePredicate:
                """A single predicate to evaluate."""
            @property
            def or_matcher(self) -> global___Matcher.MatcherList.Predicate.PredicateList:
                """A list of predicates to be OR-ed together."""
            @property
            def and_matcher(self) -> global___Matcher.MatcherList.Predicate.PredicateList:
                """A list of predicates to be AND-ed together."""
            @property
            def not_matcher(self) -> global___Matcher.MatcherList.Predicate:
                """The invert of a predicate"""
            def __init__(
                self,
                *,
                single_predicate: global___Matcher.MatcherList.Predicate.SinglePredicate | None = ...,
                or_matcher: global___Matcher.MatcherList.Predicate.PredicateList | None = ...,
                and_matcher: global___Matcher.MatcherList.Predicate.PredicateList | None = ...,
                not_matcher: global___Matcher.MatcherList.Predicate | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["and_matcher", b"and_matcher", "match_type", b"match_type", "not_matcher", b"not_matcher", "or_matcher", b"or_matcher", "single_predicate", b"single_predicate"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["and_matcher", b"and_matcher", "match_type", b"match_type", "not_matcher", b"not_matcher", "or_matcher", b"or_matcher", "single_predicate", b"single_predicate"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions.Literal["match_type", b"match_type"]) -> typing_extensions.Literal["single_predicate", "or_matcher", "and_matcher", "not_matcher"] | None: ...

        class FieldMatcher(google.protobuf.message.Message):
            """An individual matcher."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            PREDICATE_FIELD_NUMBER: builtins.int
            ON_MATCH_FIELD_NUMBER: builtins.int
            @property
            def predicate(self) -> global___Matcher.MatcherList.Predicate:
                """Determines if the match succeeds."""
            @property
            def on_match(self) -> global___Matcher.OnMatch:
                """What to do if the match succeeds."""
            def __init__(
                self,
                *,
                predicate: global___Matcher.MatcherList.Predicate | None = ...,
                on_match: global___Matcher.OnMatch | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["on_match", b"on_match", "predicate", b"predicate"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["on_match", b"on_match", "predicate", b"predicate"]) -> None: ...

        MATCHERS_FIELD_NUMBER: builtins.int
        @property
        def matchers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Matcher.MatcherList.FieldMatcher]:
            """A list of matchers. First match wins."""
        def __init__(
            self,
            *,
            matchers: collections.abc.Iterable[global___Matcher.MatcherList.FieldMatcher] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["matchers", b"matchers"]) -> None: ...

    class MatcherTree(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class MatchMap(google.protobuf.message.Message):
            """A map of configured matchers. Used to allow using a map within a oneof."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            class MapEntry(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                KEY_FIELD_NUMBER: builtins.int
                VALUE_FIELD_NUMBER: builtins.int
                key: builtins.str
                @property
                def value(self) -> global___Matcher.OnMatch: ...
                def __init__(
                    self,
                    *,
                    key: builtins.str = ...,
                    value: global___Matcher.OnMatch | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

            MAP_FIELD_NUMBER: builtins.int
            @property
            def map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Matcher.OnMatch]: ...
            def __init__(
                self,
                *,
                map: collections.abc.Mapping[builtins.str, global___Matcher.OnMatch] | None = ...,
            ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["map", b"map"]) -> None: ...

        INPUT_FIELD_NUMBER: builtins.int
        EXACT_MATCH_MAP_FIELD_NUMBER: builtins.int
        PREFIX_MATCH_MAP_FIELD_NUMBER: builtins.int
        CUSTOM_MATCH_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> xds.core.v3.extension_pb2.TypedExtensionConfig:
            """Protocol-specific specification of input field to match on."""
        @property
        def exact_match_map(self) -> global___Matcher.MatcherTree.MatchMap: ...
        @property
        def prefix_match_map(self) -> global___Matcher.MatcherTree.MatchMap:
            """Longest matching prefix wins."""
        @property
        def custom_match(self) -> xds.core.v3.extension_pb2.TypedExtensionConfig:
            """Extension for custom matching logic."""
        def __init__(
            self,
            *,
            input: xds.core.v3.extension_pb2.TypedExtensionConfig | None = ...,
            exact_match_map: global___Matcher.MatcherTree.MatchMap | None = ...,
            prefix_match_map: global___Matcher.MatcherTree.MatchMap | None = ...,
            custom_match: xds.core.v3.extension_pb2.TypedExtensionConfig | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["custom_match", b"custom_match", "exact_match_map", b"exact_match_map", "input", b"input", "prefix_match_map", b"prefix_match_map", "tree_type", b"tree_type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["custom_match", b"custom_match", "exact_match_map", b"exact_match_map", "input", b"input", "prefix_match_map", b"prefix_match_map", "tree_type", b"tree_type"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["tree_type", b"tree_type"]) -> typing_extensions.Literal["exact_match_map", "prefix_match_map", "custom_match"] | None: ...

    MATCHER_LIST_FIELD_NUMBER: builtins.int
    MATCHER_TREE_FIELD_NUMBER: builtins.int
    ON_NO_MATCH_FIELD_NUMBER: builtins.int
    @property
    def matcher_list(self) -> global___Matcher.MatcherList:
        """A linear list of matchers to evaluate."""
    @property
    def matcher_tree(self) -> global___Matcher.MatcherTree:
        """A match tree to evaluate."""
    @property
    def on_no_match(self) -> global___Matcher.OnMatch:
        """Optional OnMatch to use if no matcher above matched (e.g., if there are no matchers specified
        above, or if none of the matches specified above succeeded).
        If no matcher above matched and this field is not populated, the match will be considered unsuccessful.
        """
    def __init__(
        self,
        *,
        matcher_list: global___Matcher.MatcherList | None = ...,
        matcher_tree: global___Matcher.MatcherTree | None = ...,
        on_no_match: global___Matcher.OnMatch | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["matcher_list", b"matcher_list", "matcher_tree", b"matcher_tree", "matcher_type", b"matcher_type", "on_no_match", b"on_no_match"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["matcher_list", b"matcher_list", "matcher_tree", b"matcher_tree", "matcher_type", b"matcher_type", "on_no_match", b"on_no_match"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["matcher_type", b"matcher_type"]) -> typing_extensions.Literal["matcher_list", "matcher_tree"] | None: ...

global___Matcher = Matcher
