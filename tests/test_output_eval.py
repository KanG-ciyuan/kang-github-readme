from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.output_eval import evaluate_case, evaluate_document


ROOT = Path(__file__).resolve().parents[1]


class OutputEvalTest(unittest.TestCase):
    def test_required_and_forbidden_assertions(self) -> None:
        case = {
            "id": "sample",
            "recorded_output": "Scope lock: introduction only. R1 Rewrite.",
            "required": ["Scope lock", "R1 Rewrite"],
            "forbidden": ["installation changed"],
            "evidence_type": "recorded_fixture",
        }
        result = evaluate_case(case)
        self.assertTrue(result["passed"])
        self.assertEqual(result["missing_required"], [])
        self.assertEqual(result["present_forbidden"], [])

    def test_broken_fixture_is_rejected(self) -> None:
        case = {
            "id": "broken",
            "recorded_output": "The installation changed.",
            "required": ["Scope lock"],
            "forbidden": ["installation changed"],
            "evidence_type": "recorded_fixture",
        }
        result = evaluate_case(case)
        self.assertFalse(result["passed"])
        self.assertEqual(result["missing_required"], ["Scope lock"])
        self.assertEqual(result["present_forbidden"], ["installation changed"])

    def test_complete_recorded_fixture_set_passes_honestly(self) -> None:
        data = json.loads(
            (ROOT / "evals/output-cases.json").read_text(encoding="utf-8")
        )
        result = evaluate_document(data)

        self.assertEqual(result["evidence_type"], "recorded_fixture")
        self.assertFalse(result["provider_backed"])
        self.assertFalse(result["human_reviewed"])
        self.assertEqual(result["total"], 8)
        self.assertEqual(result["passed"], 8)
        self.assertEqual(result["failed"], 0)


if __name__ == "__main__":
    unittest.main()
