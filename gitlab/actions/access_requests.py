from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.access_requests import *

@action_store.kubiya_action()
def list_access_requests_for_a_project(input: ProjectsIdAccessRequests):
    return get_wrapper(endpoint=f'/projects/{input.id}/access_requests')
@action_store.kubiya_action()
def request_access_to_a_group(input: GroupsIdAccessRequests):
    return post_wrapper(endpoint=f'/groups/{input.id}/access_requests')
@action_store.kubiya_action()
def request_access_to_a_project(input: ProjectsIdAccessRequests):
    return post_wrapper(endpoint=f'/projects/{input.id}/access_requests', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def approve_an_access_request_to_a_group(input: GroupsIdAccessRequestsUseridApprove):
    body = {'access_level': input.access_level} if input.access_level else {}
    return put_wrapper(endpoint=f'/groups/{input.id}/access_requests/{input.user_id}/approve', args=body)
@action_store.kubiya_action()
def approve_an_access_request_to_a_project(input: ProjectsIdAccessRequestsUseridApprove):
    return put_wrapper(endpoint=f'/projects/{input.id}/access_requests/{input.user_id}/approve', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def deny_an_access_request_to_a_group(input: GroupsIdAccessRequestsUserid):
    return delete_wrapper(endpoint=f'/groups/{input.id}/access_requests/{input.user_id}')
@action_store.kubiya_action()
def deny_an_access_request_to_a_project(input: ProjectsIdAccessRequestsUserid):
    return delete_wrapper(endpoint=f'/projects/{input.id}/access_requests/{input.user_id}')