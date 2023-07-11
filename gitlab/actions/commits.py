from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectsIdRepositoryCommits(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    ref_name: Optional[str] = None  # The name of a repository branch, tag or revision range, or if not given the default branch

    since: Optional[str] = None  # Only commits after or on this date are returned in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ

    until: Optional[str] = None  # Only commits before or on this date are returned in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ

    path: Optional[str] = None  # The file path

    author: Optional[str] = None  # Search commits by commit author.

    all: Optional[bool]  # Retrieve every commit from the repository

    with_stats: Optional[bool]   # Stats about each commit are added to the response

    first_parent: Optional[bool]  # Follow only the first parent commit upon seeing a merge commit

    order: Optional[str]  # List commits in order. Possible values: default, topo. Defaults to default, the commits are shown in reverse chronological order.

    trailers: Optional[bool]   # Parse and include Git trailers for every commit


@action_store.kubiya_action()
def list_repository_commits(input: ProjectsIdRepositoryCommits):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits", args=input.dict(exclude_none=True))


# TODO
# class ProjectsIdRepositoryCommitsCreate(BaseModel):
#
#     id: int # The ID or URL-encoded path of the project
#
#     branch: str # Name of the branch to commit into. To create a new branch, also provide either start_branch or start_sha, and optionally start_project.
#
#     commit_message: str # Commit message
#
#     start_branch: Optional[str] = None # Name of the branch to start the new branch from
#
#     start_sha: Optional[str] = None # SHA of the commit to start the new branch from
#
#     start_project: Optional[int] = None # The project ID or URL-encoded path of the project to start the new branch from. Defaults to the value of id.
#
#     actions[]: array # An array of action hashes to commit as a batch. See the next table for what attributes it can take.
#
#     author_email: Optional[str] = None # Specify the commit author’s email address
#
#     author_name: Optional[str] = None # Specify the commit author’s name
#
#     stats: Optional[bool] = None # Include commit stats. Default is true
#
#     force: Optional[bool] = None # When true overwrites the target branch with a new commit based on the start_branch or start_sha
#
#
# @action_store.kubiya_action()
# def create_a_commit_with_multiple_files_and_actions(input: ProjectsIdRepositoryCommitsCreate):
#     return post_wrapper(endpoint=f"/projects/{input.id}/repository/commits", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash or name of a repository branch or tag
    stats: Optional[bool] = None  # Include commit stats. Default is true


@action_store.kubiya_action()
def get_a_single_commit(input: ProjectsIdRepositoryCommitsSha):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash or name of a repository branch or tag
    type: Optional[str] = None  # The scope of commits. Possible values branch, tag, all. Default is all.


@action_store.kubiya_action()
def get_references_a_commit_is_pushed_to(input: ProjectsIdRepositoryCommitsShaRefs):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/refs",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash
    branch: str  # The name of the branch
    dry_run: Optional[bool] = None  # Does not commit any changes. Default is false. Introduced in GitLab 13.3
    message: Optional[str] = None  # A custom commit message to use for the new commit. Introduced in GitLab 14.0


@action_store.kubiya_action()
def cherry_pick_a_commit(input: ProjectsIdRepositoryCommitsShaCherrypick):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/cherry_pick",
                        args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash
    branch: str  # The name of the branch
    dry_run: Optional[bool] = None  # Does not commit any changes. Default is false. Introduced in GitLab 13.3


@action_store.kubiya_action()
def revert_a_commit(input: ProjectsIdRepositoryCommitsShaRevert):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/revert",
                        args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash or name of a repository branch or tag


@action_store.kubiya_action()
def get_the_diff_of_a_commit(input: ProjectsIdRepositoryCommitsShaDiff):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/diff",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash or name of a repository branch or tag


@action_store.kubiya_action()
def get_the_comments_of_a_commit(input: ProjectsIdRepositoryCommitsShaComments):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/comments",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    sha: str  # The commit SHA or name of a repository branch or tag

    note: str  # The text of the comment

    path: Optional[str] = None  # The file path relative to the repository

    line: Optional[int] = None  # The line number where the comment should be placed

    line_type: Optional[str] = None  # The line type. Takes new or old as arguments


@action_store.kubiya_action()
def post_comment_to_commit(input: ProjectsIdRepositoryCommitsShaCommentsPost):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/comments",
                        args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash or name of a repository branch or tag


@action_store.kubiya_action()
def get_the_discussions_of_a_commit(input: ProjectsIdRepositoryCommitsShaDiscussions):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/discussions",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    sha: str  # The commit SHA

    ref: Optional[str] = None  # The name of a repository branch or tag or, if not given, the default branch

    stage: Optional[str] = None  # Filter by build stage, for example, test

    name: Optional[str] = None  # Filter by job name, for example, bundler:audit

    all: Optional[bool] = None  # Return all statuses, not only the latest ones


@action_store.kubiya_action()
def list_the_statuses_of_a_commit(input: ProjectsIdRepositoryCommitsShaStatuses):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/statuses",
                       args=input.dict(exclude_none=True))


class ProjectsIdStatusesSha(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    sha: str  # The commit SHA

    state: str  # The state of the status. Can be one of the following: pending, running, success, failed, canceled

    ref: Optional[str] = None  # The ref (branch or tag) to which the status refers

    context: Optional[str] = None  # The label to differentiate this status from the status of other systems. Default value is default

    name: Optional[str] = None  # The label to differentiate this status from the status of other systems. Default value is default

    target_url: Optional[str] = None  # The target URL to associate with this status

    description: Optional[str] = None  # The short description of the status

    coverage: Optional[float] = None  # The total code coverage

    pipeline_id: Optional[
        int] = None  # The ID of the pipeline to set status. Use in case of several pipeline on same SHA.


@action_store.kubiya_action()
def set_the_pipeline_status_of_a_commit(input: ProjectsIdStatusesSha):
    return post_wrapper(endpoint=f"/projects/{input.id}/statuses/{input.sha}", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit SHA


@action_store.kubiya_action()
def list_merge_requests_associated_with_a_commit(input: ProjectsIdRepositoryCommitsShaMergerequests):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/merge_requests",
                       args=input.dict(exclude_none=True))


class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    sha: str  # The commit hash or name of a repository branch or tag


@action_store.kubiya_action()
def get_gpg_signature_of_a_commit(input: ProjectsIdRepositoryCommitsShaSignature):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.sha}/signature",
                       args=input.dict(exclude_none=True))
