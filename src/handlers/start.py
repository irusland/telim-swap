import logging

from aiogram import Bot, Dispatcher, executor, types

from src.handlers.base import BaseHandler
from src.settings import BotApiSettings
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(level=logging.INFO)


class StartHandler(BaseHandler):
    def __init__(self):
        inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
        self._inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


    async def __call__(self, message: types.Message) -> None:
        """
        This handler will be called when user sends `/start` or `/help` command
        """
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=self._inline_kb1)
