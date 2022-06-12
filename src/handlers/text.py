from aiogram import types

from src.handlers.base import BaseHandler



class TextHandler(BaseHandler):
    def __init__(self):
        pass

    async def __call__(self, message: types.Message) -> None:
        await message.answer(message.text)
