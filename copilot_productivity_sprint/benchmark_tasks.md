# Benchmark Tasks

A small, varied set of coding tasks used to benchmark AI-assisted development. Each task is designed to be solvable in 15–30 minutes and includes requirements, inputs, outputs, and acceptance criteria.

---

## Task 1 - CRUD Endpoint with Validation

**Requirements**:
Implement a `POST /users` endpoint in Python (Flask or FastAPI) that creates a user.
- Request body must be JSON with `name` and `email` fields.
- Validate that `email` is a well-formed email address and `name` is a non-empty string.
- Persist the user in an in-memory store and assign a unique integer `id`.

**Inputs**:
```json
{ "name": "Ada Lovelace", "email": "ada@example.com" }