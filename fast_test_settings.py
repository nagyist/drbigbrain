import logging

from settings import *

# sqlite3 runs in-memory only when running tests.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fast_tests',
        'TEST_CHARSET': 'utf8',
    }
}

root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)

