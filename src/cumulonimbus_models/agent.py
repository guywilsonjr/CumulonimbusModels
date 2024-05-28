from enum import StrEnum

from pydantic import BaseModel, Field

from cumulonimbus_models.api import APIRequest
from cumulonimbus_models.constants import REGISTER_AGENT_FORMAT, REGISTER_AGENT_PATH, UNREGISTER_AGENT_FORMAT, UNREGISTER_AGENT_PATH


class AgentRegisterRequest(APIRequest):
    path: str = Field(default=REGISTER_AGENT_PATH, exclude=True)
    format: str = Field(default=REGISTER_AGENT_FORMAT, exclude=True)
    hostname: str


class AgentRegisterResponse(BaseModel):
    agent_id: str
    agent_key: str
    ip_address: str
    operations_queue_url: str


class UnregisterAgentRequest(APIRequest):
    path: str = Field(default=UNREGISTER_AGENT_PATH, exclude=True)
    format: str = Field(default=UNREGISTER_AGENT_FORMAT, exclude=True)

    def get_url(self, base_url: str, agent_id: str) -> str:
        return f'{base_url}{self.format.format(agent_id=agent_id)}'


class UnregisterAgentStatus(StrEnum):
    NOT_FOUND = 'NOT_FOUND'
    SUCCESS = 'SUCCESS'


class UnregisterAgentResponse(BaseModel):
    status: UnregisterAgentStatus

