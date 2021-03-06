"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RecoveryToken(google.protobuf.message.Message):
    """RecoveryToken is a recovery account for logging into the console without a
    functioning Pomerium proxy
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    namespace: typing.Text = ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    public_key: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        namespace : typing.Text = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        modified_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        expires_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        public_key : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"expires_at",b"expires_at",u"modified_at",b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"expires_at",b"expires_at",u"id",b"id",u"modified_at",b"modified_at",u"namespace",b"namespace",u"public_key",b"public_key"]) -> None: ...
global___RecoveryToken = RecoveryToken

class GroupInfo(google.protobuf.message.Message):
    """GroupInfo defines a directory group in the databroker"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    name: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id",u"name",b"name"]) -> None: ...
global___GroupInfo = GroupInfo

class UserInfo(google.protobuf.message.Message):
    """UserInfo defines the metadata for a directory user in the databroker"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class NamespaceRolesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    NAMESPACE_ROLES_FIELD_NUMBER: builtins.int
    PICTURE_URL_FIELD_NUMBER: builtins.int
    IS_IMPERSONATED_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    name: typing.Text = ...
    email: typing.Text = ...
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def namespace_roles(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    picture_url: typing.Text = ...
    is_impersonated: builtins.bool = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        email : typing.Text = ...,
        groups : typing.Optional[typing.Iterable[typing.Text]] = ...,
        namespace_roles : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        picture_url : typing.Text = ...,
        is_impersonated : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"email",b"email",u"groups",b"groups",u"id",b"id",u"is_impersonated",b"is_impersonated",u"name",b"name",u"namespace_roles",b"namespace_roles",u"picture_url",b"picture_url"]) -> None: ...
global___UserInfo = UserInfo

class GetUserInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_ID_FIELD_NUMBER: builtins.int
    user_id: typing.Text = ...
    def __init__(self,
        *,
        user_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_user_id",b"_user_id",u"user_id",b"user_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_user_id",b"_user_id",u"user_id",b"user_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_user_id",b"_user_id"]) -> typing.Optional[typing_extensions.Literal["user_id"]]: ...
global___GetUserInfoRequest = GetUserInfoRequest

class GetUserInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_INFO_FIELD_NUMBER: builtins.int
    @property
    def user_info(self) -> global___UserInfo: ...
    def __init__(self,
        *,
        user_info : typing.Optional[global___UserInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"user_info",b"user_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"user_info",b"user_info"]) -> None: ...
global___GetUserInfoResponse = GetUserInfoResponse

class QueryGroupsRequest(google.protobuf.message.Message):
    """QueryGroupsRequest defines the groups to retrieve"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    QUERY_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    query: typing.Text = ...
    offset: builtins.int = ...
    limit: builtins.int = ...
    def __init__(self,
        *,
        query : typing.Text = ...,
        offset : builtins.int = ...,
        limit : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"limit",b"limit",u"offset",b"offset",u"query",b"query"]) -> None: ...
global___QueryGroupsRequest = QueryGroupsRequest

class QueryGroupsResponse(google.protobuf.message.Message):
    """QueryGroupsResponse is the list of groups retrieved from a QueryGroupsRequest"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GROUPS_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GroupInfo]: ...
    total_count: builtins.int = ...
    def __init__(self,
        *,
        groups : typing.Optional[typing.Iterable[global___GroupInfo]] = ...,
        total_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"groups",b"groups",u"total_count",b"total_count"]) -> None: ...
global___QueryGroupsResponse = QueryGroupsResponse

class QueryUsersRequest(google.protobuf.message.Message):
    """QueryUsersRequest defines the users to retrieve"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    QUERY_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    query: typing.Text = ...
    """list Users with any fields that match the query"""

    offset: builtins.int = ...
    """list Users starting from an offset in the total list"""

    limit: builtins.int = ...
    """limit the number of User entries returned"""

    def __init__(self,
        *,
        query : typing.Text = ...,
        offset : builtins.int = ...,
        limit : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"limit",b"limit",u"offset",b"offset",u"query",b"query"]) -> None: ...
global___QueryUsersRequest = QueryUsersRequest

class QueryUsersResponse(google.protobuf.message.Message):
    """QueryUsersResponse is the list of users retrieved from a QueryUsersRequest"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USERS_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserInfo]: ...
    total_count: builtins.int = ...
    def __init__(self,
        *,
        users : typing.Optional[typing.Iterable[global___UserInfo]] = ...,
        total_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"total_count",b"total_count",u"users",b"users"]) -> None: ...
global___QueryUsersResponse = QueryUsersResponse

class PomeriumServiceAccount(google.protobuf.message.Message):
    """PomeriumServiceAccount defines the identity properties of a service account"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    ISSUED_AT_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    namespace_id: typing.Text = ...
    description: typing.Text = ...
    user_id: typing.Text = ...
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def issued_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        namespace_id : typing.Text = ...,
        description : typing.Text = ...,
        user_id : typing.Text = ...,
        expires_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        issued_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_description",b"_description",u"_namespace_id",b"_namespace_id",u"description",b"description",u"expires_at",b"expires_at",u"issued_at",b"issued_at",u"namespace_id",b"namespace_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_description",b"_description",u"_namespace_id",b"_namespace_id",u"description",b"description",u"expires_at",b"expires_at",u"id",b"id",u"issued_at",b"issued_at",u"namespace_id",b"namespace_id",u"user_id",b"user_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_description",b"_description"]) -> typing.Optional[typing_extensions.Literal["description"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_namespace_id",b"_namespace_id"]) -> typing.Optional[typing_extensions.Literal["namespace_id"]]: ...
global___PomeriumServiceAccount = PomeriumServiceAccount

class AddPomeriumServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def service_account(self) -> global___PomeriumServiceAccount: ...
    def __init__(self,
        *,
        service_account : typing.Optional[global___PomeriumServiceAccount] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"service_account",b"service_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"service_account",b"service_account"]) -> None: ...
global___AddPomeriumServiceAccountRequest = AddPomeriumServiceAccountRequest

class AddPomeriumServiceAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    JWT_FIELD_NUMBER: builtins.int
    @property
    def service_account(self) -> global___PomeriumServiceAccount: ...
    JWT: typing.Text = ...
    def __init__(self,
        *,
        service_account : typing.Optional[global___PomeriumServiceAccount] = ...,
        JWT : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"service_account",b"service_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"JWT",b"JWT",u"service_account",b"service_account"]) -> None: ...
global___AddPomeriumServiceAccountResponse = AddPomeriumServiceAccountResponse

class DeletePomeriumServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___DeletePomeriumServiceAccountRequest = DeletePomeriumServiceAccountRequest

class DeletePomeriumServiceAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___DeletePomeriumServiceAccountResponse = DeletePomeriumServiceAccountResponse

class GetPomeriumServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___GetPomeriumServiceAccountRequest = GetPomeriumServiceAccountRequest

class GetPomeriumServiceAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def service_account(self) -> global___PomeriumServiceAccount: ...
    def __init__(self,
        *,
        service_account : typing.Optional[global___PomeriumServiceAccount] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"service_account",b"service_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"service_account",b"service_account"]) -> None: ...
global___GetPomeriumServiceAccountResponse = GetPomeriumServiceAccountResponse

class ListPomeriumServiceAccountsRequest(google.protobuf.message.Message):
    """ListPomeriumServiceAccountsRequest specifies the service accounts to list"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    def __init__(self,
        *,
        namespace : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespace",b"namespace"]) -> None: ...
global___ListPomeriumServiceAccountsRequest = ListPomeriumServiceAccountsRequest

class ListPomeriumServiceAccountsResponse(google.protobuf.message.Message):
    """ListPomeriumServiceAccountsResponse is the list of service accounts found for
    a ListPomeriumServiceAccountsRequest
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVICE_ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def service_accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PomeriumServiceAccount]: ...
    def __init__(self,
        *,
        service_accounts : typing.Optional[typing.Iterable[global___PomeriumServiceAccount]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"service_accounts",b"service_accounts"]) -> None: ...
global___ListPomeriumServiceAccountsResponse = ListPomeriumServiceAccountsResponse

class PomeriumSession(google.protobuf.message.Message):
    """PomeriumSession defines a user session from the databroker"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Group(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ID_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        EMAIL_FIELD_NUMBER: builtins.int
        id: typing.Text = ...
        name: typing.Text = ...
        email: typing.Text = ...
        def __init__(self,
            *,
            id : typing.Text = ...,
            name : typing.Text = ...,
            email : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"email",b"email",u"id",b"id",u"name",b"name"]) -> None: ...

    class User(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ID_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        EMAIL_FIELD_NUMBER: builtins.int
        id: typing.Text = ...
        name: typing.Text = ...
        email: typing.Text = ...
        def __init__(self,
            *,
            id : typing.Text = ...,
            name : typing.Text = ...,
            email : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"email",b"email",u"id",b"id",u"name",b"name"]) -> None: ...

    class ClaimsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> google.protobuf.struct_pb2.ListValue: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[google.protobuf.struct_pb2.ListValue] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    ISSUED_AT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    AUDIENCE_FIELD_NUMBER: builtins.int
    CLAIMS_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    @property
    def user(self) -> global___PomeriumSession.User: ...
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PomeriumSession.Group]: ...
    issuer: typing.Text = ...
    @property
    def issued_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def audience(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def claims(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, google.protobuf.struct_pb2.ListValue]: ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        user : typing.Optional[global___PomeriumSession.User] = ...,
        groups : typing.Optional[typing.Iterable[global___PomeriumSession.Group]] = ...,
        issuer : typing.Text = ...,
        issued_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        expires_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        audience : typing.Optional[typing.Iterable[typing.Text]] = ...,
        claims : typing.Optional[typing.Mapping[typing.Text, google.protobuf.struct_pb2.ListValue]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"expires_at",b"expires_at",u"issued_at",b"issued_at",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"audience",b"audience",u"claims",b"claims",u"expires_at",b"expires_at",u"groups",b"groups",u"id",b"id",u"issued_at",b"issued_at",u"issuer",b"issuer",u"user",b"user"]) -> None: ...
global___PomeriumSession = PomeriumSession

class DeletePomeriumSessionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___DeletePomeriumSessionRequest = DeletePomeriumSessionRequest

class DeletePomeriumSessionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___DeletePomeriumSessionResponse = DeletePomeriumSessionResponse

class GetPomeriumSessionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___GetPomeriumSessionRequest = GetPomeriumSessionRequest

class GetPomeriumSessionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SESSION_FIELD_NUMBER: builtins.int
    ASSOCIATED_SESSIONS_FIELD_NUMBER: builtins.int
    @property
    def session(self) -> global___PomeriumSession: ...
    @property
    def associated_sessions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PomeriumSession]: ...
    def __init__(self,
        *,
        session : typing.Optional[global___PomeriumSession] = ...,
        associated_sessions : typing.Optional[typing.Iterable[global___PomeriumSession]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"session",b"session"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"associated_sessions",b"associated_sessions",u"session",b"session"]) -> None: ...
global___GetPomeriumSessionResponse = GetPomeriumSessionResponse

class ListPomeriumSessionsRequest(google.protobuf.message.Message):
    """ListPomeriumSessionsRequest specifies the sessions to list"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    QUERY_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    query: typing.Text = ...
    """list Sessions with any fields that contain the query string"""

    offset: builtins.int = ...
    """list Sessions starting from an offset in the total list"""

    limit: builtins.int = ...
    """limit the number of Session entries returned"""

    order_by: typing.Text = ...
    """sort the Sessions by newest, oldest or name"""

    user_id: typing.Text = ...
    def __init__(self,
        *,
        query : typing.Text = ...,
        offset : builtins.int = ...,
        limit : builtins.int = ...,
        order_by : typing.Text = ...,
        user_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_limit",b"_limit",u"_offset",b"_offset",u"_order_by",b"_order_by",u"_query",b"_query",u"_user_id",b"_user_id",u"limit",b"limit",u"offset",b"offset",u"order_by",b"order_by",u"query",b"query",u"user_id",b"user_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_limit",b"_limit",u"_offset",b"_offset",u"_order_by",b"_order_by",u"_query",b"_query",u"_user_id",b"_user_id",u"limit",b"limit",u"offset",b"offset",u"order_by",b"order_by",u"query",b"query",u"user_id",b"user_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_limit",b"_limit"]) -> typing.Optional[typing_extensions.Literal["limit"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_offset",b"_offset"]) -> typing.Optional[typing_extensions.Literal["offset"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_order_by",b"_order_by"]) -> typing.Optional[typing_extensions.Literal["order_by"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_query",b"_query"]) -> typing.Optional[typing_extensions.Literal["query"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_user_id",b"_user_id"]) -> typing.Optional[typing_extensions.Literal["user_id"]]: ...
global___ListPomeriumSessionsRequest = ListPomeriumSessionsRequest

class ListPomeriumSessionsResponse(google.protobuf.message.Message):
    """ListPomeriumSessionsResponse is the sessions found for a
    ListPomeriumSessionsRequest
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SESSIONS_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    @property
    def sessions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PomeriumSession]: ...
    total_count: builtins.int = ...
    def __init__(self,
        *,
        sessions : typing.Optional[typing.Iterable[global___PomeriumSession]] = ...,
        total_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"sessions",b"sessions",u"total_count",b"total_count"]) -> None: ...
global___ListPomeriumSessionsResponse = ListPomeriumSessionsResponse

class ImpersonateRequest(google.protobuf.message.Message):
    """ImpersonateRequest defines the identity information to impersonate"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SESSION_ID_FIELD_NUMBER: builtins.int
    session_id: typing.Text = ...
    def __init__(self,
        *,
        session_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"session_id",b"session_id"]) -> None: ...
global___ImpersonateRequest = ImpersonateRequest

class ImpersonateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ImpersonateResponse = ImpersonateResponse
