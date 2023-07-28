from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.events import *
@action_store.kubiya_action()
def list_currently_authenticated_users_events(input: AuthenticatedUserEvents):
    return get_wrapper(endpoint=f'/events', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_user_contribution_events(input: UserContributionEvents):
    return get_wrapper(endpoint=f'/users/{input.id}/events', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_a_projects_visible_events(input: ProjectVisibleEvents):
    return get_wrapper(endpoint=f'/projects/{input.project_id}/events', args=input.dict(exclude_none=True))