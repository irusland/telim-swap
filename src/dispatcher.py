
from aiogram import Bot, Dispatcher, executor, types

from src.handlers.start import StartHandler
from src.handlers.text import TextHandler


class ImSwapDispatcher(Dispatcher):
    def __init__(
            self,
            bot: Bot,
            start_handler: StartHandler,
            text_handler: TextHandler,
    ):
        super().__init__(bot)

        self._handlers = {
            'start': start_handler,
            None: text_handler,
        }
        self._register_handlers()

    def _register_handlers(self) -> None:
        for command, handler in self._handlers.items():
            if command is None:
                self.message_handler()(handler)
            else:
                self.message_handler(commands=[command])(handler)
