import time
from os import environ
from pprint import pprint
from kubiya import ActionStore, get_secret


action_store = ActionStore("action-store-gitlab", "0.1.0")
action_store.uses_secrets(["GITLAB_URL", "GITLAB_TOKEN"])