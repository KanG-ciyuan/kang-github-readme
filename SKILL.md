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

Create or selectively improve repository-specific GitHub README content and related public presentation. Treat the README as a reader-facing project page, not a fixed template or a dump of internal instructions.

## Routing Boundary

Use this Skill for README-only and repository-presentation work, including an Agent Skill repository when the requested scope is only its README. Do not take over ordinary Markdown editing, product implementation, deployment debugging, advertising copy, or end-to-end Skill engineering. Route complete Skill research, creation, evaluation, packaging, installation, governance, or publication to the applicable Meta Skill.

## Default Workflow

1. Inspect the repository in bounded stages. Read [project-type-playbook.md](references/project-type-playbook.md) when choosing inspection depth, project type, audience, visibility, or language.
2. Build a `verified / historical / to verify / do not publish` fact ledger. Read [evidence-and-claims.md](references/evidence-and-claims.md) before publishing claims, commands, links, versions, or sensitive information.
3. Produce a representative preview with stable change IDs before editing. Read [readme-structure-playbook.md](references/readme-structure-playbook.md) for dynamic modules, incremental edits, scope lock, conflicts, and visual evidence.
4. Confirm README, asset, GitHub metadata, and publication scopes separately. Read [github-metadata.md](references/github-metadata.md) only when repository settings or external GitHub writes are relevant.
5. Convert accepted IDs into an explicit scope lock.
6. Make the smallest coherent approved edit, verify it, and report unresolved gaps.
7. Publish only when separately requested; never push directly to the default branch.

## Preview Contract

Show the classification, proposed structure, representative first-screen copy, evidence gaps, and stable numbered `preserve / rewrite / add / remove` items before changing files. Include section-level before and proposed text where existing content changes. A list of headings alone is not a preview.

## Scope Lock

Approval for one item or section does not authorize changes outside it. List unresolved items and sections as outside scope. Surface contradictions as separate proposals instead of silently expanding scope, and preserve item-level accept, revise, defer, or reject decisions across iterations.

## Permission Boundary

README edits, asset changes, GitHub metadata changes, and Git publication are separate authorization scopes.

## Verification

Verify repository facts, Markdown structure, commands, local links, image paths, public claims, stale versioned instructions, and secret exposure in proportion to the project and requested scope. Classify externally checked links honestly; if checking is unavailable, label them unverified. Inspect the rendered result when visual presentation matters and a suitable browser path exists.

## Output Contract

Return the representative preview, approved change IDs and scope lock, changed files, verification evidence, separate external-action status, and unresolved gaps. Never claim publication, installation, provider evaluation, human preference, or universal README improvement without evidence.
