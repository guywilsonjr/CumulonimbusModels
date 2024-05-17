from enum import StrEnum
from typing import ClassVar

from pydantic import BaseModel, Field

from cumulonimbus_models.api import APIRequest
from constants import REGISTER_AGENT_FORMAT, REGISTER_AGENT_PATH, UNREGISTER_AGENT_FORMAT, UNREGISTER_AGENT_PATH


class AgentRegisterRequest(APIRequest):
    path: ClassVar[str] = Field(default=REGISTER_AGENT_PATH, exclude=True)
    format: ClassVar[str] = Field(default=REGISTER_AGENT_FORMAT, exclude=True)
    hostname: str


class AgentRegisterResponse(BaseModel):
    agent_id: str
    agent_key: str
    ip_address: str
    operations_queue_url: str


class UnregisterAgentRequest(APIRequest):
    path: ClassVar[str] = Field(default=UNREGISTER_AGENT_PATH, exclude=True)
    format: ClassVar[str] = Field(default=UNREGISTER_AGENT_FORMAT, exclude=True)
    agent_id: str


class UnregisterAgentStatus(StrEnum):
    NOT_FOUND = 'NOT_FOUND'
    SUCCESS = 'SUCCESS'


class UnregisterAgentResponse(BaseModel):
    status: UnregisterAgentStatus

