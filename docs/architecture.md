# Architecture

## Layers

| Layer | Path | Responsibility |
|---|---|---|
| API | `src/api/` | HTTP routing, request/response schemas |
| Core | `src/core/` | Business logic — no I/O, fully testable |
| Integrations | `src/integrations/` | External APIs, DBs, queues |
| Auth | `src/auth/` | JWT creation/validation, password hashing |
| Config | `src/config/` | Pydantic settings, env var loading |

## Key Decisions

- Async-first: all DB and HTTP calls are `async/await`
- Repository pattern: core/ never imports DB directly
- Settings via `pydantic-settings`: typed, env-driven, no config files

See `docs/decisions/` for ADRs.
