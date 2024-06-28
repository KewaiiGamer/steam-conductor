#!/usr/bin/env bash

set -euo pipefail

if [[ ! -d ./src ]]; then
  echo "this script needs to be called from the root of the project"
  exit 1
fi

if [[ ! -d ./venv ]]; then
  python -m venv venv
  source venv/bin/activate
fi

pip3 install -e .
pyinstaller --onefile --clean --name conductor-cli src/conductor/cli/__main__.py --dist bin
mkdir -p ~/.local/bin
cp bin/conductor-cli ~/.local/bin/
