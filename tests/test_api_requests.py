import pytest

import cumulonimbus_models.settings

cumulonimbus_models.settings.BASE_URL = 'https://api.local.guywilsonjr.com'
from cumulonimbus_models.agent import AgentRegisterRequest,  UnregisterAgentRequest
from cumulonimbus_models.operations import SubmitOperationRequest, UpdateOperationResultRequest
from cumulonimbus_models.system import SystemUpdateRequest
from cumulonimbus_models.api import APIRequest


@pytest.mark.parametrize('req_type', [AgentRegisterRequest,  UnregisterAgentRequest, SubmitOperationRequest, UpdateOperationResultRequest, SystemUpdateRequest, APIRequest])
def test_api_requests(req_type: type):
    req_type.route()
    req_type.get_url(**{k: 'test' for k in req_type.format_args()})


