from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class Events(BaseModel):

    action: Optional[str] = None # 	Include only events of a particular action type
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description = "Include only events created before a certain date.")
    after: Optional[datetime] = Field(None, description = "Include only events created after a particular date.")
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None

class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None

@action_store.kubiya_action()
def list_currently_authenticated_users_events(input: AuthenticatedUserEvents):
    return get_wrapper(endpoint=f"/events", args=input.dict(exclude_none=True))
    
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

@action_store.kubiya_action()
def get_user_contribution_events(input: UserContributionEvents):
    return get_wrapper(endpoint=f"/users/{input.id}/events", args=input.dict(exclude_none=True))

class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

@action_store.kubiya_action()
def list_a_projects_visible_events(input: ProjectVisibleEvents):
    return get_wrapper(endpoint=f"/projects/{input.project_id}/events", args=input.dict(exclude_none=True))
