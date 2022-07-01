import logging

from src.neural_net_clients.res_gan import ResGan, ResGanSettings

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    settings = ResGanSettings()
    net = ResGan(settings)

    with open(
            './notebooks/datasets/picasso.jpg',
            'rb') as style:
        with open(
                './notebooks/datasets/road.png',
                'rb') as content:
            print(net.enrich(content.read()))
