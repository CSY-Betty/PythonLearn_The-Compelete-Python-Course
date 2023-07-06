import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('test_loger')

logger.info('This will not show up.')
logger.warning('This will.')

"""
DEBUG  not show up
INFO  not show up
WARNING
ERROR
CRITICAL
"""