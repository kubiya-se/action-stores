from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListProjectRepositoryTags(BaseModel):
    id: Union[int, str]
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None

@action_store.kubiya_action()
def list_project_repository_tags(input: ListProjectRepositoryTags):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/tags", args=input.dict(exclude_none=True))


class GetASingleRepositoryTag(BaseModel):
    id: Union[int, str]
    tag_name: str

@action_store.kubiya_action()
def get_a_single_repository_tag(input: GetASingleRepositoryTag):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/tags/{input.tag_name}")


class CreateANewTag(BaseModel):
    id: Union[int, str]
    tag_name: str
    ref: str
    message: Optional[str] = None

@action_store.kubiya_action()
def create_a_new_tag(input: CreateANewTag):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/tags", args=input.dict(exclude_none=True))


class DeleteATag(BaseModel):
    id: Union[int, str]
    tag_name: str

@action_store.kubiya_action()
def delete_a_tag(input: DeleteATag):
    return delete_wrapper(endpoint=f"/projects/{input.id}/repository/tags/{input.tag_name}")


class GetTagSignature(BaseModel):
    id: Union[int, str]
    tag_name: str

@action_store.kubiya_action()
def get_tag_signature(input: GetTagSignature):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/tags/{input.tag_name}/signature")
