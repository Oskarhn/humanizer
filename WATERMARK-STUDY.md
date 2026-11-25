# What the watermark-tool comparison found

The 25 November 2026 study reviewed fourteen GitHub project candidates and attempted six configured writing methods on the same Bokmål and English technical texts. **It found no content-preserving detector-score improvement over the unchanged sources.** Humanizer 1.4.0 and earlier versions were retained; no new rewrite release was promoted from these results.

[Complete evidence archive](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-watermark-comparison-20261125.zip) · [Checksum](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-watermark-comparison-20261125.sha256)

## Methods, quality and scope

The executed methods were Humanizer 1.4.0, three Guillaume Meyer configurations, Shreyan's meaning-extraction/regeneration stages and krllagent's verified paraphrase workflow. Each received six synthetic technical fixtures, first with local Qwen2.5:3b and then in a separately labelled exploratory Qwen2.5:7b follow-up. These are local-model comparisons, not new native Codex-versus-Claude tests or rankings of each project's best possible configuration.

| Configuration | Both quality reviews approve, 3B / 6 | Both approve, 7B / 6 |
| --- | ---: | ---: |
| Humanizer 1.4.0 | 0 | 4 |
| Guillaume paraphrase | 0 | 0 |
| Guillaume structural | 0 | 1 |
| Guillaume backtranslation prompt | 4 | 5 |
| Shreyan direct stages | 0 | 0 |
| krllagent verified workflow | No accepted output | No accepted output |

The backtranslation prompt retained more cases, but five of its approvals were exact unchanged sources. Restraint is valid; it is not proof of removal. Other failures included missing claims, changed operations or evidence status, precision loss and language changes. The two blind LLM reviews are not human peer review or formal semantic proof.

There were 72 planned method cases, sixty returned outputs and twelve native audit/repair failures. Only fourteen results passed both source/readability checks. Their current NorBERT and Sapling scores were never lower than their unchanged sources. The archive contains all outputs and failures, including cases where Humanizer loses.

## Browser results and retained references

Thirty-five validated observations were collected through actual Chrome interfaces. Bokmål sources and approved outputs scored zero on ZeroGPT, but the sources already had that result. All approved English outputs scored 100 there. The exact old English references that had scored 0, 14.7 and 29 also now scored 100; the texts were not changed.

A mismatched ZeroGPT screenshot exposed an inadequate initial result-matching gate. Nineteen provisional records were excluded and replaced by eighteen observations checked against the separate classified-text region. Rejected evidence remains labelled in the archive. The current result does not establish why the historical ZeroGPT outcomes changed.

## Watermarks require a different test

Unicode cleanup and AI-classifier scores do not verify a statistical watermark. A real local SynthID reference pilot generated six marked and six control passages, but none passed its declared positive-control threshold and all failed source-preservation review. No removal success was counted. The failed runtime attempt, numerical fix and diagnostic results are included.

Production text-watermark verification requires access we did not have: [Anthropic's detector is in private preview](https://www.anthropic.com/news/claude-text-watermark), [Google says hosted Gemini text has no public self-service verifier](https://discuss.ai.google.dev/t/does-gemini-api-text-output-carry-synthid-watermarking-gemini-2-5-flash-lite-gemini-3-1-flash-lite-eu-ai-act-art-50-2/177241/9), and [OpenAI's textGrain verification has separate access requirements](https://openai.com/index/eu-text-provenance/). A normal login does not provide those keys.

The six writing fixtures were reused development material. Their limitation prompted a separate fresh set with new subjects, genres and lengths; it is not part of the completed figures above. Neither study should be described as a universal detector-bypass guarantee.
