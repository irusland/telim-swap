import logging

from aiogram import Bot, Dispatcher, executor, types

from src.di import get_bot_container

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    container = get_bot_container()
    dp = container.resolve(Dispatcher)
    executor.start_polling(dp, skip_updates=True)
