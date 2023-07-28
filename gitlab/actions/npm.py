from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.npm import *
@action_store.kubiya_action()
def download_package(input: DownloadPackage):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/npm/{input.package_name}/-/{input.file_name}')
@action_store.kubiya_action()
def upload_package(input: UploadPackage):
    return put_wrapper(endpoint=f'/projects/{input.id}/packages/npm/{input.package_name}', data=input.versions)
@action_store.kubiya_action()
def get_instance_metadata(input: InstanceMetadata):
    return get_wrapper(endpoint=f'/packages/npm/{input.package_name}')
@action_store.kubiya_action()
def list_instance_dist_tags(input: InstanceMetadata):
    return get_wrapper(endpoint=f'/packages/npm/-/package/{input.package_name}/dist-tags')
@action_store.kubiya_action()
def create_update_instance_tag(input: CreateUpdateTag):
    return put_wrapper(endpoint=f'/packages/npm/-/package/{input.package_name}/dist-tags/{input.tag}', data=input.version)
@action_store.kubiya_action()
def delete_instance_tag(input: PackageNameTag):
    return delete_wrapper(endpoint=f'/packages/npm/-/package/{input.package_name}/dist-tags/{input.tag}')
@action_store.kubiya_action()
def get_project_metadata(input: ProjectMetadata):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/npm/{input.package_name}')
@action_store.kubiya_action()
def list_project_dist_tags(input: ProjectMetadata):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/npm/-/package/{input.package_name}/dist-tags')
@action_store.kubiya_action()
def create_update_project_tag(input: CreateUpdateTag):
    return put_wrapper(endpoint=f'/projects/{input.id}/packages/npm/-/package/{input.package_name}/dist-tags/{input.tag}', data=input.version)
@action_store.kubiya_action()
def delete_project_tag(input: PackageNameTag):
    return delete_wrapper(endpoint=f'/projects/{input.id}/packages/npm/-/package/{input.package_name}/dist-tags/{input.tag}')
@action_store.kubiya_action()
def get_group_metadata(input: GroupMetadata):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/packages/npm/{input.package_name}')
@action_store.kubiya_action()
def list_group_dist_tags(input: GroupMetadata):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/packages/npm/-/package/{input.package_name}/dist-tags')
@action_store.kubiya_action()
def create_update_group_tag(input: CreateUpdateTag):
    return put_wrapper(endpoint=f'/groups/{input.id}/-/packages/npm/-/package/{input.package_name}/dist-tags/{input.tag}', data=input.version)
@action_store.kubiya_action()
def delete_group_tag(input: PackageNameTag):
    return delete_wrapper(endpoint=f'/groups/{input.id}/-/packages/npm/-/package/{input.package_name}/dist-tags/{input.tag}')