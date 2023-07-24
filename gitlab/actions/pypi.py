from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class GroupPackageFileDownload(BaseModel):
    id: str = Field(description="The ID or full path of the group.")
    sha256: str = Field(description="The PyPI package file’s sha256 checksum.")
    file_identifier: str = Field(description="The PyPI package file’s name.")

@action_store.kubiya_action()
def download_group_package_file_from_a_group(input: GroupPackageFileDownload):
    return get_wrapper(endpoint=f"/groups/{input.id}/-/packages/pypi/files/{input.sha256}/{input.file_identifier}", args=input.dict(exclude_none=True))

class GroupSimpleApiIndex(BaseModel):
    id: str = Field(description="The ID or full path of the group.")

@action_store.kubiya_action()
def group_simple_api_index(input: GroupSimpleApiIndex):
    return get_wrapper(endpoint=f"/groups/{input.id}/-/packages/pypi/simple", args=input.dict(exclude_none=True))

class GroupSimpleApiEntryPoint(BaseModel):
    id: str = Field(description="The ID or full path of the group.")
    package_name: str = Field(description="The name of the package.")

@action_store.kubiya_action()
def get_group_simple_api_entry_point(input: GroupSimpleApiEntryPoint):
    return get_wrapper(endpoint=f"/groups/{input.id}/-/packages/pypi/simple/{input.package_name}", args=input.dict(exclude_none=True))

class ProjectPackageFileDownload(BaseModel):
    id: str = Field(description="The ID or full path of the project.")
    sha256: str = Field(description="PyPI package file sha256 check sum.")
    file_identifier: str = Field(description="The PyPI package filename.")

@action_store.kubiya_action()
def download_a_package_file_from_a_project(input: ProjectPackageFileDownload):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/pypi/files/{input.sha256}/{input.file_identifier}", args=input.dict(exclude_none=True))

class ProjectSimpleApiIndex(BaseModel):
    id: str = Field(description="The ID or full path of the project.")

@action_store.kubiya_action()
def project_level_simple_API_index(input: ProjectSimpleApiIndex):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/pypi/simple", args=input.dict(exclude_none=True))

class ProjectSimpleApiEntryPoint(BaseModel):
    id: str = Field(description="The ID or full path of the project.")
    package_name: str = Field(description="The name of the package.")

@action_store.kubiya_action()
def project_level_simple_API_entry_point(input: ProjectSimpleApiEntryPoint):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/pypi/simple/{input.package_name}", args=input.dict(exclude_none=True))

class PackageUpload(BaseModel):
    id: str = Field(description="The ID or full path of the project.")
    requires_python: Optional[str] = Field(None, description="The PyPI required version.")

@action_store.kubiya_action()
def upload_a_package(input: PackageUpload):
    return put_wrapper(endpoint = f"/projects/{input.id}/packages/pypi")