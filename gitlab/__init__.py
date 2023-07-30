from kubiya import ActionStore


action_store = ActionStore("gitlab", "0.1.0")
action_store.uses_secrets(["GITLAB_URL", "GITLAB_TOKEN"])