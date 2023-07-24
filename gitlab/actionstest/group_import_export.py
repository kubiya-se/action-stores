from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.group_import_export import *
@action_store.kubiya_action()
def schedule_new_export(input: GroupExport):
    return post_wrapper(endpoint=f'/groups/{input.id}/export', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_export(input: GroupExport):
    return get_wrapper(endpoint=f'/groups/{input.id}/export/download', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def import_group(input: GroupImport):
    return post_wrapper(endpoint='/groups/import', args=input.dict(exclude_none=True))