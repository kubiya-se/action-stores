from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GroupPackageFileDownload(BaseModel):
    id: str = Field(description='The ID or full path of the group.')
    sha256: str = Field(description='The PyPI package file’s sha256 checksum.')
    file_identifier: str = Field(description='The PyPI package file’s name.')
class GroupSimpleApiIndex(BaseModel):
    id: str = Field(description='The ID or full path of the group.')
class GroupSimpleApiEntryPoint(BaseModel):
    id: str = Field(description='The ID or full path of the group.')
    package_name: str = Field(description='The name of the package.')
class ProjectPackageFileDownload(BaseModel):
    id: str = Field(description='The ID or full path of the project.')
    sha256: str = Field(description='PyPI package file sha256 check sum.')
    file_identifier: str = Field(description='The PyPI package filename.')
class ProjectSimpleApiIndex(BaseModel):
    id: str = Field(description='The ID or full path of the project.')
class ProjectSimpleApiEntryPoint(BaseModel):
    id: str = Field(description='The ID or full path of the project.')
    package_name: str = Field(description='The name of the package.')
class PackageUpload(BaseModel):
    id: str = Field(description='The ID or full path of the project.')
    requires_python: Optional[str] = Field(None, description='The PyPI required version.')