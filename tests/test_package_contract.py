from __future__ import annotations

import json
import re
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


if __name__ == "__main__":
    unittest.main()
