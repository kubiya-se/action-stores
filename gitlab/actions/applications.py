from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class Applications(BaseModel):
    name: str  # Name of the application.
    redirect_uri: str  # Redirect URI of the application.
    scopes: str  # Scopes of the application. You can specify multiple scopes by separating each scope using a space.
    confidential: Optional[bool] = None # The application is used where the client secret can be kept confidential. Native mobile apps and Single Page Apps are considered non-confidential. Defaults to true if not supplied


@action_store.kubiya_action()
def create_an_application(input: Applications):
    return post_wrapper(endpoint=f"/applications", args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def list_all_applications(input=None):
    return get_wrapper(endpoint=f"/applications", args=input)


class ApplicationsId(BaseModel):
    id: int  # The ID of the application (not the application_id


@action_store.kubiya_action()
def delete_an_application(input: ApplicationsId):
    return delete_wrapper(endpoint=f"/applications/{input.id}", args=input.dict(exclude_none=True))
