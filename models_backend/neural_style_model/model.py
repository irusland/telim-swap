from torchvision import models
from torchvision.models import VGG


class NeuralStyleNet(VGG):
    def __init__(self):
        _vgg = models.vgg19()
        super().__init__(features=_vgg.features)
