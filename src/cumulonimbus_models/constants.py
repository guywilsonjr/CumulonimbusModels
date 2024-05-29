REGISTER_AGENT_PATH = '/agent/register'
UNREGISTER_AGENT_PATH = '/agent/<agent_id>'
SUBMIT_OPERATION_PATH = '/agent/<agent_id>/operation/submit'
UPDATE_OPERATION_RESULT_PATH = '/agent/<agent_id>/operation/<operation_id>/result'
SYSTEM_UPDATE_PATH = '/agent/<agent_id>/system_update'

REGISTER_AGENT_FORMAT = REGISTER_AGENT_PATH
UNREGISTER_AGENT_FORMAT = UNREGISTER_AGENT_PATH.replace('<agent_id>', '{agent_id}')
SUBMIT_OPERATION_FORMAT = SUBMIT_OPERATION_PATH.replace('<agent_id>', '{agent_id}')
UPDATE_OPERATION_RESULT_FORMAT = UPDATE_OPERATION_RESULT_PATH.replace('<agent_id>', '{agent_id}').replace('<operation_id>', '{operation_id}')
SYSTEM_UPDATE_FORMAT = SYSTEM_UPDATE_PATH.replace('<agent_id>', '{agent_id}')
