from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.environments import *

from .. import action_store as action_store
from ..http_wrapper import *

@action_store.kubiya_action()
def list_environments(input: ProjectsIdEnvironments):
    response = get_wrapper(endpoint=f'/projects/{input.id}/environments', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def get_a_specific_environment(input: ProjectsIdEnvironmentsEnvironmentid):
    response = get_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environment_id}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def create_a_new_environment(input: ProjectsIdEnvironmentsCreate):
    response = post_wrapper(endpoint=f'/projects/{input.id}/environments', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def update_an_existing_environment(input: ProjectsIdEnvironmentsEnvironmentsid):
    response = put_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environments_id}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def delete_an_environment(input: ProjectsIdEnvironmentsEnvironmentidDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_multiple_stopped_review_apps(input: ProjectsIdEnvironmentsReviewapps):
    response = delete_wrapper(endpoint=f'/projects/{input.id}/environments/review_apps', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def stop_an_environment(input: ProjectsIdEnvironmentsEnvironmentidStop):
    response = post_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environment_id}/stop', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def stop_stale_environments(input: ProjectsIdEnvironmentsStopstale):
    response = post_wrapper(endpoint=f'/projects/{input.id}/environments/stop_stale', args=input.dict(exclude_none=True))
    return SingleDict(response=response)