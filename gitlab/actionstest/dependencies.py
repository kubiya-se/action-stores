from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.dependencies import *
@action_store.kubiya_action()
def list_project_dependencies(input: ProjectsIdDependencies):
    return get_wrapper(endpoint=f'/projects/{input.id}/dependencies', args=input.dict(exclude_none=True))