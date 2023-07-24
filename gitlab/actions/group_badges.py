from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class GroupsIdBadges(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the group owned by the authenticated user

    name: Optional[str] = None  # Name of the badges to return (case-sensitive).


@action_store.kubiya_action()
def list_all_badges_of_a_group(input: GroupsIdBadges):
    return get_wrapper(endpoint=f"/groups/{input.id}/badges", args=input.dict(exclude_none=True))


class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the group owned by the authenticated user

    badge_id: int  # The badge ID


@action_store.kubiya_action()
def get_a_badge_of_a_group(input: GroupsIdBadgesBadgeid):
    return get_wrapper(endpoint=f"/groups/{input.id}/badges/{input.badge_id}", args=input.dict(exclude_none=True))


class GroupsIdBadgesAdd(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the group owned by the authenticated user

    link_url: str  # URL of the badge link

    image_url: str  # URL of the badge image

    name: Optional[str] = None  # Name of the badge


@action_store.kubiya_action()
def add_a_badge_to_a_group(input: GroupsIdBadgesAdd):
    return post_wrapper(endpoint=f"/groups/{input.id}/badges", args=input.dict(exclude_none=True))


class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the group owned by the authenticated user

    badge_id: int  # The badge ID

    link_url: Optional[str] = None  # URL of the badge link

    image_url: Optional[str] = None  # URL of the badge image

    name: Optional[str] = None  # Name of the badge


@action_store.kubiya_action()
def edit_a_badge_of_a_group(input: GroupsIdBadgesBadgeidEdit):
    return put_wrapper(endpoint=f"/groups/{input.id}/badges/{input.badge_id}", args=input.dict(exclude_none=True))


class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the group owned by the authenticated user

    badge_id: int  # The badge ID


@action_store.kubiya_action()
def remove_a_badge_from_a_group(input: GroupsIdBadgesBadgeidDelete):
    return delete_wrapper(endpoint=f"/groups/{input.id}/badges/{input.badge_id}", args=input.dict(exclude_none=True))


class GroupsIdBadgesRender(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the group owned by the authenticated user

    link_url: str  # URL of the badge link

    image_url: str  # URL of the badge image


@action_store.kubiya_action()
def preview_a_badge_from_a_group(input: GroupsIdBadgesRender):
    return get_wrapper(endpoint=f"/groups/{input.id}/badges/render", args=input.dict(exclude_none=True))
