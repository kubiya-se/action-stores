from typing import List, Any, Optional
import json
from pydantic import BaseModel
from . import action_store as action_store
from ..http_wrapper import get_wrapper, post_wrapper, post_wrapper_full_response, get_wrapper_full_response
import time
import logging

logger = logging.getLogger(__name__)

class JenkinsJob(BaseModel):
    name: str
    url: str

class JenkinsBuild(BaseModel):
    id: str
    url: str
    timestamp: int
    result: str
    duration: int

class JenkinsBuildLog(BaseModel):
    log: str

class JobParams(BaseModel):
    job_name: str

class BuildParams(BaseModel):
    job_name: str
    build_number: str

class TextSearchParams(BaseModel):
    job_name: str
    build_number: str
    text: str

class NewJobConfig(BaseModel):
    job_name: str
    config_xml: str

class JenkinsJob(BaseModel):
    name: str
    url: str

class JobDeleteParams(BaseModel):
    job_name: str

class JobParamsRequest(BaseModel):
    job_name: str


class JobParameter(BaseModel):
    name: str
    type: str
    choices: List[str]


class JobParamsResponse(BaseModel):
    parameters: List[JobParameter]

class BuildConsoleLogsRequest(BaseModel):
    job_name: str
    build_number: int


class BuildConsoleLogsResponse(BaseModel):
    console_logs: str

class TriggerJobRequest(BaseModel):
    job_name: str
    parameters: Optional[dict] = None

class TriggerJobResponse(BaseModel):
    success: bool
    message: str
    build_number: Optional[str] = None

class CancelJobRequest(BaseModel):
    job_name: str

class CancelJobResponse(BaseModel):
    success: bool
    message: str

class JobStatusRequest(BaseModel):
    job_name: str

class JobStatusResponse(BaseModel):
    status: str
    message: str
    build_logs: Optional[str] = None

@action_store.kubiya_action()
def get_job_status(request: JobStatusRequest) -> JobStatusResponse:
    logger.info(f"Getting status for job {request.job_name}")
    endpoint = f"/job/{request.job_name}/lastBuild/api/json?tree=result"
    try:
        response = get_wrapper(endpoint)
        status = response["result"]
        message = "Job is in progress."
        if status in ["SUCCESS", "FAILURE"]:
            logger.info(f"Job {request.job_name} completed with status {status}")
            message = f"Job status: {status}"
        return JobStatusResponse(status=status, message=message)
    except Exception as e:
        logger.error(f"Error getting status for job {request.job_name}: {e}")
        return JobStatusResponse(status="", message=str(e))

@action_store.kubiya_action()
def cancel_job(request: CancelJobRequest) -> CancelJobResponse:
    logger.info(f"Canceling job {request.job_name}")
    endpoint = f"/job/{request.job_name}/lastBuild/stop"
    try:
        post_wrapper(endpoint)
        logger.info(f"Job {request.job_name} canceled successfully.")
        return CancelJobResponse(success=True, message="Job canceled successfully.")
    except Exception as e:
        logger.error(f"Error canceling job {request.job_name}: {e}")
        return CancelJobResponse(success=False, message=str(e))
    
# Suggested to run this action asynchronously
@action_store.kubiya_action()
def wait_for_job_completion(params: BuildParams) -> JobStatusResponse:
    logger.info(f"Waiting for job {params.job_name} to complete.")
    max_retries = 10  # Maximum number of retries
    retry_delay = 5  # Delay between retries in seconds
    timeout = 300  # Timeout in seconds (e.g., 5 minutes)

    start_time = time.time()
    retries = 0

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time > timeout:
            logger.error(f"Timeout reached while waiting for job {params.job_name} to complete.")
            return JobStatusResponse(status="", message="Timeout reached while waiting for job completion.")

        if retries >= max_retries:
            logger.error(f"Exceeded maximum number of retries while waiting for job {params.job_name} to complete.")
            return JobStatusResponse(status="", message="Exceeded maximum number of retries while waiting for job completion.")

        job_status = get_job_status(JobStatusRequest(job_name=params.job_name))
        if job_status.status in ["SUCCESS", "FAILURE"]:
            logger.info(f"Job {params.job_name} completed with status {job_status.status}")
            build_logs = get_build_console_logs(BuildConsoleLogsRequest(job_name=params.job_name, build_number=params.build_number))
            return JobStatusResponse(status=job_status.status, message=job_status.message, build_logs=build_logs.console_logs)

        retries += 1
        time.sleep(retry_delay)

def get_build_number_from_queue(queue_location: str, job_name: str) -> Optional[int]:
    for _ in range(10):  # retry for 10 times
        # Query the queue API for the build number
        queue_response = get_wrapper_full_response(queue_location)
        if queue_response.status_code == 200:
            queue_data = queue_response.json()
            if 'executable' in queue_data:
                return queue_data['executable']['number']
        elif queue_response.status_code == 404:
            # Job has left the queue
            break
        time.sleep(2)  # wait for 2 seconds before retrying
    return None


def get_latest_build_number(job_name: str) -> Optional[int]:
    # Job has left the queue, query job's builds API for the latest build number
    job_response = get_wrapper_full_response(f"/job/{job_name}/api/json")
    job_data = job_response.json()
    if 'builds' in job_data and job_data['builds']:
        return job_data['builds'][0]['number']
    return None

@action_store.kubiya_action()
def trigger_job(request: TriggerJobRequest) -> TriggerJobResponse:
    logger.info(f"Triggering job {request.job_name}")
    endpoint = f"/job/{request.job_name}/buildWithParameters" if request.parameters else f"/job/{request.job_name}/build"
    try:
        response = post_wrapper_full_response(endpoint, request.parameters)
        if response.status_code != 201:
            return TriggerJobResponse(success=False, message=f"Unexpected response status code: {response.status_code}", build_number=None)

        # Get the queue location from the response headers
        queue_location = response.headers.get('Location')
        logger.info(f"Job {request.job_name} triggered successfully.")
        if queue_location is None:
            return TriggerJobResponse(success=False, message="Queue location not found in response headers.", build_number=None)
        
        # Try to get build number from the queue
        build_number = get_build_number_from_queue(queue_location, request.job_name)
        if build_number is None:
            build_number = get_latest_build_number(request.job_name)

        if build_number is not None:
            return TriggerJobResponse(success=True, message="Job triggered successfully.", build_number=build_number)

        return TriggerJobResponse(success=False, message="Failed to retrieve build number.", build_number=None)
    except Exception as e:
        logger.error(f"Error triggering job {request.job_name}: {e}")
        return TriggerJobResponse(success=False, message=str(e), build_number=None)

@action_store.kubiya_action()
def get_build_console_logs(request: BuildConsoleLogsRequest) -> BuildConsoleLogsResponse:
    logger.info(f"Getting console logs for job {request.job_name}, build number {request.build_number}")
    job_name = request.job_name
    build_number = request.build_number
    console_logs_endpoint = f"/job/{job_name}/{build_number}/consoleText"
    console_logs = get_wrapper(console_logs_endpoint)

    return BuildConsoleLogsResponse(console_logs=console_logs)

@action_store.kubiya_action()
def get_job_params(request: JobParamsRequest) -> JobParamsResponse:
    logger.info(f"Getting parameters for job {request.job_name}")
    job_name = request.job_name
    params_endpoint = f"/job/{job_name}/api/json?tree=actions[parameterDefinitions[name,type,choices]]"
    response = get_wrapper(params_endpoint)

    parameters = []
    if "actions" in response:
        actions = response["actions"]
        for action in actions:
            if "parameterDefinitions" in action:
                parameter_definitions = action["parameterDefinitions"]
                for parameter_definition in parameter_definitions:
                    name = parameter_definition["name"]
                    param_type = parameter_definition["type"]
                    choices = parameter_definition.get("choices", [])
                    parameter = JobParameter(name=name, type=param_type, choices=choices)
                    parameters.append(parameter)

    return JobParamsResponse(parameters=parameters)

@action_store.kubiya_action()
def delete_job(params: JobDeleteParams):
    logger.info(f"Deleting job {params.job_name}")
    job_name = params.job_name
    delete_endpoint = f"/job/{job_name}/doDelete"
    response = post_wrapper(delete_endpoint)
    logger.info(f"Deleted job: {job_name}")
    resp = {"message": f"Deleted job: {job_name}"} if response else {"message": f"Failed to delete job: {job_name}"}
    return resp

@action_store.kubiya_action()
def get_all_jobs(_: Any = None) -> List[JenkinsJob]:
    logger.info("Retrieving jobs from Jenkins.")
    response = get_wrapper("/api/json?tree=jobs[name,url]")
    if response:
        logger.info("Retrieved jobs from Jenkins.")
        return [JenkinsJob(name=job["name"], url=job["url"]) for job in response["jobs"]]
    else:
        logger.error("Failed to retrieve jobs from Jenkins.")
        return []
    
@action_store.kubiya_action()
def get_all_jobs(_: Any = None) -> List[JenkinsJob]:
    logger.info("Retrieving jobs from Jenkins.")
    return get_wrapper("/api/json?tree=jobs[name,url]")

@action_store.kubiya_action()
def get_job_data(params: JobParams) -> dict:
    logger.info(f"Retrieving job data for job {params.job_name}")
    return get_wrapper(f"/job/{params.job_name}/api/json")

@action_store.kubiya_action()
def get_job_params(params: JobParams) -> dict:
    logger.info(f"Retrieving job params for job {params.job_name}")
    return get_wrapper(f"/job/{params.job_name}/api/json?tree=actions[parameterDefinitions[name,type,choices]]")

@action_store.kubiya_action()
def build_job(params: JobParams) -> str:
    logger.info(f"Building job {params.job_name} with args {params.dict()}")
    if params.dict():
        post_wrapper(f"/job/{params.job_name}/buildWithParameters", params.dict())
    else:
        post_wrapper(f"/job/{params.job_name}/build")
    return f"Building job {params.job_name} with args {params.dict()}"

@action_store.kubiya_action()
def get_builds(params: JobParams) -> List[JenkinsBuild]:
    logger.info(f"Retrieving builds for job {params.job_name}")
    return get_wrapper(f"job/{params.job_name}/api/json?tree=builds[id,url,timestamp,result,duration]")

@action_store.kubiya_action()
def get_build_console(params: BuildParams) -> JenkinsBuildLog:
    logger.info(f"Retrieving console output for job {params.job_name}, build number {params.build_number}")
    log_output = get_wrapper(f"job/{params.job_name}/{params.build_number}/consoleText")
    return JenkinsBuildLog(log=log_output)

@action_store.kubiya_action()
def text_in_build_log(params: TextSearchParams) -> bool:
    log_output = get_wrapper(f"job/{params.job_name}/{params.build_number}/consoleText")
    return params.text in log_output

@action_store.kubiya_action()
def filter_text_in_build_log(params: TextSearchParams) -> List[str]:
    log_output = get_wrapper(f"job/{params.job_name}/{params.build_number}/consoleText")
    return [line for line in log_output.splitlines() if params.text in line]

@action_store.kubiya_action()
def get_build_url(params: BuildParams) -> str:
    return get_wrapper(f"job/{params.job_name}/{params.build_number}/api/json?tree=url")["url"]

@action_store.kubiya_action()
def get_build_data(params: BuildParams) -> dict:
    return get_wrapper(f"job/{params.job_name}/{params.build_number}/api/json")

@action_store.kubiya_action()
def get_last_build(params: JobParams) -> JenkinsBuild:
    return get_wrapper(f"job/{params.job_name}/api/json?tree=lastBuild[id,url,timestamp,result,duration]")

@action_store.kubiya_action()
def get_all_builds(params: JobParams) -> dict:
    return get_wrapper(f"job/{params.job_name}/api/json")

@action_store.kubiya_action()
def list_builds(params: JobParams) -> List[JenkinsBuild]:
    return get_wrapper(f"job/{params.job_name}/api/json?tree=builds[number,timestamp,result,duration]")

@action_store.kubiya_action()
def get_build_status(params: JobParams) -> dict:
    return get_wrapper(f"job/{params.job_name}/lastBuild/api/json?tree=result")

@action_store.kubiya_action()
def stop_job(params: JobParams) -> dict:
    return post_wrapper(f"job/{params.job_name}/lastBuild/stop")

@action_store.kubiya_action()
def get_jenkins_logs(params: BuildParams) -> JenkinsBuildLog:
    log_output = get_wrapper(f"/job/{params.job_name}/{params.build_number}/consoleText")
    return JenkinsBuildLog(log=log_output)