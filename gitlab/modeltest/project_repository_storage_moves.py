from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class GetSingleRepositoryStorageMove(BaseModel):
    repository_storage_id: int
class GetASingleRepositoryStorageMoveForAProject:
    project_id: int
    repository_storage_move: int
class ScheduleARepositoryStorageMoveForAProject:
    project_id: int
    destination_storage_name: Optional[str]