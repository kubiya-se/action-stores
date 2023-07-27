from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int