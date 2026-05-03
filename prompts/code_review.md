# Code Review Prompt

Review the following Python/FastAPI code for:
- Type safety (no `Any`, strict Pydantic models)
- Separation of concerns (core vs api vs integrations)
- Error handling completeness
- Security: input validation, auth, secrets exposure
- Naming clarity and docstrings where needed

Flag each issue as: [BLOCKER] | [SUGGESTION] | [NITPICK]
