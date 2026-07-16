import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from solution.memory import MemoryStore


class MemoryTests(unittest.TestCase):
    def test_session_memory_isolated_by_session(self) -> None:
        store = MemoryStore()
        store.add_session("a", "draft report")
        store.add_session("b", "private note")

        self.assertEqual(store.recall_session("a"), ("draft report",))
        self.assertEqual(store.recall_session("b"), ("private note",))

    def test_long_term_memory_isolated_by_user(self) -> None:
        store = MemoryStore()
        store.add_long_term("alice", "prefers concise answers")
        store.add_long_term("bob", "prefers detailed answers")

        self.assertEqual(store.recall_long_term("alice", "prefers"), ("prefers concise answers",))

    def test_delete_removes_only_matching_memory(self) -> None:
        store = MemoryStore()
        store.add_long_term("alice", "prefers concise answers")
        store.add_long_term("alice", "works in finance")

        self.assertEqual(store.forget_long_term("alice", "prefers concise answers"), 1)
        self.assertEqual(store.recall_long_term("alice"), ("works in finance",))

    def test_recall_returns_a_snapshot(self) -> None:
        store = MemoryStore()
        store.add_session("a", "one")
        snapshot = store.recall_session("a")

        self.assertIsInstance(snapshot, tuple)
        self.assertEqual(snapshot, ("one",))


if __name__ == "__main__":
    unittest.main()
