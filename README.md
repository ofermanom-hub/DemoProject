# Enterprise FastAPI Template

Production-grade FastAPI starter with auth, integrations, CI, and AI-assisted development.

## Stack
- **Python 3.11** + **FastAPI** + **Pydantic v2**
- **SQLAlchemy 2** (async) + **asyncpg** + **Alembic**
- **JWT** (python-jose) + **bcrypt** (passlib)
- **Pytest** + **httpx** for testing
- **Ruff** + **mypy** for linting/types
- **GitHub Actions** CI

## Project Structure
```
src/
  api/          # HTTP layer (routes, schemas)
  core/         # Business logic — pure, testable
  integrations/ # External APIs, DB clients
  auth/         # JWT + password hashing
  models/       # SQLAlchemy ORM models
  config/       # Pydantic settings
tests/
  unit/         # Pure logic, no I/O
  integration/  # Full request/response via ASGI
prompts/        # Reusable Claude prompts
docs/           # Architecture, onboarding, ADRs
```

## Quick Start
```bash
bash scripts/setup.sh
docker-compose up -d db
bash scripts/run_local.sh
# → http://localhost:8000/docs
```

## Testing
```bash
poetry run pytest --cov=src --cov-report=term-missing
```

## Architecture
See [docs/architecture.md](docs/architecture.md)

## Why This Structure
- `core/` = pure logic → testable without HTTP or DB
- `integrations/` = external I/O isolated → easy to mock/swap
- `auth/` = dedicated module → clear security surface
- `prompts/` = reusable AI workflows → systematic, not ad-hoc
