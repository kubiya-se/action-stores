from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListAllFeatureFlagUserListsForProject(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None
class CreateFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    name: str
    user_xids: str
class GetFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    iid: Union[int, str]
class UpdateFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    iid: Union[int, str]
    name: Optional[str] = None
    user_xids: Optional[str] = None
class DeleteFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    iid: Union[int, str]