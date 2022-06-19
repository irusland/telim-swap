from typing import Optional

from src.preferences.language import LanguagePreferences


class PreferencesStorage:
    def __init__(self):
        self._storage = {}

    def _get_key(self, chat_id: str) -> str:
        return f'{PreferencesStorage.__name__}:{chat_id}'

    def get_preferences(self, chat_id: str) -> Optional[LanguagePreferences]:
        return self._storage.get(self._get_key(chat_id), None)

    def set_preferences(self, chat_id: str, preferences: LanguagePreferences) -> None:
        self._storage[self._get_key(chat_id)] = preferences
