# from typing import List, Any, Optional, Union
# from pydantic import BaseModel, Field
# from . import action_store as action_store
# from .http_wrapper import *
# from datetime import datetime
#
#
# class Users(BaseModel):
#
#     order_by: Optional[str] = None # Return users ordered by id, name, username, created_at, or updated_at fields. Default is id
#
#     sort: Optional[str] = None # Return users sorted in asc or desc order. Default is desc
#
#     two_factor: Optional[str] = None # Filter users by Two-factor authentication. Filter values are enabled or disabled. By default it returns all users
#
#     without_projects: Optional[bool] = None # Filter users without projects. Default is false, which means that all users are returned, with and without projects.
#
#     admins: Optional[bool] = None # Return only administrators. Default is false
#
#     saml_provider_id: Optional[int] = None # Return only users created by the specified SAML provider ID. If not included, it returns all users.
#
#     skip_ldap: Optional[bool] = None # Skip LDAP users.
#
#
# @action_store.kubiya_action()
# def list_users(input: Users):
#     return get_wrapper(endpoint=f"/users", args=input.dict(exclude_none=True))
#
# # TODO
# # class Users?externuid=externuid&provider=provider(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def list_users(input: Users?externuid=externuid&provider=provider):
# # return get_wrapper(endpoint=f"/users?extern_uid=:extern_uid&provider=:provider", args=input.dict(exclude_none=True))
# #
# #
# # class Users?externuid=1234567&provider=github(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def list_users(input: Users?externuid=1234567&provider=github):
# # return get_wrapper(endpoint=f"/users?extern_uid=1234567&provider=github", args=input.dict(exclude_none=True))
# #
# #
# # class Users?createdbefore=20010102t000000.060z&createdafter=19990102t000000.060(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def list_users(input: Users?createdbefore=20010102t000000.060z&createdafter=19990102t000000.060):
# # return get_wrapper(endpoint=f"/users?created_before=2001-01-02T00:00:00.060Z&created_after=1999-01-02T00:00:00.060", args=input.dict(exclude_none=True))
# #
# #
# # class Users?customattributes[key]=value&customattributes[otherkey]=othervalue(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def list_users(input: Users?customattributes[key]=value&customattributes[otherkey]=othervalue):
# # return get_wrapper(endpoint=f"/users?custom_attributes[key]=value&custom_attributes[other_key]=other_value", args=input.dict(exclude_none=True))
# #
# #
# # class Users?withcustomattributes=true(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def list_users(input: Users?withcustomattributes=true):
# # return get_wrapper(endpoint=f"/users?with_custom_attributes=true", args=input.dict(exclude_none=True))
#
#
# class UsersId(BaseModel):
#     id: str # ID of a user
#
# @action_store.kubiya_action()
# def single_user(input: UsersId):
#     return get_wrapper(endpoint=f"/users/{input.id}", args=input.dict(exclude_none=True))
#
#
# #TODO
# #
# # class UsersId?withcustomattributes=true(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def single_user(input: UsersId?withcustomattributes=true):
# # return get_wrapper(endpoint=f"/users/{input.id?with_custom_attributes=true}", args=input.dict(exclude_none=True))
#
# #TODO - params type not mentioned https://docs.gitlab.com/ee/api/users.html#user-creation
# #class UsersCreation(BaseModel):
# #
# # @action_store.kubiya_action()
# # def user_creation(input: UsersCreation):
# #     return post_wrapper(endpoint=f"/users", args=input.dict(exclude_none=True))
#
# #TODO params type not mentioned https://docs.gitlab.com/ee/api/users.html#user-modification
# #
# # class UsersId(BaseModel):
# #
# #
# # @action_store.kubiya_action()
# # def user_modification(input: UsersId):
# #     return put_wrapper(endpoint=f"/users/{input.id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdIdentitiesProvider(BaseModel):
#     id: int # The ID of the user
#     provider: str # External provider name
#
# @action_store.kubiya_action()
# def delete_authentication_identity_from_user(input: UsersIdIdentitiesProvider):
#     return delete_wrapper(endpoint=f"/users/{input.id}/identities/{input.provider}", args=input.dict(exclude_none=True))
#
#
# class UsersId(BaseModel):
#     id: int # The ID of the user
#     hard_delete: Optional[bool] = None # If true, contributions that would usually be moved to Ghost User are deleted instead, as well as groups owned solely by this user.
#
# @action_store.kubiya_action()
# def user_deletion(input: UsersId):
#     return delete_wrapper(endpoint=f"/users/{input.id}", args=input.dict(exclude_none=True))
#
#
#
# @action_store.kubiya_action()
# def list_current_user_non_admins(input=None):
#     return get_wrapper(endpoint=f"/user", args=input)
#
#
# class User(BaseModel):
#     sudo: Optional[int] = None # ID of a user to make the call in their place
#
# @action_store.kubiya_action()
# def list_current_user(input: User):
#     return get_wrapper(endpoint=f"/user", args=input.dict(exclude_none=True))
#
# @action_store.kubiya_action()
# def user_status(input=None):
#     return get_wrapper(endpoint=f"/user/status", args=input)
#
#
# class UsersIdorusernameStatus(BaseModel):
#
#     id_or_username: str # ID or username of the user to get a status of
#
# @action_store.kubiya_action()
# def get_the_status_of_a_user(input: UsersIdorusernameStatus):
#     return get_wrapper(endpoint=f"/users/{input.id_or_username}/status", args=input.dict(exclude_none=True))
#
#
# class UserStatusSet(BaseModel):
#
#     emoji: Optional[str] = None # Name of the emoji to use as status. If omitted speech_balloon is used. Emoji name can be one of the specified names in the Gemojione index.
#
#     message: Optional[str] = None # Message to set as a status. It can also contain emoji codes. Cannot exceed 100 characters.
#
#     clear_status_after: Optional[str] = None # Automatically clean up the status after a given time interval, allowed values: 30_minutes, 3_hours, 8_hours, 1_day, 3_days, 7_days, 30_days
#
#
# @action_store.kubiya_action()
# def set_user_status(input: UserStatusSet):
#     return put_wrapper(endpoint=f"/user/status", args=input.dict(exclude_none=True))
#
#
# @action_store.kubiya_action()
# def get_user_preferences(input=None):
#     return get_wrapper(endpoint=f"/user/preferences", args=input)
#
#
# class UserPreferences(BaseModel):
#     view_diffs_file_by_file: bool  # Flag indicating the user sees only one file diff per page.
#     show_whitespace_in_diffs: bool  # Flag indicating the user sees whitespace changes in diffs.
#     pass_user_identities_to_ci_jwt: bool # Pass user identities to CI job token
# @action_store.kubiya_action()
# def user_preference_modification(input: UserPreferences):
#     return put_wrapper(endpoint=f"/user/preferences", args=input.dict(exclude_none=True))
#
#
# class UsersIdFollow(BaseModel):
#     id: int # ID of the user to follow
#
# @action_store.kubiya_action()
# def user_follow(input: UsersIdFollow):
#     return post_wrapper(endpoint=f"/users/{input.id}/follow", args=input.dict(exclude_none=True))
#
# class UsersIdUnfollow(BaseModel):
#
#     id: int # ID of the user to follow
#
# @action_store.kubiya_action()
# def user_unfollow(input: UsersIdUnfollow):
#     return post_wrapper(endpoint=f"/users/{input.id}/unfollow", args=input.dict(exclude_none=True))
#
#
# class UsersIdFollowers(BaseModel):
#     id: int # ID of the user to follow
#
# @action_store.kubiya_action()
# def user_follow(input: UsersIdFollowers):
#     return get_wrapper(endpoint=f"/users/{input.id}/followers", args=input.dict(exclude_none=True))
#
# class UsersIdFollowing(BaseModel):
#
#     id: int # ID of the user to follow
#
# @action_store.kubiya_action()
# def user_follow(input: UsersIdFollowing):
#     return get_wrapper(endpoint=f"/users/{input.id}/following", args=input.dict(exclude_none=True))
#
#
# class Usercounts(BaseModel):
#
#
# @action_store.kubiya_action()
# def user_counts(input: Usercounts):
#     return get_wrapper(endpoint=f"/user_counts", args=input.dict(exclude_none=True))
#
#
# class UsersIdAssociationscount(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_associations_count_for_user(input: UsersIdAssociationscount):
#     return get_wrapper(endpoint=f"/users/{input.id}/associations_count", args=input.dict(exclude_none=True))
#
#
# class UserKeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_ssh_keys(input: UserKeys):
#     return get_wrapper(endpoint=f"/user/keys", args=input.dict(exclude_none=True))
#
#
# class UsersIdorusernameKeys(BaseModel):
#
#     id_or_username: str # ID or username of the user to get the SSH keys for.
#
#
# @action_store.kubiya_action()
# def list_ssh_keys_for_user(input: UsersIdorusernameKeys):
#     return get_wrapper(endpoint=f"/users/{input.id_or_username}/keys", args=input.dict(exclude_none=True))
#
#
# class UserKeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def single_ssh_key(input: UserKeysKeyid):
#     return get_wrapper(endpoint=f"/user/keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdKeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def single_ssh_key_for_given_user(input: UsersIdKeysKeyid):
#     return get_wrapper(endpoint=f"/users/{input.id}/keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UserKeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def add_ssh_key(input: UserKeys):
#     return post_wrapper(endpoint=f"/user/keys", args=input.dict(exclude_none=True))
#
#
# class UsersIdKeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def add_ssh_key_for_user(input: UsersIdKeys):
#     return post_wrapper(endpoint=f"/users/{input.id}/keys", args=input.dict(exclude_none=True))
#
#
# class UserKeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def delete_ssh_key_for_current_user(input: UserKeysKeyid):
#     return delete_wrapper(endpoint=f"/user/keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdKeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def delete_ssh_key_for_given_user(input: UsersIdKeysKeyid):
#     return delete_wrapper(endpoint=f"/users/{input.id}/keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UserGpgkeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_all_gpg_keys(input: UserGpgkeys):
#     return get_wrapper(endpoint=f"/user/gpg_keys", args=input.dict(exclude_none=True))
#
#
# class UserGpgkeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def get_a_specific_gpg_key(input: UserGpgkeysKeyid):
#     return get_wrapper(endpoint=f"/user/gpg_keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UserGpgkeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def add_a_gpg_key(input: UserGpgkeys):
#     return post_wrapper(endpoint=f"/user/gpg_keys", args=input.dict(exclude_none=True))
#
#
# class UserGpgkeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def delete_a_gpg_key(input: UserGpgkeysKeyid):
#     return delete_wrapper(endpoint=f"/user/gpg_keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdGpgkeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_all_gpg_keys_for_given_user(input: UsersIdGpgkeys):
#     return get_wrapper(endpoint=f"/users/{input.id}/gpg_keys", args=input.dict(exclude_none=True))
#
#
# class UsersIdGpgkeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def get_a_specific_gpg_key_for_a_given_user(input: UsersIdGpgkeysKeyid):
#     return get_wrapper(endpoint=f"/users/{input.id}/gpg_keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdGpgkeys(BaseModel):
#
#
# @action_store.kubiya_action()
# def add_a_gpg_key_for_a_given_userinput: UsersIdGpgkeys):
#     return post_wrapper(endpoint=f"/users/{input.id}/gpg_keys", args=input.dict(exclude_none=True))
#
#
# class UsersIdGpgkeysKeyid(BaseModel):
#
#
# @action_store.kubiya_action()
# def delete_a_gpg_key_for_a_given_user(input: UsersIdGpgkeysKeyid):
#     return delete_wrapper(endpoint=f"/users/{input.id}/gpg_keys/{input.key_id}", args=input.dict(exclude_none=True))
#
#
# class UserEmails(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_emails(input: UserEmails):
#     return get_wrapper(endpoint=f"/user/emails", args=input.dict(exclude_none=True))
#
#
# class UsersIdEmails(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_emails_for_user(input: UsersIdEmails):
#     return get_wrapper(endpoint=f"/users/{input.id}/emails", args=input.dict(exclude_none=True))
#
#
# class UserEmailsEmailid(BaseModel):
#
#
# @action_store.kubiya_action()
# def single_email(input: UserEmailsEmailid):
#     return get_wrapper(endpoint=f"/user/emails/{input.email_id}", args=input.dict(exclude_none=True))
#
#
# class UserEmails(BaseModel):
#
#
# @action_store.kubiya_action()
# def add_email(input: UserEmails):
#     return post_wrapper(endpoint=f"/user/emails", args=input.dict(exclude_none=True))
#
#
# class UsersIdEmails(BaseModel):
#
#
# @action_store.kubiya_action()
# def add_email_for_user(input: UsersIdEmails):
#     return post_wrapper(endpoint=f"/users/{input.id}/emails", args=input.dict(exclude_none=True))
#
#
# class UserEmailsEmailid(BaseModel):
#
#
# @action_store.kubiya_action()
# def delete_email_for_current_user(input: UserEmailsEmailid):
#     return delete_wrapper(endpoint=f"/user/emails/{input.email_id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdEmailsEmailid(BaseModel):
#
#
# @action_store.kubiya_action()
# def delete_email_for_given_user(input: UsersIdEmailsEmailid):
#     return delete_wrapper(endpoint=f"/users/{input.id}/emails/{input.email_id}", args=input.dict(exclude_none=True))
#
#
# class UsersIdBlock(BaseModel):
#
#
# @action_store.kubiya_action()
# def block_user(input: UsersIdBlock):
#     return post_wrapper(endpoint=f"/users/{input.id}/block", args=input.dict(exclude_none=True))
#
#
# class UsersIdUnblock(BaseModel):
#
#
# @action_store.kubiya_action()
# def unblock_user(input: UsersIdUnblock):
#     return post_wrapper(endpoint=f"/users/{input.id}/unblock", args=input.dict(exclude_none=True))
#
#
# class UsersIdDeactivate(BaseModel):
#
#
# @action_store.kubiya_action()
# def deactivate_user(input: UsersIdDeactivate):
#     return post_wrapper(endpoint=f"/users/{input.id}/deactivate", args=input.dict(exclude_none=True))
#
#
# class UsersIdActivate(BaseModel):
#
#
# @action_store.kubiya_action()
# def activate_user(input: UsersIdActivate):
#     return post_wrapper(endpoint=f"/users/{input.id}/activate", args=input.dict(exclude_none=True))
#
#
# class UsersIdBan(BaseModel):
#
#
# @action_store.kubiya_action()
# def ban_user(input: UsersIdBan):
#     return post_wrapper(endpoint=f"/users/{input.id}/ban", args=input.dict(exclude_none=True))
#
#
# class UsersIdUnban(BaseModel):
#
#
# @action_store.kubiya_action()
# def unban_user(input: UsersIdUnban):
#     return post_wrapper(endpoint=f"/users/{input.id}/unban", args=input.dict(exclude_none=True))
#
#
# class UsersUseridImpersonationtokens(BaseModel):
#
#
# @action_store.kubiya_action()
# def get_all_impersonation_tokens_of_a_user(input: UsersUseridImpersonationtokens):
#     return get_wrapper(endpoint=f"/users/{input.user_id}/impersonation_tokens", args=input.dict(exclude_none=True))
#
#
# class UsersIdApprove(BaseModel):
#
#
# @action_store.kubiya_action()
# def approve_user(input: UsersIdApprove):
#     return post_wrapper(endpoint=f"/users/{input.id}/approve", args=input.dict(exclude_none=True))
#
#
# class UsersIdReject(BaseModel):
#
#
# @action_store.kubiya_action()
# def reject_user(input: UsersIdReject):
#     return post_wrapper(endpoint=f"/users/{input.id}/reject", args=input.dict(exclude_none=True))
#
#
# class UsersUseridImpersonationtokensImpersonationtokenid(BaseModel):
#
#
# @action_store.kubiya_action()
# def get_an_impersonation_token_of_a_user(input: UsersUseridImpersonationtokensImpersonationtokenid):
#     return get_wrapper(endpoint=f"/users/{input.user_id}/impersonation_tokens/{input.impersonation_token_id}", args=input.dict(exclude_none=True))
#
#
# class UsersUseridImpersonationtokens(BaseModel):
#
#     user_id: int # ID of the user
#
#     name: str # Name of the impersonation token
#
#     expires_at: Optional[date] = None # Expiration date of the impersonation token in ISO format (YYYY-MM-DD)
#
#     scopes: array # Array of scopes of the impersonation token (api, read_user)
#
#
# @action_store.kubiya_action()
# def create_an_impersonation_token(input: UsersUseridImpersonationtokens):
#     return post_wrapper(endpoint=f"/users/{input.user_id}/impersonation_tokens", args=input.dict(exclude_none=True))
#
#
# class UsersUseridImpersonationtokensImpersonationtokenid(BaseModel):
#
#
# @action_store.kubiya_action()
# def revoke_an_impersonation_token(input: UsersUseridImpersonationtokensImpersonationtokenid):
#     return delete_wrapper(endpoint=f"/users/{input.user_id}/impersonation_tokens/{input.impersonation_token_id}", args=input.dict(exclude_none=True))
#
#
# class UsersUseridPersonalaccesstokens(BaseModel):
#
#     user_id: int # ID of the user
#
#     name: str # Name of the personal access token
#
#     expires_at: Optional[date] = None # Expiration date of the personal access token in ISO format (YYYY-MM-DD)
#
#     scopes: array # Array of scopes of the personal access token. See personal access token scopes for possible values.
#
#
# @action_store.kubiya_action()
# def create_a_personal_access_token(input: UsersUseridPersonalaccesstokens):
#     return post_wrapper(endpoint=f"/users/{input.user_id}/personal_access_tokens", args=input.dict(exclude_none=True))
#
#
# class UserActivities(BaseModel):
#
#
# @action_store.kubiya_action()
# def get_user_activities(input: UserActivities):
#     return get_wrapper(endpoint=f"/user/activities", args=input.dict(exclude_none=True))
#
#
# class UsersIdMemberships(BaseModel):
#
#
# @action_store.kubiya_action()
# def user_memberships(input: UsersIdMemberships):
#     return get_wrapper(endpoint=f"/users/{input.id}/memberships", args=input.dict(exclude_none=True))
#
#
# class UserRunners(BaseModel):
#
#     runner_type: str # Specifies the scope of the runner; instance_type, group_type, or project_type.
#
#     group_id: Optional[int] = None # The ID of the group that the runner is created in. Required if runner_type is group_type.
#
#     project_id: Optional[int] = None # The ID of the project that the runner is created in. Required if runner_type is project_type.
#
#     description: Optional[str] = None # Description of the runner.
#
#     paused: Optional[bool] = None # Specifies if the runner should ignore new jobs.
#
#     locked: Optional[bool] = None # Specifies if the runner should be locked for the current project.
#
#     run_untagged: Optional[bool] = None # Specifies if the runner should handle untagged jobs.
#
#     tag_list: Optional[str] = None # A list of runner tags.
#
#     access_level: Optional[str] = None # The access level of the runner; not_protected or ref_protected.
#
#     maximum_timeout: Optional[int] = None # Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.
#
#     maintenance_note: Optional[str] = None # Free-form maintenance notes for the runner (1024 characters).
#
#
# @action_store.kubiya_action()
# def create_a_runner(input: UserRunners):
#     return post_wrapper(endpoint=f"/user/runners", args=input.dict(exclude_none=True))
#
#
