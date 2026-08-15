# Kang GitHub README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Production-grade `kang-github-readme` Skill that previews repository-specific README improvements, locks approved scope, protects public facts and permissions, and validates trigger and output behavior without installing or publishing the Skill.

**Architecture:** A lean root `SKILL.md` owns routing and the preview-first workflow. Focused references hold project classification, dynamic README modules, evidence rules, and GitHub metadata boundaries; deterministic Python scripts validate the package, trigger cases, and recorded output fixtures. Generated reports distinguish structural evidence from missing provider or human evidence.

**Tech Stack:** Agent Skills Markdown/YAML, JSON eval fixtures, Python 3 standard library, `unittest`, Git.

---

## File Map

- `SKILL.md`: trigger boundary, routing precedence, preview-first workflow, scope lock, permissions, and output contract.
- `README.md`: public product page for users of the Skill.
- `LICENSE`: MIT license owned by Kang.
- `manifest.json`: identity, version, maturity, review cadence, and permission model.
- `agents/interface.yaml`: display name, concise prompt, natural-language examples, and compatibility metadata.
- `references/project-type-playbook.md`: repository type, audience, visibility, language, and bounded inspection rules.
- `references/readme-structure-playbook.md`: dynamic modules, preview shape, incremental edit rules, and visual evidence.
- `references/evidence-and-claims.md`: fact ledger, secrets, stale content, links, and claim boundaries.
- `references/github-metadata.md`: Description, Topics, homepage, social preview, and separate authorization.
- `evals/trigger-cases.json`: positive, negative, and near-neighbor routing cases.
- `evals/output-cases.json`: recorded preview fixtures and machine-checkable assertions.
- `scripts/validate_skill.py`: package, identity, privacy, and README contract validator.
- `scripts/trigger_eval.py`: deterministic routing regression runner.
- `scripts/output_eval.py`: recorded-fixture output contract runner.
- `tests/test_package_contract.py`: package and public-boundary tests.
- `tests/test_trigger_eval.py`: routing runner tests.
- `tests/test_output_eval.py`: output assertion runner tests.
- `reports/prior-art-research.md`: dated sources, lessons, rejections, and missing evidence.
- `reports/trigger-eval.json`: generated routing result.
- `reports/output-eval.json`: generated recorded-fixture result with evidence label.
- `reports/skill-ir.json`: platform-neutral identity, inputs, outputs, permissions, and exclusions.
- `reports/creation-handoff.md`: reference lessons, original contributions, evidence labels, and missing evidence.

### Task 1: Research Existing README Skills And Methods

**Files:**
- Create: `reports/prior-art-research.md`

- [ ] **Step 1: Run read-only catalog research**

Run from `/Users/kang/.codex/skills/qiaomu-meta-skill`:

```bash
python3 scripts/research_prior_art.py \
  "github readme generator" \
  "repository documentation readme" \
  "readme audit evidence" \
  --summary \
  --output /tmp/kang-github-readme-prior-art.json
```

Expected: candidate summary from at least one source, or a recorded source failure. Do not execute candidate code.

- [ ] **Step 2: Inspect only relevant candidate instructions and licenses**

For each shortlisted candidate, record repository, Skill path, license, maintenance signal, and the specific mechanism worth keeping or rejecting. Never combine installs and stars into one quality score.

- [ ] **Step 3: Write the research report**

Create `reports/prior-art-research.md` with these exact sections:

```markdown
# Prior-Art Research

## Scope And Date
## Queries And Sources
## Candidate Comparison
## Keep
## Adapt
## Reject
## Original Contributions
## Missing Evidence
```

The report must name inspected sources when available. If all catalogs fail, `Missing Evidence` must state that no external candidate was inspected and the implementation proceeds only from the approved local design.

- [ ] **Step 4: Commit research evidence**

```bash
git add reports/prior-art-research.md
git commit -m "docs: research GitHub README skill prior art"
```

### Task 2: Establish The Package Contract With A Failing Test

**Files:**
- Create: `tests/test_package_contract.py`
- Create: `SKILL.md`
- Create: `README.md`
- Create: `LICENSE`
- Create: `manifest.json`
- Create: `agents/interface.yaml`

- [ ] **Step 1: Write the failing package test**

Create `tests/test_package_contract.py`:

```python
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
```

- [ ] **Step 2: Run the test and verify RED**

```bash
python3 -m unittest tests.test_package_contract -v
```

Expected: FAIL because `SKILL.md`, `README.md`, `LICENSE`, `manifest.json`, and `agents/interface.yaml` do not exist.

- [ ] **Step 3: Create the minimal root package**

Create `SKILL.md` with this frontmatter and section skeleton:

```markdown
---
name: kang-github-readme
description: |
  Use when creating, auditing, restructuring, or selectively improving a GitHub repository README or public repository presentation, including Description, Topics, homepage metadata, project-specific evidence, screenshots, installation guidance, or a preview-before-edit request. Exclude ordinary Markdown editing, advertising copy, code or deployment fixes, syntax-only questions, and end-to-end Skill engineering owned by a Meta Skill.
metadata:
  author: Kang
  version: "0.1.0"
---

# Kang GitHub README

## Responsibility
## Routing Boundary
## Default Workflow
## Preview Contract
## Scope Lock
## Permission Boundary
## Verification
## Output Contract
```

Create `manifest.json`:

```json
{
  "name": "kang-github-readme",
  "version": "0.1.0",
  "owner": "Kang",
  "maturity": "production",
  "review_cadence": "manual",
  "installation": {"status": "not_requested"},
  "publication": {"status": "not_requested"}
}
```

Create `agents/interface.yaml` with display name `Kang GitHub README`, a short description, a preview-first default prompt, and four examples covering create, section-only improvement, audit-only, and metadata review.

Create `README.md` with a Chinese-first value statement, intended users, preview-first behavior, natural-language examples, evidence boundary, prerequisites, troubleshooting, author, and license. Do not claim installation, publication, provider-backed evaluation, or human preference evidence.

Create an MIT `LICENSE` with `Copyright (c) 2026 Kang`.

- [ ] **Step 4: Run the package test and verify GREEN**

```bash
python3 -m unittest tests.test_package_contract -v
```

Expected: PASS.

- [ ] **Step 5: Commit the root contract**

```bash
git add SKILL.md README.md LICENSE manifest.json agents/interface.yaml tests/test_package_contract.py
git commit -m "feat: establish Kang GitHub README package"
```

### Task 3: Implement Trigger Boundaries

**Files:**
- Create: `evals/trigger-cases.json`
- Create: `scripts/trigger_eval.py`
- Create: `tests/test_trigger_eval.py`
- Modify: `SKILL.md`
- Create: `reports/trigger-eval.json`

- [ ] **Step 1: Write routing cases before the runner**

Create at least 24 cases in `evals/trigger-cases.json` using this schema:

```json
{
  "cases": [
    {
      "id": "cn_create_public_readme",
      "text": "帮我给这个 GitHub 项目写一个完整 README，先给预览",
      "expected": true,
      "family": "create"
    },
    {
      "id": "cn_section_only",
      "text": "只优化这个仓库 README 的简介，其他章节不要动",
      "expected": true,
      "family": "incremental"
    },
    {
      "id": "cn_plain_markdown",
      "text": "把这份会议记录整理成 Markdown",
      "expected": false,
      "family": "ordinary_markdown"
    },
    {
      "id": "cn_end_to_end_skill",
      "text": "把这套流程创建、测试并发布成一个完整 Skill",
      "expected": false,
      "family": "meta_skill"
    }
  ]
}
```

Cover Chinese and English, create, audit, selective improvement, private repository, Description/Topics, ordinary Markdown, copywriting, syntax questions, code fixes, deployment debugging, and end-to-end Skill engineering.

- [ ] **Step 2: Write a failing runner test**

Create `tests/test_trigger_eval.py` that imports `scripts/trigger_eval.py`, asserts positive README cases trigger, negative Markdown and Meta Skill cases do not, and requires the full case file to pass with zero false positives and zero false negatives.

- [ ] **Step 3: Run the test and verify RED**

```bash
python3 -m unittest tests.test_trigger_eval -v
```

Expected: FAIL because `scripts/trigger_eval.py` does not exist.

- [ ] **Step 4: Implement the deterministic runner**

Implement `classify(text: str) -> bool`, `evaluate(cases: list[dict]) -> dict`, and a CLI accepting `--cases` and `--output`. Use action terms plus repository-presentation terms, explicit exclusions for ordinary Markdown and end-to-end Skill creation, and case-level reporting. The JSON result must include `total`, `passed`, `false_positive`, `false_negative`, and individual results without private file content.

- [ ] **Step 5: Run tests and generate the report**

```bash
python3 -m unittest tests.test_trigger_eval -v
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
```

Expected: all cases pass; report has zero false positives and false negatives.

- [ ] **Step 6: Commit trigger behavior**

```bash
git add SKILL.md evals/trigger-cases.json scripts/trigger_eval.py tests/test_trigger_eval.py reports/trigger-eval.json
git commit -m "test: define GitHub README trigger boundary"
```

### Task 4: Implement The Preview And Scope-Lock Output Contract

**Files:**
- Create: `references/project-type-playbook.md`
- Create: `references/readme-structure-playbook.md`
- Create: `references/evidence-and-claims.md`
- Create: `references/github-metadata.md`
- Create: `evals/output-cases.json`
- Create: `scripts/output_eval.py`
- Create: `tests/test_output_eval.py`
- Create: `reports/output-eval.json`
- Modify: `SKILL.md`

- [ ] **Step 1: Write recorded output fixtures first**

Create eight cases in `evals/output-cases.json`: frontend product, CLI section-only edit, library, API, Agent Skill, sparse repository, private internal repository, and large monorepo. Each case contains `prompt`, `project_context`, `recorded_output`, `required`, `forbidden`, and `evidence_type: recorded_fixture`.

The CLI scope-lock fixture must require:

```json
{
  "required": [
    "Scope lock: README introduction only",
    "R1 Rewrite",
    "Outside scope",
    "installation section"
  ],
  "forbidden": [
    "I updated the installation section",
    "all sections were improved"
  ]
}
```

The public Agent Skill fixture forbids `not installed locally`, absolute home paths, private backup rationale, and unsupported production claims. The large monorepo fixture requires staged inspection and a named evidence gap. The private repository fixture requires internal audience and unchanged secret controls.

- [ ] **Step 2: Write a failing output evaluator test**

Create `tests/test_output_eval.py` that imports `scripts/output_eval.py`, verifies required and forbidden assertions, rejects a deliberately broken fixture, and requires the complete output case set to pass.

- [ ] **Step 3: Run the test and verify RED**

```bash
python3 -m unittest tests.test_output_eval -v
```

Expected: FAIL because the output evaluator and references do not exist.

- [ ] **Step 4: Write the four focused references**

Implement the approved design without duplicating the full root workflow:

- `project-type-playbook.md`: staged inspection, project matrix, audience, visibility, and language.
- `readme-structure-playbook.md`: dynamic modules, numbered preview items, section-level before/proposed text, scope lock, conflict handling, and visual evidence.
- `evidence-and-claims.md`: fact ledger, public/private content, commands, versions, local and external links, stale docs, secrets, and evidence labels.
- `github-metadata.md`: Description, Topics, homepage, social preview, consistency, and separate external-write confirmation.

- [ ] **Step 5: Implement the recorded-fixture evaluator**

Implement `evaluate_case(case: dict) -> dict`, `evaluate_document(data: dict) -> dict`, and a CLI accepting `--cases` and `--output`. The report must label itself `recorded_fixture`, set `provider_backed` and `human_reviewed` to `false`, and never report a model win rate.

- [ ] **Step 6: Expand the root workflow minimally**

Update `SKILL.md` to require: staged repository inspection, fact ledger, project/audience/visibility classification, representative preview, stable change IDs, separate approvals, scope lock, smallest coherent edit, honest link status, verification, and optional publication only when requested. Cross-reference the four references instead of copying their detail.

- [ ] **Step 7: Run tests and generate the output report**

```bash
python3 -m unittest tests.test_output_eval -v
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
```

Expected: all recorded fixtures pass; report explicitly says it is not provider-backed or human-reviewed.

- [ ] **Step 8: Commit output behavior**

```bash
git add SKILL.md references evals/output-cases.json scripts/output_eval.py tests/test_output_eval.py reports/output-eval.json
git commit -m "feat: add preview and scope-lock README workflow"
```

### Task 5: Add Package Validation And Evidence Handoff

**Files:**
- Create: `scripts/validate_skill.py`
- Create: `reports/skill-ir.json`
- Create: `reports/creation-handoff.md`
- Modify: `tests/test_package_contract.py`
- Modify: `README.md`

- [ ] **Step 1: Extend the package test before validation exists**

Add tests requiring the four references, two eval files, three scripts, four generated reports, a Chinese-first README product page, at least four natural-language usage examples, prerequisites, outputs, evidence labels, troubleshooting, author, license, and no secret-like values or other-person identity.

- [ ] **Step 2: Run the package test and verify RED**

```bash
python3 -m unittest tests.test_package_contract -v
```

Expected: FAIL because validation and evidence files are incomplete.

- [ ] **Step 3: Implement `validate_skill.py`**

The validator must check:

- valid root frontmatter and one discoverable `SKILL.md`;
- identity consistency across SKILL, manifest, interface, README, and reports;
- required Production files;
- trigger and output reports are successful and use honest evidence labels;
- public files exclude secrets, private absolute paths, owner-local state, and placeholder text;
- README includes value, preview-first usage, natural examples, prerequisites, output description, evidence boundary, troubleshooting, author, and license.

The CLI prints JSON with `ok`, `failures`, and `warnings`, and exits nonzero on failures.

- [ ] **Step 4: Write Skill IR and creation handoff**

`reports/skill-ir.json` must define identity, intent, inputs, outputs, exclusions, permissions, evidence types, target platforms, and current `missing_evidence`.

`reports/creation-handoff.md` must contain:

```markdown
# Creation Handoff
## Package
## Reference Skills Studied
## Candidate-Specific Lessons
## Deliberate Rejections
## Original Contributions
## Validated Advantages
## Design Advantages
## Hypotheses
## Missing Evidence
```

Do not claim provider-backed improvement, human preference, installation, publication, or universal README quality.

- [ ] **Step 5: Finish the public README**

Describe the problem, preview-first behavior, dynamic project handling, installation command as future public usage only if publication later occurs, natural-language examples, outputs, permissions, evidence status, local validation commands, troubleshooting, author, and MIT license. Until publication, label installation and GitHub discovery as `not yet verified` rather than presenting a live command as proven.

- [ ] **Step 6: Run validation and tests**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skill.py .
```

Expected: all tests pass; validator returns `ok: true` with zero warnings.

- [ ] **Step 7: Commit package evidence**

```bash
git add README.md scripts/validate_skill.py tests/test_package_contract.py reports/skill-ir.json reports/creation-handoff.md
git commit -m "test: validate Kang GitHub README package"
```

### Task 6: Run Full Regression And Prepare A Local Handoff

**Files:**
- Modify: generated reports only if rerun changes them

- [ ] **Step 1: Run every regression command**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
python3 scripts/validate_skill.py .
git diff --check
```

Expected: all tests and cases pass, validation has zero failures and zero warnings, and `git diff --check` is clean.

- [ ] **Step 2: Scan public files for forbidden information**

```bash
rg -n -i "api[_ -]?key\\s*[:=]|token\\s*[:=]|cookie\\s*[:=]|/Users/|not installed locally|kang-owned backup|TODO|TBD" \
  SKILL.md README.md agents references evals reports scripts tests
```

Expected: no secret values, private absolute paths, owner-local installation state, backup positioning, or placeholders. Variable names used in safety examples are acceptable only when they do not contain values.

- [ ] **Step 3: Verify action boundaries**

Confirm no files exist under `~/.codex/skills/kang-github-readme` or `~/.agents/skills/kang-github-readme`, no GitHub remote has been added, and no publication claim appears in README or reports.

- [ ] **Step 4: Commit generated evidence if changed**

```bash
git add reports/trigger-eval.json reports/output-eval.json
git commit -m "test: record Kang GitHub README verification"
```

Skip the commit if generated reports are unchanged.

- [ ] **Step 5: Present the local handoff**

Report the package path, test totals, trigger totals, recorded output fixture totals, validator result, current evidence limitations, and the explicit fact that installation and GitHub publication were not performed.
