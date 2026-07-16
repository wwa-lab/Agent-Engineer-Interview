# Intermediate Interview Questions

Each question expects a concrete design, a metric, and a failure path. Target two to four minutes before follow-ups.

## Interview Question

How would you make an agent feature measurable and safe enough to operate?

## Difficulty

Intermediate

## Type

Production, evaluation, design, and security

## Follow-up Questions

Ask what changes at scale, what fails when a dependency is unavailable, and which metric would justify the design.

## Required dimensions

Every answer should touch **Difficulty**, **Type**, **Time**, **core evaluation**, and **follow-up direction**. Strong answers distinguish model behavior from runtime behavior.

### Q1. How would you design a no-answer policy for RAG?

- **Difficulty:** Intermediate · **Type:** Production · **Time:** 3 minutes
- **Core check:** Grounding threshold and user experience.
- **Answer:** Combine retrieval score, evidence coverage, metadata freshness, and answerability checks. If evidence is weak or conflicting, state uncertainty, ask a clarifying question, or escalate instead of filling gaps.
- **Common mistake:** Using one similarity threshold for every query.
- **Follow-up:** How would you calibrate the threshold by intent?

### Q2. How do you choose a chunking strategy?

- **Difficulty:** Intermediate · **Type:** Design · **Time:** 3 minutes
- **Core check:** Retrieval units and context fit.
- **Answer:** Preserve semantic and access-control boundaries, add enough overlap for references, and evaluate chunk sizes against recall, precision, context cost, and citation quality. Tables and code often need structure-aware parsing.
- **Common mistake:** Optimizing chunk size without a test set.
- **Follow-up:** What changes for frequently updated policies?

### Q3. When is hybrid search better than vector search alone?

- **Difficulty:** Intermediate · **Type:** Design · **Time:** 3 minutes
- **Core check:** Lexical versus semantic signals.
- **Answer:** Hybrid search combines exact term matching with semantic similarity, helping queries with IDs, error codes, names, or rare terms while preserving paraphrase recall. Fuse and evaluate rankings rather than assuming one dominates.
- **Common mistake:** Ignoring metadata filters and tenant isolation.
- **Follow-up:** Where would reranking fit?

### Q4. How should an agent handle a failed tool call?

- **Difficulty:** Intermediate · **Type:** Reliability · **Time:** 3 minutes
- **Core check:** Error taxonomy and bounded recovery.
- **Answer:** Classify validation, authorization, transient, timeout, dependency, and business errors. Retry only safe transient failures with a limit and idempotency key; otherwise return a typed observation, choose a safe fallback, or escalate.
- **Common mistake:** Retrying all exceptions.
- **Follow-up:** How would you prevent duplicate writes?

### Q5. How do you make tool calls idempotent?

- **Difficulty:** Intermediate · **Type:** Production · **Time:** 3 minutes
- **Core check:** Distributed-systems reasoning.
- **Answer:** Give each logical action an idempotency key, persist request status, make the downstream operation conditional, and return the original result for a duplicate. Keep side effects behind a policy and audit boundary.
- **Common mistake:** Using a random request ID that changes on retry.
- **Follow-up:** What if the worker crashes after the external side effect?

### Q6. What belongs in session memory versus long-term memory?

- **Difficulty:** Intermediate · **Type:** Design · **Time:** 3 minutes
- **Core check:** Scope, privacy, retention.
- **Answer:** Session memory holds context needed for the current task. Long-term memory should contain user-approved, useful facts with provenance, confidence, expiry, correction, and deletion semantics; raw transcripts should not be the default.
- **Common mistake:** Persisting sensitive facts because they may be useful later.
- **Follow-up:** How do you handle a user correction?

### Q7. Does reflection improve agent quality?

- **Difficulty:** Intermediate · **Type:** Concept · **Time:** 3 minutes
- **Core check:** Cost/quality evidence.
- **Answer:** Reflection can catch missing constraints or formatting errors, but it adds tokens and can reinforce a wrong plan. Use it when a rubric or deterministic check identifies a recoverable issue, and compare against a no-reflection baseline.
- **Common mistake:** Adding a critic loop without measuring net benefit.
- **Follow-up:** What would trigger a second pass?

### Q8. How would you evaluate an agent trajectory?

- **Difficulty:** Intermediate · **Type:** Evaluation · **Time:** 3 minutes
- **Core check:** Outcome and path.
- **Answer:** Check tool allowlist compliance, argument validity, step budget, evidence use, state transitions, and final outcome. Keep exact checks for contracts and use calibrated human/model judgments for semantic quality.
- **Common mistake:** Scoring only the final text.
- **Follow-up:** How do you store a failing trajectory?

### Q9. How can you reduce agent latency?

- **Difficulty:** Intermediate · **Type:** Production · **Time:** 3 minutes
- **Core check:** Budget decomposition.
- **Answer:** Measure model, retrieval, tool, queue, and serialization latency separately. Reduce unnecessary steps, stream user-safe output, parallelize independent reads, cache stable results, and choose a smaller model where evaluation permits.
- **Common mistake:** Optimizing average latency while ignoring p95.
- **Follow-up:** What quality guard prevents an unsafe optimization?

### Q10. How do you estimate agent cost?

- **Difficulty:** Intermediate · **Type:** Production · **Time:** 2 minutes
- **Core check:** Unit economics.
- **Answer:** Estimate input/output tokens per step, number of steps, tool and retrieval cost, retries, storage, and human review. Track cost per successful task and tail behavior rather than one average prompt.
- **Common mistake:** Counting only the final model call.
- **Follow-up:** Which budget should stop a run?

### Q11. How should you test prompt changes?

- **Difficulty:** Intermediate · **Type:** Evaluation · **Time:** 3 minutes
- **Core check:** Regression discipline.
- **Answer:** Version prompt templates and run a representative, adversarial, and no-answer dataset. Compare quality, safety, latency, and cost; require review for critical regressions and retain counterexamples.
- **Common mistake:** Validating on the one example that motivated the change.
- **Follow-up:** How would you handle evaluator disagreement?

### Q12. What is the role of MCP in a platform?

- **Difficulty:** Intermediate · **Type:** Protocol · **Time:** 3 minutes
- **Core check:** Capability versus governance.
- **Answer:** MCP can standardize capability discovery and invocation across hosts, but a platform still needs registry, trust, allowlisting, credentials, sandboxing, quotas, audit, and compatibility management.
- **Common mistake:** Treating discovery as authorization.
- **Follow-up:** How do you roll back a bad server version?

### Q13. When should multiple agents be used?

- **Difficulty:** Intermediate · **Type:** Design · **Time:** 3 minutes
- **Core check:** Decomposition and coordination cost.
- **Answer:** Use multiple agents when roles have distinct context, permissions, or evaluation criteria and the coordination cost is justified. Otherwise a single bounded agent or workflow is easier to test and operate.
- **Common mistake:** Creating agents by persona rather than boundary.
- **Follow-up:** How do agents share state safely?

### Q14. How do you defend against indirect prompt injection?

- **Difficulty:** Intermediate · **Type:** Security · **Time:** 3 minutes
- **Core check:** Trust boundaries.
- **Answer:** Treat documents and tool output as untrusted data, separate instructions from evidence, restrict tool permissions, validate destinations and arguments, redact secrets, and require approval for risky actions. Test realistic malicious content.
- **Common mistake:** Relying on text classification alone.
- **Follow-up:** What if the attack is encoded in an image or code block?

### Q15. How do you design human approval?

- **Difficulty:** Intermediate · **Type:** Production · **Time:** 3 minutes
- **Core check:** Risk and UX.
- **Answer:** Trigger approval for irreversible, high-impact, unusual, or permission-expanding actions. Show the proposed action, evidence, scope, identity, and reversibility; expire stale approvals and record the decision.
- **Common mistake:** Asking for approval after the side effect.
- **Follow-up:** How do you prevent approval fatigue?

### Q16. What should be logged for a tool invocation?

- **Difficulty:** Intermediate · **Type:** Observability · **Time:** 2 minutes
- **Core check:** Auditability with privacy.
- **Answer:** Log run and step IDs, tool/version, validated arguments or a redacted hash, actor and policy decision, timing, result class, retry, and outcome. Separate sensitive payload storage and define retention.
- **Common mistake:** Logging raw tokens and secrets by default.
- **Follow-up:** What is needed for replay?

### Q17. How do you handle model-provider outages?

- **Difficulty:** Intermediate · **Type:** Reliability · **Time:** 3 minutes
- **Core check:** Graceful degradation.
- **Answer:** Set timeouts and circuit breakers, queue resumable work, route to a compatible fallback when evaluation supports it, degrade to search or a workflow, and communicate status. Do not silently switch models if behavior or data handling changes materially.
- **Common mistake:** Infinite retries across providers.
- **Follow-up:** What state is safe to resume?

### Q18. How do you choose a model for a tool-using agent?

- **Difficulty:** Intermediate · **Type:** Design · **Time:** 3 minutes
- **Core check:** Task-fit evaluation.
- **Answer:** Define required tool accuracy, context capacity, latency, cost, privacy, and availability, then compare candidate models on a fixed task set and failure budget. Use routing only when the added complexity pays for itself.
- **Common mistake:** Choosing by benchmark score alone.
- **Follow-up:** How do you detect provider drift?

### Q19. What makes a RAG answer trustworthy?

- **Difficulty:** Intermediate · **Type:** Evaluation · **Time:** 3 minutes
- **Core check:** Evidence linkage.
- **Answer:** It cites accessible, relevant, current evidence; answers only within that evidence; identifies conflicts and uncertainty; and passes exact policy checks. Trust is a property of retrieval, generation, UX, and authorization together.
- **Common mistake:** Treating a citation marker as proof.
- **Follow-up:** How do you test citation correctness?

### Q20. How do you review an agent PR?

- **Difficulty:** Intermediate · **Type:** Production · **Time:** 3 minutes
- **Core check:** Engineering completeness.
- **Answer:** Review contracts, failure paths, permission boundaries, evaluation changes, traces, cost/latency impact, tests, rollback, and user messaging. Ask whether the change enlarges the action space or data retention.
- **Common mistake:** Reviewing only the prompt text.
- **Follow-up:** What evidence blocks merge?

## Practice

Use [agent evaluation](../evaluation/agent-evaluation.md), [MCP](../protocols/mcp.md), and the [system design framework](../system-design/system-design-framework.md) to turn any answer into a small design exercise.
