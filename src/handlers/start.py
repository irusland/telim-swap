import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from src.handlers.base import BaseHandler
from src.localisation.language_coordinator import LanguageCoordinator

logger = logging.getLogger(__name__)


class StartHandler(BaseHandler):
    def __init__(self, dp: Dispatcher,
                 language_coordinator: LanguageCoordinator,
                 ):
        @dp.message_handler(commands=['start'])
        async def __call__(message: types.Message, state: FSMContext):
            await message.reply(f'{await state.get_data()}')
            async with state.proxy() as proxy:
                if 'counter' not in proxy:
                    proxy.setdefault('counter', 0)
                proxy['counter'] += 1
                return await message.reply(f"Counter: {proxy['counter']}")

        @dp.errors_handler(exception=Exception)
        async def exception_handler(update: types.Update, error):
            message: types.Message = update.message
            localisation = language_coordinator.get_localisation(message.chat.id)
            await message.answer(localisation.ERROR_HAPPENED_TRY_AGAIN)
            logger.exception(error)
            return True

        @dp.message_handler(state='*', commands=['cancel'])
        async def cancel(message: types.Message, state: FSMContext) -> None:
            localisation = language_coordinator.get_localisation(message.chat.id)
            await state.finish()
            await message.answer(localisation.CANCELLED)
