REGISTER_AGENT_PATH = '/agent/<agent_id>/register'
UNREGISTER_AGENT_PATH = '/agent/<agent_id>'
SUBMIT_OPERATION_PATH = '/agent/<agent_id>/operation/submit'
UPDATE_OPERATION_RESULT_PATH = '/agent/<agent_id>/operation/<operation_id>/result'

REGISTER_AGENT_FORMAT = REGISTER_AGENT_PATH.replace('<agent_id>', '{agent_id}')
UNREGISTER_AGENT_FORMAT = UNREGISTER_AGENT_PATH.replace('<agent_id>', '{agent_id}')
SUBMIT_OPERATION_FORMAT = SUBMIT_OPERATION_PATH.replace('<agent_id>', '{agent_id}')
UPDATE_OPERATION_RESULT_FORMAT = UPDATE_OPERATION_RESULT_PATH.replace('<agent_id>', '{agent_id}').replace('<operation_id>', '{operation_id}')
