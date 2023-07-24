from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.vulnerabilities import *
@action_store.kubiya_action()
def single_vulnerability(input: VulnerabilitiesId):
    return get_wrapper(endpoint=f'/vulnerabilities/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def confirm_vulnerability(input: VulnerabilitiesIdConfirm):
    return post_wrapper(endpoint=f'/vulnerabilities/{input.id}/confirm', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def resolve_vulnerability(input: VulnerabilitiesIdResolve):
    return post_wrapper(endpoint=f'/vulnerabilities/{input.id}/resolve', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def dismiss_vulnerability(input: VulnerabilitiesIdDismiss):
    return post_wrapper(endpoint=f'/vulnerabilities/{input.id}/dismiss', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def revert_vulnerability_to_detected_state(input: VulnerabilitiesIdRevert):
    return post_wrapper(endpoint=f'/vulnerabilities/{input.id}/revert', args=input.dict(exclude_none=True))