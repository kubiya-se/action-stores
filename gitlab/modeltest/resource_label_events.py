from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class IssueLabelEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
class SingleIssueLabelEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
    resource_label_event_id: int = Field(description='The ID of a label event.')
class GroupEpicLabelEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    epic_id: int = Field(description='The ID of an epic.')
class SingleGroupEpicLabelEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    epic_id: int = Field(description='The ID of an epic.')
    resource_label_event_id: int = Field(description='The ID of a label event.')
class MergeRequestLabelEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestLabelEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    resource_label_event_id: int = Field(description='The ID of a label event.')