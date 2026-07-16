# Project Storytelling

Use this structure for a two-to-five-minute answer:

1. **Problem:** Who needed what, and why was a normal search or workflow insufficient?
2. **Constraints:** Scale, latency, data access, safety, model budget, and team limits.
3. **Architecture:** The smallest diagram that explains the request path and boundaries.
4. **Key decisions:** Why this retrieval strategy, tool interface, model, memory, or workflow boundary?
5. **Trade-offs:** What did you intentionally give up?
6. **Failure:** Describe a real or deliberately tested failure, including impact.
7. **Improvement:** What changed, and what metric or test justified it?
8. **Result:** Quantify quality, latency, cost, adoption, or operational load.
9. **Lessons learned:** State what you would do differently now.

## Example outline

“Support agents needed grounded policy answers, but policy pages changed weekly and refunds were irreversible. We used filtered retrieval for policy text and kept refund execution behind a typed approval tool. Early tests showed stale chunks caused confident wrong answers, so we added document version checks and a no-answer threshold. Citation pass rate rose from 71% to 91% on 240 cases while p95 stayed under five seconds. The lesson was to treat freshness and authorization as first-class product requirements, not prompt wording.”

## Follow-up drill

Prepare answers to: Why not a workflow? Why this model? What happens when retrieval is empty? How did you detect a regression? What would you remove if cost doubled? Which user action still requires approval?
