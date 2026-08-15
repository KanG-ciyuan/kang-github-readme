from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageContractTest(unittest.TestCase):
    def test_required_root_files_exist(self) -> None:
        for relative in (
            "SKILL.md",
            "README.md",
            "LICENSE",
            "manifest.json",
            "agents/interface.yaml",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_skill_identity_and_trigger_description(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^name: kang-github-readme$")
        self.assertRegex(text, r"(?ms)^description: \|\n\s+Use when ")
        self.assertIn("metadata:\n  author: Kang", text)

    def test_public_files_exclude_owner_local_state(self) -> None:
        public = "\n".join(
            (ROOT / name).read_text(encoding="utf-8")
            for name in ("SKILL.md", "README.md")
        ).lower()
        for forbidden in (
            "not installed locally",
            "author's local installation",
            "kang-owned backup",
            "/users/kang/",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, public)

    def test_manifest_declares_production_without_install_claim(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "kang-github-readme")
        self.assertEqual(manifest["owner"], "Kang")
        self.assertEqual(manifest["maturity"], "production")
        self.assertEqual(manifest["installation"]["status"], "not_requested")

    def test_only_one_discoverable_skill_entrypoint_exists(self) -> None:
        entries = sorted(ROOT.rglob("SKILL.md"))
        self.assertEqual(entries, [ROOT / "SKILL.md"])

    def test_production_package_files_exist(self) -> None:
        required = (
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
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_readme_is_a_chinese_first_product_page(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"[\u4e00-\u9fff]")
        for heading in (
            "## 为什么需要它",
            "## 工作方式",
            "## 你可以这样说",
            "## 输出内容",
            "## 使用前提",
            "## 证据状态",
            "## 常见问题",
            "## 作者",
            "## License",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)
        examples = re.findall(r'^- [“\"]', text, flags=re.MULTILINE)
        self.assertGreaterEqual(len(examples), 4)

    def test_evaluation_reports_use_honest_labels(self) -> None:
        trigger = json.loads(
            (ROOT / "reports/trigger-eval.json").read_text(encoding="utf-8")
        )
        output = json.loads(
            (ROOT / "reports/output-eval.json").read_text(encoding="utf-8")
        )
        self.assertEqual(trigger["false_positive"], 0)
        self.assertEqual(trigger["false_negative"], 0)
        self.assertEqual(output["evidence_type"], "recorded_fixture")
        self.assertFalse(output["provider_backed"])
        self.assertFalse(output["human_reviewed"])

    def test_public_package_excludes_secret_values_and_other_person_identity(self) -> None:
        public_paths = [
            ROOT / "SKILL.md",
            ROOT / "README.md",
            ROOT / "agents/interface.yaml",
            *sorted((ROOT / "references").glob("*.md")),
        ]
        public = "\n".join(
            path.read_text(encoding="utf-8") for path in public_paths
        )
        self.assertNotRegex(
            public,
            r"(?i)(api[_ -]?key|token|cookie|password)\s*[:=]\s*['\"][^'\"]{8,}",
        )
        for forbidden_identity in ("乔木", "qiaomu", "anthropic"):
            with self.subTest(forbidden_identity=forbidden_identity):
                self.assertNotIn(forbidden_identity, public.lower())

    def test_package_validator_returns_clean_result(self) -> None:
        completed = subprocess.run(
            [sys.executable, "scripts/validate_skill.py", "."],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        result = json.loads(completed.stdout)
        self.assertTrue(result["ok"])
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["warnings"], [])


if __name__ == "__main__":
    unittest.main()
