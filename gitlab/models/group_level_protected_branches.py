from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GroupProtectedBranchesGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user.')
    search: Optional[str] = None
class GroupProtectedBranchGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user.')
    name: str = Field(description='The name of the branch or wildcard.')
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
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user.')
    name: str = Field(description='The name of the branch or wildcard.')
    allow_force_push: Optional[bool] = None
    allowed_to_push: Optional[List[AccessLevel]] = None
    allowed_to_merge: Optional[List[AccessLevel]] = None
    allowed_to_unprotect: Optional[List[AccessLevel]] = None
    code_owner_approval_required: Optional[bool] = None
    merge_access_level: Optional[AccessLevel] = None
    push_access_level: Optional[AccessLevel] = None
    unprotect_access_level: Optional[AccessLevel] = None
class GroupProtectedBranchesDelete(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user.')
    name: str = Field(description='The name of the branch.')
class GroupProtectedBranchesPatch(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user.')
    name: str = Field(description='The name of the branch.')
    allow_force_push: Optional[bool] = None
    allowed_to_push: Optional[List[AccessLevel]] = None
    allowed_to_merge: Optional[List[AccessLevel]] = None
    allowed_to_unprotect: Optional[List[AccessLevel]] = None
    code_owner_approval_required: Optional[bool] = None