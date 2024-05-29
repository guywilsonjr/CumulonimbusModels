from enum import StrEnum
from typing import ClassVar

from pydantic import BaseModel
from cumulonimbus_models.api import APIRequest
from cumulonimbus_models.constants import REGISTER_AGENT_FORMAT, REGISTER_AGENT_PATH, UNREGISTER_AGENT_FORMAT, UNREGISTER_AGENT_PATH


class AgentRegisterRequest(APIRequest):
    path: ClassVar[str] = REGISTER_AGENT_PATH
    format: ClassVar[str] = REGISTER_AGENT_FORMAT
    hostname: str


class AgentRegisterResponse(BaseModel):
    agent_id: str
    agent_key: str
    ip_address: str
    operations_queue_url: str


class UnregisterAgentRequest(APIRequest):
    path: ClassVar[str] = UNREGISTER_AGENT_PATH
    format: ClassVar[str] = UNREGISTER_AGENT_FORMAT

    @classmethod
    def get_url(cls, base_url: str, agent_id: str) -> str:
        return f'{base_url}{cls.format.format(agent_id=agent_id)}'


class UnregisterAgentStatus(StrEnum):
    NOT_FOUND = 'NOT_FOUND'
    SUCCESS = 'SUCCESS'


class UnregisterAgentResponse(BaseModel):
    status: UnregisterAgentStatus

