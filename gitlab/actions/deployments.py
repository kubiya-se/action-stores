from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.deployments import *
@action_store.kubiya_action()
def list_project_deployments(input: ListProjectDeployments):
    print(input.dict(exclude_none=True))
    return get_wrapper(endpoint=f'/projects/{input.id}/deployments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_specific_deployment(input: GetASpecificDeployment):
    return get_wrapper(endpoint=f'/projects/{input.id}/deployments/{input.deployment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_deployment_frequency(input: GetDeploymentFrequency):
    deployments = get_wrapper(endpoint=f'/projects/{input.id}/deployments', args=input.dict(exclude_none=True))
    current_time = datetime.now()
    if input.finished_after is None:
        last_day = current_time - timedelta(days=1)
    else:
        last_day = input.finished_after
    count = 0
    for deployment in deployments:
        finished_at = datetime.fromisoformat(deployment['deployable']['finished_at'])
        if last_day <= finished_at <= current_time:
            count += 1
    return count
@action_store.kubiya_action()
def list_project_deployments(input: ListProjectDeployment):
    return get_wrapper(endpoint=f'/projects/{input.id}/deployments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_deployment(input: ProjectsIdDeploymentsCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/deployments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_deployments(input: ProjectsIdDeployments):
    dict_input = input.dict(exclude_none=True)
    print(f'dict_input: {dict_input}')
    return get_wrapper(endpoint=f'/projects/{input.id}/deployments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_specific_deployment(input: ProjectsIdDeploymentsDeploymentid):
    return get_wrapper(endpoint=f'/projects/{input.id}/deployments/{input.deployment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_deployment(input: CreateADeployment):
    return post_wrapper(endpoint=f'/projects/{input.id}/deployments', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_deployment(input: ProjectsIdDeploymentsDeploymentidUpdate):
    return put_wrapper(endpoint=f'/projects/{input.id}/deployments/{input.deployment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_specific_deployment(input: ProjectsIdDeploymentsDeploymentidDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/deployments/{input.deployment_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_of_merge_requests_associated_with_a_deployment(input: ProjectsIdDeploymentsDeploymentidMergerequests):
    return get_wrapper(endpoint=f'/projects/{input.id}/deployments/{input.deployment_id}/merge_requests', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def approve_or_reject_a_blocked_deployment_(input: ProjectsIdDeploymentsDeploymentidApproval):
    return post_wrapper(endpoint=f'/projects/{input.id}/deployments/{input.deployment_id}/approval', args=input.dict(exclude_none=True))