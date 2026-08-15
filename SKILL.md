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

1. Inspect repository facts and the requested scope.
2. Classify the project, audience, visibility, language, and evidence.
3. Preview representative changes before editing.
4. Lock the approved scope.
5. Edit only approved content and verify the result.
6. Treat GitHub publication as a separate optional action.

## Preview Contract

Show the proposed structure, key copy, evidence gaps, and numbered `preserve / rewrite / add / remove` items before changing files.

## Scope Lock

Approval for one item or section does not authorize changes outside it. Surface contradictions as separate proposals instead of silently expanding scope.

## Permission Boundary

README edits, asset changes, GitHub metadata changes, and Git publication are separate authorization scopes.

## Verification

Verify repository facts, Markdown structure, commands, links, image paths, public claims, and secret exposure in proportion to the project and requested scope.

## Output Contract

Return a preview, an approved scope summary, the changed files, verification evidence, and unresolved gaps. Never claim publication, installation, provider evaluation, or human preference without evidence.
