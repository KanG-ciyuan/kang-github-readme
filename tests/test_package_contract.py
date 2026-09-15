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

    def test_manifest_declares_verified_public_install(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "kang-github-readme")
        self.assertEqual(manifest["owner"], "Kang")
        self.assertEqual(manifest["version"], "0.1.1")
        self.assertEqual(manifest["maturity"], "production")
        self.assertEqual(manifest["installation"]["status"], "verified")
        self.assertEqual(manifest["publication"]["status"], "verified")

    def test_manifest_install_status_has_no_honest_value_yet(self) -> None:
        """H-9: the manifest cannot currently state the truth.

        `installation.status` carries no schema and no defined enum. The only
        value `validate_skill.py` accepts is `verified`, so the manifest cannot be
        downgraded to an honest "not yet verified" state without inventing an enum
        value and rewriting the validator's check — both out of scope.

        This test pins the gap rather than hiding it. It fails in two directions:

        * if evidence appears, the README's `to verify` label becomes stale;
        * if the manifest changes to a value that is not `verified`, the validator
          contract and this test must be revisited deliberately.

        Resolution requires the owner to define a `to_verify`-equivalent state in
        the manifest schema (`MANIFEST_SCHEMA_DECISION_REQUIRED`).
        """
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

        # The schema gap is real: no schema file, and no other value is accepted.
        schemas = sorted(ROOT.rglob("*.schema.json"))
        self.assertEqual(schemas, [], "a manifest schema appeared; revisit H-9")

        validator = (ROOT / "scripts/validate_skill.py").read_text(encoding="utf-8")
        self.assertIn(
            'manifest.get("installation", {}).get("status") != "verified"',
            validator,
            "the validator's single accepted value changed; revisit H-9",
        )

        # The contradiction is documented, not silently tolerated.
        self.assertEqual(manifest["installation"]["status"], "verified")
        self.assertEqual(sorted((ROOT / "reports").glob("*install*")), [])

    def test_readme_states_the_unverified_npx_route(self) -> None:
        """The npx route is documented but explicitly not verified.

        This test previously also required the literal sentence
        "Codex 安装已验证". That assertion is gone: the package ships no install
        evidence, so it cannot be satisfied honestly. The evidence rule it was
        trying to express now lives in
        `test_verified_install_claim_requires_shipped_evidence`.
        """
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("https://github.com/KanG-ciyuan/kang-github-readme", english)
        # Both pages must surface the npx route together with its status; the
        # exact sentence is no longer asserted, because the honest label is
        # carried by the evidence rule above.
        for page, text in (("README.md", english), ("README.zh-CN.md", chinese)):
            with self.subTest(page=page):
                self.assertIn("npx", text)
                self.assertIn("to verify", text)

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

    def test_readme_is_a_bilingual_cross_linked_pair(self) -> None:
        """The package documents itself in two languages.

        This test previously required the nine Chinese headings inside
        `README.md` itself, which forced the canonical file to be Chinese-only.
        It now asserts the invariant: both pages exist, they link to each other,
        and each carries its own reader-facing sections in its own language.
        """
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("README.zh-CN.md", english)
        self.assertIn("README.md", chinese)

        for heading in (
            "## Why This Exists",
            "## How It Works",
            "## Example",
            "## Outputs And Artifacts",
            "## Prerequisites",
            "## Evidence And Validation",
            "## FAQ",
            "## Author",
            "## License",
        ):
            with self.subTest(page="README.md", heading=heading):
                self.assertIn(heading, english)

        for heading in (
            "## 为什么需要它",
            "## 工作方式",
            "## 你可以这样说",
            "## 输出内容",
            "## 使用前提",
            "## 证据状态",
            "## 常见问题",
            "## 作者",
            "## 开源许可证",
        ):
            with self.subTest(page="README.zh-CN.md", heading=heading):
                self.assertIn(heading, chinese)

        # The four shipped invocation examples must be reader-facing in both.
        for page, text in (("README.md", english), ("README.zh-CN.md", chinese)):
            with self.subTest(page=page):
                self.assertGreaterEqual(
                    len(re.findall(r'^- [“"]', text, flags=re.MULTILINE)), 4
                )

    def test_verified_install_claim_requires_shipped_evidence(self) -> None:
        """A `verified` claim must be backed by evidence in the package.

        `manifest.json` declares `installation.status: verified`, but nothing
        here — no transcript, log, or test — reproduces an installation. The
        reader-facing pages must therefore carry the `to verify` label instead
        of restating the manifest's claim.

        This test previously required the literal sentence "Codex 安装已验证" in
        `README.md`, which could only be satisfied by publishing a claim the
        repository cannot evidence.
        """
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["installation"]["status"], "verified")

        install_evidence = sorted((ROOT / "reports").glob("*install*"))
        self.assertEqual(
            install_evidence,
            [],
            "install evidence appeared; re-evaluate the reader-facing claim",
        )

        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        for page, text in (("README.md", english), ("README.zh-CN.md", chinese)):
            with self.subTest(page=page):
                self.assertIn("to verify", text)

        for unsupported in (
            "Codex 安装已验证",
            "installation is verified",
            "install is verified",
        ):
            with self.subTest(unsupported=unsupported):
                self.assertNotIn(unsupported, english + chinese)

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
        identity_declarations = re.findall(
            r"(?im)^\s*(?:author|owner)\s*:\s*([^\n]+)$",
            public,
        )
        self.assertTrue(identity_declarations)
        self.assertTrue(
            all(value.strip().strip('"\'') == "Kang" for value in identity_declarations)
        )

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
