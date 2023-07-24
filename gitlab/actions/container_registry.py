from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from enum import Enum

# Note: this requires administrators to nape ci_job_token_scope feature flag:
# The use of CI_JOB_TOKEN scoped to the current project was introduced in GitLab 13.12.
# This is the API documentation of the GitLab Container Registry.
# When the ci_job_token_scope feature flag is enabled (it is disabled by default), you can use the below endpoints from a CI/CD job, by passing the $CI_JOB_TOKEN variable as the JOB-TOKEN header. The job token only has access to its own project.
# GitLab administrators with access to the GitLab Rails console can opt to enable it.
# To enable it:
#   Feature.enable(:ci_job_token_scope)
# To disable it:
#   Feature.disable(:ci_job_token_scope)


# Define the types
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = "enabled"
    private = "private"
    disabled = "disabled"

class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project accessible by the authenticated user.")
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum] = Field(
        default=None,
        description="The desired visibility of the Container Registry. One of enabled (default), private, or disabled."
    )

@action_store.kubiya_action()
def change_container_registry_visibility(input: ChangeContainerRegistryVisibility):
    return put_wrapper(endpoint=f"/projects/{input.id}/", args=input.dict(exclude_none=True))

class ListProjectRegistryRepositories(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project accessible by the authenticated user.

    tags: Optional[bool] = None # If the parameter is included as true, each repository includes an array of "tags" in the response.

    tags_count: Optional[bool] = None # If the parameter is included as true, each repository includes "tags_count" in the response (Introduced in GitLab 13.1).


@action_store.kubiya_action()
def list_project_registry_repositories(input: ListProjectRegistryRepositories):
    return get_wrapper(endpoint=f"/projects/{input.id}/registry/repositories", args=input.dict(exclude_none=True))


class GroupsIdRegistryRepositories(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group accessible by the authenticated user.


@action_store.kubiya_action()
def list_registry_repositories(input: GroupsIdRegistryRepositories):
    return get_wrapper(endpoint=f"/groups/{input.id}/registry/repositories", args=input.dict(exclude_none=True))


class RegistryRepositoriesId(BaseModel):

    id: Union[int,str] # The ID of the registry repository accessible by the authenticated user.

    tags: Optional[bool] = None # If the parameter is included as true, the response includes an array of "tags".

    tags_count: Optional[bool] = None # If the parameter is included as true, the response includes "tags_count".

    size: Optional[bool] = None # If the parameter is included as true, the response includes "size". This is the deduplicated size of all images within the repository. Deduplication eliminates extra copies of identical data. For example, if you upload the same image twice, the Container Registry stores only one copy. This field is only available on GitLab.com for repositories created after 2021-11-04.


@action_store.kubiya_action()
def get_details_of_a_single_repository(input: RegistryRepositoriesId):
    return get_wrapper(endpoint=f"/registry/repositories/{input.id}", args=input.dict(exclude_none=True))


class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    repository_id: int # The ID of registry repository.


@action_store.kubiya_action()
def delete_registry_repository(input: ProjectsIdRegistryRepositoriesRepositoryid):
    return delete_wrapper(endpoint=f"/projects/{input.id}/registry/repositories/{input.repository_id}", args=input.dict(exclude_none=True))


class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project accessible by the authenticated user.

    repository_id: int # The ID of registry repository.


@action_store.kubiya_action()
def list_project_registry_repository_tags(input: ProjectsIdRegistryRepositoriesRepositoryidTags):
    return get_wrapper(endpoint=f"/projects/{input.id}/registry/repositories/{input.repository_id}/tags", args=input.dict(exclude_none=True))


class GetDetailsOfARegistryRepositoryTag(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project accessible by the authenticated user.

    repository_id: int # The ID of registry repository.

    tag_name: str # The name of tag.


@action_store.kubiya_action()
def get_details_of_a_registry_repository_tag(input: GetDetailsOfARegistryRepositoryTag):
    return get_wrapper(endpoint=f"/projects/{input.id}/registry/repositories/{input.repository_id}/tags/{input.tag_name}", args=input.dict(exclude_none=True))


class DeleteARegistryRepositoryTag(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    repository_id: int # The ID of registry repository.

    tag_name: str # The name of tag.


@action_store.kubiya_action()
def delete_a_registry_repository_tag(input: DeleteARegistryRepositoryTag):
    return delete_wrapper(endpoint=f"/projects/{input.id}/registry/repositories/{input.repository_id}/tags/{input.tag_name}", args=input.dict(exclude_none=True))


class DeleteRegistryRepositoryTagsInBulk(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    repository_id: int # The ID of registry repository.

    name_regex: Optional[str] = None # The re2 regex of the name to delete. To delete all tags specify .*. Note: name_regex is deprecated in favor of name_regex_delete. This field is validated.

    name_regex_delete: str # The re2 regex of the name to delete. To delete all tags specify .*. This field is validated.

    name_regex_keep: Optional[str] = None # The re2 regex of the name to keep. This value overrides any matches from name_regex_delete. This field is validated. Note: setting to .* results in a no-op.

    keep_n: Optional[int] = None # The amount of latest tags of given name to keep.

    older_than: Optional[str] = None # Tags to delete that are older than the given time, written in human readable form 1h, 1d, 1month.


@action_store.kubiya_action()
def delete_registry_repository_tags_in_bulk(input: DeleteRegistryRepositoryTagsInBulk):
    return delete_wrapper(endpoint=f"/projects/{input.id}/registry/repositories/{input.repository_id}/tags", args=input.dict(exclude_none=True))

class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description="CI server URL.")
    service: str = Field(default="container_registry", description="The service type.")
    scope: str = Field(description="Scope for the token.")

@action_store.kubiya_action()
def obtain_token(input: ObtainTokenInput):
    return get_wrapper(endpoint=f"{input.CI_SERVER_URL}/jwt/auth?service={input.service}&scope={input.scope}")


class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description="The CI registry URL.")
    CI_REGISTRY_IMAGE: str = Field(description="The registry image.")
    CI_COMMIT_SHORT_SHA: str = Field(description="The commit SHA.")

@action_store.kubiya_action()
def delete_image_tags_by_reference(input: DeleteImageTagsByReferenceInput):
    return delete_wrapper(endpoint=f"{input.CI_REGISTRY}/v2/{input.CI_REGISTRY_IMAGE}/tags/reference/{input.CI_COMMIT_SHORT_SHA}")


class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description="The CI registry URL.")
    admin_username: str = Field(description="The admin username.")
    admin_password: str = Field(description="The admin password.")
    service: str = Field(default="container_registry", description="The service type.")
    scope: str = Field(default="registry:catalog:*", description="Scope for the token.")

@action_store.kubiya_action()
def list_all_container_repositories(input: ListAllContainerRepositoriesInput):
    # First, get the token
    token = get_wrapper(endpoint=f"{input.CI_REGISTRY}/jwt/auth?service={input.service}&scope={input.scope}", auth=(input.admin_username, input.admin_password))

    # Now, use the token to get the catalog
    return get_wrapper(endpoint=f"{input.CI_REGISTRY}/v2/_catalog", headers={"Authorization": f"Bearer {token}"})
