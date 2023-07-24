from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class IssueMilestoneEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
class SingleIssueMilestoneEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
    resource_milestone_event_id: int = Field(description='The ID of a milestone event.')
class MergeRequestMilestoneEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestMilestoneEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    resource_milestone_event_id: int = Field(description='The ID of a milestone event.')