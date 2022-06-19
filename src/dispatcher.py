from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class ImSwapDispatcher(Dispatcher):
    def __init__(
            self,
            bot: Bot,
            storage: MemoryStorage,
    ):
        super().__init__(bot, storage=storage)
