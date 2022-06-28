#!/bin/zsh

torchserve --start \
  --no-config-snapshots \
  --model-store modelstore \
  --ts-config modelstore/ts-config.properties
