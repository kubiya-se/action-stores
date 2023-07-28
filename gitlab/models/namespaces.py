from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class Namespace(BaseModel):
    search: Optional[str] = None
    owned_only: Optional[bool] = None
class GetNameSpaceByID(BaseModel):
    id: Union[int, str]
class GetExistenceOfANamespace(BaseModel):
    namespace: str
    parent_id: Optional[int]