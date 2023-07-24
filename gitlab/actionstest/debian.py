from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.debian import *
@action_store.kubiya_action()
def upload_a_package_file(input: ProjectsIdPackagesDebianFilename):
    return put_wrapper(endpoint=f'projects/{input.id}/packages/debian/{input.file_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_package(input: ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename):
    return get_wrapper(endpoint=f'projects/{input.id}/packages/debian/pool/{input.distribution}/{input.letter}/{input.package_name}/{input.package_version}/{input.file_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_distribution_release_file(input: DownloadADistributionReleaseFile):
    return get_wrapper(endpoint=f'projects/dists/*distribution/Release', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_distribution_release_file(input: DownloadADistributionReleaseFile):
    return get_wrapper(endpoint=f'groups/dists/*distribution/Release', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_signed_distribution_release_file(DownloadASignedDistributionReleaseFile):
    return get_wrapper(endpoint=f'projects/dists/*distribution/InRelease', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_signed_distribution_release_file(DownloadASignedDistributionReleaseFile):
    return get_wrapper(endpoint=f'groups/dists/*distribution/InRelease', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_release_file_signature(input: DownloadAReleaseFileSignature):
    return get_wrapper(endpoint=f'projects/dists/*distribution/Release.gpg', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_release_file_signature(input: DownloadAReleaseFileSignature):
    return get_wrapper(endpoint=f'groups/dists/*distribution/Release.gpg', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_packages_index(input: DownloadAPackagesIndex):
    return get_wrapper(endpoint=f'projects/dists/*distribution/{input.component}/binary-:architecture/Packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_packages_index(input: DownloadAPackagesIndex):
    return get_wrapper(endpoint=f'groups/dists/*distribution/{input.component}/binary-:architecture/Packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_package_index_by_hash(input: DownloadAPackagesIndexByHash):
    return get_wrapper(endpoint=f'projects/dists/*distribution/{input.component}/binary-:architecture/by-hash/SHA256/{input.file_sha256}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_index_by_hash(input: DownloadAPackagesIndexByHash):
    return get_wrapper(endpoint=f'groups/dists/*distribution/{input.component}/binary-:architecture/by-hash/SHA256/{input.file_sha256}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_debian_installer_packages_index(input: DownloadADebianInstallerPackagesIndex):
    return get_wrapper(endpoint=f'projects/dists/*distribution/{input.component}/debian-installer/binary-:architecture/Packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_debian_installer_packages_index(input: DownloadADebianInstallerPackagesIndex):
    return get_wrapper(endpoint=f'groups/dists/*distribution/{input.component}/debian-installer/binary-:architecture/Packages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_debian_installer_packages_index_by_hash(input: DowloadADebianInstallerPackagesIndexByHash):
    return get_wrapper(endpoint=f'projects/dists/*distribution/{input.component}/debian-installer/binary-:architecture/by-hash/SHA256/{input.file_sha256}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_debian_installer_packages_index_by_hash(input: DowloadADebianInstallerPackagesIndexByHash):
    return get_wrapper(endpoint=f'groups/dists/*distribution/{input.component}/debian-installer/binary-:architecture/by-hash/SHA256/{input.file_sha256}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_source_packages_index(input: DownloadASourcePackagesIndex):
    return get_wrapper(endpoint=f'projects/dists/*distribution/{input.component}/source/Sources', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_source_packages_index(input: DownloadASourcePackagesIndex):
    return get_wrapper(endpoint=f'groups/dists/*distribution/{input.component}/source/Sources', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_project_source_packages_index_by_hash(input: DownloadASourcePackagesIndexByHash):
    return get_wrapper(endpoint=f'projects/dists/*distribution/{input.component}/source/by-hash/SHA256/{input.file_sha256}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_a_group_source_packages_index_by_hash(input: DownloadASourcePackagesIndexByHash):
    return get_wrapper(endpoint=f'groups/dists/*distribution/{input.component}/source/by-hash/SHA256/{input.file_sha256}', args=input.dict(exclude_none=True))