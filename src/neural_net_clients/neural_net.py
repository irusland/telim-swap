import logging

from yarl import URL

from models_backend.neural_style_model.contract import STYLE_IMAGE_KEY, \
    CONTENT_IMAGE_KEY
from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.base_settings import BaseNetSettings


class Image:
    pass


logger = logging.getLogger(__name__)


class ImSwapNeuralNetSettings(BaseNetSettings):
    predictions_url: URL = URL('http://localhost:8080/predictions/')
    model: str = "vgg"


class ImSwapNeuralNet(NeuralNet):
    def __init__(self, settings: ImSwapNeuralNetSettings):
        super().__init__(settings)
        self._settings = settings

    def get_image_number(self) -> int:
        return 2

    async def __call__(self, style_image: bytearray,
                       content_image: bytearray) -> bytearray:
        files = {STYLE_IMAGE_KEY: style_image, CONTENT_IMAGE_KEY: content_image}
        return await self.request(files=files)
