# GitLab API
We use the GitLab REST API for all of our action stores: https://docs.gitlab.com/ee/api/repositories.html#merge-base

# Gen2 Structure
Modules

# Testing

## Bundling, Deploying
1. Secrets can be added via the Kubiya UI at https://app.kubiya.ai
2. We bundle using ttl.sh, an ephemeral Docker container
    ``` kubiya-cli action-store bundle -n action-store-gitlab -p action-store-gitlab -i ttl.sh/action-store-gitlab:24h ```
3. We deploy using our test team runner (teamrunner)
    ``` kubiya-cli action-store deploy -n action-store-gitlab -r teamrunner -i ttl.sh/action-store-gitlab:24h```
4. Then, build a test workflow in the Kubiya platform to deploy the working code, see any issues.

## Errors and Logs
1. ssh using ``` ssh -i "<keypem>" <address of EC2 instance>```
2. Verify you're in the right pod: kind-team using ```kubectl config current-context ```
3. To see pods, use ```kubectl get pods -n openfaas-fn ```
4. To get logs, use ```kubectl logs -n openfaas-fn (action store pod name from previous line) ```


## Tests
* ``` betterclassnames.py ``` : (discontinued) A way to rename the pydantic class inputs to functions based on the action store name
    *   I'm currently using ``` projectstest.py ```  as my testing module for renaming class names automatically
* ``` repeatedclasses.py ``` : Double-check if you accidentally named two pydantic classes the same thing
    * Be aware of which directory you run this in


# Coding Notes 
## Known Limitations and Issues
* **Uploading Files**: I'm not sure how the current UI interfaces to allow file uploads - feel free to slack me if you understand. 
* **Visual Review Discussions API**: This is planned for removal in May 2022 (Gitlab 17.0)

