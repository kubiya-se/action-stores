from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.alert_management import *

@action_store.kubiya_action()
def list_metric_images(input: ListMetricImages):
    return get_wrapper(endpoint=f'/projects/{input.id}/alert_management_alerts/{input.alert_iid}/metric_images', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_metric_image(input: UpdateMetricImage):
    return put_wrapper(endpoint=f'/projects/{input.id}/alert_management_alerts/{input.alert_iid}/metric_images/{input.image_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_metric_image(input: DeleteMetricImage):
    return delete_wrapper(endpoint=f'/projects/{input.id}/alert_management_alerts/{input.alert_iid}/metric_images/{input.image_id}', args=input.dict(exclude_none=True))