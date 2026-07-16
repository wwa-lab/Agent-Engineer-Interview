# Workflows vs Agents

## Interview Question

When would you choose a deterministic workflow over an agent?

## Decision rule

Use a workflow when steps, data dependencies, and escalation rules are known and correctness matters more than path flexibility. Use an agent for a bounded decision where the input variety is high and a human would otherwise choose among a small set of tools or actions. Many strong systems combine both: a workflow owns the outer lifecycle and an agent handles one uncertain step.

| Dimension | Workflow | Agent |
| --- | --- | --- |
| Control flow | Explicit graph | Model-selected within a tool set |
| Testing | Path and contract tests | Scenario, trajectory, and policy tests |
| Latency/cost | Easier to budget | More variable |
| Debugging | Reproduce a path | Reproduce context, model, and tool observations |
| Safety | Easier to constrain | Requires runtime limits and authorization |

## Example

For customer-support refunds, a workflow can authenticate the user, load the order, check policy, and route an exception. An agent can classify an ambiguous request or draft an explanation, but the refund mutation should remain behind policy and confirmation.

## Follow-up Questions

- What is the smallest decision that needs autonomy?
- How will you prove the agent does not bypass a workflow gate?
- What happens when model output is unavailable?

## Hands-on Exercise

Rewrite an open-ended “support agent” as a five-step workflow. Mark the one transition where model choice adds measurable value, then define its allowed tools and fallback.
