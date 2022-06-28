from pydantic import BaseSettings
from yarl import URL


class BaseNetSettings(BaseSettings):
    predictions_url: URL
    model: str

    @property
    def model_url(self) -> URL:
        return self.predictions_url / self.model
