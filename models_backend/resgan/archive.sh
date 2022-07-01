#!/bin/bash


torch-model-archiver \
  --model-name resgan \
  --version 0.1 \
  --model-file models_backend/resgan/model.py \
  --serialized-file ~/.cache/torch/hub/checkpoints/RealESRGAN_x4plus_fix.pth \
  --handler models_backend/resgan/handler.py \
  --export-path modelstore \
  --force
