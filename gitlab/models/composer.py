from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str