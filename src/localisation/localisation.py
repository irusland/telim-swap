import enum

from pydantic import BaseModel


class LocalisationName(str, enum.Enum):
    ENGLISH = 'English 🇺🇸'
    RUSSIAN = 'Русский 🇷🇺'


class Localisation(BaseModel):
    _NAME: str

    NOTHING_HERE: str
    BUT_IT_WILL_BE_HERE: str
    RESTRICTED: str

    LANGUAGE: str
    MENU: str
    CHOOSE_LANGUAGE: str
    LANGUAGE_WAS_SET_TO: str

    INCORRECT_INPUT: str

    AVAILABLE_MODELS: str
    SEND_A_STYLE_PICTURE: str
    SEND_A_CONTENT_PICTURE: str
    ERROR_HAPPENED_TRY_AGAIN: str
    IMAGE_SAVED: str

    CANCELLED: str


class LocalisationEN(Localisation):
    _NAME: LocalisationName = LocalisationName.ENGLISH

    NOTHING_HERE: str = 'Nothing here'
    BUT_IT_WILL_BE_HERE: str = 'But it will be here'
    RESTRICTED: str = 'Restricted'

    LANGUAGE: str = '🌍'
    MENU: str = 'Menu'
    CHOOSE_LANGUAGE: str = 'Choose language'
    LANGUAGE_WAS_SET_TO: str = 'Language was set to'

    INCORRECT_INPUT: str = 'Incorrect input'

    AVAILABLE_MODELS: str = 'Available models'
    SEND_A_STYLE_PICTURE: str = 'Please, send a style picture'
    SEND_A_CONTENT_PICTURE: str = 'Please, send a content picture'
    ERROR_HAPPENED_TRY_AGAIN: str = 'Error happened, please try again'
    IMAGE_SAVED: str = 'Image saved'

    CANCELLED: str = 'Cancelled'


class LocalisationRU(LocalisationEN):
    _NAME: LocalisationName = LocalisationName.RUSSIAN

    NOTHING_HERE: str = 'Здесь ничего нет'
    BUT_IT_WILL_BE_HERE: str = 'Но обязательно будет'
    RESTRICTED: str = 'Доступ запрещен'

    MENU: str = 'Меню'
    CHOOSE_LANGUAGE: str = 'Выберите язык'
    LANGUAGE_WAS_SET_TO: str = 'Текущий выбранный язык'

    INCORRECT_INPUT: str = 'Неправильный ввод ❌'

    AVAILABLE_MODELS: str = 'Доступные модели'
    SEND_A_STYLE_PICTURE: str = 'Отправьте картинку в качестве шаблона стиля'
    SEND_A_CONTENT_PICTURE: str = 'Отправьте картинку для применения стиля'
    ERROR_HAPPENED_TRY_AGAIN: str = 'Произошла ошибка, попробуйте позже'
    IMAGE_SAVED: str = 'Изображение сохранено'

    CANCELLED: str = 'Отменено'
