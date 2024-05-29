from datetime import datetime
from enum import StrEnum
from typing import Any, ClassVar, Dict, Optional

from pydantic import BaseModel, model_validator

from cumulonimbus_models.constants import SUBMIT_OPERATION_FORMAT, SUBMIT_OPERATION_PATH, UPDATE_OPERATION_RESULT_FORMAT, UPDATE_OPERATION_RESULT_PATH
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
    path: ClassVar[str] = SUBMIT_OPERATION_PATH
    format: ClassVar[str] = SUBMIT_OPERATION_FORMAT
    type: OperationType
    parameters: JSON

    def get_url(self, base_url: str, agent_id: str) -> str:
        return f'{base_url}{self.format.format(agent_id=agent_id)}'


class SubmitOperationResponse(BaseModel):
    operation_id: str
    submitted: datetime


class OperationResult(BaseModel):
    operation_output: str
    display_output: Optional[str] = None
    operation_status: OperationResultStatus
    result_data: Optional[JSON] = None

    @model_validator(mode='after')
    def validate_outputs(self) -> JSON:
        if self.display_output is None:
            self.display_output = self.operation_output
        return self


class UpdateOperationResultRequest(APIRequest):
    path: ClassVar[str] = UPDATE_OPERATION_RESULT_PATH
    format: ClassVar[str] = UPDATE_OPERATION_RESULT_FORMAT
    started: datetime
    completed: datetime
    operation_result: OperationResult

    def get_url(self, base_url: str, agent_id: str, operation_id: str) -> str:
        return f'{base_url}{self.format.format(agent_id=agent_id, operation_id=operation_id)}'

