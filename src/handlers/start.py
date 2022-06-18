import logging

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.handlers.base import BaseHandler
from src.utils.log import log_request

logging.basicConfig(level=logging.INFO)


class StartHandler(BaseHandler):
    def __init__(self):
        inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
        self._inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

    @log_request
    async def __call__(self, message: types.Message) -> None:
        """
        This handler will be called when user sends `/start` or `/help` command
        """
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=self._inline_kb1)
