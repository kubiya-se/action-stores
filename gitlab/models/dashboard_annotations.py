from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')