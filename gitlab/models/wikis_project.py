from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None