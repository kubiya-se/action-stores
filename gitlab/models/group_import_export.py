from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GroupExport(BaseModel):
    id: Union[int, str] = Field(description='ID of the group owned by the authenticated user.')
class GroupImport(BaseModel):
    name: str = Field(description='The name of the group to be imported')
    path: str = Field(description='Name and path for new group')
    file: str = Field(description='The file to be uploaded')
    parent_id: Optional[int] = Field(None, description='ID of a parent group to import the group into. Defaults to the current user’s namespace if not provided.')