# Coding Challenges

Each challenge is a small interview-sized project. Read the brief, inspect `starter/`, write or extend tests in `tests/`, then compare your approach with `solution/`. The solutions intentionally avoid provider SDKs so the important contracts are visible and the default tests run offline.

## Common commands

```bash
cd coding-challenges/01-tool-calling-agent
python -m unittest discover -s tests -v
```

Python 3.11+ is recommended. Every directory contains `README.md`, `requirements.txt`, `starter/`, `solution/`, and `tests/`.

| Challenge | Interview signal | Main failure path |
| --- | --- | --- |
| [01 Tool calling agent](01-tool-calling-agent/README.md) | Typed actions and bounded loops | Unknown tool, invalid arguments, step budget |
| [02 RAG pipeline](02-rag-pipeline/README.md) | Retrieval and grounding | Empty or irrelevant evidence |
| [03 Agent memory](03-agent-memory/README.md) | State scope and privacy | Cross-session leakage and deletion |
| [04 MCP server](04-mcp-server/README.md) | Protocol contracts | Invalid JSON-RPC method/arguments |
| [05 Evaluation harness](05-agent-evaluation/README.md) | Quality measurement | Failing rubric and regression reporting |

## Interview practice

For each challenge, be prepared to explain what you would change for concurrency, persistence, authorization, observability, and a real model provider.
