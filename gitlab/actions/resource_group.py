from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.resource_group import *
@action_store.kubiya_action()
def get_all_resource_group_for_a_project(input: ProjectResourceGroups):
    return get_wrapper(endpoint=f'/projects/{input.id}/resource_groups')
@action_store.kubiya_action()
def get_a_specific_resource_group(input: SingleResourceGroup):
    return get_wrapper(endpoint=f'/projects/{input.id}/resource_groups/{input.key}')
@action_store.kubiya_action()
def list_upcoming_jobs_for_a_specific_resource_group(input: ResourceGroupUpcomingJobs):
    return get_wrapper(endpoint=f'/projects/{input.id}/resource_groups/{input.key}/upcoming_jobs')
@action_store.kubiya_action()
def edit_an_existing_resource_group(input: UpdateResourceGroup):
    return put_wrapper(endpoint=f'/projects/{input.id}/resource_groups/{input.key}', args=input.dict(exclude_none=True))