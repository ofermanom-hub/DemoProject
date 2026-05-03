# Developer Onboarding

## Prerequisites
- Python 3.11+
- Docker + Docker Compose
- `poetry` (`pip install poetry`)

## Setup
```bash
bash scripts/setup.sh
docker-compose up -d db
bash scripts/run_local.sh
```

## Running Tests
```bash
poetry run pytest --cov=src
```

## Branching
- `feat/` — new features
- `fix/` — bug fixes  
- `docs/` — documentation only

Never commit directly to `main`. Always open a PR.
