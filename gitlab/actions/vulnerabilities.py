from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class VulnerabilitiesId(BaseModel):
    id: Union[int,str]  # The ID of a Vulnerability to get


@action_store.kubiya_action()
def single_vulnerability(input: VulnerabilitiesId):
    return get_wrapper(endpoint=f"/vulnerabilities/{input.id}", args=input.dict(exclude_none=True))


class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int,str]  # The ID of a vulnerability to confirm


@action_store.kubiya_action()
def confirm_vulnerability(input: VulnerabilitiesIdConfirm):
    return post_wrapper(endpoint=f"/vulnerabilities/{input.id}/confirm", args=input.dict(exclude_none=True))


class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int,str]  # The ID of a Vulnerability to resolve


@action_store.kubiya_action()
def resolve_vulnerability(input: VulnerabilitiesIdResolve):
    return post_wrapper(endpoint=f"/vulnerabilities/{input.id}/resolve", args=input.dict(exclude_none=True))


class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int,str]  # The ID of a vulnerability to dismiss


@action_store.kubiya_action()
def dismiss_vulnerability(input: VulnerabilitiesIdDismiss):
    return post_wrapper(endpoint=f"/vulnerabilities/{input.id}/dismiss", args=input.dict(exclude_none=True))


class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int,str]  # The ID of a vulnerability to revert to detected state


@action_store.kubiya_action()
def revert_vulnerability_to_detected_state(input: VulnerabilitiesIdRevert):
    return post_wrapper(endpoint=f"/vulnerabilities/{input.id}/revert", args=input.dict(exclude_none=True))
