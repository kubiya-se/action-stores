from pydantic import BaseModel
from typing import Optional, List

class ListRepoArtifactsParams(BaseModel):
    owner: str
    repo: str

class GetArtifactParams(BaseModel):
    owner: str
    repo: str
    artifact_id: int

class DeleteArtifactParams(BaseModel):
    owner: str
    repo: str
    artifact_id: int

class DownloadArtifactParams(BaseModel):
    owner: str
    repo: str
    artifact_id: int
    archive_format: str

class ListWorkflowRunArtifactsParams(BaseModel):
    owner: str
    repo: str
    run_id: int

class ListReposWithCacheUsageInOrgParams(BaseModel):
    org: str

class GetRepoCacheUsageParams(BaseModel):
    owner: str
    repo: str

class ListCachesInRepoParams(BaseModel):
    owner: str
    repo: str

class DeleteCachesByKeyParams(BaseModel):
    owner: str
    repo: str
    key: str

class DeleteCachesByIdParams(BaseModel):
    owner: str
    repo: str
    cache_id: str

class GetCustomizationTemplateForOIDCSubjectClaimOrgParams(BaseModel):
    org: str

class SetCustomizationTemplateForOIDCSubjectClaimOrgParams(BaseModel):
    org: str
    include_claim_keys: List[str]

class GetCustomizationTemplateForOIDCSubjectClaimRepoParams(BaseModel):
    owner: str
    repo: str

class SetCustomizationTemplateForOIDCSubjectClaimRepoParams(BaseModel):
    owner: str
    repo: str
    use_default: bool
    include_claim_keys: Optional[List[str]]

class GetOrgsActionsPermissionsParams(BaseModel):
    org: str

class SetOrgsActionsPermissionsParams(BaseModel):
    org: str
    enabled_repositories: str
    allowed_actions: str

class ListSelectedReposEnabledForActionsByOrgParams(BaseModel):
    org: str

class SetReposEnabledForActionsByOrgParams(BaseModel):
    org: str
    selected_repository_ids: List[int]

class EnableRepoInOrgForActionsParams(BaseModel):
    org: str
    repository_id: int

class DisableRepoInOrgForActionsParams(BaseModel):
    org: str
    repository_id: int

class GetAllowedActionsByOrgParams(BaseModel):
    org: str

class SetAllowedActionsByOrgParams(BaseModel):
    org: str
    github_owned_allowed: Optional[bool]
    verified_allowed: Optional[bool]
    patterns_allowed: Optional[List[str]]

class GetOrgDefaultWorkflowPermissionsParams(BaseModel):
    org: str

class SetOrgDefaultWorkflowPermissionsParams(BaseModel):
    org: str
    default_workflow_permissions: Optional[str]
    can_approve_pull_request_reviews: Optional[bool]

class GetRepoActionsPermissionsParams(BaseModel):
    owner: str
    repo: str

class SetRepoActionsPermissionsParams(BaseModel):
    owner: str
    repo: str
    enabled: bool
    allowed_actions: Optional[str]

class GetAccessForExternalWorkflowsByRepoParams(BaseModel):
    owner: str
    repo: str

class SetAccessForExternalWorkflowsByRepoParams(BaseModel):
    owner: str
    repo: str
    access_level: str

class GetAllowedActionsByRepoParams(BaseModel):
    owner: str
    repo: str

class SetAllowedActionsByRepoParams(BaseModel):
    owner: str
    repo: str
    github_owned_allowed: Optional[bool]
    verified_allowed: Optional[bool]
    patterns_allowed: Optional[List[str]]

class GetRepoDefaultWorkflowPermissionsParams(BaseModel):
    owner: str
    repo: str

class SetRepoDefaultWorkflowPermissionsParams(BaseModel):
    owner: str
    repo: str
    default_workflow_permissions: Optional[str]
    can_approve_pull_request_reviews: Optional[bool]

class ListOrgSecretsParams(BaseModel):
    org: str

class GetOrgPublicKeyParams(BaseModel):
    org: str

class GetOrgSecretParams(BaseModel):
    org: str
    secret_name: str

class CreateUpdateOrgSecretParams(BaseModel):
    org: str
    secret_name: str
    encrypted_value: Optional[str]
    key_id: Optional[str]
    visibility: str
    selected_repository_ids: Optional[List[int]]

class DeleteOrgSecretParams(BaseModel):
    org: str
    secret_name: str

class ListSecretSelectedReposParams(BaseModel):
    org: str
    secret_name: str

class SetOrgSecretReposParams(BaseModel):
    org: str
    secret_name: str
    selected_repository_ids: List[int]

class AddRepoToSecretParams(BaseModel):
    org: str
    secret_name: str
    repository_id: int

class RemoveRepoFromSecretParams(BaseModel):
    org: str
    secret_name: str
    repository_id: int

class ListRepoOrgSecretsParams(BaseModel):
    owner: str
    repo: str

class ListRepoSecretsParams(BaseModel):
    owner: str
    repo: str

class GetRepoPublicKeyParams(BaseModel):
    owner: str
    repo: str

class GetRepoSecretParams(BaseModel):
    owner: str
    repo: str
    secret_name: str

class CreateUpdateRepoSecretParams(BaseModel):
    owner: str
    repo: str
    secret_name: str
    encrypted_value: Optional[str]
    key_id: Optional[str]

class DeleteRepoSecretParams(BaseModel):
    owner: str
    repo: str
    secret_name: str

class ListEnvSecretsParams(BaseModel):
    repository_id: int
    environment_name: str

class GetEnvPublicKeyParams(BaseModel):
    repository_id: int
    environment_name = str

class GetEnvSecretsParams(BaseModel):
    repository_id: int
    environment_name: str
    secret_name: str

class CreateUpdateEnvSecretParams(BaseModel):
    repository_id: int
    environment_name: str
    secret_name: str
    encrypted_value: str
    key_id: str

class DeleteEnvSecretParams(BaseModel):
    repository_id: int
    environment_name: str
    secret_name: str

class ListOrgShrsParams(BaseModel):
    org: str

class ListOrgRunnerAppsParams(BaseModel):
    org: str

class CreateJustInTimeRunnerConfigOrgParams(BaseModel):
    org: str
    name: str
    runner_group_id: int
    labels: List[str]
    work_folder: Optional[str]

class CreateOrgRegistrationTokenParams(BaseModel):
    org: str

class CreateOrgRemoveTokenParams(BaseModel):
    org: str

class GetOrgShrParams(BaseModel):
    org: str
    runner_id: int

class DeleteOrgShrParams(BaseModel):
    org: str
    runner_id: int

class ListOrgSelfHostedRunnerLabelsParams(BaseModel):
    org: str
    runner_id: int

class AddCustomShrLabelsOrgParams(BaseModel):
    org: str
    runner_id: int
    labels: List[str]

class SetCustomShrLabelsOrgParams(BaseModel):
    org: str
    runner_id: int
    labels: List[str]

class RemoveAllCustomShrLabelsOrgParams(BaseModel):
    org: str
    runner_id: int

class RemoveCustomShrLabelsOrgParams(BaseModel):
    org: str
    runner_id: int
    name: str

class ListRepoShrParams(BaseModel):
    owner: str
    repo: str

class ListRepoRunnerAppsParams(BaseModel):
    owner: str
    repo: str

class CreateJustInTimeRunnerConfigRepoParams(BaseModel):
    owner: str
    repo: str
    name: str
    runner_group_id: int
    labels: List[str]
    work_folder: Optional[str]

class CreateRepoRegistrationTokenParameters(BaseModel):
    owner: str
    repo: str

class CreateRepoRemoveTokenParameters(BaseModel):
    owner: str
    repo: str

class GetRepoShrParams(BaseModel):
    owner: str
    repo: str
    runner_id: int

class DeleteRepoShrParams(BaseModel):
    owner: str
    repo: str
    runner_id: int 

class ListRepoShrLabelsParams(BaseModel):
    owner: str
    repo: str
    runner_id: int 

class AddCustomshrLabelsRepoParams(BaseModel):
    owner: str
    repo: str
    runner_id: int 
    labels: List[str]

class SetCustomShrLabelsRepoParams(BaseModel):
    owner: str
    repo: str
    runner_id: int
    labels: List[str]

class ListRepoShrLabelsParams(BaseModel):
    owner: str
    repo: str
    runner_id: int

class RemoveAllLabelsShrRepoParams(BaseModel):
    owner: str
    repo: str
    runner_id: int

class RemoveCustomLabelFromShrParams(BaseModel):
    owner: str
    repo: str
    runner_id: int
    name: str

class ListOrgVariablesParams(BaseModel):
    org: str

class CreateOrgVariableParams(BaseModel):
    org: str
    name: str
    value: str
    visibility: str
    selected_repository_ids: Optional[List[int]]

class GetOrgVariableParams(BaseModel):
    org: str
    name: str

class UpdateOrgVariableParams(BaseModel):
    org: str
    old_name: str
    name: Optional[str]
    value: Optional[str]
    visibility: Optional[str]
    selected_repository_ids: Optional[List[int]]

class DeleteOrgVariableParams(BaseModel):
    org: str
    name: str

class ListOrgVarReposParams(BaseModel):
    org: str
    name: str

class SetOrgVarReposParams(BaseModel):
    org: str
    name: str
    selected_repository_ids: List[int]

class AddRepoToOrgVariableParams(BaseModel):
    org: str
    name: str
    repository_id: int

class DeleteRepoFromOrgVariableParams(BaseModel):
    org: str
    name: str
    repository_id: int

class ListRepoOrgVariablesParams(BaseModel):
    owner: str
    repo: str 

class ListRepoVariablesParams(BaseModel):
    owner: str
    repo: str 

class CreateRepoVariableParams(BaseModel):
    owner: str
    repo: str 
    name: str
    value: str

class GetRepoVariableParams(BaseModel):
    owner: str
    repo: str 
    name: str

class UpdateRepoVariableParams(BaseModel):
    owner: str
    repo: str 
    old_name: str
    name: Optional[str]
    value: Optional[str]

class DeleteRepoVariableParams(BaseModel):
    owner: str
    repo: str 
    name: str

class ListEnvironmentVariablesParams(BaseModel):
    repository_id: int
    environment_name: str

class CreateEnvironmentVariableParams(BaseModel):
    repository_id: int
    environment_name: str
    name: str
    value: str

class GetEnvironmentVariableParams(BaseModel):
    repository_id: int
    environment_name: str
    name: str

class UpdateEnvironmentVariableParams(BaseModel):
    repository_id: int
    environment_name: str
    old_name: str
    name: Optional[str]
    value: Optional[str]

class DeleteEnvironmentVariableParams(BaseModel):
    repository_id: int
    environment_name: str
    name: str

class GetWorkflowRunJobParams(BaseModel):
    owner: str
    repo: str
    job_id: int

class DownloadJobLogsForWfRunParams(BaseModel):
    owner: str
    repo: str
    job_id: int

class ListJobsForWfRunAttemptParams(BaseModel):
    owner: str
    repo: str
    run_id: int
    attempt_number: int

class ListJobsForWfRunParams(BaseModel):
    owner: str
    repo: str
    run_id: int

class RerunJobsFromWorkflowRunParams(BaseModel):
    owner: str
    repo: str
    job_id: str

class ListRepoWorkflowRunsParams(BaseModel):
    owner: str
    repo: str

class GetWorkflowRunParams(BaseModel):
    owner: str
    repo: str
    run_id: str

class DeleteWorkflowRunParams(BaseModel):
    owner: str
    repo: str
    run_id: str

class GetWfRunReviewHistoryParams(BaseModel):
    owner: str
    repo: str
    run_id: str

class ApproveWfRunForForkPrsParams(BaseModel):
    owner: str
    repo: str
    run_id: str

class GetWorkflowRunAttemptParams(BaseModel):
    owner: str
    repo: str
    run_id: str
    attempt_number: int