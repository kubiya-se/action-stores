from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]  # ID or URL-encoded path of the project.

@action_store.kubiya_action()
def get_project_ci_cd_job_token_access_settings(input: GetProjectCICDJobTokenAccessSettingsInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/job_token_scope")

class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]  # ID or URL-encoded path of the project.
    enabled: bool  # Indicates CI/CD job tokens generated in other projects have restricted access to this project.

@action_store.kubiya_action()
def patch_project_ci_cd_job_token_access_settings(input: PatchProjectCICDJobTokenAccessSettingsInput):
    return patch_wrapper(endpoint=f"/projects/{input.id}/job_token_scope", args=input.dict())

class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]  # ID or URL-encoded path of the project.

@action_store.kubiya_action()
def get_project_ci_cd_job_token_inbound_allowlist(input: GetProjectCICDJobTokenInboundAllowlistInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/job_token_scope/allowlist")

class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]  # ID or URL-encoded path of the project.
    target_project_id: int  # The ID of the project added to the CI/CD job token inbound allowlist.

@action_store.kubiya_action()
def create_new_project_to_job_token_inbound_allowlist(input: CreateNewProjectToJobTokenInboundAllowlistInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/job_token_scope/allowlist", args=input.dict())

class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]  # ID or URL-encoded path of the project.
    target_project_id: int  # The ID of the project that is removed from the CI/CD job token inbound allowlist.

@action_store.kubiya_action()
def remove_project_from_job_token_inbound_allowlist(input: RemoveProjectFromJobTokenInboundAllowlistInput):
    return delete_wrapper(endpoint=f"/projects/{input.id}/job_token_scope/allowlist/{input.target_project_id}")
