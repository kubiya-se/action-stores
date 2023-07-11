from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int,str] = Field(description = "ID of a project")

@action_store.kubiya_action()
def get_project_external_status_check_services(input: ProjectsIdExternalstatuschecks):
    return get_wrapper(endpoint=f"/projects/{input.id}/external_status_checks", args=input.dict(exclude_none=True))

class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description="ID of a project")
    name: Optional[str] = Field(description="Display name of external status check service")
    external_url: Optional[str] = Field(description="URL of external status check service")
    protected_branch_ids: Optional[List[int]] = Field(description="IDs of protected branches to scope the rule by")

@action_store.kubiya_action()
def create_external_status_check_service(input: CreateUpdateExternalStatusCheckService):
    return post_wrapper(endpoint=f"/projects/{input.id}/external_status_checks", args=input.dict(exclude_none=True))

class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]  # ID of a project
    check_id: int  # ID of an external status check service
    name: Optional[str] = None  # Display name of external status check service
    external_url: Optional[str] = None  # URL of external status check service
    protected_branch_ids: Optional[List[int]] = None  # IDs of protected branches to scope the rule by

@action_store.kubiya_action()
def update_external_status_check_service(input: UpdateExternalStatusCheckService):
    return put_wrapper(endpoint=f"/projects/{input.id}/external_status_checks/{input.check_id}", 
                       args=input.dict(exclude_none=True))


class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description="ID of a project")
    check_id: int = Field(description="ID of an external status check service")

@action_store.kubiya_action()
def delete_external_status_check_service(input: DeleteExternalStatusCheckService):
    return delete_wrapper(endpoint=f"/projects/{input.id}/external_status_checks/{input.check_id}", args=input.dict(exclude_none=True))

class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description="ID of a project")
    merge_request_iid: int = Field(description="IID of a merge request")

@action_store.kubiya_action()
def list_status_checks_for_merge_request(input: MergeRequestStatusChecks):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/status_checks", args=input.dict(exclude_none=True))


class SetStatusCheck(BaseModel):
    id: int = Field(description="ID of a project")
    merge_request_iid: int = Field(description="IID of a merge request")
    sha: str = Field(description="SHA at HEAD of the source branch")
    external_status_check_id: int = Field(description="ID of an external status check")
    status: Optional[str] = Field(description="Set to passed to pass the check or failed to fail it")

@action_store.kubiya_action()
def set_status_of_external_status_check(input: SetStatusCheck):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/status_check_responses", args=input.dict(exclude_none=True))

class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description="ID of a project")
    merge_request_iid: int = Field(description="IID of a merge request")
    external_status_check_id: int = Field(description="ID of a failed external status check")

@action_store.kubiya_action()
def retry_failed_status_check_for_merge_request(input: RetryFailedStatusCheck):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/status_checks/{input.external_status_check_id}/retry", args=input.dict(exclude_none=True))