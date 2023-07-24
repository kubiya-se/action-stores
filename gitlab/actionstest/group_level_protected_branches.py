from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.group_level_protected_branches import *
@action_store.kubiya_action()
def list_protected_branches(input: GroupProtectedBranchesGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/protected_branches', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_single_protected_branch_or_wildcard_protected_branch(input: GroupProtectedBranchGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/protected_branches/{input.name}')
@action_store.kubiya_action()
def protect_repository_branches(input: GroupProtectedBranchesPost):
    return post_wrapper(endpoint=f'/groups/{input.id}/protected_branches', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def unprotect_repositor_branches(input: GroupProtectedBranchesDelete):
    return delete_wrapper(endpoint=f'/groups/{input.id}/protected_branches/{input.name}')
@action_store.kubiya_action()
def update_a_protected_branch(input: GroupProtectedBranchesPatch):
    return patch_wrapper(endpoint=f'/groups/{input.id}/protected_branches/{input.name}', args=input.dict(exclude_none=True))