import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from solution.agent import ToolCallingAgent, ToolRequest, calculate, service_status


class ToolCallingAgentTests(unittest.TestCase):
    def test_calls_a_tool_then_returns_final_answer(self) -> None:
        decisions = iter((ToolRequest("calculate", {"expression": "2 + 3"}), "The result is five."))
        agent = ToolCallingAgent({"calculate": calculate}, lambda _: next(decisions))

        self.assertEqual(agent.run("calculate 2 + 3"), "The result is five.")

    def test_unknown_tool_becomes_observation(self) -> None:
        observations: list[tuple[str, ...]] = []
        decisions = iter((ToolRequest("missing", {}), "I cannot use that tool."))
        agent = ToolCallingAgent({}, lambda context: (observations.append(context) or next(decisions)))

        self.assertEqual(agent.run("check"), "I cannot use that tool.")
        self.assertIn("unknown tool missing", observations[1][-1])

    def test_stops_when_step_budget_is_reached(self) -> None:
        agent = ToolCallingAgent({"status": service_status}, lambda _: ToolRequest("status", {"service": "search"}), max_steps=2)

        self.assertIn("step budget", agent.run("loop"))

    def test_tool_validation_and_local_tools(self) -> None:
        with self.assertRaises(ValueError):
            calculate("__import__('os')")
        self.assertEqual(service_status("search"), "healthy")


if __name__ == "__main__":
    unittest.main()
