# Skill Assessment

Score each statement from 0 to 2: **0** means “cannot explain yet”, **1** means “can explain with notes”, and **2** means “can explain, implement, and discuss failure modes”.

## Foundations

- I can explain tokens, context windows, embeddings, and why a model can be fluent but wrong.
- I can compare free-form text with structured output and define a validation boundary.
- I can explain a tool schema and distinguish model intent from tool authorization.
- I can describe RAG retrieval recall, grounding, freshness, and a no-answer policy.

## Agent engineering

- I can draw an agent loop with a stop condition, budget, and trace.
- I can decide whether a task needs a workflow or an agent.
- I can explain session memory versus durable memory and a deletion policy.
- I can describe planning, reflection, and human approval without assuming they always improve quality.

## Production

- I can propose metrics for quality, latency, cost, reliability, and safety.
- I can name a prompt-injection path and a defense that does not rely on a secret system prompt.
- I can design retries, idempotency, timeouts, fallbacks, and escalation.
- I can explain how an evaluation set becomes a regression gate.

## System design and communication

- I can clarify users, scale, SLOs, data boundaries, and failure budgets before drawing boxes.
- I can defend a trade-off and name what evidence would change my mind.
- I can tell a project story covering problem, constraints, decisions, failure, result, and learning.
- I can turn implementation details into measurable resume bullets.

## Interpreting your score

| Total | Suggested route |
| --- | --- |
| 0–12 | [Beginner roadmap](../roadmaps/beginner-roadmap.md), then Challenge 1. |
| 13–24 | [Intermediate roadmap](../roadmaps/intermediate-roadmap.md), RAG, evaluation, and two challenges. |
| 25–32 | [Senior roadmap](../roadmaps/senior-roadmap.md), production cases, and system design drills. |
| 33–36 | Focus on depth: incident stories, staff-level trade-offs, and teaching a topic to someone else. |

Re-take the assessment after two weeks. A higher score is useful only if your examples and measurements have become more specific.
