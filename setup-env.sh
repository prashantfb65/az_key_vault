#!/bin/sh
mkdir -p $HOME/.pythonvenv
python3 -m venv $HOME/.pythonvenv/az_key_vault
source $HOME/.pythonvenv/az_key_vault/bin/activate
export PATH="$HOME/.pythonvenv/az_key_vault/bin:$PATH"
export PYTHONDONTWRITEBYTECODE=1
