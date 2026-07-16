# System Design Interview Questions

Each prompt expects assumptions, a request path, data and trust boundaries, SLOs, failure handling, evaluation, and two trade-offs.

## Interview Question

Design an agent system whose autonomy is bounded by policy and evidence.

## Difficulty

Intermediate to Staff

## Type

System Design

## Follow-up Questions

Where is authorization enforced? How do you replay a run? What is your fallback when the model is unavailable?

### Q1. Design a grounded customer-support assistant

Clarify policy freshness, tenant access, citation expectations, escalation, and peak traffic. Discuss retrieval quality, no-answer behavior, and approval-gated mutations. See [the support case](../system-design/design-a-customer-support-agent.md).

### Q2. Design a coding agent for a local repository

Clarify read/write permissions, sandboxing, test execution, network access, and developer approval. Discuss workspace snapshots, resumable runs, diff review, and malicious repository content. See [the coding-agent case](../system-design/design-a-coding-agent.md).

### Q3. Design a research agent

Clarify source freshness, citation quality, parallel search, budget, and how conflicting evidence is represented. Discuss source allowlists, provenance, and a human review path. See [the research case](../system-design/design-a-research-agent.md).

### Q4. Design a multi-agent platform

Clarify team tenancy, agent registration, tool permissions, scheduling, queues, traces, and evaluation ownership. Discuss whether agents share memory and how a platform prevents uncontrolled nesting. See [the platform case](../system-design/design-a-multi-agent-platform.md).

### Q5. Design an agent observability platform

Clarify trace cardinality, privacy, retention, sampling, online metrics, replay, and alerting. Discuss a normalized event model and how to join quality outcomes with model and tool versions. See [the observability case](../system-design/design-an-agent-observability-platform.md).
