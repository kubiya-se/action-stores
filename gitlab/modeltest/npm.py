from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class DownloadPackage(BaseModel):
    id: Union[int, str]
    package_name: str
    file_name: str
class UploadPackage(BaseModel):
    id: Union[int, str]
    package_name: str
    versions: str
class PackageName(BaseModel):
    package_name: str
class PackageNameTag(BaseModel):
    package_name: str
    tag: str
class CreateUpdateTag(PackageNameTag):
    version: str
class InstanceMetadata(PackageName):
    id: Union[int, str]
class ProjectMetadata(PackageName):
    id: Union[int, str]
class GroupMetadata(PackageName):
    id: Union[int, str]