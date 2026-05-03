# Security Review Prompt

Analyze the following code for:
- JWT: algorithm pinning, expiry, signature validation
- Password: bcrypt usage, no plaintext storage
- Auth: dependency injection, route protection
- Secrets: env vars only, never hardcoded
- Input: Pydantic validation on all request bodies
- CORS: restrictive in production

Output findings as: CRITICAL / HIGH / MEDIUM / LOW
