from typing import List, Any
from pydantic import BaseModel
from . import action_store as action_store
from ..http_wrapper import get_wrapper

class Plugin(BaseModel):
    shortName: str
    longName: str

@action_store.kubiya_action()
def list_jenkins_plugins(_: Any = None) -> List[Plugin]:
    return get_wrapper("/pluginManager/api/json?depth=1&tree=plugins[shortName,longName]")
