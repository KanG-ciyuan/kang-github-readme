#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "manifest.json",
    "agents/interface.yaml",
    "references/project-type-playbook.md",
    "references/readme-structure-playbook.md",
    "references/evidence-and-claims.md",
    "references/github-metadata.md",
    "evals/trigger-cases.json",
    "evals/output-cases.json",
    "scripts/trigger_eval.py",
    "scripts/output_eval.py",
    "scripts/validate_skill.py",
    "reports/prior-art-research.md",
    "reports/trigger-eval.json",
    "reports/output-eval.json",
    "reports/skill-ir.json",
    "reports/creation-handoff.md",
)

README_HEADINGS = (
    "## 为什么需要它",
    "## 工作方式",
    "## 你可以这样说",
    "## 输出内容",
    "## 使用前提",
    "## 证据状态",
    "## 常见问题",
    "## 作者",
    "## License",
)


def load_json(path: Path, failures: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid JSON: {path.name}: {exc}")
        return {}


def validate(root: Path) -> dict:
    failures: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            failures.append(f"missing required file: {relative}")

    skill_entries = sorted(root.rglob("SKILL.md"))
    if skill_entries != [root / "SKILL.md"]:
        failures.append("package must contain exactly one root SKILL.md")

    if not all((root / relative).is_file() for relative in REQUIRED_FILES):
        return {"ok": False, "failures": failures, "warnings": warnings}

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")
    interface = (root / "agents/interface.yaml").read_text(encoding="utf-8")
    manifest = load_json(root / "manifest.json", failures)
    trigger = load_json(root / "reports/trigger-eval.json", failures)
    output = load_json(root / "reports/output-eval.json", failures)
    skill_ir = load_json(root / "reports/skill-ir.json", failures)
    handoff = (root / "reports/creation-handoff.md").read_text(encoding="utf-8")

    if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
        failures.append("SKILL.md frontmatter is invalid")
    if not re.search(r"(?m)^name: kang-github-readme$", skill):
        failures.append("SKILL.md identity is inconsistent")
    if not re.search(r"(?ms)^description: \|\n\s+Use when ", skill):
        failures.append("SKILL.md description must start with Use when")
    if "metadata:\n  author: Kang" not in skill:
        failures.append("SKILL.md author is inconsistent")

    if manifest.get("name") != "kang-github-readme" or manifest.get("owner") != "Kang":
        failures.append("manifest identity is inconsistent")
    if manifest.get("maturity") != "production":
        failures.append("manifest maturity must be production")
    if manifest.get("installation", {}).get("status") != "not_requested":
        failures.append("manifest installation status is inconsistent")
    if manifest.get("publication", {}).get("status") != "not_requested":
        failures.append("manifest publication status is inconsistent")
    if "Kang GitHub README" not in interface or "Kang GitHub README" not in readme:
        failures.append("public package identity is inconsistent")
    if skill_ir.get("identity", {}).get("owner") != "Kang" or "Owner: Kang" not in handoff:
        failures.append("report identity is inconsistent")

    if trigger.get("passed") != trigger.get("total"):
        failures.append("trigger evaluation is not fully passing")
    if trigger.get("false_positive") != 0 or trigger.get("false_negative") != 0:
        failures.append("trigger evaluation contains routing errors")
    if output.get("passed") != output.get("total") or output.get("failed") != 0:
        failures.append("recorded output evaluation is not fully passing")
    if output.get("evidence_type") != "recorded_fixture":
        failures.append("output evaluation evidence label is invalid")
    if output.get("provider_backed") is not False or output.get("human_reviewed") is not False:
        failures.append("output evaluation overstates its evidence")

    for heading in README_HEADINGS:
        if heading not in readme:
            failures.append(f"README missing section: {heading}")
    if len(re.findall(r'^- [“\"]', readme, flags=re.MULTILINE)) < 4:
        failures.append("README needs at least four natural-language examples")
    if "not yet verified" not in readme:
        failures.append("README must disclose unverified installation and discovery")

    public_paths = [
        root / "SKILL.md",
        root / "README.md",
        root / "agents/interface.yaml",
        *(sorted((root / "references").glob("*.md"))),
        root / "reports/creation-handoff.md",
    ]
    public = "\n".join(path.read_text(encoding="utf-8") for path in public_paths)
    public_lower = public.lower()
    prohibited_phrases = (
        "/users/",
        "not installed locally",
        "author's local installation",
        "personal backup",
        "kang-owned backup",
    )
    for phrase in prohibited_phrases:
        if phrase in public_lower:
            failures.append(f"public content contains prohibited information: {phrase}")
    if re.search(
        r"(?i)(api[_ -]?key|token|cookie|password)\s*[:=]\s*['\"][^'\"]{8,}",
        public,
    ):
        failures.append("public content contains a secret-like value")
    identity_declarations = re.findall(
        r"(?im)^\s*(?:author|owner)\s*:\s*([^\n]+)$",
        public,
    )
    if not identity_declarations or any(
        value.strip().strip('"\'') != "Kang" for value in identity_declarations
    ):
        failures.append("public content contains an inconsistent author identity")
    if re.search(r"(?i)\b(TODO|TBD|FIXME)\b", public):
        failures.append("public content contains placeholder text")

    return {"ok": not failures, "failures": failures, "warnings": warnings}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    result = validate(root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
