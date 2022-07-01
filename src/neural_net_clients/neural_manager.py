from typing import List

from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.neural_net import ImSwapNeuralNet
from src.neural_net_clients.res_gan import ResGan


class NeuralManager:
    def __init__(self,
                 im_swap_neural_net: ImSwapNeuralNet,
                 res_gan: ResGan,
                 ):
        self._models = [im_swap_neural_net, res_gan]

    def get_available_models(self) -> List[NeuralNet]:
        return self._models
