from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.project_vulnerabilities import *
@action_store.kubiya_action()
def list_project_vulnerabilities(input: ListProjectVulnerabilities):
    return get_wrapper(endpoint=f'/projects/{input.id}/vulnerabilities')
@action_store.kubiya_action()
def new_vulnerability(input: NewVulnerability):
    return post_wrapper(endpoint=f'/projects/{input.id}/vulnerabilities?finding_id={input.finding_id}')