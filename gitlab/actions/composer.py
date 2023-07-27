from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.composer import *
@action_store.kubiya_action()
def base_repository_request(input: GroupIdPackagesComposerPackages):
    return get_wrapper(endpoint=f'group/{input.id}/-/packages/composer/packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def v1_packages_list(input: GroupIdPackagesComposerPSha):
    return get_wrapper(endpoint=f'group/{input.id}/-/packages/composer/p/{input.sha}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def v1_package_metadata(input: V1PackageMetadataInput):
    return get_wrapper(endpoint=f'group/{input.id}/-/packages/composer/{input.package_name}${input.sha}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def v2_package_metadata(input: V2PackageMetadataInput):
    return get_wrapper(endpoint=f'group/{input.id}/-/packages/composer/p2/{input.package_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_package(input: CreateAPackageInput):
    return post_wrapper(endpoint=f'projects/{input.id}/packages/composer', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_package_archive(input: ProjectsIdPackagesComposerArchivesPackagename):
    return get_wrapper(endpoint=f'projects/{input.id}/packages/composer/archives/{input.package_name}', args=input.dict(exclude_none=True))