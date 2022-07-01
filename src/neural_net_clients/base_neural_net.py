import abc
from http.client import HTTPConnection
from typing import Dict

from aiohttp import ClientSession

from src.neural_net_clients.base_settings import BaseNetSettings
from src.neural_net_clients.errors import NeuralNetError


class NeuralNet(abc.ABC):
    def __init__(self, settings: BaseNetSettings):
        self._settings = settings
        self._session = ClientSession()

    async def request(self, files: Dict[str, bytearray]) -> bytearray:
        HTTPConnection.debuglevel = 1
        async with self._session.post(self._settings.model_url, data=files) as response:
            content = await response.read()
            path = 'gen.png'
            if response.status == 200:
                with open(path, 'wb') as f:
                    f.write(content)

                with open(path, 'rb') as f:
                    return f.read()
            raise NeuralNetError(response.reason)

    @abc.abstractmethod
    async def __call__(self, *images: bytearray) -> bytearray:
        pass

    @abc.abstractmethod
    def get_image_number(self) -> int:
        pass
