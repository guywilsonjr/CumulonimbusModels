from typing import Dict

from operations import Operation, OperationType


class UpdateOperation(Operation):
    type: OperationType = OperationType.UPDATE
    parameters: Dict[str, str] = {}
