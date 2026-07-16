# Beginner Interview Questions

Use two minutes per answer. Every prompt includes a difficulty and type so contributors can extend the bank consistently.

## Interview Question

What Agent Engineering fundamentals should a candidate explain clearly before discussing architecture?

## Difficulty

Beginner

## Type

Concept, production, security, and observability

## Follow-up Questions

Ask for one example, one failure mode, and one runtime control for any question below.

## Shared answer frame

For each question, give a definition, a concrete example, one failure mode, and one follow-up decision. “It depends” is useful only after you name the dependency.

### Q1. What is an LLM?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** Predictive generation, context, and uncertainty.
- **Answer:** An LLM predicts tokens conditioned on input context. It is a component that can generate useful plans or text, not a database or a guarantee of truth.
- **Common mistake:** Equating fluent output with verified facts.
- **Follow-up:** Where would you add retrieval or a deterministic check?

### Q2. What is a token?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Context and cost reasoning.
- **Answer:** A token is a model-specific unit of text processing; words may split into multiple tokens. Token count affects context limits, latency, and usage cost.
- **Common mistake:** Assuming characters and tokens have a fixed ratio.
- **Follow-up:** How would you reduce context without hiding important evidence?

### Q3. What is an embedding?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** Semantic representation and retrieval.
- **Answer:** An embedding maps content to a vector so related items can be compared in a learned representation space. It supports retrieval but does not itself prove relevance or authorization.
- **Common mistake:** Treating nearest-neighbor similarity as truth.
- **Follow-up:** What metadata filter should run before or after vector search?

### Q4. What is a prompt?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Context construction.
- **Answer:** A prompt is the structured input context supplied to a model, including instructions, user data, examples, and retrieved evidence. Prompt quality is only one part of system behavior.
- **Common mistake:** Putting security policy only in prose.
- **Follow-up:** Which rules must the runtime enforce independently?

### Q5. What is structured output?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** Validation boundaries.
- **Answer:** Structured output asks for a machine-readable shape, such as JSON matching a schema. The application must still parse, validate, handle missing fields, and reject unsafe values.
- **Common mistake:** Assuming valid JSON means valid business logic.
- **Follow-up:** What should happen on a schema mismatch?

### Q6. What is tool calling?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** Model intent versus execution.
- **Answer:** The model emits a structured request for a registered function; application code validates and authorizes it before execution, then returns an observation. The model does not directly run the function.
- **Common mistake:** Executing arguments without validation.
- **Follow-up:** How do you handle a duplicate call after a retry?

### Q7. What is RAG?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** Grounding and retrieval.
- **Answer:** Retrieval-augmented generation fetches relevant external context and gives it to a model before generation. It can improve freshness and grounding but can still fail when retrieval is poor or evidence conflicts.
- **Common mistake:** Calling any pasted text RAG without a retrieval step.
- **Follow-up:** What do you return when no passage meets the threshold?

### Q8. What is an agent loop?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** Bounded autonomy.
- **Answer:** An agent loop repeatedly builds context, asks for a decision, executes an allowed action, observes the result, and stops on success or a runtime limit.
- **Common mistake:** Letting the prompt define the only stop condition.
- **Follow-up:** Which budget limits would you enforce?

### Q9. What is memory in an agent?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 2 minutes
- **Core check:** State and privacy.
- **Answer:** Memory is persisted state used across turns or tasks. Session memory supports continuity; long-term memory needs explicit scope, retention, correction, deletion, and access control.
- **Common mistake:** Saving every conversation by default.
- **Follow-up:** How can a user delete one memory?

### Q10. What is a workflow?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Determinism.
- **Answer:** A workflow is a defined sequence or graph of steps. It may use a model, but transitions are constrained enough to test and audit.
- **Common mistake:** Using “workflow” and “agent” as synonyms.
- **Follow-up:** Which single step would you make agentic, if any?

### Q11. Why do agents need a stop condition?

- **Difficulty:** Beginner · **Type:** Production · **Time:** 90 seconds
- **Core check:** Failure containment.
- **Answer:** Without a stop condition, a loop can repeat, spend money, or mutate state indefinitely. Enforce step, time, cost, and safety limits in code.
- **Common mistake:** Relying on “finish the task” in a prompt.
- **Follow-up:** What user-facing message explains an exhausted budget?

### Q12. What is hallucination?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Uncertainty.
- **Answer:** It is an output that is unsupported, fabricated, or inconsistent with available evidence. Reduce impact with grounding, abstention, validation, and user-visible uncertainty—not only a stronger prompt.
- **Common mistake:** Treating every wrong answer as the same root cause.
- **Follow-up:** How would you classify the failure in an evaluation set?

### Q13. Why use a system message?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Instruction hierarchy limits.
- **Answer:** It gives stable task guidance and constraints to the model. It is not a security boundary; tools, data access, and authorization must be enforced outside the model.
- **Common mistake:** Storing secrets or permissions in the prompt.
- **Follow-up:** What happens if retrieved text contradicts it?

### Q14. What is temperature?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Sampling intuition.
- **Answer:** Temperature changes the distribution used when sampling tokens. Lower values often make outputs more consistent, but they do not guarantee correctness or deterministic tool behavior.
- **Common mistake:** Assuming zero temperature removes all variation across systems.
- **Follow-up:** Which outputs should be checked with exact assertions?

### Q15. What is a context window?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Context budgeting.
- **Answer:** It is the maximum input and output token budget supported for a model request. More context can add evidence but also cost, latency, and distraction.
- **Common mistake:** Sending the whole database as context.
- **Follow-up:** How do you select and compress evidence?

### Q16. What is a vector database used for?

- **Difficulty:** Beginner · **Type:** Concept · **Time:** 90 seconds
- **Core check:** Retrieval pipeline.
- **Answer:** It stores vectors and supports similarity search, often with metadata filters. It is one retrieval component; chunking, freshness, permissions, and reranking still matter.
- **Common mistake:** Thinking a vector database automatically understands documents.
- **Follow-up:** When would keyword search be better?

### Q17. What is a guardrail?

- **Difficulty:** Beginner · **Type:** Security · **Time:** 90 seconds
- **Core check:** Layered controls.
- **Answer:** A guardrail is a control that limits unsafe input, output, action, or state. Strong designs combine model guidance with schemas, policy checks, sandboxing, permissions, and monitoring.
- **Common mistake:** Treating a classifier as a complete security solution.
- **Follow-up:** Which guardrail must be fail-closed?

### Q18. What is human-in-the-loop?

- **Difficulty:** Beginner · **Type:** Production · **Time:** 90 seconds
- **Core check:** Escalation design.
- **Answer:** A person reviews, approves, corrects, or takes over a system action. The review point should be chosen by risk and reversibility, not added as an indefinite “ask a human” fallback.
- **Common mistake:** Escalating every uncertainty without a queue design.
- **Follow-up:** What information does the reviewer need?

### Q19. What should an agent trace contain?

- **Difficulty:** Beginner · **Type:** Observability · **Time:** 2 minutes
- **Core check:** Debuggability and privacy.
- **Answer:** A trace links one run to model calls, prompt/version identifiers, tool calls, latency, token usage, policy decisions, errors, and final outcome. Sensitive content needs redaction and retention controls.
- **Common mistake:** Logging only the final answer.
- **Follow-up:** How do you reproduce a run without logging secrets?

### Q20. What is prompt injection?

- **Difficulty:** Beginner · **Type:** Security · **Time:** 2 minutes
- **Core check:** Data versus instruction.
- **Answer:** Prompt injection is untrusted content attempting to alter an agent’s instructions or actions. Treat retrieved pages and tool results as data, isolate privileges, validate actions, and require approval for risky mutations.
- **Common mistake:** Believing a stronger system prompt makes the attack impossible.
- **Follow-up:** Give an example involving a tool result.

## Related practice

Start with [Challenge 1](../../coding-challenges/01-tool-calling-agent/README.md), then review [the agent loop](../agent-engineering/agent-loop.md).
