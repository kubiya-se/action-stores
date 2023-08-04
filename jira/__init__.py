from kubiya import ActionStore

action_store = ActionStore("arnav-jira", "0.1.0")

action_store.uses_secrets(["JIRA_URL", "JIRA_USERNAME", "JIRA_PASSWORD"])