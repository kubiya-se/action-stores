from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ReleaseLinksList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    tag_name: str = Field(description='The tag associated with the Release.')
class ReleaseLinkGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    tag_name: str = Field(description='The tag associated with the Release.')
    link_id: int = Field(description='The ID of the link.')
class ReleaseLinkCreate(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    tag_name: str = Field(description='The tag associated with the Release.')
    name: str = Field(description='The name of the link. Link names must be unique in the release.')
    url: str = Field(description='The URL of the link. Link URLs must be unique in the release.')
    direct_asset_path: Optional[str] = Field(None, description='Optional path for a direct asset link.')
    link_type: Optional[str] = Field(None, description='The type of the link: other, runbook, image, package. Defaults to other.')
class ReleaseLinkUpdate(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    tag_name: str = Field(description='The tag associated with the Release.')
    link_id: int = Field(description='The ID of the link.')
    name: Optional[str] = Field(None, description='The name of the link.')
    url: Optional[str] = Field(None, description='The URL of the link.')
    direct_asset_path: Optional[str] = Field(None, description='Optional path for a direct asset link.')
    link_type: Optional[str] = Field(None, description='The type of the link: other, runbook, image, package. Defaults to other.')
class ReleaseLinkDelete(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    tag_name: str = Field(description='The tag associated with the Release.')
    link_id: int = Field(description='The ID of the link.')