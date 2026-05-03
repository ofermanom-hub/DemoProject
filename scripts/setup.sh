#!/usr/bin/env bash
set -euo pipefail
pip install poetry
poetry install
cp .env.example .env
echo "✅ Setup complete. Edit .env then run: poetry run uvicorn src.main:app --reload"
