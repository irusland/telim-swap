from src.neural_net_clients.base_neural_net import NeuralNet


class Image:
    pass


class ImSwapNeuralNet(NeuralNet):
    def __init__(self):
        pass

    def swap_style(self, style_image: Image, content_image: Image) -> Image:
        return content_image
