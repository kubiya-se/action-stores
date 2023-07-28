from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListProjectPackages(BaseModel):
    id: Union[int, str]
    order_by: Optional[str] = None
    sort: Optional[str] = None
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    include_versionless: Optional[bool] = None
    status: Optional[str] = None
class ListGroupPackages(BaseModel):
    id: Union[int, str]
    exclude_subgroups: Optional[bool] = False
    order_by: Optional[str] = None
    sort: Optional[str] = None
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    include_versionless: Optional[bool] = None
    status: Optional[str] = None
class GetProjectPackage(BaseModel):
    id: Union[int, str]
    package_id: int
class ListPackageFiles(BaseModel):
    id: Union[int, str]
    package_id: int
class ListPackagePipelines(BaseModel):
    id: Union[int, str]
    package_id: int
class DeleteProjectPackage(BaseModel):
    id: Union[int, str]
    package_id: int
class DeletePackageFile(BaseModel):
    id: Union[int, str]
    package_id: int
    package_file_id: int