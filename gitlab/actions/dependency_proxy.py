from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class GroupsIdDependencyproxyCache(BaseModel):

    id: int # The ID or URL-encoded path of the group owned by the authenticated user

@action_store.kubiya_action()
def purge_the_dependency_proxy_for_a_group(input: GroupsIdDependencyproxyCache):
    return delete_wrapper(endpoint=f"/groups/{input.id}/dependency_proxy/cache", args=input.dict(exclude_none=True))
