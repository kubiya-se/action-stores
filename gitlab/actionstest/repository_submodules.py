from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.repository_submodules import *
@action_store.kubiya_action()
def update_existing_submodule_reference_in_repository(input: UpdateSubmodule):
    return put_wrapper(endpoint=f'/projects/{input.id}/repository/submodules/{input.submodule}', args=input.dict(exclude_none=True))