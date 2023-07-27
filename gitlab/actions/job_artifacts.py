from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.job_artifacts import *
@action_store.kubiya_action()
def get_job_artifacts(input: GetJobArtifacts):
    return get_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/artifacts', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_artifacts(input: DownloadArtifacts):
    return get_wrapper(endpoint=f'/projects/{input.id}/jobs/artifacts/{input.ref_name}/download?job={input.job}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_single_artifact_by_job_id(input: DownloadSingleArtifactByJobID):
    return get_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/artifacts/{input.artifact_path}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_single_artifact_from_specific_tag(input: DownloadSingleArtifactFromSpecificTag):
    return get_wrapper(endpoint=f'/projects/{input.id}/jobs/artifacts/{input.ref_name}/raw/{input.artifact_path}?job={input.job}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def keep_artifacts(input: KeepArtifacts):
    return post_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/artifacts/keep', args=input.dict(exclude_none=True))