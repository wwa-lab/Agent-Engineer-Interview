# Agent Evaluation

## Interview Question

How would you evaluate an agent whose path can change from run to run?

## Short Answer

Evaluate both outcome and trajectory. Build a versioned dataset with representative tasks, expected constraints, and safety cases; measure task success, groundedness, tool correctness, policy compliance, cost, latency, and human escalation. Use deterministic checks where possible and calibrated model-based or human judgments where necessary.

## Evaluation layers

| Layer | Example signal | Best use |
| --- | --- | --- |
| Unit | Tool schema rejects an invalid amount | Fast contract regression |
| Component | Retriever returns a relevant passage in top-k | Retrieval tuning |
| Trajectory | Agent stops within budget and uses allowed tools | Runtime and policy checks |
| Outcome | Answer solves the task with evidence | End-to-end quality |
| Online | User correction, escalation, latency, cost | Production monitoring |

## Design a useful dataset

Include easy, normal, ambiguous, adversarial, stale-data, no-answer, and tool-outage cases. Store the task, allowed context, expected properties, rubric version, model/runtime version, and evaluator rationale. Keep personally sensitive data out or apply a documented redaction and retention policy.

## Model-based judging

An LLM judge can scale semantic review, but it is not ground truth. Use a clear rubric, blind the judge to irrelevant metadata, sample human audits, track agreement, and test for position or style bias. Prefer exact assertions for citations, permissions, JSON shape, and tool arguments.

## Regression policy

Gate releases on critical safety and contract checks first. For softer quality metrics, use confidence intervals or minimum sample sizes instead of reacting to one noisy run. Keep failing examples as fixtures, label intentional behavior changes, and compare cost and latency with quality rather than optimizing a single score.

## Practice

The [evaluation harness challenge](../../coding-challenges/05-agent-evaluation/README.md) shows a small offline evaluator. Extend it with a rubric for citation presence and a report that separates failures by category.
