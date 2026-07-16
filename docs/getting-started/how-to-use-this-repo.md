# How to Use This Repository

This is a handbook and a practice loop, not a book you must read linearly. A strong study session produces three artifacts: a short spoken answer, a runnable experiment, and a note about a failure mode.

## A 45-minute study loop

1. **Orient (5 min):** choose one page and read its related links.
2. **Answer (10 min):** answer the page's interview question without looking. State assumptions and one trade-off.
3. **Build (20 min):** run or modify the related coding challenge. If the page has no challenge, write a small test or sequence diagram.
4. **Break (5 min):** change one input, dependency, or permission and observe how the design fails.
5. **Explain (5 min):** record a two-minute answer using problem, decision, evidence, and next improvement.

## Choose a starting point

| Your baseline | Start with | Proof of progress |
| --- | --- | --- |
| New to LLM systems | [LLM basics](../fundamentals/llm-basics.md) and [what is an agent?](../agent-engineering/what-is-an-agent.md) | Explain tokens, context, and a bounded loop. |
| Comfortable with APIs | [tool use](../agent-engineering/tool-use.md) and [RAG overview](../rag/rag-overview.md) | Implement Challenge 1 or 2 and name two failure modes. |
| Production engineer | [reliability](../production/reliability.md), [security](../production/security.md), and [system design](../system-design/system-design-framework.md) | Propose SLOs, fallbacks, permissions, and an evaluation plan. |
| Senior/staff candidate | [senior questions](../interview-questions/senior.md) and [multi-agent platform](../system-design/design-a-multi-agent-platform.md) | Defend a boundary, migration plan, and organizational trade-off. |

## Track evidence, not pages

Keep a small table in your notes with columns for concept, implementation, metric, failure, and story. A page is “done” when you can answer a new variant of its question, not when you have highlighted every paragraph.

## How to use the question banks

Hide the answers, set a timer, and answer at the requested level. Then compare your response with the core answer and the senior discussion. Follow-ups are where interviewers test whether you have operated the system rather than only read about it.

## How to contribute while learning

If an explanation is unclear, open an issue with the missing assumption. If you can improve it, submit a focused PR using the relevant [template](../templates/interview-question-template.md). Keep the learner-facing page concise and put implementation detail in a challenge or linked case.
