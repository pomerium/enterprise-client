"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import report_pb2

class ReportStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    PolicyReport: grpc.UnaryUnaryMultiCallable[
        report_pb2.PolicyReportRequest,
        report_pb2.PolicyReportResponse,
    ]
    """PolicyReport generates a policy report"""

class ReportServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def PolicyReport(
        self,
        request: report_pb2.PolicyReportRequest,
        context: grpc.ServicerContext,
    ) -> report_pb2.PolicyReportResponse:
        """PolicyReport generates a policy report"""

def add_ReportServicer_to_server(servicer: ReportServicer, server: grpc.Server) -> None: ...
