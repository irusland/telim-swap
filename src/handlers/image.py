from aiogram import types, Bot, Dispatcher

from src.handlers.base import BaseHandler
from src.utils.log import log_request

URL = 'https://docs.aiogram.dev/en/dev-2.x/_static/logo.png'


class ImageHandler(BaseHandler):
    def __init__(self, bot: Bot, dp: Dispatcher):
        @dp.message_handler(commands=['image'])
        @log_request("ImageHandler")
        async def __call__(message: types.Message) -> None:
            await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))
