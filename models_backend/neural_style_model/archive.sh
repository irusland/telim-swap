#!/bin/bash


torch-model-archiver \
  --model-name vgg19 \
  --version 0.1 \
  --model-file models_backend/neural_style_model/model.py \
  --serialized-file ~/.cache/torch/hub/checkpoints/vgg19-dcbb9e9d.pth \
  --extra-files "models_backend/neural_style_model/neural_style_utils.py,models_backend/neural_style_model/contract.py" \
  --handler models_backend/neural_style_model/handler.py \
  --export-path modelstore \
  --force
