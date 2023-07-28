from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.release_links import *
@action_store.kubiya_action()
def list_links_of_a_release(input: ReleaseLinksList):
    return get_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/assets/links', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_release_link(input: ReleaseLinkGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/assets/links/{input.link_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_release_link(input: ReleaseLinkCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/assets/links', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_release_link(input: ReleaseLinkUpdate):
    return put_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/assets/links/{input.link_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_release_link(input: ReleaseLinkDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/releases/{input.tag_name}/assets/links/{input.link_id}', args=input.dict(exclude_none=True))