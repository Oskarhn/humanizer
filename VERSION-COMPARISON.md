# Does 1.4.0 lower detector scores compared with 1.3.3?

The 4 November 2026 browser test found **no clear general improvement**. Version 1.4.0 had a limited English ZeroGPT gain, but a higher Norwegian NorBERT mean and a worse Norwegian Originality example. Both versions remained extremely high on Sapling. The new version also had one more quality exclusion.

[Full report, texts, scores and reviews](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-1.4.0-vs-1.3.3-20261104.zip) · [Checksum](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-1.4.0-vs-1.3.3-20261104.sha256)

## Same-source test

The two published versions received the same six synthetic technical texts used in the earlier comparison: three Bokmål and three English. Each version had two independent generation contexts, each containing all six cases, producing 24 outputs in four contexts. These are reused fixtures, not fresh held-out texts or human-authored controls.

The common prompt requested natural technical-school report editing, complete factual preservation, plain text, at most 1,850 characters and 110% of source word count. Titles and tables were permitted when useful, not forced. No text was repaired, rerolled or changed after scoring. Both versions were generated and measured again in this run; October's scores were not substituted for new observations.

This tests ordinary prose editing with the relevant references available. It does not test every optional mode or force the new file-audit helper into an otherwise clean text task. The earlier [selected report-layout pilot](EVALUATION.md) is separate. Agents inherited the same host model configuration; the exact sampled model and sampling controls were not exposed. Native Claude generation was not tested.

Same-case/attempt-index pairs are descriptive comparisons of independent generations, not shared-seed controlled trials.

## Main results

Each primary language panel has six outputs per version. Values are the provider's own mean AI score; lower is only lower on that service. **Joint pass** requires both a score below 50 and the content/readability criterion. Raw means include quality-ineligible outputs, which remain in the data.

| Detector / language | 1.3.3 mean | 1.4.0 mean | 1.3.3 joint pass | 1.4.0 joint pass |
| --- | ---: | ---: | ---: | ---: |
| NorBERT / Bokmål | 96.75 | 99.02 | 0/6 | 0/6 |
| Sapling / English | 99.93 | 99.97 | 0/6 | 0/6 |
| ZeroGPT / English | 39.48 | 33.40 | 3/6 | 4/6 |
| ZeroGPT / Bokmål | 0 | 0 | 6/6 | 6/6 |

NorBERT's matched pairs split into three lower and three higher new-version scores. One old-version statistical text scored 80.88 versus the new version's 99.93 and accounts for much of the mean difference. Neither version reached below 50. Sapling remained between 99.8 and 100; its small mean difference provides no useful target advantage.

The English ZeroGPT gain is narrower than the mean alone suggests. The diode attempts were **52.2 / 18.1 for 1.3.3** and **0 / 34.3 for 1.4.0**: one pairing improves and the other worsens. A post-hoc exact-text replay reproduced 52.2 and 0; it is kept outside the primary aggregates.

All three unedited English sources were already below 50 on ZeroGPT: 33, 14.7 and 37.2. Their mean, 28.30, was lower than either rewriting mean. Every Norwegian source also already scored zero. Retaining an acceptable source can therefore be better than rewriting it; passing those targets alone is not a skill-created gain.

## Originality subset

The preselected sampling and diode sources, plus the first generation from each version, were checked in the free guest interface with AI-only scanning and Originality 5.0. This is one case per language, not a full panel.

| Case | Source | 1.3.3 | 1.4.0 |
| --- | ---: | ---: | ---: |
| Sampling / Bokmål | 92 | 89 | 93 |
| Diode / English | 96 | 95 | 95 |

The new Norwegian score was higher, and English tied. No variant crossed below 50. One delayed browser wait was recovered by reading the completed matching result; it was not resubmitted or replaced with an old score. The panel used 15 free credits and created no account or payment.

## Content and readability

Two new blinded LLM reviewers checked every output and six unchanged-source controls, with version labels and scores withheld. Both had to approve fidelity, language and register; readability had to be at least 4/5 and no lower than the source, with neither paired judgment worse.

| Version | Quality-eligible outputs |
| --- | ---: |
| 1.3.3 | 11/12 |
| 1.4.0 | 10/12 |

Both reviewers rejected the old version's first controller output and both new-version controller outputs. They replaced the explicit addition of proportional and integral terms with a less specific conjunction. The one-step numbers survived, but the general operation was no longer stated. These three outputs remain in raw results and cannot count as joint successes. Individual readability ratings and disagreements are retained.

These are fallible LLM reviews, not human peer review or formal equivalence checks. The small difference in eligibility does not establish a general version-level quality ranking.

## Evidence and limits

The matrix contains **66 condition rows: 64 new verified measurements and two explicit exact-text reuses**. Two new-version confidence-interval outputs are identical; their Sapling and ZeroGPT scores were reused rather than counted as fresh scans. The two post-hoc replays are additional observations outside that matrix.

NorBERT ran on the author's actual website, using client-side FP16 inference. Sapling used its advertised page tool with the settled visible result checked; ZeroGPT and Originality used their actual web forms. Full input identities and native score fields were checked. No Python classifier supplied scores. All Norwegian inputs fit the site's context in a separate tokenizer-only check; loaded browser weight bytes were not captured.

Isgen was unavailable: the existing tab showed a network-error page, and the browser tool's URL policy blocked its error-page wrapper during inspection. It was not accessed through another profile or mechanism. No Isgen score or global site-health conclusion is claimed. The previous explicit Pangram credit budget had been used; this study contains no new Pangram comparison.

The archive contains every source/output, prompt, frozen version manifest, both reviews, all scores, the recovered wait event, replay records, analysis scripts and a single HTML review viewer. Its template loads external fonts and an optional spreadsheet library; the embedded JSON/CSV data and Python analysis can be read without those dependencies. Scores from different services are not pooled, and missing results are not treated as zero.

This test supports keeping the 1.4.0 audit features for their documented inspection purposes. It does **not** support choosing 1.4.0 as a reliably better detector-avoidance version. The writing instructions, installed copies and version tags were kept unchanged during the test.

## Follow-up: rebuilding from technical claims

A later bounded pilot on 4 November preserved the exact ZeroGPT successes and tried a different workflow: two independent writing contexts rebuilt six explanations from an atomic claim ledger without seeing source sentence frames. Eight of twelve drafts passed both new blind fidelity/readability reviews; four were excluded before scoring. These remained the same synthetic development sources, not held-out material.

| Eligible new drafts | Target score range | Below 50 on target | Below 50 on ZeroGPT |
| --- | ---: | ---: | ---: |
| Three Bokmål drafts / NorBERT | 99.85–99.99 | 0/3 | 3/3 |
| Five English drafts / Sapling | 99.9–100 | 0/5 | 4/5 |

The six retained references reproduced their ZeroGPT scores exactly: 0, 0, 0, 0, 14.7 and 29. Four of these references were unchanged sources, so their low scores were not created by rewriting. No new English draft beat its retained reference. The stable skill and successful exact texts were kept; no new writing release was promoted.

The exact Academic confidence-interval text that had scored 0.1 twice on Sapling on 31 October now scored **99.4 twice**, with an unchanged text hash. This does not establish the cause of the change, but it means that historical success did not reproduce in the current website checks. The earlier score cannot substantiate a current bypass claim.

The English HIP 1.7B pilot produced no draft: its watchdog ended the monitored launcher after 37 seconds for GPU memory pressure, and both recorded launcher/interpreter PIDs were absent in a later check. The remaining two runs were not attempted. Three historical PDF-extracted Bokmål report representations were retained but not scanned because a current review rejected the readability of their plain-text table serialization; the original rendered reports were not newly regraded. These unavailable arms are not scored failures or successes.

The follow-up contains 35 new website observations, including one exact-text repeat. Its matrix distinguishes 34 directly measured rows, eight same-hash reuses and 14 quality-gated `NOT_RUN` rows. NorBERT ran in the actual author website, Sapling through its advertised page tool with visible-result verification, and ZeroGPT through its form. No Python classifier supplied scores.

[Full follow-up, all drafts, exclusions, scores and reviews](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-source-rebuild-20261104.zip) · [Checksum](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-source-rebuild-20261104.sha256)

## Reproduction audit: Sapling and NorBERT

The subsequent 4 November audit found a documented service change: [Sapling's API documentation](https://sapling.ai/docs/api/detector/#november-2026-model-upgrades) records a 3 November default-model upgrade, from English `20260820` to `20261102`, including rescoring cached results. This is the strongest supported explanation for the historical 0.1-to-99.4 jump. The exact versions were not returned in our page-tool logs, so a pinned old/new-model causal comparison remains unperformed.

The exact Academic input still scored 99.4 through the advertised page tool, ordinary button and ordinary page reload. The old Humanizer comparator changed from 88.7 to 99.9 through both current methods. Complete text identities and score meanings were checked. Provider examples agreed between preset buttons and page-tool checks; they are interface controls, not independent accuracy evidence.

**All 47 archived NorBERT inputs reproduced their old displayed scores exactly**, including high sources, low reports, Markdown, tab-separated text, archived PDF extractions and heading/body controls. Three further checks after page reload also matched. The retained final tab-separated/PDF reports remained at 0.08, 3.76, 0.14, 0.05, 0.07, 0.04 and 0.05. Historical quality exclusions remain excluded; the audit did not rewrite reports or newly review PDF readability.

These exact retained reports differ from the newly generated prose in the failed follow-up. Their old results have not disappeared. Reproducing them does not establish that every new text generated with the skill will achieve the same response.

The audit contains 61 website observations: 50 NorBERT and eleven Sapling. The 25 retained ZeroGPT records covering 24 distinct texts remain byte-for-byte unchanged and were not rescanned. Writing instructions, installations and version tags were kept unchanged.

[Full reproduction audit and all scores](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-detector-reproduction-20261104.zip) · [Checksum](https://github.com/Oskarhn/humanizer/releases/download/v1.4.0/humanizer-detector-reproduction-20261104.sha256)
