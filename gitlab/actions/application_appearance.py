from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


@action_store.kubiya_action()
def get_current_appearance_configuration():
    return get_wrapper(endpoint=f"/application/appearance", args=input.dict(exclude_none=True))


class ApplicationAppearance(BaseModel):

    title: Optional[str] = None # Instance title on the sign in / sign up page

    description: Optional[str] = None # Markdown text shown on the sign in / sign up page

    pwa_name: Optional[str] = None # Full name of the Progressive Web App. Used for the attribute name in manifest.json. Introduced in GitLab 15.8.

    pwa_short_name: Optional[str] = None # Short name for Progressive Web App. Introduced in GitLab 15.8.

    pwa_description: Optional[str] = None # An explanation of what the Progressive Web App does. Used for the attribute description in manifest.json. Introduced in GitLab 15.8.

    pwa_icon: Optional[Any] = None # Icon used for Progressive Web App. See Change logo. Introduced in GitLab 15.8.

    logo: Optional[Any] = None # Instance image used on the sign in / sign up page. See Change logo

    header_logo: Optional[Any] = None # Instance image used for the main navigation bar

    favicon: Optional[Any] = None # Instance favicon in .ico or .png format

    new_project_guidelines: Optional[str] = None # Markdown text shown on the new project page

    profile_image_guidelines: Optional[str] = None # Markdown text shown on the profile page below Public Avatar

    header_message: Optional[str] = None # Message in the system header bar

    footer_message: Optional[str] = None # Message in the system footer bar

    message_background_color: Optional[str] = None # Background color for the system header / footer bar

    message_font_color: Optional[str] = None # Font color for the system header / footer bar

    email_header_and_footer_enabled: Optional[bool] = None # Add header and footer to all outgoing emails if enabled


@action_store.kubiya_action()
def change_appearance_configuration(input: ApplicationAppearance):
    return put_wrapper(endpoint=f"/application/appearance", args=input.dict(exclude_none=True))


class ChangeLogo(BaseModel):

    logo: Any # File to upload

    pwa_icon: Any # File to upload. Introduced in GitLab 15.8.


@action_store.kubiya_action()
def change_logo(input: ChangeLogo):
    return put_wrapper(endpoint=f"/application/appearance", args=input.dict(exclude_none=True))