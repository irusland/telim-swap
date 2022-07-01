import logging

from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.base_settings import BaseNetSettings
from src.neural_net_clients.errors import NeuralNetError

logger = logging.getLogger(__name__)


class ResGanSettings(BaseNetSettings):
    model: str = "resgan"


class ResGan(NeuralNet):
    def __init__(self, settings: ResGanSettings):
        super().__init__(settings)
        self._settings = settings

    def enrich(self, image: bytearray):
        files = {'image': image}
        r = self.request(files=files)

        path = 'gen.png'
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)

            with open(path, 'rb') as f:
                return f.read()
        raise NeuralNetError(r.content)
