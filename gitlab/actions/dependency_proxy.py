from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.dependency_proxy import *
@action_store.kubiya_action()
def purge_the_dependency_proxy_for_a_group(input: GroupsIdDependencyproxyCache):
    return delete_wrapper(endpoint=f'/groups/{input.id}/dependency_proxy/cache', args=input.dict(exclude_none=True))