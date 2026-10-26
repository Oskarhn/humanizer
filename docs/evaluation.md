# Evaluation record and limits

The repository separates three kinds of evidence: automated tool checks, model-generated editing trials, and source research. Passing one does not establish the others.

## Recorded editing trials

| Record | Observed result | Important limit |
| --- | --- | --- |
| [Initial 24 cases](../evals/results/2026-10-26/README.md) | 22 pass, one fail, one partial; two focused retests passed | The remaining 22 were not rerun after the focused changes |
| [1.1.0 provenance update](../evals/results/2026-10-26-v1.1.0/README.md) | Ten new provenance cases and four writing regressions passed | Reasoning about provenance was tested; actual watermark detection/removal was not |
| [External-skill comparison](../evals/comparison-2026-10-26/README.md) | 14 cases per condition, 98 final outputs | One grouped generation context per condition; four cases added after partial inspection |
| [1.1.1 paired regressions](../evals/results/2026-10-26-v1.1.1/README.md) | Both versions passed five cases; all five pairs tied | Four targeted new cases and one reused issue; no measured improvement over the old version |

These were synthetic LLM-generated and LLM-reviewed checks. Exact underlying model identifiers were not exposed by the orchestration tool. None is an independent human preference study or a population success-rate estimate.

The first run exposed a weakened evidence-versus-proof distinction and a dropped substantive assertion. Those failures remain in the record. The external comparison found a smaller logical-connection issue in local 1.1.0. The maintenance patch clarifies the source comparison and corrects teaching examples; it does not justify relabeling the old comparison as a 1.1.1 result.

## The external comparison

Academic Humanizer and Hannsxpeter had no recorded fidelity issues in their fourteen outputs. Local Humanizer 1.1.0 had one minor issue. Other conditions primarily introduced unsupported actors or altered the status of missing evidence. Many outputs tied, and several good source passages remained unchanged across all conditions.

Reviewers did not use severity labels identically. One Nynorsk penalty was checked against the language authority and corrected; the original review is retained. Inspect the actual issue descriptions before interpreting totals.

The choice to maintain this skill was based on its language coverage, technical preservation rules, and output contract, as well as the local trials. The trials do not establish that it is the best editor for every user or genre.

## Client and tool checks

Before repository preparation, 25 unit/package tests passed in Windows and WSL. The root repository adds release-tool checks; run the current suite for its current count rather than treating an old total as current CI evidence.

Filesystem installation and matching payload hashes were verified separately for Codex and Claude locations in the development environment. A native Claude Code smoke attempt stopped at an expired OAuth session before producing a writing result. This is not a successful Claude behavior test or an observed editorial failure.

The GitHub workflow files describe intended hosted checks. No hosted result is implied by their presence. Release tooling tests and extracted-package validation likewise do not show that a cloud/account skill upload has occurred.

## What remains untested

There is no recorded independent human-reader panel, repeated multi-model comparison, reliable automatic-trigger rate, detector-resistance trial, provider watermark test, or full Word/PDF layout evaluation. Longer real documents and newer models need their own checks.

The [research reference](../references/evidence.md) covers a targeted literature review, not a systematic review or a study validating this entire workflow. Its 22 entries include documentation and a language authority as well as papers. Eight distinct PDF records do not mean eight independent demonstrations of this skill's effectiveness.

## Run a new evaluation

Follow the [evaluation protocol](../evals/README.md). Hold out expectations from the generator, compare actual output with the source, allow ties, and retain failures. Predeclare the cases and decisions where practical. Record any post-inspection additions and fixture repairs.

For a change in editorial guidance, a fresh source-preservation check matters more than a test that searches for preferred wording. For a script change, use a concrete input/output or failure condition. Publish the exact scope of what ran.
