# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import events_pb2 as events__pb2


class EventsStub(object):
    """Events represent configuration changes made to envoy's controle plane by
    Pomerium
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sync = channel.unary_stream(
                '/pomerium.dashboard.Events/Sync',
                request_serializer=events__pb2.SyncRequest.SerializeToString,
                response_deserializer=events__pb2.SyncResponse.FromString,
                )


class EventsServicer(object):
    """Events represent configuration changes made to envoy's controle plane by
    Pomerium
    """

    def Sync(self, request, context):
        """Sync sends all current events and then pushes new events as they arrive
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sync': grpc.unary_stream_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=events__pb2.SyncRequest.FromString,
                    response_serializer=events__pb2.SyncResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.Events', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Events(object):
    """Events represent configuration changes made to envoy's controle plane by
    Pomerium
    """

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pomerium.dashboard.Events/Sync',
            events__pb2.SyncRequest.SerializeToString,
            events__pb2.SyncResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
