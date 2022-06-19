import logging
from typing import List

from src.localisation.localisation import Localisation, LocalisationName
from src.storage.preferences_storage import PreferencesStorage

logger = logging.getLogger(__name__)


class NoLocalisationsError(Exception):
    pass


class LanguageCoordinator:
    def __init__(self, localisations: List[Localisation], storage: PreferencesStorage):
        super().__init__()
        if len(localisations) < 1:
            raise NoLocalisationsError()

        self._localisations = localisations
        self._name_to_localisation_mapping = {
            localisation._NAME: localisation for localisation in localisations
        }
        self._storage = storage
        self._default_localisation = self._localisations[0]

    def get_localisation(self, chat_id: str) -> Localisation:
        language_preferences = self._storage.get_preferences(chat_id=chat_id)
        selected_localisation = self._name_to_localisation_mapping.get(
            language_preferences.selected_language_name
        )
        if selected_localisation is None:
            logger.warning(
                "Localisation %s for not found in %s for chat_id=%s setting default",
                language_preferences.selected_language_name,
                self._localisations,
                chat_id
            )
            selected_localisation = self._default_localisation

        return selected_localisation

    def set_localisation(self, chat_id: str,
                         localisation_name: LocalisationName) -> Localisation:
        preferences = self._storage.get_preferences(chat_id=chat_id)
        preferences.selected_language_name = localisation_name
        self._storage.set_preferences(chat_id=chat_id, preferences=preferences)

        selected_localisation = self._name_to_localisation_mapping.get(
            preferences.selected_language_name
        )
        if selected_localisation is None:
            raise RuntimeError()

        return selected_localisation
