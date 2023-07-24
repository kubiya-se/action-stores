from typing import List, Any
from pydantic import BaseModel
from . import action_store as action_store
from ..http_wrapper import get_wrapper

class JenkinsNode(BaseModel):
    displayName: str
    offline: bool

@action_store.kubiya_action()
def list_jenkins_nodes(_: Any = None) -> List[JenkinsNode]:
    return get_wrapper("/computer/api/json?tree=computer[displayName,offline]")
