from typing import ClassVar

from pydantic import BaseModel, Field

from api import APIRequest
from constants import REGISTER_AGENT_FORMAT, REGISTER_AGENT_PATH


class AgentRegisterRequest(APIRequest):
    path: ClassVar[str] = Field(default=REGISTER_AGENT_PATH, exclude=True, const=True)
    format: ClassVar[str] = Field(default=REGISTER_AGENT_FORMAT, exclude=True, const=True)
    hostname: str


class AgentRegisterResponse(BaseModel):
    agent_id: str
    agent_key: str
    ip_address: str
    operations_queue_url: str

