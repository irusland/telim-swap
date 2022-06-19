import enum
import logging
from typing import List

from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from src.handlers.base import BaseHandler
from src.localisation.language_coordinator import LanguageCoordinator
from src.localisation.localisation import Localisation, LocalisationName

logger = logging.getLogger(__name__)


class PreferencesStates(StatesGroup):
    menu = State()
    language = State()


class ButtonData(str, enum.Enum):
    LANGUAGE = 'LANGUAGE'


class PreferencesHandler(BaseHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, localisations: List[Localisation],
                 language_coordinator: LanguageCoordinator):
        @dp.message_handler(commands=['settings'])
        async def settings(message: types.Message) -> None:
            localisation = language_coordinator.get_localisation(
                chat_id=message.chat.id)

            menu_markup = InlineKeyboardMarkup()
            settings_buttons = [
                InlineKeyboardButton(localisation.LANGUAGE,
                                     callback_data=ButtonData.LANGUAGE),
            ]
            for settings_button in settings_buttons:
                menu_markup.add(settings_button)

            await PreferencesStates.menu.set()
            await message.answer(f'{localisation.MENU}:', reply_markup=menu_markup)

        language_buttons = [KeyboardButton(localisation._NAME) for localisation in
                            localisations]
        language_settings_markup = ReplyKeyboardMarkup(
            resize_keyboard=True,
            one_time_keyboard=True
        )
        for language_button in language_buttons:
            language_settings_markup.add(language_button)

        @dp.callback_query_handler(
            lambda c: c.data == ButtonData.LANGUAGE,
            state=PreferencesStates.menu,
        )
        async def process_callback_language(callback_query: types.CallbackQuery,
                                            state: FSMContext):
            localisation = language_coordinator.get_localisation(
                chat_id=callback_query.message.chat.id)
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id,
                                   localisation.CHOOSE_LANGUAGE,
                                   reply_markup=language_settings_markup)
            await PreferencesStates.language.set()

        @dp.message_handler(state=PreferencesStates.language)
        async def settings(message: types.Message, state: FSMContext) -> None:
            localisation = language_coordinator.get_localisation(
                chat_id=message.chat.id)
            selected_localisation_name = message.text
            if selected_localisation_name not in LocalisationName._value2member_map_:
                await message.reply(
                    f'{localisation.INCORRECT_INPUT}: {selected_localisation_name}')
                return

            localisation = language_coordinator.set_localisation(
                chat_id=message.chat.id, localisation_name=selected_localisation_name
            )

            await message.answer(
                f'{localisation.LANGUAGE_WAS_SET_TO}: {localisation._NAME}')
            await state.finish()
