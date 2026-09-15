# Kang GitHub README

English | [简体中文](README.zh-CN.md)

[![Status: Experimental](https://img.shields.io/badge/status-experimental-orange.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`kang-github-readme` is an Agent Skill package that creates, audits, restructures, and selectively improves the README of a GitHub repository, together with the public presentation around it — Description, Topics, homepage, screenshots. It is preview-first and evidence-aware: it inspects the repository in bounded stages, classifies every material claim in a four-state fact ledger, shows real proposed text under stable change IDs, and then makes only the smallest coherent edit that was approved.

Four things never authorize each other: **README edits, visual assets, GitHub metadata, and Git publication.**

The package is Markdown + YAML + Python, not an application. Declared version `0.1.1`. MIT-licensed.

## Why This Exists

Most weak READMEs are not weak because they contain too little Markdown. They are weak because the reader's actual questions go unanswered — what is this, who is it for, does it run, where is the evidence, what do I do next — and because claims are restated as facts without anything behind them. The usual fixes make this worse in two predictable ways: a fixed template stamps the same section order onto every project, and an "improve the README" request quietly rewrites sections nobody asked about, sometimes pulling machine-local state, unverified capabilities, or internal notes into a public repository.

This Skill starts from repository facts and reader tasks instead, chooses the information architecture per project, and shows enough real proposed text — before touching a file — that the direction is reviewable.

The package states its own responsibility in one line (`SKILL.md:14`):

> Create or selectively improve repository-specific GitHub README content and related public presentation. Treat the README as a reader-facing project page, not a fixed template or a dump of internal instructions.

## Before And After

| The wrong way | With this Skill |
| --- | --- |
| Rewrite the whole README in one pass, then discover the direction was wrong | A representative preview of real proposed text first; you accept, revise, defer, or reject each item |
| "Improve the introduction" silently rewrites three other sections | Scope lock: approving one item does not authorize adjacent sections; unapproved sections are listed under `Outside scope` |
| A capability claim appears once and is repeated as fact | Every material claim carries a ledger state: `verified`, `historical`, `to verify`, or `do not publish` |
| README approval is read as permission to edit Topics or push a commit | Four separate authorization scopes; reading and proposing authorize nothing |
| Documented commands, versions, and links drift away from the code | Commands, versions, local links, and secret exposure are checked in proportion to scope, and unresolved gaps are reported |
| A screenshot is mocked up or borrowed to imply the product is finished | Missing assets go in the gap list; fabricating a screenshot is forbidden |

## How It Works

Seven ordered steps (`SKILL.md:20-28`):

1. Inspect the repository in bounded stages — root files, existing README, license, manifests, docs, tests, run commands, releases, assets — and stop to name an evidence gap rather than scanning everything.
2. Build a `verified / historical / to verify / do not publish` fact ledger.
3. Produce a representative preview with stable change IDs before editing anything.
4. Confirm README, asset, GitHub metadata, and publication scopes separately.
5. Convert the accepted IDs into an explicit scope lock.
6. Make the smallest coherent approved edit, verify it, and report unresolved gaps.
7. Publish only when separately requested; never push directly to the default branch.

### The label sets this package defines

They are separate on purpose, and they are not interchangeable.

| Set | Values | Used for |
| --- | --- | --- |
| Public-claim ledger | `verified` · `historical` · `to verify` · `do not publish` | Whether a sentence may be stated publicly, and with what scope |
| Link state | `verified` · `redirected` · `broken` · `unverified` | The result of an external link check — or the honest absence of one |
| Evaluation provenance | `recorded_fixture` · `provider_backed` · `human_reviewed` | What kind of evaluation produced a number |

The package has **no** label meaning "supported only by synthetic data": the nearest honest states are `to verify` on the claim axis and `recorded_fixture` on the evaluation axis.

## Core Capabilities

| Capability | What it does | Defined in |
| --- | --- | --- |
| Project-type-aware structure | An 8-row classification matrix (product app, visual frontend, CLI, library/SDK, API/service, template, Agent Skill, research) selects modules instead of forcing a template | [project-type-playbook.md](references/project-type-playbook.md) |
| Representative preview | A 7-part preview — classification, information architecture, first-screen copy, numbered change IDs, section-level before/proposed text, evidence gaps, separate metadata proposal | [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| Stable change IDs | `P1 Preserve` · `R1 Rewrite` · `A1 Add` · `D1 Remove`, each accept/revise/defer/reject-able and preserved across iterations | [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| Scope lock | Approved IDs become an explicit lock; every unapproved section is listed under `Outside scope`; contradictions elsewhere become new proposal IDs | `SKILL.md` · [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| Fact ledger | Four-state classification of public claims, with a stated public-use rule per state | [evidence-and-claims.md](references/evidence-and-claims.md) |
| Link classification | Local links and image paths checked deterministically; external links labelled `verified` / `redirected` / `broken` / `unverified` | [evidence-and-claims.md](references/evidence-and-claims.md) |
| GitHub metadata proposals | Description, Topics, homepage, and social-preview proposals, checked for contradiction against the README, and gated behind their own approval | [github-metadata.md](references/github-metadata.md) |
| Public / private reader modes | Public repositories optimize for first-time external readers; private repositories optimize for internal onboarding and recovery paths, with secret controls unchanged | [project-type-playbook.md](references/project-type-playbook.md) |
| Incremental mode | A section-only request edits that section and directly necessary repairs inside it, nothing else | [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| Routing boundary | End-to-end Skill research, creation, evaluation, packaging, installation, governance, and publication are routed to the applicable Meta Skill, not absorbed here | `SKILL.md` |

## Outputs And Artifacts

A run returns (`SKILL.md:46-48`, [skill-ir.json](reports/skill-ir.json)):

- the project/audience/visibility/language classification and the strongest available evidence;
- the fact ledger for the claims in scope;
- a representative preview with numbered `P1` / `R1` / `A1` / `D1` items;
- the approved scope lock and an explicit `Outside scope` list;
- the changed README content, the verification evidence, and the unresolved gaps;
- asset, GitHub-metadata, and publication proposals listed separately from README edits.

**Scope note.** No code in this package writes a README, generates a screenshot, or performs a GitHub API write. The three scripts in `scripts/` produce evaluation reports and validator JSON only; README text is authored by the agent under your approval.

## Evidence And Validation

Everything in this section was run from the repository root on Python 3.11.15 against commit `9a5ce32`.

### What was run

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -t tests -p 'test_*.py'
```

```text
.....................................................................
----------------------------------------------------------------------
Ran 18 tests in 0.027s

OK
[exit code: 0]
```

```bash
python3 scripts/validate_skill.py .
```

```json
{
  "ok": true,
  "failures": [],
  "warnings": []
}
```

Both measurements above are reproducible against the current revision. The documentation contract that previously required a Chinese-only `README.md` and a literal install-verified sentence has been repaired — see [Documentation contract repair](#documentation-contract-repair).

```bash
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
```

```json
{ "total": 28, "passed": 28, "false_positive": 0, "false_negative": 0 }
```

```bash
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
```

```json
{ "evidence_type": "recorded_fixture", "provider_backed": false, "human_reviewed": false,
  "total": 8, "passed": 8, "failed": 0 }
```

Both eval scripts were also run with their output redirected to a scratch file **outside** the repository and compared with `diff` against the committed reports: both results are **byte-identical** to [trigger-eval.json](reports/trigger-eval.json) and [output-eval.json](reports/output-eval.json). The committed numbers are reproducible from the shipped scripts and fixtures.

### What these numbers do not show

**The trigger fixtures pass; trigger routing is not validated.** The "classifier" in [trigger_eval.py](scripts/trigger_eval.py) is a keyword matcher: it returns true exactly when the text contains one of 6 fixed subject strings *and* one of 16 action strings, unless it contains one of 15 excluded patterns. The 28 fixtures (14 positive, 14 negative) are consistent with it. An out-of-fixture probe of 8 plausible real requests — run through this repository's own `classify()` — gives:

```text
False  README 太长了，帮我精简一下
False  帮我看看这个项目的 readme 有什么问题
False  优化一下这个仓库的介绍页
False  帮我把 GitHub 仓库首页的介绍改得更清楚
True   这个项目的 README 需要重写
True   Audit this repo's readme file
False  Add badges to the project README
False  帮我把项目的说明文档整理一下
```

Six of eight plausible README requests are routed away. The `false_negative: 0` figure does not generalize beyond the 28 written cases, and the written negatives contain none of the six subject strings, so they are rejected by the subject gate regardless of the excluded-pattern list — bypassing that list still yields 28/28.

**The output fixtures are `recorded_fixture`, not model evaluation.** [output_eval.py](scripts/output_eval.py) performs case-insensitive substring assertions (`required` present, `forbidden` absent) over saved outputs in [output-cases.json](evals/output-cases.json). `provider_backed: false` and `human_reviewed: false`. No model provider was called and no human reviewed anything. Passing saved examples shows that the recorded outputs satisfy their textual rules; it is not a quality or win-rate measurement.

**The tests are package contract tests, not a behavioural suite.** Ten of the eleven tests in [test_package_contract.py](tests/test_package_contract.py) are `is_file()` or string-presence assertions. Two of them assert that `manifest.json` *says* `verified` and that the README *contains* the matching sentence — a claim pinned in text is not evidence for the claim. Only `test_package_validator_returns_clean_result` executes another program. The other two test files genuinely execute roughly 150 lines of this repository's own keyword and substring code. **No test asserts anything about README quality, model output, or the installation claim.**

**There is no CI.** No `.github/` directory, no workflow, no pre-commit configuration, no declared dependency manifest. The suite runs only when a person runs it.

<details>
<summary>Two command forms that do <strong>not</strong> work</summary>

The repository has no `tests/__init__.py`, so the common discovery form fails:

```text
$ python3 -m unittest discover -s tests -t .
ImportError: Start directory is not importable: '<repository root>/tests'
[exit code: 1]
```

And the test modules import from the repository root, so running one directly fails:

```text
$ python3 tests/test_output_eval.py
ModuleNotFoundError: No module named 'scripts'
[exit code: 1]
```

The working form is the one used above (`-t tests` plus `PYTHONPATH=.`). `pytest tests/` also collects 18 tests in an environment where pytest happens to be installed, but pytest is not declared anywhere in this repository.

</details>

### Claims ledger

This document, classified with the package's own four states.

| Statement or content class | Label | Basis |
| --- | --- | --- |
| `kang-github-readme` is an Agent Skill package owned by Kang, declared version `0.1.1`, MIT-licensed | `verified` | [SKILL.md](SKILL.md), [manifest.json](manifest.json), [LICENSE](LICENSE) |
| It classifies public claims as `verified` / `historical` / `to verify` / `do not publish` | `verified` | `SKILL.md:23`, [evidence-and-claims.md](references/evidence-and-claims.md) |
| It previews numbered `P1` / `R1` / `A1` / `D1` items before editing | `verified` | `SKILL.md:32`, [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| Approving one item does not authorize adjacent sections | `verified` | `SKILL.md:34-36`, [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| README edits, assets, GitHub metadata, and publication are four separate authorization scopes | `verified` | `SKILL.md:40`, [github-metadata.md](references/github-metadata.md), [interface.yaml](agents/interface.yaml) |
| The 18 tests, the validator, and both fixture evals produce the results shown above | `verified` | the commands in this section |
| The README is a Chinese-first document | `historical` | true of the previous revision of this file; this revision is English-canonical with [README.zh-CN.md](README.zh-CN.md) |
| Version `0.1.0` was published as a release | `historical` | commit `6e2f7d5` (`release: publish kang-github-readme v0.1.0`); the current tree declares `0.1.1` |
| A Codex global installation of this package happened on 2026-08-15 | `to verify` | self-declared in [manifest.json](manifest.json) and [creation-handoff.md](reports/creation-handoff.md); no transcript, log, or test in this repository records it |
| The trigger fixtures demonstrate correct request routing | `to verify` | the fixtures pass, but 6 of 8 out-of-fixture requests are mis-routed |
| Model-quality, provider-backed, or human-preference performance | not claimed | `provider_backed: false`, `human_reviewed: false` in [output-eval.json](reports/output-eval.json) |
| Author-local installation state, home-directory paths, authentication files, correspondence, personal workflow notes | `do not publish` | [evidence-and-claims.md](references/evidence-and-claims.md); the banned-phrase list in [validate_skill.py](scripts/validate_skill.py) |
| Internal decision notes and agent-workflow planning documents | `do not publish` | [evidence-and-claims.md](references/evidence-and-claims.md) — see [Repository Notes](#repository-notes) |

### Known gaps

These are `to verify`, and they are the package's own gap list as well ([skill-ir.json](reports/skill-ir.json) → `missing_evidence`):

- **Installation.** `manifest.json` declares `installation.status: verified` with method `codex-skill-installer` and `verified_on: 2026-08-15`. Nothing in this repository reproduces that; the guard test only asserts that the sentence exists in the README. Treat the install as unverified. This package ships no installer and documents none.
- **Provider-backed evaluation, human review, blind preference study, win rates, superiority over other README skills.** None was run, and none is claimed.
- **`npx` discovery and installation.** Not verified, not documented, not claimed.
- **External links.** This repository's own URL returned HTTP 200 when checked. `NOT_TESTABLE` for the sibling repository links below: repeated checks timed out from the authoring environment, so they remain `unverified` rather than `verified`.
- **GitHub Release.** None exists — see [Status](#status).
- **Ecosystem conformance.** This package is not fully conformant with the sibling package validator in `kang-meta-skill`, which reports `ok: false` for 4 required fields plus warnings, including a missing `evals/trigger_cases.json`. The cause is a real naming divergence: this package uses hyphenated fixture filenames (`evals/trigger-cases.json`, `evals/output-cases.json`) where its siblings use underscores. The files are referenced here by their real names.

### Corrections to the previous revision of this document

Two statements carried over from the earlier revision were downgraded:

| Previous statement | This revision |
| --- | --- |
| The bolded Chinese "installation verified" sentence, grouped under "currently verified" | Moved to `to verify`: declared in `manifest.json`, reproducible nowhere in the repository. That exact sentence no longer appears anywhere in this package |
| "28 个确定性触发案例" — listed under "currently verified" | Restated as *the 28 fixtures pass*, with the keyword-matcher internals and the 6-of-8 out-of-fixture result disclosed |

This list documents corrections to this file. It is not evidence that the Skill performs well: no provider-backed or human evaluation of the Skill has been run.

### Documentation contract repair

An earlier revision of this document was English-canonical while the package's own
contract still required a Chinese-only `README.md`. That broke three assertions:

- `tests/test_package_contract.py::test_readme_is_a_chinese_first_product_page` required nine literal Chinese headings and at least four `- “` lines **in `README.md`**.
- `tests/test_package_contract.py::test_readme_records_verified_public_state` required a literal Chinese sentence claiming the installation was verified, in `README.md` — a claim this repository cannot evidence.
- `scripts/validate_skill.py` enforced both, so `test_package_validator_returns_clean_result` failed with it.

Two things were wrong with that contract, and only one of them was about language:

1. It pinned the language of a specific file instead of asserting the documentation invariant.
2. **It required an unverified claim.** The manifest declares `installation.status: verified`, but nothing in this package records an installation. A test that demands the claim can only be satisfied by publishing it.

The contract was therefore repaired rather than the claim restored:

| Repaired assertion | What it now enforces |
| --- | --- |
| `test_readme_is_a_bilingual_cross_linked_pair` | Both pages exist and cross-link; each carries its own reader-facing sections in its own language; the four shipped invocation examples are surfaced in both |
| `test_verified_install_claim_requires_shipped_evidence` | `manifest.json` declares the install `verified`; the package ships **no** install evidence; therefore both pages must carry the `to verify` label and must never restate the claim |
| `test_readme_states_the_unverified_npx_route` | The `npx` route is documented alongside its verification status |

`validate_skill.py` mirrors the same three rules, and requires both documentation-pair
members in `REQUIRED_FILES`.

**Current result, measured against this revision:** `Ran 18 tests` / `OK`, and
`validate_skill.py` returns `{"ok": true, "failures": [], "warnings": []}`. The
install claim remains labelled `to verify`; the unevidenced sentence appears nowhere in
the package.

## Status

- Declared version `0.1.1` — consistent across [manifest.json](manifest.json), [SKILL.md](SKILL.md), and [skill-ir.json](reports/skill-ir.json).
- `manifest.json` declares `maturity: production`, and [validate_skill.py](scripts/validate_skill.py) enforces that string. That is the package's declared maturity tier.
- Reader-facing status is **experimental**: **no git tag and no GitHub Release exist** for `0.1.1`. The only commit that calls itself a release (`6e2f7d5`) shipped `0.1.0`, there is no `CHANGELOG`, and no CI is configured.
- This README therefore carries no Release badge. A `/releases/latest` link would 404 today.

## Example

The package ships four natural-language invocation examples in [interface.yaml](agents/interface.yaml):

- “先读这个仓库，给我一份 README 结构和首屏文案预览”
- “只优化 README 简介，其他章节不要动”
- “审计 README 里的命令、链接和能力声明，先不修改”
- “分开检查 README 和 GitHub Description、Topics，先只给建议”

The same four are stored verbatim in [interface.yaml](agents/interface.yaml):

```yaml
examples:
  - "先读这个仓库，给我一份 README 结构和首屏文案预览"
  - "只优化 README 简介，其他章节不要动"
  - "审计 README 里的命令、链接和能力声明，先不修改"
  - "分开检查 README 和 GitHub Description、Topics，先只给建议"
```

A preview returned for such a request has seven parts ([readme-structure-playbook.md](references/readme-structure-playbook.md)): the classification, the proposed information architecture, the first-screen title and introduction, the numbered change items, section-level before/proposed text, the evidence gaps, and the metadata proposal kept separate from the README edits. No captured run is shipped in this repository — the preview shape is documented, not exhibited.

The one artifact you can reproduce exactly is the trigger report:

```bash
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
```

## Use It / Do Not Use It

| Use it for | Do not use it for |
| --- | --- |
| Creating the first README of a repository that has none | Ordinary Markdown editing — fixing a table, a nested list, or syntax |
| Auditing an existing README's commands, links, versions, and capability claims | Advertising, landing-page, or marketing copy |
| Restructuring a README end to end | Fixing code, failing tests, or deployment errors |
| Section-only improvement, such as the introduction and nothing else | Product implementation or deployment debugging |
| Keeping README, Description, Topics, and homepage consistent | End-to-end Skill research, creation, evaluation, packaging, installation, governance, or publication — routed to the applicable Meta Skill |
| A private repository whose README serves internal handoff and ownership | Treating a private repository as a reason to relax secret controls |

## Safety And Human Boundary

### Four separate authorization scopes

`SKILL.md:40`:

> README edits, asset changes, GitHub metadata changes, and Git publication are separate authorization scopes.

Reading visible metadata and proposing text authorize nothing at all. Beyond that:

1. README-related file edits — only after approval of the specific items.
2. Creating, replacing, generating, or uploading visual assets.
3. Changing GitHub Description, Topics, homepage, social preview, or any other repository setting.
4. Git publication: commit, Pull Request, merge, release, deploy, or default-branch push.

[github-metadata.md](references/github-metadata.md):

> README approval does not authorize metadata changes. Metadata approval does not authorize asset upload, commit, Pull Request, merge, release, deploy, or default-branch push.

> Authentication or permission failure must leave the local deliverable intact and be reported as incomplete external state.

The last line is the point of the whole boundary: an external action that fails stays failed and visible. It does not become a claim, and it does not cost you the work that was already produced locally. The default workflow never pushes directly to the default branch, and publication happens only when it is separately requested.

### Anti-fabrication and privacy

[evidence-and-claims.md](references/evidence-and-claims.md):

> Repository names and old prose are leads, not proof. Do not invent commands, test results, compatibility, deployment state, adoption, production readiness, performance, or endorsement.

> Do not publish author-local installation state, backup rationale, home-directory paths, private correspondence, authentication files, raw environment content, or personal workflow notes.

[readme-structure-playbook.md](references/readme-structure-playbook.md):

> Never fabricate a product screenshot or use unrelated art to imply product completeness.

[project-type-playbook.md](references/project-type-playbook.md) — private visibility never relaxes secret controls.

`SKILL.md:46-48` closes the loop: never claim publication, installation, provider evaluation, human preference, or universal README improvement without evidence.

### What this boundary is not

It is guidance for an agent, not an enforced runtime sandbox. Nothing here prevents an agent from ignoring it, and nothing in this repository can verify that an agent obeyed. The only mechanically enforced parts are the checks in [validate_skill.py](scripts/validate_skill.py) — a prohibited-phrase list, a secret-like-value pattern, an author-identity check, and a placeholder check — and those run only when someone runs them.

## Prerequisites

- A Python 3 interpreter. The standard library is enough — this package declares no third-party dependency, no `requirements.txt` and no `pyproject.toml`.
- A local clone. There is no installer and no published package.
- No network access is required to run the tests, the validator, or either fixture evaluation. All three are local and deterministic.

This section covers only what the package can verify about itself. The prerequisites for installing it into a specific agent runtime are **not** recorded in this repository — see [Evidence And Validation](#evidence-and-validation).

## Quick Start

There is no installer, no `requirements.txt`, no `pyproject.toml`, and no published package. Clone the repository and read [SKILL.md](SKILL.md); the reference documents it routes to are under `references/`. Installation into a specific agent runtime is deliberately not documented here, because this package ships no installer and no installation transcript.

```bash
git clone https://github.com/KanG-ciyuan/kang-github-readme.git
cd kang-github-readme
```

Verify the package as described in [Evidence And Validation](#evidence-and-validation). The commands need only a Python 3 interpreter and the standard library — no third-party dependency is declared or required:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -t tests -p 'test_*.py'
python3 scripts/validate_skill.py .
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
```

To confirm that the committed reports are reproducible without overwriting them, point `--output` at a scratch file outside the repository and `diff` the two files.

## Package Layout

<details>
<summary>25 tracked files</summary>

| Path | Role |
| --- | --- |
| [SKILL.md](SKILL.md) | The only Skill entrypoint: frontmatter identity plus responsibility, routing boundary, workflow, preview contract, scope lock, permission boundary, verification, and output contract |
| [manifest.json](manifest.json) | Name, version, owner, maturity, installation and publication declarations |
| [agents/interface.yaml](agents/interface.yaml) | Display name, default prompt, four natural-language examples, compatibility, and the four permission scopes |
| [references/project-type-playbook.md](references/project-type-playbook.md) | Staged inspection, the 8-row project-type matrix, audience and visibility, language choice |
| [references/readme-structure-playbook.md](references/readme-structure-playbook.md) | Dynamic modules, the 7-part representative preview, incremental mode and scope lock, visual evidence |
| [references/evidence-and-claims.md](references/evidence-and-claims.md) | The fact ledger, public/private content, commands and versions, link labels, evaluation labels |
| [references/github-metadata.md](references/github-metadata.md) | Description/Topics/homepage/social-preview proposal rules and the separate-write boundary |
| [evals/trigger-cases.json](evals/trigger-cases.json) | 28 routing fixtures — 14 positive, 14 negative |
| [evals/output-cases.json](evals/output-cases.json) | 8 `recorded_fixture` cases, each with `required[]` and `forbidden[]` assertions |
| [scripts/validate_skill.py](scripts/validate_skill.py) | Package, identity, privacy, version, and README-contract validator; prints JSON |
| [scripts/trigger_eval.py](scripts/trigger_eval.py) | Deterministic keyword classifier plus the fixture runner |
| [scripts/output_eval.py](scripts/output_eval.py) | Substring required/forbidden matcher over the recorded outputs |
| [tests/test_package_contract.py](tests/test_package_contract.py) | 11 package contract tests |
| [tests/test_trigger_eval.py](tests/test_trigger_eval.py) | 3 tests over the classifier and its fixture set |
| [tests/test_output_eval.py](tests/test_output_eval.py) | 3 tests over the substring matcher |
| [reports/trigger-eval.json](reports/trigger-eval.json) | Committed trigger result; reproducible byte-for-byte |
| [reports/output-eval.json](reports/output-eval.json) | Committed output result, self-labelled `recorded_fixture` |
| [reports/skill-ir.json](reports/skill-ir.json) | Machine-readable package IR, including the `missing_evidence` list |
| [reports/creation-handoff.md](reports/creation-handoff.md) | Build handoff: validated advantages, design advantages, hypotheses, missing evidence |
| [reports/prior-art-research.md](reports/prior-art-research.md) | Prior-art note, which states that the public catalog query never ran |
| [docs/superpowers/specs/2026-08-15-kang-github-readme-design.md](docs/superpowers/specs/2026-08-15-kang-github-readme-design.md) | Approved design specification (310 lines) |
| [docs/superpowers/plans/2026-08-15-kang-github-readme-implementation.md](docs/superpowers/plans/2026-08-15-kang-github-readme-implementation.md) | Implementation plan (506 lines) with 35 unchecked task items |
| [LICENSE](LICENSE) | MIT, Copyright (c) 2026 Kang |
| [.gitignore](.gitignore) | `.worktrees/`, `__pycache__/`, `*.pyc` |

</details>

<a id="repository-notes"></a>

### Repository Notes

<details>
<summary>Internal documents retained in a public repository — flagged, not hidden</summary>

`docs/superpowers/**` holds 816 lines of internal design and planning material, including a plan with 35 unchecked task items and embedded excerpts of the pre-`0.1.1` version. It is retained here, and it is **not** product documentation.

By this package's own rule, that content class is questionable public material. [evidence-and-claims.md](references/evidence-and-claims.md) defines `do not publish` as covering an "internal decision note", and this is one. Removing or relocating it requires an owner decision and is outside the scope of a README change, so it is flagged here instead. The plan also refers to a sub-skill that this package does not ship.

Two smaller notes on the same axis:

- The public repository carries an unmerged branch that would add a Release badge pointing at `/releases/latest`. Since no release exists, that badge would 404. This README deliberately omits it.
- Preview item IDs are described as "stable numbered items" in `SKILL.md` while the actual IDs are letter-prefixed (`P1` / `R1` / `A1` / `D1`). The IDs above follow the implementation.

</details>

## FAQ

**Will this package write my README for me?**
No. No code in this package writes a README, generates a screenshot, or performs a GitHub write. The three scripts in `scripts/` produce evaluation reports and validator JSON only; README text is authored by the agent under your approval.

**Why is there no GitHub Release?**
Because none was ever published. `0.1.1` has no git tag, and the only commit that calls itself a release (`6e2f7d5`) shipped `0.1.0`. This README therefore carries no Release badge.

**Is the installation verified?**
No. `manifest.json` declares `installation.status: verified`, but nothing in this repository — no transcript, log, or test — reproduces it. Under the package's own evidence rule that claim is labelled `to verify` on the reader-facing side.

**Why are the `evals/` filenames hyphenated?**
This package uses `evals/trigger-cases.json` and `evals/output-cases.json` where its siblings use underscores. That is a real naming divergence and one reason this package does not pass the sibling validator. The files are referenced by their real names and were not renamed.

**Do the tests prove README quality?**
No. They are package contract tests: file-existence and string-presence assertions. No test asserts anything about README quality, model output, or the installation claim.

**The trigger fixtures pass — does that mean routing is accurate?**
It does not follow. The classifier is a keyword matcher and the 28 fixtures are consistent with it; six of eight plausible out-of-fixture requests were routed elsewhere.

## Author

This package is maintained by **Kang**, who is also the copyright holder named in [LICENSE](LICENSE).

- GitHub: [KanG-ciyuan](https://github.com/KanG-ciyuan/)
- Repository: <https://github.com/KanG-ciyuan/kang-github-readme>

No installation transcript, evaluation transcript, or author contact detail beyond the repository link is shipped here. Personal email, home-directory paths, and other author-local state are deliberately not published, per this package's own `do not publish` rule.

---

## Part of the Kang Open-Source AI System

This project is one part of an evidence-driven system for enterprise AI transformation,
agent collaboration, and AI-native product delivery.

| Stage | Project | Role |
| --- | --- | --- |
| DISCOVER | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | Understand how the business actually works before automating it |
| DEFINE | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | Turn ambiguous requirements into an implementation-ready product contract |
| DEFINE | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | Review whether workflows are executable, accountable and recoverable |
| BUILD & COORDINATE | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | Role-based AI product workforce with explicit handoffs |
| BUILD & COORDINATE | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent collaboration and handoff protocol |
| BUILD & COORDINATE | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | Frontend quality standard for AI-built interfaces |
| VERIFY | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | Can users actually finish the work? |
| VERIFY | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | Independent acceptance of AI-built products |
| DELIVER | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | Evidence-aware README engineering |
| DELIVER | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | Evidence-aware presentation design |

**Cross-cutting infrastructure:** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill engineering, evaluation and release governance.

**Earlier work:** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules),
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps),
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent).

The stage map:

```text
DISCOVER
Enterprise AI Diagnostic Skills
        ↓
DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
DELIVER
Kang GitHub README
Kang PPT Skill
```

> This is an ecosystem map, not a strict runtime pipeline. The stages describe where
> each project sits in the work, not a mandatory execution order.

## License

Released under the [MIT License](LICENSE).
