from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class SnippetId(BaseModel):
    snippet_id: int = Field(description='ID of the snippet.')
class RepositoryStorageId(BaseModel):
    repository_storage_id: int = Field(description='ID of the snippet repository storage move.')
class SnippetAndStorageId(BaseModel):
    snippet_id: int = Field(description='ID of the snippet.')
    repository_storage_id: int = Field(description='ID of the snippet repository storage move.')
class SnippetStorageMove(BaseModel):
    snippet_id: int = Field(description='ID of the snippet.')
    destination_storage_name: Optional[str] = Field(None, description='Name of the destination storage shard.')