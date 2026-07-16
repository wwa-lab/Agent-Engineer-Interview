"""Starter surface for the tool-calling challenge."""

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolRequest:
    name: str
    arguments: dict[str, Any]


Model = Callable[[tuple[str, ...]], ToolRequest | str]


class ToolCallingAgent:
    def __init__(self, tools: dict[str, Callable[..., Any]], model: Model, max_steps: int = 5) -> None:
        raise NotImplementedError

    def run(self, prompt: str) -> str:
        raise NotImplementedError
