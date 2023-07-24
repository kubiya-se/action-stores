from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class ProjectsIdBadges(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user

    name: Optional[str] = None # Name of the badges to return (case-sensitive).


@action_store.kubiya_action()
def list_all_badges_of_a_project(input: ProjectsIdBadges):
    return get_wrapper(endpoint=f"/projects/{input.id}/badges", args=input.dict(exclude_none=True))


class ProjectsIdBadgesBadgeid(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user

    badge_id: int # The badge ID


@action_store.kubiya_action()
def get_a_badge_of_a_project(input: ProjectsIdBadgesBadgeid):
    return get_wrapper(endpoint=f"/projects/{input.id}/badges/{input.badge_id}", args=input.dict(exclude_none=True))


class ProjectsIdBadgesCreate(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user

    link_url: str # URL of the badge link

    image_url: str # URL of the badge image

    name: Optional[str] = None # Name of the badge


@action_store.kubiya_action()
def add_a_badge_to_a_project(input: ProjectsIdBadgesCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/badges", args=input.dict(exclude_none=True))


class ProjectsIdBadgesBadgeidEdit(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user

    badge_id: int # The badge ID

    link_url: Optional[str] = None # URL of the badge link

    image_url: Optional[str] = None # URL of the badge image

    name: Optional[str] = None # Name of the badge


@action_store.kubiya_action()
def edit_a_badge_of_a_project(input: ProjectsIdBadgesBadgeidEdit):
    return put_wrapper(endpoint=f"/projects/{input.id}/badges/{input.badge_id}", args=input.dict(exclude_none=True))


class ProjectsIdBadgesBadgeidDelete(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user

    badge_id: int # The badge ID


@action_store.kubiya_action()
def remove_a_badge_from_a_project(input: ProjectsIdBadgesBadgeidDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/badges/{input.badge_id}", args=input.dict(exclude_none=True))


class ProjectsIdBadgesRender(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user

    link_url: str # URL of the badge link

    image_url: str # URL of the badge image


@action_store.kubiya_action()
def preview_a_badge_from_a_project(input: ProjectsIdBadgesRender):
    return get_wrapper(endpoint=f"/projects/{input.id}/badges/render", args=input.dict(exclude_none=True))