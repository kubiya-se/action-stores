from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.resource_state_events import *
@action_store.kubiya_action()
def list_issue_state_events(input: IssueStateEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_state_events')
@action_store.kubiya_action()
def get_single_issue_state_event(input: SingleIssueStateEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_state_events/{input.resource_state_event_id}')
@action_store.kubiya_action()
def list_merge_request_state_events(input: MergeRequestStateEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_state_events')
@action_store.kubiya_action()
def get_single_merge_request_state_event(input: SingleMergeRequestStateEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_state_events/{input.resource_state_event_id}')
@action_store.kubiya_action()
def list_epic_state_events(input: EpicStateEvents):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/resource_state_events')
@action_store.kubiya_action()
def get_single_epic_state_event(input: SingleEpicStateEvent):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/resource_state_events/{input.resource_state_event_id}')