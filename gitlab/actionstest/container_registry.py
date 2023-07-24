from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.container_registry import *
@action_store.kubiya_action()
def change_container_registry_visibility(input: ChangeContainerRegistryVisibility):
    return put_wrapper(endpoint=f'/projects/{input.id}/', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_registry_repositories(input: ListProjectRegistryRepositories):
    return get_wrapper(endpoint=f'/projects/{input.id}/registry/repositories', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_registry_repositories(input: GroupsIdRegistryRepositories):
    return get_wrapper(endpoint=f'/groups/{input.id}/registry/repositories', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_details_of_a_single_repository(input: RegistryRepositoriesId):
    return get_wrapper(endpoint=f'/registry/repositories/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_registry_repository(input: ProjectsIdRegistryRepositoriesRepositoryid):
    return delete_wrapper(endpoint=f'/projects/{input.id}/registry/repositories/{input.repository_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_registry_repository_tags(input: ProjectsIdRegistryRepositoriesRepositoryidTags):
    return get_wrapper(endpoint=f'/projects/{input.id}/registry/repositories/{input.repository_id}/tags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_details_of_a_registry_repository_tag(input: GetDetailsOfARegistryRepositoryTag):
    return get_wrapper(endpoint=f'/projects/{input.id}/registry/repositories/{input.repository_id}/tags/{input.tag_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_registry_repository_tag(input: DeleteARegistryRepositoryTag):
    return delete_wrapper(endpoint=f'/projects/{input.id}/registry/repositories/{input.repository_id}/tags/{input.tag_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_registry_repository_tags_in_bulk(input: DeleteRegistryRepositoryTagsInBulk):
    return delete_wrapper(endpoint=f'/projects/{input.id}/registry/repositories/{input.repository_id}/tags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def obtain_token(input: ObtainTokenInput):
    return get_wrapper(endpoint=f'{input.CI_SERVER_URL}/jwt/auth?service={input.service}&scope={input.scope}')
@action_store.kubiya_action()
def delete_image_tags_by_reference(input: DeleteImageTagsByReferenceInput):
    return delete_wrapper(endpoint=f'{input.CI_REGISTRY}/v2/{input.CI_REGISTRY_IMAGE}/tags/reference/{input.CI_COMMIT_SHORT_SHA}')
@action_store.kubiya_action()
def list_all_container_repositories(input: ListAllContainerRepositoriesInput):
    token = get_wrapper(endpoint=f'{input.CI_REGISTRY}/jwt/auth?service={input.service}&scope={input.scope}', auth=(input.admin_username, input.admin_password))
    return get_wrapper(endpoint=f'{input.CI_REGISTRY}/v2/_catalog', headers={'Authorization': f'Bearer {token}'})