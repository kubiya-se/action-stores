from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.ruby_gems import *
@action_store.kubiya_action()
def download_a_gem_file(input: DownloadGemFile):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/rubygems/gems/{input.file_name}')
@action_store.kubiya_action()
def fetch_a_list_of_dependencies(input: FetchDependencies):
    return get_wrapper(endpoint=f'/projects/{input.id}/packages/rubygems/api/v1/dependencies', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def upload_a_gem_file(input: UploadGemFile):
    return post_wrapper(endpoint=f'/projects/{input.id}/packages/rubygems/api/v1/gems', files={'file': input.file})