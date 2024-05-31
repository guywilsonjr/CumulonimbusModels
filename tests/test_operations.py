from datetime import datetime

from cumulonimbus_models import operations, operation_submissions


def test_operations():
    assert operations.Operation(id='test-operation-id', type=operations.OperationType.UPDATE, parameters={})
    assert operations.OperationResultStatus.PENDING == 'PENDING'
    assert operations.OperationType.UPDATE
    assert operations.SubmitOperationRequest(type=operations.OperationType.UPDATE, parameters={})
    assert operations.SubmitOperationResponse(operation_id='test', submitted=datetime.now())
    assert operations.OperationResult(operation_output='test', operation_status=operations.OperationResultStatus.PENDING)
    assert operations.UpdateOperationResultRequest(started=datetime.now(), completed=datetime.now(), operation_result=operations.OperationResult(operation_output='test', operation_status=operations.OperationResultStatus.PENDING))
    assert operations.OperationBase(agent_id='test', operation_id='test')

    assert operation_submissions.SubmitShellCommandOperationRequest(parameters=operation_submissions.ShellCommandOperationParameters(command='test'))
    assert operation_submissions.SubmitUpdateOperationRequest(parameters={})

