from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.job_token_scopes import *
@action_store.kubiya_action()
def get_project_ci_cd_job_token_access_settings(input: GetProjectCICDJobTokenAccessSettingsInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/job_token_scope')
@action_store.kubiya_action()
def patch_project_ci_cd_job_token_access_settings(input: PatchProjectCICDJobTokenAccessSettingsInput):
    return patch_wrapper(endpoint=f'/projects/{input.id}/job_token_scope', args=input.dict())
@action_store.kubiya_action()
def get_project_ci_cd_job_token_inbound_allowlist(input: GetProjectCICDJobTokenInboundAllowlistInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/job_token_scope/allowlist')
@action_store.kubiya_action()
def create_new_project_to_job_token_inbound_allowlist(input: CreateNewProjectToJobTokenInboundAllowlistInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/job_token_scope/allowlist', args=input.dict())
@action_store.kubiya_action()
def remove_project_from_job_token_inbound_allowlist(input: RemoveProjectFromJobTokenInboundAllowlistInput):
    return delete_wrapper(endpoint=f'/projects/{input.id}/job_token_scope/allowlist/{input.target_project_id}')