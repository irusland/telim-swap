import logging

from yarl import URL

from models_backend.neural_style_model.contract import STYLE_IMAGE_KEY, \
    CONTENT_IMAGE_KEY
from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.base_settings import BaseNetSettings
from src.neural_net_clients.errors import NeuralNetError


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

    def swap_style(self, style_image: bytearray, content_image: bytearray) -> Image:
        files = {STYLE_IMAGE_KEY: style_image, CONTENT_IMAGE_KEY: content_image}
        r = self.request(files=files)

        path = 'gen.png'
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)

            with open(path, 'rb') as f:
                return f.read()
        raise NeuralNetError(r.content)
