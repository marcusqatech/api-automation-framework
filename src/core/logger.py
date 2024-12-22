"""
Purpose
Sets up logging to record debug information during test execution.

Explanation
Configures logging to output logs both to a file (logs/api_test.log) and the console.
Helps debug issues by tracking what the framework is doing during execution.
"""

import logging

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

api_logger = setup_logger('api_test', 'logs/api_test.log')
