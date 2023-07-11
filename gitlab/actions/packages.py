from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListProjectPackages(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the project
    order_by: Optional[str] = None # The field to use as order
    sort: Optional[str] = None # The direction of the order
    package_type: Optional[str] = None # Filter the returned packages by type
    package_name: Optional[str] = None # Filter the project packages with a fuzzy search by name
    include_versionless: Optional[bool] = None # When set to true, versionless packages are included in the response
    status: Optional[str] = None # Filter the returned packages by status

@action_store.kubiya_action()
def list_project_packages(input: ListProjectPackages):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages", args=input.dict(exclude_none=True))


class ListGroupPackages(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the group
    exclude_subgroups: Optional[bool] = False # If the parameter is included as true, packages from projects from subgroups are not listed
    order_by: Optional[str] = None # The field to use as order
    sort: Optional[str] = None # The direction of the order
    package_type: Optional[str] = None # Filter the returned packages by type
    package_name: Optional[str] = None # Filter the project packages with a fuzzy search by name
    include_versionless: Optional[bool] = None # When set to true, versionless packages are included in the response
    status: Optional[str] = None # Filter the returned packages by status

@action_store.kubiya_action()
def list_group_packages(input: ListGroupPackages):
    return get_wrapper(endpoint=f"/groups/{input.id}/packages", args=input.dict(exclude_none=True))


class GetProjectPackage(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the project
    package_id: int # ID of a package

@action_store.kubiya_action()
def get_project_package(input: GetProjectPackage):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/{input.package_id}")


class ListPackageFiles(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the project
    package_id: int # ID of a package

@action_store.kubiya_action()
def list_package_files(input: ListPackageFiles):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/{input.package_id}/package_files")


class ListPackagePipelines(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the project
    package_id: int # ID of a package

@action_store.kubiya_action()
def list_package_pipelines(input: ListPackagePipelines):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/{input.package_id}/pipelines")


class DeleteProjectPackage(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the project
    package_id: int # ID of a package

@action_store.kubiya_action()
def delete_project_package(input: DeleteProjectPackage):
    return delete_wrapper(endpoint=f"/projects/{input.id}/packages/{input.package_id}")


class DeletePackageFile(BaseModel):
    id: Union[int, str] # ID or URL-encoded path of the project
    package_id: int # ID of a package
    package_file_id: int # ID of a package file

@action_store.kubiya_action()
def delete_package_file(input: DeletePackageFile):
    return delete_wrapper(endpoint=f"/projects/{input.id}/packages/{input.package_id}/package_files/{input.package_file_id}")
