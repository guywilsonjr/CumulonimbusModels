from typing import Optional

from pydantic import BaseModel

from cumulonimbus_models.network import NetworkInterface


class AgentRegisterRequest(BaseModel):
    hostname: str
    ifcs: list[NetworkInterface]
    agent_id: Optional[str] = None


class AgentRegisterResponse(BaseModel):
    agent_id: str
    agent_key: str
    operations_queue_url: str
    operation_results_queue_url: str

