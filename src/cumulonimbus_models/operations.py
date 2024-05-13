from datetime import datetime
from enum import StrEnum
from typing import ClassVar, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

from constants import SUBMIT_OPERATION_FORMAT, SUBMIT_OPERATION_PATH, UPDATE_OPERATION_RESULT_FORMAT, UPDATE_OPERATION_RESULT_PATH
from api import APIRequest
from utils import JSON


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


class SubmitUpdateOperationRequest(SubmitOperationRequest):
    type: OperationType = OperationType.UPDATE
    parameters: JSON = {}


class OperationBase(BaseModel):
    agent_id: str
    operation_id: str


class OperationDDBEntry(OperationBase):
    agent_id: str
    operation_id: str
    operation: OperationType


class SubmitOperationResponse(OperationBase):
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


