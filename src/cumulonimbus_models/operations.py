from enum import StrEnum
from typing import Dict
from pydantic import BaseModel


class OperationType(StrEnum):
    UPDATE = 'UPDATE'


class Operation(BaseModel):
    id: str
    type: OperationType
    parameters: Dict[str, str | int | float | bool | None]


class UpdateOperation(Operation):
    type: OperationType = OperationType.UPDATE
    parameters: Dict[str, str | int | float | bool | None] = {}

