from pydantic import BaseModel
from typing import List, Optional, Any

class GetAllProjectsParams(BaseModel):
    expand: Optional[str]
    recent: Optional[int]

class GetAllProjectsResponse(BaseModel):
    resp: dict

