from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.pypi import *
@action_store.kubiya_action()
def download_group_package_file_from_a_group(input: GroupPackageFileDownload):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/packages/pypi/files/{input.sha256}/{input.file_identifier}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def group_simple_api_index(input: GroupSimpleApiIndex):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/packages/pypi/simple', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_group_simple_api_entry_point(input: GroupSimpleApiEntryPoint):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/packages/pypi/simple/{input.package_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_package_file_from_a_project(input: ProjectPackageFileDownload):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/pypi/files/{input.sha256}/{input.file_identifier}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def project_level_simple_API_index(input: ProjectSimpleApiIndex):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/pypi/simple', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def project_level_simple_API_entry_point(input: ProjectSimpleApiEntryPoint):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/pypi/simple/{input.package_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def upload_a_package(input: PackageUpload):
    return put_wrapper(endpoint=f'/projects/{input.id}/packages/pypi')