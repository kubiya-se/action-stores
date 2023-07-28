from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.releases import *
@action_store.kubiya_action()
def list_releases(input: ListReleases):
    return get_wrapper(endpoint=f'/projects/{input.id}/releases', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_release_by_tag_name(input: GetReleaseByTagName):
    return get_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_release_asset(input: DownloadReleaseAsset):
    return get_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/downloads/{input.direct_asset_path}')
@action_store.kubiya_action()
def get_latest_release(input: GetLatestRelease):
    return get_wrapper(endpoint=f'/projects/{input.id}/releases/permalink/latest')
@action_store.kubiya_action()
def create_release(input: CreateRelease):
    return post_wrapper(endpoint=f'/projects/{input.id}/releases', data=input.dict(exclude_none=True))
@action_store.kubiya_action()
def collect_release_evidence(input: CollectReleaseEvidence):
    return post_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/evidence')
@action_store.kubiya_action()
def update_release(input: UpdateRelease):
    return put_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}', data=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_release(input: DeleteRelease):
    return delete_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}')