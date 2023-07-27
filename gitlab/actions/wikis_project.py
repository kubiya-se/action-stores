from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.wikis_project import *
@action_store.kubiya_action()
def list_wiki_pages(input: ProjectsIdWikis):
    return get_wrapper(endpoint=f'/projects/{input.id}/wikis', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_wiki_page(input: ProjectsIdWikisSlug):
    return get_wrapper(endpoint=f'/projects/{input.id}/wikis/{input.slug}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_new_wiki_page(input: ProjectsIdWikisCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/wikis', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_an_existing_wiki_page(input: GroupsIdWikisSlugEdit):
    return put_wrapper(endpoint=f'/projects/{input.id}/wikis/{input.slug}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_wiki_page(input: ProjectsIdWikisSlugDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/wikis/{input.slug}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def upload_an_attachment_to_the_wiki_repository(input: ProjectsIdWikisAttachments):
    return post_wrapper(endpoint=f'/projects/{input.id}/wikis/attachments', args=input.dict(exclude_none=True))