from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project accessible by the authenticated user.')
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum] = Field(default=None, description='The desired visibility of the Container Registry. One of enabled (default), private, or disabled.')
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description='The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description='The service type.')
    scope: str = Field(default='registry:catalog:*', description='Scope for the token.')