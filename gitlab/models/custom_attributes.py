from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str