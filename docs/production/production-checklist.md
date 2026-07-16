# Production Checklist

- [ ] User, tenant, tool, and data permissions are explicit and tested.
- [ ] Agent steps, time, token, and money budgets are enforced in code.
- [ ] Tool inputs and outputs are typed, bounded, timed out, and audited.
- [ ] Writes are idempotent, previewable, reversible, or approval-gated.
- [ ] Evaluation includes normal, no-answer, stale, adversarial, and outage cases.
- [ ] Traces connect versions, tool calls, cost, latency, policy, and outcome with redaction.
- [ ] Fallback, cancellation, rollback, and incident ownership are documented.
- [ ] Memory has scope, retention, deletion, correction, and tenant isolation.
- [ ] Secrets are externalized; dependencies and model/provider changes are reviewed.
