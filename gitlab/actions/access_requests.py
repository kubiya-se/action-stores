from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectsIdAccessRequests(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

@action_store.kubiya_action()
def list_access_requests_for_a_project(input: ProjectsIdAccessRequests):
    #return get_wrapper(endpoint=f"/projects/{input.id}/access_requests", args=input.dict(exclude_none=True))
    return get_wrapper(endpoint=f"/projects/{input.id}/access_requests")

class GroupsIdAccessRequests(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user


@action_store.kubiya_action()
def request_access_to_a_group(input: GroupsIdAccessRequests):
    #return post_wrapper(endpoint=f"/groups/{input.id}/access_requests", args=input.dict(exclude_none=True))
    return post_wrapper(endpoint=f"/groups/{input.id}/access_requests")


# class ProjectsIdAccessRequests(BaseModel):
#     id: int  # The ID or URL-encoded path of the group or project


@action_store.kubiya_action()
def request_access_to_a_project(input: ProjectsIdAccessRequests):
    return post_wrapper(endpoint=f"/projects/{input.id}/access_requests", args=input.dict(exclude_none=True))


class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    user_id: int  # The user ID of the access requester
    access_level: Optional[int] = None  # A valid access level (defaults: 30, the Developer role)


@action_store.kubiya_action()
def approve_an_access_request_to_a_group(input: GroupsIdAccessRequestsUseridApprove):
    body = {"access_level": input.access_level} if input.access_level else {}
    return put_wrapper(endpoint=f"/groups/{input.id}/access_requests/{input.user_id}/approve",
                       args=body)

class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    user_id: int  # The user ID of the access requester
    access_level: Optional[int] = None  # A valid access level (defaults: 30, the Developer role)


@action_store.kubiya_action()
def approve_an_access_request_to_a_project(input: ProjectsIdAccessRequestsUseridApprove):
    return put_wrapper(endpoint=f"/projects/{input.id}/access_requests/{input.user_id}/approve",
                       args=input.dict(exclude_none=True))


class GroupsIdAccessRequestsUserid(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    user_id: int  # The user ID of the access requester


@action_store.kubiya_action()
def deny_an_access_request_to_a_group(input: GroupsIdAccessRequestsUserid):
    #return delete_wrapper(endpoint=f"/groups/{input.id}/access_requests/{input.user_id}",
                          #args=input.dict(exclude_none=True))
    return delete_wrapper(endpoint=f"/groups/{input.id}/access_requests/{input.user_id}")


class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    user_id: int  # The user ID of the access requester


@action_store.kubiya_action()
def deny_an_access_request_to_a_project(input: ProjectsIdAccessRequestsUserid):
    return delete_wrapper(endpoint=f"/projects/{input.id}/access_requests/{input.user_id}")
