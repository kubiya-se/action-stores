from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.runners import *
@action_store.kubiya_action()
def list_owned_runners(input: RunnerFilter):
    return get_wrapper(endpoint='/runners', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_all_runners(input: RunnerFilter):
    return get_wrapper(endpoint='/runners/all', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_runner_details(input: RunnerId):
    return get_wrapper(endpoint=f'/runners/{input.id}')
@action_store.kubiya_action()
def update_runner_details(input: RunnerUpdate):
    return put_wrapper(endpoint=f'/runners/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def pause_runner(input: RunnerPause):
    return put_wrapper(endpoint=f'/runners/{input.runner_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_runner_jobs(input: RunnerJobsFilter):
    return get_wrapper(endpoint=f'/runners/{input.id}/jobs', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_runners(input: ProjectRunnersFilter):
    return get_wrapper(endpoint=f'/projects/{input.id}/runners', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def enable_runner_in_project(input: EnableRunnerInProject):
    return post_wrapper(endpoint=f'/projects/{input.id}/runners', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def disable_runner_from_project(input: DisableRunnerFromProject):
    return delete_wrapper(endpoint=f'/projects/{input.id}/runners/{input.runner_id}')
@action_store.kubiya_action()
def list_group_runners(input: GroupRunnersFilter):
    return get_wrapper(endpoint=f'/groups/{input.id}/runners', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def register_new_runner(input: RegisterRunner):
    return post_wrapper(endpoint='/runners', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_runner_by_id(input: RunnerId):
    return delete_wrapper(endpoint=f'/runners/{input.id}')
@action_store.kubiya_action()
def delete_runner_by_token(input: RunnerToken):
    return delete_wrapper(endpoint='/runners', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def verify_runner_authentication(input: VerifyRunnerAuthentication):
    return post_wrapper(endpoint='/runners/verify', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def reset_instance_runner_registration_token():
    return post_wrapper(endpoint='/runners/reset_registration_token')
@action_store.kubiya_action()
def reset_project_runner_registration_token(input: ProjectId):
    return post_wrapper(endpoint=f'/projects/{input.id}/runners/reset_registration_token')
@action_store.kubiya_action()
def reset_group_runner_registration_token(input: ProjectId):
    return post_wrapper(endpoint=f'/groups/{input.id}/runners/reset_registration_token')
@action_store.kubiya_action()
def reset_runner_authentication_token_by_id(input: RunnerId):
    return post_wrapper(endpoint=f'/runners/{input.id}/reset_authentication_token')
@action_store.kubiya_action()
def reset_runner_authentication_token_by_token(input: RunnerToken):
    return post_wrapper(endpoint='/runners/reset_authentication_token', args=input.dict(exclude_none=True))