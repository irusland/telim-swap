
from aiogram import Bot, Dispatcher, executor, types

from src.handlers.start import send_welcome


class ImSwapDispatcher(Dispatcher):
    def __init__(self, bot: Bot):
        super().__init__(bot)

        self._register_handlers()

    def _register_handlers(self) -> None:
        self.message_handler(commands=['start', 'help'])(send_welcome)
