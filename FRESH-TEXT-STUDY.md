# Testing different technical texts

The 25–26 November 2026 follow-up used eight new AI-authored texts: four Bokmål and four English, ranging from 106 to 346 words. Subjects included thermal modelling, deadlock, battery energy, lossless compression, amplifiers, cache latency, emissions accounting and binary search. Sources were frozen before rewriting or detector checks.

**Three retained Bokmål revisions scored below 50 on NorBERT. English results remained high.** The gains came from Humanizer 1.4.0's existing deep mode and a later reader-oriented writing experiment. They do not establish a new universally better version. Humanizer remains at 1.4.0, and earlier versions and results are preserved.

[Complete evidence archive](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-fresh-variety-20261125-26.zip) · [Checksum](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-fresh-variety-20261125-26.sha256)

## What changed the scores

| Bokmål subject | Original NorBERT | Existing deep mode | Later reader-oriented rewrite |
| --- | ---: | ---: | ---: |
| Thermal estimate | 100 | 0.22 | Not run |
| Deadlock | 100 | 100 | 100 |
| Battery energy | 99.98 | 10.11 | Not run |
| Lossless compression | 99.98 | 99.97 | 23.98 |

The three low outcomes were repeated with the exact same text. Both independent blind LLM reviews approved their technical content, language and readability. ZeroGPT scored all three zero; the thermal source had scored 26.1 there, while the other two sources already scored zero.

Deep mode rebuilt the explanations around their calculations and limits. The later compression rewrite connected byte preservation to the counting argument. A similar reader-oriented rewrite did not help the deadlock case. These observations support a limited practical conclusion: useful reorganization can change a score, but the same instruction does not work across topics or detectors. They do not identify the detector's internal cause.

The reader-oriented follow-up was selected after the primary scores were seen. Combining its best result with the earlier deep-mode results is a post-hoc shortlist, not an independently tested method or a general three-in-four success rate. Longer rewrites, headings and tables may also contribute; their individual effects were not isolated.

For English, the originals scored 93.9–98.2 on Sapling and 100 on ZeroGPT. No qualified revision reached below 50 on either service. Small changes in Sapling's displayed score do not establish a useful improvement. One local deep rewrite received a Sapling service error and has no score.

## Methods and preservation

The primary comparison separated two backends:

- **Codex agent contexts:** the unchanged skill in standard and deep modes, eight sources each. All sixteen revisions passed both reviews; two were exact unchanged texts. Each mode used one context for all eight cases. The host model and sampling settings were not exposed, and native Claude generation was not tested.
- **Pinned local Qwen2.5:7b:** forty method cases, covering Humanizer's two modes and language-appropriate configurations from Guillaume Meyer, Shreyan and krllagent. Thirty-six returned text; sixteen passed both reviews, including five exact unchanged sources. Four native audit/repair workflows failed. None produced a qualified below-50 outcome on NorBERT or Sapling.

Six reader-oriented revisions were a separate exploratory Codex follow-up; all passed both reviews. A different learned rewriter, the cached HIP 1.7B adapter, returned four English outputs. All four failed both fidelity and readability reviews, so none was submitted to a web detector. Their raw outputs and concrete errors remain in the archive.

Reviews checked claims in both directions, including values, units, conditions, uncertainty and the distinction between a calculation and a physical measurement. Equivalent numeric formatting was allowed when meaning and stated precision were unchanged. These are fallible LLM reviews, not human peer review or formal proof. The earlier study's stricter outcomes have not been regraded.

## Evidence and limits

There were **82 validated browser observations**, including five repeated NorBERT checks. Sources, exact unchanged outputs and repeats are identified separately. The archive includes all 62 returned revisions, four method failures, both reviews for every revision, full tables, raw generation records, service errors, inspected screenshots and a review viewer. Rejected results are retained.

Measurements used the normal Chrome interfaces for [NorBERT](https://pegesund.github.io/norsk-ai-detektor/), [Sapling](https://sapling.ai/ai-content-detector) and [ZeroGPT](https://www.zerogpt.com/). NorBERT performs inference inside its website. Every eligible Bokmål input fit its declared token limit. Sapling's full-text coverage was checked. ZeroGPT's classified-text region and editor had to match independently in two reads. Scores from different services are not interchangeable.

These are development comparisons on synthetic texts. They do not measure false positives on verified human writing, performance on private reports or removal of production SynthID/textGrain watermarks. The [earlier watermark-tool study](WATERMARK-STUDY.md) documents the separate GitHub review, failed reference-watermark pilot and production-verifier access limits.
