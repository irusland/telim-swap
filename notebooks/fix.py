import torch

from models_backend.resgan.model import RealESRGANer

if __name__ == '__main__':
    model = RealESRGANer()
    model_path = '~/.cache/torch/hub/checkpoints/RealESRGAN_x4plus.pth'
    PATH = '~/.cache/torch/hub/checkpoints/RealESRGAN_x4plus_fix.pth'
    loadnet = torch.load(model_path)
    if 'params_ema' in loadnet:
        keyname = 'params_ema'
    else:
        keyname = 'params'
    model.load_state_dict(loadnet[keyname], strict=True)
    model.eval()
    torch.save(model.state_dict(), PATH)
