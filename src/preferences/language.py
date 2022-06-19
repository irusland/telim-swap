from pydantic import BaseModel

from src.localisation.localisation import LocalisationName


class LanguagePreferences(BaseModel):
    selected_language_name: LocalisationName = LocalisationName.ENGLISH
