import logging

# create logger with 'spam_application'
logger = logging.getLogger('data-structures-and-algorithm')
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()

# create formatter and add it to the handlers
format = '%(levelname)s | %(asctime)s.%(msecs)03d | %(module)s:%(funcName)s > %(message)s'
formatter = logging.Formatter(fmt=format, datefmt='%m-%d %H:%M:%S')
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(ch)