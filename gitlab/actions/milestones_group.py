from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.milestones_group import *
@action_store.kubiya_action()
def list_group_milestones(input: GroupMilestonesGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/milestones', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/milestones/{input.milestone_id}')
@action_store.kubiya_action()
def create_new_group_milestone(input: GroupMilestoneCreate):
    return post_wrapper(endpoint=f'/groups/{input.id}/milestones', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_group_milestone(input: GroupMilestoneUpdate):
    return put_wrapper(endpoint=f'/groups/{input.id}/milestones/{input.milestone_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_group_milestone(input: GroupMilestoneDelete):
    return delete_wrapper(endpoint=f'/groups/{input.id}/milestones/{input.milestone_id}')
@action_store.kubiya_action()
def get_all_issues_assigned_to_a_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/milestones/{input.milestone_id}/issues')
@action_store.kubiya_action()
def get_all_merge_requests_assigned_to_a_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/milestones/{input.milestone_id}/merge_requests')
@action_store.kubiya_action()
def get_all_burndown_chart_events_for_a_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/milestones/{input.milestone_id}/burndown_events')