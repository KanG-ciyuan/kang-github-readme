# Evidence And Claims

Read this reference when deciding what may be stated publicly, validating commands or links, or handling secrets and stale documentation.

## Fact Ledger

Classify every material claim:

| Status | Meaning | Public use |
|---|---|---|
| `verified` | Supported by current code, configuration, tests, rendered output, or an authoritative live source | State with the matching scope |
| `historical` | Previously documented but not reverified now | Label as historical or recheck |
| `to verify` | Plausible but missing sufficient evidence | Put in the gap list, not as fact |
| `do not publish` | Secret, private path, owner-local state, correspondence, unrelated personal data, or internal decision note | Exclude from public output |

Repository names and old prose are leads, not proof. Do not invent commands, test results, compatibility, deployment state, adoption, production readiness, performance, or endorsement.

## Public And Private Content

Public content must answer reader questions. Do not publish author-local installation state, backup rationale, home-directory paths, private correspondence, authentication files, raw environment content, or personal workflow notes.

For private repositories, include useful internal ownership and support context only when authorized. Secret controls remain unchanged. When a secret risk is found, report the variable name, location, and risk without exposing its value. Never move, replace, revoke, or delete credentials without explicit authorization.

## Commands, Versions, And Stale Content

- Verify commands against current manifests, scripts, help output, or a safe local run.
- Verify version claims against authoritative configuration.
- When README text conflicts with current code or configuration, show the conflict and favor current evidence.
- Flag stale versioned instructions as a separate proposal rather than silently preserving or changing them outside scope.

## Links And Assets

- Check local links and image paths deterministically.
- When network access exists, classify external links as `verified`, `redirected`, or `broken`.
- When external checking is unavailable, label the link `unverified`; never claim universal validation.
- Missing images or links belong in the preview gap list. Do not fabricate replacements.

## Evaluation Labels

Keep structural fixtures, model runs, and human judgments distinct:

- `recorded_fixture`: deterministic assertions over saved examples;
- `provider_backed`: a live model or provider evaluation actually ran;
- `human_reviewed`: a person evaluated the output under a stated method.

Never turn recorded fixtures into a model win rate, human preference score, or universal quality claim.
