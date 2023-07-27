from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.resource_milestone_events import *
@action_store.kubiya_action()
def list_issue_milestone_events(input: IssueMilestoneEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_milestone_events')
@action_store.kubiya_action()
def get_single_issue_milestone_event(input: SingleIssueMilestoneEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_milestone_events/{input.resource_milestone_event_id}')
@action_store.kubiya_action()
def list_merge_request_milestone_events(input: MergeRequestMilestoneEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_milestone_events')
@action_store.kubiya_action()
def get_single_merge_request_milestone_event(input: SingleMergeRequestMilestoneEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_milestone_events/{input.resource_milestone_event_id}')