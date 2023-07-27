from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.packages import *
@action_store.kubiya_action()
def list_project_packages(input: ListProjectPackages):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_group_packages(input: ListGroupPackages):
    return get_wrapper(endpoint=f'/groups/{input.id}/packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_project_package(input: GetProjectPackage):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/{input.package_id}')
@action_store.kubiya_action()
def list_package_files(input: ListPackageFiles):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/{input.package_id}/package_files')
@action_store.kubiya_action()
def list_package_pipelines(input: ListPackagePipelines):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/{input.package_id}/pipelines')
@action_store.kubiya_action()
def delete_project_package(input: DeleteProjectPackage):
    return delete_wrapper(endpoint=f'/projects/{input.id}/packages/{input.package_id}')
@action_store.kubiya_action()
def delete_package_file(input: DeletePackageFile):
    return delete_wrapper(endpoint=f'/projects/{input.id}/packages/{input.package_id}/package_files/{input.package_file_id}')