from aiogram import types, Dispatcher

from src.handlers.base import BaseHandler


class TextHandler(BaseHandler):
    def __init__(self, dp: Dispatcher):
        @dp.message_handler()
        async def __call__(message: types.Message) -> None:
            await message.answer(message.text)
