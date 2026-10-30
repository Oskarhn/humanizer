# How it works and what informed it

Humanizer is a reusable editing workflow, implemented as instructions and references that Codex or Claude Code can read. It is not a separate model. Its usefulness depends on the host model, the source material, and the writing brief.

## The editing process

1. **Establish what must survive.** Identify claims, figures, qualifications, source links, author voice, and required structure.
2. **Find the consequential problems.** Look for unclear reasoning, repeated paragraph jobs, empty claims, awkward syntax, or the wrong register.
3. **Revise to the requested depth.** A light edit can stay local; a deep rewrite can reorganize expression while preserving the argument and evidence.
4. **Compare with the source.** Check what changed in content, accountability, voice, readability, and delivery. Inspect new connectors as well as individual facts.

For example, “No temperature measurement is available” does not establish “The temperature was never measured.” A change from passive voice to “we measured” can add an operator the source did not identify. These are editorial distinctions the skill explicitly asks the model to protect, not guarantees that a model will never make an error.

## What the research contributes

Research on human and model writing helps identify questions worth asking. It does not supply a universal recipe for good prose.

- **Grammar and genre:** Reinhart and colleagues examine grammatical and rhetorical variation in human and model text. The editorial response is to inspect how a sentence fits its genre while retaining legitimate terminology and syntax. [Paper and author version](https://arxiv.org/abs/2410.16107).
- **Vocabulary in context:** Kobak and colleagues study excess vocabulary across biomedical abstracts. Population-level word shifts do not identify the author of one paragraph or justify banning the words. [Author version](https://arxiv.org/abs/2406.07016v5).
- **Norwegian clarity:** Språkrådet's guidance supports reader-appropriate structure, concrete language, and useful verbs. This informs the Norwegian reference; it is language guidance, not a detector-evasion experiment. [Writing advice](https://sprakradet.no/klarsprak/om-skriving/generelle-skriverad-bokmal/).

The earlier [research notes](https://github.com/Oskarhn/humanizer/blob/304f74ebe1c57e5b58bed384cb286e20206eb950/references/evidence.md) document the broader reading and access limits. The review includes research papers, provider documentation, and language guidance; those are different kinds of evidence. No cited external study validates this complete skill or establishes its Norwegian detector effect. The separate local test below measures a narrower result.

## Text-hygiene source review

On 29 October 2026, the MIT-licensed [watermarks-remover source](https://github.com/guillaumemeyer/watermarks-remover/tree/5c180932a00c793261177f79aee21db8929f3fe2) was reviewed for reusable ideas. Its useful distinction is between character cleanup, prose rewriting, and file provenance. The resulting [optional reference](references/text-hygiene.md) adds context-sensitive inspection and a final check of what actually changed.

The reviewed benchmark targets a configurable MarkLLM SynthID reimplementation. No textGrain-specific removal validation was found in the reviewed material, and no such experiment was run here. A same-configuration research detector is not proof about a production provider's detector. The upstream heuristic scores, vocabulary rules, and sentence-variation thresholds are not used to decide whether a text is human or worth editing. No upstream code, installer, hook, or service is bundled.

A small old/new regression used eight synthetic tasks, including exact character cleanup, multilingual preservation, protected code/quotes, and accurate reporting of unverified detector claims. Both versions passed all eight under a separate anonymous LLM review, with ties throughout. Four cleaned-file checks confirmed the expected character edits. This supports a narrow regression check; it does not demonstrate a detector improvement or native-Claude writing performance. Test artifacts remain outside the user package.

## What the package promises

The instructions prioritize meaning, author intent, genre, and natural expression. They do not impose a human persona, intentional mistakes, sentence-length quotas, or a universal punctuation blacklist. The supporting references supply practical editing guidance; character inspection and local detector measurement are loaded only when relevant.

The result should be assessed against the original and the brief. A natural-sounding revision does not certify authorship, establish that a detector will accept it, or verify the absence of a statistical watermark. See the [comparison](COMPARISON.md) for the actual local evaluation and its limitations.

## Detector research and the optional tool

The local [Norwegian classifier](https://huggingface.co/pegesund/norwegian-ai-detector/tree/0df563e67066e1eadd08eaceac80f1db4ed71f90) is fine-tuned from NorBERT-4-small. It compares learned contextual representations, rather than applying a public list of forbidden words. The helper preserves the author's preprocessing and class order, uses the pinned INT8 ONNX export, and checks artifact hashes. Its default 1,024-token limit follows the published inference example. Longer texts require an explicit, separately labelled full-coverage window protocol.

The user-supplied [Pangram 4 technical report](https://pangram-public.s3.us-east-1.amazonaws.com/pdf/pangram_4_technical_report.pdf) describes segment/token models, mixed-writing labels and training on humanized examples. The [4.1 model card](https://www.pangram.com/research/model-card/pangram-4-1) adds class probabilities and does not list Norwegian among its officially supported languages. [Copyleaks' V11 methodology](https://copyleaks.com/ai-detector/testing-methodology) documents vendor-run API evaluation, but does not expose reproducible model weights. These sources inform what to measure; they do not reveal a wording recipe that defeats either service.

Research methods such as [HIP](https://github.com/YixuanEvenXu/humanization-by-iterative-paraphrasing), [adversarial paraphrasing](https://github.com/chengez/Adversarial-Paraphrasing) and [HALO](https://arxiv.org/abs/2609.31876v1) use model adaptation, decoding tools or separate model runtimes. Their reported effects do not transfer merely by copying prompt instructions. This package implements its own smaller, bounded search over paragraph alternatives. It does not bundle those projects, train a paraphraser or reproduce token-level adversarial decoding.

## Local Norwegian evaluation

On 29 October 2026, four previously tested reports were used for development, followed by six new synthetic reports: three Bokmål and three Nynorsk, 197–209 words each. Their source claims and arithmetic were checked separately before rewriting. A normal 1.2.0 revision and three alternatives per source paragraph were generated in separate contexts. The detector and recipe were frozen before this fresh evaluation.

Search used beam width four, two passes, full-text scoring, numeric/length screens and a maximum of 256 actual inferences per document. It made 252 inference calls across the six documents, with 258 separately counted cache hits. Source/baseline scoring added twelve calls. Two blind LLM reviewers compared the top three texts and normal revision against each source. Selection required factual fidelity and readability/register of at least four out of five from both reviewers.

Two one-pass language/readability repairs were rescored and re-reviewed, adding two calls. The probe text illustrates why this matters: its lowest uncorrected score was 4.19, but an awkward numerical sentence failed the readability gate. After repair, its score was 72.80. The table uses the final text's score.

| Report | Normal 1.2.0 | Local search, after review |
| --- | ---: | ---: |
| LED current driver (Bokmål) | 18.59 | 1.82 |
| Sampling and quantization (Bokmål) | 100.00 | 22.94 |
| Probe response (Bokmål) | 99.85 | 72.80 |
| Rectifier and ripple (Nynorsk) | 99.99 | 73.64 |
| Encoder timing (Nynorsk) | 99.97 | 9.46 |
| Repeatability statistics (Nynorsk) | 100.00 | 99.57 |

Values are the model's two-class AI softmax scores multiplied by 100. They are not the fraction of words written by AI or calibrated authorship probabilities. The mean fell from 86.40 to 46.70; all six final scores were lower, and three crossed below 50. The planned stronger target required four of six below 50 and was **not met**. All selected texts passed both source-fidelity and prose-quality reviews after the disclosed repairs. Mean readability was 4.08/5 for the selected texts versus 5/5 for ordinary editing; mean register was 4.92 versus 5. These are model judgments, but they indicate a prose-quality cost. Prefer ordinary editing when fluent expression matters more than the measured detector response.

This supports a useful local measurement capability and an improvement in this small sample. It does not establish reliability across reports, generators, long documents or detector versions. The sources were synthetic; the reviews were LLM-based, with no independent human panel. Exact host model IDs and token usage were unavailable. Native Claude generation, Pangram/Copyleaks/Sapling transfer, detector accuracy, and watermark removal were not tested by this evaluation. Ordinary/English editing instructions and the five existing practical references were preserved.

The evaluation data, raw candidates, reviews, query logs and development failures are kept outside the installable package. They are not bundled in the release ZIP. The source and setup instructions are sufficient to inspect the method and run a new local test; the small test above should not be treated as an independently reproduced benchmark.

## Quality-first follow-up

Version 1.3.1 prioritizes Bokmål and English. Its ordinary editing instructions and English language guidance are unchanged. The optional workflow now considers complete source-ledger redrafts alongside paragraph combinations and explicitly compares readability before using detector scores to choose a text.

The three previously high-scoring report topics were revisited on 29 October 2026. The rectifier and statistics sources and their accepted comparison texts were translated from Nynorsk to Bokmål first, with a separate check of every fact, number, qualification and work-status distinction. These same-language comparisons must not be mixed with the older Nynorsk scores.

| Bokmål report | Accepted comparison | Selected result | Decision |
| --- | ---: | ---: | --- |
| Probe frequency response | 72.80 | 6.39 | Keep a source-faithful, equally readable alternative |
| Rectifier and ripple | 4.00 | 4.00 | Retain the translated comparison |
| Repeatability statistics | 98.10 | 98.10 | Retain the comparison after two unsuccessful rounds |

The 4.00 rectifier score was obtained by translating the earlier accepted text, before the new method ran. It is a language-change observation, not an editing improvement. Two blind LLM reviewers found no substantive source changes in the selected outputs and rated their readability equal to the accepted comparison. The English candidate set also contained two obligation shifts; those drafts were rejected.

Fresh validation used three independently authored synthetic Bokmål reports on DAC settling, sensor hysteresis and thermocouple compensation. Some low-scoring drafts received paired “equal readability” labels despite lower numerical clarity ratings and specific new awkwardness. The user required no readability sacrifice, so selection was tightened conservatively: both the paired judgment and each reviewer's clarity rating had to be no worse than the matched normal 1.3.0 revision. The earlier, less restrictive analysis was retained; no further generation or detector tuning followed this decision.

| Fresh report | Normal 1.3.0 | Quality-preserving result |
| --- | ---: | ---: |
| DAC settling | 100.00 | 100.00 |
| Sensor hysteresis | 99.99 | 99.99 |
| Thermocouple compensation | 99.98 | 99.92 |

All final readability ratings were 5/5 from both reviewers. Two normal revisions were retained. The remaining change was negligible for detection, and all three stayed above 50. This follow-up does **not** demonstrate a general detector advantage without a readability trade-off. The synthetic sources also had two nonblocking documentation/terminology imprecisions, recorded in their independent audit. A fresh candidate read the identical installed main instructions before the specified frozen copy; this duplicate exposure was recorded, and no outcomes or prior rewrites were exposed.

### Commercial-detector check

Texts were selected and frozen before seeing commercial results. Copyleaks completed seven distinct scans at sensitivity 2/3, with three identical-text reuses, before reporting its free scan limit. The complete Bokmål pairs were probe 0→0, rectifier 100→100 and statistics 100→100. An unchanged English pair was also 100→100. Two changed English after-texts scored 0 and 100, but their before-texts could not be measured after the quota, so no English improvement can be inferred from them. The served model build was not exposed.

Sapling completed five distinct English scans plus one identical-text reuse. The three pairs were 100→99.9, 100→100 and 100→99.9: all still flagged, with no practical improvement. Native editor paragraph rendering added line breaks; all other characters and every submitted own-text field were verified. Fresh responses and matching result text prevented stale scores from being mistaken for measurements. Sapling's [published supported-language list](https://sapling.ai/docs/api/detector/) excludes Norwegian; no Norwegian efficacy claim is made for it.

These are small, model-reviewed experiments, not human-reader studies, detector accuracy estimates or native-Claude generation tests. All raw texts, rejected candidates, reviews, query logs, quota failures and the stricter-quality correction remain outside the installable package. No extra account, payment, profile reset or quota bypass was used.

## Version and regression audit

The 1.3.2 audit found a missing continuity check: early good outputs had not been carried unchanged through the later website comparisons. Case IDs were reused across different studies, newer tests concentrated on difficult texts, detectors and languages differed, and a later quality gate rejected readability losses previously accepted at four out of five. These changes prevent treating the sequence of study averages as a release ranking.

The audit recovered the exact archived 1.2.0 English outputs and their source texts. Canonical UTF-8/LF inputs were checked against the original frozen hashes, submitted to the actual websites and checked against fresh responses. Three current ZeroGPT response values matched the rendered scores and the historical values exactly:

| Archived 1.2.0 output | ZeroGPT then | ZeroGPT retest | Sapling then | Sapling retest |
| --- | ---: | ---: | ---: | ---: |
| Observational training-method comparison | 39.9 | 39.9 | 100 | 100 |
| RC filter report | 28.1 | 28.1 | 100 | 100 |
| Firmware acquisition report | 46.5 | 46.5 | 100 | 100 |

The raw source ZeroGPT scores also repeated: 22.5, 33.3 and 34.6. Thus two highlighted low 1.2.0 outputs were worse than their sources. Different generations under that same version scored 83.0, 57.3 and 50.0. These observations demonstrate output variability and provider-specific results; they do not establish that later installed releases became generally worse or better.

The early 1.2.0 Bokmål power report really did receive a Copyleaks zero. It could not be rescanned during this audit because the existing free quota had been reached; no new Copyleaks result is claimed. The failed compact prototype and German/French pivot experiments were never installed. The four ordinary editing references and Codex metadata are unchanged from 1.1.3 through 1.3.2. Initial fidelity review also covered one assigned reviewer per output, whereas later studies used two per candidate; that stronger coverage must not be projected backward.

An exploratory file-upload reading differed from the text checks, but was not confirmed against its matching response. Subsequent response-matched file and text checks both returned 39.9. Those provisional readings are retained as unverified observations; they do not prove a backend, route or line-ending effect. The audit corrected an initial line-break hypothesis after exact input hashes showed equal visible text. Future comparisons must wait for the current result to settle and verify response/UI agreement where available.

### What 1.3.2 actually fixes

The old search helper accepted separate `source` and `baseline` texts but measured and retained only the baseline automatically. A source or earlier accepted draft could therefore be absent from the ranked report. The earlier tests largely used source-seeded packets or external selection, so this gap is a demonstrated implementation risk, not a proven explanation for their failed rewrites.

The fixed helper measures every distinct source, baseline and optional `accepted_reference` before search, deduplicates identical text, includes all their windows in its budget and returns them as `protected_references`. It fails before inference if the budget cannot cover those references. Their scores participate in the lowest-measured-hash calculation, while factual approval remains a separate host review.

Thirty deterministic code tests passed, including a saved failing reproduction against the old helper and retained original test fixtures. These tests validate reference preservation, budget accounting and unchanged input/output safeguards; they are not detector measurements. No model weights, preprocessing, ordinary language instructions or generation settings changed. Documentation now requires fixed same-provider comparisons and an explicit source/previous-draft fallback. No general detector-score improvement is claimed for this maintenance release.

## Bokmål report presentation in 1.3.3

The optional report mode makes source-preserving presentation explicit: retain a useful source, try an informative title when the document needs one, and reorganize comparable values into a labelled table only when it helps the reader. Essential method definitions remain in the body. Calculations, evidence status and limitations keep their original meaning.

The [report pilot](EVALUATION.md) records 47 actual NorBERT website measurements, matched source reviews, text representations and a real PDF extraction check. Seven synthetic high-scoring sources had reviewed alternatives below 50 in plain text and the tested PDF pipeline. A title alone was sufficient in five cases, so the workflow retains that smaller option. One title-removal control lost a method definition and was rejected; the final filter report was clarified and measured again. The result is bounded evidence for this optional workflow, not a cross-detector guarantee or a general release ranking. The ordinary English editing references and local detector code are unchanged.
