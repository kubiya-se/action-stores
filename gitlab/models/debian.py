from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str