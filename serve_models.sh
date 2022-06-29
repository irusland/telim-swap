#!/bin/bash


torchserve --start \
  --no-config-snapshots \
  --model-store modelstore \
  --ts-config ts-config.properties \
  --foreground