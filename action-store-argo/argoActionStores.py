from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union
from kubiya import ActionStore
from requests_wrapper import *


class AccountService_ListAccountsInput(BaseModel):
    pass

@action_store.kubiya_action()
def AccountService_ListAccounts(input: AccountService_ListAccountsInput):
    return get_wrapper(endpoint="/api/v1/account", args=input.dict(exclude_none=True))

class AccountService_CanIInput(BaseModel):
    resource: str = Field(None, description="")
    action: str = Field(None, description="")
    subresource: str = Field(None, description="")

@action_store.kubiya_action()
def AccountService_CanI(input: AccountService_CanIInput):
    return get_wrapper(endpoint="/api/v1/account/can-i/{resource}/{action}/{subresource}", args=input.dict(exclude_none=True))

class AccountService_UpdatePasswordInput(BaseModel):
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def AccountService_UpdatePassword(input: AccountService_UpdatePasswordInput):
    return put_wrapper(endpoint="/api/v1/account/password", args=input.dict(exclude_none=True))

class AccountService_GetAccountInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def AccountService_GetAccount(input: AccountService_GetAccountInput):
    return get_wrapper(endpoint="/api/v1/account/{name}", args=input.dict(exclude_none=True))

class AccountService_CreateTokenInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def AccountService_CreateToken(input: AccountService_CreateTokenInput):
    return post_wrapper(endpoint="/api/v1/account/{name}/token", args=input.dict(exclude_none=True))

class AccountService_DeleteTokenInput(BaseModel):
    name: str = Field(None, description="")
    id: str = Field(None, description="")

@action_store.kubiya_action()
def AccountService_DeleteToken(input: AccountService_DeleteTokenInput):
    return delete_wrapper(endpoint="/api/v1/account/{name}/token/{id}", args=input.dict(exclude_none=True))

class ApplicationService_ListInput(BaseModel):
    name: Optional[str] = Field(None, description="the application's name.")
    refresh: Optional[str] = Field(None, description="forces application reconciliation if set to true.")
    projects: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applications.")
    resourceVersion: Optional[str] = Field(None, description="when specified with a watch call, shows changes that occur after that particular version of a resource.")
    selector: Optional[str] = Field(None, description="the selector to restrict returned list to applications only with matched labels.")
    repo: Optional[str] = Field(None, description="the repoURL to restrict returned list applications.")
    appNamespace: Optional[str] = Field(None, description="the application's namespace.")
    project: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applications (legacy name for backwards-compatibility).")

@action_store.kubiya_action()
def ApplicationService_List(input: ApplicationService_ListInput):
    return get_wrapper(endpoint="/api/v1/applications", args=input.dict(exclude_none=True))

class ApplicationService_CreateInput(BaseModel):
    body: Any = Field(None, description="")
    upsert: Optional[bool] = Field(None, description="")
    validate: Optional[bool] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_Create(input: ApplicationService_CreateInput):
    return post_wrapper(endpoint="/api/v1/applications", args=input.dict(exclude_none=True))

class ApplicationService_GetManifestsWithFilesInput(BaseModel):
    body: Any = Field(None, description=" (streaming inputs)")

@action_store.kubiya_action()
def ApplicationService_GetManifestsWithFiles(input: ApplicationService_GetManifestsWithFilesInput):
    return post_wrapper(endpoint="/api/v1/applications/manifestsWithFiles", args=input.dict(exclude_none=True))

class ApplicationService_UpdateInput(BaseModel):
    application_metadata_name: str = Field(None, description="Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client " "to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and " "configuration definition.")
    body: Any = Field(None, description="")
    validate: Optional[bool] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_Update(input: ApplicationService_UpdateInput):
    return put_wrapper(endpoint="/api/v1/applications/{application.metadata.name}", args=input.dict(exclude_none=True))

class ApplicationService_ManagedResourcesInput(BaseModel):
    applicationName: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_ManagedResources(input: ApplicationService_ManagedResourcesInput):
    return get_wrapper(endpoint="/api/v1/applications/{applicationName}/managed-resources", args=input.dict(exclude_none=True))

class ApplicationService_ResourceTreeInput(BaseModel):
    applicationName: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_ResourceTree(input: ApplicationService_ResourceTreeInput):
    return get_wrapper(endpoint="/api/v1/applications/{applicationName}/resource-tree", args=input.dict(exclude_none=True))

class ApplicationService_GetInput(BaseModel):
    name: str = Field(None, description="the application's name")
    refresh: Optional[str] = Field(None, description="forces application reconciliation if set to true.")
    projects: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applications.")
    resourceVersion: Optional[str] = Field(None, description="when specified with a watch call, shows changes that occur after that particular version of a resource.")
    selector: Optional[str] = Field(None, description="the selector to restrict returned list to applications only with matched labels.")
    repo: Optional[str] = Field(None, description="the repoURL to restrict returned list applications.")
    appNamespace: Optional[str] = Field(None, description="the application's namespace.")
    project: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applications (legacy name for backwards-compatibility).")

@action_store.kubiya_action()
def ApplicationService_Get(input: ApplicationService_GetInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}", args=input.dict(exclude_none=True))

class ApplicationService_DeleteInput(BaseModel):
    name: str = Field(None, description="")
    cascade: Optional[bool] = Field(None, description="")
    propagationPolicy: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_Delete(input: ApplicationService_DeleteInput):
    return delete_wrapper(endpoint="/api/v1/applications/{name}", args=input.dict(exclude_none=True))

class ApplicationService_PatchInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_Patch(input: ApplicationService_PatchInput):
    return patch_wrapper(endpoint="/api/v1/applications/{name}", args=input.dict(exclude_none=True))

class ApplicationService_ListResourceEventsInput(BaseModel):
    name: str = Field(None, description="")
    resourceNamespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    resourceUID: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_ListResourceEvents(input: ApplicationService_ListResourceEventsInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/events", args=input.dict(exclude_none=True))

class ApplicationService_ListLinksInput(BaseModel):
    name: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_ListLinks(input: ApplicationService_ListLinksInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/links", args=input.dict(exclude_none=True))

class ApplicationService_PodLogs2Input(BaseModel):
    name: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    podName: Optional[str] = Field(None, description="")
    container: Optional[str] = Field(None, description="")
    sinceSeconds: Optional[str] = Field(None, description="")
    sinceTime_seconds: Optional[str] = Field(
        None,
        description="Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive."
    )
    sinceTime_nanos: Optional[int] = Field(
        None,
        description="Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context."
    )
    tailLines: Optional[str] = Field(None, description="")
    follow: Optional[bool] = Field(None, description="")
    untilTime: Optional[str] = Field(None, description="")
    filter: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    previous: Optional[bool] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_PodLogs2(input: ApplicationService_PodLogs2Input):
    return get_wrapper(endpoint="/api/v1/applications/{name}/logs", args=input.dict(exclude_none=True))

class ApplicationService_GetManifestsInput(BaseModel):
    name: str = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_GetManifests(input: ApplicationService_GetManifestsInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/manifests", args=input.dict(exclude_none=True))

class ApplicationService_TerminateOperationInput(BaseModel):
    name: str = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_TerminateOperation(input: ApplicationService_TerminateOperationInput):
    return delete_wrapper(endpoint="/api/v1/applications/{name}/operation", args=input.dict(exclude_none=True))

class ApplicationService_PodLogsInput(BaseModel):
    name: str = Field(None, description="")
    podName: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    container: Optional[str] = Field(None, description="")
    sinceSeconds: Optional[str] = Field(
        None,
        description=""
    )

    sinceTime_seconds: Optional[str] = Field(
        None,
        description="Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive."
    )

    sinceTime_nanos: Optional[int] = Field(
        None,
        description="Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context."
    )
    tailLines: Optional[str] = Field(None, description="")
    follow: Optional[bool] = Field(None, description="")
    untilTime: Optional[str] = Field(None, description="")
    filter: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    previous: Optional[bool] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_PodLogs(input: ApplicationService_PodLogsInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/pods/{podName}/logs", args=input.dict(exclude_none=True))

class ApplicationService_GetResourceInput(BaseModel):
    name: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_GetResource(input: ApplicationService_GetResourceInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/resource", args=input.dict(exclude_none=True))

class ApplicationService_PatchResourceInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    patchType: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_PatchResource(input: ApplicationService_PatchResourceInput):
    return post_wrapper(endpoint="/api/v1/applications/{name}/resource", args=input.dict(exclude_none=True))

class ApplicationService_DeleteResourceInput(BaseModel):
    name: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    force: Optional[bool] = Field(None, description="")
    orphan: Optional[bool] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_DeleteResource(input: ApplicationService_DeleteResourceInput):
    return delete_wrapper(endpoint="/api/v1/applications/{name}/resource", args=input.dict(exclude_none=True))

class ApplicationService_ListResourceActionsInput(BaseModel):
    name: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_ListResourceActions(input: ApplicationService_ListResourceActionsInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/resource/actions", args=input.dict(exclude_none=True))

class ApplicationService_RunResourceActionInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_RunResourceAction(input: ApplicationService_RunResourceActionInput):
    return post_wrapper(endpoint="/api/v1/applications/{name}/resource/actions", args=input.dict(exclude_none=True))

class ApplicationService_ListResourceLinksInput(BaseModel):
    name: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    resourceName: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_ListResourceLinks(input: ApplicationService_ListResourceLinksInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/resource/links", args=input.dict(exclude_none=True))

class ApplicationService_RevisionChartDetailsInput(BaseModel):
    name: str = Field(None, description="the application's name")
    revision: str = Field(None, description="the revision of the app")
    appNamespace: Optional[str] = Field(None, description="the application's namespace.")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_RevisionChartDetails(input: ApplicationService_RevisionChartDetailsInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/revisions/{revision}/chartdetails", args=input.dict(exclude_none=True))

class ApplicationService_RevisionMetadataInput(BaseModel):
    name: str = Field(None, description="the application's name")
    revision: str = Field(None, description="the revision of the app")
    appNamespace: Optional[str] = Field(None, description="the application's namespace.")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_RevisionMetadata(input: ApplicationService_RevisionMetadataInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/revisions/{revision}/metadata", args=input.dict(exclude_none=True))

class ApplicationService_RollbackInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_Rollback(input: ApplicationService_RollbackInput):
    return post_wrapper(endpoint="/api/v1/applications/{name}/rollback", args=input.dict(exclude_none=True))

class ApplicationService_UpdateSpecInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")
    validate: Optional[bool] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_UpdateSpec(input: ApplicationService_UpdateSpecInput):
    return put_wrapper(endpoint="/api/v1/applications/{name}/spec", args=input.dict(exclude_none=True))

class ApplicationService_SyncInput(BaseModel):
    name: str = Field(None, description="")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_Sync(input: ApplicationService_SyncInput):
    return post_wrapper(endpoint="/api/v1/applications/{name}/sync", args=input.dict(exclude_none=True))

class ApplicationService_GetApplicationSyncWindowsInput(BaseModel):
    name: str = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_GetApplicationSyncWindows(input: ApplicationService_GetApplicationSyncWindowsInput):
    return get_wrapper(endpoint="/api/v1/applications/{name}/syncwindows", args=input.dict(exclude_none=True))

class ApplicationSetService_ListInput(BaseModel):
    projects: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applicationsets.")
    selector: Optional[str] = Field(None, description="the selector to restrict returned list to applications only with matched labels.")
    appsetNamespace: Optional[str] = Field(None, description="The application set namespace. Default empty is argocd control plane namespace.")

@action_store.kubiya_action()
def ApplicationSetService_List(input: ApplicationSetService_ListInput):
    return get_wrapper(endpoint="/api/v1/applicationsets", args=input.dict(exclude_none=True))

class ApplicationSetService_CreateInput(BaseModel):
    body: Any = Field(None, description="")
    upsert: Optional[bool] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationSetService_Create(input: ApplicationSetService_CreateInput):
    return post_wrapper(endpoint="/api/v1/applicationsets", args=input.dict(exclude_none=True))

class ApplicationSetService_GetInput(BaseModel):
    name: str = Field(None, description="the applicationsets's name")
    appsetNamespace: Optional[str] = Field(None, description="The application set namespace. Default empty is argocd control plane namespace.")

@action_store.kubiya_action()
def ApplicationSetService_Get(input: ApplicationSetService_GetInput):
    return get_wrapper(endpoint="/api/v1/applicationsets/{name}", args=input.dict(exclude_none=True))

class ApplicationSetService_DeleteInput(BaseModel):
    name: str = Field(None, description="")
    appsetNamespace: Optional[str] = Field(None, description="The application set namespace. Default empty is argocd control plane namespace.")

@action_store.kubiya_action()
def ApplicationSetService_Delete(input: ApplicationSetService_DeleteInput):
    return delete_wrapper(endpoint="/api/v1/applicationsets/{name}", args=input.dict(exclude_none=True))

class CertificateService_ListCertificatesInput(BaseModel):
    hostNamePattern: Optional[str] = Field(None, description="A file-glob pattern (not regular expression) the host name has to match.")
    certType: Optional[str] = Field(None, description="The type of the certificate to match (ssh or https).")
    certSubType: Optional[str] = Field(None, description="The sub type of the certificate to match (protocol dependent, usually only used for ssh certs).")

@action_store.kubiya_action()
def CertificateService_ListCertificates(input: CertificateService_ListCertificatesInput):
    return get_wrapper(endpoint="/api/v1/certificates", args=input.dict(exclude_none=True))

class CertificateService_CreateCertificateInput(BaseModel):
    body: Any = Field(None, description="List of certificates to be created")
    upsert: Optional[bool] = Field(None, description="Whether to upsert already existing certificates.")

@action_store.kubiya_action()
def CertificateService_CreateCertificate(input: CertificateService_CreateCertificateInput):
    return post_wrapper(endpoint="/api/v1/certificates", args=input.dict(exclude_none=True))

class CertificateService_DeleteCertificateInput(BaseModel):
    hostNamePattern: Optional[str] = Field(None, description="A file-glob pattern (not regular expression) the host name has to match.")
    certType: Optional[str] = Field(None, description="The type of the certificate to match (ssh or https).")
    certSubType: Optional[str] = Field(None, description="The sub type of the certificate to match (protocol dependent, usually only used for ssh certs).")

@action_store.kubiya_action()
def CertificateService_DeleteCertificate(input: CertificateService_DeleteCertificateInput):
    return delete_wrapper(endpoint="/api/v1/certificates", args=input.dict(exclude_none=True))

class ClusterService_ListInput(BaseModel):
    server: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    id.type: Optional[str] = Field(None, description="type is the type of the specified cluster identifier ( server - default, name ).")
    id.value: Optional[str] = Field(None, description="value holds the cluster server URL or cluster name.")

@action_store.kubiya_action()
def ClusterService_List(input: ClusterService_ListInput):
    return get_wrapper(endpoint="/api/v1/clusters", args=input.dict(exclude_none=True))

class ClusterService_CreateInput(BaseModel):
    body: Any = Field(None, description="")
    upsert: Optional[bool] = Field(None, description="")

@action_store.kubiya_action()
def ClusterService_Create(input: ClusterService_CreateInput):
    return post_wrapper(endpoint="/api/v1/clusters", args=input.dict(exclude_none=True))

class ClusterService_GetInput(BaseModel):
    id.value: str = Field(None, description="value holds the cluster server URL or cluster name")
    server: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    id.type: Optional[str] = Field(None, description="type is the type of the specified cluster identifier ( server - default, name ).")

@action_store.kubiya_action()
def ClusterService_Get(input: ClusterService_GetInput):
    return get_wrapper(endpoint="/api/v1/clusters/{id.value}", args=input.dict(exclude_none=True))

class ClusterService_UpdateInput(BaseModel):
    id.value: str = Field(None, description="value holds the cluster server URL or cluster name")
    body: Any = Field(None, description="")
    updatedFields: Optional[List[Any]] = Field(None, description="")
    id.type: Optional[str] = Field(None, description="type is the type of the specified cluster identifier ( server - default, name ).")

@action_store.kubiya_action()
def ClusterService_Update(input: ClusterService_UpdateInput):
    return put_wrapper(endpoint="/api/v1/clusters/{id.value}", args=input.dict(exclude_none=True))

class ClusterService_DeleteInput(BaseModel):
    id.value: str = Field(None, description="value holds the cluster server URL or cluster name")
    server: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    id.type: Optional[str] = Field(None, description="type is the type of the specified cluster identifier ( server - default, name ).")

@action_store.kubiya_action()
def ClusterService_Delete(input: ClusterService_DeleteInput):
    return delete_wrapper(endpoint="/api/v1/clusters/{id.value}", args=input.dict(exclude_none=True))

class ClusterService_InvalidateCacheInput(BaseModel):
    id.value: str = Field(None, description="value holds the cluster server URL or cluster name")

@action_store.kubiya_action()
def ClusterService_InvalidateCache(input: ClusterService_InvalidateCacheInput):
    return post_wrapper(endpoint="/api/v1/clusters/{id.value}/invalidate-cache", args=input.dict(exclude_none=True))

class ClusterService_RotateAuthInput(BaseModel):
    id.value: str = Field(None, description="value holds the cluster server URL or cluster name")

@action_store.kubiya_action()
def ClusterService_RotateAuth(input: ClusterService_RotateAuthInput):
    return post_wrapper(endpoint="/api/v1/clusters/{id.value}/rotate-auth", args=input.dict(exclude_none=True))

class GPGKeyService_ListInput(BaseModel):
    keyID: Optional[str] = Field(None, description="The GPG key ID to query for.")

@action_store.kubiya_action()
def GPGKeyService_List(input: GPGKeyService_ListInput):
    return get_wrapper(endpoint="/api/v1/gpgkeys", args=input.dict(exclude_none=True))

class GPGKeyService_CreateInput(BaseModel):
    body: Any = Field(None, description="Raw key data of the GPG key(s) to create")
    upsert: Optional[bool] = Field(None, description="Whether to upsert already existing public keys.")

@action_store.kubiya_action()
def GPGKeyService_Create(input: GPGKeyService_CreateInput):
    return post_wrapper(endpoint="/api/v1/gpgkeys", args=input.dict(exclude_none=True))

class GPGKeyService_DeleteInput(BaseModel):
    keyID: Optional[str] = Field(None, description="The GPG key ID to query for.")

@action_store.kubiya_action()
def GPGKeyService_Delete(input: GPGKeyService_DeleteInput):
    return delete_wrapper(endpoint="/api/v1/gpgkeys", args=input.dict(exclude_none=True))

class GPGKeyService_GetInput(BaseModel):
    keyID: str = Field(None, description="The GPG key ID to query for")

@action_store.kubiya_action()
def GPGKeyService_Get(input: GPGKeyService_GetInput):
    return get_wrapper(endpoint="/api/v1/gpgkeys/{keyID}", args=input.dict(exclude_none=True))

class NotificationService_ListServicesInput(BaseModel):
    pass

@action_store.kubiya_action()
def NotificationService_ListServices(input: NotificationService_ListServicesInput):
    return get_wrapper(endpoint="/api/v1/notifications/services", args=input.dict(exclude_none=True))

class NotificationService_ListTemplatesInput(BaseModel):
    pass

@action_store.kubiya_action()
def NotificationService_ListTemplates(input: NotificationService_ListTemplatesInput):
    return get_wrapper(endpoint="/api/v1/notifications/templates", args=input.dict(exclude_none=True))

class NotificationService_ListTriggersInput(BaseModel):
    pass

@action_store.kubiya_action()
def NotificationService_ListTriggers(input: NotificationService_ListTriggersInput):
    return get_wrapper(endpoint="/api/v1/notifications/triggers", args=input.dict(exclude_none=True))

class ProjectService_ListInput(BaseModel):
    name: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_List(input: ProjectService_ListInput):
    return get_wrapper(endpoint="/api/v1/projects", args=input.dict(exclude_none=True))

class ProjectService_CreateInput(BaseModel):
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_Create(input: ProjectService_CreateInput):
    return post_wrapper(endpoint="/api/v1/projects", args=input.dict(exclude_none=True))

class ProjectService_GetInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_Get(input: ProjectService_GetInput):
    return get_wrapper(endpoint="/api/v1/projects/{name}", args=input.dict(exclude_none=True))

class ProjectService_DeleteInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_Delete(input: ProjectService_DeleteInput):
    return delete_wrapper(endpoint="/api/v1/projects/{name}", args=input.dict(exclude_none=True))

class ProjectService_GetDetailedProjectInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_GetDetailedProject(input: ProjectService_GetDetailedProjectInput):
    return get_wrapper(endpoint="/api/v1/projects/{name}/detailed", args=input.dict(exclude_none=True))

class ProjectService_ListEventsInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_ListEvents(input: ProjectService_ListEventsInput):
    return get_wrapper(endpoint="/api/v1/projects/{name}/events", args=input.dict(exclude_none=True))

class ProjectService_GetGlobalProjectsInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_GetGlobalProjects(input: ProjectService_GetGlobalProjectsInput):
    return get_wrapper(endpoint="/api/v1/projects/{name}/globalprojects", args=input.dict(exclude_none=True))

class ProjectService_ListLinksInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_ListLinks(input: ProjectService_ListLinksInput):
    return get_wrapper(endpoint="/api/v1/projects/{name}/links", args=input.dict(exclude_none=True))

class ProjectService_GetSyncWindowsStateInput(BaseModel):
    name: str = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_GetSyncWindowsState(input: ProjectService_GetSyncWindowsStateInput):
    return get_wrapper(endpoint="/api/v1/projects/{name}/syncwindows", args=input.dict(exclude_none=True))

class ProjectService_UpdateInput(BaseModel):
    project_metadata_name: str = Field(
        None,
        description="Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional"
    )

    body: Any = Field(
        None,
        description=""
    )

@action_store.kubiya_action()
def ProjectService_Update(input: ProjectService_UpdateInput):
    return put_wrapper(endpoint="/api/v1/projects/{project.metadata.name}", args=input.dict(exclude_none=True))

class ProjectService_CreateTokenInput(BaseModel):
    project: str = Field(None, description="")
    role: str = Field(None, description="")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_CreateToken(input: ProjectService_CreateTokenInput):
    return post_wrapper(endpoint="/api/v1/projects/{project}/roles/{role}/token", args=input.dict(exclude_none=True))

class ProjectService_DeleteTokenInput(BaseModel):
    project: str = Field(None, description="")
    role: str = Field(None, description="")
    iat: str = Field(None, description="")
    id: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ProjectService_DeleteToken(input: ProjectService_DeleteTokenInput):
    return delete_wrapper(endpoint="/api/v1/projects/{project}/roles/{role}/token/{iat}", args=input.dict(exclude_none=True))

class RepoCredsService_ListRepositoryCredentialsInput(BaseModel):
    url: Optional[str] = Field(None, description="Repo URL for query.")

@action_store.kubiya_action()
def RepoCredsService_ListRepositoryCredentials(input: RepoCredsService_ListRepositoryCredentialsInput):
    return get_wrapper(endpoint="/api/v1/repocreds", args=input.dict(exclude_none=True))

class RepoCredsService_CreateRepositoryCredentialsInput(BaseModel):
    body: Any = Field(None, description="Repository definition")
    upsert: Optional[bool] = Field(None, description="Whether to create in upsert mode.")

@action_store.kubiya_action()
def RepoCredsService_CreateRepositoryCredentials(input: RepoCredsService_CreateRepositoryCredentialsInput):
    return post_wrapper(endpoint="/api/v1/repocreds", args=input.dict(exclude_none=True))

class RepoCredsService_UpdateRepositoryCredentialsInput(BaseModel):
    creds_url: str = Field(None, description="URL is the URL that this credentials matches to")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def RepoCredsService_UpdateRepositoryCredentials(input: RepoCredsService_UpdateRepositoryCredentialsInput):
    return put_wrapper(endpoint="/api/v1/repocreds/{creds.url}", args=input.dict(exclude_none=True))

class RepoCredsService_DeleteRepositoryCredentialsInput(BaseModel):
    url: str = Field(None, description="")

@action_store.kubiya_action()
def RepoCredsService_DeleteRepositoryCredentials(input: RepoCredsService_DeleteRepositoryCredentialsInput):
    return delete_wrapper(endpoint="/api/v1/repocreds/{url}", args=input.dict(exclude_none=True))

class RepositoryService_ListRepositoriesInput(BaseModel):
    repo: Optional[str] = Field(None, description="Repo URL for query.")
    forceRefresh: Optional[bool] = Field(None, description="Whether to force a cache refresh on repo's connection state.")

@action_store.kubiya_action()
def RepositoryService_ListRepositories(input: RepositoryService_ListRepositoriesInput):
    return get_wrapper(endpoint="/api/v1/repositories", args=input.dict(exclude_none=True))

class RepositoryService_CreateRepositoryInput(BaseModel):
    body: Any = Field(None, description="Repository definition")
    upsert: Optional[bool] = Field(None, description="Whether to create in upsert mode.")
    credsOnly: Optional[bool] = Field(None, description="Whether to operate on credential set instead of repository.")

@action_store.kubiya_action()
def RepositoryService_CreateRepository(input: RepositoryService_CreateRepositoryInput):
    return post_wrapper(endpoint="/api/v1/repositories", args=input.dict(exclude_none=True))

class RepositoryService_UpdateRepositoryInput(BaseModel):
    repo_repo: str = Field(None, description="Repo contains the URL to the remote repository")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def RepositoryService_UpdateRepository(input: RepositoryService_UpdateRepositoryInput):
    return put_wrapper(endpoint="/api/v1/repositories/{repo.repo}", args=input.dict(exclude_none=True))

class RepositoryService_GetInput(BaseModel):
    repo: str = Field(None, description="Repo URL for query")
    forceRefresh: Optional[bool] = Field(None, description="Whether to force a cache refresh on repo's connection state.")

@action_store.kubiya_action()
def RepositoryService_Get(input: RepositoryService_GetInput):
    return get_wrapper(endpoint="/api/v1/repositories/{repo}", args=input.dict(exclude_none=True))

class RepositoryService_DeleteRepositoryInput(BaseModel):
    repo: str = Field(None, description="Repo URL for query")
    forceRefresh: Optional[bool] = Field(None, description="Whether to force a cache refresh on repo's connection state.")

@action_store.kubiya_action()
def RepositoryService_DeleteRepository(input: RepositoryService_DeleteRepositoryInput):
    return delete_wrapper(endpoint="/api/v1/repositories/{repo}", args=input.dict(exclude_none=True))

class RepositoryService_ListAppsInput(BaseModel):
    repo: str = Field(None, description="")
    revision: Optional[str] = Field(None, description="")
    appName: Optional[str] = Field(None, description="")
    appProject: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def RepositoryService_ListApps(input: RepositoryService_ListAppsInput):
    return get_wrapper(endpoint="/api/v1/repositories/{repo}/apps", args=input.dict(exclude_none=True))

class RepositoryService_GetHelmChartsInput(BaseModel):
    repo: str = Field(None, description="Repo URL for query")
    forceRefresh: Optional[bool] = Field(None, description="Whether to force a cache refresh on repo's connection state.")

@action_store.kubiya_action()
def RepositoryService_GetHelmCharts(input: RepositoryService_GetHelmChartsInput):
    return get_wrapper(endpoint="/api/v1/repositories/{repo}/helmcharts", args=input.dict(exclude_none=True))

class RepositoryService_ListRefsInput(BaseModel):
    repo: str = Field(None, description="Repo URL for query")
    forceRefresh: Optional[bool] = Field(None, description="Whether to force a cache refresh on repo's connection state.")

@action_store.kubiya_action()
def RepositoryService_ListRefs(input: RepositoryService_ListRefsInput):
    return get_wrapper(endpoint="/api/v1/repositories/{repo}/refs", args=input.dict(exclude_none=True))

class RepositoryService_ValidateAccessInput(BaseModel):
    repo: str = Field(None, description="The URL to the repo")
    body: Any = Field(None, description="The URL to the repo")
    username: Optional[str] = Field(None, description="Username for accessing repo.")
    password: Optional[str] = Field(None, description="Password for accessing repo.")
    sshPrivateKey: Optional[str] = Field(None, description="Private key data for accessing SSH repository.")
    insecure: Optional[bool] = Field(None, description="Whether to skip certificate or host key validation.")
    tlsClientCertData: Optional[str] = Field(None, description="TLS client cert data for accessing HTTPS repository.")
    tlsClientCertKey: Optional[str] = Field(None, description="TLS client cert key for accessing HTTPS repository.")
    type: Optional[str] = Field(None, description="The type of the repo.")
    name: Optional[str] = Field(None, description="The name of the repo.")
    enableOci: Optional[bool] = Field(None, description="Whether helm-oci support should be enabled for this repo.")
    githubAppPrivateKey: Optional[str] = Field(None, description="Github App Private Key PEM data.")
    githubAppID: Optional[str] = Field(None, description="Github App ID of the app used to access the repo.")
    githubAppInstallationID: Optional[str] = Field(None, description="Github App Installation ID of the installed GitHub App.")
    githubAppEnterpriseBaseUrl: Optional[str] = Field(None, description="Github App Enterprise base url if empty will default to https://api.github.com.")
    proxy: Optional[str] = Field(None, description="HTTP/HTTPS proxy to access the repository.")
    project: Optional[str] = Field(None, description="Reference between project and repository that allow you automatically to be added as item inside SourceRepos project ent"
"ity.")
    gcpServiceAccountKey: Optional[str] = Field(None, description="Google Cloud Platform service account key.")
    forceHttpBasicAuth: Optional[bool] = Field(None, description="Whether to force HTTP basic auth.")

@action_store.kubiya_action()
def RepositoryService_ValidateAccess(input: RepositoryService_ValidateAccessInput):
    return post_wrapper(endpoint="/api/v1/repositories/{repo}/validate", args=input.dict(exclude_none=True))

class RepositoryService_GetAppDetailsInput(BaseModel):
    source_repoURL: str = Field(None, description="RepoURL is the URL to the repository (Git or Helm) that contains the application manifests")
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def RepositoryService_GetAppDetails(input: RepositoryService_GetAppDetailsInput):
    return post_wrapper(endpoint="/api/v1/repositories/{source.repoURL}/appdetails", args=input.dict(exclude_none=True))

class SessionService_CreateInput(BaseModel):
    body: Any = Field(None, description="")

@action_store.kubiya_action()
def SessionService_Create(input: SessionService_CreateInput):
    return post_wrapper(endpoint="/api/v1/session", args=input.dict(exclude_none=True))

class SessionService_DeleteInput(BaseModel):
    pass

@action_store.kubiya_action()
def SessionService_Delete(input: SessionService_DeleteInput):
    return delete_wrapper(endpoint="/api/v1/session", args=input.dict(exclude_none=True))

class SessionService_GetUserInfoInput(BaseModel):
    pass

@action_store.kubiya_action()
def SessionService_GetUserInfo(input: SessionService_GetUserInfoInput):
    return get_wrapper(endpoint="/api/v1/session/userinfo", args=input.dict(exclude_none=True))

class SettingsService_GetInput(BaseModel):
    pass

@action_store.kubiya_action()
def SettingsService_Get(input: SettingsService_GetInput):
    return get_wrapper(endpoint="/api/v1/settings", args=input.dict(exclude_none=True))

class SettingsService_GetPluginsInput(BaseModel):
    pass

@action_store.kubiya_action()
def SettingsService_GetPlugins(input: SettingsService_GetPluginsInput):
    return get_wrapper(endpoint="/api/v1/settings/plugins", args=input.dict(exclude_none=True))

class ApplicationService_WatchInput(BaseModel):
    name: Optional[str] = Field(None, description="the application's name.")
    refresh: Optional[str] = Field(None, description="forces application reconciliation if set to true.")
    projects: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applications.")
    resourceVersion: Optional[str] = Field(None, description="when specified with a watch call, shows changes that occur after that particular version of a resource.")
    selector: Optional[str] = Field(None, description="the selector to restrict returned list to applications only with matched labels.")
    repo: Optional[str] = Field(None, description="the repoURL to restrict returned list applications.")
    appNamespace: Optional[str] = Field(None, description="the application's namespace.")
    project: Optional[List[Any]] = Field(None, description="the project names to restrict returned list applications (legacy name for backwards-compatibility).")

@action_store.kubiya_action()
def ApplicationService_Watch(input: ApplicationService_WatchInput):
    return get_wrapper(endpoint="/api/v1/stream/applications", args=input.dict(exclude_none=True))

class ApplicationService_WatchResourceTreeInput(BaseModel):
    applicationName: str = Field(None, description="")
    namespace: Optional[str] = Field(None, description="")
    name: Optional[str] = Field(None, description="")
    version: Optional[str] = Field(None, description="")
    group: Optional[str] = Field(None, description="")
    kind: Optional[str] = Field(None, description="")
    appNamespace: Optional[str] = Field(None, description="")
    project: Optional[str] = Field(None, description="")

@action_store.kubiya_action()
def ApplicationService_WatchResourceTree(input: ApplicationService_WatchResourceTreeInput):
    return get_wrapper(endpoint="/api/v1/stream/applications/{applicationName}/resource-tree", args=input.dict(exclude_none=True))

class VersionService_VersionInput(BaseModel):
    pass

@action_store.kubiya_action()
def VersionService_Version(input: VersionService_VersionInput):
    return get_wrapper(endpoint="/api/version", args=input.dict(exclude_none=True))