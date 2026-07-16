"""Minimal deterministic evaluation harness."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    case_id: str
    expected_keywords: tuple[str, ...]
    forbidden_keywords: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    passed: bool
    reasons: tuple[str, ...]


def evaluate(cases: tuple[Case, ...], outputs: dict[str, str]) -> tuple[EvaluationResult, ...]:
    results = []
    for case in cases:
        output = outputs.get(case.case_id, "")
        normalized = output.lower()
        missing = tuple(keyword for keyword in case.expected_keywords if keyword.lower() not in normalized)
        forbidden = tuple(keyword for keyword in case.forbidden_keywords if keyword.lower() in normalized)
        reasons = tuple(f"missing keyword: {keyword}" for keyword in missing) + tuple(f"forbidden keyword: {keyword}" for keyword in forbidden)
        results.append(EvaluationResult(case.case_id, not reasons, reasons))
    return tuple(results)


def pass_rate(results: tuple[EvaluationResult, ...]) -> float:
    if not results:
        return 0.0
    return sum(result.passed for result in results) / len(results)
