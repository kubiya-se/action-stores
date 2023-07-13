from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class ValidAccessLevels(int, Enum):
    No_access = 0
    Developer_access = 30
    Maintainer_access = 40
    Admin_access = 60


class AccessLevel(BaseModel):
    user_id: Optional[ValidAccessLevels] = None
    group_id: Optional[ValidAccessLevels] = None
    access_level: Optional[ValidAccessLevels] = None


class GroupProtectedBranchesPost(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user.")
    name: str = Field(description="The name of the branch or wildcard.")
    allow_force_push: Optional[bool] = None
    allowed_to_push: Optional[List[AccessLevel]] = None
    allowed_to_merge: Optional[List[AccessLevel]] = None
    allowed_to_unprotect: Optional[List[AccessLevel]] = None
    code_owner_approval_required: Optional[bool] = None
    merge_access_level: Optional[int] = None
    push_access_level: Optional[int] = None
    unprotect_access_level: Optional[int] = None

AccessInput = AccessLevel(user_id = 10, group_id = 10, access_level = 10)

BranchesInput = GroupProtectedBranchesPost(id = 10, name = "Hello", allow_force_push = True, allowed_to_push = [AccessInput])

print(BranchesInput.dict())