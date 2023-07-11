from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectsIdRepositoryBranches(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    search: Optional[
        str] = None  # Return list of branches containing the search string. You can use ^term to find branches that begin with term, and term$ to find branches that end with term.
    regex: Optional[str] = None  # Return list of branches with names matching a re2 regular expression..


@action_store.kubiya_action()
def list_repository_branches(input: ProjectsIdRepositoryBranches):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/branches", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    branch: str  # URL-encoded name of the branch.


@action_store.kubiya_action()
def get_single_repository_branch(input: ProjectsIdRepositoryBranchesBranchSingle):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/branches/{input.branch}",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    branch: str  # The name of the branch
    ref: str  # Branch name or commit SHA to create branch from.


@action_store.kubiya_action()
def create_repository_branch(input: ProjectsIdRepositoryBranchesCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/branches", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    branch: str  # The name of the branch


@action_store.kubiya_action()
def delete_repository_branch(input: ProjectsIdRepositoryBranchesBranch):
    return delete_wrapper(endpoint=f"/projects/{input.id}/repository/branches/{input.branch}",
                          args=input.dict(exclude_none=True))


class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user


@action_store.kubiya_action()
def delete_merged_branches(input: ProjectsIdRepositoryMergedbranches):
    return delete_wrapper(endpoint=f"/projects/{input.id}/repository/merged_branches",
                          args=input.dict(exclude_none=True))
