# Test Generation Prompt

Generate pytest tests for the following module.

Requirements:
- Unit tests: pure logic, no I/O, mock external calls
- Integration tests: use httpx AsyncClient with ASGITransport
- Cover happy path + at least 2 edge/error cases per function
- Use `pytest.mark.asyncio` for async tests
- No hardcoded secrets
