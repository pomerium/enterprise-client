# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import namespaces_pb2 as namespaces__pb2


class NamespaceServiceStub(object):
    """NamespaceService manages namespaces
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeleteNamespace = channel.unary_unary(
                '/pomerium.dashboard.NamespaceService/DeleteNamespace',
                request_serializer=namespaces__pb2.DeleteNamespaceRequest.SerializeToString,
                response_deserializer=namespaces__pb2.DeleteNamespaceResponse.FromString,
                )
        self.GetNamespace = channel.unary_unary(
                '/pomerium.dashboard.NamespaceService/GetNamespace',
                request_serializer=namespaces__pb2.GetNamespaceRequest.SerializeToString,
                response_deserializer=namespaces__pb2.GetNamespaceResponse.FromString,
                )
        self.ListNamespaces = channel.unary_unary(
                '/pomerium.dashboard.NamespaceService/ListNamespaces',
                request_serializer=namespaces__pb2.ListNamespacesRequest.SerializeToString,
                response_deserializer=namespaces__pb2.ListNamespacesResponse.FromString,
                )
        self.SetNamespace = channel.unary_unary(
                '/pomerium.dashboard.NamespaceService/SetNamespace',
                request_serializer=namespaces__pb2.SetNamespaceRequest.SerializeToString,
                response_deserializer=namespaces__pb2.SetNamespaceResponse.FromString,
                )


class NamespaceServiceServicer(object):
    """NamespaceService manages namespaces
    """

    def DeleteNamespace(self, request, context):
        """DeleteNamespace deletes a namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNamespace(self, request, context):
        """GetNamespace retrieves a namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamespaces(self, request, context):
        """ListNamespaces lists all namespaces
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNamespace(self, request, context):
        """SetNamespace creates a namespace or, if the id is specified, updates an
        existing namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NamespaceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeleteNamespace': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNamespace,
                    request_deserializer=namespaces__pb2.DeleteNamespaceRequest.FromString,
                    response_serializer=namespaces__pb2.DeleteNamespaceResponse.SerializeToString,
            ),
            'GetNamespace': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNamespace,
                    request_deserializer=namespaces__pb2.GetNamespaceRequest.FromString,
                    response_serializer=namespaces__pb2.GetNamespaceResponse.SerializeToString,
            ),
            'ListNamespaces': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamespaces,
                    request_deserializer=namespaces__pb2.ListNamespacesRequest.FromString,
                    response_serializer=namespaces__pb2.ListNamespacesResponse.SerializeToString,
            ),
            'SetNamespace': grpc.unary_unary_rpc_method_handler(
                    servicer.SetNamespace,
                    request_deserializer=namespaces__pb2.SetNamespaceRequest.FromString,
                    response_serializer=namespaces__pb2.SetNamespaceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.NamespaceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NamespaceService(object):
    """NamespaceService manages namespaces
    """

    @staticmethod
    def DeleteNamespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespaceService/DeleteNamespace',
            namespaces__pb2.DeleteNamespaceRequest.SerializeToString,
            namespaces__pb2.DeleteNamespaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNamespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespaceService/GetNamespace',
            namespaces__pb2.GetNamespaceRequest.SerializeToString,
            namespaces__pb2.GetNamespaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamespaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespaceService/ListNamespaces',
            namespaces__pb2.ListNamespacesRequest.SerializeToString,
            namespaces__pb2.ListNamespacesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNamespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespaceService/SetNamespace',
            namespaces__pb2.SetNamespaceRequest.SerializeToString,
            namespaces__pb2.SetNamespaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NamespacePermissionServiceStub(object):
    """NamespacePermissionService manages permissions set on namespaces
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeleteNamespacePermission = channel.unary_unary(
                '/pomerium.dashboard.NamespacePermissionService/DeleteNamespacePermission',
                request_serializer=namespaces__pb2.DeleteNamespacePermissionRequest.SerializeToString,
                response_deserializer=namespaces__pb2.DeleteNamespacePermissionResponse.FromString,
                )
        self.GetNamespacePermission = channel.unary_unary(
                '/pomerium.dashboard.NamespacePermissionService/GetNamespacePermission',
                request_serializer=namespaces__pb2.GetNamespacePermissionRequest.SerializeToString,
                response_deserializer=namespaces__pb2.GetNamespacePermissionResponse.FromString,
                )
        self.ListNamespacePermissions = channel.unary_unary(
                '/pomerium.dashboard.NamespacePermissionService/ListNamespacePermissions',
                request_serializer=namespaces__pb2.ListNamespacePermissionsRequest.SerializeToString,
                response_deserializer=namespaces__pb2.ListNamespacePermissionsResponse.FromString,
                )
        self.ListNamespacePermissionGroups = channel.unary_unary(
                '/pomerium.dashboard.NamespacePermissionService/ListNamespacePermissionGroups',
                request_serializer=namespaces__pb2.ListNamespacePermissionGroupsRequest.SerializeToString,
                response_deserializer=namespaces__pb2.ListNamespacePermissionGroupsResponse.FromString,
                )
        self.ListNamespacePermissionUsers = channel.unary_unary(
                '/pomerium.dashboard.NamespacePermissionService/ListNamespacePermissionUsers',
                request_serializer=namespaces__pb2.ListNamespacePermissionUsersRequest.SerializeToString,
                response_deserializer=namespaces__pb2.ListNamespacePermissionUsersResponse.FromString,
                )
        self.SetNamespacePermission = channel.unary_unary(
                '/pomerium.dashboard.NamespacePermissionService/SetNamespacePermission',
                request_serializer=namespaces__pb2.SetNamespacePermissionRequest.SerializeToString,
                response_deserializer=namespaces__pb2.SetNamespacePermissionResponse.FromString,
                )


class NamespacePermissionServiceServicer(object):
    """NamespacePermissionService manages permissions set on namespaces
    """

    def DeleteNamespacePermission(self, request, context):
        """DeleteNamespacePermission removes an existing permission definition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNamespacePermission(self, request, context):
        """GetNamespacePermission retrieves an existing permission definition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamespacePermissions(self, request, context):
        """ListNamespacePermissions retrieves existing permissions for all namespaces
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamespacePermissionGroups(self, request, context):
        """ListNamespacePermissionGroups retrieves existing group based permissions on
        a namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamespacePermissionUsers(self, request, context):
        """ListNamespacePermissionUsers retrieves existing user based permissions on a
        namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNamespacePermission(self, request, context):
        """SetNamespacePermission set a new permission definition on a namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NamespacePermissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeleteNamespacePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNamespacePermission,
                    request_deserializer=namespaces__pb2.DeleteNamespacePermissionRequest.FromString,
                    response_serializer=namespaces__pb2.DeleteNamespacePermissionResponse.SerializeToString,
            ),
            'GetNamespacePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNamespacePermission,
                    request_deserializer=namespaces__pb2.GetNamespacePermissionRequest.FromString,
                    response_serializer=namespaces__pb2.GetNamespacePermissionResponse.SerializeToString,
            ),
            'ListNamespacePermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamespacePermissions,
                    request_deserializer=namespaces__pb2.ListNamespacePermissionsRequest.FromString,
                    response_serializer=namespaces__pb2.ListNamespacePermissionsResponse.SerializeToString,
            ),
            'ListNamespacePermissionGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamespacePermissionGroups,
                    request_deserializer=namespaces__pb2.ListNamespacePermissionGroupsRequest.FromString,
                    response_serializer=namespaces__pb2.ListNamespacePermissionGroupsResponse.SerializeToString,
            ),
            'ListNamespacePermissionUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamespacePermissionUsers,
                    request_deserializer=namespaces__pb2.ListNamespacePermissionUsersRequest.FromString,
                    response_serializer=namespaces__pb2.ListNamespacePermissionUsersResponse.SerializeToString,
            ),
            'SetNamespacePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.SetNamespacePermission,
                    request_deserializer=namespaces__pb2.SetNamespacePermissionRequest.FromString,
                    response_serializer=namespaces__pb2.SetNamespacePermissionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.NamespacePermissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NamespacePermissionService(object):
    """NamespacePermissionService manages permissions set on namespaces
    """

    @staticmethod
    def DeleteNamespacePermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespacePermissionService/DeleteNamespacePermission',
            namespaces__pb2.DeleteNamespacePermissionRequest.SerializeToString,
            namespaces__pb2.DeleteNamespacePermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNamespacePermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespacePermissionService/GetNamespacePermission',
            namespaces__pb2.GetNamespacePermissionRequest.SerializeToString,
            namespaces__pb2.GetNamespacePermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamespacePermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespacePermissionService/ListNamespacePermissions',
            namespaces__pb2.ListNamespacePermissionsRequest.SerializeToString,
            namespaces__pb2.ListNamespacePermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamespacePermissionGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespacePermissionService/ListNamespacePermissionGroups',
            namespaces__pb2.ListNamespacePermissionGroupsRequest.SerializeToString,
            namespaces__pb2.ListNamespacePermissionGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamespacePermissionUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespacePermissionService/ListNamespacePermissionUsers',
            namespaces__pb2.ListNamespacePermissionUsersRequest.SerializeToString,
            namespaces__pb2.ListNamespacePermissionUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNamespacePermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.NamespacePermissionService/SetNamespacePermission',
            namespaces__pb2.SetNamespacePermissionRequest.SerializeToString,
            namespaces__pb2.SetNamespacePermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
