from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class MergeOrder(str, Enum):
    asc = 'asc'
    desc = 'desc'
class MergeScope(str, Enum):
    active = 'active'
    complete = 'complete'
class MergeTrainsGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project')
    scope: Optional[MergeScope] = None
    sort: Optional[MergeOrder] = None
class MergeTrainsTargetBranchGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project')
    target_branch: str = Field(description='The target branch of the merge train')
    scope: Optional[MergeScope] = None
    sort: Optional[MergeOrder] = None
class MergeTrainStatusGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project')
    merge_request_iid: int = Field(description='The internal ID of the merge request')
class MergeTrainAdd(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project')
    merge_request_iid: int = Field(description='The internal ID of the merge request')
    when_pipeline_succeeds: Optional[bool] = None
    sha: Optional[str] = None
    squash: Optional[bool] = None