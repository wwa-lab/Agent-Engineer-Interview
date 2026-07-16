# Senior Interview Questions

Senior answers should connect architecture to operating reality. State the boundary, the evidence, and what you would not automate.

## Interview Question

What decision would you make differently after operating an agent for six months?

## Difficulty

Senior / Staff

## Type

Production and system judgment

## Follow-up Questions

Which metric changed your mind? What was the blast radius? How did you migrate without hiding a regression?

### Q1. How do you bound autonomy in a high-impact workflow?

- **Difficulty:** Senior · **Type:** System Design · **Time:** 5 minutes
- **Core check:** Risk, permissions, reversibility, and escalation.
- **Answer:** Partition actions by impact and reversibility, keep policies outside the model, use least-privilege tools, require approval for irreversible actions, and cap budgets. Expand autonomy only after scenario and incident evidence supports it.
- **Common mistake:** Using confidence as the only risk signal.
- **Follow-up:** How would you audit an incorrect approval?

### Q2. How would you design an evaluation program for a changing agent?

- **Difficulty:** Senior · **Type:** Evaluation · **Time:** 5 minutes
- **Core check:** Dataset ownership and release gates.
- **Answer:** Maintain versioned task, safety, and trajectory sets; define exact contract checks and calibrated semantic rubrics; compare quality, cost, latency, and policy compliance; sample production failures into regression tests.
- **Common mistake:** Treating one aggregate score as a release decision.
- **Follow-up:** Who owns the evaluation set and its freshness?

### Q3. What is your strategy for model or provider migration?

- **Difficulty:** Senior · **Type:** Production · **Time:** 5 minutes
- **Core check:** Compatibility and rollback.
- **Answer:** Freeze a baseline, build an adapter for schemas and policy hooks, replay representative and adversarial cases, shadow or canary traffic, compare tail metrics, and retain a fast rollback path. Re-check data handling and tool behavior, not only text quality.
- **Common mistake:** Switching based on price or benchmark headline.
- **Follow-up:** How do you handle a model that is better overall but worse on one safety class?

### Q4. How do you prevent an agent platform from becoming a distributed prompt pile?

- **Difficulty:** Senior · **Type:** Architecture · **Time:** 5 minutes
- **Core check:** Platform boundaries.
- **Answer:** Standardize runtime contracts—context, tools, policy, tracing, evaluation, and cancellation—while allowing domain teams to own prompts and task logic. Version interfaces, provide local test harnesses, and make platform guarantees explicit.
- **Common mistake:** Centralizing every prompt and domain decision.
- **Follow-up:** What belongs in a platform SLA?

### Q5. How would you investigate a sudden quality regression?

- **Difficulty:** Senior · **Type:** Incident · **Time:** 5 minutes
- **Core check:** Evidence-driven debugging.
- **Answer:** Confirm the metric and cohort, compare release/config/provider/model/context versions, sample traces, classify failures, and check data freshness, tool errors, and evaluator drift. Mitigate with rollback or a narrower route, then add a regression fixture.
- **Common mistake:** Tweaking prompts before isolating the changed variable.
- **Follow-up:** Which logs are safe to retain during the incident?

### Q6. How should memory be governed across tenants?

- **Difficulty:** Senior · **Type:** Security · **Time:** 5 minutes
- **Core check:** Isolation, deletion, provenance.
- **Answer:** Namespace by tenant and user, attach purpose and provenance, encrypt and minimize data, enforce read/write policies, provide deletion and correction APIs, and test cross-tenant retrieval. Treat memory writes as privileged actions.
- **Common mistake:** Assuming vector filters alone prove isolation.
- **Follow-up:** How do you verify deletion from indexes and caches?

### Q7. What is your architecture for long-running agent tasks?

- **Difficulty:** Senior · **Type:** System Design · **Time:** 5 minutes
- **Core check:** Durable execution.
- **Answer:** Persist a state machine or event log, make steps resumable and idempotent, run work through a queue, enforce leases and cancellation, checkpoint context references, and expose progress plus human escalation.
- **Common mistake:** Keeping the entire run in one request thread.
- **Follow-up:** How do you recover a worker after a partial side effect?

### Q8. How do you make traces useful without storing sensitive prompts?

- **Difficulty:** Senior · **Type:** Observability · **Time:** 4 minutes
- **Core check:** Debuggability and privacy.
- **Answer:** Log stable identifiers, versions, hashes, sizes, policy results, tool metadata, timing, and redacted excerpts; store sensitive payloads separately with access controls and short retention. Support sampled, consented replay fixtures.
- **Common mistake:** Choosing between “log everything” and “log nothing.”
- **Follow-up:** What is your redaction failure mode?

### Q9. When is multi-agent architecture justified?

- **Difficulty:** Senior · **Type:** Architecture · **Time:** 5 minutes
- **Core check:** Separation of context and authority.
- **Answer:** Justify it when agents have genuinely different tools, data, permissions, or evaluation loops, or when parallel independent work materially improves the objective. Define contracts and ownership; otherwise use one orchestrator or workflow.
- **Common mistake:** Using personas as a substitute for system boundaries.
- **Follow-up:** How do you prevent conflicting writes?

### Q10. How do you design safe tool authorization?

- **Difficulty:** Senior · **Type:** Security · **Time:** 5 minutes
- **Core check:** Identity, policy, and confused-deputy defense.
- **Answer:** The runtime evaluates user, tenant, task, resource, action, and risk—not the model’s prose. Use short-lived scoped credentials, destination validation, approval for elevation, audit logs, and deny-by-default behavior.
- **Common mistake:** Giving the agent a broad service account.
- **Follow-up:** How do you test confused-deputy attacks?

### Q11. How would you decide between build and buy for agent infrastructure?

- **Difficulty:** Senior · **Type:** Strategy · **Time:** 4 minutes
- **Core check:** Total cost and differentiating surface.
- **Answer:** Buy commodity capabilities when their security, reliability, data handling, and integration fit; build the domain-specific policy, evaluation, and user experience that create differentiation. Include migration, lock-in, observability, and incident ownership in total cost.
- **Common mistake:** Comparing license price with engineering cost only.
- **Follow-up:** What exit criteria would you set?

### Q12. How do you handle a production hallucination incident?

- **Difficulty:** Senior · **Type:** Incident · **Time:** 5 minutes
- **Core check:** Containment and learning.
- **Answer:** Stop or narrow the affected action, preserve evidence, notify impacted users as appropriate, classify whether retrieval, model, policy, or UX failed, add a targeted regression case, and ship a measurable mitigation with rollback.
- **Common mistake:** Editing the prompt and closing the incident.
- **Follow-up:** What user harm changes the severity level?

### Q13. What should a platform promise to product teams?

- **Difficulty:** Senior · **Type:** Architecture · **Time:** 4 minutes
- **Core check:** Explicit contracts.
- **Answer:** Promise stable runtime APIs, policy hooks, tracing, evaluation tooling, budgets, and operational support. Do not promise that the model will always be correct; product teams own task-specific quality criteria and user experience.
- **Common mistake:** Hiding provider variance behind vague guarantees.
- **Follow-up:** Which contract needs versioning first?

### Q14. How do you evaluate whether an agent is worth deploying?

- **Difficulty:** Senior · **Type:** Product · **Time:** 4 minutes
- **Core check:** Value, risk, and alternatives.
- **Answer:** Compare it with the current workflow on successful task cost, user time, quality, safety incidents, escalation load, and operational complexity. A more capable demo is not a win if it adds unbounded review or risk.
- **Common mistake:** Optimizing completion rate without measuring harm.
- **Follow-up:** What is the smallest launchable scope?

### Q15. How do you mentor engineers on agent quality?

- **Difficulty:** Senior · **Type:** Behavioral · **Time:** 4 minutes
- **Core check:** Engineering culture.
- **Answer:** Establish shared failure taxonomies, small reproducible fixtures, review questions, and blameless incident learning. Pair model experiments with runtime tests and make uncertainty visible rather than rewarding optimistic demos.
- **Common mistake:** Teaching a framework API instead of transferable boundaries.
- **Follow-up:** How do you resolve disagreement over a quality metric?
