from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.merge_trains import *
@action_store.kubiya_action()
def list_merge_trains_for_a_project(input: MergeTrainsGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_trains', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_merge_requests_in_a_merge_train(input: MergeTrainsTargetBranchGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_trains/{input.target_branch}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_the_status_of_a_merge_request_on_a_merge_train(input: MergeTrainStatusGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_trains/merge_requests/{input.merge_request_iid}')
@action_store.kubiya_action()
def add_a_merge_request_to_a_merge_train(input: MergeTrainAdd):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_trains/merge_requests/{input.merge_request_iid}', args=input.dict(exclude_none=True))