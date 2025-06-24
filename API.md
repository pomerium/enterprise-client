# Contents




  - [ActivityLogService](#activitylogservice)
  
    - [GetActivityLogEntry](#getactivitylogentry)
  
    - [ListActivityLogEntries](#listactivitylogentries)
  





  - [ClustersService](#clustersservice)
  
    - [AddCluster](#addcluster)
  
    - [DeleteCluster](#deletecluster)
  
    - [GetCluster](#getcluster)
  
    - [ListClusters](#listclusters)
  
    - [UpdateCluster](#updatecluster)
  





  - [DeviceService](#deviceservice)
  
    - [ApproveDevice](#approvedevice)
  
    - [CreateDeviceEnrollment](#createdeviceenrollment)
  
    - [SetDeviceType](#setdevicetype)
  
    - [DeleteDevice](#deletedevice)
  
    - [DeleteDeviceType](#deletedevicetype)
  
    - [ListDevices](#listdevices)
  
    - [ListDeviceTypes](#listdevicetypes)
  





  - [ExternalDataSourceService](#externaldatasourceservice)
  
    - [DeleteExternalDataSource](#deleteexternaldatasource)
  
    - [GetExternalDataSource](#getexternaldatasource)
  
    - [ListExternalDataSources](#listexternaldatasources)
  
    - [ListExternalDataSourceRecordTypes](#listexternaldatasourcerecordtypes)
  
    - [ListExternalDataSourceRecordFields](#listexternaldatasourcerecordfields)
  
    - [SetExternalDataSource](#setexternaldatasource)
  





  - [KeyChainService](#keychainservice)
  
    - [DeleteKeyPair](#deletekeypair)
  
    - [GetKeyPair](#getkeypair)
  
    - [ListKeyPairs](#listkeypairs)
  
    - [CreateKeyPair](#createkeypair)
  
    - [UpdateKeyPair](#updatekeypair)
  





  - [NamespacePermissionService](#namespacepermissionservice)
  
    - [DeleteNamespacePermission](#deletenamespacepermission)
  
    - [GetNamespacePermission](#getnamespacepermission)
  
    - [ListNamespacePermissions](#listnamespacepermissions)
  
    - [ListNamespacePermissionGroups](#listnamespacepermissiongroups)
  
    - [ListNamespacePermissionUsers](#listnamespacepermissionusers)
  
    - [SetNamespacePermission](#setnamespacepermission)
  

  - [NamespaceService](#namespaceservice)
  
    - [DeleteNamespace](#deletenamespace)
  
    - [GetNamespace](#getnamespace)
  
    - [ListNamespaces](#listnamespaces)
  
    - [ListNamespaceResources](#listnamespaceresources)
  
    - [SetNamespace](#setnamespace)
  





  - [PolicyService](#policyservice)
  
    - [DeletePolicy](#deletepolicy)
  
    - [GetPolicy](#getpolicy)
  
    - [ListPolicies](#listpolicies)
  
    - [SetPolicy](#setpolicy)
  









  - [RouteService](#routeservice)
  
    - [DeleteRoute](#deleteroute)
  
    - [DeleteRoutes](#deleteroutes)
  
    - [GetRoute](#getroute)
  
    - [ListRoutes](#listroutes)
  
    - [LoadRoutes](#loadroutes)
  
    - [SetRoute](#setroute)
  
    - [SetRoutes](#setroutes)
  
    - [MoveRoutes](#moveroutes)
  





  - [SettingsService](#settingsservice)
  
    - [GetSettings](#getsettings)
  
    - [SetSettings](#setsettings)
  
    - [GetBrandingSettings](#getbrandingsettings)
  
    - [GetConsoleSettings](#getconsolesettings)
  







  - [PomeriumServiceAccountService](#pomeriumserviceaccountservice)
  
    - [AddPomeriumServiceAccount](#addpomeriumserviceaccount)
  
    - [DeletePomeriumServiceAccount](#deletepomeriumserviceaccount)
  
    - [GetPomeriumServiceAccount](#getpomeriumserviceaccount)
  
    - [ListPomeriumServiceAccounts](#listpomeriumserviceaccounts)
  
    - [SetPomeriumServiceAccount](#setpomeriumserviceaccount)
  

  - [PomeriumSessionService](#pomeriumsessionservice)
  
    - [DeletePomeriumSession](#deletepomeriumsession)
  
    - [GetPomeriumSession](#getpomeriumsession)
  
    - [Impersonate](#impersonate)
  
    - [ListPomeriumSessions](#listpomeriumsessions)
  

  - [UserService](#userservice)
  
    - [GetUserInfo](#getuserinfo)
  
    - [QueryGroups](#querygroups)
  
    - [QueryUsers](#queryusers)
  






# ActivityLogService
ActivityLogService tracks historical changes to configuration made through
Pomerium Enterprise

## Methods
### GetActivityLogEntry

> **rpc** GetActivityLogEntry([GetActivityLogEntryRequest](#getactivitylogentryrequest))
    [GetActivityLogEntryResponse](#getactivitylogentryresponse)

GetActivityLogEntry retrieves a specific activity log entry
### ListActivityLogEntries

> **rpc** ListActivityLogEntries([ListActivityLogEntriesRequest](#listactivitylogentriesrequest))
    [ListActivityLogEntriesResponse](#listactivitylogentriesresponse)

ListActivityLogEntries lists activity log entries based on paramters in the
ListActivityLogEntriesRequest
 <!-- end methods -->
 <!-- end services -->

## Messages


### ActivityLogEntry
ActivityLogEntry contains context associated with a change in the deployment
history


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
| activity_type | [ string](#string) | `DELETE` or `SET` |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
| namespace_id | [ string](#string) | none |
| namespace_name | [ string](#string) | none |
| user_id | [ string](#string) | none |
| user_name | [ string](#string) | none |
| user_email | [ string](#string) | none |
| entity_type | [ string](#string) | `route` | `policy` | `settings` |
| entity_id | [ string](#string) | none |
| entity_data | [ string](#string) | none |
| diff_summary | [ ActivityLogEntry.DiffSummary](#activitylogentrydiffsummary) | none |
| db_version | [ uint64](#uint64) | databroker version this change synced to |
| session_id | [ string](#string) | none |
| service_account_id | [ string](#string) | none |
| impersonate_user_id | [ string](#string) | none |
| impersonate_user_name | [ string](#string) | none |
| impersonate_user_email | [ string](#string) | none |
| impersonate_user_groups | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ActivityLogEntry.DiffSummary



| Field | Type | Description |
| ----- | ---- | ----------- |
| added | [ int64](#int64) | number of lines added |
| removed | [ int64](#int64) | number of lines removed |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetActivityLogEntryRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetActivityLogEntryResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| entry | [ ActivityLogEntry](#activitylogentry) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _previous_entry_id.previous_entry_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _next_entry_id.next_entry_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListActivityLogEntriesRequest
ListActivityLogEntriesRequest defines the types of Activity Log entries to
list


| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _activity_type.activity_type | [optional string](#string) | `DELETE` | `SET` |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _namespace_id.namespace_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _user_id.user_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _entity_type.entity_type | [optional string](#string) | `route` | `policy` | `settings` |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _entity_id.entity_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _query.query | [optional string](#string) | `newest` | `oldest` | `from` | `name` |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _offset.offset | [optional int64](#int64) | list entries starting from an offset in the total list |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _limit.limit | [optional int64](#int64) | limit the number of entries returned |
| db_versions | [repeated uint64](#uint64) | databroker versions of the change |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _recurse_namespace.recurse_namespace | [optional bool](#bool) | if true, show activity for the namespace and any child namespaces |
| entities | [repeated ListActivityLogEntriesRequest.Entity](#listactivitylogentriesrequestentity) | the entities are a list of entities to retrieve the activity log for |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _sort.sort | [optional ListActivityLogEntriesRequest.Sort](#listactivitylogentriesrequestsort) | none |
| date_filter | [ ListActivityLogEntriesRequest.DateFilter](#listactivitylogentriesrequestdatefilter) | none |
| string_filter | [ ListActivityLogEntriesRequest.StringFilter](#listactivitylogentriesrequeststringfilter) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListActivityLogEntriesRequest.DateFilter
filter for dates


| Field | Type | Description |
| ----- | ---- | ----------- |
| operator | [ string](#string) | `=` | `!=` | `<` | `<=` | `>` | `>=` |
| date | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListActivityLogEntriesRequest.Entity
an entity is a single entity (route, policy, etc.)


| Field | Type | Description |
| ----- | ---- | ----------- |
| type | [ string](#string) | none |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListActivityLogEntriesRequest.Sort
used to sort the db query


| Field | Type | Description |
| ----- | ---- | ----------- |
| column | [ string](#string) | `activity_type` | `created_at` | `namespace_name` | `user_name` | `user_email` | `entity_type` |
| direction | [ string](#string) | `ASC` | `DESC` |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListActivityLogEntriesRequest.StringFilter
filter for strings


| Field | Type | Description |
| ----- | ---- | ----------- |
| fieldName | [ string](#string) | none |
| operator | [ string](#string) | `contains` | `equals` | `startsWith` | `endsWith` |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListActivityLogEntriesResponse
ListActivityLogEntriesResponse is a list of Activity Log entries found from a
ListActivityLogEntriesRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| entries | [repeated ActivityLogEntry](#activitylogentry) | Activity Log entries |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->


# ClustersService


## Methods
### AddCluster

> **rpc** AddCluster([AddClusterRequest](#addclusterrequest))
    [AddClusterResponse](#addclusterresponse)


### DeleteCluster

> **rpc** DeleteCluster([DeleteClusterRequest](#deleteclusterrequest))
    [DeleteClusterResponse](#deleteclusterresponse)


### GetCluster

> **rpc** GetCluster([GetClusterRequest](#getclusterrequest))
    [GetClusterResponse](#getclusterresponse)


### ListClusters

> **rpc** ListClusters([ListClustersRequest](#listclustersrequest))
    [ListClustersResponse](#listclustersresponse)


### UpdateCluster

> **rpc** UpdateCluster([UpdateClusterRequest](#updateclusterrequest))
    [UpdateClusterResponse](#updateclusterresponse)


 <!-- end methods -->
 <!-- end services -->

## Messages


### AddClusterRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| parent_namespace_id | [ string](#string) | none |
| cluster | [ Cluster](#cluster) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### AddClusterResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| cluster | [ Cluster](#cluster) | none |
| namespace | [ Namespace](#namespace) | none |
| settings | [ Settings](#settings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Cluster



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| name | [ string](#string) | none |
| databroker_service_url | [ string](#string) | none |
| shared_secret | [ bytes](#bytes) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _insecure_skip_verify.insecure_skip_verify | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _override_certificate_name.override_certificate_name | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _certificate_authority.certificate_authority | [optional bytes](#bytes) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _certificate_authority_file.certificate_authority_file | [optional string](#string) | none |
| originator_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteClusterRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteClusterResponse


 <!-- end HasFields -->


### GetClusterRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetClusterResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| cluster | [ Cluster](#cluster) | none |
| namespace | [ Namespace](#namespace) | none |
| settings | [ Settings](#settings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListClustersRequest


 <!-- end HasFields -->


### ListClustersResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| clusters | [repeated Cluster](#cluster) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### UpdateClusterRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| cluster | [ Cluster](#cluster) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### UpdateClusterResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| cluster | [ Cluster](#cluster) | none |
| namespace | [ Namespace](#namespace) | none |
| settings | [ Settings](#settings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->


# DeviceService
DeviceService manages device credentials, enrollments and types

## Methods
### ApproveDevice

> **rpc** ApproveDevice([ApproveDeviceRequest](#approvedevicerequest))
    [.google.protobuf.Empty](#googleprotobufempty)


### CreateDeviceEnrollment

> **rpc** CreateDeviceEnrollment([CreateDeviceEnrollmentRequest](#createdeviceenrollmentrequest))
    [CreateDeviceEnrollmentResponse](#createdeviceenrollmentresponse)


### SetDeviceType

> **rpc** SetDeviceType([SetDeviceTypeRequest](#setdevicetyperequest))
    [SetDeviceTypeResponse](#setdevicetyperesponse)


### DeleteDevice

> **rpc** DeleteDevice([DeleteDeviceRequest](#deletedevicerequest))
    [.google.protobuf.Empty](#googleprotobufempty)


### DeleteDeviceType

> **rpc** DeleteDeviceType([DeleteDeviceTypeRequest](#deletedevicetyperequest))
    [.google.protobuf.Empty](#googleprotobufempty)


### ListDevices

> **rpc** ListDevices([ListDevicesRequest](#listdevicesrequest))
    [ListDevicesResponse](#listdevicesresponse)


### ListDeviceTypes

> **rpc** ListDeviceTypes([ListDeviceTypesRequest](#listdevicetypesrequest))
    [ListDeviceTypesResponse](#listdevicetypesresponse)


 <!-- end methods -->
 <!-- end services -->

## Messages


### ApproveDeviceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) id.credential_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) id.enrollment_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### CreateDeviceEnrollmentRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| enrollment | [ DeviceEnrollment](#deviceenrollment) | none |
| route_url | [ string](#string) | none |
| redirect_url | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### CreateDeviceEnrollmentResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| enrollment | [ DeviceEnrollment](#deviceenrollment) | none |
| enrollment_url | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteDeviceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) id.credential_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) id.enrollment_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteDeviceTypeRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| type_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeviceCredential
A DeviceCredential is a user's device-specific credential.


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| device_type_id | [ string](#string) | none |
| device_enrollment_id | [ string](#string) | none |
| user_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) specifier.webauthn | [ DeviceCredential.WebAuthn](#devicecredentialwebauthn) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeviceCredential.WebAuthn



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ bytes](#bytes) | none |
| public_key | [ bytes](#bytes) | none |
| register_options | [ bytes](#bytes) | the options that were used to do initial registration |
| register_response | [ bytes](#bytes) | the response returned from initial registration |
| authenticate_response | [repeated bytes](#bytes) | subsequent authenticate responses |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeviceEnrollment
A DeviceEnrollment is used to approve a user's device.


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| device_type_id | [ string](#string) | none |
| device_credential_id | [ string](#string) | none |
| user_id | [ string](#string) | none |
| approved_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| approved_by_user_id | [ string](#string) | none |
| enrolled_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| user_agent | [ string](#string) | none |
| ip_address | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeviceOwnerCredentialRecord
A DeviceOwnerCredentialRecord is used to track credential owners to prevent
credential re-use.


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ bytes](#bytes) | none |
| owner_id | [ bytes](#bytes) | none |
| public_key | [ bytes](#bytes) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeviceType
A DeviceType constrains which kinds of devices are allowed to be registered.


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| name | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) specifier.webauthn | [ DeviceType.WebAuthn](#devicetypewebauthn) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeviceType.WebAuthn



| Field | Type | Description |
| ----- | ---- | ----------- |
| options | [ WebAuthnOptions](#webauthnoptions) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListDeviceTypesRequest


 <!-- end HasFields -->


### ListDeviceTypesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| types | [repeated DeviceType](#devicetype) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListDevicesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _type_id.type_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _user_id.user_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _approved_by.approved_by | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListDevicesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| devices | [repeated ListDevicesResponse.Device](#listdevicesresponsedevice) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListDevicesResponse.Device



| Field | Type | Description |
| ----- | ---- | ----------- |
| type | [ DeviceType](#devicetype) | none |
| credential | [ DeviceCredential](#devicecredential) | none |
| enrollment | [ DeviceEnrollment](#deviceenrollment) | none |
| kind | [ DeviceKind](#devicekind) | none |
| user_name | [ string](#string) | none |
| approved_by_user_name | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetDeviceTypeRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| type | [ DeviceType](#devicetype) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetDeviceTypeResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| type | [ DeviceType](#devicetype) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### WebAuthnOptions



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _attestation.attestation | [optional WebAuthnOptions.AttestationConveyancePreference](#webauthnoptionsattestationconveyancepreference) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _authenticator_selection.authenticator_selection | [optional WebAuthnOptions.AuthenticatorSelectionCriteria](#webauthnoptionsauthenticatorselectioncriteria) | none |
| pub_key_cred_params | [repeated WebAuthnOptions.PublicKeyCredentialParameters](#webauthnoptionspublickeycredentialparameters) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### WebAuthnOptions.AuthenticatorSelectionCriteria



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _authenticator_attachment.authenticator_attachment | [optional WebAuthnOptions.AuthenticatorAttachment](#webauthnoptionsauthenticatorattachment) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _require_resident_key.require_resident_key | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _resident_key_requirement.resident_key_requirement | [optional WebAuthnOptions.ResidentKeyRequirement](#webauthnoptionsresidentkeyrequirement) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _user_verification.user_verification | [optional WebAuthnOptions.UserVerificationRequirement](#webauthnoptionsuserverificationrequirement) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### WebAuthnOptions.PublicKeyCredentialParameters



| Field | Type | Description |
| ----- | ---- | ----------- |
| alg | [ int64](#int64) | none |
| type | [ WebAuthnOptions.PublicKeyCredentialType](#webauthnoptionspublickeycredentialtype) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums


### DeviceKind {#devicekind}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 | none |
| FIDO_U2F | 1 | none |
| ANDROID | 2 | none |
| APPLE | 3 | none |
| TPM | 4 | none |
| WINDOWS | 5 | none |




### WebAuthnOptions.AttestationConveyancePreference {#webauthnoptionsattestationconveyancepreference}


| Name | Number | Description |
| ---- | ------ | ----------- |
| NONE | 0 | none |
| INDIRECT | 1 | none |
| DIRECT | 2 | none |
| ENTERPRISE | 3 | none |




### WebAuthnOptions.AuthenticatorAttachment {#webauthnoptionsauthenticatorattachment}


| Name | Number | Description |
| ---- | ------ | ----------- |
| PLATFORM | 0 | none |
| CROSS_PLATFORM | 2 | none |




### WebAuthnOptions.PublicKeyCredentialType {#webauthnoptionspublickeycredentialtype}


| Name | Number | Description |
| ---- | ------ | ----------- |
| PUBLIC_KEY | 0 | none |




### WebAuthnOptions.ResidentKeyRequirement {#webauthnoptionsresidentkeyrequirement}


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESIDENT_KEY_DISCOURAGED | 0 | none |
| RESIDENT_KEY_PREFERRED | 1 | none |
| RESIDENT_KEY_REQUIRED | 2 | none |




### WebAuthnOptions.UserVerificationRequirement {#webauthnoptionsuserverificationrequirement}


| Name | Number | Description |
| ---- | ------ | ----------- |
| USER_VERIFICATION_DISCOURAGED | 0 | none |
| USER_VERIFICATION_PREFERRED | 1 | none |
| USER_VERIFICATION_REQUIRED | 2 | none |


 <!-- end Enums -->


# ExternalDataSourceService


## Methods
### DeleteExternalDataSource

> **rpc** DeleteExternalDataSource([DeleteExternalDataSourceRequest](#deleteexternaldatasourcerequest))
    [.google.protobuf.Empty](#googleprotobufempty)


### GetExternalDataSource

> **rpc** GetExternalDataSource([GetExternalDataSourceRequest](#getexternaldatasourcerequest))
    [GetExternalDataSourceResponse](#getexternaldatasourceresponse)


### ListExternalDataSources

> **rpc** ListExternalDataSources([ListExternalDataSourcesRequest](#listexternaldatasourcesrequest))
    [ListExternalDataSourcesResponse](#listexternaldatasourcesresponse)


### ListExternalDataSourceRecordTypes

> **rpc** ListExternalDataSourceRecordTypes([ListExternalDataSourceRecordTypesRequest](#listexternaldatasourcerecordtypesrequest))
    [ListExternalDataSourceRecordTypesResponse](#listexternaldatasourcerecordtypesresponse)


### ListExternalDataSourceRecordFields

> **rpc** ListExternalDataSourceRecordFields([ListExternalDataSourceRecordFieldsRequest](#listexternaldatasourcerecordfieldsrequest))
    [ListExternalDataSourceRecordFieldsResponse](#listexternaldatasourcerecordfieldsresponse)


### SetExternalDataSource

> **rpc** SetExternalDataSource([SetExternalDataSourceRequest](#setexternaldatasourcerequest))
    [SetExternalDataSourceResponse](#setexternaldatasourceresponse)


 <!-- end methods -->
 <!-- end services -->

## Messages


### DeleteExternalDataSourceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ExternalDataSource



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| originator_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| url | [ string](#string) | Url is the URL to query for data. |
| record_type | [ string](#string) | RecordType is how the queried records will be stored in the databroker. |
| foreign_key | [ string](#string) | ForeignKey is the key referenced for policy evaluation. E.g. user.id. |
| headers | [map ExternalDataSource.HeadersEntry](#externaldatasourceheadersentry) | Headers are request headers sent to the external data source. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _allow_insecure_tls.allow_insecure_tls | [optional bool](#bool) | AllowInsecureTls ignores TLS errors from the external data source. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _client_tls_key_id.client_tls_key_id | [optional string](#string) | ClientTlsKeyId is the key pair used for TLS to the external data source. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _polling_min_delay.polling_min_delay | [optional google.protobuf.Duration](#googleprotobufduration) | PollingMinDelay is the minimum amount of time to wait before polling again. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _polling_max_delay.polling_max_delay | [optional google.protobuf.Duration](#googleprotobufduration) | PollingMaxDelay is the maximum amount of time to wait before polling again. |
 <!-- end Fields -->
 <!-- end HasFields -->


### ExternalDataSource.HeadersEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetExternalDataSourceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetExternalDataSourceResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| external_data_source | [ ExternalDataSource](#externaldatasource) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListExternalDataSourceRecordFieldsRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| record_type | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListExternalDataSourceRecordFieldsResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| record_fields | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListExternalDataSourceRecordTypesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListExternalDataSourceRecordTypesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| record_types | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListExternalDataSourcesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListExternalDataSourcesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| external_data_sources | [repeated ExternalDataSource](#externaldatasource) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetExternalDataSourceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| external_data_source | [ ExternalDataSource](#externaldatasource) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetExternalDataSourceResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| external_data_source | [ ExternalDataSource](#externaldatasource) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->


# KeyChainService
KeyChainService manages and store TLS Certificates, Keys and CAs, known as
Key Pairs

## Methods
### DeleteKeyPair

> **rpc** DeleteKeyPair([DeleteKeyPairRequest](#deletekeypairrequest))
    [DeleteKeyPairResponse](#deletekeypairresponse)

DeleteKeyPair remove an x509 key pair based on a DeleteKeyPairRequest
### GetKeyPair

> **rpc** GetKeyPair([GetKeyPairRequest](#getkeypairrequest))
    [GetKeyPairResponse](#getkeypairresponse)

GetKeyPair retrieves an existing key pair
### ListKeyPairs

> **rpc** ListKeyPairs([ListKeyPairsRequest](#listkeypairsrequest))
    [ListKeyPairsResponse](#listkeypairsresponse)

ListKeyPairs lists existing key pairs based on parameters in
ListKeyPairsRequest
### CreateKeyPair

> **rpc** CreateKeyPair([CreateKeyPairRequest](#createkeypairrequest))
    [CreateKeyPairResponse](#createkeypairresponse)

CreateKeyPair creates a new key pair
### UpdateKeyPair

> **rpc** UpdateKeyPair([UpdateKeyPairRequest](#updatekeypairrequest))
    [UpdateKeyPairResponse](#updatekeypairresponse)

CreateKeyPair creates a new key pair
 <!-- end methods -->
 <!-- end services -->

## Messages


### CertificateInfo
CertificateInfo is a .proto reflection of
https://golang.org/pkg/crypto/x509/#Certificate


| Field | Type | Description |
| ----- | ---- | ----------- |
| version | [ int64](#int64) | none |
| serial | [ string](#string) | none |
| issuer | [ Name](#name) | none |
| subject | [ Name](#name) | none |
| not_before | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| not_after | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| key_usage | [ KeyUsage](#keyusage) | none |
| dns_names | [repeated string](#string) | none |
| email_addresses | [repeated string](#string) | none |
| ip_addresses | [repeated string](#string) | none |
| uris | [repeated string](#string) | none |
| permitted_dns_domains_critical | [ bool](#bool) | none |
| permitted_dns_domains | [repeated string](#string) | none |
| excluded_dns_domains | [repeated string](#string) | none |
| permitted_ip_ranges | [repeated string](#string) | none |
| excluded_ip_ranges | [repeated string](#string) | none |
| permitted_email_addresses | [repeated string](#string) | none |
| excluded_email_addresses | [repeated string](#string) | none |
| permitted_uri_domains | [repeated string](#string) | none |
| excluded_uri_domains | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### CreateKeyPairRequest
CreateKeyPairRequest defines a Key Pair to create


| Field | Type | Description |
| ----- | ---- | ----------- |
| originator_id | [ string](#string) | none |
| name | [ string](#string) | none |
| namespace_id | [ string](#string) | none |
| format | [ Format](#format) | encoding format of data |
| certificate | [ bytes](#bytes) | public certificate data |
| key | [ bytes](#bytes) | private key data |
 <!-- end Fields -->
 <!-- end HasFields -->


### CreateKeyPairResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| key_pair | [ KeyPairRecord](#keypairrecord) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteKeyPairRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteKeyPairResponse


 <!-- end HasFields -->


### GetKeyPairRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetKeyPairResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| key_pair | [ KeyPairRecord](#keypairrecord) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### KeyPair
KeyPair represents raw Key Pair data for internal usage


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
| namespace_id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| certificate | [ bytes](#bytes) | public certificate data |
| key | [ bytes](#bytes) | private key data |
| originator_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### KeyPairRecord
KeyPairRecord provides existing Key Pair metadata


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
| namespace_id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | database record creation time |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | database record modification time |
| cert_info | [ CertificateInfo](#certificateinfo) | information about the public certificate |
| has_private_key | [ bool](#bool) | Key Pair has a private key attached |
| certificate | [ bytes](#bytes) | public certificate data |
| originator_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### KeyUsage
KeyUsage specifies the usage flags set on a signed TLS certificate


| Field | Type | Description |
| ----- | ---- | ----------- |
| digital_signature | [ bool](#bool) | standard key usages |
| content_commitment | [ bool](#bool) | none |
| key_encipherment | [ bool](#bool) | none |
| data_encipherment | [ bool](#bool) | none |
| key_agreement | [ bool](#bool) | none |
| cert_sign | [ bool](#bool) | certificate authority |
| crl_sign | [ bool](#bool) | none |
| encipher_only | [ bool](#bool) | none |
| decipher_only | [ bool](#bool) | none |
| server_auth | [ bool](#bool) | extensions derived from x509.ExtKeyUsage server certificate |
| client_auth | [ bool](#bool) | client certificate |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListKeyPairsRequest
ListKeyPairsRequest defines the types of key pairs to list


| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _query.query | [optional string](#string) | list Key Pairs whose name contains the query string |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _offset.offset | [optional int64](#int64) | list Key Pairs starting from an offset in the total list |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _limit.limit | [optional int64](#int64) | limit the number of entries returned |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _order_by.order_by | [optional string](#string) | `newest`, `oldest`, `name`, `from` |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _domain.domain | [optional string](#string) | return key pairs that match the given domain |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListKeyPairsResponse
ListKeyPairsResponse is the list of Key Pairs found from a
ListKeyPairsRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| key_pairs | [repeated KeyPairRecord](#keypairrecord) | Key Pairs found |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Name
Name defines the x509 identity


| Field | Type | Description |
| ----- | ---- | ----------- |
| country | [repeated string](#string) | none |
| organization | [repeated string](#string) | none |
| organizational_unit | [repeated string](#string) | none |
| locality | [repeated string](#string) | none |
| province | [repeated string](#string) | none |
| street_address | [repeated string](#string) | none |
| postal_code | [repeated string](#string) | none |
| serial_number | [ string](#string) | none |
| common_name | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### UpdateKeyPairRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| originator_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _name.name | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _format.format | [optional Format](#format) | encoding format of data |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _certificate.certificate | [optional bytes](#bytes) | public certificate data |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _key.key | [optional bytes](#bytes) | private key data |
 <!-- end Fields -->
 <!-- end HasFields -->


### UpdateKeyPairResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| key_pair | [ KeyPairRecord](#keypairrecord) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums


### Format {#format}
Format specifies the encoding format of a certificate or key

| Name | Number | Description |
| ---- | ------ | ----------- |
| FORMAT_UNDEFINED_DO_NOT_USE | 0 | none |
| PEM | 1 | none |




### PublicKeyAlgorithm {#publickeyalgorithm}
PublicKeyAlgorithm is the algorithm of a public key

| Name | Number | Description |
| ---- | ------ | ----------- |
| PKA_UNKNOWN_DO_NOT_USE | 0 | none |
| RSA | 1 | none |
| DSA | 2 | none |
| ECDSA | 3 | none |
| ED25519 | 4 | none |


 <!-- end Enums -->


# NamespacePermissionService
NamespacePermissionService manages permissions set on namespaces

## Methods
### DeleteNamespacePermission

> **rpc** DeleteNamespacePermission([DeleteNamespacePermissionRequest](#deletenamespacepermissionrequest))
    [DeleteNamespacePermissionResponse](#deletenamespacepermissionresponse)

DeleteNamespacePermission removes an existing permission definition
### GetNamespacePermission

> **rpc** GetNamespacePermission([GetNamespacePermissionRequest](#getnamespacepermissionrequest))
    [GetNamespacePermissionResponse](#getnamespacepermissionresponse)

GetNamespacePermission retrieves an existing permission definition
### ListNamespacePermissions

> **rpc** ListNamespacePermissions([ListNamespacePermissionsRequest](#listnamespacepermissionsrequest))
    [ListNamespacePermissionsResponse](#listnamespacepermissionsresponse)

ListNamespacePermissions retrieves existing permissions for all namespaces
### ListNamespacePermissionGroups

> **rpc** ListNamespacePermissionGroups([ListNamespacePermissionGroupsRequest](#listnamespacepermissiongroupsrequest))
    [ListNamespacePermissionGroupsResponse](#listnamespacepermissiongroupsresponse)

ListNamespacePermissionGroups retrieves existing group based permissions on
a namespace
### ListNamespacePermissionUsers

> **rpc** ListNamespacePermissionUsers([ListNamespacePermissionUsersRequest](#listnamespacepermissionusersrequest))
    [ListNamespacePermissionUsersResponse](#listnamespacepermissionusersresponse)

ListNamespacePermissionUsers retrieves existing user based permissions on a
namespace
### SetNamespacePermission

> **rpc** SetNamespacePermission([SetNamespacePermissionRequest](#setnamespacepermissionrequest))
    [SetNamespacePermissionResponse](#setnamespacepermissionresponse)

SetNamespacePermission set a new permission definition on a namespace
 <!-- end methods -->
# NamespaceService
NamespaceService manages namespaces

## Methods
### DeleteNamespace

> **rpc** DeleteNamespace([DeleteNamespaceRequest](#deletenamespacerequest))
    [DeleteNamespaceResponse](#deletenamespaceresponse)

DeleteNamespace deletes a namespace
### GetNamespace

> **rpc** GetNamespace([GetNamespaceRequest](#getnamespacerequest))
    [GetNamespaceResponse](#getnamespaceresponse)

GetNamespace retrieves a namespace
### ListNamespaces

> **rpc** ListNamespaces([ListNamespacesRequest](#listnamespacesrequest))
    [ListNamespacesResponse](#listnamespacesresponse)

ListNamespaces lists all namespaces
### ListNamespaceResources

> **rpc** ListNamespaceResources([ListNamespaceResourcesRequest](#listnamespaceresourcesrequest))
    [ListNamespaceResourcesResponse](#listnamespaceresourcesresponse)

ListNamespaceResources lists all the resources for a namespace.
### SetNamespace

> **rpc** SetNamespace([SetNamespaceRequest](#setnamespacerequest))
    [SetNamespaceResponse](#setnamespaceresponse)

SetNamespace creates a namespace or, if the id is specified, updates an
existing namespace
 <!-- end methods -->
 <!-- end services -->

## Messages


### DeleteNamespacePermissionRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteNamespacePermissionResponse


 <!-- end HasFields -->


### DeleteNamespaceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteNamespaceResponse


 <!-- end HasFields -->


### GetNamespacePermissionRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetNamespacePermissionResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_permission | [ NamespacePermission](#namespacepermission) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetNamespaceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetNamespaceResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace | [ Namespace](#namespace) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespacePermissionGroupsRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespacePermissionGroupsResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| groups | [repeated NamespacePermissionGroup](#namespacepermissiongroup) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespacePermissionUsersRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespacePermissionUsersResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| users | [repeated NamespacePermissionUser](#namespacepermissionuser) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespacePermissionsRequest


 <!-- end HasFields -->


### ListNamespacePermissionsResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_permissions | [repeated NamespacePermission](#namespacepermission) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespaceResourcesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| ids | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespaceResourcesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| resources | [repeated ListNamespaceResourcesResponse.Resource](#listnamespaceresourcesresponseresource) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespaceResourcesResponse.Resource



| Field | Type | Description |
| ----- | ---- | ----------- |
| type | [ string](#string) | none |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListNamespacesRequest


 <!-- end HasFields -->


### ListNamespacesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespaces | [repeated Namespace](#namespace) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Namespace
Namespace defines a namespace


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| parent_id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| name | [ string](#string) | none |
| originator_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
| route_count | [ int64](#int64) | computed |
| policy_count | [ int64](#int64) | computed |
 <!-- end Fields -->
 <!-- end HasFields -->


### NamespacePermission
NamespacePermission defines a permission binding to an identity


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| namespace_id | [ string](#string) | none |
| namespace_name | [ string](#string) | none |
| subject_type | [ string](#string) | none |
| subject_id | [ string](#string) | none |
| role | [ string](#string) | none |
| originator_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### NamespacePermissionGroup
NamespacePermissionGroup defines a permission binding to a group identity


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| namespace_id | [ string](#string) | none |
| namespace_name | [ string](#string) | none |
| group_id | [ string](#string) | none |
| group_name | [ string](#string) | none |
| group_email | [ string](#string) | none |
| role | [ string](#string) | none |
| originator_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### NamespacePermissionUser
NamespacePermissionUser defines a permission binding to a user identity


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| namespace_id | [ string](#string) | none |
| namespace_name | [ string](#string) | none |
| user_id | [ string](#string) | none |
| user_name | [ string](#string) | none |
| user_email | [ string](#string) | none |
| group_ids | [repeated string](#string) | none |
| role | [ string](#string) | none |
| originator_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetNamespacePermissionRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_permission | [ NamespacePermission](#namespacepermission) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetNamespacePermissionResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace_permission | [ NamespacePermission](#namespacepermission) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetNamespaceRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace | [ Namespace](#namespace) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetNamespaceResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace | [ Namespace](#namespace) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->


# PolicyService
PolicyService manages policy creation and definition

## Methods
### DeletePolicy

> **rpc** DeletePolicy([DeletePolicyRequest](#deletepolicyrequest))
    [DeletePolicyResponse](#deletepolicyresponse)

DeletePolicy deletes an existing policy
### GetPolicy

> **rpc** GetPolicy([GetPolicyRequest](#getpolicyrequest))
    [GetPolicyResponse](#getpolicyresponse)

GetPolicy retrieves an existing policy
### ListPolicies

> **rpc** ListPolicies([ListPoliciesRequest](#listpoliciesrequest))
    [ListPoliciesResponse](#listpoliciesresponse)

ListPolicies lists existing policies based on the ListPoliciesRequest
parameters
### SetPolicy

> **rpc** SetPolicy([SetPolicyRequest](#setpolicyrequest))
    [SetPolicyResponse](#setpolicyresponse)

SetPolicy creates a new policy or, if the id is specified, updates an
existing policy
 <!-- end methods -->
 <!-- end services -->

## Messages


### DeletePolicyRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeletePolicyResponse


 <!-- end HasFields -->


### GetPolicyRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetPolicyResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| policy | [ Policy](#policy) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListPoliciesRequest
ListPoliciesRequest specifies the policies to list


| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _query.query | [optional string](#string) | list Policies whose name contains the query string |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _offset.offset | [optional int64](#int64) | list Policies starting from an offset in the total list |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _limit.limit | [optional int64](#int64) | limit the number of entries returned |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _order_by.order_by | [optional string](#string) | sort the Policies by newest, oldest or name |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | list Policies belonging to the cluster, or the default cluster if not set |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListPoliciesResponse
ListPoliciesResponse is the list of policies found for a ListPoliciesRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| policies | [repeated Policy](#policy) | none |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Policy
Policy defines an authorization policy which can be applied to a route or
routes


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| namespace_id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| name | [ string](#string) | none |
| description | [ string](#string) | none |
| allowed_users | [repeated string](#string) | none |
| allowed_domains | [repeated string](#string) | none |
| allowed_idp_claims | [map Policy.AllowedIdpClaimsEntry](#policyallowedidpclaimsentry) | none |
| rego | [repeated string](#string) | custom rego definition in string format |
| ppl | [ string](#string) | PPL definition in JSON format |
| enforced | [ bool](#bool) | policy is automatically applied to all routes in namespace_id and child namespaces |
| explanation | [ string](#string) | none |
| remediation | [ string](#string) | none |
| originator_id | [ string](#string) | none |
| routes | [map Policy.RoutesEntry](#policyroutesentry) | computed

route id => name |
| namespace_name | [ string](#string) | computed |
 <!-- end Fields -->
 <!-- end HasFields -->


### Policy.AllowedIdpClaimsEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ google.protobuf.ListValue](#googleprotobuflistvalue) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Policy.RoutesEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetPolicyRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| policy | [ Policy](#policy) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetPolicyResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| policy | [ Policy](#policy) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->


 <!-- end services -->

## Messages


### HealthCheck
[#next-free-field: 27]


| Field | Type | Description |
| ----- | ---- | ----------- |
| timeout | [ google.protobuf.Duration](#googleprotobufduration) | The time to wait for a health check response. If the timeout is reached the health check attempt will be considered a failure. |
| interval | [ google.protobuf.Duration](#googleprotobufduration) | The interval between health checks. |
| initial_jitter | [ google.protobuf.Duration](#googleprotobufduration) | An optional jitter amount in milliseconds. If specified, Envoy will start health checking after for a random time in ms between 0 and initial_jitter. This only applies to the first health check. |
| interval_jitter | [ google.protobuf.Duration](#googleprotobufduration) | An optional jitter amount in milliseconds. If specified, during every interval Envoy will add interval_jitter to the wait time. |
| interval_jitter_percent | [ uint32](#uint32) | An optional jitter amount as a percentage of interval_ms. If specified, during every interval Envoy will add ``interval_ms`` * ``interval_jitter_percent`` / 100 to the wait time.

If interval_jitter_ms and interval_jitter_percent are both set, both of them will be used to increase the wait time. |
| unhealthy_threshold | [ uint32](#uint32) | The number of unhealthy health checks required before a host is marked unhealthy. Note that for ``http`` health checking if a host responds with a code not in :ref:`expected_statuses <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.expected_statuses>` or :ref:`retriable_statuses <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.retriable_statuses>`, this threshold is ignored and the host is considered immediately unhealthy. |
| healthy_threshold | [ uint32](#uint32) | The number of healthy health checks required before a host is marked healthy. Note that during startup, only a single successful health check is required to mark a host healthy. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) health_checker.http_health_check | [ HealthCheck.HttpHealthCheck](#healthcheckhttphealthcheck) | HTTP health check. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) health_checker.tcp_health_check | [ HealthCheck.TcpHealthCheck](#healthchecktcphealthcheck) | TCP health check. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) health_checker.grpc_health_check | [ HealthCheck.GrpcHealthCheck](#healthcheckgrpchealthcheck) | gRPC health check. |
 <!-- end Fields -->
 <!-- end HasFields -->


### HealthCheck.GrpcHealthCheck
`grpc.health.v1.Health
<https://github.com/grpc/grpc/blob/master/src/proto/grpc/health/v1/health.proto>`_-based
healthcheck. See `gRPC doc
<https://github.com/grpc/grpc/blob/master/doc/health-checking.md>`_ for
details.


| Field | Type | Description |
| ----- | ---- | ----------- |
| service_name | [ string](#string) | An optional service name parameter which will be sent to gRPC service in `grpc.health.v1.HealthCheckRequest <https://github.com/grpc/grpc/blob/master/src/proto/grpc/health/v1/health.proto#L20>`_. message. See `gRPC health-checking overview <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>`_ for more information. |
| authority | [ string](#string) | The value of the :authority header in the gRPC health check request. If left empty (default value), the name of the cluster this health check is associated with will be used. The authority header can be customized for a specific endpoint by setting the :ref:`hostname <envoy_v3_api_field_config.endpoint.v3.Endpoint.HealthCheckConfig.hostname>` field. |
 <!-- end Fields -->
 <!-- end HasFields -->


### HealthCheck.HttpHealthCheck
[#next-free-field: 15]


| Field | Type | Description |
| ----- | ---- | ----------- |
| host | [ string](#string) | The value of the host header in the HTTP health check request. If left empty (default value), the name of the cluster this health check is associated with will be used. The host header can be customized for a specific endpoint by setting the :ref:`hostname <envoy_v3_api_field_config.endpoint.v3.Endpoint.HealthCheckConfig.hostname>` field. |
| path | [ string](#string) | Specifies the HTTP path that will be requested during health checking. For example ``/healthcheck``. |
| expected_statuses | [repeated Int64Range](#int64range) | Specifies a list of HTTP response statuses considered healthy. If provided, replaces default 200-only policy - 200 must be included explicitly as needed. Ranges follow half-open semantics of :ref:`Int64Range <envoy_v3_api_msg_type.v3.Int64Range>`. The start and end of each range are required. Only statuses in the range [100, 600) are allowed. |
| retriable_statuses | [repeated Int64Range](#int64range) | Specifies a list of HTTP response statuses considered retriable. If provided, responses in this range will count towards the configured :ref:`unhealthy_threshold <envoy_v3_api_field_config.core.v3.HealthCheck.unhealthy_threshold>`, but will not result in the host being considered immediately unhealthy. Ranges follow half-open semantics of :ref:`Int64Range <envoy_v3_api_msg_type.v3.Int64Range>`. The start and end of each range are required. Only statuses in the range [100, 600) are allowed. The :ref:`expected_statuses <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.expected_statuses>` field takes precedence for any range overlaps with this field i.e. if status code 200 is both retriable and expected, a 200 response will be considered a successful health check. By default all responses not in :ref:`expected_statuses <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.expected_statuses>` will result in the host being considered immediately unhealthy i.e. if status code 200 is expected and there are no configured retriable statuses, any non-200 response will result in the host being marked unhealthy. |
| codec_client_type | [ CodecClientType](#codecclienttype) | Use specified application protocol for health checks. |
 <!-- end Fields -->
 <!-- end HasFields -->


### HealthCheck.Payload
Describes the encoding of the payload bytes in the payload.


| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) payload.text | [ string](#string) | Hex encoded payload. E.g., "000000FF". |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) payload.binary | [ bytes](#bytes) | Binary payload. |
 <!-- end Fields -->
 <!-- end HasFields -->


### HealthCheck.TcpHealthCheck



| Field | Type | Description |
| ----- | ---- | ----------- |
| send | [ HealthCheck.Payload](#healthcheckpayload) | Empty payloads imply a connect-only health check. |
| receive | [repeated HealthCheck.Payload](#healthcheckpayload) | When checking the response, “fuzzy” matching is performed such that each payload block must be found, and in the order specified, but not necessarily contiguous. |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->


 <!-- end services -->

## Messages


### RedirectAction



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) scheme_rewrite_specifier.https_redirect | [ bool](#bool) | The scheme portion of the URL will be swapped with "https". |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) scheme_rewrite_specifier.scheme_redirect | [ string](#string) | The scheme portion of the URL will be swapped with this value. |
| host_redirect | [ string](#string) | The host portion of the URL will be swapped with this value. |
| port_redirect | [ uint32](#uint32) | The port value of the URL will be swapped with this value. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) path_rewrite_specifier.path_redirect | [ string](#string) | The path portion of the URL will be swapped with this value. Please note that query string in path_redirect will override the request's query string and will not be stripped.

For example, let's say we have the following routes:

- match: { path: "/old-path-1" } redirect: { path_redirect: "/new-path-1" } - match: { path: "/old-path-2" } redirect: { path_redirect: "/new-path-2", strip-query: "true" } - match: { path: "/old-path-3" } redirect: { path_redirect: "/new-path-3?foo=1", strip_query: "true" }

1. if request uri is "/old-path-1?bar=1", users will be redirected to "/new-path-1?bar=1" 2. if request uri is "/old-path-2?bar=1", users will be redirected to "/new-path-2" 3. if request uri is "/old-path-3?bar=1", users will be redirected to "/new-path-3?foo=1" |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) path_rewrite_specifier.prefix_rewrite | [ string](#string) | Indicates that during redirection, the matched prefix (or path) should be swapped with this value. This option allows redirect URLs be dynamically created based on the request.

.. attention::

 Pay attention to the use of trailing slashes as mentioned in :ref:`RouteAction's prefix_rewrite <envoy_v3_api_field_config.route.v3.RouteAction.prefix_rewrite>`. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) path_rewrite_specifier.regex_rewrite | [ RedirectAction.RegexMatchAndSubstitute](#redirectactionregexmatchandsubstitute) | Indicates that during redirect, portions of the path that match the pattern should be rewritten, even allowing the substitution of capture groups from the pattern into the new path as specified by the rewrite substitution string. This is useful to allow application paths to be rewritten in a way that is aware of segments with variable content like identifiers.

Examples using Google's `RE2 <https://github.com/google/re2>`_ engine:

* The path pattern ``^/service/([^/]+)(/.*)$`` paired with a substitution string of ``\2/instance/\1`` would transform ``/service/foo/v1/api`` into ``/v1/api/instance/foo``.

* The pattern ``one`` paired with a substitution string of ``two`` would transform ``/xxx/one/yyy/one/zzz`` into ``/xxx/two/yyy/two/zzz``.

* The pattern ``^(.*?)one(.*)$`` paired with a substitution string of ``\1two\2`` would replace only the first occurrence of ``one``, transforming path ``/xxx/one/yyy/one/zzz`` into ``/xxx/two/yyy/one/zzz``.

* The pattern ``(?i)/xxx/`` paired with a substitution string of ``/yyy/`` would do a case-insensitive match and transform path ``/aaa/XxX/bbb`` to ``/aaa/yyy/bbb``. |
| response_code | [ RedirectAction.RedirectResponseCode](#redirectactionredirectresponsecode) | The HTTP status code to use in the redirect response. The default response code is MOVED_PERMANENTLY (301). |
| strip_query | [ bool](#bool) | Indicates that during redirection, the query portion of the URL will be removed. Default value is false. |
 <!-- end Fields -->
 <!-- end HasFields -->


### RedirectAction.RegexMatchAndSubstitute
Describes how to match a string and then produce a new string using a
regular expression and a substitution string.


| Field | Type | Description |
| ----- | ---- | ----------- |
| pattern | [ string](#string) | The regular expression used to find portions of a string (hereafter called the "subject string") that should be replaced. When a new string is produced during the substitution operation, the new string is initially the same as the subject string, but then all matches in the subject string are replaced by the substitution string. If replacing all matches isn't desired, regular expression anchors can be used to ensure a single match, so as to replace just one occurrence of a pattern. Capture groups can be used in the pattern to extract portions of the subject string, and then referenced in the substitution string. |
| substitution | [ string](#string) | The string that should be substituted into matching portions of the subject string during a substitution operation to produce a new string. Capture groups in the pattern can be referenced in the substitution string. Note, however, that the syntax for referring to capture groups is defined by the chosen regular expression engine. Google's `RE2 <https://github.com/google/re2>`_ regular expression engine uses a backslash followed by the capture group number to denote a numbered capture group. E.g., ``\1`` refers to capture group 1, and ``\2`` refers to capture group 2. |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums


### RedirectAction.RedirectResponseCode {#redirectactionredirectresponsecode}


| Name | Number | Description |
| ---- | ------ | ----------- |
| MOVED_PERMANENTLY | 0 | Moved Permanently HTTP Status Code - 301. |
| FOUND | 1 | Found HTTP Status Code - 302. |
| SEE_OTHER | 2 | See Other HTTP Status Code - 303. |
| TEMPORARY_REDIRECT | 3 | Temporary Redirect HTTP Status Code - 307. |
| PERMANENT_REDIRECT | 4 | Permanent Redirect HTTP Status Code - 308. |


 <!-- end Enums -->


# RouteService
RouteService manages proxy route definitions

## Methods
### DeleteRoute

> **rpc** DeleteRoute([DeleteRouteRequest](#deleterouterequest))
    [DeleteRouteResponse](#deleterouteresponse)

DeleteRoute removes an existing route
### DeleteRoutes

> **rpc** DeleteRoutes([DeleteRoutesRequest](#deleteroutesrequest))
    [DeleteRoutesResponse](#deleteroutesresponse)

DeleteRoutes removes existing routes.
### GetRoute

> **rpc** GetRoute([GetRouteRequest](#getrouterequest))
    [GetRouteResponse](#getrouteresponse)

GetRoute retrieves an existing route
### ListRoutes

> **rpc** ListRoutes([ListRoutesRequest](#listroutesrequest))
    [ListRoutesResponse](#listroutesresponse)

ListRoutes lists routes based on ListRoutesRequest
### LoadRoutes

> **rpc** LoadRoutes([LoadRoutesRequest](#loadroutesrequest))
    [LoadRoutesResponse](#loadroutesresponse)

LoadRoutes imports routes from an existing OSS configuration
### SetRoute

> **rpc** SetRoute([SetRouteRequest](#setrouterequest))
    [SetRouteResponse](#setrouteresponse)

SetRoute creates or, if id is defined, updates an existing route
### SetRoutes

> **rpc** SetRoutes([SetRoutesRequest](#setroutesrequest))
    [SetRoutesResponse](#setroutesresponse)

SetRoutes creates or, if id is defined, updates existing routes
### MoveRoutes

> **rpc** MoveRoutes([MoveRoutesRequest](#moveroutesrequest))
    [MoveRoutesResponse](#moveroutesresponse)

MoveRoutes takes an array of routeIds and moves them to a new namespace
 <!-- end methods -->
 <!-- end services -->

## Messages


### CircuitBreakerThresholds
CircuitBreakerThresholds defines CircuitBreaker settings.


| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _max_connections.max_connections | [optional uint32](#uint32) | The maximum number of connections that Envoy will make to the upstream cluster. If not specified, the default is 1024. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _max_pending_requests.max_pending_requests | [optional uint32](#uint32) | The maximum number of pending requests that Envoy will allow to the upstream cluster. If not specified, the default is 1024. This limit is applied as a connection limit for non-HTTP traffic. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _max_requests.max_requests | [optional uint32](#uint32) | The maximum number of parallel requests that Envoy will make to the upstream cluster. If not specified, the default is 1024. This limit does not apply to non-HTTP traffic. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _max_retries.max_retries | [optional uint32](#uint32) | The maximum number of parallel retries that Envoy will allow to the upstream cluster. If not specified, the default is 3. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _max_connection_pools.max_connection_pools | [optional uint32](#uint32) | The maximum number of connection pools per cluster that Envoy will concurrently support at once. If not specified, the default is unlimited. Set this for clusters which create a large number of connection pools. |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteRouteRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteRouteResponse


 <!-- end HasFields -->


### DeleteRoutesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| ids | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeleteRoutesResponse


 <!-- end HasFields -->


### GetRouteRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetRouteResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| route | [ Route](#route) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### JwtGroupsFilter



| Field | Type | Description |
| ----- | ---- | ----------- |
| groups | [repeated string](#string) | Explicit list of group IDs/names to include. |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _infer_from_ppl.infer_from_ppl | [optional bool](#bool) | Infer group IDs/names based on PPL groups criteria. |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListRoutesRequest
ListRoutesRequest defines the routes to list


| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _query.query | [optional string](#string) | list Routes who's name, from or to contains the query string |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _offset.offset | [optional int64](#int64) | list Routes starting from an offset in the total list |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _limit.limit | [optional int64](#int64) | limit the number of Route entries returned |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _order_by.order_by | [optional string](#string) | sort the Routes by newest, oldest, name or from |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | list Routes belonging to the cluster, or the default cluster if not set |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListRoutesResponse
ListRoutesResponse is the list of routes found for a ListRoutesRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| routes | [repeated Route](#route) | none |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### LoadRoutesRequest
LoadRoutesRequest creates a route based on a yaml payload


| Field | Type | Description |
| ----- | ---- | ----------- |
| name | [ string](#string) | none |
| contents | [ bytes](#bytes) | OSS pomerium policy block |
 <!-- end Fields -->
 <!-- end HasFields -->


### LoadRoutesResponse
LoadRoutesResponse contains the routes and policies crated from a
LoadRoutesRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| routes | [repeated RouteWithPolicies](#routewithpolicies) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### MoveRoutesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| route_ids | [repeated string](#string) | none |
| new_namespace_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### MoveRoutesResponse


 <!-- end HasFields -->


### Route
Route defines a proxy route's settings and policy associations
Next ID: 74


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| namespace_id | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| deleted_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| name | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _description.description | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _logo_url.logo_url | [optional string](#string) | none |
| stat_name | [ string](#string) | name for prometheus stats, computed on first save |
| from | [ string](#string) | none |
| to | [repeated string](#string) | none |
| redirect | [ RedirectAction](#redirectaction) | none |
| response | [ RouteDirectResponse](#routedirectresponse) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _prefix.prefix | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _path.path | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _regex.regex | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _prefix_rewrite.prefix_rewrite | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _regex_rewrite_pattern.regex_rewrite_pattern | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _regex_rewrite_substitution.regex_rewrite_substitution | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _host_rewrite.host_rewrite | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _host_rewrite_header.host_rewrite_header | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _host_path_regex_rewrite_pattern.host_path_regex_rewrite_pattern | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _host_path_regex_rewrite_substitution.host_path_regex_rewrite_substitution | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _regex_priority_order.regex_priority_order | [optional int64](#int64) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _timeout.timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idle_timeout.idle_timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _allow_websockets.allow_websockets | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _allow_spdy.allow_spdy | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_skip_verify.tls_skip_verify | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_upstream_server_name.tls_upstream_server_name | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_downstream_server_name.tls_downstream_server_name | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_custom_ca_key_pair_id.tls_custom_ca_key_pair_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_client_key_pair_id.tls_client_key_pair_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_downstream_client_ca_key_pair_id.tls_downstream_client_ca_key_pair_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _tls_upstream_allow_renegotiation.tls_upstream_allow_renegotiation | [optional bool](#bool) | none |
| set_request_headers | [map Route.SetRequestHeadersEntry](#routesetrequestheadersentry) | none |
| remove_request_headers | [repeated string](#string) | none |
| set_response_headers | [map Route.SetResponseHeadersEntry](#routesetresponseheadersentry) | none |
| rewrite_response_headers | [repeated RouteRewriteHeader](#routerewriteheader) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _preserve_host_header.preserve_host_header | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _pass_identity_headers.pass_identity_headers | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _kubernetes_service_account_token.kubernetes_service_account_token | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _kubernetes_service_account_token_file.kubernetes_service_account_token_file | [optional string](#string) | none |
| enable_google_cloud_serverless_authentication | [ bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _jwt_issuer_format.jwt_issuer_format | [optional IssuerFormat](#issuerformat) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _bearer_token_format.bearer_token_format | [optional BearerTokenFormat](#bearertokenformat) | none |
| jwt_groups_filter | [ JwtGroupsFilter](#jwtgroupsfilter) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_client_id.idp_client_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_client_secret.idp_client_secret | [optional string](#string) | none |
| show_error_details | [ bool](#bool) | none |
| originator_id | [ string](#string) | none |
| policy_ids | [repeated string](#string) | policies applied to this route |
| depends_on | [repeated string](#string) | multi-route login additional hosts |
| policy_names | [repeated string](#string) | computed properties (may be nil) |
| namespace_name | [ string](#string) | computed |
| enforced_policy_ids | [repeated string](#string) | computed |
| enforced_policy_names | [repeated string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_access_token_allowed_audiences.idp_access_token_allowed_audiences | [optional Route.StringList](#routestringlist) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _load_balancing_policy.load_balancing_policy | [optional LoadBalancingPolicy](#loadbalancingpolicy) | none |
| health_checks | [repeated HealthCheck](#healthcheck) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _circuit_breaker_thresholds.circuit_breaker_thresholds | [optional CircuitBreakerThresholds](#circuitbreakerthresholds) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Route.SetRequestHeadersEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Route.SetResponseHeadersEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Route.StringList



| Field | Type | Description |
| ----- | ---- | ----------- |
| values | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### RouteDirectResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| status | [ uint32](#uint32) | none |
| body | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### RouteRewriteHeader



| Field | Type | Description |
| ----- | ---- | ----------- |
| header | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) matcher.prefix | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### RouteWithPolicies
RouteWithPolicies contains automatically created routes and policies from a
LoadRoutesRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| route | [ Route](#route) | none |
| policies | [repeated Policy](#policy) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetRouteRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| route | [ Route](#route) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetRouteResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| route | [ Route](#route) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetRoutesRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| routes | [repeated Route](#route) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetRoutesResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| routes | [repeated Route](#route) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums


### BearerTokenFormat {#bearertokenformat}


| Name | Number | Description |
| ---- | ------ | ----------- |
| BEARER_TOKEN_FORMAT_UNKNOWN | 0 | none |
| BEARER_TOKEN_FORMAT_DEFAULT | 1 | none |
| BEARER_TOKEN_FORMAT_IDP_ACCESS_TOKEN | 2 | none |
| BEARER_TOKEN_FORMAT_IDP_IDENTITY_TOKEN | 3 | none |




### IssuerFormat {#issuerformat}


| Name | Number | Description |
| ---- | ------ | ----------- |
| IssuerHostOnly | 0 | Issuer strings will be the hostname of the route, with no scheme or trailing slash. |
| IssuerURI | 1 | Issuer strings will be a complete URI, including the scheme and ending with a trailing slash. |




### LoadBalancingPolicy {#loadbalancingpolicy}
LoadBalancingPolicy defines the strategy used to balance requests across
upstream endpoints

| Name | Number | Description |
| ---- | ------ | ----------- |
| LOAD_BALANCING_POLICY_UNSPECIFIED | 0 | Default load balancing if not specified |
| LOAD_BALANCING_POLICY_ROUND_ROBIN | 1 | Classic round robin algorithm |
| LOAD_BALANCING_POLICY_MAGLEV | 2 | Consistent hashing load balancing |
| LOAD_BALANCING_POLICY_RANDOM | 3 | Random selection of backend |
| LOAD_BALANCING_POLICY_RING_HASH | 4 | Consistent hashing on an attribute |
| LOAD_BALANCING_POLICY_LEAST_REQUEST | 5 | Select backend with fewest active requests |


 <!-- end Enums -->


# SettingsService
SettingsService manages global pomerium settings

## Methods
### GetSettings

> **rpc** GetSettings([GetSettingsRequest](#getsettingsrequest))
    [GetSettingsResponse](#getsettingsresponse)

GetSettings retrieves the currently applied settings
### SetSettings

> **rpc** SetSettings([SetSettingsRequest](#setsettingsrequest))
    [SetSettingsResponse](#setsettingsresponse)

SetSettings applies new global settings
### GetBrandingSettings

> **rpc** GetBrandingSettings([GetSettingsRequest](#getsettingsrequest))
    [GetSettingsResponse](#getsettingsresponse)

GetBrandingSettings retrieves just the branding part of the settings
### GetConsoleSettings

> **rpc** GetConsoleSettings([GetConsoleSettingsRequest](#getconsolesettingsrequest))
    [GetConsoleSettingsResponse](#getconsolesettingsresponse)

GetConsoleSettings retrieves the console settings.
 <!-- end methods -->
 <!-- end services -->

## Messages


### ConsoleSettings



| Field | Type | Description |
| ----- | ---- | ----------- |
| enable_feedback_widget | [ bool](#bool) | none |
| use_changesets | [ bool](#bool) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetConsoleSettingsRequest


 <!-- end HasFields -->


### GetConsoleSettingsResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| console_settings | [ ConsoleSettings](#consolesettings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetSettingsRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetSettingsResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| settings | [ Settings](#settings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetSettingsRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| settings | [ Settings](#settings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetSettingsResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| settings | [ Settings](#settings) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Settings
Settings defines the global pomerium settings
Next id: 116.


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _installation_id.installation_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _log_level.log_level | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _proxy_log_level.proxy_log_level | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _shared_secret.shared_secret | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _services.services | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _address.address | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _insecure_server.insecure_server | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _dns_lookup_family.dns_lookup_family | [optional string](#string) | none |
| certificates | [repeated Settings.Certificate](#settingscertificate) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _http_redirect_addr.http_redirect_addr | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _timeout_read.timeout_read | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _timeout_write.timeout_write | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _timeout_idle.timeout_idle | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _authenticate_service_url.authenticate_service_url | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _authenticate_callback_path.authenticate_callback_path | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_name.cookie_name | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_secret.cookie_secret | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_domain.cookie_domain | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_secure.cookie_secure | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_http_only.cookie_http_only | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_same_site.cookie_same_site | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cookie_expire.cookie_expire | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_client_id.idp_client_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_client_secret.idp_client_secret | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_provider.idp_provider | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_provider_url.idp_provider_url | [optional string](#string) | none |
| scopes | [repeated string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_service_account.idp_service_account | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_refresh_directory_timeout.idp_refresh_directory_timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_refresh_directory_interval.idp_refresh_directory_interval | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| request_params | [map Settings.RequestParamsEntry](#settingsrequestparamsentry) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _authorize_service_url.authorize_service_url | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _certificate_authority.certificate_authority | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _certificate_authority_file.certificate_authority_file | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _certificate_authority_key_pair_id.certificate_authority_key_pair_id | [optional string](#string) | none |
| set_response_headers | [map Settings.SetResponseHeadersEntry](#settingssetresponseheadersentry) | none |
| jwt_claims_headers | [map Settings.JwtClaimsHeadersEntry](#settingsjwtclaimsheadersentry) | none |
| jwt_groups_filter | [ JwtGroupsFilter](#jwtgroupsfilter) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _jwt_issuer_format.jwt_issuer_format | [optional IssuerFormat](#issuerformat) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _default_upstream_timeout.default_upstream_timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _metrics_address.metrics_address | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_traces_exporter.otel_traces_exporter | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_traces_sampler_arg.otel_traces_sampler_arg | [optional double](#double) | none |
| otel_resource_attributes | [repeated string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_log_level.otel_log_level | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_attribute_value_length_limit.otel_attribute_value_length_limit | [optional int32](#int32) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_exporter_otlp_endpoint.otel_exporter_otlp_endpoint | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_exporter_otlp_traces_endpoint.otel_exporter_otlp_traces_endpoint | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_exporter_otlp_protocol.otel_exporter_otlp_protocol | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_exporter_otlp_traces_protocol.otel_exporter_otlp_traces_protocol | [optional string](#string) | none |
| otel_exporter_otlp_headers | [repeated string](#string) | none |
| otel_exporter_otlp_traces_headers | [repeated string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_exporter_otlp_timeout.otel_exporter_otlp_timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_exporter_otlp_traces_timeout.otel_exporter_otlp_traces_timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_bsp_schedule_delay.otel_bsp_schedule_delay | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _otel_bsp_max_export_batch_size.otel_bsp_max_export_batch_size | [optional int32](#int32) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _grpc_address.grpc_address | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _grpc_insecure.grpc_insecure | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cache_service_url.cache_service_url | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _databroker_service_url.databroker_service_url | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _client_ca.client_ca | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _client_ca_file.client_ca_file | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _client_ca_key_pair_id.client_ca_key_pair_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _google_cloud_serverless_authentication_service_account.google_cloud_serverless_authentication_service_account | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _autocert.autocert | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _autocert_use_staging.autocert_use_staging | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _autocert_must_staple.autocert_must_staple | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _autocert_dir.autocert_dir | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _skip_xff_append.skip_xff_append | [optional bool](#bool) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _primary_color.primary_color | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _secondary_color.secondary_color | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _darkmode_primary_color.darkmode_primary_color | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _darkmode_secondary_color.darkmode_secondary_color | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _logo_url.logo_url | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _favicon_url.favicon_url | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _error_message_first_paragraph.error_message_first_paragraph | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _identity_provider.identity_provider | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _identity_provider_options.identity_provider_options | [optional google.protobuf.Struct](#googleprotobufstruct) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _identity_provider_refresh_interval.identity_provider_refresh_interval | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _identity_provider_refresh_timeout.identity_provider_refresh_timeout | [optional google.protobuf.Duration](#googleprotobufduration) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _access_log_fields.access_log_fields | [optional Settings.StringList](#settingsstringlist) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _authorize_log_fields.authorize_log_fields | [optional Settings.StringList](#settingsstringlist) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _pass_identity_headers.pass_identity_headers | [optional bool](#bool) | none |
| originator_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _bearer_token_format.bearer_token_format | [optional BearerTokenFormat](#bearertokenformat) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _idp_access_token_allowed_audiences.idp_access_token_allowed_audiences | [optional Settings.StringList](#settingsstringlist) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _codec_type.codec_type | [optional CodecType](#codectype) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _circuit_breaker_thresholds.circuit_breaker_thresholds | [optional CircuitBreakerThresholds](#circuitbreakerthresholds) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _ssh_address.ssh_address | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _ssh_host_key_files.ssh_host_key_files | [optional Settings.StringList](#settingsstringlist) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _ssh_host_keys.ssh_host_keys | [optional Settings.StringList](#settingsstringlist) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _ssh_user_ca_key_file.ssh_user_ca_key_file | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _ssh_user_ca_key.ssh_user_ca_key | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Settings.Certificate



| Field | Type | Description |
| ----- | ---- | ----------- |
| cert_bytes | [ bytes](#bytes) | none |
| key_bytes | [ bytes](#bytes) | none |
| key_pair_id | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Settings.JwtClaimsHeadersEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Settings.RequestParamsEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Settings.SetResponseHeadersEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### Settings.StringList



| Field | Type | Description |
| ----- | ---- | ----------- |
| values | [repeated string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums


### CodecType {#codectype}


| Name | Number | Description |
| ---- | ------ | ----------- |
| CODEC_TYPE_UNKNOWN | 0 | none |
| CODEC_TYPE_AUTO | 1 | none |
| CODEC_TYPE_HTTP1 | 2 | none |
| CODEC_TYPE_HTTP2 | 3 | none |
| CODEC_TYPE_HTTP3 | 4 | none |


 <!-- end Enums -->


 <!-- end services -->

## Messages


### Int64Range



| Field | Type | Description |
| ----- | ---- | ----------- |
| start | [ int64](#int64) | start of the range (inclusive) |
| end | [ int64](#int64) | end of the range (exclusive) |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums


### CodecClientType {#codecclienttype}


| Name | Number | Description |
| ---- | ------ | ----------- |
| HTTP1 | 0 | none |
| HTTP2 | 1 | none |
| HTTP3 | 2 | none |


 <!-- end Enums -->


# PomeriumServiceAccountService
PomeriumServiceAccountService manages service accounts for use with the
pomerium console API

## Methods
### AddPomeriumServiceAccount

> **rpc** AddPomeriumServiceAccount([AddPomeriumServiceAccountRequest](#addpomeriumserviceaccountrequest))
    [AddPomeriumServiceAccountResponse](#addpomeriumserviceaccountresponse)

AddPomeriumServiceAccount creates a new service account
### DeletePomeriumServiceAccount

> **rpc** DeletePomeriumServiceAccount([DeletePomeriumServiceAccountRequest](#deletepomeriumserviceaccountrequest))
    [DeletePomeriumServiceAccountResponse](#deletepomeriumserviceaccountresponse)

DeletePomeriumServiceAccount removes an existing service account
### GetPomeriumServiceAccount

> **rpc** GetPomeriumServiceAccount([GetPomeriumServiceAccountRequest](#getpomeriumserviceaccountrequest))
    [GetPomeriumServiceAccountResponse](#getpomeriumserviceaccountresponse)

GetPomeriumServiceAccount retrieves an existing service account
### ListPomeriumServiceAccounts

> **rpc** ListPomeriumServiceAccounts([ListPomeriumServiceAccountsRequest](#listpomeriumserviceaccountsrequest))
    [ListPomeriumServiceAccountsResponse](#listpomeriumserviceaccountsresponse)

ListPomeriumServiceAccounts lists service accounts based on the parameters
in ListPomeriumServiceAccountsRequest
### SetPomeriumServiceAccount

> **rpc** SetPomeriumServiceAccount([SetPomeriumServiceAccountRequest](#setpomeriumserviceaccountrequest))
    [SetPomeriumServiceAccountResponse](#setpomeriumserviceaccountresponse)


 <!-- end methods -->
# PomeriumSessionService
PomeriumSessionService manages user sessions inside the databroker

## Methods
### DeletePomeriumSession

> **rpc** DeletePomeriumSession([DeletePomeriumSessionRequest](#deletepomeriumsessionrequest))
    [DeletePomeriumSessionResponse](#deletepomeriumsessionresponse)

DeletePomeriumSession clears an existing user session
### GetPomeriumSession

> **rpc** GetPomeriumSession([GetPomeriumSessionRequest](#getpomeriumsessionrequest))
    [GetPomeriumSessionResponse](#getpomeriumsessionresponse)

GetPomeriumSession retrieves information about an existing user session
### Impersonate

> **rpc** Impersonate([ImpersonateRequest](#impersonaterequest))
    [ImpersonateResponse](#impersonateresponse)

Impersonate updates an existing session to impersonate another identity
### ListPomeriumSessions

> **rpc** ListPomeriumSessions([ListPomeriumSessionsRequest](#listpomeriumsessionsrequest))
    [ListPomeriumSessionsResponse](#listpomeriumsessionsresponse)

ListPomeriumSessions lists existing sessions based on the parameters of
ListPomeriumSessionsRequest
 <!-- end methods -->
# UserService
UserService supports querying directory data from the databroker

## Methods
### GetUserInfo

> **rpc** GetUserInfo([GetUserInfoRequest](#getuserinforequest))
    [GetUserInfoResponse](#getuserinforesponse)

GetUserInfo retrieves identity information and permission mappings for a
user
### QueryGroups

> **rpc** QueryGroups([QueryGroupsRequest](#querygroupsrequest))
    [QueryGroupsResponse](#querygroupsresponse)

QueryGroups retrieves groups from the databroker based on
QueryGroupsRequest parameters
### QueryUsers

> **rpc** QueryUsers([QueryUsersRequest](#queryusersrequest))
    [QueryUsersResponse](#queryusersresponse)

QueryUsers retrieves users from the databroker based on QueryUsersRequest
parameters
 <!-- end methods -->
 <!-- end services -->

## Messages


### AddPomeriumServiceAccountRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| service_account | [ PomeriumServiceAccount](#pomeriumserviceaccount) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### AddPomeriumServiceAccountResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| service_account | [ PomeriumServiceAccount](#pomeriumserviceaccount) | none |
| JWT | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeletePomeriumServiceAccountRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeletePomeriumServiceAccountResponse


 <!-- end HasFields -->


### DeletePomeriumSessionRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### DeletePomeriumSessionResponse


 <!-- end HasFields -->


### GetPomeriumServiceAccountRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetPomeriumServiceAccountResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| service_account | [ PomeriumServiceAccount](#pomeriumserviceaccount) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetPomeriumSessionRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetPomeriumSessionResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| session | [ PomeriumSession](#pomeriumsession) | none |
| associated_sessions | [repeated PomeriumSession](#pomeriumsession) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetUserInfoRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _user_id.user_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GetUserInfoResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| user_info | [ UserInfo](#userinfo) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### GroupInfo
GroupInfo defines a directory group in the databroker


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ImpersonateRequest
ImpersonateRequest defines the identity information to impersonate


| Field | Type | Description |
| ----- | ---- | ----------- |
| session_id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ImpersonateResponse


 <!-- end HasFields -->


### ListPomeriumServiceAccountsRequest
ListPomeriumServiceAccountsRequest specifies the service accounts to list


| Field | Type | Description |
| ----- | ---- | ----------- |
| namespace | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListPomeriumServiceAccountsResponse
ListPomeriumServiceAccountsResponse is the list of service accounts found for
a ListPomeriumServiceAccountsRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| service_accounts | [repeated PomeriumServiceAccount](#pomeriumserviceaccount) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListPomeriumSessionsRequest
ListPomeriumSessionsRequest specifies the sessions to list


| Field | Type | Description |
| ----- | ---- | ----------- |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _query.query | [optional string](#string) | list Sessions with any fields that contain the query string |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _offset.offset | [optional int64](#int64) | list Sessions starting from an offset in the total list |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _limit.limit | [optional int64](#int64) | limit the number of Session entries returned |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _order_by.order_by | [optional string](#string) | sort the Sessions by newest, oldest or name |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _user_id.user_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### ListPomeriumSessionsResponse
ListPomeriumSessionsResponse is the sessions found for a
ListPomeriumSessionsRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| sessions | [repeated PomeriumSession](#pomeriumsession) | none |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### PomeriumServiceAccount
PomeriumServiceAccount defines the identity properties of a service account


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _namespace_id.namespace_id | [optional string](#string) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _description.description | [optional string](#string) | none |
| user_id | [ string](#string) | none |
| accessed_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| expires_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| issued_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _originator_id.originator_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### PomeriumSession
PomeriumSession defines a user session from the databroker


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| user | [ PomeriumSession.User](#pomeriumsessionuser) | none |
| groups | [repeated PomeriumSession.Group](#pomeriumsessiongroup) | none |
| issuer | [ string](#string) | none |
| accessed_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| issued_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| expires_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| audience | [repeated string](#string) | none |
| claims | [map PomeriumSession.ClaimsEntry](#pomeriumsessionclaimsentry) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### PomeriumSession.ClaimsEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ google.protobuf.ListValue](#googleprotobuflistvalue) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### PomeriumSession.Group



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
| email | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### PomeriumSession.User



| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
| email | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### QueryGroupsRequest
QueryGroupsRequest defines the groups to retrieve


| Field | Type | Description |
| ----- | ---- | ----------- |
| query | [ string](#string) | none |
| offset | [ int64](#int64) | none |
| limit | [ int64](#int64) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### QueryGroupsResponse
QueryGroupsResponse is the list of groups retrieved from a QueryGroupsRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| groups | [repeated GroupInfo](#groupinfo) | none |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### QueryUsersRequest
QueryUsersRequest defines the users to retrieve


| Field | Type | Description |
| ----- | ---- | ----------- |
| query | [ string](#string) | list Users with any fields that match the query |
| offset | [ int64](#int64) | list Users starting from an offset in the total list |
| limit | [ int64](#int64) | limit the number of User entries returned |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### QueryUsersResponse
QueryUsersResponse is the list of users retrieved from a QueryUsersRequest


| Field | Type | Description |
| ----- | ---- | ----------- |
| users | [repeated UserInfo](#userinfo) | none |
| total_count | [ int64](#int64) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### RecoveryToken
RecoveryToken is a recovery account for logging into the console without a
functioning Pomerium proxy


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| namespace | [ string](#string) | none |
| created_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| modified_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| expires_at | [ google.protobuf.Timestamp](#googleprotobuftimestamp) | none |
| public_key | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetPomeriumServiceAccountRequest



| Field | Type | Description |
| ----- | ---- | ----------- |
| service_account | [ PomeriumServiceAccount](#pomeriumserviceaccount) | none |
| [**oneof**](https://developers.google.com/protocol-buffers/docs/proto3#oneof) _cluster_id.cluster_id | [optional string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### SetPomeriumServiceAccountResponse



| Field | Type | Description |
| ----- | ---- | ----------- |
| service_account | [ PomeriumServiceAccount](#pomeriumserviceaccount) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### UserInfo
UserInfo defines the metadata for a directory user in the databroker


| Field | Type | Description |
| ----- | ---- | ----------- |
| id | [ string](#string) | none |
| name | [ string](#string) | none |
| email | [ string](#string) | none |
| groups | [repeated string](#string) | none |
| namespace_roles | [map UserInfo.NamespaceRolesEntry](#userinfonamespacerolesentry) | none |
| picture_url | [ string](#string) | none |
| is_impersonated | [ bool](#bool) | none |
 <!-- end Fields -->
 <!-- end HasFields -->


### UserInfo.NamespaceRolesEntry



| Field | Type | Description |
| ----- | ---- | ----------- |
| key | [ string](#string) | none |
| value | [ string](#string) | none |
 <!-- end Fields -->
 <!-- end HasFields -->
 <!-- end messages -->

## Enums
 <!-- end Enums -->
 <!-- end Files -->

# Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <div><h4 id="double" /></div><a name="double" /> double |  | double | double | float |
| <div><h4 id="float" /></div><a name="float" /> float |  | float | float | float |
| <div><h4 id="int32" /></div><a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <div><h4 id="int64" /></div><a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <div><h4 id="uint32" /></div><a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <div><h4 id="uint64" /></div><a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <div><h4 id="sint32" /></div><a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <div><h4 id="sint64" /></div><a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <div><h4 id="fixed32" /></div><a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <div><h4 id="fixed64" /></div><a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <div><h4 id="sfixed32" /></div><a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int |
| <div><h4 id="sfixed64" /></div><a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <div><h4 id="bool" /></div><a name="bool" /> bool |  | bool | boolean | boolean |
| <div><h4 id="string" /></div><a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <div><h4 id="bytes" /></div><a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |
