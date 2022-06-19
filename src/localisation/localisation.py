import enum

from pydantic import BaseModel


class Localisation(BaseModel):
    _NAME: str

    NOTHING_HERE: str
    RESTRICTED: str


class LocalisationName(str, enum.Enum):
    ENGLISH = 'English 🇺🇸'
    RUSSIAN = 'Русский 🇷🇺'


class LocalisationEN(Localisation):
    _NAME: LocalisationName = LocalisationName.ENGLISH

    NOTHING_HERE: str = 'Nothing here'
    RESTRICTED: str = 'Restricted'


class LocalisationRU(LocalisationEN):
    _NAME: LocalisationName = LocalisationName.RUSSIAN

    NOTHING_HERE: str = 'Здесь ничего нет'
    RESTRICTED: str = 'Доступ запрещен'
