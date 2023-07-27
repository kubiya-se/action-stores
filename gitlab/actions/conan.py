from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.conan import *

@action_store.kubiya_action()
def ping(input: Ping):
    return get_wrapper(endpoint=f'{input.route_prefix}/ping')
@action_store.kubiya_action()
def search(input: SearchInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/conans/search?q={input.q}')
@action_store.kubiya_action()
def authenticate(input: AuthenticateInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/users/authenticate')
@action_store.kubiya_action()
def check_credentials(input: CheckCredentialsInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/users/check_credentials')
@action_store.kubiya_action()
def recipe_snapshot(input: RecipeSnapshotInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}')
@action_store.kubiya_action()
def package_snapshot(input: PackageSnapshotInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}')
@action_store.kubiya_action()
def recipe_manifest(input: RecipeManifestInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/digest')
@action_store.kubiya_action()
def package_manifest(input: PackageManifestInput):
    return get_wrapper(endpoint=f'{input.route_prefix}/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/digest')
@action_store.kubiya_action()
def get_recipe_manifest(input: RecipeManifest):
    return get_wrapper(endpoint=f'/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/digest', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_package_manifest(input: PackageManifest):
    return get_wrapper(endpoint=f'/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/digest', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_recipe_download_urls(input: RecipeManifest):
    return get_wrapper(endpoint=f'/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/download_urls', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_package_download_urls(input: PackageManifest):
    return get_wrapper(endpoint=f'/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/download_urls', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def post_recipe_upload_urls(input: UploadUrls):
    return post_wrapper(endpoint=f'/packages/conan/v1/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/upload_urls', args=input.dict(exclude_none=True), data=input.files)
@action_store.kubiya_action()
def package_upload_urls(input: PackageUploadUrlsInput):
    endpoint = f'/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/packages/{input.conan_package_reference}/upload_urls'
    return post_wrapper(endpoint=endpoint, args=input.file_sizes)
@action_store.kubiya_action()
def download_recipe_file(input: DownloadRecipeFileInput):
    endpoint = f'/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/export/{input.file_name}'
    return get_wrapper(endpoint=endpoint)
@action_store.kubiya_action()
def upload_recipe_file(input: UploadRecipeFileInput):
    endpoint = f'/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/export/{input.file_name}'
    return put_wrapper(endpoint=endpoint, args=input.file_content)
@action_store.kubiya_action()
def download_package_file(input: DownloadPackageFileInput):
    endpoint = f'/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/package/{input.conan_package_reference}/{input.package_revision}/{input.file_name}'
    return get_wrapper(endpoint=endpoint)
@action_store.kubiya_action()
def upload_package_file(input: UploadPackageFileInput):
    endpoint = f'/packages/conan/v1/files/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}/{input.recipe_revision}/package/{input.conan_package_reference}/{input.package_revision}/{input.file_name}'
    return put_wrapper(endpoint=endpoint, args=input.file_content)
@action_store.kubiya_action()
def delete_package(input: DeletePackageInput):
    endpoint = f'/conans/{input.package_name}/{input.package_version}/{input.package_username}/{input.package_channel}'
    return delete_wrapper(endpoint=endpoint)