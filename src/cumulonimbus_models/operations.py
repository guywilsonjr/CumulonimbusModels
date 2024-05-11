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


class OperationResult(BaseModel):
    output: str


class UpdateOperationResultRequest(BaseModel):
    id: str
    started: datetime
    completed: datetime
    result: OperationResult

    @field_validator('result')
    @classmethod
    def validate_result(cls, v: JSON) -> JSON:
        if 'result_str' not in v:
            raise ValueError('must contain a result_str key')
        return v
