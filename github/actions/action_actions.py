from .. import action_store as action_store
import logging
from ..models.actions import *
from ..http_wrapper import get_wrapper, post_wrapper, patch_wrapper, delete_wrapper, put_wrapper

FAILED_MSG = "Insufficient data"

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def delete_artifact(params:GetArtifactParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/artifacts/{params.artifact_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def download_artifact(params:DownloadArtifactParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/artifacts/{params.artifact_id}/{params.archive_format}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_workflow_run_artifacts(params: ListWorkflowRunArtifactsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}/artifacts")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()    
def list_repos_with_cache_usage_by_org(params: ListReposWithCacheUsageInOrgParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/cache/usage-by-repository")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()        
def get_repo_cache_usage(params: GetRepoCacheUsageParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/cache/usage")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()        
def list_caches_in_repo(params: ListCachesInRepoParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/caches")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()        
def delete_caches_by_key(params: DeleteCachesByKeyParams): ##test if ? works
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/caches?{params.key}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()        
def delete_caches_by_key(params: DeleteCachesByIdParams): ##test if ? works
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/caches/{params.cache_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action() 
def get_oidc_sc_customization_template_by_org(params: GetCustomizationTemplateForOIDCSubjectClaimOrgParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/oidc/customization/sub")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_oidc_sc_customization_template_by_org(params: SetCustomizationTemplateForOIDCSubjectClaimOrgParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = put_wrapper(f"/orgs/{params.org}/actions/oidc/customization/sub", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_oidc_sc_customization_template_by_repo(params: GetCustomizationTemplateForOIDCSubjectClaimRepoParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.owner}/{params.repo}/actions/oidc/customization/sub")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_oidc_sc_customization_template_by_repo(params: SetCustomizationTemplateForOIDCSubjectClaimRepoParams):
    data = params.dict(exclude_none = True)
    if data:
        data.drop("owner")
        data.drop("repo")
        resp = put_wrapper(f"/orgs/{params.owner}/{params.repo}/actions/oidc/customization/sub", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action() 
def get_actions_permissions_by_org(params: GetOrgsActionsPermissionsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/permissions")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action() 
def set_actions_permissions_by_org(params: SetOrgsActionsPermissionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = put_wrapper(f"/orgs/{params.org}/actions/permissions", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_selected_repos_with_actions_by_org(params: ListSelectedReposEnabledForActionsByOrgParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/permissions/repositories")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_repos_enabled_for_actions_by_org(params: SetReposEnabledForActionsByOrgParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = put_wrapper(f"/orgs/{params.org}/actions/permissions/repositories", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def enable_repo_in_org_for_actions(params: EnableRepoInOrgForActionsParams):
    if params.dict(exclude_none = True):
        resp = put_wrapper(f"/orgs/{params.org}/actions/permissions/repositories/{params.repository_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def disable_repo_in_org_for_actions(params: DisableRepoInOrgForActionsParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/permissions/repositories/{params.repository_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_allowed_actions_for_org(params: GetAllowedActionsByOrgParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/permissions/selected-actions")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_allowed_actions_for_org(params: SetAllowedActionsByOrgParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = put_wrapper(f"/orgs/{params.org}/actions/permissions/selected-actions", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_org_default_workflow_permissions(params: GetOrgDefaultWorkflowPermissionsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/permissions/workflow")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_org_default_workflow_permissions(params: SetOrgDefaultWorkflowPermissionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = put_wrapper(f"/orgs/{params.org}/actions/permissions/workflow", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_repo_actions_permissions(params: GetRepoActionsPermissionsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_repo_actions_permissions(params: SetRepoActionsPermissionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.drop("owner")
        data.drop("repo")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_access_for_external_workflows_by_repo(params: GetAccessForExternalWorkflowsByRepoParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions/access")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_access_for_external_workflows_by_repo(params: SetAccessForExternalWorkflowsByRepoParams):
    data = params.dict(exclude_none = True)
    if data:
        data.drop("owner")
        data.drop("repo")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions/access", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_allowed_actions_by_repo(params: GetAllowedActionsByRepoParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions/selected-actions")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action() 
def set_allowed_actions_by_repo(params: SetAllowedActionsByRepoParams):
    data = params.dict(exclude_none = True)
    if data:
        data.drop("owner")
        data.drop("repo")
        if len(data) == 0:
            data = None
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions/selected-actions", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_repo_default_workflow_permissions(params: GetRepoDefaultWorkflowPermissionsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions/workflow")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_repo_default_workflow_permissions(params: SetRepoDefaultWorkflowPermissionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.drop("owner")
        data.drop("repo")
        if len(data) == 0:
            data = None
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/permissions/workflow", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_org_secrets(params: ListOrgSecretsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/secrets")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def get_org_public_key(params: GetOrgPublicKeyParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/secrets/public-key")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_org_secret(params: GetOrgSecretParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_update_org_secret(params: CreateUpdateOrgSecretParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        data.pop("secret_name")
        resp = put_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def delete_org_secret(params: DeleteOrgSecretParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def list_secret_selected_repos(params: ListSecretSelectedReposParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}/repositories")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def set_org_secret_repos(params: SetOrgSecretReposParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        data.pop("secret_name")
        resp = put_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}/repositories", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def add_repo_to_secret(params: AddRepoToSecretParams):
    if params.dict(exclude_none = True):
        resp = put_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}/repositories/{params.repository_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def remove_repo_from_secret(params: RemoveRepoFromSecretParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/secrets/{params.secret_name}/repositories/{params.repository_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_repo_org_secrets(params: ListRepoOrgSecretsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/organization-secrets")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_repo_secrets(params: ListRepoSecretsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/secrets")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_repo_public_key(params: GetRepoPublicKeyParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/secrets/public-key")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_repo_secret(params: GetRepoSecretParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/secrets/{params.secret_name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def create_update_repo_secret(params: CreateUpdateRepoSecretParams):
    data = params.dict(exclude_none=True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("secret_name")
        if len(data) == 0:
            data = None
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/secrets/{params.secret_name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def delete_repo_secret(params: DeleteRepoSecretParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/secrets/{params.secret_name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_environment_secrets(params: ListEnvSecretsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/secrets")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def get_environment_public_key(params: GetEnvPublicKeyParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/secrets/public-key")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_environment_secret(params: GetEnvSecretsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/secrets/{params.secret_name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_update_environment_secret(params: CreateUpdateEnvSecretParams):
    data = params.dict(exclude_none=True)
    if data:
        data.pop("repository_id")
        data.pop("environment_name")
        data.pop("secret_name")
        resp = put_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/secrets/{params.secret_name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def delete_environment_secret(params: DeleteEnvSecretParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/secrets/{params.secret_name}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()  
def list_org_self_hosted_runners(params: ListOrgShrsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/runners")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def list_org_runner_apps(params: ListOrgRunnerAppsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/runners/downloads")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_just_in_time_runner_config_for_org(params: CreateJustInTimeRunnerConfigOrgParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = get_wrapper(f"/orgs/{params.org}/actions/runners/generate-jitconfig", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_org_registration_token(params: CreateOrgRegistrationTokenParams):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"/orgs/{params.org}/actions/runners/registration-token")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_org_remove_token(params: CreateOrgRemoveTokenParams):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"/orgs/{params.org}/actions/runners/remove-token")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_org_self_hosted_runner(params: GetOrgShrParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_org_self_hosted_runner(params: DeleteOrgShrParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_org_self_hosted_runner_labels(params: ListOrgSelfHostedRunnerLabelsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}/labels")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def add_org_custom_self_hosted_runner_labels(params: AddCustomShrLabelsOrgParams):
    data = params.dict(exclude_none=True)
    if data:
        data.pop("org")
        data.pop("runner_id")
        resp = post_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def set_custom_self_hosted_runner_labels_for_org(params: SetCustomShrLabelsOrgParams):
    data = params.dict(exclude_none=True)
    if data:
        data.pop("org")
        data.pop("runner_id")
        resp = put_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def remove_all_custom_self_hosted_runner_labels_for_orgs(params: RemoveAllCustomShrLabelsOrgParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}/labels")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def remove_all_custom_self_hosted_runner_labels_for_orgs(params: RemoveCustomShrLabelsOrgParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/runners/{params.runner_id}/labels/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_repo_self_hosted_runners(params: ListRepoShrParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_repo_runner_applications(params: ListRepoRunnerAppsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/downloads")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_just_in_time_runner_configuration_for_repo(params: CreateJustInTimeRunnerConfigRepoParams):
    data = params.dict(exclude_none=True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/generate-jitconfig", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def create_repo_registration_token(params: CreateRepoRegistrationTokenParameters):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/registration_token")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_repo_remove_token(params: CreateRepoRemoveTokenParameters):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/remove_token")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_repo_self_hosted_runner(params: GetRepoShrParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_repo_self_hosted_runner(params: DeleteRepoShrParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_repo_self_hosted_runner_labels(params: ListRepoShrLabelsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}/labels")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def add_custom_label_to_a_self_hosted_runner_in_repo(params: AddCustomshrLabelsRepoParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("runner_id")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def set_custom_labels_for_a_self_hosted_runner_in_repo(params: SetCustomShrLabelsRepoParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("runner_id")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def remove_all_custom_labels_from_repo_self_hosted_runner(params: RemoveAllLabelsShrRepoParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}/labels")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def remove_custom_label_from_repo_self_hosted_runner(params: RemoveCustomLabelFromShrParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runners/{params.runner_id}/labels/{params.name}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()  
def list_org_variables(params: ListOrgVariablesParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/variables")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def create_org_variable(params: CreateOrgVariableParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = post_wrapper(f"/orgs/{params.org}/actions/variables")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_org_variable(params: GetOrgVariableParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/variables/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def update_org_variable(params: UpdateOrgVariableParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        data.pop("old_name")
        if len(data) == 0:
            data = None
        resp = patch_wrapper(f"/orgs/{params.org}/actions/variables/{params.old_name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_org_variable(params: DeleteOrgVariableParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/variables/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_repos_for_org_variable(params: ListOrgVarReposParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/orgs/{params.org}/actions/variables/{params.name}/repositories")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def set_repos_for_org_variable(params: SetOrgVarReposParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        data.pop("name")
        resp = put_wrapper(f"/orgs/{params.org}/actions/variables/{params.name}/repositories", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def add_selected_repo_to_org_variable(params: AddRepoToOrgVariableParams):
    if params.dict(exclude_none = True):
        resp = put_wrapper(f"/orgs/{params.org}/actions/variables/{params.name}/repositories/{params.repository_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_selected_repo_from_org_variable(params: DeleteRepoFromOrgVariableParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/orgs/{params.org}/actions/variables/{params.name}/repositories/{params.repository_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_repo_org_variables(params: ListRepoOrgVariablesParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/organization-variables")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_repo_variables(params: ListRepoVariablesParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/variables")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_repo_variable(params: CreateRepoVariableParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/actions/variables", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_repo_variable(params: GetRepoVariableParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/variables/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def update_repo_variable(params: UpdateRepoVariableParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("old_name")
        if len(data) == 0:
            data = None
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/actions/variables/{params.old_name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_repo_variable(params: GetRepoVariableParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/variables/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def list_environment_variables(params: ListEnvironmentVariablesParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/variables")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_environment_variable(params: CreateEnvironmentVariableParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("repository_id")
        data.pop("environment_name")
        resp = post_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/variables", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_environment_variable(params: GetEnvironmentVariableParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/variables/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def update_environment_variable(params: UpdateEnvironmentVariableParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("repository_id")
        data.pop("environment_name")
        data.pop("old_name")
        resp = patch_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/variables/{params.old_name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_environment_variable(params: DeleteEnvironmentVariableParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repositories/{params.repository_id}/environments/{params.environment_name}/variables/{params.name}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action() 
def get_a_job_for_a_workflow_run(params: GetWorkflowRunJobParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/jobs/{params.job_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def download_job_logs_for_a_workflow_run(params: DownloadJobLogsForWfRunParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/jobs/{params.job_id}/logs")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_jobs_for_a_workflow_run_attempt(params: ListJobsForWfRunAttemptParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}/attempts/{params.attempt_number}/jobs")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_jobs_for_a_workflow_run(params: ListJobsForWfRunParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}/jobs")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def rerun_a_job_from_a_workflow_run(params: RerunJobsFromWorkflowRunParams):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/actions/jobs/{params.job_id}/rerun")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def rerun_a_job_from_a_workflow_run(params: ListRepoWorkflowRunsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_a_workflow_run(params: GetWorkflowRunParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def delete_a_workflow_run(params: DeleteWorkflowRunParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_review_history_for_workflow_run(params: GetWfRunReviewHistoryParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}/approvals")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def approve_workflow_run_for_fork_pull_request(params: ApproveWfRunForForkPrsParams):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}/approve")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_workflow_run_attempt(params: GetWorkflowRunAttemptParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/actions/runs/{params.run_id}/attempts/{params.attempt_number}")
        return resp
    else:
        return FAILED_MSG