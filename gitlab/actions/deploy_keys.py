from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.deploy_keys import *
@action_store.kubiya_action()
def list_all_deploy_keys_(input: Deploykeys):
    return get_wrapper(endpoint=f'/deploy_keys', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_deploy_keys_for_project(input: ProjectsIdDeploykeys):
    return get_wrapper(endpoint=f'/projects/{input.id}/deploy_keys', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_deploy_keys_for_user(input: UsersIdorusernameProjectdeploykeys):
    return get_wrapper(endpoint=f'/users/{input.id_or_username}/project_deploy_keys', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_single_deploy_key(input: ProjectsIdDeploykeysKeyidSingle):
    return get_wrapper(endpoint=f'/projects/{input.id}/deploy_keys/{input.key_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_deploy_key(input: ProjectsIdDeploykeysAdd):
    return post_wrapper(endpoint=f'/projects/{input.id}/deploy_keys', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_deploy_key(input: ProjectsIdDeploykeysKeyidUpdate):
    return put_wrapper(endpoint=f'/projects/{input.id}/deploy_keys/{input.key_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_deploy_key(input: ProjectsIdDeploykeysKeyidDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/deploy_keys/{input.key_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def enable_a_deploy_key(input: ProjectsIdDeploykeysKeyidEnable):
    return post_wrapper(endpoint=f'/projects/{input.id}/deploy_keys/{input.key_id}/enable', args=input.dict(exclude_none=True))