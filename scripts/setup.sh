#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt -r ai-service/requirements.txt
echo "Backend and AI Python dependencies installed."
echo "Run npm install inside each frontend app before starting Vite."

