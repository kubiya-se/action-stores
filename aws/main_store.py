import kubiya

# ActionStore is a singleton that stores all the actions in the application

store = kubiya.ActionStore("aws", "0.1.0")
store.uses_secrets(["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN"])

from .actions import ec2_actions, iam_actions, ecr_actions, ecs_actions, cloudwatch_actions, eks_actions, lambda_actions