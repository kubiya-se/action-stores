from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict

class ProjectStatInput(BaseModel):
    id: Union[int,str]
    
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