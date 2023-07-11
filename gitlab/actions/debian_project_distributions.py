from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime



class ListAllDebianDistributionsInAProject(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.#
    codename: Optional[str] = None # Filter with a specific codename.
    suite: Optional[str] = None # Filter with a specific suite.


@action_store.kubiya_action()
def list_all_debian_distributions_in_a_project(input: ListAllDebianDistributionsInAProject):
    return get_wrapper(endpoint=f"/projects/{input.id}/debian_distributions", args=input.dict(exclude_none=True))


class SingleDebianProjectDistribution(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project owned by the authenticated user.

    codename: int # The codename of a distribution.


@action_store.kubiya_action()
def single_debian_project_distribution(input: SingleDebianProjectDistribution):
    return get_wrapper(endpoint=f"/projects/{input.id}/debian_distributions/{input.codename}", args=input.dict(exclude_none=True))


class SingleDebianProjectDistributionKey(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    codename: int # The codename of a distribution.


@action_store.kubiya_action()
def single_debian_project_distribution_key(input: SingleDebianProjectDistributionKey):
    return get_wrapper(endpoint=f"/projects/{input.id}/debian_distributions/{input.codename}/key.asc", args=input.dict(exclude_none=True))


class CreateADebianProjectDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    codename: str # The Debian distribution’s codename.

    suite: Optional[str] = None # The new Debian distribution’s suite.

    origin: Optional[str] = None # The new Debian distribution’s origin.

    label: Optional[str] = None # The new Debian distribution’s label.

    version: Optional[str] = None # The new Debian distribution’s version.

    description: Optional[str] = None # The new Debian distribution’s description.

    valid_time_duration_seconds: Optional[int] = None # The new Debian distribution’s valid time duration (in seconds).

    components: Optional[List[str]] = None # The new Debian distribution’s list of components.

    architectures: Optional[List[str]] = None # The new Debian distribution’s list of architectures.


@action_store.kubiya_action()
def create_a_debian_project_distribution(input: CreateADebianProjectDistribution):
    return post_wrapper(endpoint=f"/projects/{input.id}/debian_distributions", args=input.dict(exclude_none=True))


class UpdateADebianProjectDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    codename: str # The Debian distribution’s codename.

    suite: Optional[str] = None # The Debian distribution’s new suite.

    origin: Optional[str] = None # The Debian distribution’s new origin.

    label: Optional[str] = None # The Debian distribution’s new label.

    version: Optional[str] = None # The Debian distribution’s new version.

    description: Optional[str] = None # The Debian distribution’s new description.

    valid_time_duration_seconds: Optional[int] = None # The Debian distribution’s new valid time duration (in seconds).

    components: Optional[List[str]] = None # The Debian distribution’s new list of components.

    architectures: Optional[List[str]] = None # The Debian distribution’s new list of architectures.


@action_store.kubiya_action()
def update_a_debian_project_distribution(input: UpdateADebianProjectDistribution):
    return put_wrapper(endpoint=f"/projects/{input.id}/debian_distributions/{input.codename}", args=input.dict(exclude_none=True))


class DeleteADebianProjectDistribution(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the project owned by the authenticated user.

    codename: int # The Debian distribution’s codename.


@action_store.kubiya_action()
def delete_a_debian_project_distribution(input: DeleteADebianProjectDistribution):
    return delete_wrapper(endpoint=f"/projects/{input.id}/debian_distributions/{input.codename}", args=input.dict(exclude_none=True))
