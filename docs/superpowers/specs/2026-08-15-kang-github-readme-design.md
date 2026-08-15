# Kang GitHub README Design

Date: 2026-08-15
Status: approved for implementation planning
Owner: Kang

## Objective

Create a globally reusable Agent Skill that helps a user create or selectively improve the public presentation of a GitHub repository. The Skill must treat `README.md` as a project-specific product page without forcing one template, inventing evidence, exposing private state, or expanding a documentation request into an unauthorized GitHub write.

The Skill is intended for new repositories and iterative improvement of existing repositories across products, frontend applications, command-line tools, libraries, APIs, templates, Skills, research projects, and other repository types.

## Core Decisions

- The Skill name is `kang-github-readme`.
- It is a global reusable method, not a project-specific Skill.
- It defaults to preview-first behavior: analyze, propose, and wait for approval before editing.
- Existing README content is handled through selective improvement: preserve, rewrite, add, or remove.
- README edits, visual asset changes, GitHub metadata changes, and publication are separate authorization scopes.
- Language is selected dynamically from the repository audience and user intent.
- Structure, badges, visual assets, and section order are chosen by project type rather than fixed globally.
- The initial package targets Production maturity. GitHub publication and installation are separate later decisions.

## Trigger Boundary

Use the Skill when the user asks to create, rewrite, improve, audit, structure, or productize a GitHub repository README or public repository introduction. It also applies when the user explicitly asks to review GitHub Description, Topics, or homepage metadata as part of repository presentation.

Do not trigger it for:

- ordinary Markdown documents unrelated to a GitHub repository;
- isolated advertising copy or social posts;
- code fixes, deployment debugging, or product implementation;
- a narrow Markdown syntax question;
- one-off prose polishing without repository context;
- end-to-end Skill creation, packaging, evaluation, or release when a Meta Skill owns the larger workflow.

Routing precedence:

- README-only or repository-presentation work uses `kang-github-readme`.
- End-to-end Skill engineering uses the selected Meta Skill; README work remains one part of that larger workflow.
- Project-specific permanent rules belong in that repository's instructions, not in this global Skill.

## Default Workflow

### 1. Inspect The Repository

Read the repository structure, existing README, license, package metadata, executable commands, tests, deployment configuration, releases, and available visual assets. Do not infer product capabilities from the repository name alone.

### 2. Build A Fact Ledger

Classify candidate README claims as:

- `verified`: supported by current code, configuration, tests, rendered output, or a live authoritative source;
- `historical`: documented previously but not reverified in the current task;
- `to verify`: plausible but missing sufficient evidence;
- `do not publish`: secrets, credentials, private paths, owner-local state, private correspondence, unrelated personal information, or internal decision notes.

Public README content must answer reader questions. The author's local installation state, private backup purpose, local paths, and personal workflow notes are not public product facts.

### 3. Classify The Project And Audience

Determine the repository category, target reader, expected technical depth, primary user action, language, and strongest available evidence. Ask the user when classification would materially change the README and the repository does not provide enough evidence.

Language rules:

- Chinese-oriented personal or domestic projects default to Chinese-first.
- International open-source projects default to English-first.
- Full bilingual output is used only when requested or clearly justified by the audience.
- If the audience cannot be determined reliably, ask before drafting.

### 4. Produce A Preview

Before editing, show:

- proposed README information architecture;
- first-screen title, value proposition, and key introduction;
- a `preserve / rewrite / add / remove` decision list;
- recommended screenshots, demos, command output, diagrams, examples, and badges;
- proposed GitHub Description, Topics, and homepage link changes when relevant;
- facts or assets that still require user confirmation.

The preview must be representative text, not only section names.

### 5. Confirm Separate Scopes

Obtain separate approval for:

1. modifying `README.md` or related documentation files;
2. creating, changing, or uploading visual assets;
3. modifying GitHub Description, Topics, or homepage metadata;
4. committing, opening a Pull Request, merging, releasing, or deploying.

Approval for one scope must not be treated as approval for the others.

### 6. Edit And Verify

After approval, make the smallest coherent edit. Verify Markdown structure, links, commands, image paths, badges, public claims, secret exposure, readability, and repository consistency. For visual repositories, inspect the real rendered result when a suitable browser path exists.

### 7. Publish Only When Requested

GitHub publication is optional. When explicitly requested, use a feature branch and Pull Request workflow. Do not push directly to the default branch. Publication failures must leave a valid local deliverable and be reported as incomplete external state.

## Dynamic README Strategy

The Skill must not impose a universal section list. It selects from project-appropriate modules.

| Project type | Primary public evidence | Common useful modules |
|---|---|---|
| Product or web application | Real screenshots, live demo, verified workflow | Value, demo, main workflow, setup, status, limitations |
| Frontend or visual project | Stable screenshots, video, interaction evidence | Visual preview, design intent, run locally, browser support |
| CLI tool | Real command and terminal output | Install, quick command, options, examples, exit behavior |
| Library or SDK | Minimal working code and supported versions | Install, quick start, API surface, compatibility, migration |
| API or service | Request and response contract | Authentication boundary, endpoint example, errors, limits |
| Template or starter | Generated result and included stack | Preview, use template, structure, customization, update model |
| Agent Skill | Natural-language triggers and concrete outputs | Install, say-this examples, outputs, evidence, boundaries |
| Research project | Data, method, reproducibility evidence | Question, method, data, reproduce, limitations, citation |

The first screen should normally contain a literal project name, a reader-centered value statement, useful status badges, one quick-start path, and a concrete preview when the project is visual. These are defaults, not mandatory decorations.

## Visual Evidence Rules

- Products, applications, games, and visual frontend projects should use real screenshots, demonstrations, or videos when available.
- CLI tools, libraries, and APIs should favor real output, working examples, or diagrams over decorative images.
- Agent Skills should favor natural-language invocation examples, output artifacts, and validation evidence.
- Do not generate fake product screenshots or use unrelated cover art to make a repository appear complete.
- Do not upload, replace, or generate assets without separate approval.
- Clearly label prototypes, simulations, historical images, and unverified visuals.

## GitHub Metadata

The Skill may inspect and propose changes to:

- repository Description;
- Topics;
- homepage or demo URL;
- social preview recommendations when relevant.

Metadata must remain concise and consistent with the README. It must not contain private owner-local state, unsupported claims, or a positioning that contradicts the public project. Metadata edits always require separate confirmation because they are external GitHub writes.

## Package Architecture

```text
kang-github-readme/
├── SKILL.md
├── README.md
├── agents/interface.yaml
├── references/
│   ├── project-type-playbook.md
│   ├── readme-structure-playbook.md
│   ├── evidence-and-claims.md
│   └── github-metadata.md
├── evals/
│   ├── trigger-cases.json
│   └── output-cases.json
├── reports/
│   ├── prior-art-research.md
│   ├── trigger-eval.json
│   └── creation-handoff.md
└── tests/
```

`SKILL.md` remains a lean routing and decision document. Project-type judgment belongs in `references/`. Deterministic checks belong in tests or scripts only when they remove real repetition. Empty ceremonial directories are not created.

## Safety And Permission Rules

- Never publish API keys, tokens, cookies, `.env` content, authentication files, passwords, private correspondence, or private absolute paths.
- Secret inspection reports variable names, locations, and risks without revealing values.
- Do not expose the maintainer's local installation status or internal backup rationale as public product information.
- Do not invent installation commands, test results, deployment state, adoption, compatibility, or production readiness.
- Do not copy another project's branding, logo, biography, or claims.
- Do not upload assets, edit GitHub metadata, commit, merge, release, or deploy without the corresponding authorization.
- Existing user changes must be preserved unless the user explicitly approves their removal.

## Failure And Degradation Behavior

| Condition | Required behavior |
|---|---|
| Project type is ambiguous | Ask the user before choosing a materially different structure |
| Run or test evidence is absent | Mark it `to verify`; do not invent commands or success claims |
| External references are unavailable | Continue from repository facts and disclose the evidence gap |
| Existing README contains useful content | Preserve it selectively instead of replacing the whole file |
| README conflicts with code or configuration | Show the conflict and favor currently verifiable repository facts |
| Secret or private data is detected | Report location and risk without displaying the value |
| Images or links are missing | Include them in the preview gap list; do not fabricate replacements |
| GitHub authentication or permission fails | Stop at the local deliverable and report publication as incomplete |

## Evaluation Strategy

### Trigger Evaluation

Include positive cases for creating, auditing, selectively improving, and restructuring GitHub repository READMEs and public metadata. Include negative and near-neighbor cases for ordinary Markdown, advertising copy, code fixes, deployment debugging, and syntax-only questions.

### Output Evaluation

Evaluate representative repositories for:

- preview-before-edit compliance;
- correct project classification;
- dynamic language and structure;
- `preserve / rewrite / add / remove` reasoning;
- separation of verified, historical, and unverified claims;
- project-appropriate visual evidence;
- absence of owner-local state and private information;
- separate authorization for README, assets, metadata, and publication;
- consistency between README and GitHub metadata proposals.

The initial domain set includes a frontend product, CLI, library, API, Agent Skill, and sparse new repository.

### Package Validation

Validate one discoverable root `SKILL.md`, aligned interface metadata, trigger cases, output cases, public README quality, secret safety, and creation handoff evidence. Do not claim the Skill improves all README quality until human review or fair comparative evidence exists.

## Installation Strategy

The Skill is globally reusable and should be installed only once after it passes evaluation. It must not be copied into every project. One narrowly routed global Skill has low routing cost; overlapping or rarely used Skills create more context and selection risk.

The current design phase does not authorize installation or GitHub publication. Those decisions occur after implementation and verification.

## Follow-Up Skill Inventory

A separate future task will audit all installed Skills in read-only mode. It will classify them by recent use, routing overlap, maintenance, source trust, and replacement options. Deletion requires a named list and explicit user approval. This inventory is outside the implementation scope of `kang-github-readme`.

## Acceptance Criteria

The implementation is ready for user review when:

1. the Skill triggers for GitHub README and repository-presentation work without taking over ordinary Markdown or end-to-end Skill engineering;
2. it defaults to representative preview before file edits;
3. it dynamically adapts language, structure, visuals, and evidence to the repository;
4. it never treats owner-local state or internal notes as public product facts;
5. it separates README, asset, metadata, and publication authorization;
6. positive, negative, near-neighbor, and output cases pass;
7. package and secret validation pass without warnings;
8. the creation handoff distinguishes validated behavior, design advantages, hypotheses, and missing evidence;
9. no local installation or GitHub publication occurs without a later explicit request.
