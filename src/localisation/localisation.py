import enum

from pydantic import BaseModel


class LocalisationName(str, enum.Enum):
    ENGLISH = 'English 🇺🇸'
    RUSSIAN = 'Русский 🇷🇺'


class Localisation(BaseModel):
    _NAME: str

    NOTHING_HERE: str
    BUT_IT_WILL_BE_HERE: str
    NEED_HELP: str
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

    STARTER: str
    CREDITS: str
    HELP: str


class LocalisationEN(Localisation):
    _NAME: LocalisationName = LocalisationName.ENGLISH

    NOTHING_HERE: str = 'Nothing here'
    BUT_IT_WILL_BE_HERE: str = 'But it will be here'
    NEED_HELP: str = 'Need help'
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

    STARTER: str = """Hello!
This is an asynchronous bot that processes images with neural networks, made by @irusland, especially for https://www.dlschool.org!
The bot consists of 2 parts - containers running in docker, on vm 4c4r at yandex cloud
1st part - frontend for interacting with api telegram
2nd part - backing for neural networks on torchserve
Due to the fact that machines with vGPU cost decently, for educational purposes, calculations are made on cpu and the quality of pictures is limited.
Enjoy using it 🔥
"""
    CREDITS: str = "Credits: \ntg: @irusland\nstepik: https://stepik.org/users/45922671\ngithub: https://github.com/irusland/telim-swap"
    HELP: str = """Available commands:
/start - display start message
/image - see available neural networks
/cancel - cancel operation
/admin - admin panel
/settings - preferences panel
/help - show this message
"""


class LocalisationRU(LocalisationEN):
    _NAME: LocalisationName = LocalisationName.RUSSIAN

    NOTHING_HERE: str = 'Здесь ничего нет'
    BUT_IT_WILL_BE_HERE: str = 'Но обязательно будет'
    NEED_HELP: str = 'Нужна помощь'
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

    STARTER: str = """Привет!
Это асинхронный бот обрабатывающий картинки нейронными сетями, сделаный @irusland, специально для https://www.dlschool.org!
Бот состоит из 2ух частей - контейнеров запущенных в докере, на вм 4c4r в yandex cloud
1ая часть - фронтэнд для взаимодействия с api telegram
2ая часть - бэк для нейросетей на torchserve
Ввиду того, что машинки с vGPU стоят прилично, в образовтельных целях вычисления производятся на cpu и качество картинок лимитировано.
Приятного использования 🔥  
"""
    CREDITS: str = "Список литературы: \n✈ @irusland\n⫸ https://stepik.org/users/45922671\n🐈‍⬛ https://github.com/irusland/telim-swap"
    HELP: str = """Список команд:
/start - показать стартовое сообщение
/image - доступные нейросети
/cancel - отменить и выйти на главный экран
/admin - панель админа
/settings - панель настроек
/help - показать это сообщение
"""