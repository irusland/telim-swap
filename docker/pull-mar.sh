#!/bin/bash
set -e

git clone --verbose --no-checkout https://github.com/irusland/telim-swap.git || echo already exists
(
  cd telim-swap
  git lfs pull --include modelstore
  git lfs logs last
)
ln -sf telim-swap/modelstore modelstore
