from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ProtectedTagsList(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")

@action_store.kubiya_action()
def list_protected_tags(input: ProtectedTagsList):
    return get_wrapper(endpoint=f"/projects/{input.id}/protected_tags", args=input.dict(exclude_none=True))

class SingleProtectedTag(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    name: str = Field(description="The name of the tag or wildcard.")

@action_store.kubiya_action()
def get_a_single_protected_tag_or_wildcard_protected_tag(input: SingleProtectedTag):
    return get_wrapper(endpoint=f"/projects/{input.id}/protected_tags/{input.name}", args=input.dict(exclude_none=True))

class CreateAccess(BaseModel):
    user_id: Optional[int] = None
    access_level: Optional[int] = None

class ProtectRepositoryTags(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    name: str = Field(description="The name of the tag or wildcard.")
    allowed_to_create: Optional[List[CreateAccess]] = None
    create_access_level: Optional[int] = Field(None, description="Access levels allowed to create. Default: 40, for Maintainer role.")

@action_store.kubiya_action()
def protect_repository_tags(input: ProtectRepositoryTags):
    return post_wrapper(endpoint=f"/projects/{input.id}/protected_tags", args=input.dict(exclude_none=True))

class UnprotectRepositoryTags(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    name: str = Field(description="The name of the tag.")

@action_store.kubiya_action()
def unprotect_repository_tags(input: UnprotectRepositoryTags):
    return delete_wrapper(endpoint=f"/projects/{input.id}/protected_tags/{input.name}", args=input.dict(exclude_none=True))
