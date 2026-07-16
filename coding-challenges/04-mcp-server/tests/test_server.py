import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from solution.server import McpServer


class ServerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = McpServer()

    def test_lists_capabilities(self) -> None:
        response = self.server.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})

        self.assertEqual(response["result"]["tools"][0]["name"], "sum")

    def test_calls_sum(self) -> None:
        response = self.server.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "sum", "arguments": {"left": 2, "right": 3}}})

        self.assertEqual(response["result"]["content"][0]["text"], "5.0")

    def test_rejects_unknown_method_and_bad_arguments(self) -> None:
        unknown = self.server.handle({"id": 3, "method": "tools/delete"})
        bad = self.server.handle({"id": 4, "method": "tools/call", "params": {"name": "sum", "arguments": {"left": "2", "right": 3}}})

        self.assertEqual(unknown["error"]["code"], -32601)
        self.assertEqual(bad["error"]["code"], -32602)

    def test_reads_health_resource(self) -> None:
        response = self.server.handle({"id": 5, "method": "resources/read", "params": {"uri": "memory://health"}})

        self.assertEqual(response["result"]["contents"][0]["text"], "ok")


if __name__ == "__main__":
    unittest.main()
