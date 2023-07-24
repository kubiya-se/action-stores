from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description='pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description='Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description='Conan username of a package. This attribute is the +-separated full path of your project.')
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description='Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description='Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str