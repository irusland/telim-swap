import functools
import logging

logger = logging.getLogger(__name__)


def log_request(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        logger.info('Got request %s(%s, %s)', f.__name__, args, kwargs)
        return f(*args, **kwargs)

    return wrap
