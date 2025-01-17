import typing
import requests

from .base import BaseClient


class Client(BaseClient):
    def __init__(self, user, password, owner=None):
        """Initial session with user/password, and setup repository owner

        Args:
            params:

        Returns:

        """
        super().__init__(user, password, owner)

        # for shared repo, set baseURL to owner
        if owner is None:
            user_data = self.get_user()
            owner = user_data.get("username")
        self.workspace = owner

    def all_pages(
        self,
        method: typing.Callable[..., typing.Union[typing.Dict, None]],
        *args,
        **kwargs,
    ) -> typing.Generator[typing.Dict[str, typing.Any], None, None]:
        """
        Retrieves all pages in the response from a BitBucket API list endpoint and yields a generator for the items in the
        response.

        Example:

        ```python
        for item in client.all_pages(
            client.get_issues,
            "{726f1aab-826f-4c08-a127-1224347b3d09}"
        ):
            print(item["id"])
        ```

        Args:
            method: A client class method to retrieve all pages from.
            *args: Variable length argument list to be passed to the `method` callable.
            **kwargs: Arbitrary keyword arguments to be passed to the `method` callable.

        Returns:
            A generator that yields a dictionary of item data for each item in the response.

        Raises:
            Any exceptions raised by the `method` callable.
        """
        resp = method(*args, **kwargs)
        while True:
            if resp is None:
                break

            yield from resp["values"]

            if "next" not in resp:
                break
            resp = self._get(resp["next"])

    def get_user(self, params=None):
        """Returns the currently logged in user.

        Args:
            params:

        Returns:

        """
        return self._get("2.0/user", params=params)

    def get_privileges(self, params=None):
        """Gets a list of all the privilege across all an account's repositories.
        If a repository has no individual users with privileges, it does not appear in this list.
        Only the repository owner, a team account administrator, or an account with administrative
        rights on the repository can make this call. This method has the following parameters:


        Args:
            params:

        Returns:

        """
        return self._get("1.0/privileges/{}".format(self.workspace), params=params)

    def get_repositories(self, params=None):
        """Returns a paginated list of all repositories owned by the specified account or UUID.

        The result can be narrowed down based on the authenticated user's role.

        E.g. with ?role=contributor, only those repositories that the authenticated user has write access to are
        returned (this includes any repo the user is an admin on, as that implies write access).

        This endpoint also supports filtering and sorting of the results. See filtering and sorting for more details.

        Args:
            params:

        Returns:

        """
        return self._get("2.0/repositories/{}".format(self.workspace), params=params)

    def get_repository(self, repository_slug, params=None):
        """Returns the object describing this repository.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}".format(self.workspace, repository_slug),
            params=params,
        )

    def create_repository(self, params=None, data=None, name=None, team=None):
        """Creates a new repository.

        Example:
            {
              "scm": "git",
              "description": "Repository Description",
              "is_private": boolean,
              "project": [
                "key": "Project key"
              ]
            }

        Args:
            data:
            params:
            Name:
            team:
        Returns: Repository
        """
        return self._post(
            "2.0/repositories/{}/{}".format(team or self.workspace, name), params, data
        )

    def get_repository_branches(self, repository_slug, params=None):
        return self._get(
            "2.0/repositories/{}/{}/refs/branches".format(
                self.workspace, repository_slug
            ),
            params=params,
        )

    def get_repository_tags(self, repository_slug, params=None):
        return self._get(
            "2.0/repositories/{}/{}/refs/tags".format(self.workspace, repository_slug),
            params=params,
        )

    def get_repository_commits(self, repository_slug, params=None):
        """Returns the commits from the repository.

        Params can be used to return commits from a branch like this:

            params={'include': 'branch'}

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/commits".format(self.workspace, repository_slug),
            params=params,
        )

    def get_repository_components(self, repository_slug, params=None):
        """Returns the components that have been defined in the issue tracker.

        This resource is only available on repositories that have the issue tracker enabled.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/components".format(self.workspace, repository_slug),
            params=params,
        )

    def get_repository_milestones(self, repository_slug, params=None):
        """Returns the milestones that have been defined in the issue tracker.

        This resource is only available on repositories that have the issue tracker enabled.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/milestones".format(self.workspace, repository_slug),
            params=params,
        )

    def get_repository_versions(self, repository_slug, params=None):
        """Returns the versions that have been defined in the issue tracker.

        This resource is only available on repositories that have the issue tracker enabled.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/versions".format(self.workspace, repository_slug),
            params=params,
        )

    def get_repository_source_code(
        self, repository_slug, branch_or_commit, params=None
    ):
        """Returns data about the source code of given repository.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/src/{}/".format(
                self.workspace, repository_slug, branch_or_commit
            ),
            params=params,
        )

    def get_repository_folder_source_code(
        self, repository_slug, branch_or_commit, path="", params=None
    ):
        return self._get(
            "2.0/repositories/{}/{}/src/{}/{}".format(
                self.workspace, repository_slug, branch_or_commit, path
            ),
            params=params,
        )

    def get_repository_structure(self, repository_slug, branch_or_commit, params=None):
        objs = list(
            self.all_pages(
                self.get_repository_source_code,
                repository_slug,
                branch_or_commit,
                params=params,
            )
        )
        return self._get_objs(repository_slug, objs, params=params)

    def get_open_pull_requests(self, repository_slug, params=None):
        """Returns a paginated list of open pull requests from the specified repository.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/pullrequests".format(
                self.workspace, repository_slug
            ),
            params=params,
        )

    def create_pull_request(
        self, repository_slug, title, source_branch, destination_branch, params=None
    ):
        data = {
            "title": title,
            "source": {"branch": {"name": source_branch}},
            "destination": {"branch": {"name": destination_branch}},
        }

        return self._post(
            "2.0/repositories/{}/{}/pullrequests".format(
                self.workspace, repository_slug
            ),
            data=data,
            params=params,
        )

    def merge_pull_request(self, repository_slug, pull_request_id, params=None):
        return self._post(
            "2.0/repositories/{}/{}/pullrequests/{}/merge".format(
                self.workspace, repository_slug, pull_request_id
            ),
            params=params,
        )

    def _get_objs(
        self,
        repository_slug: str,
        objs: typing.List[typing.Dict[str, typing.Any]],
        params=None,
    ) -> typing.List[dict[str, typing.Any]]:
        files = []
        for obj in objs:
            if obj.get("type") == "commit_directory":
                link = obj.get("links", {}).get("self", {}).get("href")
                print(f"link: {link}")
                if link is None:
                    continue
                folder_objs = list(self.all_pages(self._get, link, params=params))
                files = files + self._get_objs(
                    repository_slug, folder_objs, params=params
                )
            elif obj.get("type") == "commit_file":
                files.append(
                    {
                        "path": obj["path"],
                        "commit_hash": obj["commit"]["hash"],
                    }
                )
        return files

    def get_repository_commit_path_source_code(
        self, repository_slug, commit_hash, path, params=None
    ):
        """Returns source code of given path at specified commit_hash of given repository.

        Args:
            repository_slug:
            commit_hash:
            path:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/src/{}/{}".format(
                self.workspace, repository_slug, commit_hash, path
            ),
            params=params,
        )

    def post_repository_files(
        self,
        repository_slug: str,
        commit_message: str,
        branch: str,
        files: dict,
        params=None,
    ):
        """files ex.
        files = {
            "folder123/file1": ("file1", "content"),
            "folder123/file2": ("file2", "content2"),
        }
        """

        return self._post_files(
            "2.0/repositories/{}/{}/src".format(self.workspace, repository_slug),
            params=params,
            data={
                "message": commit_message,
                "branch": branch,
            },
            files=files,
        )

    def create_issue(self, repository_slug, data, params=None):
        """Creates a new issue.

        This call requires authentication. Private repositories or private issue trackers require
        the caller to authenticate with an account that has appropriate authorisation.

        The authenticated user is used for the issue's reporter field.

        Args:
            repository_slug:
            data:
            params:

        Returns:

        """
        return self._post(
            "2.0/repositories/{}/{}/issues".format(self.workspace, repository_slug),
            data=data,
            params=params,
        )

    def get_issue(self, repository_slug, issue_id, params=None):
        """Returns the specified issue.

        Args:
            repository_slug:
            issue_id:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/issues/{}".format(
                self.workspace, repository_slug, issue_id
            ),
            params=params,
        )

    def get_issues(self, repository_slug, params=None):
        """Returns the issues in the issue tracker.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/issues".format(self.workspace, repository_slug),
            params=params,
        )

    def delete_issue(self, repository_slug, issue_id, params=None):
        """Deletes the specified issue. This requires write access to the repository.

        Args:
            repository_slug:
            issue_id:
            params:

        Returns:

        """
        return self._delete(
            "2.0/repositories/{}/{}/issues/{}".format(
                self.workspace, repository_slug, issue_id
            ),
            params=params,
        )

    def create_webhook(self, repository_slug, data, params=None):
        """Creates a new webhook on the specified repository.

        Example:
            {
              "description": "Webhook Description",
              "url": "https://example.com/",
              "active": true,
              "events": [
                "repo:push",
                "issue:created",
                "issue:updated"
              ]
            }

        Note that this call requires the webhook scope, as well as any scope that applies to the events
        that the webhook subscribes to. In the example above that means: webhook, repository and issue.
        Also note that the url must properly resolve and cannot be an internal, non-routed address.

        Args:
            repository_slug:
            data:
            params:

        Returns:

        """
        return self._post(
            "2.0/repositories/{}/{}/hooks".format(self.workspace, repository_slug),
            data=data,
            params=params,
        )

    def get_webhook(self, repository_slug, webhook_uid, params=None):
        """Returns the webhook with the specified id installed on the specified repository.

        Args:
            repository_slug:
            webhook_uid:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/hooks/{}".format(
                self.workspace, repository_slug, webhook_uid
            ),
            params=params,
        )

    def get_webhooks(self, repository_slug, params=None):
        """Returns a paginated list of webhooks installed on this repository.

        Args:
            repository_slug:
            params:

        Returns:

        """
        return self._get(
            "2.0/repositories/{}/{}/hooks".format(self.workspace, repository_slug),
            params=params,
        )

    def delete_webhook(self, repository_slug, webhook_uid, params=None):
        """Deletes the specified webhook subscription from the given repository.

        Args:
            repository_slug:
            webhook_uid:
            params:

        Returns:

        """
        return self._delete(
            "2.0/repositories/{}/{}/hooks/{}".format(
                self.workspace, repository_slug, webhook_uid
            ),
            params=params,
        )

    def _get(self, endpoint: str, params=None):
        print(f"GET {endpoint}")
        response = requests.get(
            endpoint if endpoint.startswith("http") else self.BASE_URL + endpoint,
            params=params,
            auth=(self.user, self.password),
        )
        return self.parse(response)

    def _post_files(self, endpoint, params=None, data=None, files=None):
        print(f"MY POST {endpoint}")
        response = requests.post(
            self.BASE_URL + endpoint,
            params=params,
            data=data,
            files=files,
            auth=(self.user, self.password),
        )
        return self.parse(response)

    def _post(self, endpoint, params=None, data=None):
        print(f"POST {endpoint}")
        response = requests.post(
            self.BASE_URL + endpoint,
            params=params,
            json=data,
            auth=(self.user, self.password),
        )
        return self.parse(response)

    def _put(self, endpoint, params=None, data=None):
        print(f"PUT {endpoint}")
        response = requests.put(
            self.BASE_URL + endpoint,
            params=params,
            json=data,
            auth=(self.user, self.password),
        )
        return self.parse(response)

    def _delete(self, endpoint, params=None):
        print(f"DELETE {endpoint}")
        response = requests.delete(
            self.BASE_URL + endpoint, params=params, auth=(self.user, self.password)
        )
        return self.parse(response)
