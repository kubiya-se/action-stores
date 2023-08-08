from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime

class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict

class ProjectStatInput(BaseModel):
    id: Union[int,str]
    
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass