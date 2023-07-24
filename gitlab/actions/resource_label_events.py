from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class IssueLabelEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")

@action_store.kubiya_action()
def list_issue_label_events(input: IssueLabelEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_label_events")

class SingleIssueLabelEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")
    resource_label_event_id: int = Field(description="The ID of a label event.")

@action_store.kubiya_action()
def get_single_issue_label_event(input: SingleIssueLabelEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_label_events/{input.resource_label_event_id}")

class GroupEpicLabelEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    epic_id: int = Field(description="The ID of an epic.")

@action_store.kubiya_action()
def list_group_epic_label_events(input: GroupEpicLabelEvents):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/resource_label_events")

class SingleGroupEpicLabelEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    epic_id: int = Field(description="The ID of an epic.")
    resource_label_event_id: int = Field(description="The ID of a label event.")

@action_store.kubiya_action()
def get_single_group_epic_label_event(input: SingleGroupEpicLabelEvent):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/resource_label_events/{input.resource_label_event_id}")

class MergeRequestLabelEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")

@action_store.kubiya_action()
def list_merge_request_label_events(input: MergeRequestLabelEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_label_events")

class SingleMergeRequestLabelEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    resource_label_event_id: int = Field(description="The ID of a label event.")

@action_store.kubiya_action()
def get_single_merge_request_label_event(input: SingleMergeRequestLabelEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_label_events/{input.resource_label_event_id}")

