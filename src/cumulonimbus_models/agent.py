from pydantic import BaseModel


class AgentRegisterRequest(BaseModel):
    hostname: str


class AgentRegisterResponse(BaseModel):
    agent_id: str
    agent_key: str
    ip_address: str
    operations_queue_url: str
    operation_results_queue_url: str

