from pydantic import BaseModel
from typing import List, Optional, Any

class GetAllProjectsParams(BaseModel):
    expand: Optional[str]
    recent: Optional[int]

class GetAllProjectsResponse(BaseModel):
    resp: List

class CreateProjectParams(BaseModel):
    assigneeType: Optional[str]
    avatarId: Optional[int]
    categoryId: Optional[int]
    description: Optional[str]
    fieldConfigurationScheme: Optional[int]
    issueSecurityScheme: Optional[int]
    issueTypeScheme: Optional[int]
    issueTypeScreenScheme: Optional[int]
    key: str
    lead: Optional[str]
    leadAccountId: Optional[str]
    name: str
    notificationScheme: Optional[int]
    permissionScheme: Optional[int]
    projectTemplateKey: Optional[str]
    projectTypeKey: Optional[str]
    url: Optional[str]
    workflowScheme: Optional[int]

class CreateProjectResponse(BaseModel):
    resp: dict

class GetRecentProjectsParams(BaseModel):
    expand: Optional[str]
    properties: Optional[List]

class GetRecentProjectsResponse(BaseModel):
    resp: dict

class GetProjectsPaginatedParams(BaseModel):
    startAt: Optional[int]
    maxResults: Optional[int]
    orderBy: Optional[str]
    id: Optional[List]
    keys: Optional[List]
    query: Optional[str]
    typeKey: Optional[str]
    categoryId: Optional[int]
    action: Optional[str]
    expand: Optional[str]
    status: Optional[List]
    properties: Optional[List]
    propertyQuery: Optional[str]

class GetProjectsPaginatedResponse(BaseModel):
    resp: List

class GetProjectParams(BaseModel):
    projectIdOrKey: str
    expand: Optional[str]
    properties: Optional[List]

class GetProjectResposne(BaseModel):
    resp: dict

class UpdateProjectParams(BaseModel):
    projectIdOrKey: str
    expand: Optional[str]
    assigneeType: Optional[str]
    avatarId: Optional[int]
    categoryId: Optional[int]
    description: Optional[str]
    issueSecurityScheme: Optional[int]
    key: Optional[str]
    lead: Optional[str]
    leadAccountId: Optional[str]
    name: Optional[str]
    notificationScheme: Optional[int]
    permissionScheme: Optional[int]
    url: Optional[str]

class UpdateProjectResponse(BaseModel):
    resp: dict

class DeleteProjectParams(BaseModel):
    projectIdOrKey: str
    enableUndo: Optional[bool]

class ArchiveProjectParams(BaseModel):
    projectIdOrKey: str

class DeleteProjectAsynchronouslyParams(BaseModel):
    projectIdOrKey: str

class DeleteProjectAsynchronouslyResponse(BaseModel):
    resp: dict

class RestoreDeletedOrArchivedProjectParams(BaseModel):
    projectIdOrKey: str

class RestoreDeletedOrArchivedProjectResponse(BaseModel):
    resp: dict

class GetAllStatusesForProjectParams(BaseModel):
    projectIdOrKey: str

class GetAllStatusesForProjectResponse(BaseModel):
    resp: List

class GetProjectNotificationSchemeParams(BaseModel):
    projectIdOrKey: str

class GetProjectNotificationSchemeResponse(BaseModel):
    resp: dict







