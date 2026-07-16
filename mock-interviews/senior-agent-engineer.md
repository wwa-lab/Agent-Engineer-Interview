# Senior Agent Engineer Mock Interview

## 60-minute format

### 1. Project deep dive — 15 minutes

Explain the user problem, constraints, architecture, one failure, metric, and what you would change. The interviewer should ask why a workflow was insufficient and how permissions were enforced.

### 2. Production judgment — 15 minutes

Discuss a quality regression after a model upgrade, a cost spike caused by loops, and an indirect prompt injection through retrieved content. Cover containment, evidence, and prevention.

### 3. System design — 20 minutes

Design a multi-tenant coding agent. Clarify read/write boundaries, sandboxing, durable execution, approval, traces, evaluation, and rollback. Use the [framework](../docs/system-design/system-design-framework.md).

### 4. Leadership — 10 minutes

Explain a build-vs-buy decision, a cross-team disagreement, and how you would set a platform contract without centralizing every prompt.

## Scoring

Score 0–3 for system boundaries, correctness, safety, operations, evidence, and communication. A senior answer is not the one with the most boxes; it makes the risky decisions explicit.
