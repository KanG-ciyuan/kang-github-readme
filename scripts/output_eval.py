#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def evaluate_case(case: dict) -> dict:
    output = case["recorded_output"]
    normalized = output.casefold()
    missing_required = [
        item for item in case["required"] if item.casefold() not in normalized
    ]
    present_forbidden = [
        item for item in case["forbidden"] if item.casefold() in normalized
    ]
    evidence_matches = case.get("evidence_type") == "recorded_fixture"
    return {
        "id": case["id"],
        "passed": not missing_required and not present_forbidden and evidence_matches,
        "missing_required": missing_required,
        "present_forbidden": present_forbidden,
        "evidence_type": case.get("evidence_type"),
    }


def evaluate_document(data: dict) -> dict:
    results = [evaluate_case(case) for case in data["cases"]]
    passed = sum(item["passed"] for item in results)
    return {
        "evidence_type": "recorded_fixture",
        "provider_backed": False,
        "human_reviewed": False,
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate recorded README output fixtures")
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    data = json.loads(args.cases.read_text(encoding="utf-8"))
    result = evaluate_document(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
