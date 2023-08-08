from typing import List, Any, Optional, Union
from pydantic import BaseModel
from datetime import datetime
from ..models.commits import *

from .. import action_store as action_store
from ..http_wrapper import *

@action_store.kubiya_action()
def list_repository_commits(input: ProjectsIdRepositoryCommits):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def get_a_single_commit(input: ProjectsIdRepositoryCommitsSha):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)


# @action_store.kubiya_action()
# def get_references_a_commit_is_pushed_to(input: ProjectsIdRepositoryCommitsShaRefs):
#     response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/refs', args=input.dict(exclude_none=True))
#     return ListDict(response=response)

# @action_store.kubiya_action()
# def cherry_pick_a_commit(input: ProjectsIdRepositoryCommitsShaCherrypick):
#     response = post_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/cherry_pick', args=input.dict(exclude_none=True))
#     return SingleDict(response=response)

@action_store.kubiya_action()
def revert_a_commit(input: ProjectsIdRepositoryCommitsShaRevert):
    response = post_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/revert', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def get_the_diff_of_a_commit(input: ProjectsIdRepositoryCommitsShaDiff):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/diff', args=input.dict(exclude_none=True))
    return ListDict(response=response)

# @action_store.kubiya_action()
# def get_the_comments_of_a_commit(input: ProjectsIdRepositoryCommitsShaComments):
#     response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/comments', args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def post_comment_to_commit(input: ProjectsIdRepositoryCommitsShaCommentsPost):
    response = post_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/comments', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def get_the_discussions_of_a_commit(input: ProjectsIdRepositoryCommitsShaDiscussions):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/discussions', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def list_the_statuses_of_a_commit(input: ProjectsIdRepositoryCommitsShaStatuses):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/statuses', args=input.dict(exclude_none=True))
    return ListDict(response=response)

# @action_store.kubiya_action()
# def set_the_pipeline_status_of_a_commit(input: ProjectsIdStatusesSha):
#     response = post_wrapper(endpoint=f'/projects/{input.id}/statuses/{input.sha}', args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def list_merge_requests_associated_with_a_commit(input: ProjectsIdRepositoryCommitsShaMergerequests):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/merge_requests', args=input.dict(exclude_none=True))
    return ListDict(response=response)    

@action_store.kubiya_action()
def get_gpg_signature_of_a_commit(input: ProjectsIdRepositoryCommitsShaSignature):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.sha}/signature', args=input.dict(exclude_none=True))
    return SingleDict(response=response)