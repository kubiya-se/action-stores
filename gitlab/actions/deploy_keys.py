
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class Deploykeys(BaseModel):

    public: Optional[bool] = None # Only return deploy keys that are public. Defaults to false.
@action_store.kubiya_action()
def list_all_deploy_keys_(input: Deploykeys):
    return get_wrapper(endpoint=f"/deploy_keys", args=input.dict(exclude_none=True))


class ProjectsIdDeploykeys(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user


@action_store.kubiya_action()
def list_deploy_keys_for_project(input: ProjectsIdDeploykeys):
    return get_wrapper(endpoint=f"/projects/{input.id}/deploy_keys", args=input.dict(exclude_none=True))


class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str # The ID or username of the user

@action_store.kubiya_action()
def list_project_deploy_keys_for_user(input: UsersIdorusernameProjectdeploykeys):
    return get_wrapper(endpoint=f"/users/{input.id_or_username}/project_deploy_keys", args=input.dict(exclude_none=True))


class ProjectsIdDeploykeysKeyidSingle(BaseModel):

        id: int # The ID or URL-encoded path of the project owned by the authenticated user

        key_id: int # The ID of the deploy key

@action_store.kubiya_action()
def get_a_single_deploy_key(input: ProjectsIdDeploykeysKeyidSingle):
    return get_wrapper(endpoint=f"/projects/{input.id}/deploy_keys/{input.key_id}", args=input.dict(exclude_none=True))


class ProjectsIdDeploykeysAdd(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user

    key: str # New deploy key

    title: str # New deploy key’s title

    can_push: Optional[bool] = None # Can deploy key push to the project’s repository

    expires_at: Optional[datetime] = None # Expiration date for the deploy key. Does not expire if no value is provided. Expected in ISO 8601 format (2019-03-15T08:00:00Z)


@action_store.kubiya_action()
def add_deploy_key(input: ProjectsIdDeploykeysAdd):
    return post_wrapper(endpoint=f"/projects/{input.id}/deploy_keys", args=input.dict(exclude_none=True))


class ProjectsIdDeploykeysKeyidUpdate(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user

    can_push: Optional[bool] = None # Can deploy key push to the project’s repository

    title: Optional[str] = None # New deploy key’s title


@action_store.kubiya_action()
def update_deploy_key(input: ProjectsIdDeploykeysKeyidUpdate):
    return put_wrapper(endpoint=f"/projects/{input.id}/deploy_keys/{input.key_id}", args=input.dict(exclude_none=True))


class ProjectsIdDeploykeysKeyidDelete(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user

    key_id: int # The ID of the deploy key


@action_store.kubiya_action()
def delete_deploy_key(input: ProjectsIdDeploykeysKeyidDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/deploy_keys/{input.key_id}", args=input.dict(exclude_none=True))


class ProjectsIdDeploykeysKeyidEnable(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user

    key_id: int # The ID of the deploy key


@action_store.kubiya_action()
def enable_a_deploy_key(input: ProjectsIdDeploykeysKeyidEnable):
    return post_wrapper(endpoint=f"/projects/{input.id}/deploy_keys/{input.key_id}/enable", args=input.dict(exclude_none=True))
