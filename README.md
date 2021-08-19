# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [activity_log.proto](#activity_log.proto)
    - [ActivityLogEntry](#pomerium.dashboard.ActivityLogEntry)
    - [ActivityLogEntry.DiffSummary](#pomerium.dashboard.ActivityLogEntry.DiffSummary)
    - [GetActivityLogEntryRequest](#pomerium.dashboard.GetActivityLogEntryRequest)
    - [GetActivityLogEntryResponse](#pomerium.dashboard.GetActivityLogEntryResponse)
    - [ListActivityLogEntriesRequest](#pomerium.dashboard.ListActivityLogEntriesRequest)
    - [ListActivityLogEntriesRequest.DateFilter](#pomerium.dashboard.ListActivityLogEntriesRequest.DateFilter)
    - [ListActivityLogEntriesRequest.Entity](#pomerium.dashboard.ListActivityLogEntriesRequest.Entity)
    - [ListActivityLogEntriesRequest.Sort](#pomerium.dashboard.ListActivityLogEntriesRequest.Sort)
    - [ListActivityLogEntriesRequest.StringFilter](#pomerium.dashboard.ListActivityLogEntriesRequest.StringFilter)
    - [ListActivityLogEntriesResponse](#pomerium.dashboard.ListActivityLogEntriesResponse)
  
    - [ActivityLogService](#pomerium.dashboard.ActivityLogService)
  
- [console_config.proto](#console_config.proto)
    - [ConsoleConfig](#pomerium.dashboard.ConsoleConfig)
  
- [events.proto](#events.proto)
    - [Event](#pomerium.dashboard.Event)
    - [SyncRequest](#pomerium.dashboard.SyncRequest)
    - [SyncResponse](#pomerium.dashboard.SyncResponse)
  
    - [Event.EventKind](#pomerium.dashboard.Event.EventKind)
  
    - [Events](#pomerium.dashboard.Events)
  
- [key_chain.proto](#key_chain.proto)
    - [CertificateInfo](#pomerium.dashboard.CertificateInfo)
    - [CreateKeyPairRequest](#pomerium.dashboard.CreateKeyPairRequest)
    - [CreateKeyPairResponse](#pomerium.dashboard.CreateKeyPairResponse)
    - [DeleteKeyPairRequest](#pomerium.dashboard.DeleteKeyPairRequest)
    - [DeleteKeyPairResponse](#pomerium.dashboard.DeleteKeyPairResponse)
    - [GetKeyPairRequest](#pomerium.dashboard.GetKeyPairRequest)
    - [GetKeyPairResponse](#pomerium.dashboard.GetKeyPairResponse)
    - [KeyPair](#pomerium.dashboard.KeyPair)
    - [KeyPairRecord](#pomerium.dashboard.KeyPairRecord)
    - [KeyUsage](#pomerium.dashboard.KeyUsage)
    - [ListKeyPairsRequest](#pomerium.dashboard.ListKeyPairsRequest)
    - [ListKeyPairsResponse](#pomerium.dashboard.ListKeyPairsResponse)
    - [Name](#pomerium.dashboard.Name)
    - [UpdateKeyPairRequest](#pomerium.dashboard.UpdateKeyPairRequest)
    - [UpdateKeyPairResponse](#pomerium.dashboard.UpdateKeyPairResponse)
  
    - [Format](#pomerium.dashboard.Format)
    - [PublicKeyAlgorithm](#pomerium.dashboard.PublicKeyAlgorithm)
  
    - [KeyChainService](#pomerium.dashboard.KeyChainService)
  
- [namespaces.proto](#namespaces.proto)
    - [DeleteNamespacePermissionRequest](#pomerium.dashboard.DeleteNamespacePermissionRequest)
    - [DeleteNamespacePermissionResponse](#pomerium.dashboard.DeleteNamespacePermissionResponse)
    - [DeleteNamespaceRequest](#pomerium.dashboard.DeleteNamespaceRequest)
    - [DeleteNamespaceResponse](#pomerium.dashboard.DeleteNamespaceResponse)
    - [GetNamespacePermissionRequest](#pomerium.dashboard.GetNamespacePermissionRequest)
    - [GetNamespacePermissionResponse](#pomerium.dashboard.GetNamespacePermissionResponse)
    - [GetNamespaceRequest](#pomerium.dashboard.GetNamespaceRequest)
    - [GetNamespaceResponse](#pomerium.dashboard.GetNamespaceResponse)
    - [ListNamespacePermissionGroupsRequest](#pomerium.dashboard.ListNamespacePermissionGroupsRequest)
    - [ListNamespacePermissionGroupsResponse](#pomerium.dashboard.ListNamespacePermissionGroupsResponse)
    - [ListNamespacePermissionUsersRequest](#pomerium.dashboard.ListNamespacePermissionUsersRequest)
    - [ListNamespacePermissionUsersResponse](#pomerium.dashboard.ListNamespacePermissionUsersResponse)
    - [ListNamespacePermissionsRequest](#pomerium.dashboard.ListNamespacePermissionsRequest)
    - [ListNamespacePermissionsResponse](#pomerium.dashboard.ListNamespacePermissionsResponse)
    - [ListNamespacesRequest](#pomerium.dashboard.ListNamespacesRequest)
    - [ListNamespacesResponse](#pomerium.dashboard.ListNamespacesResponse)
    - [Namespace](#pomerium.dashboard.Namespace)
    - [NamespacePermission](#pomerium.dashboard.NamespacePermission)
    - [NamespacePermissionGroup](#pomerium.dashboard.NamespacePermissionGroup)
    - [NamespacePermissionUser](#pomerium.dashboard.NamespacePermissionUser)
    - [SetNamespacePermissionRequest](#pomerium.dashboard.SetNamespacePermissionRequest)
    - [SetNamespacePermissionResponse](#pomerium.dashboard.SetNamespacePermissionResponse)
    - [SetNamespaceRequest](#pomerium.dashboard.SetNamespaceRequest)
    - [SetNamespaceResponse](#pomerium.dashboard.SetNamespaceResponse)
  
    - [NamespacePermissionService](#pomerium.dashboard.NamespacePermissionService)
    - [NamespaceService](#pomerium.dashboard.NamespaceService)
  
- [policy.proto](#policy.proto)
    - [DeletePolicyRequest](#pomerium.dashboard.DeletePolicyRequest)
    - [DeletePolicyResponse](#pomerium.dashboard.DeletePolicyResponse)
    - [GetPolicyRequest](#pomerium.dashboard.GetPolicyRequest)
    - [GetPolicyResponse](#pomerium.dashboard.GetPolicyResponse)
    - [ListPoliciesRequest](#pomerium.dashboard.ListPoliciesRequest)
    - [ListPoliciesResponse](#pomerium.dashboard.ListPoliciesResponse)
    - [Policy](#pomerium.dashboard.Policy)
    - [Policy.AllowedIdpClaimsEntry](#pomerium.dashboard.Policy.AllowedIdpClaimsEntry)
    - [Policy.RoutesEntry](#pomerium.dashboard.Policy.RoutesEntry)
    - [SetPolicyRequest](#pomerium.dashboard.SetPolicyRequest)
    - [SetPolicyResponse](#pomerium.dashboard.SetPolicyResponse)
  
    - [PolicyService](#pomerium.dashboard.PolicyService)
  
- [report.proto](#report.proto)
    - [PolicyReportRequest](#pomerium.dashboard.PolicyReportRequest)
    - [PolicyReportResponse](#pomerium.dashboard.PolicyReportResponse)
  
    - [Report](#pomerium.dashboard.Report)
  
- [routes.proto](#routes.proto)
    - [DeleteRouteRequest](#pomerium.dashboard.DeleteRouteRequest)
    - [DeleteRouteResponse](#pomerium.dashboard.DeleteRouteResponse)
    - [GetRouteRequest](#pomerium.dashboard.GetRouteRequest)
    - [GetRouteResponse](#pomerium.dashboard.GetRouteResponse)
    - [ListRoutesRequest](#pomerium.dashboard.ListRoutesRequest)
    - [ListRoutesResponse](#pomerium.dashboard.ListRoutesResponse)
    - [LoadRoutesRequest](#pomerium.dashboard.LoadRoutesRequest)
    - [LoadRoutesResponse](#pomerium.dashboard.LoadRoutesResponse)
    - [MoveRoutesRequest](#pomerium.dashboard.MoveRoutesRequest)
    - [MoveRoutesResponse](#pomerium.dashboard.MoveRoutesResponse)
    - [Route](#pomerium.dashboard.Route)
    - [Route.SetRequestHeadersEntry](#pomerium.dashboard.Route.SetRequestHeadersEntry)
    - [RouteRewriteHeader](#pomerium.dashboard.RouteRewriteHeader)
    - [RouteWithPolicies](#pomerium.dashboard.RouteWithPolicies)
    - [SetRouteRequest](#pomerium.dashboard.SetRouteRequest)
    - [SetRouteResponse](#pomerium.dashboard.SetRouteResponse)
  
    - [RouteService](#pomerium.dashboard.RouteService)
  
- [settings.proto](#settings.proto)
    - [GetSettingsRequest](#pomerium.dashboard.GetSettingsRequest)
    - [GetSettingsResponse](#pomerium.dashboard.GetSettingsResponse)
    - [SetSettingsRequest](#pomerium.dashboard.SetSettingsRequest)
    - [SetSettingsResponse](#pomerium.dashboard.SetSettingsResponse)
    - [Settings](#pomerium.dashboard.Settings)
    - [Settings.Certificate](#pomerium.dashboard.Settings.Certificate)
    - [Settings.JwtClaimsHeadersEntry](#pomerium.dashboard.Settings.JwtClaimsHeadersEntry)
    - [Settings.RequestParamsEntry](#pomerium.dashboard.Settings.RequestParamsEntry)
    - [Settings.SetResponseHeadersEntry](#pomerium.dashboard.Settings.SetResponseHeadersEntry)
  
    - [SettingsService](#pomerium.dashboard.SettingsService)
  
- [tsdb.proto](#tsdb.proto)
    - [GetInstanceInfoRequest](#pomerium.dashboard.GetInstanceInfoRequest)
    - [GetInstancesRequest](#pomerium.dashboard.GetInstancesRequest)
    - [GetStatusRequest](#pomerium.dashboard.GetStatusRequest)
    - [GetStatusResponse](#pomerium.dashboard.GetStatusResponse)
    - [GetStatusResponse.Target](#pomerium.dashboard.GetStatusResponse.Target)
    - [Instances](#pomerium.dashboard.Instances)
    - [Instances.Instance](#pomerium.dashboard.Instances.Instance)
    - [Labels](#pomerium.dashboard.Labels)
    - [Labels.LabelsEntry](#pomerium.dashboard.Labels.LabelsEntry)
    - [Matrix](#pomerium.dashboard.Matrix)
    - [Range](#pomerium.dashboard.Range)
    - [RouteMatcher](#pomerium.dashboard.RouteMatcher)
    - [RouteMetricChangeRequest](#pomerium.dashboard.RouteMetricChangeRequest)
    - [RouteMetricSeriesHistogramRequest](#pomerium.dashboard.RouteMetricSeriesHistogramRequest)
    - [RouteMetricSeriesRequest](#pomerium.dashboard.RouteMetricSeriesRequest)
    - [Sample](#pomerium.dashboard.Sample)
    - [Sample.LabelsEntry](#pomerium.dashboard.Sample.LabelsEntry)
    - [Scalar](#pomerium.dashboard.Scalar)
    - [ScalarBuckets](#pomerium.dashboard.ScalarBuckets)
    - [ScalarBuckets.Bucket](#pomerium.dashboard.ScalarBuckets.Bucket)
    - [ServerMetricRequest](#pomerium.dashboard.ServerMetricRequest)
    - [ServerMetricSeriesRequest](#pomerium.dashboard.ServerMetricSeriesRequest)
    - [String](#pomerium.dashboard.String)
    - [TimeSeries](#pomerium.dashboard.TimeSeries)
    - [TimeSeries.LabelsEntry](#pomerium.dashboard.TimeSeries.LabelsEntry)
    - [TimeSeriesResponse](#pomerium.dashboard.TimeSeriesResponse)
    - [TimeSeriesResponseMulti](#pomerium.dashboard.TimeSeriesResponseMulti)
    - [UptimeRequest](#pomerium.dashboard.UptimeRequest)
    - [UptimeResponse](#pomerium.dashboard.UptimeResponse)
    - [UptimeResponse.Summary](#pomerium.dashboard.UptimeResponse.Summary)
    - [Vector](#pomerium.dashboard.Vector)
  
    - [Component](#pomerium.dashboard.Component)
    - [GetStatusResponse.Target.Health](#pomerium.dashboard.GetStatusResponse.Target.Health)
    - [Metric](#pomerium.dashboard.Metric)
    - [Rate](#pomerium.dashboard.Rate)
    - [UptimeResponse.Status](#pomerium.dashboard.UptimeResponse.Status)
  
    - [TimeSeriesDB](#pomerium.dashboard.TimeSeriesDB)
  
- [users.proto](#users.proto)
    - [AddPomeriumServiceAccountRequest](#pomerium.dashboard.AddPomeriumServiceAccountRequest)
    - [AddPomeriumServiceAccountResponse](#pomerium.dashboard.AddPomeriumServiceAccountResponse)
    - [DeletePomeriumServiceAccountRequest](#pomerium.dashboard.DeletePomeriumServiceAccountRequest)
    - [DeletePomeriumServiceAccountResponse](#pomerium.dashboard.DeletePomeriumServiceAccountResponse)
    - [DeletePomeriumSessionRequest](#pomerium.dashboard.DeletePomeriumSessionRequest)
    - [DeletePomeriumSessionResponse](#pomerium.dashboard.DeletePomeriumSessionResponse)
    - [GetPomeriumServiceAccountRequest](#pomerium.dashboard.GetPomeriumServiceAccountRequest)
    - [GetPomeriumServiceAccountResponse](#pomerium.dashboard.GetPomeriumServiceAccountResponse)
    - [GetPomeriumSessionRequest](#pomerium.dashboard.GetPomeriumSessionRequest)
    - [GetPomeriumSessionResponse](#pomerium.dashboard.GetPomeriumSessionResponse)
    - [GetUserInfoRequest](#pomerium.dashboard.GetUserInfoRequest)
    - [GetUserInfoResponse](#pomerium.dashboard.GetUserInfoResponse)
    - [GroupInfo](#pomerium.dashboard.GroupInfo)
    - [ImpersonateRequest](#pomerium.dashboard.ImpersonateRequest)
    - [ImpersonateResponse](#pomerium.dashboard.ImpersonateResponse)
    - [ListPomeriumServiceAccountsRequest](#pomerium.dashboard.ListPomeriumServiceAccountsRequest)
    - [ListPomeriumServiceAccountsResponse](#pomerium.dashboard.ListPomeriumServiceAccountsResponse)
    - [ListPomeriumSessionsRequest](#pomerium.dashboard.ListPomeriumSessionsRequest)
    - [ListPomeriumSessionsResponse](#pomerium.dashboard.ListPomeriumSessionsResponse)
    - [PomeriumServiceAccount](#pomerium.dashboard.PomeriumServiceAccount)
    - [PomeriumSession](#pomerium.dashboard.PomeriumSession)
    - [PomeriumSession.ClaimsEntry](#pomerium.dashboard.PomeriumSession.ClaimsEntry)
    - [PomeriumSession.Group](#pomerium.dashboard.PomeriumSession.Group)
    - [PomeriumSession.User](#pomerium.dashboard.PomeriumSession.User)
    - [QueryGroupsRequest](#pomerium.dashboard.QueryGroupsRequest)
    - [QueryGroupsResponse](#pomerium.dashboard.QueryGroupsResponse)
    - [QueryUsersRequest](#pomerium.dashboard.QueryUsersRequest)
    - [QueryUsersResponse](#pomerium.dashboard.QueryUsersResponse)
    - [RecoveryToken](#pomerium.dashboard.RecoveryToken)
    - [UserInfo](#pomerium.dashboard.UserInfo)
    - [UserInfo.NamespaceRolesEntry](#pomerium.dashboard.UserInfo.NamespaceRolesEntry)
  
    - [PomeriumServiceAccountService](#pomerium.dashboard.PomeriumServiceAccountService)
    - [PomeriumSessionService](#pomerium.dashboard.PomeriumSessionService)
    - [UserService](#pomerium.dashboard.UserService)
  
- [Scalar Value Types](#scalar-value-types)



<a name="activity_log.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## activity_log.proto



<a name="pomerium.dashboard.ActivityLogEntry"></a>

### ActivityLogEntry
ActivityLogEntry contains context associated with a change in the deployment
history


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| activity_type | [string](#string) |  | `DELETE` or `SET` |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| namespace_id | [string](#string) |  |  |
| namespace_name | [string](#string) |  |  |
| user_id | [string](#string) |  |  |
| user_name | [string](#string) |  |  |
| user_email | [string](#string) |  |  |
| entity_type | [string](#string) |  | `route` | `policy` | `settings` |
| entity_id | [string](#string) |  |  |
| entity_data | [string](#string) |  |  |
| diff_summary | [ActivityLogEntry.DiffSummary](#pomerium.dashboard.ActivityLogEntry.DiffSummary) |  |  |
| db_version | [uint64](#uint64) |  | databroker version this change synced to |
| session_id | [string](#string) |  |  |
| service_account_id | [string](#string) |  |  |
| impersonate_user_id | [string](#string) |  |  |
| impersonate_user_name | [string](#string) |  |  |
| impersonate_user_email | [string](#string) |  |  |
| impersonate_user_groups | [string](#string) | repeated |  |






<a name="pomerium.dashboard.ActivityLogEntry.DiffSummary"></a>

### ActivityLogEntry.DiffSummary



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| added | [int64](#int64) |  | number of lines added |
| removed | [int64](#int64) |  | number of lines removed |






<a name="pomerium.dashboard.GetActivityLogEntryRequest"></a>

### GetActivityLogEntryRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetActivityLogEntryResponse"></a>

### GetActivityLogEntryResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entry | [ActivityLogEntry](#pomerium.dashboard.ActivityLogEntry) |  |  |






<a name="pomerium.dashboard.ListActivityLogEntriesRequest"></a>

### ListActivityLogEntriesRequest
ListActivityLogEntriesRequest defines the types of Activity Log entries to
list


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_type | [string](#string) | optional | `DELETE` | `SET` |
| namespace_id | [string](#string) | optional |  |
| user_id | [string](#string) | optional |  |
| entity_type | [string](#string) | optional | `route` | `policy` | `settings` |
| entity_id | [string](#string) | optional |  |
| query | [string](#string) | optional | `newest` | `oldest` | `from` | `name` |
| offset | [int64](#int64) | optional | list entries starting from an offset in the total list |
| limit | [int64](#int64) | optional | limit the number of entries returned |
| db_versions | [uint64](#uint64) | repeated | databroker versions of the change |
| recurse_namespace | [bool](#bool) | optional | if true, show activity for the namespace and any child namespaces |
| entities | [ListActivityLogEntriesRequest.Entity](#pomerium.dashboard.ListActivityLogEntriesRequest.Entity) | repeated | the entities are a list of entities to retrieve the activity log for |
| sort | [ListActivityLogEntriesRequest.Sort](#pomerium.dashboard.ListActivityLogEntriesRequest.Sort) | optional |  |
| date_filter | [ListActivityLogEntriesRequest.DateFilter](#pomerium.dashboard.ListActivityLogEntriesRequest.DateFilter) |  |  |
| string_filter | [ListActivityLogEntriesRequest.StringFilter](#pomerium.dashboard.ListActivityLogEntriesRequest.StringFilter) |  |  |






<a name="pomerium.dashboard.ListActivityLogEntriesRequest.DateFilter"></a>

### ListActivityLogEntriesRequest.DateFilter
filter for dates


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| operator | [string](#string) |  | `=` | `!=` | `&lt;` | `&lt;=` | `&gt;` | `&gt;=` |
| date | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="pomerium.dashboard.ListActivityLogEntriesRequest.Entity"></a>

### ListActivityLogEntriesRequest.Entity
an entity is a single entity (route, policy, etc.)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  |  |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.ListActivityLogEntriesRequest.Sort"></a>

### ListActivityLogEntriesRequest.Sort
used to sort the db query


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| column | [string](#string) |  | `activity_type` | `created_at` | `namespace_name` | `user_name` | `user_email` | `entity_type` |
| direction | [string](#string) |  | `ASC` | `DESC` |






<a name="pomerium.dashboard.ListActivityLogEntriesRequest.StringFilter"></a>

### ListActivityLogEntriesRequest.StringFilter
filter for strings


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fieldName | [string](#string) |  |  |
| operator | [string](#string) |  | `contains` | `equals` | `startsWith` | `endsWith` |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.ListActivityLogEntriesResponse"></a>

### ListActivityLogEntriesResponse
ListActivityLogEntriesResponse is a list of Activity Log entries found from a
ListActivityLogEntriesRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entries | [ActivityLogEntry](#pomerium.dashboard.ActivityLogEntry) | repeated | Activity Log entries |
| total_count | [int64](#int64) |  |  |





 

 

 


<a name="pomerium.dashboard.ActivityLogService"></a>

### ActivityLogService
ActivityLogService tracks historical changes to configuration made through
Pomerium Enterprise

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetActivityLogEntry | [GetActivityLogEntryRequest](#pomerium.dashboard.GetActivityLogEntryRequest) | [GetActivityLogEntryResponse](#pomerium.dashboard.GetActivityLogEntryResponse) | GetActivityLogEntry retrieves a specific activity log entry |
| ListActivityLogEntries | [ListActivityLogEntriesRequest](#pomerium.dashboard.ListActivityLogEntriesRequest) | [ListActivityLogEntriesResponse](#pomerium.dashboard.ListActivityLogEntriesResponse) | ListActivityLogEntries lists activity log entries based on paramters in the ListActivityLogEntriesRequest |

 



<a name="console_config.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## console_config.proto



<a name="pomerium.dashboard.ConsoleConfig"></a>

### ConsoleConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_pairs | [KeyPair](#pomerium.dashboard.KeyPair) | repeated |  |
| namespaces | [Namespace](#pomerium.dashboard.Namespace) | repeated |  |
| policies | [Policy](#pomerium.dashboard.Policy) | repeated |  |
| routes | [Route](#pomerium.dashboard.Route) | repeated |  |
| settings | [Settings](#pomerium.dashboard.Settings) |  |  |





 

 

 

 



<a name="events.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## events.proto



<a name="pomerium.dashboard.Event"></a>

### Event
Event represents a single envoy DeltaDiscovery event


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| message | [string](#string) |  |  |
| code | [int32](#int32) |  |  |
| details | [string](#string) | repeated | JSON serialized details |
| config_version | [uint64](#uint64) |  | databroker config version |
| type_url | [string](#string) |  | envoy resource type (i.e. listener, cluster) |
| kind | [Event.EventKind](#pomerium.dashboard.Event.EventKind) |  | envoy event kind |
| resource_subscribed | [string](#string) | repeated | envoy clusters or listeners that were added to the configuration |
| resource_unsubscribed | [string](#string) | repeated | clusters or listeners that were removed from the envoy configuration |
| instance | [string](#string) |  | pomerium instance this event originated from |
| seq_no | [uint64](#uint64) |  | databroker record version during this event |
| nonce | [string](#string) |  |  |






<a name="pomerium.dashboard.SyncRequest"></a>

### SyncRequest







<a name="pomerium.dashboard.SyncResponse"></a>

### SyncResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| event | [Event](#pomerium.dashboard.Event) |  |  |





 


<a name="pomerium.dashboard.Event.EventKind"></a>

### Event.EventKind


| Name | Number | Description |
| ---- | ------ | ----------- |
| EVENT_KIND_UNDEFINED | 0 |  |
| EVENT_DISCOVERY_REQUEST_ACK | 1 | envoy_service_discovery_v3.DeltaDiscoveryRequest |
| EVENT_DISCOVERY_REQUEST_NACK | 2 |  |
| EVENT_DISCOVERY_RESPONSE | 3 | envoy_service_discovery_v3.DeltaDiscoveryResponse |


 

 


<a name="pomerium.dashboard.Events"></a>

### Events
Events represent configuration changes made to envoy&#39;s controle plane by
Pomerium

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Sync | [SyncRequest](#pomerium.dashboard.SyncRequest) | [SyncResponse](#pomerium.dashboard.SyncResponse) stream | Sync sends all current events and then pushes new events as they arrive |

 



<a name="key_chain.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## key_chain.proto



<a name="pomerium.dashboard.CertificateInfo"></a>

### CertificateInfo
CertificateInfo is a .proto reflection of
https://golang.org/pkg/crypto/x509/#Certificate


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [int64](#int64) |  |  |
| serial | [string](#string) |  |  |
| issuer | [Name](#pomerium.dashboard.Name) |  |  |
| subject | [Name](#pomerium.dashboard.Name) |  |  |
| not_before | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| not_after | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| key_usage | [KeyUsage](#pomerium.dashboard.KeyUsage) |  |  |
| dns_names | [string](#string) | repeated |  |
| email_addresses | [string](#string) | repeated |  |
| ip_addresses | [string](#string) | repeated |  |
| uris | [string](#string) | repeated |  |
| permitted_dns_domains_critical | [bool](#bool) |  |  |
| permitted_dns_domains | [string](#string) | repeated |  |
| excluded_dns_domains | [string](#string) | repeated |  |
| permitted_ip_ranges | [string](#string) | repeated |  |
| excluded_ip_ranges | [string](#string) | repeated |  |
| permitted_email_addresses | [string](#string) | repeated |  |
| excluded_email_addresses | [string](#string) | repeated |  |
| permitted_uri_domains | [string](#string) | repeated |  |
| excluded_uri_domains | [string](#string) | repeated |  |






<a name="pomerium.dashboard.CreateKeyPairRequest"></a>

### CreateKeyPairRequest
CreateKeyPairRequest defines a Key Pair to create


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| namespace_id | [string](#string) |  |  |
| format | [Format](#pomerium.dashboard.Format) |  | encoding format of data |
| certificate | [bytes](#bytes) |  | public certificate data |
| key | [bytes](#bytes) |  | private key data |






<a name="pomerium.dashboard.CreateKeyPairResponse"></a>

### CreateKeyPairResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_pair | [KeyPairRecord](#pomerium.dashboard.KeyPairRecord) |  |  |






<a name="pomerium.dashboard.DeleteKeyPairRequest"></a>

### DeleteKeyPairRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeleteKeyPairResponse"></a>

### DeleteKeyPairResponse







<a name="pomerium.dashboard.GetKeyPairRequest"></a>

### GetKeyPairRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetKeyPairResponse"></a>

### GetKeyPairResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_pair | [KeyPairRecord](#pomerium.dashboard.KeyPairRecord) |  |  |






<a name="pomerium.dashboard.KeyPair"></a>

### KeyPair
KeyPair represents raw Key Pair data for internal usage


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| namespace_id | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| certificate | [bytes](#bytes) |  | public certificate data |
| key | [bytes](#bytes) |  | private key data |






<a name="pomerium.dashboard.KeyPairRecord"></a>

### KeyPairRecord
KeyPairRecord provides existing Key Pair metadata


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| namespace_id | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  | database record creation time |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  | database record modification time |
| cert_info | [CertificateInfo](#pomerium.dashboard.CertificateInfo) |  | information about the public certificate |
| has_private_key | [bool](#bool) |  | Key Pair has a private key attached |






<a name="pomerium.dashboard.KeyUsage"></a>

### KeyUsage
KeyUsage specifies the usage flags set on a signed TLS certificate


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| digital_signature | [bool](#bool) |  | standard key usages |
| content_commitment | [bool](#bool) |  |  |
| key_encipherment | [bool](#bool) |  |  |
| data_encipherment | [bool](#bool) |  |  |
| key_agreement | [bool](#bool) |  |  |
| cert_sign | [bool](#bool) |  | certificate authority |
| crl_sign | [bool](#bool) |  |  |
| encipher_only | [bool](#bool) |  |  |
| decipher_only | [bool](#bool) |  |  |
| server_auth | [bool](#bool) |  | extensions derived from x509.ExtKeyUsage server certificate |
| client_auth | [bool](#bool) |  | client certificate |






<a name="pomerium.dashboard.ListKeyPairsRequest"></a>

### ListKeyPairsRequest
ListKeyPairsRequest defines the types of key pairs to list


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_id | [string](#string) |  |  |
| query | [string](#string) | optional | list Key Pairs whose name contains the query string |
| offset | [int64](#int64) | optional | list Key Pairs starting from an offset in the total list |
| limit | [int64](#int64) | optional | limit the number of entries returned |
| order_by | [string](#string) | optional | `newest`, `oldest`, `name`, `from` |






<a name="pomerium.dashboard.ListKeyPairsResponse"></a>

### ListKeyPairsResponse
ListKeyPairsResponse is the list of Key Pairs found from a
ListKeyPairsRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_pairs | [KeyPairRecord](#pomerium.dashboard.KeyPairRecord) | repeated | Key Pairs found |
| total_count | [int64](#int64) |  |  |






<a name="pomerium.dashboard.Name"></a>

### Name
Name defines the x509 identity


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| country | [string](#string) | repeated |  |
| organization | [string](#string) | repeated |  |
| organizational_unit | [string](#string) | repeated |  |
| locality | [string](#string) | repeated |  |
| province | [string](#string) | repeated |  |
| street_address | [string](#string) | repeated |  |
| postal_code | [string](#string) | repeated |  |
| serial_number | [string](#string) |  |  |
| common_name | [string](#string) |  |  |






<a name="pomerium.dashboard.UpdateKeyPairRequest"></a>

### UpdateKeyPairRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| format | [Format](#pomerium.dashboard.Format) |  | encoding format of data |
| certificate | [bytes](#bytes) |  | public certificate data |
| key | [bytes](#bytes) |  | private key data |






<a name="pomerium.dashboard.UpdateKeyPairResponse"></a>

### UpdateKeyPairResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_pair | [KeyPairRecord](#pomerium.dashboard.KeyPairRecord) |  |  |





 


<a name="pomerium.dashboard.Format"></a>

### Format
Format specifies the encoding format of a certificate or key

| Name | Number | Description |
| ---- | ------ | ----------- |
| FORMAT_UNDEFINED_DO_NOT_USE | 0 |  |
| PEM | 1 |  |



<a name="pomerium.dashboard.PublicKeyAlgorithm"></a>

### PublicKeyAlgorithm
PublicKeyAlgorithm is the algorithm of a public key

| Name | Number | Description |
| ---- | ------ | ----------- |
| PKA_UNKNOWN_DO_NOT_USE | 0 |  |
| RSA | 1 |  |
| DSA | 2 |  |
| ECDSA | 3 |  |
| ED25519 | 4 |  |


 

 


<a name="pomerium.dashboard.KeyChainService"></a>

### KeyChainService
KeyChainService manages and store TLS Certificates, Keys and CAs, known as
Key Pairs

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DeleteKeyPair | [DeleteKeyPairRequest](#pomerium.dashboard.DeleteKeyPairRequest) | [DeleteKeyPairResponse](#pomerium.dashboard.DeleteKeyPairResponse) | DeleteKeyPair remove an x509 key pair based on a DeleteKeyPairRequest |
| GetKeyPair | [GetKeyPairRequest](#pomerium.dashboard.GetKeyPairRequest) | [GetKeyPairResponse](#pomerium.dashboard.GetKeyPairResponse) | GetKeyPair retrieves an existing key pair |
| ListKeyPairs | [ListKeyPairsRequest](#pomerium.dashboard.ListKeyPairsRequest) | [ListKeyPairsResponse](#pomerium.dashboard.ListKeyPairsResponse) | ListKeyPairs lists existing key pairs based on parameters in ListKeyPairsRequest |
| CreateKeyPair | [CreateKeyPairRequest](#pomerium.dashboard.CreateKeyPairRequest) | [CreateKeyPairResponse](#pomerium.dashboard.CreateKeyPairResponse) | CreateKeyPair creates a new key pair |
| UpdateKeyPair | [UpdateKeyPairRequest](#pomerium.dashboard.UpdateKeyPairRequest) | [UpdateKeyPairResponse](#pomerium.dashboard.UpdateKeyPairResponse) | CreateKeyPair creates a new key pair |

 



<a name="namespaces.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## namespaces.proto



<a name="pomerium.dashboard.DeleteNamespacePermissionRequest"></a>

### DeleteNamespacePermissionRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeleteNamespacePermissionResponse"></a>

### DeleteNamespacePermissionResponse







<a name="pomerium.dashboard.DeleteNamespaceRequest"></a>

### DeleteNamespaceRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeleteNamespaceResponse"></a>

### DeleteNamespaceResponse







<a name="pomerium.dashboard.GetNamespacePermissionRequest"></a>

### GetNamespacePermissionRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetNamespacePermissionResponse"></a>

### GetNamespacePermissionResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_permission | [NamespacePermission](#pomerium.dashboard.NamespacePermission) |  |  |






<a name="pomerium.dashboard.GetNamespaceRequest"></a>

### GetNamespaceRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetNamespaceResponse"></a>

### GetNamespaceResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace | [Namespace](#pomerium.dashboard.Namespace) |  |  |






<a name="pomerium.dashboard.ListNamespacePermissionGroupsRequest"></a>

### ListNamespacePermissionGroupsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_id | [string](#string) |  |  |






<a name="pomerium.dashboard.ListNamespacePermissionGroupsResponse"></a>

### ListNamespacePermissionGroupsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| groups | [NamespacePermissionGroup](#pomerium.dashboard.NamespacePermissionGroup) | repeated |  |






<a name="pomerium.dashboard.ListNamespacePermissionUsersRequest"></a>

### ListNamespacePermissionUsersRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_id | [string](#string) |  |  |






<a name="pomerium.dashboard.ListNamespacePermissionUsersResponse"></a>

### ListNamespacePermissionUsersResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| users | [NamespacePermissionUser](#pomerium.dashboard.NamespacePermissionUser) | repeated |  |






<a name="pomerium.dashboard.ListNamespacePermissionsRequest"></a>

### ListNamespacePermissionsRequest







<a name="pomerium.dashboard.ListNamespacePermissionsResponse"></a>

### ListNamespacePermissionsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_permissions | [NamespacePermission](#pomerium.dashboard.NamespacePermission) | repeated |  |






<a name="pomerium.dashboard.ListNamespacesRequest"></a>

### ListNamespacesRequest







<a name="pomerium.dashboard.ListNamespacesResponse"></a>

### ListNamespacesResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespaces | [Namespace](#pomerium.dashboard.Namespace) | repeated |  |






<a name="pomerium.dashboard.Namespace"></a>

### Namespace
Namespace defines a namespace


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| parent_id | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| deleted_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| name | [string](#string) |  |  |
| route_count | [int64](#int64) |  | computed |
| policy_count | [int64](#int64) |  | computed |






<a name="pomerium.dashboard.NamespacePermission"></a>

### NamespacePermission
NamespacePermission defines a permission binding to an identity


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| namespace_id | [string](#string) |  |  |
| namespace_name | [string](#string) |  |  |
| subject_type | [string](#string) |  |  |
| subject_id | [string](#string) |  |  |
| role | [string](#string) |  |  |






<a name="pomerium.dashboard.NamespacePermissionGroup"></a>

### NamespacePermissionGroup
NamespacePermissionGroup defines a permission binding to a group identity


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [string](#string) |  |  |
| group_name | [string](#string) |  |  |
| group_email | [string](#string) |  |  |
| namespace_id | [string](#string) |  |  |
| namespace_name | [string](#string) |  |  |
| role | [string](#string) |  |  |






<a name="pomerium.dashboard.NamespacePermissionUser"></a>

### NamespacePermissionUser
NamespacePermissionUser defines a permission binding to a user identity


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [string](#string) |  |  |
| user_name | [string](#string) |  |  |
| user_email | [string](#string) |  |  |
| group_ids | [string](#string) | repeated |  |
| namespace_id | [string](#string) |  |  |
| namespace_name | [string](#string) |  |  |
| role | [string](#string) |  |  |






<a name="pomerium.dashboard.SetNamespacePermissionRequest"></a>

### SetNamespacePermissionRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_permission | [NamespacePermission](#pomerium.dashboard.NamespacePermission) |  |  |






<a name="pomerium.dashboard.SetNamespacePermissionResponse"></a>

### SetNamespacePermissionResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace_permission | [NamespacePermission](#pomerium.dashboard.NamespacePermission) |  |  |






<a name="pomerium.dashboard.SetNamespaceRequest"></a>

### SetNamespaceRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace | [Namespace](#pomerium.dashboard.Namespace) |  |  |






<a name="pomerium.dashboard.SetNamespaceResponse"></a>

### SetNamespaceResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace | [Namespace](#pomerium.dashboard.Namespace) |  |  |





 

 

 


<a name="pomerium.dashboard.NamespacePermissionService"></a>

### NamespacePermissionService
NamespacePermissionService manages permissions set on namespaces

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DeleteNamespacePermission | [DeleteNamespacePermissionRequest](#pomerium.dashboard.DeleteNamespacePermissionRequest) | [DeleteNamespacePermissionResponse](#pomerium.dashboard.DeleteNamespacePermissionResponse) | DeleteNamespacePermission removes an existing permission definition |
| GetNamespacePermission | [GetNamespacePermissionRequest](#pomerium.dashboard.GetNamespacePermissionRequest) | [GetNamespacePermissionResponse](#pomerium.dashboard.GetNamespacePermissionResponse) | GetNamespacePermission retrieves an existing permission definition |
| ListNamespacePermissions | [ListNamespacePermissionsRequest](#pomerium.dashboard.ListNamespacePermissionsRequest) | [ListNamespacePermissionsResponse](#pomerium.dashboard.ListNamespacePermissionsResponse) | ListNamespacePermissions retrieves existing permissions for all namespaces |
| ListNamespacePermissionGroups | [ListNamespacePermissionGroupsRequest](#pomerium.dashboard.ListNamespacePermissionGroupsRequest) | [ListNamespacePermissionGroupsResponse](#pomerium.dashboard.ListNamespacePermissionGroupsResponse) | ListNamespacePermissionGroups retrieves existing group based permissions on a namespace |
| ListNamespacePermissionUsers | [ListNamespacePermissionUsersRequest](#pomerium.dashboard.ListNamespacePermissionUsersRequest) | [ListNamespacePermissionUsersResponse](#pomerium.dashboard.ListNamespacePermissionUsersResponse) | ListNamespacePermissionUsers retrieves existing user based permissions on a namespace |
| SetNamespacePermission | [SetNamespacePermissionRequest](#pomerium.dashboard.SetNamespacePermissionRequest) | [SetNamespacePermissionResponse](#pomerium.dashboard.SetNamespacePermissionResponse) | SetNamespacePermission set a new permission definition on a namespace |


<a name="pomerium.dashboard.NamespaceService"></a>

### NamespaceService
NamespaceService manages namespaces

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DeleteNamespace | [DeleteNamespaceRequest](#pomerium.dashboard.DeleteNamespaceRequest) | [DeleteNamespaceResponse](#pomerium.dashboard.DeleteNamespaceResponse) | DeleteNamespace deletes a namespace |
| GetNamespace | [GetNamespaceRequest](#pomerium.dashboard.GetNamespaceRequest) | [GetNamespaceResponse](#pomerium.dashboard.GetNamespaceResponse) | GetNamespace retrieves a namespace |
| ListNamespaces | [ListNamespacesRequest](#pomerium.dashboard.ListNamespacesRequest) | [ListNamespacesResponse](#pomerium.dashboard.ListNamespacesResponse) | ListNamespaces lists all namespaces |
| SetNamespace | [SetNamespaceRequest](#pomerium.dashboard.SetNamespaceRequest) | [SetNamespaceResponse](#pomerium.dashboard.SetNamespaceResponse) | SetNamespace creates a namespace or, if the id is specified, updates an existing namespace |

 



<a name="policy.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## policy.proto



<a name="pomerium.dashboard.DeletePolicyRequest"></a>

### DeletePolicyRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeletePolicyResponse"></a>

### DeletePolicyResponse







<a name="pomerium.dashboard.GetPolicyRequest"></a>

### GetPolicyRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetPolicyResponse"></a>

### GetPolicyResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| policy | [Policy](#pomerium.dashboard.Policy) |  |  |






<a name="pomerium.dashboard.ListPoliciesRequest"></a>

### ListPoliciesRequest
ListPoliciesRequest specifies the policies to list


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace | [string](#string) |  |  |
| query | [string](#string) | optional | list Policies whose name contains the query string |
| offset | [int64](#int64) | optional | list Policies starting from an offset in the total list |
| limit | [int64](#int64) | optional | limit the number of entries returned |
| order_by | [string](#string) | optional | sort the Policies by newest, oldest or name |






<a name="pomerium.dashboard.ListPoliciesResponse"></a>

### ListPoliciesResponse
ListPoliciesResponse is the list of policies found for a ListPoliciesRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| policies | [Policy](#pomerium.dashboard.Policy) | repeated |  |
| total_count | [int64](#int64) |  |  |






<a name="pomerium.dashboard.Policy"></a>

### Policy
Policy defines an authorization policy which can be applied to a route or
routes


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| namespace_id | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| deleted_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| allowed_users | [string](#string) | repeated |  |
| allowed_groups | [string](#string) | repeated |  |
| allowed_domains | [string](#string) | repeated |  |
| allowed_idp_claims | [Policy.AllowedIdpClaimsEntry](#pomerium.dashboard.Policy.AllowedIdpClaimsEntry) | repeated |  |
| rego | [string](#string) | repeated | custom rego definition in string format |
| ppl | [string](#string) |  | PPL definition in JSON format |
| enforced | [bool](#bool) |  | policy is automatically applied to all routes in namespace_id and child namespaces |
| routes | [Policy.RoutesEntry](#pomerium.dashboard.Policy.RoutesEntry) | repeated | computed

route id =&gt; name |
| namespace_name | [string](#string) |  | computed |






<a name="pomerium.dashboard.Policy.AllowedIdpClaimsEntry"></a>

### Policy.AllowedIdpClaimsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [google.protobuf.ListValue](#google.protobuf.ListValue) |  |  |






<a name="pomerium.dashboard.Policy.RoutesEntry"></a>

### Policy.RoutesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.SetPolicyRequest"></a>

### SetPolicyRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| policy | [Policy](#pomerium.dashboard.Policy) |  |  |






<a name="pomerium.dashboard.SetPolicyResponse"></a>

### SetPolicyResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| policy | [Policy](#pomerium.dashboard.Policy) |  |  |





 

 

 


<a name="pomerium.dashboard.PolicyService"></a>

### PolicyService
PolicyService manages policy creation and definition

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DeletePolicy | [DeletePolicyRequest](#pomerium.dashboard.DeletePolicyRequest) | [DeletePolicyResponse](#pomerium.dashboard.DeletePolicyResponse) | DeletePolicy deletes an existing policy |
| GetPolicy | [GetPolicyRequest](#pomerium.dashboard.GetPolicyRequest) | [GetPolicyResponse](#pomerium.dashboard.GetPolicyResponse) | GetPolicy retrieves an existing policy |
| ListPolicies | [ListPoliciesRequest](#pomerium.dashboard.ListPoliciesRequest) | [ListPoliciesResponse](#pomerium.dashboard.ListPoliciesResponse) | ListPolicies lists existing policies based on the ListPoliciesRequest parameters |
| SetPolicy | [SetPolicyRequest](#pomerium.dashboard.SetPolicyRequest) | [SetPolicyResponse](#pomerium.dashboard.SetPolicyResponse) | SetPolicy creates a new policy or, if the id is specified, updates an existing policy |

 



<a name="report.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## report.proto



<a name="pomerium.dashboard.PolicyReportRequest"></a>

### PolicyReportRequest
PolicyReportRequest may either specify a list of routes,
or request to report all routes of the namespace


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route_ids | [string](#string) | repeated |  |
| namespace_id | [string](#string) |  |  |






<a name="pomerium.dashboard.PolicyReportResponse"></a>

### PolicyReportResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| routes | [Route](#pomerium.dashboard.Route) | repeated |  |
| policies | [Policy](#pomerium.dashboard.Policy) | repeated |  |





 

 

 


<a name="pomerium.dashboard.Report"></a>

### Report


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PolicyReport | [PolicyReportRequest](#pomerium.dashboard.PolicyReportRequest) | [PolicyReportResponse](#pomerium.dashboard.PolicyReportResponse) | PolicyReport generates a policy report |

 



<a name="routes.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## routes.proto



<a name="pomerium.dashboard.DeleteRouteRequest"></a>

### DeleteRouteRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeleteRouteResponse"></a>

### DeleteRouteResponse







<a name="pomerium.dashboard.GetRouteRequest"></a>

### GetRouteRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetRouteResponse"></a>

### GetRouteResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route | [Route](#pomerium.dashboard.Route) |  |  |






<a name="pomerium.dashboard.ListRoutesRequest"></a>

### ListRoutesRequest
ListRoutesRequest defines the routes to list


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace | [string](#string) |  |  |
| query | [string](#string) | optional | list Routes who&#39;s name, from or to contains the query string |
| offset | [int64](#int64) | optional | list Routes starting from an offset in the total list |
| limit | [int64](#int64) | optional | limit the number of Route entries returned |
| order_by | [string](#string) | optional | sort the Routes by newest, oldest, name or from |






<a name="pomerium.dashboard.ListRoutesResponse"></a>

### ListRoutesResponse
ListRoutesResponse is the list of routes found for a ListRoutesRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| routes | [Route](#pomerium.dashboard.Route) | repeated |  |
| total_count | [int64](#int64) |  |  |






<a name="pomerium.dashboard.LoadRoutesRequest"></a>

### LoadRoutesRequest
LoadRoutesRequest creates a route based on a yaml payload


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| contents | [bytes](#bytes) |  | OSS pomerium policy block |






<a name="pomerium.dashboard.LoadRoutesResponse"></a>

### LoadRoutesResponse
LoadRoutesResponse contains the routes and policies crated from a
LoadRoutesRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| routes | [RouteWithPolicies](#pomerium.dashboard.RouteWithPolicies) | repeated |  |






<a name="pomerium.dashboard.MoveRoutesRequest"></a>

### MoveRoutesRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route_ids | [string](#string) | repeated |  |
| new_namespace_id | [string](#string) |  |  |






<a name="pomerium.dashboard.MoveRoutesResponse"></a>

### MoveRoutesResponse







<a name="pomerium.dashboard.Route"></a>

### Route
Route defines a proxy route&#39;s settings and policy associations


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| namespace_id | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| deleted_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| name | [string](#string) |  |  |
| stat_name | [string](#string) |  | name for prometheus stats, computed on first save |
| from | [string](#string) |  |  |
| to | [string](#string) | repeated |  |
| prefix | [string](#string) | optional |  |
| path | [string](#string) | optional |  |
| regex | [string](#string) | optional |  |
| prefix_rewrite | [string](#string) | optional |  |
| regex_rewrite_pattern | [string](#string) | optional |  |
| regex_rewrite_substitution | [string](#string) | optional |  |
| host_rewrite | [string](#string) | optional |  |
| host_rewrite_header | [string](#string) | optional |  |
| host_path_regex_rewrite_pattern | [string](#string) | optional |  |
| host_path_regex_rewrite_substitution | [string](#string) | optional |  |
| regex_priority_order | [int64](#int64) | optional |  |
| timeout | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| idle_timeout | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| allow_websockets | [bool](#bool) | optional |  |
| allow_spdy | [bool](#bool) | optional |  |
| tls_skip_verify | [bool](#bool) | optional |  |
| tls_server_name | [string](#string) | optional |  |
| tls_custom_ca_key_pair_id | [string](#string) | optional |  |
| tls_client_key_pair_id | [string](#string) | optional |  |
| tls_downstream_client_ca_key_pair_id | [string](#string) | optional |  |
| set_request_headers | [Route.SetRequestHeadersEntry](#pomerium.dashboard.Route.SetRequestHeadersEntry) | repeated |  |
| remove_request_headers | [string](#string) | repeated |  |
| rewrite_response_headers | [RouteRewriteHeader](#pomerium.dashboard.RouteRewriteHeader) | repeated |  |
| preserve_host_header | [bool](#bool) | optional |  |
| pass_identity_headers | [bool](#bool) | optional |  |
| kubernetes_service_account_token | [string](#string) | optional |  |
| envoy_opts | [envoy.config.cluster.v3.Cluster](#envoy.config.cluster.v3.Cluster) |  |  |
| redirect | [envoy.config.route.v3.RedirectAction](#envoy.config.route.v3.RedirectAction) |  |  |
| enable_google_cloud_serverless_authentication | [bool](#bool) |  |  |
| policy_ids | [string](#string) | repeated | policies applied to this route |
| policy_names | [string](#string) | repeated | computed properties (may be nil) |
| namespace_name | [string](#string) |  | computed |






<a name="pomerium.dashboard.Route.SetRequestHeadersEntry"></a>

### Route.SetRequestHeadersEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.RouteRewriteHeader"></a>

### RouteRewriteHeader



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [string](#string) |  |  |
| prefix | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.RouteWithPolicies"></a>

### RouteWithPolicies
RouteWithPolicies contains automatically created routes and policies from a
LoadRoutesRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route | [Route](#pomerium.dashboard.Route) |  |  |
| policies | [Policy](#pomerium.dashboard.Policy) | repeated |  |






<a name="pomerium.dashboard.SetRouteRequest"></a>

### SetRouteRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route | [Route](#pomerium.dashboard.Route) |  |  |






<a name="pomerium.dashboard.SetRouteResponse"></a>

### SetRouteResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route | [Route](#pomerium.dashboard.Route) |  |  |





 

 

 


<a name="pomerium.dashboard.RouteService"></a>

### RouteService
RouteService manages proxy route definitions

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DeleteRoute | [DeleteRouteRequest](#pomerium.dashboard.DeleteRouteRequest) | [DeleteRouteResponse](#pomerium.dashboard.DeleteRouteResponse) | DeleteRoute removes an existing route |
| GetRoute | [GetRouteRequest](#pomerium.dashboard.GetRouteRequest) | [GetRouteResponse](#pomerium.dashboard.GetRouteResponse) | GetRoute retrieves an existing route |
| ListRoutes | [ListRoutesRequest](#pomerium.dashboard.ListRoutesRequest) | [ListRoutesResponse](#pomerium.dashboard.ListRoutesResponse) | ListRoutes lists routes based on ListRoutesRequest |
| LoadRoutes | [LoadRoutesRequest](#pomerium.dashboard.LoadRoutesRequest) | [LoadRoutesResponse](#pomerium.dashboard.LoadRoutesResponse) | LoadRoutes imports routes from an existing OSS configuration |
| SetRoute | [SetRouteRequest](#pomerium.dashboard.SetRouteRequest) | [SetRouteResponse](#pomerium.dashboard.SetRouteResponse) | SetRoute creates or, if id is defined, updates an existing route |
| MoveRoutes | [MoveRoutesRequest](#pomerium.dashboard.MoveRoutesRequest) | [MoveRoutesResponse](#pomerium.dashboard.MoveRoutesResponse) | MoveRoutes takes an array of routeIds and moves them to a new namespace |

 



<a name="settings.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## settings.proto



<a name="pomerium.dashboard.GetSettingsRequest"></a>

### GetSettingsRequest







<a name="pomerium.dashboard.GetSettingsResponse"></a>

### GetSettingsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| settings | [Settings](#pomerium.dashboard.Settings) |  |  |






<a name="pomerium.dashboard.SetSettingsRequest"></a>

### SetSettingsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| settings | [Settings](#pomerium.dashboard.Settings) |  |  |






<a name="pomerium.dashboard.SetSettingsResponse"></a>

### SetSettingsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| settings | [Settings](#pomerium.dashboard.Settings) |  |  |






<a name="pomerium.dashboard.Settings"></a>

### Settings
Settings defines the global pomerium settings


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| installation_id | [string](#string) | optional |  |
| debug | [bool](#bool) | optional |  |
| log_level | [string](#string) | optional |  |
| proxy_log_level | [string](#string) | optional |  |
| shared_secret | [string](#string) | optional |  |
| services | [string](#string) | optional |  |
| address | [string](#string) | optional |  |
| insecure_server | [bool](#bool) | optional |  |
| dns_lookup_family | [string](#string) | optional |  |
| certificates | [Settings.Certificate](#pomerium.dashboard.Settings.Certificate) | repeated |  |
| http_redirect_addr | [string](#string) | optional |  |
| timeout_read | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| timeout_write | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| timeout_idle | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| authenticate_service_url | [string](#string) | optional |  |
| authenticate_callback_path | [string](#string) | optional |  |
| cookie_name | [string](#string) | optional |  |
| cookie_secret | [string](#string) | optional |  |
| cookie_domain | [string](#string) | optional |  |
| cookie_secure | [bool](#bool) | optional |  |
| cookie_http_only | [bool](#bool) | optional |  |
| cookie_expire | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| idp_client_id | [string](#string) | optional |  |
| idp_client_secret | [string](#string) | optional |  |
| idp_provider | [string](#string) | optional |  |
| idp_provider_url | [string](#string) | optional |  |
| scopes | [string](#string) | repeated |  |
| idp_service_account | [string](#string) | optional |  |
| idp_refresh_directory_timeout | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| idp_refresh_directory_interval | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| request_params | [Settings.RequestParamsEntry](#pomerium.dashboard.Settings.RequestParamsEntry) | repeated |  |
| authorize_service_url | [string](#string) | optional |  |
| certificate_authority | [string](#string) | optional |  |
| certificate_authority_file | [string](#string) | optional |  |
| certificate_authority_key_pair_id | [string](#string) | optional |  |
| set_response_headers | [Settings.SetResponseHeadersEntry](#pomerium.dashboard.Settings.SetResponseHeadersEntry) | repeated |  |
| jwt_claims_headers | [Settings.JwtClaimsHeadersEntry](#pomerium.dashboard.Settings.JwtClaimsHeadersEntry) | repeated |  |
| default_upstream_timeout | [google.protobuf.Duration](#google.protobuf.Duration) | optional |  |
| metrics_address | [string](#string) | optional |  |
| tracing_provider | [string](#string) | optional |  |
| tracing_sample_rate | [double](#double) | optional |  |
| tracing_jaeger_collector_endpoint | [string](#string) | optional |  |
| tracing_jaeger_agent_endpoint | [string](#string) | optional |  |
| tracing_zipkin_endpoint | [string](#string) | optional |  |
| grpc_address | [string](#string) | optional |  |
| grpc_insecure | [bool](#bool) | optional |  |
| forward_auth_url | [string](#string) | optional |  |
| cache_service_url | [string](#string) | optional |  |
| databroker_service_url | [string](#string) | optional |  |
| client_ca | [string](#string) | optional |  |
| client_ca_file | [string](#string) | optional |  |
| client_ca_key_pair_id | [string](#string) | optional |  |
| google_cloud_serverless_authentication_service_account | [string](#string) | optional |  |
| autocert | [bool](#bool) | optional |  |
| autocert_use_staging | [bool](#bool) | optional |  |
| autocert_must_staple | [bool](#bool) | optional |  |
| autocert_dir | [string](#string) | optional |  |
| skip_xff_append | [bool](#bool) | optional |  |






<a name="pomerium.dashboard.Settings.Certificate"></a>

### Settings.Certificate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cert_bytes | [bytes](#bytes) |  |  |
| key_bytes | [bytes](#bytes) |  |  |
| key_pair_id | [string](#string) |  |  |






<a name="pomerium.dashboard.Settings.JwtClaimsHeadersEntry"></a>

### Settings.JwtClaimsHeadersEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.Settings.RequestParamsEntry"></a>

### Settings.RequestParamsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.Settings.SetResponseHeadersEntry"></a>

### Settings.SetResponseHeadersEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |





 

 

 


<a name="pomerium.dashboard.SettingsService"></a>

### SettingsService
SettingsService manages global pomerium settings

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetSettings | [GetSettingsRequest](#pomerium.dashboard.GetSettingsRequest) | [GetSettingsResponse](#pomerium.dashboard.GetSettingsResponse) | GetSettings retrieves the currently applied settings |
| SetSettings | [SetSettingsRequest](#pomerium.dashboard.SetSettingsRequest) | [SetSettingsResponse](#pomerium.dashboard.SetSettingsResponse) | SetSettings applies new global settings |

 



<a name="tsdb.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## tsdb.proto



<a name="pomerium.dashboard.GetInstanceInfoRequest"></a>

### GetInstanceInfoRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| component | [Component](#pomerium.dashboard.Component) |  |  |
| instance_id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetInstancesRequest"></a>

### GetInstancesRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="pomerium.dashboard.GetStatusRequest"></a>

### GetStatusRequest







<a name="pomerium.dashboard.GetStatusResponse"></a>

### GetStatusResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| targets | [GetStatusResponse.Target](#pomerium.dashboard.GetStatusResponse.Target) | repeated |  |
| ok | [bool](#bool) |  |  |
| last_error | [string](#string) |  |  |






<a name="pomerium.dashboard.GetStatusResponse.Target"></a>

### GetStatusResponse.Target



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scrape_url | [string](#string) |  |  |
| global_url | [string](#string) |  |  |
| last_error | [string](#string) |  |  |
| last_scrape | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| health | [GetStatusResponse.Target.Health](#pomerium.dashboard.GetStatusResponse.Target.Health) |  |  |






<a name="pomerium.dashboard.Instances"></a>

### Instances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instances | [Instances.Instance](#pomerium.dashboard.Instances.Instance) | repeated |  |






<a name="pomerium.dashboard.Instances.Instance"></a>

### Instances.Instance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| component | [Component](#pomerium.dashboard.Component) |  |  |
| id | [string](#string) |  | ID that should be used in requests for metrics |
| name | [string](#string) |  | human readable instance name |






<a name="pomerium.dashboard.Labels"></a>

### Labels



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| labels | [Labels.LabelsEntry](#pomerium.dashboard.Labels.LabelsEntry) | repeated |  |






<a name="pomerium.dashboard.Labels.LabelsEntry"></a>

### Labels.LabelsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.Matrix"></a>

### Matrix



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| series | [TimeSeries](#pomerium.dashboard.TimeSeries) | repeated |  |






<a name="pomerium.dashboard.Range"></a>

### Range



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  | Start time |
| end | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  | End time |
| step | [google.protobuf.Duration](#google.protobuf.Duration) |  | Max time between two slices within [start:end] |






<a name="pomerium.dashboard.RouteMatcher"></a>

### RouteMatcher
RouteMatcher may be used to query data for multiple routes


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| route_id | [string](#string) |  | route database ID |
| namespace_id | [string](#string) |  | namespace ID |






<a name="pomerium.dashboard.RouteMetricChangeRequest"></a>

### RouteMetricChangeRequest
Used to request a particular metric change within a given period of time


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| matcher | [RouteMatcher](#pomerium.dashboard.RouteMatcher) |  | route to match |
| metric | [Metric](#pomerium.dashboard.Metric) |  | metric to retrieve |
| start | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  | Start time |
| end | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  | End time |






<a name="pomerium.dashboard.RouteMetricSeriesHistogramRequest"></a>

### RouteMetricSeriesHistogramRequest
request route-specific metric time series histogram


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| matcher | [RouteMatcher](#pomerium.dashboard.RouteMatcher) |  | route to match |
| metric | [Metric](#pomerium.dashboard.Metric) |  | metric to retrieve |
| range | [Range](#pomerium.dashboard.Range) |  | time range and sampling step |
| percentile | [double](#double) |  | if data for the metric was precomputed as histogram, the data may be requested within a certain percentile |






<a name="pomerium.dashboard.RouteMetricSeriesRequest"></a>

### RouteMetricSeriesRequest
request route-specific metric time series


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| matcher | [RouteMatcher](#pomerium.dashboard.RouteMatcher) |  | route to match |
| metric | [Metric](#pomerium.dashboard.Metric) |  | metric to retrieve |
| range | [Range](#pomerium.dashboard.Range) |  | time range and sampling step |






<a name="pomerium.dashboard.Sample"></a>

### Sample



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| labels | [Sample.LabelsEntry](#pomerium.dashboard.Sample.LabelsEntry) | repeated |  |
| value | [Scalar](#pomerium.dashboard.Scalar) |  |  |






<a name="pomerium.dashboard.Sample.LabelsEntry"></a>

### Sample.LabelsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.Scalar"></a>

### Scalar



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [double](#double) |  |  |
| ts | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="pomerium.dashboard.ScalarBuckets"></a>

### ScalarBuckets
returns histogram values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buckets | [ScalarBuckets.Bucket](#pomerium.dashboard.ScalarBuckets.Bucket) | repeated |  |






<a name="pomerium.dashboard.ScalarBuckets.Bucket"></a>

### ScalarBuckets.Bucket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| less_or_equal_than | [double](#double) |  | bucket identifier |
| count | [int64](#int64) |  | occurences for the given bucket |






<a name="pomerium.dashboard.ServerMetricRequest"></a>

### ServerMetricRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| component | [Component](#pomerium.dashboard.Component) |  |  |
| instance_id | [string](#string) |  |  |
| metric | [Metric](#pomerium.dashboard.Metric) |  | metric to retrieve |






<a name="pomerium.dashboard.ServerMetricSeriesRequest"></a>

### ServerMetricSeriesRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| metric | [Metric](#pomerium.dashboard.Metric) |  | metric to retrieve |
| range | [Range](#pomerium.dashboard.Range) |  | time range and sampling step |
| percentile | [double](#double) |  | if data for the metric was precomputed as histogram, the data may be requested within a certain percentile |
| component | [Component](#pomerium.dashboard.Component) |  | server component and instance ID |
| instance_id | [string](#string) |  |  |






<a name="pomerium.dashboard.String"></a>

### String



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |
| ts | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="pomerium.dashboard.TimeSeries"></a>

### TimeSeries



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| labels | [TimeSeries.LabelsEntry](#pomerium.dashboard.TimeSeries.LabelsEntry) | repeated |  |
| series | [Scalar](#pomerium.dashboard.Scalar) | repeated |  |






<a name="pomerium.dashboard.TimeSeries.LabelsEntry"></a>

### TimeSeries.LabelsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="pomerium.dashboard.TimeSeriesResponse"></a>

### TimeSeriesResponse
TimeSeries response returns


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rate | [Rate](#pomerium.dashboard.Rate) |  | provided for time-sampled values - i.e. requests &lt;per second&gt; |
| series | [Scalar](#pomerium.dashboard.Scalar) | repeated | series are (timestamp,value) data points |






<a name="pomerium.dashboard.TimeSeriesResponseMulti"></a>

### TimeSeriesResponseMulti
Multiple time series response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rate | [Rate](#pomerium.dashboard.Rate) |  |  |
| series | [TimeSeries](#pomerium.dashboard.TimeSeries) | repeated |  |






<a name="pomerium.dashboard.UptimeRequest"></a>

### UptimeRequest
uptime info for all pomerium services for a given period of time


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| component | [Component](#pomerium.dashboard.Component) |  |  |
| instance_id | [string](#string) |  |  |






<a name="pomerium.dashboard.UptimeResponse"></a>

### UptimeResponse
service uptime is calculated based on liveness probe published by each
component it is delivered as 2-level hierarchical periods to make it simple
for the UI consumer it does not provide statistics as data representation
makes it trivial to calculate depending on the UI requirements


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| intervals | [UptimeResponse.Summary](#pomerium.dashboard.UptimeResponse.Summary) | repeated |  |






<a name="pomerium.dashboard.UptimeResponse.Summary"></a>

### UptimeResponse.Summary
summary provides a higher level information re health of the component


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| status | [UptimeResponse.Status](#pomerium.dashboard.UptimeResponse.Status) |  | aggregate status of the system |






<a name="pomerium.dashboard.Vector"></a>

### Vector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| samples | [Sample](#pomerium.dashboard.Sample) | repeated |  |





 


<a name="pomerium.dashboard.Component"></a>

### Component


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN_DO_NOT_USE | 0 |  |
| AUTHENTICATE | 1 |  |
| AUTHORIZE | 2 |  |
| DATABROKER | 3 |  |
| CONSOLE | 4 |  |
| PROXY | 5 |  |
| ALL_IN_ONE | 6 | used when all components are running in the all-in-one mode |
| PROXY_ENVOY | 7 | Proxy envoy is always reported separately |
| PROMETHEUS | 8 |  |



<a name="pomerium.dashboard.GetStatusResponse.Target.Health"></a>

### GetStatusResponse.Target.Health


| Name | Number | Description |
| ---- | ------ | ----------- |
| TARGET_HEALTH_UNKNOWN | 0 |  |
| TARGET_HEALTH_UP | 1 |  |
| TARGET_HEALTH_DOWN | 2 |  |



<a name="pomerium.dashboard.Metric"></a>

### Metric
see
https://www.envoyproxy.io/docs/envoy/latest/configuration/upstream/cluster_manager/cluster_stats

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_METRIC_DO_NOT_USE | 0 |  |
| REQUESTS | 1 | request counter |
| REQUESTS_RATE | 2 | request rate (per second) |
| REQUESTS_DURATION_MS | 3 | duration of the request in milliseconds - this is a histogram counter and requires percentile |
| RESPONSE_CODES | 4 | returns distribution of response codes |
| AUTHZ_OK | 20 | Total responses from the authz filter (note that does not imply that requests were allowed to pass thru) |
| AUTHZ_DENIED | 21 | Total responses from the authorizations service that were to deny the traffic. |
| AUTHZ_ERROR | 22 | Total errors contacting the external service. |
| AUTHZ_DISABLED | 23 | Total requests that are allowed without calling external services due to the filter is disabled. |
| AUTHZ_FAILURE_MODE_ALLOWED | 24 | Total requests that were error(s) but were allowed through because of failure_mode_allow set to true. |
| MEMBERSHIP_HEALTHY | 30 | Current cluster healthy total (inclusive of both health checking and outlier detection) |
| MEMBERSHIP_DEGRADED | 31 | Current cluster degraded total |
| MEMBERSHIP_EXCLUDED | 32 | Current cluster excluded total |
| MEMBERSHIP_TOTAL | 33 | Current cluster membership total |
| RX_BYTES | 40 | bytes received - upstream_cx_rx_bytes_total |
| TX_BYTES | 41 | bytes sent - upstream_cx_tx_bytes_total |
| TOTAL_BYTES | 42 | total of rx &#43; tx bytes |
| MEMORY_ALLOCATED | 51 | system metrics |
| CPU_USAGE | 52 |  |
| IDP_LAST_REFRESH_TIMESTAMP | 60 | identity provider specific |
| CONFIG_LAST_RELOAD_SUCCESS_TIMESTAMP | 70 | configuration related |
| BUILD_INFO | 71 |  |
| CONFIG_CHECKSUM_LOCAL | 72 |  |
| CONFIG_CHECKSUM_DATABROKER | 73 |  |
| CONFIG_VERSION | 74 |  |
| CONFIG_ERRORS | 75 |  |
| CONFIG_CONSOLE_VERSION | 76 |  |
| PROMETHEUS_STORAGE_BYTES | 80 | prometheus metrics |



<a name="pomerium.dashboard.Rate"></a>

### Rate
Rate defines time-sampled values

| Name | Number | Description |
| ---- | ------ | ----------- |
| NONE | 0 | undefined means this is an actual value that is not sampled |
| PER_SECOND | 1 | value represents &lt;something&gt; per second |



<a name="pomerium.dashboard.UptimeResponse.Status"></a>

### UptimeResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_STATUS_DO_NOT_USE | 0 |  |
| LIVE | 1 | fully operational |
| NO_DATA | 2 | no data is available for the period in the prometheus |
| DOWN | 3 | prometheus is up but the scraping instance is down |


 

 


<a name="pomerium.dashboard.TimeSeriesDB"></a>

### TimeSeriesDB
TimeSeriesDB is a generic service that is meant to be able to query for
historical metrics and should provide a sufficient abstraction between the UI
and underlying time series service, would it be Prometheus, embedded TSDB or
other 3rd party provider

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRouteMetricChange | [RouteMetricChangeRequest](#pomerium.dashboard.RouteMetricChangeRequest) | [Scalar](#pomerium.dashboard.Scalar) | returns metric change for a period of time |
| GetRouteMetricChangeHistogram | [RouteMetricChangeRequest](#pomerium.dashboard.RouteMetricChangeRequest) | [ScalarBuckets](#pomerium.dashboard.ScalarBuckets) | returns buckets of values for a given metric |
| GetRouteMetricSeries | [RouteMetricSeriesRequest](#pomerium.dashboard.RouteMetricSeriesRequest) | [TimeSeriesResponse](#pomerium.dashboard.TimeSeriesResponse) | returns metric change as time series |
| GetRouteMetricSeriesHistogram | [RouteMetricSeriesHistogramRequest](#pomerium.dashboard.RouteMetricSeriesHistogramRequest) | [TimeSeriesResponse](#pomerium.dashboard.TimeSeriesResponse) | returns metric change as time series |
| GetRouteMetricSeriesMulti | [RouteMetricSeriesRequest](#pomerium.dashboard.RouteMetricSeriesRequest) | [TimeSeriesResponseMulti](#pomerium.dashboard.TimeSeriesResponseMulti) | returns multiple annotated time series |
| GetUptime | [UptimeRequest](#pomerium.dashboard.UptimeRequest) | [UptimeResponse](#pomerium.dashboard.UptimeResponse) | returns service uptime statistics |
| GetInstances | [GetInstancesRequest](#pomerium.dashboard.GetInstancesRequest) | [Instances](#pomerium.dashboard.Instances) | returns list of system services with metrics |
| GetServerMetricSeries | [ServerMetricSeriesRequest](#pomerium.dashboard.ServerMetricSeriesRequest) | [TimeSeriesResponse](#pomerium.dashboard.TimeSeriesResponse) | returns server queries |
| GetServerMetric | [ServerMetricRequest](#pomerium.dashboard.ServerMetricRequest) | [Sample](#pomerium.dashboard.Sample) | returns current metric value |
| GetStatus | [GetStatusRequest](#pomerium.dashboard.GetStatusRequest) | [GetStatusResponse](#pomerium.dashboard.GetStatusResponse) | returns current status of scraping targets |

 



<a name="users.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## users.proto



<a name="pomerium.dashboard.AddPomeriumServiceAccountRequest"></a>

### AddPomeriumServiceAccountRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service_account | [PomeriumServiceAccount](#pomerium.dashboard.PomeriumServiceAccount) |  |  |






<a name="pomerium.dashboard.AddPomeriumServiceAccountResponse"></a>

### AddPomeriumServiceAccountResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service_account | [PomeriumServiceAccount](#pomerium.dashboard.PomeriumServiceAccount) |  |  |
| JWT | [string](#string) |  |  |






<a name="pomerium.dashboard.DeletePomeriumServiceAccountRequest"></a>

### DeletePomeriumServiceAccountRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeletePomeriumServiceAccountResponse"></a>

### DeletePomeriumServiceAccountResponse







<a name="pomerium.dashboard.DeletePomeriumSessionRequest"></a>

### DeletePomeriumSessionRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.DeletePomeriumSessionResponse"></a>

### DeletePomeriumSessionResponse







<a name="pomerium.dashboard.GetPomeriumServiceAccountRequest"></a>

### GetPomeriumServiceAccountRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetPomeriumServiceAccountResponse"></a>

### GetPomeriumServiceAccountResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service_account | [PomeriumServiceAccount](#pomerium.dashboard.PomeriumServiceAccount) |  |  |






<a name="pomerium.dashboard.GetPomeriumSessionRequest"></a>

### GetPomeriumSessionRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="pomerium.dashboard.GetPomeriumSessionResponse"></a>

### GetPomeriumSessionResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| session | [PomeriumSession](#pomerium.dashboard.PomeriumSession) |  |  |






<a name="pomerium.dashboard.GetUserInfoRequest"></a>

### GetUserInfoRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [string](#string) | optional |  |






<a name="pomerium.dashboard.GetUserInfoResponse"></a>

### GetUserInfoResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_info | [UserInfo](#pomerium.dashboard.UserInfo) |  |  |






<a name="pomerium.dashboard.GroupInfo"></a>

### GroupInfo
GroupInfo defines a directory group in the databroker


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |






<a name="pomerium.dashboard.ImpersonateRequest"></a>

### ImpersonateRequest
ImpersonateRequest defines the identity information to impersonate


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| session_id | [string](#string) |  |  |






<a name="pomerium.dashboard.ImpersonateResponse"></a>

### ImpersonateResponse







<a name="pomerium.dashboard.ListPomeriumServiceAccountsRequest"></a>

### ListPomeriumServiceAccountsRequest
ListPomeriumServiceAccountsRequest specifies the service accounts to list


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| namespace | [string](#string) |  |  |






<a name="pomerium.dashboard.ListPomeriumServiceAccountsResponse"></a>

### ListPomeriumServiceAccountsResponse
ListPomeriumServiceAccountsResponse is the list of service accounts found for
a ListPomeriumServiceAccountsRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service_accounts | [PomeriumServiceAccount](#pomerium.dashboard.PomeriumServiceAccount) | repeated |  |






<a name="pomerium.dashboard.ListPomeriumSessionsRequest"></a>

### ListPomeriumSessionsRequest
ListPomeriumSessionsRequest specifies the sessions to list


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [string](#string) | optional | list Sessions with any fields that contain the query string |
| offset | [int64](#int64) | optional | list Sessions starting from an offset in the total list |
| limit | [int64](#int64) | optional | limit the number of Session entries returned |
| order_by | [string](#string) | optional | sort the Sessions by newest, oldest or name |
| user_id | [string](#string) | optional |  |






<a name="pomerium.dashboard.ListPomeriumSessionsResponse"></a>

### ListPomeriumSessionsResponse
ListPomeriumSessionsResponse is the sessions found for a
ListPomeriumSessionsRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sessions | [PomeriumSession](#pomerium.dashboard.PomeriumSession) | repeated |  |
| total_count | [int64](#int64) |  |  |






<a name="pomerium.dashboard.PomeriumServiceAccount"></a>

### PomeriumServiceAccount
PomeriumServiceAccount defines the identity properties of a service account


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| namespace_id | [string](#string) | optional |  |
| user_id | [string](#string) |  |  |
| expires_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| issued_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="pomerium.dashboard.PomeriumSession"></a>

### PomeriumSession
PomeriumSession defines a user session from the databroker


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| user | [PomeriumSession.User](#pomerium.dashboard.PomeriumSession.User) |  |  |
| groups | [PomeriumSession.Group](#pomerium.dashboard.PomeriumSession.Group) | repeated |  |
| issuer | [string](#string) |  |  |
| issued_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| expires_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| audience | [string](#string) | repeated |  |
| claims | [PomeriumSession.ClaimsEntry](#pomerium.dashboard.PomeriumSession.ClaimsEntry) | repeated |  |






<a name="pomerium.dashboard.PomeriumSession.ClaimsEntry"></a>

### PomeriumSession.ClaimsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [google.protobuf.ListValue](#google.protobuf.ListValue) |  |  |






<a name="pomerium.dashboard.PomeriumSession.Group"></a>

### PomeriumSession.Group



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| email | [string](#string) |  |  |






<a name="pomerium.dashboard.PomeriumSession.User"></a>

### PomeriumSession.User



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| email | [string](#string) |  |  |






<a name="pomerium.dashboard.QueryGroupsRequest"></a>

### QueryGroupsRequest
QueryGroupsRequest defines the groups to retrieve


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [string](#string) |  |  |
| offset | [int64](#int64) |  |  |
| limit | [int64](#int64) |  |  |






<a name="pomerium.dashboard.QueryGroupsResponse"></a>

### QueryGroupsResponse
QueryGroupsResponse is the list of groups retrieved from a QueryGroupsRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| groups | [GroupInfo](#pomerium.dashboard.GroupInfo) | repeated |  |
| total_count | [int64](#int64) |  |  |






<a name="pomerium.dashboard.QueryUsersRequest"></a>

### QueryUsersRequest
QueryUsersRequest defines the users to retrieve


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [string](#string) |  | list Users with any fields that match the query |
| offset | [int64](#int64) |  | list Users starting from an offset in the total list |
| limit | [int64](#int64) |  | limit the number of User entries returned |






<a name="pomerium.dashboard.QueryUsersResponse"></a>

### QueryUsersResponse
QueryUsersResponse is the list of users retrieved from a QueryUsersRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| users | [UserInfo](#pomerium.dashboard.UserInfo) | repeated |  |
| total_count | [int64](#int64) |  |  |






<a name="pomerium.dashboard.RecoveryToken"></a>

### RecoveryToken
RecoveryToken is a recovery account for logging into the console without a
functioning Pomerium proxy


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| namespace | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| modified_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| expires_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| public_key | [string](#string) |  |  |






<a name="pomerium.dashboard.UserInfo"></a>

### UserInfo
UserInfo defines the metadata for a directory user in the databroker


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| email | [string](#string) |  |  |
| groups | [string](#string) | repeated |  |
| namespace_roles | [UserInfo.NamespaceRolesEntry](#pomerium.dashboard.UserInfo.NamespaceRolesEntry) | repeated |  |
| picture_url | [string](#string) |  |  |
| is_impersonated | [bool](#bool) |  |  |






<a name="pomerium.dashboard.UserInfo.NamespaceRolesEntry"></a>

### UserInfo.NamespaceRolesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |





 

 

 


<a name="pomerium.dashboard.PomeriumServiceAccountService"></a>

### PomeriumServiceAccountService
PomeriumServiceAccountService manages service accounts for use with the
pomerium console API

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| AddPomeriumServiceAccount | [AddPomeriumServiceAccountRequest](#pomerium.dashboard.AddPomeriumServiceAccountRequest) | [AddPomeriumServiceAccountResponse](#pomerium.dashboard.AddPomeriumServiceAccountResponse) | AddPomeriumServiceAccount creates a new service account |
| DeletePomeriumServiceAccount | [DeletePomeriumServiceAccountRequest](#pomerium.dashboard.DeletePomeriumServiceAccountRequest) | [DeletePomeriumServiceAccountResponse](#pomerium.dashboard.DeletePomeriumServiceAccountResponse) | DeletePomeriumServiceAccount removes an existing service account |
| GetPomeriumServiceAccount | [GetPomeriumServiceAccountRequest](#pomerium.dashboard.GetPomeriumServiceAccountRequest) | [GetPomeriumServiceAccountResponse](#pomerium.dashboard.GetPomeriumServiceAccountResponse) | GetPomeriumServiceAccount retrieves an existing service account |
| ListPomeriumServiceAccounts | [ListPomeriumServiceAccountsRequest](#pomerium.dashboard.ListPomeriumServiceAccountsRequest) | [ListPomeriumServiceAccountsResponse](#pomerium.dashboard.ListPomeriumServiceAccountsResponse) | ListPomeriumServiceAccounts lists service accounts based on the parameters in ListPomeriumServiceAccountsRequest |


<a name="pomerium.dashboard.PomeriumSessionService"></a>

### PomeriumSessionService
PomeriumSessionService manages user sessions inside the databroker

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DeletePomeriumSession | [DeletePomeriumSessionRequest](#pomerium.dashboard.DeletePomeriumSessionRequest) | [DeletePomeriumSessionResponse](#pomerium.dashboard.DeletePomeriumSessionResponse) | DeletePomeriumSession clears an existing user session |
| GetPomeriumSession | [GetPomeriumSessionRequest](#pomerium.dashboard.GetPomeriumSessionRequest) | [GetPomeriumSessionResponse](#pomerium.dashboard.GetPomeriumSessionResponse) | GetPomeriumSession retrieves information about an existing user session |
| Impersonate | [ImpersonateRequest](#pomerium.dashboard.ImpersonateRequest) | [ImpersonateResponse](#pomerium.dashboard.ImpersonateResponse) | Impersonate updates an existing session to impersonate another identity |
| ListPomeriumSessions | [ListPomeriumSessionsRequest](#pomerium.dashboard.ListPomeriumSessionsRequest) | [ListPomeriumSessionsResponse](#pomerium.dashboard.ListPomeriumSessionsResponse) | ListPomeriumSessions lists existing sessions based on the parameters of ListPomeriumSessionsRequest |


<a name="pomerium.dashboard.UserService"></a>

### UserService
UserService supports querying directory data from the databroker

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetUserInfo | [GetUserInfoRequest](#pomerium.dashboard.GetUserInfoRequest) | [GetUserInfoResponse](#pomerium.dashboard.GetUserInfoResponse) | GetUserInfo retrieves identity information and permission mappings for a user |
| QueryGroups | [QueryGroupsRequest](#pomerium.dashboard.QueryGroupsRequest) | [QueryGroupsResponse](#pomerium.dashboard.QueryGroupsResponse) | QueryGroups retrieves groups from the databroker based on QueryGroupsRequest parameters |
| QueryUsers | [QueryUsersRequest](#pomerium.dashboard.QueryUsersRequest) | [QueryUsersResponse](#pomerium.dashboard.QueryUsersResponse) | QueryUsers retrieves users from the databroker based on QueryUsersRequest parameters |

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

