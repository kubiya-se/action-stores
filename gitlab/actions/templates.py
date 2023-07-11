from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import get_wrapper, post_wrapper
from datetime import datetime


@action_store.kubiya_action()
def get_all_gitignore_templates(input=None):
    return get_wrapper(endpoint=f"/templates/gitignores", args=input)


class TemplatesGitignoresKey(BaseModel):
    key: str  # The key of the .gitignore template


@action_store.kubiya_action()
def get_a_single_gitignore_template(input: TemplatesGitignoresKey):
    return get_wrapper(endpoint=f"/templates/gitignores/{input.key}", args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def list_gitlab_ci_yaml_templates(input=None):
    return get_wrapper(endpoint=f"/templates/gitlab_ci_ymls", args=input)


class TemplatesGitlabciymlsKey(BaseModel):
    key: str  # The key of the GitLab CI/CD YAML template


@action_store.kubiya_action()
def single_gitlab_ci_yaml_template(input: TemplatesGitlabciymlsKey):
    return get_wrapper(endpoint=f"/templates/gitlab_ci_ymls/{input.key}", args=input.dict(exclude_none=True))
