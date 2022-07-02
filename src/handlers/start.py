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
            locale = language_coordinator.get_localisation(message.chat.id)
            await message.answer(f'{locale.STARTER}\n\n{locale.HELP}\n\n{locale.CREDITS}')

        @dp.errors_handler(exception=Exception)
        async def exception_handler(update: types.Update, error):
            message: types.Message = update.message
            localisation = language_coordinator.get_localisation(message.chat.id)
            await message.answer(localisation.ERROR_HAPPENED_TRY_AGAIN)
            logger.exception(error)
            state: FSMContext = dp.current_state(chat=message.chat.id,
                                                 user=message.from_user.id)
            await state.finish()
            return True

        @dp.message_handler(state='*', commands=['cancel'])
        async def cancel(message: types.Message, state: FSMContext) -> None:
            localisation = language_coordinator.get_localisation(message.chat.id)
            await state.finish()
            await message.answer(localisation.CANCELLED)

        @dp.message_handler(state='*', commands=['help'])
        async def help(message: types.Message, state: FSMContext) -> None:
            localisation = language_coordinator.get_localisation(message.chat.id)
            await message.answer(localisation.HELP)
