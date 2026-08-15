# Project Type Playbook

Read this reference when classifying the repository, audience, visibility, language, or inspection depth.

## Staged Inspection

1. Read the root file list, existing README, license, primary manifests, and entry documentation.
2. Locate tests, run commands, deployment configuration, releases, and visual assets suggested by the apparent project type.
3. Read deeper only to support a concrete public claim or resolve a conflict.
4. Stop and name the evidence gap when confidence would require a broad scan.

For a large repository, never default to a recursive full-file read. Build a root map, sample representative packages, and ask before materially expanding time or context use.

## Classification Matrix

| Type | Primary reader | Strong evidence | Often useful modules |
|---|---|---|---|
| Product or web app | User, evaluator, contributor | Real UI, verified workflow, live status | Value, preview, workflow, setup, limitations |
| Visual frontend | User, designer, developer | Stable screenshots, interaction evidence | Preview, design intent, local run, browser support |
| CLI | Operator, developer | Real command and terminal output | Install, quick command, options, examples, exit behavior |
| Library or SDK | Adopting developer | Minimal working code, supported versions | Install, quick start, API, compatibility, migration |
| API or service | Integrator, operator | Request/response contract, verified endpoint | Authentication boundary, example, errors, limits |
| Template or starter | Builder | Generated result, included stack | Preview, use, structure, customization, update model |
| Agent Skill | User, reviewer | Natural-language triggers, concrete outputs, evaluations | Invoke, outputs, evidence, permissions, exclusions |
| Research project | Researcher, reviewer | Data, method, reproducibility | Question, method, reproduce, limitations, citation |

Treat this as a selection guide, not a mandatory section list. When the repository does not support a confident classification and the choice would materially change the result, ask the user.

## Audience And Visibility

- For a public repository, optimize for a first-time external reader, adoption, contribution, and verifiable public evidence.
- For a private repository, optimize for authorized team onboarding, ownership, operational context, setup, support, and recovery paths.
- Private visibility never relaxes secret controls. Exclude credential values, private keys, raw environment files, and unnecessary personal data.
- If visibility is unknown and changes the information architecture, ask before drafting.

## Language

- Use Chinese-first for a Chinese-oriented personal or domestic audience.
- Use English-first for an international open-source audience.
- Use full bilingual content only when requested or clearly justified.
- Ask when audience evidence is insufficient and the language choice materially changes the deliverable.

## Inspection Cost

Do not optimize merely for the fewest model tokens. Prefer the lowest-cost path that preserves the same evidence quality and reader outcome. When two approaches produce equivalent results, choose the narrower inspection and smaller coherent edit.
