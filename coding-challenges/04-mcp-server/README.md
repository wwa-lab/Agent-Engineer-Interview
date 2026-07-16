# 04 — Minimal MCP-Style Server

Implement a small JSON-RPC capability server with a `sum` tool and a `health` resource. This is an educational protocol exercise, not a full implementation of any external specification.

## Requirements

- List capabilities explicitly.
- Reject unknown methods and malformed arguments.
- Return JSON-RPC-shaped success and error responses.
- Keep dispatch separate from business logic.

## Run

```bash
python -m unittest discover -s tests -v
```

## Extensions

Add authentication, server versioning, output-size limits, cancellation, audit traces, and a host-side allowlist. Discovery must not grant permission.
