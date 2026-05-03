#!/usr/bin/env bash
set -euo pipefail
poetry run uvicorn src.main:app --reload --port 8000
