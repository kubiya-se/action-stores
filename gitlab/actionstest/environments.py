from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.environments import *
@action_store.kubiya_action()
def list_environments(input: ProjectsIdEnvironments):
    return get_wrapper(endpoint=f'/projects/{input.id}/environments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_specific_environment(input: ProjectsIdEnvironmentsEnvironmentid):
    return get_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_new_environment(input: ProjectsIdEnvironmentsCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/environments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_an_existing_environment(input: ProjectsIdEnvironmentsEnvironmentsid):
    return put_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environments_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_an_environment(input: ProjectsIdEnvironmentsEnvironmentidDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_multiple_stopped_review_apps(input: ProjectsIdEnvironmentsReviewapps):
    return delete_wrapper(endpoint=f'/projects/{input.id}/environments/review_apps', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def stop_an_environment(input: ProjectsIdEnvironmentsEnvironmentidStop):
    return post_wrapper(endpoint=f'/projects/{input.id}/environments/{input.environment_id}/stop', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def stop_stale_environments(input: ProjectsIdEnvironmentsStopstale):
    return post_wrapper(endpoint=f'/projects/{input.id}/environments/stop_stale', args=input.dict(exclude_none=True))