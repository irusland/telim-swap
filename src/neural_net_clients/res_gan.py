import logging

from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.base_settings import BaseNetSettings

logger = logging.getLogger(__name__)


class ResGanSettings(BaseNetSettings):
    model: str = "resgan"


class ResGan(NeuralNet):
    def __init__(self, settings: ResGanSettings):
        super().__init__(settings)
        self._settings = settings

    def get_image_number(self) -> int:
        return 1

    async def __call__(self, image: bytearray) -> bytearray:
        files = {'image': image}
        return await self.request(files=files)
