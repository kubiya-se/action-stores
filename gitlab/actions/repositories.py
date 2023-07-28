from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field, parse_object_as
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.repositories import *

class Repository(BaseModel):
    id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    path: Optional[str]
    mode: Optional[str]

@action_store.kubiya_action()
def list_repository_tree(input: ProjectsIdRepositoryTree):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/tree', args=input.dict(exclude_none=True))
    return parse_object_as(List[Repository], response)
@action_store.kubiya_action()
def get_a_blob_from_repository(input: ProjectsIdRepositoryBlobsSha):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/blobs/{input.sha}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def raw_blob_content(input: ProjectsIdRepositoryBlobsShaRaw):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/blobs/{input.sha}/raw', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_file_archive(input: ProjectsIdRepositoryArchive):
    format_suffix = f'.{input.format}' if input.format else ''
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/archive{format_suffix}', args=input.dict(exclude_none=True))

class Commit(BaseModel):
    id: str
    short_id: str
    title: str
    author_name: str
    author_email: str
    created_at: str

class Diff(BaseModel):
    old_path: str
    new_path: str
    a_mode: Optional[str] = None
    b_mode: str
    diff: str
    new_file: bool
    renamed_file: bool
    deleted_file: bool

class Compare(BaseModel):
    commit: Commit
    commits: List[Commit]
    diffs: List[Diff]
    compare_timeout: bool
    compare_same_ref: bool
    web_url: str

@action_store.kubiya_action()
def compare_branches_tags_or_commits(input: ProjectsIdRepositoryCompare):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/repository/compare', args=input.dict(exclude_none=True, by_alias=True))
    return parse_object_as(Compare, response)


class User(BaseModel):
    name: str
    email: str
    commits: int
    additions: int
    deletions: int

class Users(BaseModel):
    users: List[User]

@action_store.kubiya_action()
def contributors(input: ProjectsIdRepositoryContributors):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/contributors', args=input.dict(exclude_none=True))
    return parse_object_as(Users,response)


class MergeBase(BaseModel):
    id: str
    short_id: str
    title: str
    created_at: str
    parent_ids: List[str]
    message: str
    author_name: str
    author_email: str
    authored_date: str
    committer_name: str
    committer_email: str
    committed_date: str


@action_store.kubiya_action()
def get_merge_base(input: ProjectsIdRepositoryMergebase):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/merge_base', params={'refs[]': input.refs})
    return parse_object_as(MergeBase, response)

@action_store.kubiya_action()
def add_changelog_data_to_a_changelog_file(input: ProjectsIdRepositoryChangelog):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/changelog', args=input.dict(by_alias=True, exclude_none=True))
@action_store.kubiya_action()
def generate_changelog_data(input: GenerateChangelogData):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/changelog', args=input.dict(by_alias=True, exclude_none=True))