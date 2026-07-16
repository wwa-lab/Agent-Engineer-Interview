# 05 — Agent Evaluation Harness

Build a small offline harness that evaluates agent outputs against expected properties. The goal is to make failures reportable and regression-friendly, not to pretend that one score captures quality.

## Requirements

- Represent cases with IDs, inputs, expected keywords, and safety constraints.
- Run deterministic checks and return per-case results.
- Report pass rate and failed case IDs.
- Keep evaluator errors visible.

## Run

```bash
python -m unittest discover -s tests -v
```

## Extensions

Add trajectory checks, citation support, latency/cost fields, evaluator versioning, human review samples, and confidence intervals.
