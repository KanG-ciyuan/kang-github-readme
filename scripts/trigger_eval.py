#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


README_TERMS = (
    "readme",
    "github description",
    "description 和 topics",
    "description、topics",
    "repository presentation",
    "仓库介绍",
)

ACTION_TERMS = (
    "create",
    "write",
    "rewrite",
    "improve",
    "audit",
    "review",
    "check",
    "plan",
    "创建",
    "写",
    "改",
    "优化",
    "审计",
    "检查",
    "规划",
    "整理",
)

EXCLUDED_PATTERNS = (
    "meeting notes",
    "会议记录",
    "marketing landing page",
    "小红书",
    "markdown 表格",
    "nested list in markdown",
    "登录按钮",
    "unit tests",
    "502",
    "deployment fails",
    "internal api design",
    "内部 api 设计",
    "release notes",
    "完整 skill",
    "complete agent skill",
)


def classify(text: str) -> bool:
    normalized = " ".join(text.lower().split())
    if any(pattern in normalized for pattern in EXCLUDED_PATTERNS):
        return False
    has_readme_subject = any(term in normalized for term in README_TERMS)
    has_action = any(term in normalized for term in ACTION_TERMS)
    return has_readme_subject and has_action


def evaluate(cases: list[dict]) -> dict:
    results = []
    false_positive = 0
    false_negative = 0

    for case in cases:
        actual = classify(case["text"])
        expected = bool(case["expected"])
        passed = actual == expected
        if actual and not expected:
            false_positive += 1
        elif expected and not actual:
            false_negative += 1
        results.append(
            {
                "id": case["id"],
                "family": case["family"],
                "expected": expected,
                "actual": actual,
                "passed": passed,
            }
        )

    return {
        "total": len(results),
        "passed": sum(item["passed"] for item in results),
        "false_positive": false_positive,
        "false_negative": false_negative,
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate README Skill routing cases")
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    data = json.loads(args.cases.read_text(encoding="utf-8"))
    result = evaluate(data["cases"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
