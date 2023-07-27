from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListOfToDoItems(BaseModel):
    action: Optional[str] = None
    author_id: Optional[int] = None
    project_id: Optional[int] = None
    group_id: Optional[int] = None
    state: Optional[str] = None
    type: Optional[str] = None
class MarkAToDoItemAsDone(BaseModel):
    id: int