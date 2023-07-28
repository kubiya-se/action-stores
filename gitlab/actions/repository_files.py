from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.repository_files import *
@action_store.kubiya_action()
def get_file_from_repository(input: ProjectIdRepositoryFiles):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/files/{input.file_path}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_file_blame_from_repository(input: ProjectIdRepositoryFilesBlame):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/files/{input.file_path}/blame', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_raw_file_from_repository(input: ProjectsIdRepositoryFilesFilepathRaw):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/files/{input.file_path}/raw', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_new_file_in_repository(input: ProjectsIdRepositoryFilesFilepathCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/files/{input.file_path}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_existing_file_in_repository(input: ProjectsIdRepositoryFilesFilepathUpdate):
    return put_wrapper(endpoint=f'/projects/{input.id}/repository/files/{input.file_path}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_existing_file_in_repository(input: ProjectsIdRepositoryFilesFilepathDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/repository/files/{input.file_path}', args=input.dict(exclude_none=True))