from .. import action_store as action_store
import logging
from ..models.orgs import *
from ..http_wrapper import get_wrapper, post_wrapper, patch_wrapper, delete_wrapper, put_wrapper

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def list_orgs(_: Any=None):
    response = get_wrapper("/organizations")
    return response

@action_store.kubiya_action()
def get_org(params: OrgParams):
    response = get_wrapper(f"/orgs/{params.name}")
    return response 