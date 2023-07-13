
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

@action_store.kubiya_action()
def get_current_queue_metrics(input: None):
    return get_wrapper(endpoint="/sidekiq/queue_metrics")

@action_store.kubiya_action()
def get_current_process_metrics(input: None):
    return get_wrapper(endpoint="/sidekiq/process_metrics")


@action_store.kubiya_action()
def get_current_job_stats(input: None):
    return get_wrapper(endpoint="/sidekiq/job_stats")

@action_store.kubiya_action()
def get_compound_metrics(input: None):
    return get_wrapper(endpoint="/sidekiq/compound_metrics")
