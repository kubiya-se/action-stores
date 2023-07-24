from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int