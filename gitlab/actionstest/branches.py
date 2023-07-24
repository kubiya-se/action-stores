from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.branches import *
@action_store.kubiya_action()
def list_repository_branches(input: ProjectsIdRepositoryBranches):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/branches', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_repository_branch(input: ProjectsIdRepositoryBranchesBranchSingle):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/branches/{input.branch}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_repository_branch(input: ProjectsIdRepositoryBranchesCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/branches', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_repository_branch(input: ProjectsIdRepositoryBranchesBranch):
    return delete_wrapper(endpoint=f'/projects/{input.id}/repository/branches/{input.branch}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_merged_branches(input: ProjectsIdRepositoryMergedbranches):
    return delete_wrapper(endpoint=f'/projects/{input.id}/repository/merged_branches', args=input.dict(exclude_none=True))