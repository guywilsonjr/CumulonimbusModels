from typing import List

from pydantic import BaseModel

from cumulonimbus_models.operations import OperationType, SubmitOperationRequest
from cumulonimbus_models.utils import JSON


class SubmitUpdateOperationRequest(SubmitOperationRequest):
    type: OperationType = OperationType.UPDATE
    parameters: JSON = {}


class ShellCommandOperationParameters(BaseModel):
    command: str
    args: List[str] = []


class SubmitShellCommandOperationRequest(SubmitOperationRequest):
    type: OperationType = OperationType.SHELL_COMMAND
    parameters: ShellCommandOperationParameters

