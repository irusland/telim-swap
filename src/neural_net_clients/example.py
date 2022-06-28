import logging

from src.neural_net_clients.neural_net import ImSwapNeuralNetSettings, ImSwapNeuralNet

logger = logging.getLogger(__name__)

settings = ImSwapNeuralNetSettings()
net = ImSwapNeuralNet(settings)

with open(
        '/Users/ruslansirazhetdinov/Documents/MIPT/telim-swap/notebooks/datasets/picasso.jpg',
        'rb') as style:
    with open(
            '/Users/ruslansirazhetdinov/Documents/MIPT/telim-swap/notebooks/datasets/dancing.jpg',
            'rb') as content:
        print(net.swap_style(style.read(), content.read()))
