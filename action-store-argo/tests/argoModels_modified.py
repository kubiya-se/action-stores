from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union


class accountAccount(BaseModel):
    capabilities: Optional[List[str]] = Field(None, description="")
    enabled: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    tokens: Optional[List[accountToken]] = Field(None, description="")

class accountAccountsList(BaseModel):
    items: Optional[List[accountAccount]] = Field(None, description="")

class accountCanIResponse(BaseModel):
    value: Optional[str] = Field(None, description="")

class accountCreateTokenRequest(BaseModel):
    expiresIn: Optional[str] = Field(None, description="")
    id: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")

class accountCreateTokenResponse(BaseModel):
    token: Optional[str] = Field(None, description="")

class accountEmptyResponse(BaseModel):
    pass

class accountToken(BaseModel):
    expiresAt: Optional[str] = Field(None, description="")
    id: Optional[str] = Field(None, description="")
    issuedAt: Optional[str] = Field(None, description="")

class accountUpdatePasswordRequest(BaseModel):
    currentPassword: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    newPassword: Optional[str] = Field(None, description="")

class accountUpdatePasswordResponse(BaseModel):
    pass

class applicationApplicationManifestQueryWithFiles(BaseModel):
    appNamespace: Optional[str] = Field(None, description="")
    checksum: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

class applicationApplicationManifestQueryWithFilesWrapper(BaseModel):
    chunk: Optional[applicationFileChunk] = Field(None, description="")
    query: Optional[applicationApplicationManifestQueryWithFiles] = Field(None, description="")

class applicationApplicationPatchRequest(BaseModel):
    appNamespace: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    patch: Optional[str] = Field(None, description="")
    patchType: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

class applicationApplicationResourceResponse(BaseModel):
    manifest: Optional[str] = Field(None, description="")

class applicationApplicationResponse(BaseModel):
    pass

class applicationApplicationRollbackRequest(BaseModel):
    appNamespace: Optional[str] = Field(None, description="")
    dryRun: Optional[bool] = Field(None, description="")
    id: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")
    prune: Optional[bool] = Field(None, description="")

class applicationApplicationSyncRequest(BaseModel):
    appNamespace: Optional[str] = Field(None, description="")
    dryRun: Optional[bool] = Field(None, description="")
    infos: Optional[List[v1alpha1Info]] = Field(None, description="")
    manifests: Optional[List[str]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")
    prune: Optional[bool] = Field(None, description="")
    resources: Optional[List[v1alpha1SyncOperationResource]] = Field(None, description="")
    retryStrategy: Optional[v1alpha1RetryStrategy] = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    strategy: Optional[v1alpha1SyncStrategy] = Field(None, description="")
    syncOptions: Optional[applicationSyncOptions] = Field(None, description="")

class applicationApplicationSyncWindow(BaseModel):
    duration: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    manualSync: Optional[bool] = Field(None, description="")
    schedule: Optional[str] = Field(None, description="")

class applicationApplicationSyncWindowsResponse(BaseModel):
    activeWindows: Optional[List[applicationApplicationSyncWindow]] = Field(None, description="")
    assignedWindows: Optional[List[applicationApplicationSyncWindow]] = Field(None, description="")
    canSync: Optional[bool] = Field(None, description="")

class applicationFileChunk(BaseModel):
    chunk: Optional[str] = Field(None, description="")

class applicationLinkInfo(BaseModel):
    description: Optional[str] = Field(None, description="")
    iconClass: Optional[str] = Field(None, description="")
    title: Optional[str] = Field(None, description="")
    url: Optional[str] = Field(None, description="")

class applicationLinksResponse(BaseModel):
    items: Optional[List[applicationLinkInfo]] = Field(None, description="")

class applicationLogEntry(BaseModel):
    content: Optional[str] = Field(None, description="")
    last: Optional[bool] = Field(None, description="")
    podName: Optional[str] = Field(None, description="")
    timeStamp: Optional[v1Time] = Field(None, description="")
    timeStampStr: Optional[str] = Field(None, description="")

class applicationManagedResourcesResponse(BaseModel):
    items: Optional[List[v1alpha1ResourceDiff]] = Field(None, description="")

class applicationOperationTerminateResponse(BaseModel):
    pass

class applicationResourceActionsListResponse(BaseModel):
    actions: Optional[List[v1alpha1ResourceAction]] = Field(None, description="")

class applicationSyncOptions(BaseModel):
    items: Optional[List[str]] = Field(None, description="")

class applicationsetApplicationSetResponse(BaseModel):
    applicationset: Optional[v1alpha1ApplicationSet] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

class applicationv1alpha1EnvEntry(BaseModel):
    name: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class clusterClusterID(BaseModel):
    type: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class clusterClusterResponse(BaseModel):
    pass

class clusterConnector(BaseModel):
    name: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class clusterDexConfig(BaseModel):
    connectors: Optional[List[clusterConnector]] = Field(None, description="")

class clusterGoogleAnalyticsConfig(BaseModel):
    anonymizeUsers: Optional[bool] = Field(None, description="")
    trackingID: Optional[str] = Field(None, description="")

class clusterHelp(BaseModel):
    binaryUrls: Optional[Dict[str, Any]] = Field(None, description="")
    chatText: Optional[str] = Field(None, description="")
    chatUrl: Optional[str] = Field(None, description="")

class clusterOIDCConfig(BaseModel):
    cliClientID: Optional[str] = Field(None, description="")
    clientID: Optional[str] = Field(None, description="")
    idTokenClaims: Optional[Dict[str, Any]] = Field(None, description="")
    issuer: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    scopes: Optional[List[str]] = Field(None, description="")

class clusterPlugin(BaseModel):
    name: Optional[str] = Field(None, description="")

class clusterSettings(BaseModel):
    appLabelKey: Optional[str] = Field(None, description="")
    appsInAnyNamespaceEnabled: Optional[bool] = Field(None, description="")
    configManagementPlugins: Optional[List[v1alpha1ConfigManagementPlugin]] = Field(None, description="Deprecated: use sidecar plugins instead.")
    controllerNamespace: Optional[str] = Field(None, description="")
    dexConfig: Optional[clusterDexConfig] = Field(None, description="")
    execEnabled: Optional[bool] = Field(None, description="")
    googleAnalytics: Optional[clusterGoogleAnalyticsConfig] = Field(None, description="")
    help: Optional[clusterHelp] = Field(None, description="")
    kustomizeOptions: Optional[v1alpha1KustomizeOptions] = Field(None, description="")
    kustomizeVersions: Optional[List[str]] = Field(None, description="")
    oidcConfig: Optional[clusterOIDCConfig] = Field(None, description="")
    passwordPattern: Optional[str] = Field(None, description="")
    plugins: Optional[List[clusterPlugin]] = Field(None, description="")
    resourceOverrides: Optional[Dict[str, Any]] = Field(None, description="")
    statusBadgeEnabled: Optional[bool] = Field(None, description="")
    statusBadgeRootUrl: Optional[str] = Field(None, description="")
    trackingMethod: Optional[str] = Field(None, description="")
    uiBannerContent: Optional[str] = Field(None, description="")
    uiBannerPermanent: Optional[bool] = Field(None, description="")
    uiBannerPosition: Optional[str] = Field(None, description="")
    uiBannerURL: Optional[str] = Field(None, description="")
    uiCssURL: Optional[str] = Field(None, description="")
    url: Optional[str] = Field(None, description="")
    userLoginsDisabled: Optional[bool] = Field(None, description="")

class clusterSettingsPluginsResponse(BaseModel):
    plugins: Optional[List[clusterPlugin]] = Field(None, description="")

class gpgkeyGnuPGPublicKeyCreateResponse(BaseModel):
    created: Optional[v1alpha1GnuPGPublicKeyList] = Field(None, description="")
    skipped: Optional[List[str]] = Field(None, description="")

class gpgkeyGnuPGPublicKeyResponse(BaseModel):
    pass

class intstrIntOrString(BaseModel):
    intVal: Optional[int] = Field(None, description="")
    strVal: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class notificationService(BaseModel):
    name: Optional[str] = Field(None, description="")

class notificationServiceList(BaseModel):
    items: Optional[List[notificationService]] = Field(None, description="")

class notificationTemplate(BaseModel):
    name: Optional[str] = Field(None, description="")

class notificationTemplateList(BaseModel):
    items: Optional[List[notificationTemplate]] = Field(None, description="")

class notificationTrigger(BaseModel):
    name: Optional[str] = Field(None, description="")

class notificationTriggerList(BaseModel):
    items: Optional[List[notificationTrigger]] = Field(None, description="")

class oidcClaim(BaseModel):
    essential: Optional[bool] = Field(None, description="")
    value: Optional[str] = Field(None, description="")
    values: Optional[List[str]] = Field(None, description="")

class projectDetailedProjectsResponse(BaseModel):
    clusters: Optional[List[v1alpha1Cluster]] = Field(None, description="")
    globalProjects: Optional[List[v1alpha1AppProject]] = Field(None, description="")
    project: Optional[v1alpha1AppProject] = Field(None, description="")
    repositories: Optional[List[v1alpha1Repository]] = Field(None, description="")

class projectEmptyResponse(BaseModel):
    pass

class projectGlobalProjectsResponse(BaseModel):
    items: Optional[List[v1alpha1AppProject]] = Field(None, description="")

class projectProjectCreateRequest(BaseModel):
    project: Optional[v1alpha1AppProject] = Field(None, description="")
    upsert: Optional[bool] = Field(None, description="")

class projectProjectTokenCreateRequest(BaseModel):
    description: Optional[str] = Field(None, description="")
    expiresIn: Optional[str] = Field(None, description="")
    id: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")
    role: Optional[str] = Field(None, description="")

class projectProjectTokenResponse(BaseModel):
    token: Optional[str] = Field(None, description="")

class projectProjectUpdateRequest(BaseModel):
    project: Optional[v1alpha1AppProject] = Field(None, description="")

class projectSyncWindowsResponse(BaseModel):
    windows: Optional[List[v1alpha1SyncWindow]] = Field(None, description="")

class protobufAny(BaseModel):
    type_url: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class repocredsRepoCredsResponse(BaseModel):
    pass

class repositoryAppInfo(BaseModel):
    path: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class repositoryDirectoryAppSpec(BaseModel):
    pass

class repositoryHelmAppSpec(BaseModel):
    fileParameters: Optional[List[v1alpha1HelmFileParameter]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    parameters: Optional[List[v1alpha1HelmParameter]] = Field(None, description="")
    valueFiles: Optional[List[str]] = Field(None, description="")
    values: Optional[str] = Field(None, description="")

class repositoryHelmChart(BaseModel):
    name: Optional[str] = Field(None, description="")
    versions: Optional[List[str]] = Field(None, description="")

class repositoryHelmChartsResponse(BaseModel):
    items: Optional[List[repositoryHelmChart]] = Field(None, description="")

class repositoryKustomizeAppSpec(BaseModel):
    images: Optional[List[str]] = Field(None, description="images is a list of available images.")

class repositoryManifestResponse(BaseModel):
    manifests: Optional[List[str]] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    server: Optional[str] = Field(None, description="")
    sourceType: Optional[str] = Field(None, description="")
    verifyResult: Optional[str] = Field(None, description="")

class repositoryParameterAnnouncement(BaseModel):
    array: Optional[List[str]] = Field(None, description="array is the default value of the parameter if the parameter is an array.")
    collectionType: Optional[str] = Field(None, description="collectionType is the type of value this parameter holds - either a single value (a string) or a collection (array or map). If collectionType is set, only the field with that type will be used. If collectionType is not set, `string` is the default. If collectionType is set to an invalid value, a validation error is thrown.")
    itemType: Optional[str] = Field(None, description="itemType determines the primitive data type represented by the parameter. Parameters are always encoded as strings, but this field lets them be interpreted as other primitive types.")
    map: Optional[Dict[str, Any]] = Field(None, description="map is the default value of the parameter if the parameter is a map.")
    name: Optional[str] = Field(None, description="name is the name identifying a parameter.")
    required: Optional[bool] = Field(None, description="required defines if this given parameter is mandatory.")
    string: Optional[str] = Field(None, description="string is the default value of the parameter if the parameter is a string.")
    title: Optional[str] = Field(None, description="title is a human-readable text of the parameter name.")
    tooltip: Optional[str] = Field(None, description="tooltip is a human-readable description of the parameter.")

class repositoryPluginAppSpec(BaseModel):
    parametersAnnouncement: Optional[List[repositoryParameterAnnouncement]] = Field(None, description="")

class repositoryRefs(BaseModel):
    branches: Optional[List[str]] = Field(None, description="")
    tags: Optional[List[str]] = Field(None, description="")

class repositoryRepoAppDetailsQuery(BaseModel):
    appName: Optional[str] = Field(None, description="")
    appProject: Optional[str] = Field(None, description="")
    source: Optional[v1alpha1ApplicationSource] = Field(None, description="")

class repositoryRepoAppDetailsResponse(BaseModel):
    directory: Optional[repositoryDirectoryAppSpec] = Field(None, description="")
    helm: Optional[repositoryHelmAppSpec] = Field(None, description="")
    kustomize: Optional[repositoryKustomizeAppSpec] = Field(None, description="")
    plugin: Optional[repositoryPluginAppSpec] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class repositoryRepoAppsResponse(BaseModel):
    items: Optional[List[repositoryAppInfo]] = Field(None, description="")

class repositoryRepoResponse(BaseModel):
    pass

class runtimeError(BaseModel):
    code: Optional[int] = Field(None, description="")
    details: Optional[List[protobufAny]] = Field(None, description="")
    error: Optional[str] = Field(None, description="")
    message: Optional[str] = Field(None, description="")

class runtimeRawExtension(BaseModel):
    raw: Optional[str] = Field(None, description="Raw is the underlying serialization of this object. TODO: Determine how to detect ContentType and ContentEncoding of 'Raw' data.")

class runtimeStreamError(BaseModel):
    details: Optional[List[protobufAny]] = Field(None, description="")
    grpc_code: Optional[int] = Field(None, description="")
    http_code: Optional[int] = Field(None, description="")
    http_status: Optional[str] = Field(None, description="")
    message: Optional[str] = Field(None, description="")

class sessionGetUserInfoResponse(BaseModel):
    groups: Optional[List[str]] = Field(None, description="")
    iss: Optional[str] = Field(None, description="")
    loggedIn: Optional[bool] = Field(None, description="")
    username: Optional[str] = Field(None, description="")

class sessionSessionCreateRequest(BaseModel):
    password: Optional[str] = Field(None, description="")
    token: Optional[str] = Field(None, description="")
    username: Optional[str] = Field(None, description="")

class sessionSessionResponse(BaseModel):
    token: Optional[str] = Field(None, description="")

class v1Event(BaseModel):
    action: Optional[str] = Field(None, description="")
    count: Optional[int] = Field(None, description="")
    eventTime: Optional[v1MicroTime] = Field(None, description="")
    firstTimestamp: Optional[v1Time] = Field(None, description="")
    involvedObject: Optional[v1ObjectReference] = Field(None, description="")
    lastTimestamp: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="")
    metadata: Optional[v1ObjectMeta] = Field(None, description="")
    reason: Optional[str] = Field(None, description="")
    related: Optional[v1ObjectReference] = Field(None, description="")
    reportingComponent: Optional[str] = Field(None, description="")
    reportingInstance: Optional[str] = Field(None, description="")
    series: Optional[v1EventSeries] = Field(None, description="")
    source: Optional[v1EventSource] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class v1EventList(BaseModel):
    items: Optional[List[v1Event]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1EventSeries(BaseModel):
    count: Optional[int] = Field(None, description="")
    lastObservedTime: Optional[v1MicroTime] = Field(None, description="")

class v1EventSource(BaseModel):
    component: Optional[str] = Field(None, description="")
    host: Optional[str] = Field(None, description="")

class v1FieldsV1(BaseModel):
    Raw: Optional[str] = Field(None, description="Raw is the underlying serialization of this object.")

class v1GroupKind(BaseModel):
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")

class v1JSON(BaseModel):
    raw: Optional[str] = Field(None, description="")

class v1LabelSelector(BaseModel):
    matchExpressions: Optional[List[v1LabelSelectorRequirement]] = Field(None, description="")
    matchLabels: Optional[Dict[str, Any]] = Field(None, description="")

class v1LabelSelectorRequirement(BaseModel):
    key: Optional[str] = Field(None, description="")
    operator: Optional[str] = Field(None, description="operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.")
    values: Optional[List[str]] = Field(None, description="")

class v1ListMeta(BaseModel):
    _continue: Optional[str] = Field(None, alias = "continue")
    remainingItemCount: Optional[str] = Field(None, description="")
    resourceVersion: Optional[str] = Field(None, description="")
    selfLink: Optional[str] = Field(None, description="")

class v1LoadBalancerIngress(BaseModel):
    hostname: Optional[str] = Field(None, description="")
    ip: Optional[str] = Field(None, description="")
    ports: Optional[List[v1PortStatus]] = Field(None, description="")

class v1ManagedFieldsEntry(BaseModel):
    apiVersion: Optional[str] = Field(None, description="APIVersion defines the version of this resource that this field set applies to. The format is groupversion just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.")
    fieldsType: Optional[str] = Field(None, description="")
    fieldsV1: Optional[v1FieldsV1] = Field(None, description="")
    manager: Optional[str] = Field(None, description="Manager is an identifier of the workflow managing these fields.")
    operation: Optional[str] = Field(
        None,
        description=(
            "Operation is the type of operation which lead to this ManagedFieldsEntry being created. "
            "The only valid values for this field are 'Apply' and 'Update'."
        )
    )
    subresource: Optional[str] = Field(
        None,
        description=(
            "Subresource is the name of the subresource used to update that object, or "
            "empty string if the object was updated through the main resource. The "
            "value of this field is used to distinguish between managers, even if they "
            "share the same name. For example, a status update will be distinct from a "
            "regular update using the same manager name. "
            "Note that the APIVersion field is not related to the Subresource field and "
            "it always corresponds to the version of the main resource."
        )
    )
    time: Optional[v1Time] = Field(None, description="")


class v1MicroTime(BaseModel):
    nanos: Optional[int] = Field(
        None,
        description=(
            "Non-negative fractions of a second at nanosecond resolution. Negative "
            "second values with fractions must still have non-negative nanos values "
            "that count forward in time. Must be from 0 to 999,999,999 "
            "inclusive. This field may be limited in precision depending on context."
        )
    )
    seconds: Optional[str] = Field(
        None,
        description=(
            "Represents seconds of UTC time since Unix epoch "
            "1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to "
            "9999-12-31T23:59:59Z inclusive."
        )
    )

class v1NodeSystemInfo(BaseModel):
    architecture: Optional[str] = Field(None, description="")
    bootID: Optional[str] = Field(None, description="Boot ID reported by the node.")
    containerRuntimeVersion: Optional[str] = Field(None, description="ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).")
    kernelVersion: Optional[str] = Field(None, description="Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).")
    kubeProxyVersion: Optional[str] = Field(None, description="KubeProxy Version reported by the node.")
    kubeletVersion: Optional[str] = Field(None, description="Kubelet Version reported by the node.")
    machineID: Optional[str] = Field(None, description="")
    operatingSystem: Optional[str] = Field(None, description="")
    osImage: Optional[str] = Field(None, description="OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).")
    systemUUID: Optional[str] = Field(None, description="")

#Look over this

class v1ObjectMeta(BaseModel):
    annotations: Optional[Dict[str, Any]] = Field(None, description="")
    clusterName: Optional[str] = Field(None, description="")

class v1ObjectReference(BaseModel):
    apiVersion: Optional[str] = Field(None, description="")
    fieldPath: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceVersion: Optional[str] = Field(None, description="")
    uid: Optional[str] = Field(None, description="")

class v1OwnerReference(BaseModel):
    apiVersion: Optional[str] = Field(None, description="API version of the referent.")
    blockOwnerDeletion: Optional[bool] = Field(None, description="")
    controller: Optional[bool] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    uid: Optional[str] = Field(None, description="")

class v1PortStatus(BaseModel):
    error: Optional[str] = Field(None, description="")
    port: Optional[int] = Field(None, description="")
    protocol: Optional[str] = Field(None, description="")

class v1Time(BaseModel):
    nanos: Optional[int] = Field(
        None,
        description=(
            "Non-negative fractions of a second at nanosecond resolution. Negative "
            "second values with fractions must still have non-negative nanos values "
            "that count forward in time. Must be from 0 to 999,999,999 "
            "inclusive. This field may be limited in precision depending on context."
        )
    )
    seconds: Optional[str] = Field(
        None,
        description=(
            "Represents seconds of UTC time since Unix epoch "
            "1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to "
            "9999-12-31T23:59:59Z inclusive."
        )
    )

class v1alpha1AWSAuthConfig(BaseModel):
    clusterName: Optional[str] = Field(None, description="")
    roleARN: Optional[str] = Field(None, description="RoleARN contains optional role ARN. If set then AWS IAM Authenticator assume a role to perform cluster operations instead of the default AWS credential provider chain.")

class v1alpha1AppProject(BaseModel):
    metadata: Optional[v1ObjectMeta] = Field(None, description="")
    spec: Optional[v1alpha1AppProjectSpec] = Field(None, description="")
    status: Optional[v1alpha1AppProjectStatus] = Field(None, description="")

class v1alpha1AppProjectList(BaseModel):
    items: Optional[List[v1alpha1AppProject]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1AppProjectSpec(BaseModel):
    clusterResourceBlacklist: Optional[List[v1GroupKind]] = Field(None, description="")
    clusterResourceWhitelist: Optional[List[v1GroupKind]] = Field(None, description="")
    description: Optional[str] = Field(None, description="")
    destinations: Optional[List[v1alpha1ApplicationDestination]] = Field(None, description="")
    namespaceResourceBlacklist: Optional[List[v1GroupKind]] = Field(None, description="")
    namespaceResourceWhitelist: Optional[List[v1GroupKind]] = Field(None, description="")
    orphanedResources: Optional[v1alpha1OrphanedResourcesMonitorSettings] = Field(None, description="")
    permitOnlyProjectScopedClusters: Optional[bool] = Field(None, description="")
    roles: Optional[List[v1alpha1ProjectRole]] = Field(None, description="")
    signatureKeys: Optional[List[v1alpha1SignatureKey]] = Field(None, description="")
    sourceNamespaces: Optional[List[str]] = Field(None, description="")
    sourceRepos: Optional[List[str]] = Field(None, description="")
    syncWindows: Optional[List[v1alpha1SyncWindow]] = Field(None, description="")

class v1alpha1AppProjectStatus(BaseModel):
    jwtTokensByRole: Optional[Dict[str, Any]] = Field(None, description="")

class v1alpha1Application(BaseModel):
    metadata: Optional[v1ObjectMeta] = Field(None, description="")
    operation: Optional[v1alpha1Operation] = Field(None, description="")
    spec: Optional[v1alpha1ApplicationSpec] = Field(None, description="")
    status: Optional[v1alpha1ApplicationStatus] = Field(None, description="")

class v1alpha1ApplicationCondition(BaseModel):
    lastTransitionTime: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class v1alpha1ApplicationDestination(BaseModel):
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    server: Optional[str] = Field(None, description="")

class v1alpha1ApplicationList(BaseModel):
    items: Optional[List[v1alpha1Application]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1ApplicationMatchExpression(BaseModel):
    key: Optional[str] = Field(None, description="")
    operator: Optional[str] = Field(None, description="")
    values: Optional[List[str]] = Field(None, description="")

class v1alpha1ApplicationPreservedFields(BaseModel):
    annotations: Optional[List[str]] = Field(None, description="")

class v1alpha1ApplicationSet(BaseModel):
    metadata: Optional[v1ObjectMeta] = Field(None, description="")
    spec: Optional[v1alpha1ApplicationSetSpec] = Field(None, description="")
    status: Optional[v1alpha1ApplicationSetStatus] = Field(None, description="")

class v1alpha1ApplicationSetApplicationStatus(BaseModel):
    application: Optional[str] = Field(None, description="")
    lastTransitionTime: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="")
    status: Optional[str] = Field(None, description="")
    step: Optional[str] = Field(None, description="")

class v1alpha1ApplicationSetCondition(BaseModel):
    lastTransitionTime: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="")
    reason: Optional[str] = Field(None, description="")
    status: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class v1alpha1ApplicationSetGenerator(BaseModel):
    clusterDecisionResource: Optional[v1alpha1DuckTypeGenerator] = Field(None, description="")
    clusters: Optional[v1alpha1ClusterGenerator] = Field(None, description="")
    git: Optional[v1alpha1GitGenerator] = Field(None, description="")
    list: Optional[v1alpha1ListGenerator] = Field(None, description="")
    matrix: Optional[v1alpha1MatrixGenerator] = Field(None, description="")
    merge: Optional[v1alpha1MergeGenerator] = Field(None, description="")
    plugin: Optional[v1alpha1PluginGenerator] = Field(None, description="")
    pullRequest: Optional[v1alpha1PullRequestGenerator] = Field(None, description="")
    scmProvider: Optional[v1alpha1SCMProviderGenerator] = Field(None, description="")
    selector: Optional[v1LabelSelector] = Field(None, description="")

class v1alpha1ApplicationSetList(BaseModel):
    items: Optional[List[v1alpha1ApplicationSet]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1ApplicationSetNestedGenerator(BaseModel):
    clusterDecisionResource: Optional[v1alpha1DuckTypeGenerator] = Field(None, description="")
    clusters: Optional[v1alpha1ClusterGenerator] = Field(None, description="")
    git: Optional[v1alpha1GitGenerator] = Field(None, description="")
    list: Optional[v1alpha1ListGenerator] = Field(None, description="")
    matrix: Optional[v1JSON] = Field(None, description="")
    merge: Optional[v1JSON] = Field(None, description="")
    plugin: Optional[v1alpha1PluginGenerator] = Field(None, description="")
    pullRequest: Optional[v1alpha1PullRequestGenerator] = Field(None, description="")
    scmProvider: Optional[v1alpha1SCMProviderGenerator] = Field(None, description="")
    selector: Optional[v1LabelSelector] = Field(None, description="")

class v1alpha1ApplicationSetRolloutStep(BaseModel):
    matchExpressions: Optional[List[v1alpha1ApplicationMatchExpression]] = Field(None, description="")
    maxUpdate: Optional[intstrIntOrString] = Field(None, description="")

class v1alpha1ApplicationSetRolloutStrategy(BaseModel):
    steps: Optional[List[v1alpha1ApplicationSetRolloutStep]] = Field(None, description="")

class v1alpha1ApplicationSetSpec(BaseModel):
    applyNestedSelectors: Optional[bool] = Field(None, description="")
    generators: Optional[List[v1alpha1ApplicationSetGenerator]] = Field(None, description="")
    goTemplate: Optional[bool] = Field(None, description="")
    goTemplateOptions: Optional[List[str]] = Field(None, description="")
    preservedFields: Optional[v1alpha1ApplicationPreservedFields] = Field(None, description="")
    strategy: Optional[v1alpha1ApplicationSetStrategy] = Field(None, description="")
    syncPolicy: Optional[v1alpha1ApplicationSetSyncPolicy] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")

class v1alpha1ApplicationSetStatus(BaseModel):
    applicationStatus: Optional[List[v1alpha1ApplicationSetApplicationStatus]] = Field(None, description="")
    conditions: Optional[List[v1alpha1ApplicationSetCondition]] = Field(None, description="")

class v1alpha1ApplicationSetStrategy(BaseModel):
    rollingSync: Optional[v1alpha1ApplicationSetRolloutStrategy] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class v1alpha1ApplicationSetSyncPolicy(BaseModel):
    applicationsSync: Optional[str] = Field(None, description="")
    preserveResourcesOnDeletion: Optional[bool] = Field(None, description="PreserveResourcesOnDeletion will preserve resources on deletion. If PreserveResourcesOnDeletion is set to true, these Applications will not be deleted.")

class v1alpha1ApplicationSetTemplate(BaseModel):
    metadata: Optional[v1alpha1ApplicationSetTemplateMeta] = Field(None, description="")
    spec: Optional[v1alpha1ApplicationSpec] = Field(None, description="")

class v1alpha1ApplicationSetTemplateMeta(BaseModel):
    annotations: Optional[Dict[str, Any]] = Field(None, description="")
    finalizers: Optional[List[str]] = Field(None, description="")
    labels: Optional[Dict[str, Any]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")

class v1alpha1ApplicationSource(BaseModel):
    chart: Optional[str] = Field(None, description="Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo.")
    directory: Optional[v1alpha1ApplicationSourceDirectory] = Field(None, description="")
    helm: Optional[v1alpha1ApplicationSourceHelm] = Field(None, description="")
    kustomize: Optional[v1alpha1ApplicationSourceKustomize] = Field(None, description="")
    path: Optional[str] = Field(None, description="Path is a directory path within the Git repository, and is only valid for applications sourced from Git.")
    plugin: Optional[v1alpha1ApplicationSourcePlugin] = Field(None, description="")
    ref: Optional[str] = Field(None, description="Ref is reference to another source within sources field. This field will not be used if used with a `source` tag.")
    repoURL: Optional[str] = Field(None, description="")
    targetRevision: Optional[str] = Field(None, description="TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version.")

class v1alpha1ApplicationSourceDirectory(BaseModel):
    exclude: Optional[str] = Field(None, description="")
    include: Optional[str] = Field(None, description="")
    jsonnet: Optional[v1alpha1ApplicationSourceJsonnet] = Field(None, description="")
    recurse: Optional[bool] = Field(None, description="")

class v1alpha1ApplicationSourceHelm(BaseModel):
    fileParameters: Optional[List[v1alpha1HelmFileParameter]] = Field(None, description="")
    ignoreMissingValueFiles: Optional[bool] = Field(None, description="")
    parameters: Optional[List[v1alpha1HelmParameter]] = Field(None, description="")
    passCredentials: Optional[bool] = Field(None, description="")
    releaseName: Optional[str] = Field(None, description="")
    skipCrds: Optional[bool] = Field(None, description="")
    valueFiles: Optional[List[str]] = Field(None, description="")
    values: Optional[str] = Field(None, description="")
    valuesObject: Optional[runtimeRawExtension] = Field(None, description="")
    version: Optional[str] = Field(None, description="")

class v1alpha1ApplicationSourceJsonnet(BaseModel):
    extVars: Optional[List[v1alpha1JsonnetVar]] = Field(None, description="")
    libs: Optional[List[str]] = Field(None, description="")
    tlas: Optional[List[v1alpha1JsonnetVar]] = Field(None, description="")

class v1alpha1ApplicationSourceKustomize(BaseModel):
    commonAnnotations: Optional[Dict[str, Any]] = Field(None, description="")
    commonAnnotationsEnvsubst: Optional[bool] = Field(None, description="")
    commonLabels: Optional[Dict[str, Any]] = Field(None, description="")
    forceCommonAnnotations: Optional[bool] = Field(None, description="")
    forceCommonLabels: Optional[bool] = Field(None, description="")
    images: Optional[List[str]] = Field(None, description="")
    namePrefix: Optional[str] = Field(None, description="")
    nameSuffix: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    replicas: Optional[List[v1alpha1KustomizeReplica]] = Field(None, description="")
    version: Optional[str] = Field(None, description="")

class v1alpha1ApplicationSourcePlugin(BaseModel):
    env: Optional[List[applicationv1alpha1EnvEntry]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    parameters: Optional[List[v1alpha1ApplicationSourcePluginParameter]] = Field(None, description="")

class v1alpha1ApplicationSourcePluginParameter(BaseModel):
    array: Optional[List[str]] = Field(None, description="Array is the value of an array type parameter.")
    map: Optional[Dict[str, Any]] = Field(None, description="Map is the value of a map type parameter.")
    name: Optional[str] = Field(None, description="Name is the name identifying a parameter.")
    string: Optional[str] = Field(None, description="String_ is the value of a string type parameter.")

class v1alpha1ApplicationSpec(BaseModel):
    destination: Optional[v1alpha1ApplicationDestination] = Field(None, description="")
    ignoreDifferences: Optional[List[v1alpha1ResourceIgnoreDifferences]] = Field(None, description="")
    info: Optional[List[v1alpha1Info]] = Field(None, description="")
    project: Optional[str] = Field(
        None,
        description="Project is a reference to the project this application belongs to. "
                "The empty string means that the application belongs to the 'default' project."
    )
    revisionHistoryLimit: Optional[str] = Field(
        None,
        description="RevisionHistoryLimit limits the number of items kept in the application's revision history, which is used for informational purposes as well as for rollbacks to previous versions. "
                "This should only be changed in exceptional circumstances. "
                "Setting to zero will store no history. This will reduce storage used. "
                "Increasing will increase the space used to store the history, so we do not recommend increasing it. "
                "Default is 10."
    )
source: Optional[v1alpha1ApplicationSource] = Field(None, description="")
sources: Optional[List[v1alpha1ApplicationSource]] = Field(None, description="")
syncPolicy: Optional[v1alpha1SyncPolicy] = Field(None, description="")


class v1alpha1ApplicationStatus(BaseModel):
    conditions: Optional[List[v1alpha1ApplicationCondition]] = Field(None, description="")
    controllerNamespace: Optional[str] = Field(None, description="")
    health: Optional[v1alpha1HealthStatus] = Field(None, description="")
    history: Optional[List[v1alpha1RevisionHistory]] = Field(None, description="")
    observedAt: Optional[v1Time] = Field(None, description="")
    operationState: Optional[v1alpha1OperationState] = Field(None, description="")
    reconciledAt: Optional[v1Time] = Field(None, description="")
    resourceHealthSource: Optional[str] = Field(None, description="")
    resources: Optional[List[v1alpha1ResourceStatus]] = Field(None, description="")
    sourceType: Optional[str] = Field(None, description="")
    sourceTypes: Optional[List[str]] = Field(None, description="")
    summary: Optional[v1alpha1ApplicationSummary] = Field(None, description="")
    sync: Optional[v1alpha1SyncStatus] = Field(None, description="")

class v1alpha1ApplicationSummary(BaseModel):
    externalURLs: Optional[List[str]] = Field(None, description="ExternalURLs holds all external URLs of application child resources.")
    images: Optional[List[str]] = Field(None, description="Images holds all images of application child resources.")

class v1alpha1ApplicationTree(BaseModel):
    hosts: Optional[List[v1alpha1HostInfo]] = Field(None, description="")
    nodes: Optional[List[v1alpha1ResourceNode]] = Field(None, description="Nodes contains list of nodes which either directly managed by the application and children of directly managed nodes.")
    orphanedNodes: Optional[List[v1alpha1ResourceNode]] = Field(None, description="OrphanedNodes contains if or orphaned nodes: nodes which are not managed by the app but in the same namespace. List is populated only if orphaned resources enabled in app project.")

class v1alpha1ApplicationWatchEvent(BaseModel):
    application: Optional[v1alpha1Application] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class v1alpha1Backoff(BaseModel):
    duration: Optional[str] = Field(None, description="")
    factor: Optional[str] = Field(None, description="")
    maxDuration: Optional[str] = Field(None, description="")

class v1alpha1BasicAuthBitbucketServer(BaseModel):
    passwordRef: Optional[v1alpha1SecretRef] = Field(None, description="")
    username: Optional[str] = Field(None, description="")

class v1alpha1BearerTokenBitbucketCloud(BaseModel):
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1ChartDetails(BaseModel):
    description: Optional[str] = Field(None, description="")
    home: Optional[str] = Field(None, description="")
    maintainers: Optional[List[str]] = Field(None, description="")

class v1alpha1Cluster(BaseModel):
    annotations: Optional[Dict[str, Any]] = Field(None, description="")
    clusterResources: Optional[bool] = Field(None, description="Indicates if cluster level resources should be managed. This setting is used only if cluster is connected in a namespaced mode.")
    config: Optional[v1alpha1ClusterConfig] = Field(None, description="")
    connectionState: Optional[v1alpha1ConnectionState] = Field(None, description="")
    info: Optional[v1alpha1ClusterInfo] = Field(None, description="")
    labels: Optional[Dict[str, Any]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespaces: Optional[List[str]] = Field(None, description="Holds list of namespaces which are accessible in that cluster. Cluster level resources will be ignored if namespace list is not empty.")
    project: Optional[str] = Field(None, description="")
    refreshRequestedAt: Optional[v1Time] = Field(None, description="")
    server: Optional[str] = Field(None, description="")
    serverVersion: Optional[str] = Field(None, description="")
    shard: Optional[str] = Field(None, description="Shard contains optional shard number. Calculated on the fly by the application controller if not specified.")

class v1alpha1ClusterCacheInfo(BaseModel):
    apisCount: Optional[str] = Field(None, description="")
    lastCacheSyncTime: Optional[v1Time] = Field(None, description="")
    resourcesCount: Optional[str] = Field(None, description="")

class v1alpha1ClusterConfig(BaseModel):
    awsAuthConfig: Optional[v1alpha1AWSAuthConfig] = Field(None, description="")
    bearerToken: Optional[str] = Field(
        None,
        description="Server requires Bearer authentication. This client will not attempt to use "
                    "refresh tokens for an OAuth2 flow. "
                    "TODO: demonstrate an OAuth2 compatible client."
    )
    execProviderConfig: Optional[v1alpha1ExecProviderConfig] = Field(None, description="")
    password: Optional[str] = Field(None, description="")
    tlsClientConfig: Optional[v1alpha1TLSClientConfig] = Field(None, description="")
    username: Optional[str] = Field(None, description="")

class v1alpha1ClusterGenerator(BaseModel):
    selector: Optional[v1LabelSelector] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")
    values: Optional[Dict[str, Any]] = Field(None, description="")

class v1alpha1ClusterInfo(BaseModel):
    apiVersions: Optional[List[str]] = Field(None, description="")
    applicationsCount: Optional[str] = Field(None, description="")
    cacheInfo: Optional[v1alpha1ClusterCacheInfo] = Field(None, description="")
    connectionState: Optional[v1alpha1ConnectionState] = Field(None, description="")
    serverVersion: Optional[str] = Field(None, description="")

class v1alpha1ClusterList(BaseModel):
    items: Optional[List[v1alpha1Cluster]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1Command(BaseModel):
    args: Optional[List[str]] = Field(None, description="")
    command: Optional[List[str]] = Field(None, description="")

class v1alpha1ComparedTo(BaseModel):
    destination: Optional[v1alpha1ApplicationDestination] = Field(None, description="")
    ignoreDifferences: Optional[List[v1alpha1ResourceIgnoreDifferences]] = Field(None, description="")
    source: Optional[v1alpha1ApplicationSource] = Field(None, description="")
    sources: Optional[List[v1alpha1ApplicationSource]] = Field(None, description="")

class v1alpha1ConfigManagementPlugin(BaseModel):
    generate: Optional[v1alpha1Command] = Field(None, description="")
    init: Optional[v1alpha1Command] = Field(None, description="")
    lockRepo: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")

class v1alpha1ConnectionState(BaseModel):
    attemptedAt: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="")
    status: Optional[str] = Field(None, description="")

class v1alpha1DuckTypeGenerator(BaseModel):
    configMapRef: Optional[str] = Field(None, description="")
    labelSelector: Optional[v1LabelSelector] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    requeueAfterSeconds: Optional[str] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")
    values: Optional[Dict[str, Any]] = Field(None, description="")

class v1alpha1ExecProviderConfig(BaseModel):
    apiVersion: Optional[str] = Field(None, description="")
    args: Optional[List[str]] = Field(None, description="")
    command: Optional[str] = Field(None, description="")
    env: Optional[Dict[str, Any]] = Field(None, description="")
    installHint: Optional[str] = Field(None, description="")

class v1alpha1GitDirectoryGeneratorItem(BaseModel):
    exclude: Optional[bool] = Field(None, description="")
    path: Optional[str] = Field(None, description="")

class v1alpha1GitFileGeneratorItem(BaseModel):
    path: Optional[str] = Field(None, description="")

class v1alpha1GitGenerator(BaseModel):
    directories: Optional[List[v1alpha1GitDirectoryGeneratorItem]] = Field(None, description="")
    files: Optional[List[v1alpha1GitFileGeneratorItem]] = Field(None, description="")
    pathParamPrefix: Optional[str] = Field(None, description="")
    repoURL: Optional[str] = Field(None, description="")
    requeueAfterSeconds: Optional[str] = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")
    values: Optional[Dict[str, Any]] = Field(None, description="")

class v1alpha1GnuPGPublicKey(BaseModel):
    fingerprint: Optional[str] = Field(None, description="")
    keyData: Optional[str] = Field(None, description="")
    keyID: Optional[str] = Field(None, description="")
    owner: Optional[str] = Field(None, description="")
    subType: Optional[str] = Field(None, description="")
    trust: Optional[str] = Field(None, description="")

class v1alpha1GnuPGPublicKeyList(BaseModel):
    items: Optional[List[v1alpha1GnuPGPublicKey]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1HealthStatus(BaseModel):
    message: Optional[str] = Field(None, description="")
    status: Optional[str] = Field(None, description="")

class v1alpha1HelmFileParameter(BaseModel):
    name: Optional[str] = Field(None, description="")
    path: Optional[str] = Field(None, description="")

class v1alpha1HelmParameter(BaseModel):
    forceString: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class v1alpha1HostInfo(BaseModel):
    name: Optional[str] = Field(None, description="")
    resourcesInfo: Optional[List[v1alpha1HostResourceInfo]] = Field(None, description="")
    systemInfo: Optional[v1NodeSystemInfo] = Field(None, description="")

class v1alpha1HostResourceInfo(BaseModel):
    capacity: Optional[str] = Field(None, description="")
    requestedByApp: Optional[str] = Field(None, description="")
    requestedByNeighbors: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")

class v1alpha1Info(BaseModel):
    name: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class v1alpha1InfoItem(BaseModel):
    name: Optional[str] = Field(None, description="Name is a human readable title for this piece of information.")
    value: Optional[str] = Field(None, description="Value is human readable content.")

class v1alpha1JWTToken(BaseModel):
    exp: Optional[str] = Field(None, description="")
    iat: Optional[str] = Field(None, description="")
    id: Optional[str] = Field(None, description="")

class v1alpha1JWTTokens(BaseModel):
    items: Optional[List[v1alpha1JWTToken]] = Field(None, description="")

class v1alpha1JsonnetVar(BaseModel):
    code: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class v1alpha1KnownTypeField(BaseModel):
    field: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")

class v1alpha1KustomizeOptions(BaseModel):
    binaryPath: Optional[str] = Field(None, description="")
    buildOptions: Optional[str] = Field(None, description="")

class v1alpha1KustomizeReplica(BaseModel):
    count: Optional[intstrIntOrString] = Field(None, description="")
    name: Optional[str] = Field(None, description="")

class v1alpha1ListGenerator(BaseModel):
    elements: Optional[List[v1JSON]] = Field(None, description="")
    elementsYaml: Optional[str] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")

class v1alpha1ManagedNamespaceMetadata(BaseModel):
    annotations: Optional[Dict[str, Any]] = Field(None, description="")
    labels: Optional[Dict[str, Any]] = Field(None, description="")

class v1alpha1MatrixGenerator(BaseModel):
    generators: Optional[List[v1alpha1ApplicationSetNestedGenerator]] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")

class v1alpha1MergeGenerator(BaseModel):
    generators: Optional[List[v1alpha1ApplicationSetNestedGenerator]] = Field(None, description="")
    mergeKeys: Optional[List[str]] = Field(None, description="")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")

class v1alpha1Operation(BaseModel):
    info: Optional[List[v1alpha1Info]] = Field(None, description="")
    initiatedBy: Optional[v1alpha1OperationInitiator] = Field(None, description="")
    retry: Optional[v1alpha1RetryStrategy] = Field(None, description="")
    sync: Optional[v1alpha1SyncOperation] = Field(None, description="")

class v1alpha1OperationInitiator(BaseModel):
    automated: Optional[bool] = Field(None, description="Automated is set to true if operation was initiated automatically by the application controller.")
    username: Optional[str] = Field(None, description="")

class v1alpha1OperationState(BaseModel):
    finishedAt: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="Message holds any pertinent messages when attempting to perform operation (typically errors).")
    operation: Optional[v1alpha1Operation] = Field(None, description="")
    phase: Optional[str] = Field(None, description="")
    retryCount: Optional[str] = Field(None, description="")
    startedAt: Optional[v1Time] = Field(None, description="")
    syncResult: Optional[v1alpha1SyncOperationResult] = Field(None, description="")

class v1alpha1OrphanedResourceKey(BaseModel):
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")

class v1alpha1OrphanedResourcesMonitorSettings(BaseModel):
    ignore: Optional[List[v1alpha1OrphanedResourceKey]] = Field(None, description="")
    warn: Optional[bool] = Field(None, description="")

class v1alpha1OverrideIgnoreDiff(BaseModel):
    jSONPointers: Optional[List[str]] = Field(None, description="")
    jqPathExpressions: Optional[List[str]] = Field(None, description="")
    managedFieldsManagers: Optional[List[str]] = Field(None, description="")

class v1alpha1PluginConfigMapRef(BaseModel):
    name: Optional[str] = Field(None, description="")

class v1alpha1PluginGenerator(BaseModel):
    configMapRef: Optional[v1alpha1PluginConfigMapRef] = Field(None, description="")
    input: Optional[v1alpha1PluginInput] = Field(None, description="")
    requeueAfterSeconds: Optional[str] = Field(None, description="RequeueAfterSeconds determines how long the ApplicationSet controller will wait before reconciling the ApplicationSet again.")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")
    values: Optional[Dict[str, Any]] = Field(None, description="Values contains key/value pairs which are passed directly as parameters to the template. These values will not be sent as parameters to the plugin.")

class v1alpha1PluginInput(BaseModel):
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters contains the information to pass to the plugin. It is a map. The keys must be strings, and the values can be any type.")

class v1alpha1ProjectRole(BaseModel):
    description: Optional[str] = Field(None, description="")
    groups: Optional[List[str]] = Field(None, description="")
    jwtTokens: Optional[List[v1alpha1JWTToken]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    policies: Optional[List[str]] = Field(None, description="")

class v1alpha1PullRequestGenerator(BaseModel):
    azuredevops: Optional[v1alpha1PullRequestGeneratorAzureDevOps] = Field(None, description="")
    bitbucket: Optional[v1alpha1PullRequestGeneratorBitbucket] = Field(None, description="")
    bitbucketServer: Optional[v1alpha1PullRequestGeneratorBitbucketServer] = Field(None, description="")
    filters: Optional[List[v1alpha1PullRequestGeneratorFilter]] = Field(None, description="Filters for which pull requests should be considered.")
    gitea: Optional[v1alpha1PullRequestGeneratorGitea] = Field(None, description="")
    github: Optional[v1alpha1PullRequestGeneratorGithub] = Field(None, description="")
    gitlab: Optional[v1alpha1PullRequestGeneratorGitLab] = Field(None, description="")
    requeueAfterSeconds: Optional[str] = Field(None, description="Standard parameters.")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")

class v1alpha1PullRequestGeneratorAzureDevOps(BaseModel):
    api: Optional[str] = Field(None, description="The Azure DevOps API URL to talk to. If blank, use https://dev.azure.com/.")
    labels: Optional[List[str]] = Field(None, description="")
    organization: Optional[str] = Field(None, description="Azure DevOps org to scan. Required.")
    project: Optional[str] = Field(None, description="Azure DevOps project name to scan. Required.")
    repo: Optional[str] = Field(None, description="Azure DevOps repo name to scan. Required.")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1PullRequestGeneratorBitbucket(BaseModel):
    api: Optional[str] = Field(None, description="The Bitbucket REST API URL to talk to. If blank, uses https://api.bitbucket.org/2.0.")
    basicAuth: Optional[v1alpha1BasicAuthBitbucketServer] = Field(None, description="")
    bearerToken: Optional[v1alpha1BearerTokenBitbucketCloud] = Field(None, description="")
    owner: Optional[str] = Field(None, description="Workspace to scan. Required.")
    repo: Optional[str] = Field(None, description="Repo name to scan. Required.")

class v1alpha1PullRequestGeneratorBitbucketServer(BaseModel):
    api: Optional[str] = Field(None, description="The Bitbucket REST API URL to talk to e.g. https://bitbucket.org/rest Required.")
    basicAuth: Optional[v1alpha1BasicAuthBitbucketServer] = Field(None, description="")
    project: Optional[str] = Field(None, description="Project to scan. Required.")
    repo: Optional[str] = Field(None, description="Repo name to scan. Required.")

class v1alpha1PullRequestGeneratorFilter(BaseModel):
    branchMatch: Optional[str] = Field(None, description="")
    targetBranchMatch: Optional[str] = Field(None, description="")

class v1alpha1PullRequestGeneratorGitLab(BaseModel):
    api: Optional[str] = Field(None, description="The GitLab API URL to talk to. If blank, uses https://gitlab.com/.")
    insecure: Optional[bool] = Field(None, description="")
    labels: Optional[List[str]] = Field(None, description="")
    project: Optional[str] = Field(None, description="GitLab project to scan. Required.")
    pullRequestState: Optional[str] = Field(None, description="")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1PullRequestGeneratorGitea(BaseModel):
    api: Optional[str] = Field(None, description="")
    insecure: Optional[bool] = Field(None, description="Allow insecure tls, for self-signed certificates; default: false.")
    owner: Optional[str] = Field(None, description="Gitea org or user to scan. Required.")
    repo: Optional[str] = Field(None, description="Gitea repo name to scan. Required.")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1PullRequestGeneratorGithub(BaseModel):
    api: Optional[str] = Field(None, description="The GitHub API URL to talk to. If blank, use https://api.github.com/.")
    appSecretName: Optional[str] = Field(None, description="AppSecretName is a reference to a GitHub App repo-creds secret with permission to access pull requests.")
    labels: Optional[List[str]] = Field(None, description="")
    owner: Optional[str] = Field(None, description="GitHub org or user to scan. Required.")
    repo: Optional[str] = Field(None, description="GitHub repo name to scan. Required.")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1RepoCreds(BaseModel):
    enableOCI: Optional[bool] = Field(None, description="")
    forceHttpBasicAuth: Optional[bool] = Field(None, description="")
    gcpServiceAccountKey: Optional[str] = Field(None, description="")
    githubAppEnterpriseBaseUrl: Optional[str] = Field(None, description="")
    githubAppID: Optional[str] = Field(None, description="")
    githubAppInstallationID: Optional[str] = Field(None, description="")
    githubAppPrivateKey: Optional[str] = Field(None, description="")
    password: Optional[str] = Field(None, description="")
    proxy: Optional[str] = Field(None, description="")
    sshPrivateKey: Optional[str] = Field(None, description="")
    tlsClientCertData: Optional[str] = Field(None, description="")
    tlsClientCertKey: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="Type specifies the type of the repoCreds. Can be either git or helm. git is assumed if empty or absent.")
    url: Optional[str] = Field(None, description="")
    username: Optional[str] = Field(None, description="")

class v1alpha1RepoCredsList(BaseModel):
    items: Optional[List[v1alpha1RepoCreds]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1Repository(BaseModel):
    connectionState: Optional[v1alpha1ConnectionState] = Field(None, description="")
    enableLfs: Optional[bool] = Field(None, description="EnableLFS specifies whether git-lfs support should be enabled for this repo. Only valid for Git repositories.")
    enableOCI: Optional[bool] = Field(None, description="")
    forceHttpBasicAuth: Optional[bool] = Field(None, description="")
    gcpServiceAccountKey: Optional[str] = Field(None, description="")
    githubAppEnterpriseBaseUrl: Optional[str] = Field(None, description="")
    githubAppID: Optional[str] = Field(None, description="")
    githubAppInstallationID: Optional[str] = Field(None, description="")
    githubAppPrivateKey: Optional[str] = Field(None, description="")
    inheritedCreds: Optional[bool] = Field(None, description="")
    insecure: Optional[bool] = Field(None, description="")
    insecureIgnoreHostKey: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    password: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")
    proxy: Optional[str] = Field(None, description="")
    repo: Optional[str] = Field(None, description="")
    sshPrivateKey: Optional[str] = Field(None, description="SSHPrivateKey contains the PEM data for authenticating at the repo server. Only used with Git repos.")
    tlsClientCertData: Optional[str] = Field(None, description="")
    tlsClientCertKey: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="Type specifies the type of the repo. Can be either git or helm. git is assumed if empty or absent.")
    username: Optional[str] = Field(None, description="")

class v1alpha1RepositoryCertificate(BaseModel):
    certData: Optional[str] = Field(None, description="")
    certInfo: Optional[str] = Field(None, description="")
    certSubType: Optional[str] = Field(None, description="")
    certType: Optional[str] = Field(None, description="")
    serverName: Optional[str] = Field(None, description="")

class v1alpha1RepositoryCertificateList(BaseModel):
    items: Optional[List[v1alpha1RepositoryCertificate]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1RepositoryList(BaseModel):
    items: Optional[List[v1alpha1Repository]] = Field(None, description="")
    metadata: Optional[v1ListMeta] = Field(None, description="")

class v1alpha1ResourceAction(BaseModel):
    disabled: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    params: Optional[List[v1alpha1ResourceActionParam]] = Field(None, description="")

class v1alpha1ResourceActionParam(BaseModel):
    default: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    type: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class v1alpha1ResourceDiff(BaseModel):
    diff: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    hook: Optional[bool] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    liveState: Optional[str] = Field(None, description="")
    modified: Optional[bool] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    normalizedLiveState: Optional[str] = Field(None, description="")
    predictedLiveState: Optional[str] = Field(None, description="")
    resourceVersion: Optional[str] = Field(None, description="")
    targetState: Optional[str] = Field(None, description="")

class v1alpha1ResourceIgnoreDifferences(BaseModel):
    group: Optional[str] = Field(None, description="")
    jqPathExpressions: Optional[List[str]] = Field(None, description="")
    jsonPointers: Optional[List[str]] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    managedFieldsManagers: Optional[List[str]] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")

class v1alpha1ResourceNetworkingInfo(BaseModel):
    externalURLs: Optional[List[str]] = Field(None, description="ExternalURLs holds list of URLs which should be available externally. List is populated for ingress resources using rules hostnames.")
    ingress: Optional[List[v1LoadBalancerIngress]] = Field(None, description="")
    labels: Optional[Dict[str, Any]] = Field(None, description="")
    targetLabels: Optional[Dict[str, Any]] = Field(None, description="")
    targetRefs: Optional[List[v1alpha1ResourceRef]] = Field(None, description="")

class v1alpha1ResourceNode(BaseModel):
    createdAt: Optional[v1Time] = Field(None, description="")
    health: Optional[v1alpha1HealthStatus] = Field(None, description="")
    images: Optional[List[str]] = Field(None, description="")
    info: Optional[List[v1alpha1InfoItem]] = Field(None, description="")
    networkingInfo: Optional[v1alpha1ResourceNetworkingInfo] = Field(None, description="")
    parentRefs: Optional[List[v1alpha1ResourceRef]] = Field(None, description="")
    resourceRef: Optional[v1alpha1ResourceRef] = Field(None, description="")
    resourceVersion: Optional[str] = Field(None, description="")

class v1alpha1ResourceOverride(BaseModel):
    actions: Optional[str] = Field(None, description="")
    healthLua: Optional[str] = Field(None, description="")
    ignoreDifferences: Optional[v1alpha1OverrideIgnoreDiff] = Field(None, description="")
    ignoreResourceUpdates: Optional[v1alpha1OverrideIgnoreDiff] = Field(None, description="")
    knownTypeFields: Optional[List[v1alpha1KnownTypeField]] = Field(None, description="")
    useOpenLibs: Optional[bool] = Field(None, description="")

class v1alpha1ResourceRef(BaseModel):
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    uid: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")

class v1alpha1ResourceResult(BaseModel):
    group: Optional[str] = Field(None, description="")
    hookPhase: Optional[str] = Field(None, description="HookPhase contains the state of any operation associated with this resource OR hook This can also contain values for non-hook resources.")
    hookType: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    message: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    status: Optional[str] = Field(None, description="")
    syncPhase: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")

class v1alpha1ResourceStatus(BaseModel):
    group: Optional[str] = Field(None, description="")
    health: Optional[v1alpha1HealthStatus] = Field(None, description="")
    hook: Optional[bool] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    requiresPruning: Optional[bool] = Field(None, description="")
    status: Optional[str] = Field(None, description="")
    syncWave: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")

class v1alpha1RetryStrategy(BaseModel):
    backoff: Optional[v1alpha1Backoff] = Field(None, description="")
    limit: Optional[str] = Field(None, description="Limit is the maximum number of attempts for retrying a failed sync. If set to 0, no retries will be performed.")

class v1alpha1RevisionHistory(BaseModel):
    deployStartedAt: Optional[v1Time] = Field(None, description="")
    deployedAt: Optional[v1Time] = Field(None, description="")
    id: Optional[str] = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    revisions: Optional[List[str]] = Field(None, description="")
    source: Optional[v1alpha1ApplicationSource] = Field(None, description="")
    sources: Optional[List[v1alpha1ApplicationSource]] = Field(None, description="")

class v1alpha1RevisionMetadata(BaseModel):
    author: Optional[str] = Field(None, description="")
    date: Optional[v1Time] = Field(None, description="")
    message: Optional[str] = Field(None, description="Message contains the message associated with the revision, most likely the commit message.")
    signatureInfo: Optional[str] = Field(None, description="SignatureInfo contains a hint on the signer if the revision was signed with GPG, and signature verification is enabled.")
    tags: Optional[List[str]] = Field(None, description="")

class v1alpha1SCMProviderGenerator(BaseModel):
    awsCodeCommit: Optional[v1alpha1SCMProviderGeneratorAWSCodeCommit] = Field(None, description="")
    azureDevOps: Optional[v1alpha1SCMProviderGeneratorAzureDevOps] = Field(None, description="")
    bitbucket: Optional[v1alpha1SCMProviderGeneratorBitbucket] = Field(None, description="")
    bitbucketServer: Optional[v1alpha1SCMProviderGeneratorBitbucketServer] = Field(None, description="")
    cloneProtocol: Optional[str] = Field(None, description="Which protocol to use for the SCM URL. Default is provider-specific but ssh if possible. Not all providers necessarily support all protocols.")
    filters: Optional[List[v1alpha1SCMProviderGeneratorFilter]] = Field(None, description="Filters for which repos should be considered.")
    gitea: Optional[v1alpha1SCMProviderGeneratorGitea] = Field(None, description="")
    github: Optional[v1alpha1SCMProviderGeneratorGithub] = Field(None, description="")
    gitlab: Optional[v1alpha1SCMProviderGeneratorGitlab] = Field(None, description="")
    requeueAfterSeconds: Optional[str] = Field(None, description="Standard parameters.")
    template: Optional[v1alpha1ApplicationSetTemplate] = Field(None, description="")
    values: Optional[Dict[str, Any]] = Field(None, description="")

class v1alpha1SCMProviderGeneratorAWSCodeCommit(BaseModel):
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the default branch.")
    region: Optional[str] = Field(None, description="Region provides the AWS region to discover repos. if not provided, AppSet controller will infer the current region from environment.")
    role: Optional[str] = Field(None, description="Role provides the AWS IAM role to assume, for cross-account repo discovery if not provided, AppSet controller will use its pod/node identity to discover.")
    tagFilters: Optional[List[v1alpha1TagFilter]] = Field(None, description="")

class v1alpha1SCMProviderGeneratorAzureDevOps(BaseModel):
    accessTokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the default branch.")
    api: Optional[str] = Field(None, description="The URL to Azure DevOps. If blank, use https://dev.azure.com.")
    organization: Optional[str] = Field(None, description="Azure Devops organization. Required. E.g. my-organization")
    teamProject: Optional[str] = Field(None, description="Azure Devops team project. Required. E.g my-team.")

class v1alpha1SCMProviderGeneratorBitbucket(BaseModel):
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the main branch.")
    appPasswordRef: Optional[v1alpha1SecretRef] = Field(None, description="")
    owner: Optional[str] = Field(None, description="Bitbucket workspace to scan. Required.")
    user: Optional[str] = Field(None, description="")

class v1alpha1SCMProviderGeneratorBitbucketServer(BaseModel):
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the default branch.")
    api: Optional[str] = Field(None, description="The Bitbucket Server REST API URL to talk to. Required.")
    basicAuth: Optional[v1alpha1BasicAuthBitbucketServer] = Field(None, description="")
    project: Optional[str] = Field(None, description="Project to scan. Required.")

class v1alpha1SCMProviderGeneratorFilter(BaseModel):
    branchMatch: Optional[str] = Field(None, description="A regex which must match the branch name.")
    labelMatch: Optional[str] = Field(None, description="A regex which must match at least one label.")
    pathsDoNotExist: Optional[List[str]] = Field(None, description="An array of paths, all of which must not exist.")
    pathsExist: Optional[List[str]] = Field(None, description="An array of paths, all of which must exist.")
    repositoryMatch: Optional[str] = Field(None, description="A regex for repo names.")

class v1alpha1SCMProviderGeneratorGitea(BaseModel):
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the default branch.")
    api: Optional[str] = Field(None, description="The Gitea URL to talk to. For example https://gitea.mydomain.com/.")
    insecure: Optional[bool] = Field(None, description="")
    owner: Optional[str] = Field(None, description="Gitea organization or user to scan. Required.")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1SCMProviderGeneratorGithub(BaseModel):
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the default branch.")
    api: Optional[str] = Field(None, description="The GitHub API URL to talk to. If blank, use https://api.github.com/.")
    appSecretName: Optional[str] = Field(None, description="AppSecretName is a reference to a GitHub App repo-creds secret.")
    organization: Optional[str] = Field(None, description="GitHub org to scan. Required.")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1SCMProviderGeneratorGitlab(BaseModel):
    allBranches: Optional[bool] = Field(None, description="Scan all branches instead of just the default branch.")
    api: Optional[str] = Field(None, description="The Gitlab API URL to talk to.")
    group: Optional[str] = Field(None, description="Gitlab group to scan. Required.  You can use either the project id (recommended) or the full namespaced path.")
    includeSubgroups: Optional[bool] = Field(None, description="")
    insecure: Optional[bool] = Field(None, description="")
    tokenRef: Optional[v1alpha1SecretRef] = Field(None, description="")

class v1alpha1SecretRef(BaseModel):
    key: Optional[str] = Field(None, description="")
    secretName: Optional[str] = Field(None, description="")

class v1alpha1SignatureKey(BaseModel):
    keyID: Optional[str] = Field(None, description="")

class v1alpha1SyncOperation(BaseModel):
    dryRun: Optional[bool] = Field(None, description="")
    manifests: Optional[List[str]] = Field(None, description="")
    prune: Optional[bool] = Field(None, description="")
    resources: Optional[List[v1alpha1SyncOperationResource]] = Field(None, description="")
    revision: Optional[str] = Field(None, description="Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec.")
    revisions: Optional[List[str]] = Field(None, description="Revisions is the list of revision (Git) or chart version (Helm) which to sync each source in sources field for the application to If omitted, will use the revision specified in app spec.")
    source: Optional[v1alpha1ApplicationSource] = Field(None, description="")
    sources: Optional[List[v1alpha1ApplicationSource]] = Field(None, description="")
    syncOptions: Optional[List[str]] = Field(None, description="")
    syncStrategy: Optional[v1alpha1SyncStrategy] = Field(None, description="")

class v1alpha1SyncOperationResource(BaseModel):
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")

class v1alpha1SyncOperationResult(BaseModel):
    managedNamespaceMetadata: Optional[v1alpha1ManagedNamespaceMetadata] = Field(None, description="")
    resources: Optional[List[v1alpha1ResourceResult]] = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    revisions: Optional[List[str]] = Field(None, description="")
    source: Optional[v1alpha1ApplicationSource] = Field(None, description="")
    sources: Optional[List[v1alpha1ApplicationSource]] = Field(None, description="")

class v1alpha1SyncPolicy(BaseModel):
    automated: Optional[v1alpha1SyncPolicyAutomated] = Field(None, description="")
    managedNamespaceMetadata: Optional[v1alpha1ManagedNamespaceMetadata] = Field(None, description="")
    retry: Optional[v1alpha1RetryStrategy] = Field(None, description="")
    syncOptions: Optional[List[str]] = Field(None, description="")

class v1alpha1SyncPolicyAutomated(BaseModel):
    allowEmpty: Optional[bool] = Field(None, description="")
    prune: Optional[bool] = Field(None, description="")
    selfHeal: Optional[bool] = Field(None, description="")

class v1alpha1SyncStatus(BaseModel):
    comparedTo: Optional[v1alpha1ComparedTo] = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    revisions: Optional[List[str]] = Field(None, description="")
    status: Optional[str] = Field(None, description="")

class v1alpha1SyncStrategy(BaseModel):
    apply: Optional[v1alpha1SyncStrategyApply] = Field(None, description="")
    hook: Optional[v1alpha1SyncStrategyHook] = Field(None, description="")

class v1alpha1SyncStrategyApply(BaseModel):
    force: Optional[bool] = Field(None, description="Force indicates whether or not to supply the --force flag to `kubectl apply`. The --force flag deletes and re-create the resource, when PATCH encounters conflict and has retried for 5 times.")

class v1alpha1SyncStrategyHook(BaseModel):
    syncStrategyApply: Optional[v1alpha1SyncStrategyApply] = Field(None, description="")

class v1alpha1SyncWindow(BaseModel):
    applications: Optional[List[str]] = Field(None, description="")
    clusters: Optional[List[str]] = Field(None, description="")
    duration: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    manualSync: Optional[bool] = Field(None, description="")
    namespaces: Optional[List[str]] = Field(None, description="")
    schedule: Optional[str] = Field(None, description="")
    timeZone: Optional[str] = Field(None, description="")

class v1alpha1TLSClientConfig(BaseModel):
    caData: Optional[str] = Field(None, description="")
    certData: Optional[str] = Field(None, description="")
    insecure: Optional[bool] = Field(None, description="Insecure specifies that the server should be accessed without verifying the TLS certificate. For testing only.")
    keyData: Optional[str] = Field(None, description="")
    serverName: Optional[str] = Field(None, description="ServerName is passed to the server for SNI and is used in the client to check server certificates against. If ServerName is empty, the hostname used to contact the server is used.")

class v1alpha1TagFilter(BaseModel):
    key: Optional[str] = Field(None, description="")
    value: Optional[str] = Field(None, description="")

class versionVersionMessage(BaseModel):
    BuildDate: Optional[str] = Field(None, description="")
    Compiler: Optional[str] = Field(None, description="")
    ExtraBuildInfo: Optional[str] = Field(None, description="")
    GitCommit: Optional[str] = Field(None, description="")
    GitTag: Optional[str] = Field(None, description="")
    GitTreeState: Optional[str] = Field(None, description="")
    GoVersion: Optional[str] = Field(None, description="")
    HelmVersion: Optional[str] = Field(None, description="")
    JsonnetVersion: Optional[str] = Field(None, description="")
    KubectlVersion: Optional[str] = Field(None, description="")
    KustomizeVersion: Optional[str] = Field(None, description="")
    Platform: Optional[str] = Field(None, description="")
    Version: Optional[str] = Field(None, description="")