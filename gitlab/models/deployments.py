from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None