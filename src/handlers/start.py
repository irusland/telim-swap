import logging

from aiogram import Bot, Dispatcher, executor, types

from src.handlers.base import BaseHandler
from src.settings import BotApiSettings

logging.basicConfig(level=logging.INFO)


class StartHandler(BaseHandler):
    async def __call__(self, message: types.Message) -> None:
        """
        This handler will be called when user sends `/start` or `/help` command
        """
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
