from typing import Type

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from punq import Container, Scope
from pydantic import BaseSettings, BaseModel

from src.animations import Animation
from src.bot import ImSwapBot
from src.dispatcher import ImSwapDispatcher
from src.handlers.admin import AdminHandler, AdminSettings
from src.handlers.base import BaseHandler
from src.handlers.image import ImageHandler
from src.handlers.preferences import PreferencesHandler
from src.handlers.start import StartHandler
from src.handlers.text import TextHandler
from src.localisation.language_coordinator import LanguageCoordinator
from src.localisation.localisation import Localisation, LocalisationEN, LocalisationRU
from src.neural_net_clients.neural_manager import NeuralManager
from src.neural_net_clients.neural_net import ImSwapNeuralNet, ImSwapNeuralNetSettings
from src.neural_net_clients.res_gan import ResGanSettings, ResGan
from src.settings import BotApiSettings
from src.storage.preferences_storage import PreferencesStorage
from src.utils.reflection import inheritors


def register_settings(container: Container, settings: Type[BaseSettings]):
    container.register(settings, lambda: settings())


def register_model(container: Container, model: Type[BaseModel],
                   factory: Type[BaseModel]):
    container.register(model, lambda: factory())


def get_bot_container() -> Container:
    container = Container()

    register_settings(container, BotApiSettings)

    container.register(MemoryStorage, MemoryStorage, scope=Scope.singleton)
    container.register(Bot, ImSwapBot, scope=Scope.singleton)
    container.register(Dispatcher, ImSwapDispatcher, scope=Scope.singleton)
    container.register(BaseHandler, StartHandler)

    register_settings(container, AdminSettings)
    container.register(LanguageCoordinator)
    register_model(container, Localisation, LocalisationEN)
    register_model(container, Localisation, LocalisationRU)
    container.register(PreferencesStorage)
    container.register(BaseHandler, AdminHandler)

    container.register(BaseHandler, PreferencesHandler)

    container.register(NeuralManager)
    container.register(BaseHandler, ImageHandler)
    register_settings(container, ImSwapNeuralNetSettings)
    container.register(ImSwapNeuralNet)
    register_settings(container, ResGanSettings)
    container.register(ResGan)

    container.register(BaseHandler, TextHandler)

    for animation_class in inheritors(Animation):
        container.register(Animation, animation_class)

    return container
