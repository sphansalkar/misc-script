import glob
import logging
import logging.handlers
import sys
import time

LOG_FILENAME = 'logging_rotatingfile_example.out'

print __name__

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="M", interval=1, backupCount=5)

my_logger.addHandler(handler)

# Log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)
    time.sleep(10)

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print filename
