from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any