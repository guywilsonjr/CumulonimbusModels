from enum import StrEnum
from typing import Any, ClassVar, Dict, List

from pydantic import BaseModel

from cumulonimbus_models.api import APIRequest
from cumulonimbus_models.constants import SYSTEM_UPDATE_FORMAT, SYSTEM_UPDATE_PATH


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


class SystemInfo(BaseModel):
    os: str
    hostname: str
    software: List[Software]


class SystemUpdateRequest(APIRequest):
    path: ClassVar[str] = SYSTEM_UPDATE_PATH
    format: ClassVar[str] = SYSTEM_UPDATE_FORMAT
    system_info: SystemInfo

    @classmethod
    def get_url(cls, base_url: str, agent_id: str) -> str:
        return f'{base_url}{cls.format.format(agent_id=agent_id)}'
