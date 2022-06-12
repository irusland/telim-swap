
from aiogram import Bot, Dispatcher, executor, types

from src.handlers.start import StartHandler


class ImSwapDispatcher(Dispatcher):
    def __init__(self, bot: Bot, start_handler: StartHandler):
        super().__init__(bot)

        self._handlers = {
            ('start', 'help'): start_handler,
        }
        self._register_handlers()

    def _register_handlers(self) -> None:
        for commands, handler in self._handlers.items():
            self.message_handler(commands=list(commands))(handler)
