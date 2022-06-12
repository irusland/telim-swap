
from aiogram import Bot, Dispatcher, executor, types

from src.settings import BotApiSettings


class ImSwapBot(Bot):
    def __init__(self, settings: BotApiSettings):
        self._api_token = settings.api_token

        super().__init__(token=self._api_token)
