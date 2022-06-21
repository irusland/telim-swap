import json
import logging
import shutil

import requests

from src.neural_net_clients.base_neural_net import NeuralNet


class Image:
    pass


logger = logging.getLogger(__name__)


class ImSwapNeuralNet(NeuralNet):
    def __init__(self):
        pass

    def swap_style(self, style_image: Image, content_image: Image) -> Image:
        url = 'http://localhost:8080/predictions/dcgan_fashiongen'
        r = requests.post(
            url,
            data=json.dumps({"number_of_images": 64, "input_gender": "Men",
                             "input_category": "SHIRTS", "input_pose": "id_gridfs_1"}),
            headers={"Content-Type": "application/json"},
            stream=True
        )
        logger.info(r.status_code)
        path = 'gen.jpg'
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

            with open(path, 'rb') as f:
                return f.read()
        return content_image
