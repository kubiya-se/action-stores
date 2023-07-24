from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from enum import Enum


class ListAllGitignoreTemplates(BaseModel):
    pass  # No input parameters required for this API

@action_store.kubiya_action()
def list_all_gitignore_templates(input: ListAllGitignoreTemplates):
    return get_wrapper(endpoint="/templates/gitignores", args=input.dict(exclude_none=True))

class GetSingleGitignoreTemplate(BaseModel):
    key: str  # The key of the .gitignore template

@action_store.kubiya_action()
def get_single_gitignore_template(input: GetSingleGitignoreTemplate):
    return get_wrapper(endpoint=f"/templates/gitignores/{input.key}", args=input.dict(exclude_none=True))
