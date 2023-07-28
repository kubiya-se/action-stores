from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.debian_group_distributions import *
@action_store.kubiya_action()
def list_all_debian_distributions_in_a_group(input: ListAllDebianDistributionsInAGroup):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/debian_distributions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_debian_group_distribution(input: SingleDebianGroupDistribution):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/debian_distributions/{input.codename}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_debian_group_distribution_key(input: GroupsIdDebiandistributionsCodenameKey):
    return get_wrapper(endpoint=f'/groups/{input.id}/-/debian_distributions/{input.codename}/key.asc', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_debian_group_distribution(input: CreateADebianGroupDistribution):
    return post_wrapper(endpoint=f'/groups/{input.id}/-/debian_distributions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_debian_group_distribution(input: UpdateADebianGroupDistribution):
    return put_wrapper(endpoint=f'/groups/{input.id}/-/debian_distributions/{input.codename}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_debian_group_distribution(input: DeleteADebianGroupDistribution):
    return delete_wrapper(endpoint=f'/groups/{input.id}/-/debian_distributions/{input.codename}', args=input.dict(exclude_none=True))