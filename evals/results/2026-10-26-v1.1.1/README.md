# 1.1.1 comparison-driven maintenance

Date: 26 October 2026. This is a small local behavioral check and source-design review, not a scientific trial or detector experiment.

## Changes and reasons

- Correct the voice example: a possible useful suggestion stays a suggestion; lack of approval does not create an approval requirement.
- Make the operational-update example preserve the unknown maintenance actor directly, rather than introduce an actor through a separate assumption.
- Clarify the final check for newly invented causal/logical connections. This responds to an observed minor change in an English statistical paragraph.
- Add one concise Bokmål/Nynorsk technical example preserving simulation status, model limits and the lack of physical measurement.
- Clarify the heading for the originally supplied PDF set. Add M01–M05 behavioral cases. No scripts, dependencies, detection tools or provider settings changed.

## External comparison

An immutable 1.1.0 snapshot was compared with five external skills and a no-skill control. Fourteen synthetic cases per condition produced 98 final outputs. Independent LLM evaluators received shuffled anonymous labels per case and inspected meaning before style.

| Condition | Cases with no fidelity issue recorded |
|---|---:|
| Academic Humanizer | 14/14 |
| Hannsxpeter | 14/14 |
| Humanizer 1.1.0 | 13/14 |
| Milock | 12/14 |
| No skill | 12/14 |
| Blader | 11/14 |
| Stop Slop | 5/14 |

The Humanizer 1.1.0 issue was a connective that slightly altered the statistical reasoning. Other candidates' observed issues primarily concerned attribution or the distinction between absent available measurements and measurements not performed. These are observed reviewer judgments, not validated error rates. Most style judgments tied. Do not claim that this demonstrates superiority of 1.1.1; that version did not generate the 98-output comparison.

The comparison also examined conflicting teaching examples and default behavior. For this project's language and genre coverage, the decision was to maintain this skill with narrow corrections. No external prose or code was incorporated. Useful restraint, author-sample, claim-preservation and evidence principles were already present; concatenating pattern catalogs was not justified.

Reviewed primary source versions:

- [Blader](https://github.com/blader/humanizer/tree/8c307f367c91bd974002f10f2be2965d642c13df)
- [Academic](https://github.com/AIScientists-Dev/academic-humanizer/tree/94b88b23703bed7df507acae7d6d5876209a0cdf)
- [Hannsxpeter](https://github.com/hannsxpeter/humanizer/tree/e8f1248a7d4919689c1f942e356ed95b102d9f07)
- [Milock](https://github.com/milock/humanizer/tree/ec66c203c0400481819fda9cb17a6f1c7977c975)
- [Stop Slop](https://github.com/hardikpandya/stop-slop/tree/8da1f030185bdfe8471220585162991eaeb970e9)
- [Awesome Humanizer Skills catalog](https://github.com/zhuyansen/awesome-humanizer-skills/tree/67a50a8120d9f52f44f2c40c502483aa916ddb80)

## Paired patch regression

Five identical prompts were run in fresh old/new generation contexts. Four prompts were new targeted cases; M05 reused the observed comparison issue. Generator inputs omitted gold expectations. A separate evaluator received shuffled anonymous A/B outputs. All five pairs tied and all ten outputs passed. The older version also passed the repeated statistical case, illustrating sampling variability and the absence of measured improvement in this small retest.

- [Old outputs](outputs-v1.1.0.json)
- [New outputs](outputs-v1.1.1.json)
- [Independent review, decoded after grading](review.json)

## Limits

Both evaluation stages use inherited Codex agent settings, not verified native-Claude execution. Exact model identifiers, durations and token counts were not exposed. Cases were grouped in one context per condition, with one sample per request. Four comparison stress cases were added after inspecting some initial outputs. Two line-break fixtures were repaired and rerun for every condition; original inputs/outputs were retained in the local audit archive. One incorrect Nynorsk penalty was checked against [Nynorskordboka](https://ordbokene.no/nob/nn/krets), corrected, and retained separately in the local audit record. Judges may differ in severity and share generator biases. No independent human preference panel, model-transfer trial, detector service or watermark test was run.
