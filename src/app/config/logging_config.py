import logging
import os
import json

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

# Configure logging
logging.basicConfig(level=LOG_LEVEL, format='%(message)s')
logger = logging.getLogger('api-logger')

def log_request(log_data):
    logger.info(json.dumps(log_data))

