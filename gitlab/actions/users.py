from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.users import *

from .. import action_store as action_store
from ..http_wrapper import *

@action_store.kubiya_action()
def list_users(input: ListUsersInput):
    response = get_wrapper(endpoint='/users', args=input.dict(exclude_none=True))
    #return ListUsersOutput(users=response)
    return ListDict(response=response)

@action_store.kubiya_action()
def get_user(input: GetUserInput):
    response = get_wrapper(endpoint=f'/users/{input.id}')
    #return User(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def create_user(input: CreateUserInput):
    response = post_wrapper(endpoint='/users', data=input.dict(exclude_none=True))
    #return User(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def modify_user(input: ModifyUserInput):
    response = put_wrapper(endpoint=f'/users/{input.id}', data=input.dict(exclude_none=True, exclude={'id'}))
    #return User(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def delete_user(input: DeleteUserInput):
    response = delete_wrapper(endpoint=f'/users/{input.id}', data=input.dict(exclude_none=True, exclude={'id'}))
    #return response
    return SingleDict(response=response)

@action_store.kubiya_action()
def get_current_user():
    response = get_wrapper(endpoint='/user')
    #return User(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def get_current_user_status():
    response = get_wrapper(endpoint='/user/status')
    #return UserStatus(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def get_user_status(id_or_username: str):
    response = get_wrapper(endpoint=f'/users/{id_or_username}/status')
    #return UserStatus(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def set_user_status(input: SetUserStatusInput):
    response = put_wrapper(endpoint='/user/status', data=input.dict(exclude_none=True))
    #return UserStatus(**response)
    return SingleDict(response=response)

@action_store.kubiya_action()
def get_user_preferences():
    response = get_wrapper(endpoint='/user/preferences')
    #return UserPreferences(**response)
    return SingleDict(response=response)
