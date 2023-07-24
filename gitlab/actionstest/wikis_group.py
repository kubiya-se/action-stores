from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.wikis_group import *
@action_store.kubiya_action()
def list_wiki_pages(input: GroupsIdWikis):
    return get_wrapper(endpoint=f'/groups/{input.id}/wikis', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_wiki_page(input: GroupsIdWikisSlug):
    return get_wrapper(endpoint=f'/groups/{input.id}/wikis/{input.slug}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_new_wiki_page(input: GroupsIdWikisCreate):
    return post_wrapper(endpoint=f'/groups/{input.id}/wikis', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_an_existing_wiki_page(input: GroupsIdWikisSlugEdit):
    return put_wrapper(endpoint=f'/groups/{input.id}/wikis/{input.slug}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_wiki_page(input: GroupsIdWikisSlugDelete):
    return delete_wrapper(endpoint=f'/groups/{input.id}/wikis/{input.slug}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def upload_an_attachment_to_the_wiki_repository(input: GroupsIdWikisAttachments):
    return post_wrapper(endpoint=f'/groups/{input.id}/wikis/attachments', args=input.dict(exclude_none=True))