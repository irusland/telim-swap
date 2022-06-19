import enum

from pydantic import BaseModel


class LocalisationName(str, enum.Enum):
    ENGLISH = 'English 🇺🇸'
    RUSSIAN = 'Русский 🇷🇺'


class Localisation(BaseModel):
    _NAME: str

    NOTHING_HERE: str
    RESTRICTED: str

    LANGUAGE: str
    MENU: str
    CHOOSE_LANGUAGE: str
    LANGUAGE_WAS_SET_TO: str

    INCORRECT_INPUT: str


class LocalisationEN(Localisation):
    _NAME: LocalisationName = LocalisationName.ENGLISH

    NOTHING_HERE: str = 'Nothing here'
    RESTRICTED: str = 'Restricted'

    LANGUAGE: str = '🌍'
    MENU: str = 'Menu'
    CHOOSE_LANGUAGE: str = 'Choose language'
    LANGUAGE_WAS_SET_TO: str = 'Language was set to'

    INCORRECT_INPUT: str = 'Incorrect input'


class LocalisationRU(LocalisationEN):
    _NAME: LocalisationName = LocalisationName.RUSSIAN

    NOTHING_HERE: str = 'Здесь ничего нет'
    RESTRICTED: str = 'Доступ запрещен'

    MENU: str = 'Меню'
    CHOOSE_LANGUAGE: str = 'Выберите язык'
    LANGUAGE_WAS_SET_TO: str = 'Текущий выбранный язык'

    INCORRECT_INPUT: str = 'Неправильный ввод ❌'
