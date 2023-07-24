from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from enum import Enum
from datetime import datetime


class MergeOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class MergeScope(str, Enum):
    active = "active"
    complete = "complete"

class MergeTrainsGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project")
    scope: Optional[MergeScope] = None
    sort: Optional[MergeOrder] = None

@action_store.kubiya_action()
def list_merge_trains_for_a_project(input: MergeTrainsGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_trains", args=input.dict(exclude_none=True))

class MergeTrainsTargetBranchGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project")
    target_branch: str = Field(description="The target branch of the merge train")
    scope: Optional[MergeScope] = None
    sort: Optional[MergeOrder] = None

@action_store.kubiya_action()
def list_merge_requests_in_a_merge_train(input: MergeTrainsTargetBranchGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_trains/{input.target_branch}", args=input.dict(exclude_none=True))

class MergeTrainStatusGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project")
    merge_request_iid: int = Field(description="The internal ID of the merge request")

@action_store.kubiya_action()
def get_the_status_of_a_merge_request_on_a_merge_train(input: MergeTrainStatusGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_trains/merge_requests/{input.merge_request_iid}")

class MergeTrainAdd(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project")
    merge_request_iid: int = Field(description="The internal ID of the merge request")
    when_pipeline_succeeds: Optional[bool] = None
    sha: Optional[str] = None
    squash: Optional[bool] = None

@action_store.kubiya_action()
def add_a_merge_request_to_a_merge_train(input: MergeTrainAdd):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_trains/merge_requests/{input.merge_request_iid}", args=input.dict(exclude_none=True))
