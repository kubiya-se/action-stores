from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectsIdEnvironments(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    name: Optional[str] = None  # Return the environment with this name. Mutually exclusive with search.

    search: Optional[
        str] = None  # Return list of environments matching the search criteria. Mutually exclusive with name. Must be at least 3 characters long.

    states: Optional[
        str] = None  # List all environments that match a specific state. Accepted values: available, stopping, or stopped. If no state value given, returns all environments.


@action_store.kubiya_action()
def list_environments(input: ProjectsIdEnvironments):
    return get_wrapper(endpoint=f"/projects/{input.id}/environments", args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    environment_id: int  # The ID of the environment.


@action_store.kubiya_action()
def get_a_specific_environment(input: ProjectsIdEnvironmentsEnvironmentid):
    return get_wrapper(endpoint=f"/projects/{input.id}/environments/{input.environment_id}",
                       args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    name: str  # The name of the environment.

    external_url: Optional[str] = None  # Place to link to for this environment.

    tier: Optional[str] = None  # The tier of the new environment. Allowed values are production, staging, testing, development, and other.


@action_store.kubiya_action()
def create_a_new_environment(input: ProjectsIdEnvironmentsCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/environments", args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    environment_id: int  # The ID of the environment.

    external_url: Optional[str] = None  # The new external_url.

    tier: Optional[
        str] = None  # The tier of the new environment. Allowed values are production, staging, testing, development, and other.


@action_store.kubiya_action()
def update_an_existing_environment(input: ProjectsIdEnvironmentsEnvironmentsid):
    return put_wrapper(endpoint=f"/projects/{input.id}/environments/{input.environments_id}",
                       args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    environment_id: int  # The ID of the environment.


@action_store.kubiya_action()
def delete_an_environment(input: ProjectsIdEnvironmentsEnvironmentidDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/environments/{input.environment_id}",
                          args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    before: Optional[
        datetime] = None  # The date before which environments can be deleted. Defaults to 30 days ago. Expected in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).

    limit: Optional[int] = None  # Maximum number of environments to delete. Defaults to 100.

    dry_run: Optional[bool] = None  # Defaults to true for safety reasons. It performs a dry run where no actual deletion is performed. Set to false to actually delete the environment.


@action_store.kubiya_action()
def delete_multiple_stopped_review_apps(input: ProjectsIdEnvironmentsReviewapps):
    return delete_wrapper(endpoint=f"/projects/{input.id}/environments/review_apps", args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    environment_id: int  # The ID of the environment.

    force: Optional[bool] = None  # Force environment to stop without executing on_stop actions.


@action_store.kubiya_action()
def stop_an_environment(input: ProjectsIdEnvironmentsEnvironmentidStop):
    return post_wrapper(endpoint=f"/projects/{input.id}/environments/{input.environment_id}/stop",
                        args=input.dict(exclude_none=True))


class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int  # The ID or URL-encoded path of the project.

    before: datetime  # Stop environments that have been modified or deployed to before the specified date. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Valid inputs are between 10 years ago and 1 week ago


@action_store.kubiya_action()
def stop_stale_environments(input: ProjectsIdEnvironmentsStopstale):
    return post_wrapper(endpoint=f"/projects/{input.id}/environments/stop_stale", args=input.dict(exclude_none=True))
