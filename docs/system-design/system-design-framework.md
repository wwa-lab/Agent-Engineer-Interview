# Agent System Design Framework

## The interview flow

1. **Clarify:** users, task boundary, geography, data sensitivity, scale, latency, availability, and what “good” means.
2. **Choose autonomy:** identify which transitions are deterministic, model-assisted, agentic, or human-approved.
3. **Define contracts:** model output schema, tool inputs/outputs, identity, permissions, budgets, and cancellation.
4. **Draw the path:** client → gateway → context/retrieval → orchestrator → model → tool sandbox → stores → response.
5. **Add quality:** offline dataset, component checks, trajectory checks, online feedback, and rollback gates.
6. **Add operations:** traces, logs, metrics, queues, retries, timeouts, rate limits, and incident runbooks.
7. **Name trade-offs:** choose two decisions, explain the alternative, and say what evidence would change the choice.

## Minimum architecture questions

- Where is tenant and user authorization enforced?
- Which data is retrieved, copied into context, or persisted to memory?
- How do you prevent duplicate mutations after a retry?
- What happens when the model, retriever, tool, or evaluator is unavailable?
- How can an operator reconstruct one run without storing raw secrets?

## Useful default boundaries

Keep orchestration separate from tool execution. Make read tools broadly reusable, but keep write tools narrow and approval-gated. Put context assembly behind a versioned interface. Store run metadata separately from sensitive content, with retention and deletion controls.

## Trade-off examples

- More model autonomy can reduce hard-coded branching but increases variance and audit burden.
- A larger context can improve recall but raises cost, latency, and distraction.
- Synchronous tools simplify user feedback; queues improve resilience for long work.
- Centralized memory improves reuse; per-tenant stores improve isolation and deletion.

Use the individual cases for practice: [RAG assistant](design-a-rag-assistant.md), [coding agent](design-a-coding-agent.md), [research agent](design-a-research-agent.md), [support agent](design-a-customer-support-agent.md), [multi-agent platform](design-a-multi-agent-platform.md), and [observability platform](design-an-agent-observability-platform.md).
