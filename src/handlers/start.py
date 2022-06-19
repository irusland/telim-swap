from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from src.handlers.base import BaseHandler


class StartHandler(BaseHandler):
    def __init__(self, dp: Dispatcher):
        @dp.message_handler(commands=['start'])
        async def __call__(message: types.Message, state: FSMContext):
            async with state.proxy() as proxy:
                if 'counter' not in proxy:
                    proxy.setdefault('counter', 0)
                proxy['counter'] += 1
                return await message.reply(f"Counter: {proxy['counter']}")
