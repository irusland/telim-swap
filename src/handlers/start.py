import logging

from aiogram import Bot, Dispatcher, executor, types


from src.settings import BotApiSettings

logging.basicConfig(level=logging.INFO)


async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
