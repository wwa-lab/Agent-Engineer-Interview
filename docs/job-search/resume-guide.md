# Agent Engineer Resume Guide

## What a strong bullet contains

Use **action + system boundary + engineering decision + measured result**. Name the model-independent capability, the constraint, and the evidence.

| Weak | Stronger |
| --- | --- |
| Built an AI agent. | Built a bounded support-triage agent with policy retrieval, typed escalation tools, and approval-gated refunds; raised citation pass rate from 71% to 91% on a 240-case regression set. |
| Added RAG. | Designed hybrid retrieval with metadata filters and reranking for 18k policy chunks; cut unsupported answers 34% while keeping p95 retrieval under 180 ms. |
| Integrated MCP. | Exposed six read-only repository tools through a versioned MCP server, added allowlisting and audit traces, and reduced connector-specific code across three clients. |
| Improved performance. | Added streaming, bounded parallel retrieval, and cached embeddings; reduced p95 response time from 8.4 s to 4.9 s at the same evaluation score. |

Do not invent metrics. If you have no production traffic, report test-set size, latency on a stated machine, cost assumptions, or qualitative constraints.

## Evidence to collect

- Architecture diagram with trust and permission boundaries.
- Evaluation set, rubric, and representative failures.
- Trace screenshot or redacted run explanation.
- Cost and latency budget, including fallbacks.
- A short note on one incident or design change.

## Resume checklist

- Put software fundamentals and ownership near the top.
- Name tools, retrieval, evaluation, observability, and security only when you can explain them.
- Link to a readable project README, not only a demo video.
- Keep bullets outcome-oriented and remove framework name-dropping.
