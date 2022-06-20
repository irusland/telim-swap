from typing import List

from src.neural_net_clients.base_neural_net import NeuralNet
from src.neural_net_clients.neural_net import ImSwapNeuralNet


class NeuralManager:
    def __init__(self):
        self._models = [ImSwapNeuralNet()]

    def get_available_models(self) -> List[NeuralNet]:
        return self._models
