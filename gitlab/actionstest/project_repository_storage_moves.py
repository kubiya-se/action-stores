from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.project_repository_storage_moves import *
@action_store.kubiya_action()
def retrieve_all_project_repository_storage_moves():
    return get_wrapper(endpoint='/project_repository_storage_moves', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retrieve_repository_storage_moves_for_a_project(input: GetSingleRepositoryStorageMove):
    return get_wrapper(endpoint=f'/projects/{input.project_id}/repository_storage_moves', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_project_repository_storage_move(input: GetSingleRepositoryStorageMove):
    return get_wrapper(endpoint=f'/project_repository_storage_moves/{input.repository_storage_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_repository_storage_move_for_a_project(input: GetASingleRepositoryStorageMoveForAProject):
    return get_wrapper(endpoint=f'/projects/{input.project_id}/repository_storage_moves/{input.repository_storage_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def schedule_repository_storage_move_for_a_project(input: ScheduleARepositoryStorageMoveForAProject):
    return post_wrapper(endpoint=f'/projects/{input.project_id}/repository_storage_moves', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def schedule_repository_storage_moves_for_all_projects(input: ScheduleARepositoryStorageMoveForAProject):
    return post_wrapper(endpoint='/project_repository_storage_moves', args=input.dict(exclude_none=True))