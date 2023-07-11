from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int,str] # The ID or full path of the group.


@action_store.kubiya_action()
def base_repository_request(input: GroupIdPackagesComposerPackages):
    return get_wrapper(endpoint=f"group/{input.id}/-/packages/composer/packages", args=input.dict(exclude_none=True))


class GroupIdPackagesComposerPSha(BaseModel):

    id: Union[int,str] # The ID or full path of the group.

    sha: str # The provider SHA, provided by the Composer base request.


@action_store.kubiya_action()
def v1_packages_list(input: GroupIdPackagesComposerPSha):
    return get_wrapper(endpoint=f"group/{input.id}/-/packages/composer/p/{input.sha}", args=input.dict(exclude_none=True))


class V1PackageMetadataInput(BaseModel):
    id: Union[int,str]
    package_name: str
    sha: str

@action_store.kubiya_action()
def v1_package_metadata(input: V1PackageMetadataInput):
    return get_wrapper(endpoint=f"group/{input.id}/-/packages/composer/{input.package_name}${input.sha}", args=input.dict(exclude_none=True))


class V2PackageMetadataInput(BaseModel):

    id: Union[int,str] # The ID or full path of the group.

    package_name: str # The name of the package.


@action_store.kubiya_action()
def v2_package_metadata(input: V2PackageMetadataInput):
    return get_wrapper(endpoint=f"group/{input.id}/-/packages/composer/p2/{input.package_name}", args=input.dict(exclude_none=True))


class CreateAPackageInput(BaseModel):

    id: Union[int,str] # The ID or full path of the group.

    tag: Optional[str] = None # The name of the tag to target for the package.

    branch: Optional[str] = None # The name of the branch to target for the package.


@action_store.kubiya_action()
def create_a_package(input: CreateAPackageInput):
    return post_wrapper(endpoint=f"projects/{input.id}/packages/composer", args=input.dict(exclude_none=True))


class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):

    id: Union[int,str] # The ID or full path of the group.

    package_name: str # The name of the package.

    sha: str # The target SHA of the requested package version.


@action_store.kubiya_action()
def download_a_package_archive(input: ProjectsIdPackagesComposerArchivesPackagename):
    return get_wrapper(endpoint=f"projects/{input.id}/packages/composer/archives/{input.package_name}", args=input.dict(exclude_none=True))