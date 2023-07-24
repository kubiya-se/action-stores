from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from enum import Enum


class RoutePrefix(str, Enum):
    instance_level = "/packages/conan/v1"
    project_level = "/projects/:id/packages/conan/v1`"


class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description = "pick either instance_level or project_level")


@action_store.kubiya_action()
def ping(input: Ping):
    return get_wrapper(endpoint=f"{input.route_prefix}/ping")


class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description="Search query. You can use * as a wildcard.")

@action_store.kubiya_action()
def search(input: SearchInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/conans/search?q={input.q}")


class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix

@action_store.kubiya_action()
def authenticate(input: AuthenticateInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/users/authenticate")


class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix

@action_store.kubiya_action()
def check_credentials(input: CheckCredentialsInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/users/check_credentials")


class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

@action_store.kubiya_action()
def recipe_snapshot(input: RecipeSnapshotInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}")


class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str

@action_store.kubiya_action()
def package_snapshot(input: PackageSnapshotInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}")


class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

@action_store.kubiya_action()
def recipe_manifest(input: RecipeManifestInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/digest")


class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str

@action_store.kubiya_action()
def package_manifest(input: PackageManifestInput):
    return get_wrapper(endpoint=f"{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/digest")

class RecipeManifest(BaseModel):
    package_name: str = Field(description="Name of a package.")
    package_version: str = Field(description="Version of a package.")
    package_username: str = Field(description="Conan username of a package. This attribute is the +-separated full path of your project.")
    package_channel: str = Field(description="Channel of a package.")

class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description="Reference hash of a Conan package. Conan generates this value.")

class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description="Dictionary of file names with their sizes.")

@action_store.kubiya_action()
def get_recipe_manifest(input: RecipeManifest):
    return get_wrapper(endpoint=f"/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/digest", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_package_manifest(input: PackageManifest):
    return get_wrapper(endpoint=f"/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/digest", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_recipe_download_urls(input: RecipeManifest):
    return get_wrapper(endpoint=f"/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/download_urls", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_package_download_urls(input: PackageManifest):
    return get_wrapper(endpoint=f"/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/download_urls", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def post_recipe_upload_urls(input: UploadUrls):
    return post_wrapper(endpoint=f"/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/upload_urls", args=input.dict(exclude_none=True), data=input.files)

class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]

@action_store.kubiya_action()
def package_upload_urls(input: PackageUploadUrlsInput):
    endpoint = f"/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/upload_urls"
    return post_wrapper(endpoint=endpoint, args=input.file_sizes)

class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = "0"
    file_name: str

@action_store.kubiya_action()
def download_recipe_file(input: DownloadRecipeFileInput):
    endpoint = f"/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/export/{input.file_name}"
    return get_wrapper(endpoint=endpoint)

class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = "0"
    file_name: str
    file_content: str

@action_store.kubiya_action()
def upload_recipe_file(input: UploadRecipeFileInput):
    endpoint = f"/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/export/{input.file_name}"
    return put_wrapper(endpoint=endpoint, args=input.file_content)

class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = "0"
    conan_package_reference: str
    package_revision: str = "0"
    file_name: str

@action_store.kubiya_action()
def download_package_file(input: DownloadPackageFileInput):
    endpoint = f"/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/package/{input.conan_package_reference}/{input.package_revision}/{input.file_name}"
    return get_wrapper(endpoint=endpoint)

class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = "0"
    conan_package_reference: str
    package_revision: str = "0"
    file_name: str
    file_content: str

@action_store.kubiya_action()
def upload_package_file(input: UploadPackageFileInput):
    endpoint = f"/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/package/{input.conan_package_reference}/{input.package_revision}/{input.file_name}"
    return put_wrapper(endpoint=endpoint, args=input.file_content)

class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

@action_store.kubiya_action()
def delete_package(input: DeletePackageInput):
    endpoint = f"/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}"
    return delete_wrapper(endpoint=endpoint)




