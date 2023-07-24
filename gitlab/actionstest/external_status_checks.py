from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.external_status_checks import *
@action_store.kubiya_action()
def get_project_external_status_check_services(input: ProjectsIdExternalstatuschecks):
    return get_wrapper(endpoint=f'/projects/{input.id}/external_status_checks', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_external_status_check_service(input: CreateUpdateExternalStatusCheckService):
    return post_wrapper(endpoint=f'/projects/{input.id}/external_status_checks', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_external_status_check_service(input: UpdateExternalStatusCheckService):
    return put_wrapper(endpoint=f'/projects/{input.id}/external_status_checks/{input.check_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_external_status_check_service(input: DeleteExternalStatusCheckService):
    return delete_wrapper(endpoint=f'/projects/{input.id}/external_status_checks/{input.check_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_status_checks_for_merge_request(input: MergeRequestStatusChecks):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/status_checks', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_status_of_external_status_check(input: SetStatusCheck):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/status_check_responses', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retry_failed_status_check_for_merge_request(input: RetryFailedStatusCheck):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/status_checks/{input.external_status_check_id}/retry', args=input.dict(exclude_none=True))