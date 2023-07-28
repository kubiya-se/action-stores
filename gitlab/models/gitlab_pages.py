from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsPagesDelete(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')