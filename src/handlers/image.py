import logging

from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton

from src.handlers.base import BaseHandler
from src.localisation.language_coordinator import LanguageCoordinator
from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.errors import NeuralNetError
from src.neural_net_clients.neural_manager import NeuralManager

logger = logging.getLogger(__name__)


class ModelStates(StatesGroup):
    menu = State()
    model = State()
    photo1 = State()
    photo2 = State()
    eval = State()


MODEL_CHOSEN_KEY = 'MODEL_CHOSEN_KEY'
STYLE_PHOTO_KEY = 'STYLE_PHOTO_KEY'
CONTENT_PHOTO_KEY = 'CONTENT_PHOTO_KEY'
RESULT_PHOTO_KEY = 'RESULT_PHOTO_KEY'


class ImageHandler(BaseHandler):
    def _get_model(self, model_id) -> NeuralNet:
        models = self._neural_manager.get_available_models()
        filtered_models = list(filter(lambda m: str(id(m)) == model_id, models))
        if len(filtered_models) != 1:
            raise NeuralNetError()
        return filtered_models[0]

    def __init__(
            self, bot: Bot, dp: Dispatcher,
            language_coordinator: LanguageCoordinator,
            neural_manager: NeuralManager,
    ):
        self._neural_manager = neural_manager

        @dp.message_handler(commands=['image'])
        async def model_choice(message: types.Message) -> None:
            await ModelStates.menu.set()
            localisation = language_coordinator.get_localisation(
                chat_id=message.chat.id
            )
            models = neural_manager.get_available_models()
            menu_markup = InlineKeyboardMarkup()
            settings_buttons = [
                InlineKeyboardButton(
                    f'{i + 1}) {model.__class__.__name__}',
                    callback_data=str(id(model))
                )
                for i, model in enumerate(models)
            ]
            for settings_button in settings_buttons:
                menu_markup.add(settings_button)

            await message.answer(
                f'{localisation.AVAILABLE_MODELS}:',
                reply_markup=menu_markup
            )

        @dp.callback_query_handler(
            state=ModelStates.menu,
        )
        async def model_chosen(callback_query: types.CallbackQuery, state: FSMContext):
            await bot.answer_callback_query(callback_query.id)
            async with state.proxy() as state_proxy:
                model_id = callback_query.data
                state_proxy[MODEL_CHOSEN_KEY] = model_id

            localisation = language_coordinator.get_localisation(
                chat_id=callback_query.message.chat.id
            )

            model = self._get_model(model_id)
            photos_needed = model.get_image_number()
            if photos_needed == 1:
                await bot.send_message(
                    callback_query.from_user.id,
                    localisation.SEND_A_CONTENT_PICTURE
                )
                await ModelStates.photo2.set()
            elif photos_needed == 2:
                await bot.send_message(
                    callback_query.from_user.id,
                    localisation.SEND_A_STYLE_PICTURE
                )
                await ModelStates.photo1.set()
            else:
                raise NotImplementedError()

        @dp.message_handler(content_types=['photo'], state=ModelStates.photo1)
        async def style_photo(message: types.Message, state: FSMContext) -> None:
            localisation = language_coordinator.get_localisation(
                chat_id=message.chat.id
            )
            file_info = await bot.get_file(message.photo[-1].file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            await message.photo[-1].download(
                destination_file='test.jpg'
            )
            await message.answer(localisation.IMAGE_SAVED)
            await message.answer(localisation.SEND_A_CONTENT_PICTURE)

            async with state.proxy() as state_proxy:
                state_proxy[STYLE_PHOTO_KEY] = downloaded_file

            await ModelStates.photo2.set()

        @dp.message_handler(content_types=['photo'], state=ModelStates.photo2)
        async def content_photo(message: types.Message, state: FSMContext) -> None:
            localisation = language_coordinator.get_localisation(
                chat_id=message.chat.id
            )

            file_info = await bot.get_file(message.photo[-1].file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            await message.photo[-1].download(
                destination_file='test2.jpg'
            )

            await message.answer(localisation.IMAGE_SAVED)

            async with state.proxy() as state_proxy:
                state_proxy[CONTENT_PHOTO_KEY] = downloaded_file

                model = self._get_model(model_id=state_proxy[MODEL_CHOSEN_KEY])

                photos_needed = model.get_image_number()

                photos_keys = [STYLE_PHOTO_KEY, CONTENT_PHOTO_KEY][-photos_needed:]
                photos = [state_proxy[key] for key in photos_keys]

            await state.finish()

            result_image = await model(
                *photos
            )
            async with state.proxy() as state_proxy:
                state_proxy[RESULT_PHOTO_KEY] = result_image

            await bot.send_photo(message.chat.id, result_image)
