from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class IssueStateEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")

@action_store.kubiya_action()
def list_issue_state_events(input: IssueStateEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_state_events")

class SingleIssueStateEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")
    resource_state_event_id: int = Field(description="The ID of a state event.")

@action_store.kubiya_action()
def get_single_issue_state_event(input: SingleIssueStateEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_state_events/{input.resource_state_event_id}")

class MergeRequestStateEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")

@action_store.kubiya_action()
def list_merge_request_state_events(input: MergeRequestStateEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_state_events")

class SingleMergeRequestStateEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    resource_state_event_id: int = Field(description="The ID of a state event.")

@action_store.kubiya_action()
def get_single_merge_request_state_event(input: SingleMergeRequestStateEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_state_events/{input.resource_state_event_id}")

class EpicStateEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    epic_id: int = Field(description="The ID of an epic.")

@action_store.kubiya_action()
def list_epic_state_events(input: EpicStateEvents):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/resource_state_events")

class SingleEpicStateEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    epic_id: int = Field(description="The ID of an epic.")
    resource_state_event_id: int = Field(description="The ID of a state event.")

@action_store.kubiya_action()
def get_single_epic_state_event(input: SingleEpicStateEvent):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/resource_state_events/{input.resource_state_event_id}")
