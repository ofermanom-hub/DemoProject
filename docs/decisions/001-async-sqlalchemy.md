# ADR 001: Use Async SQLAlchemy

## Status: Accepted

## Context
FastAPI is async-native. Using sync SQLAlchemy blocks the event loop.

## Decision
Use `sqlalchemy[asyncio]` with `asyncpg` driver.

## Consequences
- All DB calls must be `await`ed
- Sessions managed via `async_sessionmaker`
- Slightly more boilerplate, but no blocking
