from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.tags import *
@action_store.kubiya_action()
def list_project_repository_tags(input: ListProjectRepositoryTags):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/tags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_single_repository_tag(input: GetASingleRepositoryTag):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/tags/{input.tag_name}')
@action_store.kubiya_action()
def create_a_new_tag(input: CreateANewTag):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/tags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_tag(input: DeleteATag):
    return delete_wrapper(endpoint=f'/projects/{input.id}/repository/tags/{input.tag_name}')
@action_store.kubiya_action()
def get_tag_signature(input: GetTagSignature):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/tags/{input.tag_name}/signature')