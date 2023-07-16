
import logging as log
from . import action_store
from .bitbucket_actions import get_client


def health_check():    
    org = action_store.secrets["BITBUCKET_SPACE"]
    user = action_store.secrets["BITBUCKET_USERNAME"]
    pwd = action_store.secrets["BITBUCKET_APP_PASSWORD"]
    return _param(user) & _param(pwd) & _param(org) & _conn(org)

def _conn(v: str) -> bool:
    try:
        c = get_client(v)
        return c.get_user().login != ""
    except Exception as e:
        log.error("[error]", exception=str(e))
        return False


def _param(p: str) -> bool:
    return p is not None & p != ""

