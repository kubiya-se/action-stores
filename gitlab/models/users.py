from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime

class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict

class ListUsersInput(BaseModel):
    username: Optional[str] = None
    extern_uid: Optional[str] = None
    provider: Optional[str] = None
    search: Optional[str] = None
    active: Optional[bool] = None
    external: Optional[bool] = None
    exclude_external: Optional[bool] = None
    blocked: Optional[bool] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    exclude_internal: Optional[bool] = None
    without_project_bots: Optional[bool] = None

class User(BaseModel):
    id: int
    username: str
    name: str
    state: str
    avatar_url: str
    web_url: str

class ListUsersOutput(BaseModel):
    users: List[User]
    
class GetUserInput(BaseModel):
    id: int

class CreateUserInput(BaseModel):
    admin: Optional[bool] = None
    auditor: Optional[bool] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    can_create_group: Optional[bool] = None
    color_scheme_id: Optional[int] = None
    email: str
    extern_uid: Optional[str] = None
    external: Optional[bool] = None
    extra_shared_runners_minutes_limit: Optional[int] = None
    force_random_password: Optional[bool] = None
    group_id_for_saml: Optional[int] = None
    linkedin: Optional[str] = None
    location: Optional[str] = None
    name: str
    note: Optional[str] = None
    organization: Optional[str] = None
    password: Optional[str] = None
    private_profile: Optional[bool] = None
    projects_limit: Optional[int] = None
    provider: Optional[str] = None
    reset_password: Optional[bool] = None
    shared_runners_minutes_limit: Optional[int] = None
    skip_confirmation: Optional[bool] = None
    skype: Optional[str] = None
    theme_id: Optional[int] = None
    twitter: Optional[str] = None
    discord: Optional[str] = None
    username: str
    view_diffs_file_by_file: Optional[bool] = None
    website_url: Optional[str] = None

class ModifyUserInput(BaseModel):
    id: int
    admin: Optional[bool] = None
    auditor: Optional[bool] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    can_create_group: Optional[bool] = None
    color_scheme_id: Optional[int] = None
    commit_email: Optional[str] = None
    email: Optional[str] = None
    extern_uid: Optional[str] = None
    external: Optional[bool] = None
    extra_shared_runners_minutes_limit: Optional[int] = None
    group_id_for_saml: Optional[int] = None
    linkedin: Optional[str] = None
    location: Optional[str] = None
    name: Optional[str] = None
    note: Optional[str] = None
    organization: Optional[str] = None
    password: Optional[str] = None
    private_profile: Optional[bool] = None
    projects_limit: Optional[int] = None
    pronouns: Optional[str] = None
    provider: Optional[str] = None
    public_email: Optional[str] = None
    shared_runners_minutes_limit: Optional[int] = None
    skip_reconfirmation: Optional[bool] = None
    skype: Optional[str] = None
    theme_id: Optional[int] = None
    twitter: Optional[str] = None
    discord: Optional[str] = None
    username: Optional[str] = None
    view_diffs_file_by_file: Optional[bool] = None
    website_url: Optional[str] = None


class DeleteUserInput(BaseModel):
    id: int
    hard_delete: Optional[bool] = None

class UserStatus(BaseModel):
    emoji: str
    availability: str
    message: str
    message_html: str
    clear_status_at: Optional[str] = None

class SetUserStatusInput(BaseModel):
    emoji: Optional[str] = None
    message: Optional[str] = None
    clear_status_after: Optional[str] = None

class UserPreferences(BaseModel):
    id: int
    user_id: int
    view_diffs_file_by_file: bool
    show_whitespace_in_diffs: bool
    pass_user_identities_to_ci_jwt: bool