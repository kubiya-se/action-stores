from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
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