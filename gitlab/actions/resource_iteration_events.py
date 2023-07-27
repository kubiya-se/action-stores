from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.resource_iteration_events import *
@action_store.kubiya_action()
def list_project_issue_iteration_events(input: IssueIterationEvents):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_iteration_events')
@action_store.kubiya_action()
def get_single_issue_iteration_event(input: SingleIssueIterationEvent):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/resource_iteration_events/{input.resource_iteration_event_id}')