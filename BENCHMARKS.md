# Browser comparison: 31 October 2026

Humanizer 1.3.3 did not consistently outperform the other skills or meet the detector target. Academic Humanizer won a clear English Sapling comparison; Blader scored lower on the Norwegian Originality example. Our skill lowered one Isgen result, while every tested alternative remained at 100 on Pangram. The complete dataset includes these losses, unchanged texts, quality flags and failed attempts.

[Download the full report, texts and results](https://github.com/Oskarhn/humanizer/releases/download/v1.3.3/humanizer-comparison-20261031.zip) · [SHA-256 checksum](https://github.com/Oskarhn/humanizer/releases/download/v1.3.3/humanizer-comparison-20261031.sha256)

Open `REPORT.md` in the archive for the method and every case. Open `review.html` for the standalone review viewer. Run `python analyze.py` to recompute the tables from the exported records; it performs no new detection.

## What was compared

Four skills and a no-skill editing control received the same six synthetic technical texts: three Bokmål and three English. Each arm had two separate generation contexts, each containing all six cases, producing 60 outputs in ten contexts. The source texts had been used before; they are not fresh held-out material or human-authored controls.

| Condition | Frozen source |
| --- | --- |
| This Humanizer 1.3.3 | [`7f52a0453d`](https://github.com/Oskarhn/humanizer/tree/7f52a0453d5afe69a8ef61d285fdfacd02006584) |
| Blader 3.1.0 | [`0ef9fe5bc3`](https://github.com/blader/humanizer/tree/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0) |
| Academic Humanizer | [`94b88b2370`](https://github.com/AIScientists-Dev/academic-humanizer/tree/94b88b23703bed7df507acae7d6d5876209a0cdf) |
| Hannsxpeter | [`e8f1248a7d`](https://github.com/hannsxpeter/humanizer/tree/e8f1248a7d4919689c1f942e356ed95b102d9f07) |
| No-skill control | Same editing request, without a writing skill |

Every arm received the same preservation, readability, plain-text and length requirements. Titles or tab-separated tables were permitted when useful, but neither was forced. No output was repaired, rerolled or changed after scoring. Humanizer used ordinary editing with its report reference available, without detector feedback or local search. This is separate from the earlier [selected report-layout pilot](EVALUATION.md).

The agents inherited the same host model configuration. The exact sampled model identifier and sampling controls were not exposed. Native Claude generation was not tested, so these results do not establish identical behavior across clients or models.

## Primary results

These are native service scores, with lower numbers treated only as lower detector output. **Joint pass** means the output scored below 50 and passed the content/readability criterion. Means include quality-ineligible outputs; failures are not removed to improve an average. Each editing condition has six outputs per language.

| Condition | NorBERT, Bokmål mean | Joint pass | Sapling, English mean | Joint pass | ZeroGPT, English mean | Joint pass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Humanizer 1.3.3 | 99.73 | 0/6 | 96.58 | 0/6 | 35.50 | 4/6 |
| Blader | 99.94 | 0/6 | 88.82 | 0/6 | 42.78 | 4/6 |
| Academic Humanizer | 99.97 | 0/6 | 83.10 | 1/6 | 40.90 | 4/6 |
| Hannsxpeter | 99.96 | 0/6 | 99.53 | 0/6 | 28.30 | 6/6 |
| No-skill edit | 99.97 | 0/6 | 88.20 | 1/6 | 40.45 | 4/6 |

All Norwegian source and rewritten texts scored zero on ZeroGPT, so that panel did not distinguish the skills. All three English sources were also already below 50 there: 33, 14.7 and 37.2. Hannsxpeter retained every source exactly; its results demonstrate restraint, not a rewriting gain. Several other edits raised the controller source from 14.7 to above 50.

On the English confidence-interval text, second generation, **Academic Humanizer scored 0.1 on Sapling; ours scored 88.7**. Both were quality-eligible. An additional same-text check reproduced both scores. That check is reported separately and does not replace the primary observations. The no-skill versions scored 30.7 and 98.6, showing how much two generations can differ.

NorBERT was the author's official website, which runs FP16 inference in the browser. Sapling used the page's advertised WebMCP tool with its visible result checked; ZeroGPT used its actual web form. No local Python classifier generated these scores. Norwegian Sapling efficacy was not claimed; Norwegian ZeroGPT results remain exploratory because its language support is a broad vendor claim. Scores from different services are not averaged into a common percentage.

## Balanced secondary checks

Isgen and Originality received one source per language and the first output from every condition. Pangram received the same Norwegian case and first outputs, within ten approved free credits. Hannsxpeter's exact-source result could be reused. These small panels do not establish general rankings.

| Service / case | Source | Ours | Blader | Academic | Hannsxpeter | No skill |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Isgen / sampling, Bokmål | 46 | 0 | 46 | 100 | 46 | 45 |
| Isgen / diode, English | 100 | 100 | 100 | 100 | 100 | 100 |
| Originality 5.0 / sampling, Bokmål | 92 | 92 | 90 | 92 | 92 | 93 |
| Originality 5.0 / diode, English | 96 | 95 | 95 | 95 | 96 | 95 |
| Pangram 4.1 / sampling, Bokmål | 100 | 100 | 100 | 100 | 100 | 100 |

Our Isgen result improved numerically, but its source was already below the target. No Originality or Pangram variant crossed below 50. Pangram's current Norwegian validation remains uncertain; accepting an input is not proof of language-specific validation. No English Pangram comparison is claimed here.

## Content and readability

Two blinded LLM reviewers checked all outputs and six unchanged-source controls. Eligibility required both to approve factual completeness, language and register, with readability at least 4/5 and no lower than the source. All absolute readability ratings were 4/5, so this scale did not establish an improvement in readability. This was not human peer review or a proof of semantic equivalence.

| Condition | Quality-eligible outputs |
| --- | ---: |
| Humanizer 1.3.3 | 10/12 |
| Blader | 10/12 |
| Academic Humanizer | 11/12 |
| Hannsxpeter | 12/12, all unchanged |
| No-skill edit | 11/12 |

One reviewer flagged six controller texts for replacing an explicit addition rule with a less specific conjunction. The other reviewer approved them. Both judgments and their source spans remain in the archive; the six disputed cases are conservatively excluded from joint successes. They are not presented as unanimously established factual errors.

## Evidence and limits

The comparison has **162 scored condition rows: 136 new verified measurements and 26 explicit exact-text reuses**. Some new measurements repeat an already measured source, so neither figure is a count of distinct texts. Three additional successful observations are kept outside the main matrix: two same-text Sapling repeats and the delayed Originality check of an earlier report-layout output.

A stale ZeroGPT result was rejected because it displayed another fixture. One ordinary reload/retry recovered the correct result. An Originality failure and an error in the additional Sapling check were also retained before ordinary retries succeeded. Browser profiles, cookies and quotas were not reset, and no accounts, subscriptions or payments were created. Every complete input was checked against its frozen text.

The archive also contains the dated 30 October survey of 25 detector providers and the separate Sapling/Phrasly follow-up, including high scores, unsupported-language observations, locked previews and access limits. They are not pooled into this comparison. The [47-measurement NorBERT presentation pilot](EVALUATION.md) remains separately documented and downloadable with v1.3.3.

This small, reused synthetic set does not establish a universally best humanizer, detector accuracy, a false-positive rate or future success. The useful finding is narrower: ordinary edits can preserve readability and still score worse, while an unchanged source can be the best available choice. Use the skill for the writing task, and assess any requested detector result on its exact text and service.
