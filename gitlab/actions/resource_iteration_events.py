from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class IssueIterationEvents(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")

@action_store.kubiya_action()
def list_project_issue_iteration_events(input: IssueIterationEvents):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_iteration_events")

class SingleIssueIterationEvent(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(description="The IID of an issue.")
    resource_iteration_event_id: int = Field(description="The ID of an iteration event.")

@action_store.kubiya_action()
def get_single_issue_iteration_event(input: SingleIssueIterationEvent):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/resource_iteration_events/{input.resource_iteration_event_id}")
