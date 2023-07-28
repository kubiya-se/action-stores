from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.milestones_project import *
@action_store.kubiya_action()
def list_project_milestones(input: ProjectMilestonesGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/milestones', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_project_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}')
@action_store.kubiya_action()
def create_new_project_milestone(input: ProjectMilestoneCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/milestones', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_project_milestone(input: ProjectMilestoneUpdate):
    return put_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_project_milestone(input: ProjectMilestoneDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}')
@action_store.kubiya_action()
def get_all_issues_assigned_to_a_single_project_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}/issues')
@action_store.kubiya_action()
def get_all_merge_requests_assigned_to_a_single_project_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}/merge_requests')
@action_store.kubiya_action()
def promote_project_milestone_to_a_group_milestone(input: SingleProjectMilestoneGet):
    return post_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}/promote')
@action_store.kubiya_action()
def get_all_burndown_chart_events_for_a_single_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/milestones/{input.milestone_id}/burndown_events')