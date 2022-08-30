"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class IDToken(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISSUER_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    ISSUED_AT_FIELD_NUMBER: builtins.int
    RAW_FIELD_NUMBER: builtins.int
    issuer: builtins.str
    subject: builtins.str
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def issued_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    raw: builtins.str
    def __init__(
        self,
        *,
        issuer: builtins.str = ...,
        subject: builtins.str = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        issued_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        raw: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expires_at", b"expires_at", "issued_at", b"issued_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expires_at", b"expires_at", "issued_at", b"issued_at", "issuer", b"issuer", "raw", b"raw", "subject", b"subject"]) -> None: ...

global___IDToken = IDToken

class OAuthToken(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    TOKEN_TYPE_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    REFRESH_TOKEN_FIELD_NUMBER: builtins.int
    access_token: builtins.str
    token_type: builtins.str
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    refresh_token: builtins.str
    def __init__(
        self,
        *,
        access_token: builtins.str = ...,
        token_type: builtins.str = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        refresh_token: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_token", b"access_token", "expires_at", b"expires_at", "refresh_token", b"refresh_token", "token_type", b"token_type"]) -> None: ...

global___OAuthToken = OAuthToken

class Session(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DeviceCredential(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_ID_FIELD_NUMBER: builtins.int
        UNAVAILABLE_FIELD_NUMBER: builtins.int
        ID_FIELD_NUMBER: builtins.int
        type_id: builtins.str
        @property
        def unavailable(self) -> google.protobuf.empty_pb2.Empty: ...
        id: builtins.str
        def __init__(
            self,
            *,
            type_id: builtins.str = ...,
            unavailable: google.protobuf.empty_pb2.Empty | None = ...,
            id: builtins.str = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["credential", b"credential", "id", b"id", "unavailable", b"unavailable"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["credential", b"credential", "id", b"id", "type_id", b"type_id", "unavailable", b"unavailable"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["credential", b"credential"]) -> typing_extensions.Literal["unavailable", "id"] | None: ...

    class ClaimsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> google.protobuf.struct_pb2.ListValue: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: google.protobuf.struct_pb2.ListValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    DEVICE_CREDENTIALS_FIELD_NUMBER: builtins.int
    ISSUED_AT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    ACCESSED_AT_FIELD_NUMBER: builtins.int
    ID_TOKEN_FIELD_NUMBER: builtins.int
    OAUTH_TOKEN_FIELD_NUMBER: builtins.int
    CLAIMS_FIELD_NUMBER: builtins.int
    AUDIENCE_FIELD_NUMBER: builtins.int
    IMPERSONATE_SESSION_ID_FIELD_NUMBER: builtins.int
    version: builtins.str
    id: builtins.str
    user_id: builtins.str
    @property
    def device_credentials(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Session.DeviceCredential]: ...
    @property
    def issued_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def accessed_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def id_token(self) -> global___IDToken: ...
    @property
    def oauth_token(self) -> global___OAuthToken: ...
    @property
    def claims(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, google.protobuf.struct_pb2.ListValue]: ...
    @property
    def audience(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    impersonate_session_id: builtins.str
    def __init__(
        self,
        *,
        version: builtins.str = ...,
        id: builtins.str = ...,
        user_id: builtins.str = ...,
        device_credentials: collections.abc.Iterable[global___Session.DeviceCredential] | None = ...,
        issued_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        accessed_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id_token: global___IDToken | None = ...,
        oauth_token: global___OAuthToken | None = ...,
        claims: collections.abc.Mapping[builtins.str, google.protobuf.struct_pb2.ListValue] | None = ...,
        audience: collections.abc.Iterable[builtins.str] | None = ...,
        impersonate_session_id: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_impersonate_session_id", b"_impersonate_session_id", "accessed_at", b"accessed_at", "expires_at", b"expires_at", "id_token", b"id_token", "impersonate_session_id", b"impersonate_session_id", "issued_at", b"issued_at", "oauth_token", b"oauth_token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_impersonate_session_id", b"_impersonate_session_id", "accessed_at", b"accessed_at", "audience", b"audience", "claims", b"claims", "device_credentials", b"device_credentials", "expires_at", b"expires_at", "id", b"id", "id_token", b"id_token", "impersonate_session_id", b"impersonate_session_id", "issued_at", b"issued_at", "oauth_token", b"oauth_token", "user_id", b"user_id", "version", b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_impersonate_session_id", b"_impersonate_session_id"]) -> typing_extensions.Literal["impersonate_session_id"] | None: ...

global___Session = Session
