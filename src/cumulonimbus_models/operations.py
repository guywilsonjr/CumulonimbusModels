import uuid
from datetime import datetime
from enum import StrEnum
from typing import ClassVar, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

from cumulonimbus_models.constants import SUBMIT_OPERATION_FORMAT, SUBMIT_OPERATION_PATH, UNREGISTER_AGENT_FORMAT, UNREGISTER_AGENT_PATH, UPDATE_OPERATION_RESULT_FORMAT, UPDATE_OPERATION_RESULT_PATH
from api import APIRequest
from utils import JSON


class OperationBase(BaseModel):
    agent_id: str
    operation_id: str


class OperationResultStatus(StrEnum):
    PENDING = 'PENDING'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'


class OperationType(StrEnum):
    UPDATE = 'UPDATE'


class Operation(BaseModel):
    id: str
    type: OperationType
    parameters: JSON


class SubmitOperationRequest(APIRequest):
    path: ClassVar[str] = Field(default=SUBMIT_OPERATION_PATH, exclude=True, const=True)
    format: ClassVar[str] = Field(default=SUBMIT_OPERATION_FORMAT, exclude=True, const=True)
    type: OperationType
    parameters: JSON


class SubmitOperationResponse(BaseModel):
    operation_id: str
    submitted: datetime


class OperationResult(BaseModel):
    model_config = ConfigDict(extra='allow')
    output: str
    display_output: Optional[str] = None
    status: OperationResultStatus

    @model_validator(mode='after')
    def validate_outputs(self) -> JSON:
        if self.display_output is None:
            self.display_output = self.output
        return self


class UpdateOperationResultRequest(APIRequest):
    path: ClassVar[str] = Field(default=UPDATE_OPERATION_RESULT_PATH, exclude=True, const=True)
    format: ClassVar[str] = Field(default=UPDATE_OPERATION_RESULT_FORMAT, exclude=True, const=True)
    started: datetime
    completed: datetime
    operation_result: OperationResult


class UnregisterAgentRequest(APIRequest):
    path: ClassVar[str] = Field(default=UNREGISTER_AGENT_PATH, exclude=True, const=True)
    format: ClassVar[str] = Field(default=UNREGISTER_AGENT_FORMAT, exclude=True, const=True)
    agent_id: str


class UnregisterAgentStatus(StrEnum):
    NOT_FOUND = 'NOT_FOUND'
    SUCCESS = 'SUCCESS'


class UnregisterAgentResponse(BaseModel):
    status: UnregisterAgentStatus