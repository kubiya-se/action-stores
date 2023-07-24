from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from enum import Enum

class GroupProtectedBranchesGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user.")
    search: Optional[str] = None

@action_store.kubiya_action()
def list_protected_branches(input: GroupProtectedBranchesGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/protected_branches", args=input.dict(exclude_none=True))

class GroupProtectedBranchGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user.")
    name: str = Field(description="The name of the branch or wildcard.")

@action_store.kubiya_action()
def get_a_single_protected_branch_or_wildcard_protected_branch(input: GroupProtectedBranchGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/protected_branches/{input.name}")


class ValidAccessLevels(int, Enum):
    No_access = 0
    Developer_access = 30
    Maintainer_access = 40
    Admin_access = 60


class AccessLevel(BaseModel):
    user_id: Optional[int] = ValidAccessLevels
    group_id: Optional[int] = ValidAccessLevels
    access_level: Optional[int] = ValidAccessLevels

class GroupProtectedBranchesPost(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user.")
    name: str = Field(description="The name of the branch or wildcard.")
    allow_force_push: Optional[bool] = None
    allowed_to_push: Optional[List[AccessLevel]] = None
    allowed_to_merge: Optional[List[AccessLevel]] = None
    allowed_to_unprotect: Optional[List[AccessLevel]] = None
    code_owner_approval_required: Optional[bool] = None
    merge_access_level: Optional[AccessLevel] = None
    push_access_level: Optional[AccessLevel] = None
    unprotect_access_level: Optional[AccessLevel] = None

@action_store.kubiya_action()
def protect_repository_branches(input: GroupProtectedBranchesPost):
    return post_wrapper(endpoint=f"/groups/{input.id}/protected_branches", args=input.dict(exclude_none=True))

class GroupProtectedBranchesDelete(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user.")
    name: str = Field(description="The name of the branch.")

@action_store.kubiya_action()
def unprotect_repositor_branches(input: GroupProtectedBranchesDelete):
    return delete_wrapper(endpoint=f"/groups/{input.id}/protected_branches/{input.name}")

class GroupProtectedBranchesPatch(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user.")
    name: str = Field(description="The name of the branch.")
    allow_force_push: Optional[bool] = None
    allowed_to_push: Optional[List[AccessLevel]] = None
    allowed_to_merge: Optional[List[AccessLevel]] = None
    allowed_to_unprotect: Optional[List[AccessLevel]] = None
    code_owner_approval_required: Optional[bool] = None

@action_store.kubiya_action()
def update_a_protected_branch(input: GroupProtectedBranchesPatch):
    return patch_wrapper(endpoint=f"/groups/{input.id}/protected_branches/{input.name}", args=input.dict(exclude_none=True))
