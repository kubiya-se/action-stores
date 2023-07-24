from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')