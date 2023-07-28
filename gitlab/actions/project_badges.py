from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.project_badges import *
@action_store.kubiya_action()
def list_all_badges_of_a_project(input: ProjectsIdBadges):
    return get_wrapper(endpoint=f'/projects/{input.id}/badges', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_badge_of_a_project(input: ProjectsIdBadgesBadgeid):
    return get_wrapper(endpoint=f'/projects/{input.id}/badges/{input.badge_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_a_badge_to_a_project(input: ProjectsIdBadgesCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/badges', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_a_badge_of_a_project(input: ProjectsIdBadgesBadgeidEdit):
    return put_wrapper(endpoint=f'/projects/{input.id}/badges/{input.badge_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_a_badge_from_a_project(input: ProjectsIdBadgesBadgeidDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/badges/{input.badge_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def preview_a_badge_from_a_project(input: ProjectsIdBadgesRender):
    return get_wrapper(endpoint=f'/projects/{input.id}/badges/render', args=input.dict(exclude_none=True))