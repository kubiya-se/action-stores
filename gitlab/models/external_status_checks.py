from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description='Display name of external status check service')
    external_url: Optional[str] = Field(description='URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description='IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description='ID of an external status check')
    status: Optional[str] = Field(description='Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description='ID of a failed external status check')