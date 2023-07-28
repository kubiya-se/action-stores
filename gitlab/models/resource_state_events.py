from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class IssueStateEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
class SingleIssueStateEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
    resource_state_event_id: int = Field(description='The ID of a state event.')
class MergeRequestStateEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestStateEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    resource_state_event_id: int = Field(description='The ID of a state event.')
class EpicStateEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    epic_id: int = Field(description='The ID of an epic.')
class SingleEpicStateEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    epic_id: int = Field(description='The ID of an epic.')
    resource_state_event_id: int = Field(description='The ID of a state event.')