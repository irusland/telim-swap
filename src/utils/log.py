import functools
import logging

logger = logging.getLogger(__name__)


def log_request(name=''):
    def wrapper(f):
        @functools.wraps(f)
        async def wrap(*args):
            logger.info('Got request %s.%s(%s)', name, f.__name__, args)
            return await f(*args)

        return wrap

    return wrapper
