# 03 — Agent Memory

Implement session memory and long-term memory with explicit user scope. The challenge emphasizes retention and deletion semantics rather than a specific database.

## Requirements

- Session memory is isolated by session ID.
- Long-term memory is isolated by user ID and can be recalled by keyword.
- Deletion removes matching durable memories.
- Returned collections do not expose mutable internal state.

## Run

```bash
python -m unittest discover -s tests -v
```

## Extensions

Add TTL, provenance, confidence, encryption, tenant scope, and an audit event for every memory write/delete.
