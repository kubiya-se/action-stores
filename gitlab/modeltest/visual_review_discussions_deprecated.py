from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None