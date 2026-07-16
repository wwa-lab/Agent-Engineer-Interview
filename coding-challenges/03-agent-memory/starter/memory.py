"""Starter surface for the memory challenge."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Memory:
    user_id: str
    text: str


class MemoryStore:
    def add_session(self, session_id: str, text: str) -> None:
        raise NotImplementedError

    def recall_session(self, session_id: str) -> tuple[str, ...]:
        raise NotImplementedError
