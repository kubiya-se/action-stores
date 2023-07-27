from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int