import logging
import logstash
import sys
import time
from random import randint

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('18.220.206.63', 5959, version=1))

test_logger.error('python-logstash: test logstash error message')
test_logger.info('python-logstash: test logstash info message')
test_logger.warning('python-logstash: test logstash warning message')

errorMessageLog = test_logger.error('python-logstash: This is an error message!')
infoMessageLog = test_logger.info('python-logstash: This is an informational message.')
warningMessageLog = test_logger.warning('python-logstash: This is a warning message')

for i in range(1000):
    n = randint(0,4)
    if n == 1:
        errorMessageLog
    elif n == 2:
        infoMessageLog
    elif n == 3:
        warningMessageLog



