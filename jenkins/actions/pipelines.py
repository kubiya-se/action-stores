from typing import List, Any
from pydantic import BaseModel
from . import action_store as action_store
from ..http_wrapper import get_wrapper

class JenkinsPipeline(BaseModel):
    name: str
    url: str

@action_store.kubiya_action()
def list_jenkins_pipelines(_: Any = None) -> List[JenkinsPipeline]:
    return get_wrapper("/api/json?tree=jobs[name,url]")