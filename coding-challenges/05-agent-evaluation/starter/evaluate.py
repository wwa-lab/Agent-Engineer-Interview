"""Starter surface for the evaluation challenge."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    case_id: str
    expected_keywords: tuple[str, ...]


def evaluate(cases: tuple[Case, ...], outputs: dict[str, str]) -> tuple[bool, ...]:
    raise NotImplementedError
