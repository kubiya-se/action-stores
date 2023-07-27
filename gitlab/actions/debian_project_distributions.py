from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.debian_project_distributions import *
@action_store.kubiya_action()
def list_all_debian_distributions_in_a_project(input: ListAllDebianDistributionsInAProject):
    return get_wrapper(endpoint=f'/projects/{input.id}/debian_distributions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_debian_project_distribution(input: SingleDebianProjectDistribution):
    return get_wrapper(endpoint=f'/projects/{input.id}/debian_distributions/{input.codename}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_debian_project_distribution_key(input: SingleDebianProjectDistributionKey):
    return get_wrapper(endpoint=f'/projects/{input.id}/debian_distributions/{input.codename}/key.asc', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_debian_project_distribution(input: CreateADebianProjectDistribution):
    return post_wrapper(endpoint=f'/projects/{input.id}/debian_distributions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_debian_project_distribution(input: UpdateADebianProjectDistribution):
    return put_wrapper(endpoint=f'/projects/{input.id}/debian_distributions/{input.codename}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_debian_project_distribution(input: DeleteADebianProjectDistribution):
    return delete_wrapper(endpoint=f'/projects/{input.id}/debian_distributions/{input.codename}', args=input.dict(exclude_none=True))