from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.templates import *
@action_store.kubiya_action()
def get_all_gitignore_templates(input=None):
    return get_wrapper(endpoint=f'/templates/gitignores', args=input)
@action_store.kubiya_action()
def get_a_single_gitignore_template(input: TemplatesGitignoresKey):
    return get_wrapper(endpoint=f'/templates/gitignores/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_gitlab_ci_yaml_templates(input=None):
    return get_wrapper(endpoint=f'/templates/gitlab_ci_ymls', args=input)
@action_store.kubiya_action()
def single_gitlab_ci_yaml_template(input: TemplatesGitlabciymlsKey):
    return get_wrapper(endpoint=f'/templates/gitlab_ci_ymls/{input.key}', args=input.dict(exclude_none=True))