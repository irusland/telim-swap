import logging

from src.neural_net_clients.res_gan import ResGan, ResGanSettings

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    settings = ResGanSettings()
    net = ResGan(settings)

    with open(
            '/Users/ruslansirazhetdinov/Documents/MIPT/telim-swap/notebooks/datasets/picasso.jpg',
            'rb') as style:
        with open(
                '/Users/ruslansirazhetdinov/Documents/MIPT/telim-swap/notebooks/datasets/lilpic.png',
                'rb') as content:
            print(net.enrich(content.read()))
