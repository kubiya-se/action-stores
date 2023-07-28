from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.group_badges import *
@action_store.kubiya_action()
def list_all_badges_of_a_group(input: GroupsIdBadges):
    return get_wrapper(endpoint=f'/groups/{input.id}/badges', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_badge_of_a_group(input: GroupsIdBadgesBadgeid):
    return get_wrapper(endpoint=f'/groups/{input.id}/badges/{input.badge_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_a_badge_to_a_group(input: GroupsIdBadgesAdd):
    return post_wrapper(endpoint=f'/groups/{input.id}/badges', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_a_badge_of_a_group(input: GroupsIdBadgesBadgeidEdit):
    return put_wrapper(endpoint=f'/groups/{input.id}/badges/{input.badge_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_a_badge_from_a_group(input: GroupsIdBadgesBadgeidDelete):
    return delete_wrapper(endpoint=f'/groups/{input.id}/badges/{input.badge_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def preview_a_badge_from_a_group(input: GroupsIdBadgesRender):
    return get_wrapper(endpoint=f'/groups/{input.id}/badges/render', args=input.dict(exclude_none=True))