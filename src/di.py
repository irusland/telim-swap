from typing import Type

from punq import Container

from src.bot import ImSwapBot
from src.dispatcher import ImSwapDispatcher
from src.handlers.start import StartHandler
from src.handlers.text import TextHandler
from src.settings import BotApiSettings

import logging

from aiogram import Bot, Dispatcher, executor, types
from pydantic import BaseSettings

from src.settings import BotApiSettings


def register_settings(container: Container, settings: Type[BaseSettings]):
    container.register(settings, lambda: settings())


def get_bot_container() -> Container:
    container = Container()

    register_settings(container, BotApiSettings)
    container.register(Bot, ImSwapBot)
    container.register(Dispatcher, ImSwapDispatcher)
    container.register(StartHandler)
    container.register(TextHandler)

    return container
