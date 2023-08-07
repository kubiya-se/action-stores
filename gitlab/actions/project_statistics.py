from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from .. import action_store as action_store
from ..http_wrapper import *
from ..models.project_statistics import *


@action_store.kubiya_action()
def get_project_statistics(input: ProjectStatInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/statistics')
    return ListDict(response=response)