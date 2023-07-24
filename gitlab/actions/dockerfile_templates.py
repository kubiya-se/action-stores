from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


@action_store.kubiya_action()
def list_dockerfile_templates(input=None):
    return get_wrapper(endpoint=f"/templates/dockerfiles", args=input)


class TemplatesDockerfilesKey(BaseModel):
    key: str  # The key of the Dockerfile template


@action_store.kubiya_action()
def single_dockerfile_template(input: TemplatesDockerfilesKey):
    return get_wrapper(endpoint=f"/templates/dockerfiles/{input.key}", args=input.dict(exclude_none=True))
