from enum import StrEnum
from typing import Any, ClassVar, Dict, List

from pydantic import BaseModel

from cumulonimbus_models.api import APIRequest


class SoftwareInstallationMethod(StrEnum):
    PIP = 'PIP'
    MANUAL = 'MANUAL'
    APT = 'APT'
    GIT = 'GIT'


class Software(BaseModel):
    name: str
    version: str
    installation_method: SoftwareInstallationMethod
    installation_data: Dict[str, Any]
    config_data: Dict[str, Any]


class SystemInfo(BaseModel):
    os: str
    hostname: str
    software: List[Software]


# noinspection PyMethodOverriding,PyUnusedClass
class SystemUpdateRequest(APIRequest):
    route_format: ClassVar[str] = '/agent/{agent_id}/system_update'
    system_info: SystemInfo

