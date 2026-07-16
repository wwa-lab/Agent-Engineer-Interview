# 01 — Tool Calling Agent

Build a bounded agent that can call two local tools: a calculator and a service-status lookup. The model is represented by a deterministic callback so the tests do not need an API key.

## Requirements

- Validate tool name and JSON-like arguments before execution.
- Return tool errors as observations instead of crashing the whole run.
- Stop on a final answer or `max_steps`.
- Keep tools explicit and easy to authorize.

## Run

```bash
python -m unittest discover -s tests -v
```

## Interview extensions

Add timeouts, an idempotency key for writes, a trace event per step, and a policy callback that can deny a tool. Explain why a tool result is untrusted input.
