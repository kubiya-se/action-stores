from typing import List, Any, Dict
from kubiya import ActionStore
from requests_wrapper import *

action_store.uses_secrets(["ARGO_TOKEN"])
action_store = ActionStore("argo", version="0.0.3")