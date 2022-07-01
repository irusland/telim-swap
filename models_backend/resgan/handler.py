import io
import logging
import math
from typing import List, Any, Dict

import PIL.Image
import cv2
import numpy
import numpy as np
import torch
from PIL import Image
from torch.nn import functional as F
from ts.torch_handler.base_handler import BaseHandler

logger = logging.getLogger(__name__)


class NeuralHandler(BaseHandler):
    def __init__(self):
        super().__init__()

        self.scale = 4
        self.tile_size = 0
        self.tile_pad = 10
        self.pre_pad = 10
        self.mod_scale = None

        self.limsize = 256

    def _bytes_to_image(self, raw: bytearray) -> PIL.Image.Image:
        return Image.open(io.BytesIO(raw))

    def _bytes_to_numpy(self, raw: bytearray) -> np.array:
        return np.array(self._bytes_to_image(raw))

    def preprocess(self, data: List[Any]):
        logger.info('Preprocess %s', data)
        files: Dict[str, bytearray] = data[0]
        _, raw_image = files.popitem()

        nparr = np.fromstring(bytes(raw_image), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        height, width = img_np.shape[0], img_np.shape[1]
        logger.info('Image shape %s', (width, height))
        max_ = max(height, width)
        if max_ > self.limsize:
            scale_percent = self.limsize / max_
            height = int(height * scale_percent)
            width = int(width * scale_percent)
            dim = (width, height)
            img_np = cv2.resize(img_np, dim, interpolation=cv2.INTER_LINEAR)
            logger.info('Limit reached, downsclaing by %s to %s', scale_percent, dim)
        return img_np

    def inference(self, data, *args, **kwargs):
        logger.info('Inference %s', data)
        content_img = data
        output = self.enhance(img=content_img)

        return output

    def postprocess(self, data) -> List[bytes]:
        logger.info('Postprocess %s', data)
        array: numpy.ndarray = data
        image: PIL.Image.Image = Image.fromarray(array)
        r, g, b = image.split()
        image = Image.merge('RGB', (b, g, r))
        raw = io.BytesIO()
        image.save(raw, format='PNG')
        return [raw.getvalue()]

    def pre_process(self, img):
        """Pre-process, such as pre-pad and mod pad, so that the images can be divisible
        """
        img = torch.from_numpy(np.transpose(img, (2, 0, 1))).float()
        img = img.unsqueeze(0).to(self.device)

        if self.pre_pad != 0:
            img = F.pad(img, (0, self.pre_pad, 0, self.pre_pad), 'reflect')
        if self.scale == 2:
            self.mod_scale = 2
        elif self.scale == 1:
            self.mod_scale = 4
        if self.mod_scale is not None:
            self.mod_pad_h, self.mod_pad_w = 0, 0
            _, _, h, w = img.size()
            if (h % self.mod_scale != 0):
                self.mod_pad_h = (self.mod_scale - h % self.mod_scale)
            if (w % self.mod_scale != 0):
                self.mod_pad_w = (self.mod_scale - w % self.mod_scale)
            img = F.pad(img, (0, self.mod_pad_w, 0, self.mod_pad_h), 'reflect')
        return img

    def process(self, img):
        return self.model(img)

    def tile_process(self, img):
        """It will first crop input images to tiles, and then process each tile.
        Finally, all the processed tiles are merged into one images.

        Modified from: https://github.com/ata4/esrgan-launcher
        """
        batch, channel, height, width = img.shape
        output_height = height * self.scale
        output_width = width * self.scale
        output_shape = (batch, channel, output_height, output_width)

        # start with black image
        output = img.new_zeros(output_shape)
        tiles_x = math.ceil(width / self.tile_size)
        tiles_y = math.ceil(height / self.tile_size)

        # loop over all tiles
        for y in range(tiles_y):
            for x in range(tiles_x):
                # extract tile from input image
                ofs_x = x * self.tile_size
                ofs_y = y * self.tile_size
                # input tile area on total image
                input_start_x = ofs_x
                input_end_x = min(ofs_x + self.tile_size, width)
                input_start_y = ofs_y
                input_end_y = min(ofs_y + self.tile_size, height)

                # input tile area on total image with padding
                input_start_x_pad = max(input_start_x - self.tile_pad, 0)
                input_end_x_pad = min(input_end_x + self.tile_pad, width)
                input_start_y_pad = max(input_start_y - self.tile_pad, 0)
                input_end_y_pad = min(input_end_y + self.tile_pad, height)

                # input tile dimensions
                input_tile_width = input_end_x - input_start_x
                input_tile_height = input_end_y - input_start_y
                tile_idx = y * tiles_x + x + 1
                input_tile = img[:, :, input_start_y_pad:input_end_y_pad,
                             input_start_x_pad:input_end_x_pad]

                # upscale tile
                try:
                    with torch.no_grad():
                        output_tile = self.model(input_tile)
                except RuntimeError as error:
                    print('Error', error)
                print(f'\tTile {tile_idx}/{tiles_x * tiles_y}')

                # output tile area on total image
                output_start_x = input_start_x * self.scale
                output_end_x = input_end_x * self.scale
                output_start_y = input_start_y * self.scale
                output_end_y = input_end_y * self.scale

                # output tile area without padding
                output_start_x_tile = (input_start_x - input_start_x_pad) * self.scale
                output_end_x_tile = output_start_x_tile + input_tile_width * self.scale
                output_start_y_tile = (input_start_y - input_start_y_pad) * self.scale
                output_end_y_tile = output_start_y_tile + input_tile_height * self.scale

                output[:, :, output_start_y:output_end_y,
                output_start_x:output_end_x] = output_tile[:, :,
                                               output_start_y_tile:output_end_y_tile,
                                               output_start_x_tile:output_end_x_tile]
        return output

    def post_process(self, output):
        if self.mod_scale is not None:
            _, _, h, w = output.size()
            output = output[:, :, 0:h - self.mod_pad_h * self.scale,
                     0:w - self.mod_pad_w * self.scale]
        if self.pre_pad != 0:
            _, _, h, w = output.size()
            output = output[:, :, 0:h - self.pre_pad * self.scale,
                     0:w - self.pre_pad * self.scale]
        return output

    @torch.no_grad()
    def enhance(self, img, outscale=None, alpha_upsampler='realesrgan'):
        h_input, w_input = img.shape[0:2]
        # img: numpy
        img = img.astype(np.float32)
        if np.max(img) > 256:  # 16-bit image
            max_range = 65535
            print('\tInput is a 16-bit image')
        else:
            max_range = 255
        img = img / max_range
        if len(img.shape) == 2:  # gray image
            img_mode = 'L'
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        elif img.shape[2] == 4:  # RGBA image with alpha channel
            img_mode = 'RGBA'
            alpha = img[:, :, 3]
            img = img[:, :, 0:3]
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            if alpha_upsampler == 'realesrgan':
                alpha = cv2.cvtColor(alpha, cv2.COLOR_GRAY2RGB)
        else:
            img_mode = 'RGB'
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # ------------------- process image (without the alpha channel) ------------------- #
        img = self.pre_process(img)
        if self.tile_size > 0:
            img = self.tile_process(img)
        else:
            img = self.process(img)
        output_img = self.post_process(img)
        output_img = output_img.data.squeeze().float().cpu().clamp_(0, 1).numpy()
        output_img = np.transpose(output_img[[2, 1, 0], :, :], (1, 2, 0))
        if img_mode == 'L':
            output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)

        # ------------------- process the alpha channel if necessary ------------------- #
        if img_mode == 'RGBA':
            if alpha_upsampler == 'realesrgan':
                img = self.pre_process(alpha)
                if self.tile_size > 0:
                    img = self.tile_process(img)
                else:
                    img = self.process(img)
                output_alpha = self.post_process(img)
                output_alpha = output_alpha.data.squeeze().float().cpu().clamp_(0,
                                                                                1).numpy()
                output_alpha = np.transpose(output_alpha[[2, 1, 0], :, :], (1, 2, 0))
                output_alpha = cv2.cvtColor(output_alpha, cv2.COLOR_BGR2GRAY)
            else:  # use the cv2 resize for alpha channel
                h, w = alpha.shape[0:2]
                output_alpha = cv2.resize(alpha, (w * self.scale, h * self.scale),
                                          interpolation=cv2.INTER_LINEAR)

            # merge the alpha channel
            output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2BGRA)
            output_img[:, :, 3] = output_alpha

        # ------------------------------ return ------------------------------ #
        if max_range == 65535:  # 16-bit image
            output = (output_img * 65535.0).round().astype(np.uint16)
        else:
            output = (output_img * 255.0).round().astype(np.uint8)

        if outscale is not None and outscale != float(self.scale):
            output = cv2.resize(
                output, (
                    int(w_input * outscale),
                    int(h_input * outscale),
                ), interpolation=cv2.INTER_LANCZOS4)

        return output
