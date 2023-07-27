from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.namespaces import *
@action_store.kubiya_action()
def list_namespaces(input: Namespace):
    return get_wrapper(endpoint='/namespaces', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_namespace_by_id(input: GetNameSpaceByID):
    return get_wrapper(endpoint=f'/namespaces/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_namespace_existence(input: GetExistenceOfANamespace):
    return get_wrapper(endpoint=f'/namespaces/{input.namespace}/exists', args=input.dict(exclude_none=True))