from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

@action_store.kubiya_action()
def retreive_all_snippet_repository_storage_moves():
    return get_wrapper(endpoint="/snippet_repository_storage_moves", args=input.dict(exclude_none=True))

class SnippetId(BaseModel):
    snippet_id: int = Field(description="ID of the snippet.")

@action_store.kubiya_action()
def get_all_repository_storage_moves_for_snippet(input: SnippetId):
    return get_wrapper(endpoint=f"/snippets/{input.snippet_id}/repository_storage_moves", args=input.dict(exclude_none=True))

class RepositoryStorageId(BaseModel):
    repository_storage_id: int = Field(description="ID of the snippet repository storage move.")

@action_store.kubiya_action()
def get_single_snippet_repository_storage_move(input: RepositoryStorageId):
    return get_wrapper(endpoint=f"/snippet_repository_storage_moves/{input.repository_storage_id}", args=input.dict(exclude_none=True))

class SnippetAndStorageId(BaseModel):
    snippet_id: int = Field(description="ID of the snippet.")
    repository_storage_id: int = Field(description="ID of the snippet repository storage move.")

@action_store.kubiya_action()
def get_single_repository_storage_move_for_snippet(input: SnippetAndStorageId):
    return get_wrapper(endpoint=f"/snippets/{input.snippet_id}/repository_storage_moves/{input.repository_storage_id}", args=input.dict(exclude_none=True))

class SnippetStorageMove(BaseModel):
    snippet_id: int = Field(description="ID of the snippet.")
    destination_storage_name: Optional[str] = Field(None, description="Name of the destination storage shard.")

@action_store.kubiya_action()
def schedule_repository_storage_move_for_snippet(input: SnippetStorageMove):
    return post_wrapper(endpoint=f"/snippets/{input.snippet_id}/repository_storage_moves", args=input.dict(exclude_none=True))
