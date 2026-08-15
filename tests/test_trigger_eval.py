from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.trigger_eval import classify, evaluate


ROOT = Path(__file__).resolve().parents[1]


class TriggerEvalTest(unittest.TestCase):
    def test_readme_requests_trigger(self) -> None:
        self.assertTrue(classify("只优化这个仓库 README 的简介，其他章节不要动"))
        self.assertTrue(classify("Audit this repository README before editing"))

    def test_near_neighbors_do_not_trigger(self) -> None:
        self.assertFalse(classify("把这份会议记录整理成 Markdown"))
        self.assertFalse(classify("Create, test, and publish a complete Agent Skill"))

    def test_complete_case_set_has_no_routing_errors(self) -> None:
        data = json.loads(
            (ROOT / "evals/trigger-cases.json").read_text(encoding="utf-8")
        )
        result = evaluate(data["cases"])

        self.assertGreaterEqual(result["total"], 24)
        self.assertEqual(result["false_positive"], 0)
        self.assertEqual(result["false_negative"], 0)
        self.assertEqual(result["passed"], result["total"])


if __name__ == "__main__":
    unittest.main()
