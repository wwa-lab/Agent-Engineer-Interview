# What Is an Agent?

## Interview Question

What makes a software system an agent rather than a model call or a workflow?

## Why Interviewers Ask This

The label “agent” is often used for any LLM feature. Interviewers want to see whether you can define autonomy precisely and avoid adding an open-ended loop where a deterministic workflow is safer.

## Short Answer

An agent is a software system that uses a model to select or sequence actions toward a goal, observes results, and continues until a stopping condition is reached. The useful distinction is not whether a model is present; it is whether action selection is dynamic and bounded by explicit tools, permissions, budgets, and evaluation.

## Deep Dive

A production agent has at least five boundaries: goal and context, model decision, tool execution, observation, and termination. The runtime owns the loop. It should enforce a maximum number of steps, time and cost budgets, schema validation, authorization, cancellation, and a way to hand control to a person. A workflow may contain model calls, but its transitions are predetermined enough to test as a graph.

## Example

An invoice workflow extracts fields, validates them, and routes exceptions through fixed steps. An accounts-payable agent may choose whether to look up a vendor, ask for missing evidence, or request approval. The latter needs a stronger policy boundary because the model can choose a different path.

## Trade-offs

Dynamic behavior can handle varied tasks and reduce hard-coded branching, but it increases latency, nondeterminism, cost, and attack surface. Start with a workflow and introduce autonomy only at a measured decision boundary.

## Common Mistakes

- Calling a single prompt an agent without an action-observation loop.
- Assuming more autonomy means a better user experience.
- Letting the model decide permissions or termination without runtime checks.

## Follow-up Questions

- Where is the stop condition enforced?
- What happens when a tool returns malformed or adversarial output?
- Which decisions are reversible, and which require human approval?

## Senior-Level Discussion

Discuss autonomy as a risk budget. A useful design makes the action space small, auditable, and reversible, then expands it only when evaluation shows that the extra freedom creates user value.

## Hands-on Exercise

Implement the loop in [Challenge 1](../../coding-challenges/01-tool-calling-agent/README.md), then add a maximum-step test and a denied-tool test.

## Related Topics

[Agent loop](agent-loop.md), [workflows vs agents](workflows-vs-agents.md), [human in the loop](human-in-the-loop.md), [reliability](../production/reliability.md).
