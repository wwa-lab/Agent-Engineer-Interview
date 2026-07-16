# Agent Engineer Career Path

An Agent Engineer turns model capabilities into dependable software. The role usually sits between application engineering, platform engineering, and applied ML: you build loops and tools, but you also own interfaces, data, evaluation, observability, and operational behavior.

## Capability map

| Area | Evidence in an interview |
| --- | --- |
| Model and context literacy | You can explain token, context, structured output, and model-selection trade-offs. |
| Agent runtime | You can implement stop conditions, budgets, retries, tool contracts, and human approval. |
| Data and retrieval | You can reason about chunking, freshness, access control, recall, and no-answer behavior. |
| Production ownership | You can define traces, SLOs, evaluation gates, incident response, and rollback. |
| Product judgment | You can bound autonomy and choose a workflow when an agent adds risk without value. |
| Communication | You can make a decision legible to users, reviewers, and future maintainers. |

## What to build

Choose one narrow workflow with a visible constraint: a support triage assistant that must cite policy, a coding agent that must request approval before edits, or a research assistant that tracks evidence. Show the test set, failure behavior, trace fields, and cost assumptions. A thin system with honest limits is stronger evidence than a broad demo that only works on the happy path.

## Interview signal

Interviewers look for boundaries. Ask what the model is allowed to decide, what tools can mutate, what data can be retained, how an answer is evaluated, and how the system degrades. The [system design framework](../system-design/system-design-framework.md) and [resume guide](../job-search/resume-guide.md) help you make those boundaries explicit.
