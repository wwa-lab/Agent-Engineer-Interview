import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from solution.evaluate import Case, evaluate, pass_rate


class EvaluationTests(unittest.TestCase):
    def test_reports_pass_and_failure_reasons(self) -> None:
        cases = (
            Case("grounded", ("policy", "citation")),
            Case("unsafe", ("approval",), ("send all",)),
        )
        outputs = {"grounded": "Use the policy with a citation.", "unsafe": "send all records"}

        results = evaluate(cases, outputs)

        self.assertTrue(results[0].passed)
        self.assertFalse(results[1].passed)
        self.assertIn("missing keyword: approval", results[1].reasons)
        self.assertIn("forbidden keyword: send all", results[1].reasons)

    def test_missing_output_fails_closed(self) -> None:
        results = evaluate((Case("missing", ("answer",)),), {})

        self.assertFalse(results[0].passed)
        self.assertEqual(pass_rate(results), 0.0)

    def test_empty_suite_has_zero_rate(self) -> None:
        self.assertEqual(pass_rate(()), 0.0)


if __name__ == "__main__":
    unittest.main()
