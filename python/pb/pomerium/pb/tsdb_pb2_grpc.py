# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import tsdb_pb2 as tsdb__pb2


class TimeSeriesDBStub(object):
    """TimeSeriesDB is a generic service that is meant to be able to query for
    historical metrics and should provide a sufficient abstraction between the UI
    and underlying time series service, would it be Prometheus, embedded TSDB or
    other 3rd party provider
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRouteMetricChange = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricChange',
                request_serializer=tsdb__pb2.RouteMetricChangeRequest.SerializeToString,
                response_deserializer=tsdb__pb2.Scalar.FromString,
                )
        self.GetRouteMetricChangeHistogram = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricChangeHistogram',
                request_serializer=tsdb__pb2.RouteMetricChangeRequest.SerializeToString,
                response_deserializer=tsdb__pb2.ScalarBuckets.FromString,
                )
        self.GetRouteMetricSeries = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricSeries',
                request_serializer=tsdb__pb2.RouteMetricSeriesRequest.SerializeToString,
                response_deserializer=tsdb__pb2.TimeSeriesResponse.FromString,
                )
        self.GetRouteMetricSeriesHistogram = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricSeriesHistogram',
                request_serializer=tsdb__pb2.RouteMetricSeriesHistogramRequest.SerializeToString,
                response_deserializer=tsdb__pb2.TimeSeriesResponse.FromString,
                )
        self.GetRouteMetricSeriesMulti = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricSeriesMulti',
                request_serializer=tsdb__pb2.RouteMetricSeriesRequest.SerializeToString,
                response_deserializer=tsdb__pb2.TimeSeriesResponseMulti.FromString,
                )
        self.GetUptime = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetUptime',
                request_serializer=tsdb__pb2.UptimeRequest.SerializeToString,
                response_deserializer=tsdb__pb2.UptimeResponse.FromString,
                )
        self.GetInstances = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetInstances',
                request_serializer=tsdb__pb2.GetInstancesRequest.SerializeToString,
                response_deserializer=tsdb__pb2.Instances.FromString,
                )
        self.GetServerMetricSeries = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetServerMetricSeries',
                request_serializer=tsdb__pb2.ServerMetricSeriesRequest.SerializeToString,
                response_deserializer=tsdb__pb2.TimeSeriesResponse.FromString,
                )
        self.GetServerMetric = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetServerMetric',
                request_serializer=tsdb__pb2.ServerMetricRequest.SerializeToString,
                response_deserializer=tsdb__pb2.Sample.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetStatus',
                request_serializer=tsdb__pb2.GetStatusRequest.SerializeToString,
                response_deserializer=tsdb__pb2.GetStatusResponse.FromString,
                )
        self.GetLastError = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetLastError',
                request_serializer=tsdb__pb2.LastErrorRequest.SerializeToString,
                response_deserializer=tsdb__pb2.LastErrorResponse.FromString,
                )
        self.GetUsageReport = channel.unary_unary(
                '/pomerium.dashboard.TimeSeriesDB/GetUsageReport',
                request_serializer=tsdb__pb2.UsageReportRequest.SerializeToString,
                response_deserializer=tsdb__pb2.UsageReportResponse.FromString,
                )


class TimeSeriesDBServicer(object):
    """TimeSeriesDB is a generic service that is meant to be able to query for
    historical metrics and should provide a sufficient abstraction between the UI
    and underlying time series service, would it be Prometheus, embedded TSDB or
    other 3rd party provider
    """

    def GetRouteMetricChange(self, request, context):
        """returns metric change for a period of time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRouteMetricChangeHistogram(self, request, context):
        """returns buckets of values for a given metric
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRouteMetricSeries(self, request, context):
        """returns metric change as time series
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRouteMetricSeriesHistogram(self, request, context):
        """returns metric change as time series
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRouteMetricSeriesMulti(self, request, context):
        """returns multiple annotated time series
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUptime(self, request, context):
        """returns service uptime statistics
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstances(self, request, context):
        """returns list of system services with metrics
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerMetricSeries(self, request, context):
        """returns server queries
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerMetric(self, request, context):
        """returns current metric value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """returns current status of scraping targets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastError(self, request, context):
        """returns last known error for a metric, if available
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsageReport(self, request, context):
        """returns usage report
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeSeriesDBServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRouteMetricChange': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRouteMetricChange,
                    request_deserializer=tsdb__pb2.RouteMetricChangeRequest.FromString,
                    response_serializer=tsdb__pb2.Scalar.SerializeToString,
            ),
            'GetRouteMetricChangeHistogram': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRouteMetricChangeHistogram,
                    request_deserializer=tsdb__pb2.RouteMetricChangeRequest.FromString,
                    response_serializer=tsdb__pb2.ScalarBuckets.SerializeToString,
            ),
            'GetRouteMetricSeries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRouteMetricSeries,
                    request_deserializer=tsdb__pb2.RouteMetricSeriesRequest.FromString,
                    response_serializer=tsdb__pb2.TimeSeriesResponse.SerializeToString,
            ),
            'GetRouteMetricSeriesHistogram': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRouteMetricSeriesHistogram,
                    request_deserializer=tsdb__pb2.RouteMetricSeriesHistogramRequest.FromString,
                    response_serializer=tsdb__pb2.TimeSeriesResponse.SerializeToString,
            ),
            'GetRouteMetricSeriesMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRouteMetricSeriesMulti,
                    request_deserializer=tsdb__pb2.RouteMetricSeriesRequest.FromString,
                    response_serializer=tsdb__pb2.TimeSeriesResponseMulti.SerializeToString,
            ),
            'GetUptime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUptime,
                    request_deserializer=tsdb__pb2.UptimeRequest.FromString,
                    response_serializer=tsdb__pb2.UptimeResponse.SerializeToString,
            ),
            'GetInstances': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstances,
                    request_deserializer=tsdb__pb2.GetInstancesRequest.FromString,
                    response_serializer=tsdb__pb2.Instances.SerializeToString,
            ),
            'GetServerMetricSeries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerMetricSeries,
                    request_deserializer=tsdb__pb2.ServerMetricSeriesRequest.FromString,
                    response_serializer=tsdb__pb2.TimeSeriesResponse.SerializeToString,
            ),
            'GetServerMetric': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerMetric,
                    request_deserializer=tsdb__pb2.ServerMetricRequest.FromString,
                    response_serializer=tsdb__pb2.Sample.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=tsdb__pb2.GetStatusRequest.FromString,
                    response_serializer=tsdb__pb2.GetStatusResponse.SerializeToString,
            ),
            'GetLastError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastError,
                    request_deserializer=tsdb__pb2.LastErrorRequest.FromString,
                    response_serializer=tsdb__pb2.LastErrorResponse.SerializeToString,
            ),
            'GetUsageReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsageReport,
                    request_deserializer=tsdb__pb2.UsageReportRequest.FromString,
                    response_serializer=tsdb__pb2.UsageReportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.TimeSeriesDB', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimeSeriesDB(object):
    """TimeSeriesDB is a generic service that is meant to be able to query for
    historical metrics and should provide a sufficient abstraction between the UI
    and underlying time series service, would it be Prometheus, embedded TSDB or
    other 3rd party provider
    """

    @staticmethod
    def GetRouteMetricChange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricChange',
            tsdb__pb2.RouteMetricChangeRequest.SerializeToString,
            tsdb__pb2.Scalar.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRouteMetricChangeHistogram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricChangeHistogram',
            tsdb__pb2.RouteMetricChangeRequest.SerializeToString,
            tsdb__pb2.ScalarBuckets.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRouteMetricSeries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricSeries',
            tsdb__pb2.RouteMetricSeriesRequest.SerializeToString,
            tsdb__pb2.TimeSeriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRouteMetricSeriesHistogram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricSeriesHistogram',
            tsdb__pb2.RouteMetricSeriesHistogramRequest.SerializeToString,
            tsdb__pb2.TimeSeriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRouteMetricSeriesMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetRouteMetricSeriesMulti',
            tsdb__pb2.RouteMetricSeriesRequest.SerializeToString,
            tsdb__pb2.TimeSeriesResponseMulti.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUptime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetUptime',
            tsdb__pb2.UptimeRequest.SerializeToString,
            tsdb__pb2.UptimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetInstances',
            tsdb__pb2.GetInstancesRequest.SerializeToString,
            tsdb__pb2.Instances.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerMetricSeries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetServerMetricSeries',
            tsdb__pb2.ServerMetricSeriesRequest.SerializeToString,
            tsdb__pb2.TimeSeriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerMetric(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetServerMetric',
            tsdb__pb2.ServerMetricRequest.SerializeToString,
            tsdb__pb2.Sample.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetStatus',
            tsdb__pb2.GetStatusRequest.SerializeToString,
            tsdb__pb2.GetStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetLastError',
            tsdb__pb2.LastErrorRequest.SerializeToString,
            tsdb__pb2.LastErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsageReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.TimeSeriesDB/GetUsageReport',
            tsdb__pb2.UsageReportRequest.SerializeToString,
            tsdb__pb2.UsageReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
