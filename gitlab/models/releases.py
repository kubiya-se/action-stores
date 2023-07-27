from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListReleases(BaseModel):
    id: Union[int, str]
    order_by: Optional[str] = None
    sort: Optional[str] = None
    include_html_description: Optional[bool] = None
class GetReleaseByTagName(BaseModel):
    id: Union[int, str]
    tag_name: str
    include_html_description: Optional[bool] = None
class DownloadReleaseAsset(BaseModel):
    id: Union[int, str]
    tag_name: str
    direct_asset_path: str
class GetLatestRelease(BaseModel):
    id: Union[int, str]
class ReleaseLinks(BaseModel):
    name: str
    url: str
    filepath: Optional[str] = None
    direct_asset_path: Optional[str] = None
    link_type: Optional[str] = None
class CreateRelease(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
    tag_name: str
    tag_message: Optional[str] = None
    description: Optional[str] = None
    ref: Optional[str] = None
    milestones: Optional[List[str]] = None
    assets: Optional[Dict[str, List[ReleaseLinks]]] = None
    released_at: Optional[datetime] = None
class CollectReleaseEvidence(BaseModel):
    id: Union[int, str]
    tag_name: str
class UpdateRelease(BaseModel):
    id: Union[int, str]
    tag_name: str
    name: Optional[str] = None
    description: Optional[str] = None
    milestones: Optional[List[str]] = None
    released_at: Optional[datetime] = None
class DeleteRelease(BaseModel):
    id: Union[int, str]
    tag_name: str