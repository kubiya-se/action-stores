from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListProjectVulnerabilities(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project owned by the authenticated user.

@action_store.kubiya_action()
def list_project_vulnerabilities(input: ListProjectVulnerabilities):
    return get_wrapper(endpoint=f"/projects/{input.id}/vulnerabilities")


class NewVulnerability(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project which the authenticated user is a member of.
    finding_id: Union[int, str]  # The ID of a Vulnerability Finding to create the new Vulnerability from.

@action_store.kubiya_action()
def new_vulnerability(input: NewVulnerability):
    return post_wrapper(endpoint=f"/projects/{input.id}/vulnerabilities?finding_id={input.finding_id}")
