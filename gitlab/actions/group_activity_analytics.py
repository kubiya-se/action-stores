from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.group_activity_analytics import *
@action_store.kubiya_action()
def get_count_of_recently_created_issues_for_group(input: GroupActivityIssuesCount):
    return get_wrapper(endpoint='/analytics/group_activity/issues_count', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_count_of_recently_created_merge_requests_for_group(input: GroupActivityMergeRequestsCount):
    return get_wrapper(endpoint='/analytics/group_activity/merge_requests_count', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_count_of_members_recently_added_to_a_group(input: GroupActivityNewMembersCount):
    return get_wrapper(endpoint='/analytics/group_activity/new_members_count', args=input.dict(exclude_none=True))