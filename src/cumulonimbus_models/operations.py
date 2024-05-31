from datetime import datetime
from enum import StrEnum
from typing import Any, ClassVar, Dict, Optional

from pydantic import BaseModel, model_validator

from cumulonimbus_models.api import APIRequest
from cumulonimbus_models.utils import JSON


class OperationBase(BaseModel):
    agent_id: str
    operation_id: str


class OperationResultStatus(StrEnum):
    PENDING = 'PENDING'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'


class OperationType(StrEnum):
    UPDATE = 'UPDATE'
    SHELL_COMMAND = 'SHELL_COMMAND'


class Operation(BaseModel):
    id: str
    type: OperationType
    parameters: Dict[str, Any]


class SubmitOperationRequest(APIRequest):
    route_format: ClassVar[str] = '/agent/{agent_id}/operation/submit'
    type: OperationType
    parameters: JSON


class SubmitOperationResponse(BaseModel):
    operation_id: str
    submitted: datetime


class OperationResult(BaseModel):
    operation_output: str
    display_output: Optional[str] = None
    operation_status: OperationResultStatus
    result_data: Optional[JSON] = None

    @model_validator(mode='after')
    def validate_outputs(self) -> 'OperationResult':
        if self.display_output is None:
            self.display_output = self.operation_output
        return self


class UpdateOperationResultRequest(APIRequest):
    route_format: ClassVar[str] = '/agent/{agent_id}/operation/{operation_id}/result'
    started: datetime
    completed: datetime
    operation_result: OperationResult
