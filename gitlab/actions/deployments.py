from typing import List, Any, Optional, Union, Dict
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime, timedelta


class ListProjectDeployments(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    order_by: Optional[str] = None  # Return deployments ordered by either one of id, iid, created_at, updated_at, finished_at or ref fields. Default is id.

    sort: Optional[str] = None  # Return deployments sorted in asc or desc order. Default is asc.

    updated_after: Optional[datetime] = None  # Return deployments updated after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    updated_before: Optional[datetime] = None  # Return deployments updated before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    finished_after: Optional[datetime] = None  # Return deployments finished after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    finished_before: Optional[datetime] = None  # Return deployments finished before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    environment: Optional[str] = None  # The name of the environment to filter deployments by.

    status: Optional[str] = None  # The status to filter deployments by. One of created, running, success, failed, canceled, or blocked.


@action_store.kubiya_action()
def list_project_deployments(input: ListProjectDeployments):
    print(input.dict(exclude_none = True))
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))


class GetASpecificDeployment(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    deployment_id: int  # The ID of the deployment


@action_store.kubiya_action()
def get_a_specific_deployment(input: GetASpecificDeployment):
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments/{input.deployment_id}",
                       args=input.dict(exclude_none=True))



class GetDeploymentFrequency(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.
    finished_after: Optional[datetime] = None  # Return deployments finished after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

@action_store.kubiya_action()
def get_deployment_frequency(input: GetDeploymentFrequency):
    deployments = get_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))
    current_time = datetime.now()
    
    if input.finished_after is None:
        last_day = current_time - timedelta(days=1)
    else:
        last_day = input.finished_after
    
    count = 0

    for deployment in deployments:
        finished_at = datetime.fromisoformat(deployment["deployable"]["finished_at"])
        if last_day <= finished_at <= current_time:
            count += 1

    return count


class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime

def calculate_deployment_duration(deployment: DeploymentDuration):
    duration = deployment.finished_at - deployment.created_at
    return duration.total_seconds()


class ListProjectDeployment(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    order_by: Optional[str] = None  # Return deployments ordered by either one of id, iid, created_at, updated_at, finished_at or ref fields. Default is id.

    sort: Optional[str] = None  # Return deployments sorted in asc or desc order. Default is asc.

    updated_after: Optional[datetime] = None  # Return deployments updated after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    updated_before: Optional[datetime] = None  # Return deployments updated before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    finished_after: Optional[datetime] = None  # Return deployments finished after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    finished_before: Optional[datetime] = None  # Return deployments finished before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    environment: Optional[str] = None  # The name of the environment to filter deployments by.

    status: Optional[str] = None  # The status to filter deployments by. One of created, running, success, failed, canceled, or blocked.


@action_store.kubiya_action()
def list_project_deployments(input: ListProjectDeployment):
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))

class ProjectsIdDeploymentsCreate(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    environment: str  # The name of the environment to create the deployment for.

    sha: str  # The SHA of the commit that is deployed.

    ref: str  # The name of the branch or tag that is deployed.

    tag: bool  # A boolean that indicates if the deployed ref is a tag (true) or not (false).

    status: str  # The status to filter deployments by. One of running, success, failed, or canceled.


@action_store.kubiya_action()
def create_a_deployment(input: ProjectsIdDeploymentsCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))

class ProjectsIdDeployments(BaseModel):

    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    order_by: Optional[str] = None  # Return deployments ordered by either one of id, iid, created_at, updated_at, finished_at or ref fields. Default is id.

    sort: Optional[str] = None  # Return deployments sorted in asc or desc order. Default is asc.

    updated_after: Optional[datetime] = None  # Return deployments updated after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    updated_before: Optional[datetime] = None  # Return deployments updated before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    finished_after: Optional[datetime] = None  # Return deployments finished after the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    finished_before: Optional[datetime] = None  # Return deployments finished before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

    environment: Optional[str] = None  # The name of the environment to filter deployments by.

    status: Optional[str] = None  # The status to filter deployments by. One of created, running, success, failed, canceled, or blocked.


@action_store.kubiya_action()
def list_project_deployments(input: ProjectsIdDeployments):
    dict_input = input.dict(exclude_none=True)
    print(f"dict_input: {dict_input}")
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))


class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    deployment_id: int  # The ID of the deployment


@action_store.kubiya_action()
def get_a_specific_deployment(input: ProjectsIdDeploymentsDeploymentid):
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments/{input.deployment_id}",
                       args=input.dict(exclude_none=True))


class CreateADeployment(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    environment: str  # The name of the environment to create the deployment for.

    sha: str  # The SHA of the commit that is deployed.

    ref: str  # The name of the branch or tag that is deployed.

    tag: bool  # A boolean that indicates if the deployed ref is a tag (true) or not (false).

    status: str  # The status to filter deployments by. One of running, success, failed, or canceled.


@action_store.kubiya_action()
def create_a_deployment(input: CreateADeployment):
    return post_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))


class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    deployment_id: int  # The ID of the deployment to update.

    status: str  # The new status of the deployment. One of running, success, failed, or canceled.


@action_store.kubiya_action()
def update_a_deployment(input: ProjectsIdDeploymentsDeploymentidUpdate):
    return put_wrapper(endpoint=f"/projects/{input.id}/deployments/{input.deployment_id}",
                       args=input.dict(exclude_none=True))


class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user

    deployment_id: int  # The ID of the deployment


@action_store.kubiya_action()
def delete_a_specific_deployment(input: ProjectsIdDeploymentsDeploymentidDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/deployments/{input.deployment_id}",
                          args=input.dict(exclude_none=True))


class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.
    deployment_id: int  # The ID of the deployment.


@action_store.kubiya_action()
def list_of_merge_requests_associated_with_a_deployment(input: ProjectsIdDeploymentsDeploymentidMergerequests):
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments/{input.deployment_id}/merge_requests",
                       args=input.dict(exclude_none=True))


class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user.

    deployment_id: int  # The ID of the deployment.

    status: str  # The status of the approval (either approved or rejected).

    comment: Optional[str] = None  # A comment to go with the approval

    represented_as: Optional[str] = None  # The name of the User/Group/Role to use for the approval, when the user belongs to multiple approval rules.


@action_store.kubiya_action()
def approve_or_reject_a_blocked_deployment_(input: ProjectsIdDeploymentsDeploymentidApproval):
    return post_wrapper(endpoint=f"/projects/{input.id}/deployments/{input.deployment_id}/approval",
                        args=input.dict(exclude_none=True))
