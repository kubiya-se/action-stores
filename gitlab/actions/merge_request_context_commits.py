from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class MergeRequestContextCommits(BaseModel):
    id: Union[int,str]
    merge_request_iid: int
    commits: Optional[List[str]] = None

@action_store.kubiya_action()
def list_merge_request_context_commits(input: MergeRequestContextCommits):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/context_commits", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def create_merge_request_context_commits(input: MergeRequestContextCommits):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/context_commits", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def delete_merge_request_context_commits(input: MergeRequestContextCommits):
    return delete_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/context_commits", args=input.dict(exclude_none=True))
