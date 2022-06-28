from torchvision import models
from torchvision.models import VGG


class NeuralStyleNet(VGG):
    def __init__(self):
        # from torchvision.models.vgg import model_urls
        # model_urls['vgg19'] todo download link readme
        _vgg = models.vgg19()
        super().__init__(features=_vgg.features)
