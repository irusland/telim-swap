import abc
from http.client import HTTPConnection
from typing import Dict

import requests
from requests import Response

from src.neural_net_clients.base_settings import BaseNetSettings


class NeuralNet(abc.ABC):
    def __init__(self, settings: BaseNetSettings):
        self._settings = settings
        self._session = requests.Session()

    def request(self, files: Dict[str, bytearray]) -> Response:
        HTTPConnection.debuglevel = 1
        response = self._session.post(
            self._settings.model_url,
            files=files,
        )
        return response

    @abc.abstractmethod
    def __call__(self, *images: bytearray) -> bytearray:
        pass

    @abc.abstractmethod
    def get_image_number(self) -> int:
        pass
