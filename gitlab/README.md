# GitLab API
We use the GitLab REST API for all of our action stores: https://docs.gitlab.com/ee/api/repositories.html#merge-base

# Testing

## Bundling, Deploying
1. Secrets can be added via the Kubiya UI at https://app.kubiya.ai
2. We bundle using ttl.sh, an ephemeral Docker container
    ``` kubiya-cli action-store bundle -n action-store-gitlab -p action-store-gitlab -i ttl.sh/action-store-gitlab:24h ```
3. We deploy using our test team runner (teamrunner)
    ``` kubiya-cli action-store deploy -n action-store-gitlab -r teamrunner -i ttl.sh/action-store-gitlab:24h```
4. Then, build a test workflow in the Kubiya platform to deploy the working code, see any issues.

## Errors and Logs
1. ssh using ``` ssh -i "michaelsec2keypair.pem" ubuntu@ec2-18-233-97-45.compute-1.amazonaws.com```
2. Verify you're in the right pod: kind-team using ```kubectl config current-context ```
3. To see pods, use ```kubectl get pods -n openfaas-fn ```
4. To get logs, use ```kubectl logs -n openfaas-fn (action store pod name from previous line) ```


## Tests
* ``` betterclassnames.py ``` : (in progress) A way to rename the pydantic class inputs to functions based on the ac.tion store name
    *   I'm currently using ``` projectstest.py ```  as my testing module for renaming class names automatically
* ``` repeatedclasses.py ``` : Double-check if you accidentally named two pydantic classes the same thing
    * Be aware of which directory you run this in


# Coding Notes 
## Known Limitations and Issues
* **Enums and Validators**: I used Enums and the python @validator for fields where it's "one or the other", such as in wikis_group.py. The user either needs to specify title or content. I'm still a little unsure of how well it operates
* **Uploading Files**: How should we upload files to GitLab, such as avatars? All we have is a string input. 
* **Visual Review Discussions API**: This is planned for removal in May 2022 (Gitlab 17.0)

