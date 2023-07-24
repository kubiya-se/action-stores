from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field, validator
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from enum import Enum


class GroupsIdWikis(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group

    with_content: Optional[bool] = None # Include pages’ content


@action_store.kubiya_action()
def list_wiki_pages(input: GroupsIdWikis):
    return get_wrapper(endpoint=f"/groups/{input.id}/wikis", args=input.dict(exclude_none=True))


class GroupsIdWikisSlug(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group

    slug: str # URL-encoded slug (a unique string) of the wiki page, such as dir%2Fpage_name

    render_html: Optional[bool] = None # Return the rendered HTML of the wiki page

    version: Optional[str] = None # Wiki page version SHA



@action_store.kubiya_action()
def get_a_wiki_page(input: GroupsIdWikisSlug):
    return get_wrapper(endpoint=f"/groups/{input.id}/wikis/{input.slug}", args=input.dict(exclude_none=True))


class GroupsIdWikisCreate(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group

    content: str # The content of the wiki page

    title: str # The title of the wiki page

    format: Optional[str] = None # The format of the wiki page. Available formats are: markdown (default), rdoc, asciidoc and org


@action_store.kubiya_action()
def create_a_new_wiki_page(input: GroupsIdWikisCreate):
    return post_wrapper(endpoint=f"/groups/{input.id}/wikis", args=input.dict(exclude_none=True))

class WikiFormat(str, Enum):
    markdown = "markdown"
    rdoc = "rdoc"
    asciidoc = "asciidoc"
    org = "org"

class GroupsIdWikisSlugEdit(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group.
    content: str # The content of the wiki page.
    title: str # The title of the wiki page.
    format: Optional[WikiFormat] = None # The format of the wiki page. Available formats are markdown (default), rdoc, asciidoc, and org.
    slug: str # URL encoded slug (a unique string) of the wiki page. For example: dir%2Fpage_name.

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v



@action_store.kubiya_action()
def edit_an_existing_wiki_page(input: GroupsIdWikisSlugEdit):
    return put_wrapper(endpoint=f"/groups/{input.id}/wikis/{input.slug}", args=input.dict(exclude_none=True))


class GroupsIdWikisSlugDelete(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group

    slug: str # URL-encoded slug (a unique string) of the wiki page, such as dir%2Fpage_name


@action_store.kubiya_action()
def delete_a_wiki_page(input: GroupsIdWikisSlugDelete):
    return delete_wrapper(endpoint=f"/groups/{input.id}/wikis/{input.slug}", args=input.dict(exclude_none=True))


class GroupsIdWikisAttachments(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group

    file: str # The attachment to be uploaded

    branch: Optional[str] = None # The name of the branch. Defaults to the wiki repository default branch


@action_store.kubiya_action()
def upload_an_attachment_to_the_wiki_repository(input: GroupsIdWikisAttachments):
    return post_wrapper(endpoint=f"/groups/{input.id}/wikis/attachments", args=input.dict(exclude_none=True))