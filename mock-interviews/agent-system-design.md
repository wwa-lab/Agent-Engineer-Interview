# Agent System Design Mock Interview

## Prompt

Design a customer-support agent that answers from tenant-specific policy, can create a ticket, and may issue a refund only after approval.

## Expected discussion

- Clarify tenant scale, policy freshness, refund rules, p95 latency, and escalation SLO.
- Separate retrieval and drafting from mutation authorization.
- Add document versioning, citations, no-answer behavior, and a human review queue.
- Use idempotency for ticket/refund actions and trace every decision.
- Evaluate normal, stale, ambiguous, malicious, and tool-outage cases.

## Follow-ups

What happens when policy documents conflict? How do you migrate models? How can a reviewer see evidence without exposing unrelated customer data? What is the safe fallback when the policy store is unavailable?
