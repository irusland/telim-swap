import json
import logging
from pathlib import Path
from typing import List

from aiogram import types, Bot, Dispatcher
from pydantic import BaseSettings

from src.handlers.base import BaseHandler
from src.localisation.language_coordinator import LanguageCoordinator
from src.utils.log import log_request

URL = 'https://docs.aiogram.dev/en/dev-2.x/_static/logo.png'
logger = logging.getLogger(__name__)


class AdminSettings(BaseSettings):
    is_enabled: bool = False
    _admin_usernames_file_path: Path = Path('.admins.json')

    def get_admin_usernames(self) -> List[str]:
        if not self._admin_usernames_file_path.exists():
            self._admin_usernames_file_path.write_text(json.dumps([]))
        raw_admins = self._admin_usernames_file_path.read_text()
        return json.loads(raw_admins)

    def set_admin_usernames(self, admin_usernames: List[str]) -> None:
        raw_admins = json.dumps(admin_usernames)
        self._admin_usernames_file_path.write_text(raw_admins)

    class Config:
        env_prefix: str = 'ADMIN_SETTINGS_'


class AdminHandler(BaseHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, settings: AdminSettings,
                 localizator: LanguageCoordinator):

        @dp.message_handler(commands=['admin'])
        @log_request(type(self))
        async def __call__(message: types.Message) -> None:
            localization = localizator.get_localisation(message.chat.id)
            if not settings.is_enabled:
                await message.reply(localization.NOTHING_HERE)
                return

            admin_usernames = settings.get_admin_usernames()
            if message.from_user.username not in admin_usernames:
                await message.reply(localization.RESTRICTED)
                return

            await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))
            await bot.send_message(message.from_user.id, message.from_user.first_name)
            await bot.send_message(message.from_user.id, message.from_user.id)
            await bot.send_message(message.from_user.id, message.from_user.username)
            await bot.send_message(message.from_user.id, message.from_user.full_name)
