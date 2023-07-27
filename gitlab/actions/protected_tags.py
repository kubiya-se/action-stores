from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.protected_tags import *
@action_store.kubiya_action()
def list_protected_tags(input: ProtectedTagsList):
    return get_wrapper(endpoint=f'/projects/{input.id}/protected_tags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_single_protected_tag_or_wildcard_protected_tag(input: SingleProtectedTag):
    return get_wrapper(endpoint=f'/projects/{input.id}/protected_tags/{input.name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def protect_repository_tags(input: ProtectRepositoryTags):
    return post_wrapper(endpoint=f'/projects/{input.id}/protected_tags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def unprotect_repository_tags(input: UnprotectRepositoryTags):
    return delete_wrapper(endpoint=f'/projects/{input.id}/protected_tags/{input.name}', args=input.dict(exclude_none=True))