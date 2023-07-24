from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime



class ListAllDebianDistributionsInAGroup(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group.

    codename: Optional[str] = None # Filter with specific codename.

    suite: Optional[str] = None # Filter with specific suite.

@action_store.kubiya_action()
def list_all_debian_distributions_in_a_group(input: ListAllDebianDistributionsInAGroup):
    return get_wrapper(endpoint=f"/groups/{input.id}/-/debian_distributions", args=input.dict(exclude_none=True))


class SingleDebianGroupDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user.

    codename: int # The codename of a distribution.

@action_store.kubiya_action()
def single_debian_group_distribution(input: SingleDebianGroupDistribution):
    return get_wrapper(endpoint=f"/groups/{input.id}/-/debian_distributions/{input.codename}", args=input.dict(exclude_none=True))


class GroupsIdDebiandistributionsCodenameKey(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user.

    codename: int # The codename of a distribution.

@action_store.kubiya_action()
def single_debian_group_distribution_key(input: GroupsIdDebiandistributionsCodenameKey):
    return get_wrapper(endpoint=f"/groups/{input.id}/-/debian_distributions/{input.codename}/key.asc", args=input.dict(exclude_none=True))

class CreateADebianGroupDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user.

    codename: str # The codename of a Debian distribution.

    suite: Optional[str] = None # The suite of the new Debian distribution.

    origin: Optional[str] = None # The origin of the new Debian distribution.

    label: Optional[str] = None # The label of the new Debian distribution.

    version: Optional[str] = None # The version of the new Debian distribution.

    description: Optional[str] = None # The description of the new Debian distribution.

    valid_time_duration_seconds: Optional[int] = None # The valid time duration (in seconds) of the new Debian distribution.

    components: Optional[List[str]] = None # The new Debian distribution’s list of components.

    architectures: Optional[List[str]] = None # The new Debian distribution’s list of architectures.

@action_store.kubiya_action()
def create_a_debian_group_distribution(input: CreateADebianGroupDistribution):
    return post_wrapper(endpoint=f"/groups/{input.id}/-/debian_distributions", args=input.dict(exclude_none=True))


class UpdateADebianGroupDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user.

    codename: str # The Debian distribution’s new codename.

    suite: Optional[str] = None # The Debian distribution’s new suite.

    origin: Optional[str] = None # The Debian distribution’s new origin.

    label: Optional[str] = None # The Debian distribution’s new label.

    version: Optional[str] = None # The Debian distribution’s new version.

    description: Optional[str] = None # The Debian distribution’s new description.

    valid_time_duration_seconds: Optional[int] = None # The Debian distribution’s new valid time duration (in seconds).

    components: Optional[List[str]] = None # The Debian distribution’s new list of components.

    architectures: Optional[List[str]] = None # The Debian distribution’s new list of architectures.


@action_store.kubiya_action()
def update_a_debian_group_distribution(input: UpdateADebianGroupDistribution):
    return put_wrapper(endpoint=f"/groups/{input.id}/-/debian_distributions/{input.codename}", args=input.dict(exclude_none=True))

class DeleteADebianGroupDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user.
    codename: int # The codename of the Debian distribution.

@action_store.kubiya_action()
def delete_a_debian_group_distribution(input: DeleteADebianGroupDistribution):
    return delete_wrapper(endpoint=f"/groups/{input.id}/-/debian_distributions/{input.codename}", args=input.dict(exclude_none=True))
