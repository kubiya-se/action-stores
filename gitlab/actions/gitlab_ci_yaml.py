from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from enum import Enum


class ListAllCICDYamlTemplates(BaseModel):
    pass  # No input parameters required for this API

@action_store.kubiya_action()
def list_all_ci_cd_yaml_templates(input: ListAllCICDYamlTemplates):
    return get_wrapper(endpoint="/templates/gitlab_ci_ymls", args=input.dict(exclude_none=True))

class GetSingleCICDYamlTemplate(BaseModel):
    key: str  # The key of the CI/CD YAML template

@action_store.kubiya_action()
def get_single_ci_cd_yaml_template(input: GetSingleCICDYamlTemplate):
    return get_wrapper(endpoint=f"/templates/gitlab_ci_ymls/{input.key}", args=input.dict(exclude_none=True))
