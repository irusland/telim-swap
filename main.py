import logging
import sys

from aiogram import Dispatcher, executor

from src.di import get_bot_container
from src.handlers.base import BaseHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s'
                              # ' |\n     File "%(pathname)s", line %(lineno)d, in %(funcName)s'
                              )

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# logger.addHandler(stdout_handler)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('starting')
    container = get_bot_container()
    dp = container.resolve(Dispatcher)
    container.resolve_all(BaseHandler)
    executor.start_polling(dp, skip_updates=True)
