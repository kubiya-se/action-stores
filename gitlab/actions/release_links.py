
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ReleaseLinksList(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    tag_name: str = Field(description="The tag associated with the Release.")

@action_store.kubiya_action()
def list_links_of_a_release(input: ReleaseLinksList):
    return get_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/assets/links", args=input.dict(exclude_none=True))

class ReleaseLinkGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    tag_name: str = Field(description="The tag associated with the Release.")
    link_id: int = Field(description="The ID of the link.")

@action_store.kubiya_action()
def get_a_release_link(input: ReleaseLinkGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/assets/links/{input.link_id}", args=input.dict(exclude_none=True))

class ReleaseLinkCreate(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    tag_name: str = Field(description="The tag associated with the Release.")
    name: str = Field(description="The name of the link. Link names must be unique in the release.")
    url: str = Field(description="The URL of the link. Link URLs must be unique in the release.")
    direct_asset_path: Optional[str] = Field(None, description="Optional path for a direct asset link.")
    link_type: Optional[str] = Field(None, description="The type of the link: other, runbook, image, package. Defaults to other.")

@action_store.kubiya_action()
def create_a_release_link(input: ReleaseLinkCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/assets/links", args=input.dict(exclude_none=True))

class ReleaseLinkUpdate(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    tag_name: str = Field(description="The tag associated with the Release.")
    link_id: int = Field(description="The ID of the link.")
    name: Optional[str] = Field(None, description="The name of the link.")
    url: Optional[str] = Field(None, description="The URL of the link.")
    direct_asset_path: Optional[str] = Field(None, description="Optional path for a direct asset link.")
    link_type: Optional[str] = Field(None, description="The type of the link: other, runbook, image, package. Defaults to other.")

@action_store.kubiya_action()
def update_a_release_link(input: ReleaseLinkUpdate):
    return put_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/assets/links/{input.link_id}", args=input.dict(exclude_none=True))

class ReleaseLinkDelete(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    tag_name: str = Field(description="The tag associated with the Release.")
    link_id: int = Field(description="The ID of the link.")

@action_store.kubiya_action()
def delete_a_release_link(input: ReleaseLinkDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/assets/links/{input.link_id}", args=input.dict(exclude_none=True))
