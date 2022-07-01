import io
import logging
from typing import List, Any, Dict

import PIL.Image
import torch
import torchvision.transforms as transforms
from PIL import Image
from ts.torch_handler.base_handler import BaseHandler

from contract import STYLE_IMAGE_KEY, CONTENT_IMAGE_KEY
from neural_style_utils import run_style_transfer

logger = logging.getLogger(__name__)


class NeuralHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.imsize = 512 if torch.cuda.is_available() else 128
        self.loader = transforms.Compose([
            transforms.ToTensor()
        ])
        self.resize = transforms.Resize(self.imsize)
        self.unloader = transforms.ToPILImage()

        self.cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(
            self.device)
        self.cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(self.device)

    def _bytes_to_image(self, raw: bytearray) -> PIL.Image.Image:
        return Image.open(io.BytesIO(raw))

    def _prepare_tensor(self, image: PIL.Image.Image) -> torch.Tensor:
        image = self.loader(image).unsqueeze(0)
        return image.to(self.device, torch.float)

    def _bytes_to_tensor(self, raw: bytearray) -> torch.Tensor:
        return self._prepare_tensor(self._bytes_to_image(raw))

    def preprocess(self, data: List[Any]):
        logger.info('Preprocess %s', data)
        files: Dict[str, bytearray] = data[0]

        style_img, content_img = (
            self._bytes_to_tensor(files[key]).to(self.device, torch.float)
            for key in (STYLE_IMAGE_KEY, CONTENT_IMAGE_KEY)
        )

        return [style_img, content_img]

    def inference(self, data, *args, **kwargs):
        logger.info('Inference %s', data)
        style_img, content_img = data
        style_img_shape, content_img_shape = style_img.shape[-2:], content_img.shape[-2:]
        logger.info('Shapes: %s, %s', style_img_shape, content_img_shape)
        to_content_resize = transforms.Resize(content_img_shape)
        style_img, content_img = self.resize(to_content_resize(style_img)), self.resize(content_img)
        input_img = content_img.clone()

        cnn = self.model.features.to(self.device).eval()
        output = run_style_transfer(
            cnn, self.cnn_normalization_mean, self.cnn_normalization_std,
            content_img, style_img, input_img, device=self.device
        )

        return to_content_resize(output)

    def postprocess(self, data) -> List[bytes]:
        logger.info('Postprocess %s', data)
        tensor: torch.Tensor = data
        tensor = tensor.cpu().clone()
        tensor = tensor.squeeze(0)
        image: PIL.Image.Image = self.unloader(tensor)
        raw = io.BytesIO()
        image.save(raw, format='PNG')
        return [raw.getvalue()]
