# External-skill comparison — 26 October 2026

This directory retains the synthetic inputs, outputs, source identities, and judgments from a local comparison. It is an audit record, not a scientific ranking of writing tools.

## Conditions

Five external skills, local Humanizer **1.1.0**, and a no-skill control received fourteen requests each. The final set contains 98 outputs. Each condition used an inherited Codex agent configuration in its own generation context; requests were grouped rather than isolated into fourteen sessions. Exact model identifiers, durations, and token counts were not exposed.

The generator read its assigned skill and relevant references, then the request and source text. It did not receive the expected outcomes. User constraints took precedence over conflicting skill defaults. External code execution, detector services, unrelated file edits, and active installation changes were outside the permitted tasks.

Separate LLM reviewers received anonymous labels shuffled for each case. They compared meaning with the source before assessing clarity, genre fit, proportionality, and output compliance. The label map was decoded after grading. Labels reduce some identity bias but cannot prevent a reviewer from recognizing a distinctive style or sharing the generator's biases.

## Observed fidelity judgments

| Condition | No issue recorded | Minor flags | Material flags |
| --- | ---: | ---: | ---: |
| Academic Humanizer | 14/14 | 0 | 0 |
| Hannsxpeter | 14/14 | 0 | 0 |
| Local Humanizer 1.1.0 | 13/14 | 1 | 0 |
| Milock | 12/14 | 2 | 0 |
| No skill | 12/14 | 2 | 0 |
| Blader | 11/14 | 3 | 0 |
| Stop Slop | 5/14 | 5 | 4 |

These are reviewer outcomes for one small convenience sample. They are not human-authorship percentages, estimated real-world error rates, or statistical superiority. Severity was not calibrated identically between reviewers: actor-attribution changes were rated minor in some cases and material in others. Read the actual issue descriptions. Tied preferences overlap; they are not individual wins.

The principal differences concerned introduced operators, the scope of absent evidence, and one new logical connector in local 1.1.0. All conditions retained the already good Norwegian passage unchanged and preserved the technical vocabulary in its light-copyedit case. All preserved the exact protected strings in the corrected math/code/quote case. The deeper technical discussion and the conclusion drafted from incomplete measurements were also completed successfully across conditions.

## Corrections and added cases

E07 and E08 initially contained literal backslash-n sequences instead of actual paragraph breaks. Their original inputs and outputs remain in [superseded-fixtures](superseded-fixtures/README.md). Both cases were rerun for every condition with repaired formatting. Only those repaired outputs enter the final totals.

E11–E14 were added after some initial outputs had been inspected. They test a minimal brief, deeper organization, matching a writing sample, and drafting from incomplete measurements. They are a declared post-initial stress set, not untouched held-out data.

A reviewer incorrectly penalized `krets` as invalid Nynorsk. The form is accepted by [Nynorskordboka](https://ordbokene.no/nob/nn/krets). The original and corrected reviews are both retained in `judgments/`; actor-attribution judgments were kept separate from that correction.

## Read the artifacts

- [Cases and expectations](cases.json): fourteen sources and requests with the grading criteria.
- [Generator inputs](inputs.json): request/source pairs without expectations.
- `outputs/`: seven condition files containing `{id, output}` entries.
- [Decoded results](results.json): every judgment with its condition identity.
- [Summary](summary.json): aggregates of those judgments.
- [Label map](label-map.json): the case-specific anonymous identities used by reviewers.
- [Literal checks](literal-checks.json): an automatic screen, not semantic verification.
- [Fixture revision](fixture-revision.json) and [execution limits](execution-limits.json): changes and unmeasured fields.
- [Source identities](sources.json): repository commits, archive hashes, and file hashes. External source text and repository snapshots are not redistributed here.

Raw reviewer comments and multilingual output excerpts remain as recorded. A passed expectation does not exclude every unanticipated issue; some extra attribution flags were recorded outside the predefined assertions.

## Repeat a comparison

Use these cases as regression examples, not fresh held-out material. For a new claim, choose additional realistic texts before inspecting new outputs. Retrieve each external skill at its recorded commit and check its license before use.

Give each condition the same `request` and `input` fields from inputs.json, its assigned skill only, and the same model/settings. Keep expectations, other outputs, identities, and prior scores away from the generator. Save the actual result as `{id, output}`. Run a no-skill control with the same request and source.

Shuffle treatment labels per case. Give a different reviewer the source, request, expectations, and anonymous outputs. Record specific evidence for missing qualifications, changed actors, invented results, and altered logical connections. Allow ties. Keep original outputs, corrections, failures, and the actual model/client information where available.

Several independent trials and human reviewers would be needed for stronger preference claims. Native Claude Code execution, automatic-trigger reliability, detector resistance, and watermark removal were not established by this comparison.

## Relationship to the current version

Local 1.1.0 generated the comparison column. The later 1.1.1 maintenance patch corrects teaching examples and clarifies preservation checks. Its separate [paired regression record](../results/2026-10-26-v1.1.1/README.md) shows five ties with the old version, not an observed improvement. Do not relabel the 98-output comparison as a test of 1.1.1.
