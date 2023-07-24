from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class ListReleases(BaseModel):
    id: Union[int, str]
    order_by: Optional[str] = None
    sort: Optional[str] = None
    include_html_description: Optional[bool] = None

@action_store.kubiya_action()
def list_releases(input: ListReleases):
    return get_wrapper(endpoint=f"/projects/{input.id}/releases", args=input.dict(exclude_none=True))

class GetReleaseByTagName(BaseModel):
    id: Union[int, str]
    tag_name: str
    include_html_description: Optional[bool] = None

@action_store.kubiya_action()
def get_release_by_tag_name(input: GetReleaseByTagName):
    return get_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}", args=input.dict(exclude_none=True))

class DownloadReleaseAsset(BaseModel):
    id: Union[int, str]
    tag_name: str
    direct_asset_path: str

@action_store.kubiya_action()
def download_release_asset(input: DownloadReleaseAsset):
    return get_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/downloads/{input.direct_asset_path}")

class GetLatestRelease(BaseModel):
    id: Union[int, str]

@action_store.kubiya_action()
def get_latest_release(input: GetLatestRelease):
    return get_wrapper(endpoint=f"/projects/{input.id}/releases/permalink/latest")

class ReleaseLinks(BaseModel):
    name: str
    url: str
    filepath: Optional[str] = None
    direct_asset_path: Optional[str] = None
    link_type: Optional[str] = None

class CreateRelease(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    name: Optional[str] = None  # The release name.
    tag_name: str  # The tag where the release is created from.
    tag_message: Optional[str] = None  # Message to use if creating a new annotated tag.
    description: Optional[str] = None  # The description of the release. You can use Markdown.
    ref: Optional[str] = None  # If a tag specified in tag_name doesn’t exist, the release is created from ref and tagged with tag_name.
    milestones: Optional[List[str]] = None  # The title of each milestone the release is associated with.
    assets: Optional[Dict[str, List[ReleaseLinks]]] = None  # An array of assets links.
    released_at: Optional[datetime] = None  # Date and time for the release.

@action_store.kubiya_action()
def create_release(input: CreateRelease):
    return post_wrapper(endpoint=f"/projects/{input.id}/releases", data=input.dict(exclude_none=True))


class CollectReleaseEvidence(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    tag_name: str  # The Git tag the release is associated with.

@action_store.kubiya_action()
def collect_release_evidence(input: CollectReleaseEvidence):
    return post_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}/evidence")


class UpdateRelease(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    tag_name: str  # The Git tag the release is associated with.
    name: Optional[str] = None  # The release name.
    description: Optional[str] = None  # The description of the release. You can use Markdown.
    milestones: Optional[List[str]] = None  # The title of each milestone to associate with the release.
    released_at: Optional[datetime] = None  # The date when the release is/was ready.

@action_store.kubiya_action()
def update_release(input: UpdateRelease):
    return put_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}", data=input.dict(exclude_none=True))

class DeleteRelease(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    tag_name: str  # The Git tag the release is associated with.

@action_store.kubiya_action()
def delete_release(input: DeleteRelease):
    return delete_wrapper(endpoint=f"/projects/{input.id}/releases/{input.tag_name}")
