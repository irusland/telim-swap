import enum

from pydantic import BaseModel


class LocalisationName(str, enum.Enum):
    ENGLISH = 'English ๐บ๐ธ'
    RUSSIAN = 'ะ ัััะบะธะน ๐ท๐บ'


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

    LANGUAGE: str = '๐'
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
Enjoy using it ๐ฅ
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

    NOTHING_HERE: str = 'ะะดะตัั ะฝะธัะตะณะพ ะฝะตั'
    BUT_IT_WILL_BE_HERE: str = 'ะะพ ะพะฑัะทะฐัะตะปัะฝะพ ะฑัะดะตั'
    NEED_HELP: str = 'ะัะถะฝะฐ ะฟะพะผะพัั'
    RESTRICTED: str = 'ะะพัััะฟ ะทะฐะฟัะตัะตะฝ'

    MENU: str = 'ะะตะฝั'
    CHOOSE_LANGUAGE: str = 'ะัะฑะตัะธัะต ัะทัะบ'
    LANGUAGE_WAS_SET_TO: str = 'ะขะตะบััะธะน ะฒัะฑัะฐะฝะฝัะน ัะทัะบ'

    INCORRECT_INPUT: str = 'ะะตะฟัะฐะฒะธะปัะฝัะน ะฒะฒะพะด โ'

    AVAILABLE_MODELS: str = 'ะะพัััะฟะฝัะต ะผะพะดะตะปะธ'
    SEND_A_STYLE_PICTURE: str = 'ะัะฟัะฐะฒััะต ะบะฐััะธะฝะบั ะฒ ะบะฐัะตััะฒะต ัะฐะฑะปะพะฝะฐ ััะธะปั'
    SEND_A_CONTENT_PICTURE: str = 'ะัะฟัะฐะฒััะต ะบะฐััะธะฝะบั ะดะปั ะฟัะธะผะตะฝะตะฝะธั ััะธะปั'
    ERROR_HAPPENED_TRY_AGAIN: str = 'ะัะพะธะทะพัะปะฐ ะพัะธะฑะบะฐ, ะฟะพะฟัะพะฑัะนัะต ะฟะพะทะถะต'
    IMAGE_SAVED: str = 'ะะทะพะฑัะฐะถะตะฝะธะต ัะพััะฐะฝะตะฝะพ'

    CANCELLED: str = 'ะัะผะตะฝะตะฝะพ'

    STARTER: str = """ะัะธะฒะตั!
ะญัะพ ะฐัะธะฝััะพะฝะฝัะน ะฑะพั ะพะฑัะฐะฑะฐััะฒะฐััะธะน ะบะฐััะธะฝะบะธ ะฝะตะนัะพะฝะฝัะผะธ ัะตััะผะธ, ัะดะตะปะฐะฝัะน @irusland, ัะฟะตัะธะฐะปัะฝะพ ะดะปั https://www.dlschool.org!
ะะพั ัะพััะพะธั ะธะท 2ัั ัะฐััะตะน - ะบะพะฝัะตะนะฝะตัะพะฒ ะทะฐะฟััะตะฝะฝัั ะฒ ะดะพะบะตัะต, ะฝะฐ ะฒะผ 4c4r ะฒ yandex cloud
1ะฐั ัะฐััั - ััะพะฝััะฝะด ะดะปั ะฒะทะฐะธะผะพะดะตะนััะฒะธั ั api telegram
2ะฐั ัะฐััั - ะฑัะบ ะดะปั ะฝะตะนัะพัะตัะตะน ะฝะฐ torchserve
ะะฒะธะดั ัะพะณะพ, ััะพ ะผะฐัะธะฝะบะธ ั vGPU ััะพัั ะฟัะธะปะธัะฝะพ, ะฒ ะพะฑัะฐะทะพะฒัะตะปัะฝัั ัะตะปัั ะฒััะธัะปะตะฝะธั ะฟัะพะธะทะฒะพะดัััั ะฝะฐ cpu ะธ ะบะฐัะตััะฒะพ ะบะฐััะธะฝะพะบ ะปะธะผะธัะธัะพะฒะฐะฝะพ.
ะัะธััะฝะพะณะพ ะธัะฟะพะปัะทะพะฒะฐะฝะธั ๐ฅ  
"""
    CREDITS: str = "ะกะฟะธัะพะบ ะปะธัะตัะฐัััั: \nโ @irusland\nโซธ https://stepik.org/users/45922671\n๐โโฌ https://github.com/irusland/telim-swap"
    HELP: str = """ะกะฟะธัะพะบ ะบะพะผะฐะฝะด:
/start - ะฟะพะบะฐะทะฐัั ััะฐััะพะฒะพะต ัะพะพะฑัะตะฝะธะต
/image - ะดะพัััะฟะฝัะต ะฝะตะนัะพัะตัะธ
/cancel - ะพัะผะตะฝะธัั ะธ ะฒัะนัะธ ะฝะฐ ะณะปะฐะฒะฝัะน ัะบัะฐะฝ
/admin - ะฟะฐะฝะตะปั ะฐะดะผะธะฝะฐ
/settings - ะฟะฐะฝะตะปั ะฝะฐัััะพะตะบ
/help - ะฟะพะบะฐะทะฐัั ััะพ ัะพะพะฑัะตะฝะธะต
"""