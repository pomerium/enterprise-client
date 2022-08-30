"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import activity_log_pb2
import grpc

class ActivityLogServiceStub:
    """ActivityLogService tracks historical changes to configuration made through
    Pomerium Enterprise
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    GetActivityLogEntry: grpc.UnaryUnaryMultiCallable[
        activity_log_pb2.GetActivityLogEntryRequest,
        activity_log_pb2.GetActivityLogEntryResponse,
    ]
    """GetActivityLogEntry retrieves a specific activity log entry"""
    ListActivityLogEntries: grpc.UnaryUnaryMultiCallable[
        activity_log_pb2.ListActivityLogEntriesRequest,
        activity_log_pb2.ListActivityLogEntriesResponse,
    ]
    """ListActivityLogEntries lists activity log entries based on paramters in the
    ListActivityLogEntriesRequest
    """

class ActivityLogServiceServicer(metaclass=abc.ABCMeta):
    """ActivityLogService tracks historical changes to configuration made through
    Pomerium Enterprise
    """

    @abc.abstractmethod
    def GetActivityLogEntry(
        self,
        request: activity_log_pb2.GetActivityLogEntryRequest,
        context: grpc.ServicerContext,
    ) -> activity_log_pb2.GetActivityLogEntryResponse:
        """GetActivityLogEntry retrieves a specific activity log entry"""
    @abc.abstractmethod
    def ListActivityLogEntries(
        self,
        request: activity_log_pb2.ListActivityLogEntriesRequest,
        context: grpc.ServicerContext,
    ) -> activity_log_pb2.ListActivityLogEntriesResponse:
        """ListActivityLogEntries lists activity log entries based on paramters in the
        ListActivityLogEntriesRequest
        """

def add_ActivityLogServiceServicer_to_server(servicer: ActivityLogServiceServicer, server: grpc.Server) -> None: ...
