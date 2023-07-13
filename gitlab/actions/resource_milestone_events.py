from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class IssueMilestoneEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")

@action_store.kubiya_action()
def list_issue_milestone_events(input: IssueMilestoneEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_milestone_events")

class SingleIssueMilestoneEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")
    resource_milestone_event_id: int = Field(description="The ID of a milestone event.")

@action_store.kubiya_action()
def get_single_issue_milestone_event(input: SingleIssueMilestoneEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_milestone_events/{input.resource_milestone_event_id}")

class MergeRequestMilestoneEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")

@action_store.kubiya_action()
def list_merge_request_milestone_events(input: MergeRequestMilestoneEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_milestone_events")

class SingleMergeRequestMilestoneEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    resource_milestone_event_id: int = Field(description="The ID of a milestone event.")

@action_store.kubiya_action()
def get_single_merge_request_milestone_event(input: SingleMergeRequestMilestoneEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_milestone_events/{input.resource_milestone_event_id}")
