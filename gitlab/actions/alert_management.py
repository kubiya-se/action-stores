from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ListMetricImages(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user.

    alert_iid: int # The internal ID of a project’s alert.


@action_store.kubiya_action()
def list_metric_images(input: ListMetricImages):
    return get_wrapper(endpoint=f"/projects/{input.id}/alert_management_alerts/{input.alert_iid}/metric_images", args=input.dict(exclude_none=True))


class UpdateMetricImage(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user.

    alert_iid: int # The internal ID of a project’s alert.

    image_id: int # The ID of the image.

    url: Optional[str] = None # The URL to view more metrics information.

    url_text: Optional[str] = None # A description of the image or URL.


@action_store.kubiya_action()
def update_metric_image(input: UpdateMetricImage):
    return put_wrapper(endpoint=f"/projects/{input.id}/alert_management_alerts/{input.alert_iid}/metric_images/{input.image_id}", args=input.dict(exclude_none=True))


class DeleteMetricImage(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user.

    alert_iid: int # The internal ID of a project’s alert.

    image_id: int # The ID of the image.


@action_store.kubiya_action()
def delete_metric_image(input: DeleteMetricImage):
    return delete_wrapper(endpoint=f"/projects/{input.id}/alert_management_alerts/{input.alert_iid}/metric_images/{input.image_id}", args=input.dict(exclude_none=True))
