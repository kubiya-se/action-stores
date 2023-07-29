import kubiya


action_store = kubiya.ActionStore("action-store-gitlab", "0.1.0")
action_store.uses_secrets(["GITLAB_URL", "GITLAB_TOKEN"])

from .actions import(
    projects,
    groups,
    merge_requests,
    issues
)
