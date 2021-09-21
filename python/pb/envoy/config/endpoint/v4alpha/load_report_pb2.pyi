"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import envoy.config.core.v4alpha.address_pb2
import envoy.config.core.v4alpha.base_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UpstreamLocalityStats(google.protobuf.message.Message):
    """[#protodoc-title: Load Report]

    These are stats Envoy reports to the management server at a frequency defined by
    :ref:`LoadStatsResponse.load_reporting_interval<envoy_v3_api_field_service.load_stats.v3.LoadStatsResponse.load_reporting_interval>`.
    Stats per upstream region/zone and optionally per subzone.
    [#next-free-field: 9]
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOCALITY_FIELD_NUMBER: builtins.int
    TOTAL_SUCCESSFUL_REQUESTS_FIELD_NUMBER: builtins.int
    TOTAL_REQUESTS_IN_PROGRESS_FIELD_NUMBER: builtins.int
    TOTAL_ERROR_REQUESTS_FIELD_NUMBER: builtins.int
    TOTAL_ISSUED_REQUESTS_FIELD_NUMBER: builtins.int
    LOAD_METRIC_STATS_FIELD_NUMBER: builtins.int
    UPSTREAM_ENDPOINT_STATS_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    @property
    def locality(self) -> envoy.config.core.v4alpha.base_pb2.Locality:
        """Name of zone, region and optionally endpoint group these metrics were
        collected from. Zone and region names could be empty if unknown.
        """
        pass
    total_successful_requests: builtins.int = ...
    """The total number of requests successfully completed by the endpoints in the
    locality.
    """

    total_requests_in_progress: builtins.int = ...
    """The total number of unfinished requests"""

    total_error_requests: builtins.int = ...
    """The total number of requests that failed due to errors at the endpoint,
    aggregated over all endpoints in the locality.
    """

    total_issued_requests: builtins.int = ...
    """The total number of requests that were issued by this Envoy since
    the last report. This information is aggregated over all the
    upstream endpoints in the locality.
    """

    @property
    def load_metric_stats(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EndpointLoadMetricStats]:
        """Stats for multi-dimensional load balancing."""
        pass
    @property
    def upstream_endpoint_stats(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UpstreamEndpointStats]:
        """Endpoint granularity stats information for this locality. This information
        is populated if the Server requests it by setting
        :ref:`LoadStatsResponse.report_endpoint_granularity<envoy_v3_api_field_service.load_stats.v3.LoadStatsResponse.report_endpoint_granularity>`.
        """
        pass
    priority: builtins.int = ...
    """[#not-implemented-hide:] The priority of the endpoint group these metrics
    were collected from.
    """

    def __init__(self,
        *,
        locality : typing.Optional[envoy.config.core.v4alpha.base_pb2.Locality] = ...,
        total_successful_requests : builtins.int = ...,
        total_requests_in_progress : builtins.int = ...,
        total_error_requests : builtins.int = ...,
        total_issued_requests : builtins.int = ...,
        load_metric_stats : typing.Optional[typing.Iterable[global___EndpointLoadMetricStats]] = ...,
        upstream_endpoint_stats : typing.Optional[typing.Iterable[global___UpstreamEndpointStats]] = ...,
        priority : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"locality",b"locality"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"load_metric_stats",b"load_metric_stats",u"locality",b"locality",u"priority",b"priority",u"total_error_requests",b"total_error_requests",u"total_issued_requests",b"total_issued_requests",u"total_requests_in_progress",b"total_requests_in_progress",u"total_successful_requests",b"total_successful_requests",u"upstream_endpoint_stats",b"upstream_endpoint_stats"]) -> None: ...
global___UpstreamLocalityStats = UpstreamLocalityStats

class UpstreamEndpointStats(google.protobuf.message.Message):
    """[#next-free-field: 8]"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    TOTAL_SUCCESSFUL_REQUESTS_FIELD_NUMBER: builtins.int
    TOTAL_REQUESTS_IN_PROGRESS_FIELD_NUMBER: builtins.int
    TOTAL_ERROR_REQUESTS_FIELD_NUMBER: builtins.int
    TOTAL_ISSUED_REQUESTS_FIELD_NUMBER: builtins.int
    LOAD_METRIC_STATS_FIELD_NUMBER: builtins.int
    @property
    def address(self) -> envoy.config.core.v4alpha.address_pb2.Address:
        """Upstream host address."""
        pass
    @property
    def metadata(self) -> google.protobuf.struct_pb2.Struct:
        """Opaque and implementation dependent metadata of the
        endpoint. Envoy will pass this directly to the management server.
        """
        pass
    total_successful_requests: builtins.int = ...
    """The total number of requests successfully completed by the endpoints in the
    locality. These include non-5xx responses for HTTP, where errors
    originate at the client and the endpoint responded successfully. For gRPC,
    the grpc-status values are those not covered by total_error_requests below.
    """

    total_requests_in_progress: builtins.int = ...
    """The total number of unfinished requests for this endpoint."""

    total_error_requests: builtins.int = ...
    """The total number of requests that failed due to errors at the endpoint.
    For HTTP these are responses with 5xx status codes and for gRPC the
    grpc-status values:

      - DeadlineExceeded
      - Unimplemented
      - Internal
      - Unavailable
      - Unknown
      - DataLoss
    """

    total_issued_requests: builtins.int = ...
    """The total number of requests that were issued to this endpoint
    since the last report. A single TCP connection, HTTP or gRPC
    request or stream is counted as one request.
    """

    @property
    def load_metric_stats(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EndpointLoadMetricStats]:
        """Stats for multi-dimensional load balancing."""
        pass
    def __init__(self,
        *,
        address : typing.Optional[envoy.config.core.v4alpha.address_pb2.Address] = ...,
        metadata : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        total_successful_requests : builtins.int = ...,
        total_requests_in_progress : builtins.int = ...,
        total_error_requests : builtins.int = ...,
        total_issued_requests : builtins.int = ...,
        load_metric_stats : typing.Optional[typing.Iterable[global___EndpointLoadMetricStats]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"address",b"address",u"metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"load_metric_stats",b"load_metric_stats",u"metadata",b"metadata",u"total_error_requests",b"total_error_requests",u"total_issued_requests",b"total_issued_requests",u"total_requests_in_progress",b"total_requests_in_progress",u"total_successful_requests",b"total_successful_requests"]) -> None: ...
global___UpstreamEndpointStats = UpstreamEndpointStats

class EndpointLoadMetricStats(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METRIC_NAME_FIELD_NUMBER: builtins.int
    NUM_REQUESTS_FINISHED_WITH_METRIC_FIELD_NUMBER: builtins.int
    TOTAL_METRIC_VALUE_FIELD_NUMBER: builtins.int
    metric_name: typing.Text = ...
    """Name of the metric; may be empty."""

    num_requests_finished_with_metric: builtins.int = ...
    """Number of calls that finished and included this metric."""

    total_metric_value: builtins.float = ...
    """Sum of metric values across all calls that finished with this metric for
    load_reporting_interval.
    """

    def __init__(self,
        *,
        metric_name : typing.Text = ...,
        num_requests_finished_with_metric : builtins.int = ...,
        total_metric_value : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metric_name",b"metric_name",u"num_requests_finished_with_metric",b"num_requests_finished_with_metric",u"total_metric_value",b"total_metric_value"]) -> None: ...
global___EndpointLoadMetricStats = EndpointLoadMetricStats

class ClusterStats(google.protobuf.message.Message):
    """Per cluster load stats. Envoy reports these stats a management server in a
    :ref:`LoadStatsRequest<envoy_v3_api_msg_service.load_stats.v3.LoadStatsRequest>`
    Next ID: 7
    [#next-free-field: 7]
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class DroppedRequests(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        CATEGORY_FIELD_NUMBER: builtins.int
        DROPPED_COUNT_FIELD_NUMBER: builtins.int
        category: typing.Text = ...
        """Identifier for the policy specifying the drop."""

        dropped_count: builtins.int = ...
        """Total number of deliberately dropped requests for the category."""

        def __init__(self,
            *,
            category : typing.Text = ...,
            dropped_count : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"category",b"category",u"dropped_count",b"dropped_count"]) -> None: ...

    CLUSTER_NAME_FIELD_NUMBER: builtins.int
    CLUSTER_SERVICE_NAME_FIELD_NUMBER: builtins.int
    UPSTREAM_LOCALITY_STATS_FIELD_NUMBER: builtins.int
    TOTAL_DROPPED_REQUESTS_FIELD_NUMBER: builtins.int
    DROPPED_REQUESTS_FIELD_NUMBER: builtins.int
    LOAD_REPORT_INTERVAL_FIELD_NUMBER: builtins.int
    cluster_name: typing.Text = ...
    """The name of the cluster."""

    cluster_service_name: typing.Text = ...
    """The eds_cluster_config service_name of the cluster.
    It's possible that two clusters send the same service_name to EDS,
    in that case, the management server is supposed to do aggregation on the load reports.
    """

    @property
    def upstream_locality_stats(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UpstreamLocalityStats]:
        """Need at least one."""
        pass
    total_dropped_requests: builtins.int = ...
    """Cluster-level stats such as total_successful_requests may be computed by
    summing upstream_locality_stats. In addition, below there are additional
    cluster-wide stats.

    The total number of dropped requests. This covers requests
    deliberately dropped by the drop_overload policy and circuit breaking.
    """

    @property
    def dropped_requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClusterStats.DroppedRequests]:
        """Information about deliberately dropped requests for each category specified
        in the DropOverload policy.
        """
        pass
    @property
    def load_report_interval(self) -> google.protobuf.duration_pb2.Duration:
        """Period over which the actual load report occurred. This will be guaranteed to include every
        request reported. Due to system load and delays between the *LoadStatsRequest* sent from Envoy
        and the *LoadStatsResponse* message sent from the management server, this may be longer than
        the requested load reporting interval in the *LoadStatsResponse*.
        """
        pass
    def __init__(self,
        *,
        cluster_name : typing.Text = ...,
        cluster_service_name : typing.Text = ...,
        upstream_locality_stats : typing.Optional[typing.Iterable[global___UpstreamLocalityStats]] = ...,
        total_dropped_requests : builtins.int = ...,
        dropped_requests : typing.Optional[typing.Iterable[global___ClusterStats.DroppedRequests]] = ...,
        load_report_interval : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"load_report_interval",b"load_report_interval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cluster_name",b"cluster_name",u"cluster_service_name",b"cluster_service_name",u"dropped_requests",b"dropped_requests",u"load_report_interval",b"load_report_interval",u"total_dropped_requests",b"total_dropped_requests",u"upstream_locality_stats",b"upstream_locality_stats"]) -> None: ...
global___ClusterStats = ClusterStats
