"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import namespaces_pb2

class NamespaceServiceStub:
    """NamespaceService manages namespaces"""

    def __init__(self, channel: grpc.Channel) -> None: ...
    DeleteNamespace: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.DeleteNamespaceRequest,
        namespaces_pb2.DeleteNamespaceResponse,
    ]
    """DeleteNamespace deletes a namespace"""
    GetNamespace: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.GetNamespaceRequest,
        namespaces_pb2.GetNamespaceResponse,
    ]
    """GetNamespace retrieves a namespace"""
    ListNamespaces: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.ListNamespacesRequest,
        namespaces_pb2.ListNamespacesResponse,
    ]
    """ListNamespaces lists all namespaces"""
    SetNamespace: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.SetNamespaceRequest,
        namespaces_pb2.SetNamespaceResponse,
    ]
    """SetNamespace creates a namespace or, if the id is specified, updates an
    existing namespace
    """

class NamespaceServiceServicer(metaclass=abc.ABCMeta):
    """NamespaceService manages namespaces"""

    @abc.abstractmethod
    def DeleteNamespace(
        self,
        request: namespaces_pb2.DeleteNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.DeleteNamespaceResponse:
        """DeleteNamespace deletes a namespace"""
    @abc.abstractmethod
    def GetNamespace(
        self,
        request: namespaces_pb2.GetNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.GetNamespaceResponse:
        """GetNamespace retrieves a namespace"""
    @abc.abstractmethod
    def ListNamespaces(
        self,
        request: namespaces_pb2.ListNamespacesRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.ListNamespacesResponse:
        """ListNamespaces lists all namespaces"""
    @abc.abstractmethod
    def SetNamespace(
        self,
        request: namespaces_pb2.SetNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.SetNamespaceResponse:
        """SetNamespace creates a namespace or, if the id is specified, updates an
        existing namespace
        """

def add_NamespaceServiceServicer_to_server(servicer: NamespaceServiceServicer, server: grpc.Server) -> None: ...

class NamespacePermissionServiceStub:
    """NamespacePermissionService manages permissions set on namespaces"""

    def __init__(self, channel: grpc.Channel) -> None: ...
    DeleteNamespacePermission: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.DeleteNamespacePermissionRequest,
        namespaces_pb2.DeleteNamespacePermissionResponse,
    ]
    """DeleteNamespacePermission removes an existing permission definition"""
    GetNamespacePermission: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.GetNamespacePermissionRequest,
        namespaces_pb2.GetNamespacePermissionResponse,
    ]
    """GetNamespacePermission retrieves an existing permission definition"""
    ListNamespacePermissions: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.ListNamespacePermissionsRequest,
        namespaces_pb2.ListNamespacePermissionsResponse,
    ]
    """ListNamespacePermissions retrieves existing permissions for all namespaces"""
    ListNamespacePermissionGroups: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.ListNamespacePermissionGroupsRequest,
        namespaces_pb2.ListNamespacePermissionGroupsResponse,
    ]
    """ListNamespacePermissionGroups retrieves existing group based permissions on
    a namespace
    """
    ListNamespacePermissionUsers: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.ListNamespacePermissionUsersRequest,
        namespaces_pb2.ListNamespacePermissionUsersResponse,
    ]
    """ListNamespacePermissionUsers retrieves existing user based permissions on a
    namespace
    """
    SetNamespacePermission: grpc.UnaryUnaryMultiCallable[
        namespaces_pb2.SetNamespacePermissionRequest,
        namespaces_pb2.SetNamespacePermissionResponse,
    ]
    """SetNamespacePermission set a new permission definition on a namespace"""

class NamespacePermissionServiceServicer(metaclass=abc.ABCMeta):
    """NamespacePermissionService manages permissions set on namespaces"""

    @abc.abstractmethod
    def DeleteNamespacePermission(
        self,
        request: namespaces_pb2.DeleteNamespacePermissionRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.DeleteNamespacePermissionResponse:
        """DeleteNamespacePermission removes an existing permission definition"""
    @abc.abstractmethod
    def GetNamespacePermission(
        self,
        request: namespaces_pb2.GetNamespacePermissionRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.GetNamespacePermissionResponse:
        """GetNamespacePermission retrieves an existing permission definition"""
    @abc.abstractmethod
    def ListNamespacePermissions(
        self,
        request: namespaces_pb2.ListNamespacePermissionsRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.ListNamespacePermissionsResponse:
        """ListNamespacePermissions retrieves existing permissions for all namespaces"""
    @abc.abstractmethod
    def ListNamespacePermissionGroups(
        self,
        request: namespaces_pb2.ListNamespacePermissionGroupsRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.ListNamespacePermissionGroupsResponse:
        """ListNamespacePermissionGroups retrieves existing group based permissions on
        a namespace
        """
    @abc.abstractmethod
    def ListNamespacePermissionUsers(
        self,
        request: namespaces_pb2.ListNamespacePermissionUsersRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.ListNamespacePermissionUsersResponse:
        """ListNamespacePermissionUsers retrieves existing user based permissions on a
        namespace
        """
    @abc.abstractmethod
    def SetNamespacePermission(
        self,
        request: namespaces_pb2.SetNamespacePermissionRequest,
        context: grpc.ServicerContext,
    ) -> namespaces_pb2.SetNamespacePermissionResponse:
        """SetNamespacePermission set a new permission definition on a namespace"""

def add_NamespacePermissionServiceServicer_to_server(servicer: NamespacePermissionServiceServicer, server: grpc.Server) -> None: ...
