"""Small in-memory store with explicit state scopes."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Memory:
    user_id: str
    text: str


class MemoryStore:
    def __init__(self) -> None:
        self._sessions: dict[str, tuple[str, ...]] = {}
        self._long_term: tuple[Memory, ...] = ()

    def add_session(self, session_id: str, text: str) -> None:
        current = self._sessions.get(session_id, ())
        self._sessions = {**self._sessions, session_id: (*current, text)}

    def recall_session(self, session_id: str) -> tuple[str, ...]:
        return tuple(self._sessions.get(session_id, ()))

    def add_long_term(self, user_id: str, text: str) -> None:
        self._long_term = (*self._long_term, Memory(user_id, text))

    def recall_long_term(self, user_id: str, query: str = "") -> tuple[str, ...]:
        normalized = query.lower().strip()
        return tuple(memory.text for memory in self._long_term if memory.user_id == user_id and normalized in memory.text.lower())

    def forget_long_term(self, user_id: str, text: str) -> int:
        retained = tuple(memory for memory in self._long_term if not (memory.user_id == user_id and memory.text == text))
        removed = len(self._long_term) - len(retained)
        self._long_term = retained
        return removed
