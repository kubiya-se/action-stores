from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.gitlab_pages import *
@action_store.kubiya_action()
def delete_project_pages(input: ProjectsPagesDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/pages', args=input.dict(exclude_none=True))