from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, field_validator

from utils import JSON


class OperationType(StrEnum):
    UPDATE = 'UPDATE'


class Operation(BaseModel):
    id: str
    type: OperationType
    parameters: JSON


class SubmitOperationRequest(BaseModel):
    agent_id: str
    type: OperationType
    parameters: JSON


class SubmitUpdateOperationRequest(SubmitOperationRequest):
    type: OperationType = OperationType.UPDATE
    parameters: JSON = {}


class SubmitOperationResponse(BaseModel):
    agent_id: str
    operation_id: str
    submitted: datetime


class OperationResult(BaseModel):
    output: str


class UpdateOperationResultRequest(BaseModel):
    agent_id: str
    operation_id: str
    started: datetime
    completed: datetime
    result: OperationResult

    @field_validator('result')
    @classmethod
    def validate_result(cls, v: JSON) -> JSON:
        if 'result_str' not in v:
            raise ValueError('must contain a result_str key')
        return v
