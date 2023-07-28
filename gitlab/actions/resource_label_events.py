from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.resource_label_events import *
@action_store.kubiya_action()
def list_issue_label_events(input: IssueLabelEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_label_events')
@action_store.kubiya_action()
def get_single_issue_label_event(input: SingleIssueLabelEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_label_events/{input.resource_label_event_id}')
@action_store.kubiya_action()
def list_group_epic_label_events(input: GroupEpicLabelEvents):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/resource_label_events')
@action_store.kubiya_action()
def get_single_group_epic_label_event(input: SingleGroupEpicLabelEvent):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/resource_label_events/{input.resource_label_event_id}')
@action_store.kubiya_action()
def list_merge_request_label_events(input: MergeRequestLabelEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_label_events')
@action_store.kubiya_action()
def get_single_merge_request_label_event(input: SingleMergeRequestLabelEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/resource_label_events/{input.resource_label_event_id}')