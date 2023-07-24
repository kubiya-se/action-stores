from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class GroupActivityIssuesCount(BaseModel):
    group_path: str = Field(description="Group path")

@action_store.kubiya_action()
def get_count_of_recently_created_issues_for_group(input: GroupActivityIssuesCount):
    return get_wrapper(endpoint="/analytics/group_activity/issues_count", args=input.dict(exclude_none=True))

class GroupActivityMergeRequestsCount(BaseModel):
    group_path: str = Field(description="Group path")

@action_store.kubiya_action()
def get_count_of_recently_created_merge_requests_for_group(input: GroupActivityMergeRequestsCount):
    return get_wrapper(endpoint="/analytics/group_activity/merge_requests_count", args=input.dict(exclude_none=True))

class GroupActivityNewMembersCount(BaseModel):
    group_path: str = Field(description="Group path")

@action_store.kubiya_action()
def get_count_of_members_recently_added_to_a_group(input: GroupActivityNewMembersCount):
    return get_wrapper(endpoint="/analytics/group_activity/new_members_count", args=input.dict(exclude_none=True))
