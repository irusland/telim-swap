from random import choice

from aiogram import types, Dispatcher

from src.handlers.base import BaseHandler
from src.localisation.language_coordinator import LanguageCoordinator


class TextHandler(BaseHandler):
    def __init__(self, dp: Dispatcher, language_coordinator: LanguageCoordinator):
        emojis = "😏😛🙂😅😂🤣😀😃😄😁😆😊😋"

        @dp.message_handler()
        async def __call__(message: types.Message) -> None:
            localisation = language_coordinator.get_localisation(message.chat.id)
            emoji = choice(emojis)
            msg = (f'{localisation.NOTHING_HERE}, '
                   f'{localisation.BUT_IT_WILL_BE_HERE.lower()}! '
                   f'{emoji}\n{localisation.NEED_HELP}? /help')
            await message.answer(msg)
