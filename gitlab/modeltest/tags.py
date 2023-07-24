from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListProjectRepositoryTags(BaseModel):
    id: Union[int, str]
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
class GetASingleRepositoryTag(BaseModel):
    id: Union[int, str]
    tag_name: str
class CreateANewTag(BaseModel):
    id: Union[int, str]
    tag_name: str
    ref: str
    message: Optional[str] = None
class DeleteATag(BaseModel):
    id: Union[int, str]
    tag_name: str
class GetTagSignature(BaseModel):
    id: Union[int, str]
    tag_name: str