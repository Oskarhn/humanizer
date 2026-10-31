# Bokmål technical-report pilot

This pilot tested source-preserving report presentation on the official [NorBERT website](https://pegesund.github.io/norsk-ai-detektor/) on 30 October 2026. It supports an optional workflow for this genre. It is not a general detector-bypass benchmark or proof that version numbers measure progressively lower detectability.

For the later ordinary-editing comparison against other skills and six actual detector websites, see [the 31 October benchmark](BENCHMARKS.md). Its different generations and workflow are reported separately; neither study replaces the other's exact-text results.

## What was compared

The set contained six previously used synthetic engineering texts and three newly authored synthetic fixtures. Seven high-scoring sources received one report alternative each. Two already-low sources were retained unchanged as controls. The initial alternatives were frozen before scoring; the later heading controls and one documented source-aware clarification are reported separately below.

The report alternatives used an informative title, labelled tables for comparable data, and ordinary prose for calculations, assumptions, interpretation and limitations. Their complete texts were measured in three representations:

- Original Markdown, including headings and table syntax.
- Plain text with tab-separated table cells and no Markdown syntax. This was a declared text representation, not an assumed PDF extraction.
- Text actually extracted from A4 PDFs rendered with ReportLab and embedded Arial fonts, using installed Poppler `pdftotext` in its default reading order. Every non-whitespace word and its order matched the corresponding plain-text report. All seven rendered pages were visually inspected.

## Website results

Values are the visible **P(AI), percent** field. Each original was measured again in the same session. They are detector outputs, not a calibrated probability that a person used AI.

| Synthetic report | Source | Source plus title | Full report, Markdown | Full report, plain text | Full report, PDF extraction |
| --- | ---: | ---: | ---: | ---: | ---: |
| Temperature-channel comparison | 99.93 | 2.11 | 0.97 | 0.08 | 0.08 |
| Sampling and aliasing | 100.00 | 99.95 | 56.37 | 3.76 | 3.76 |
| DC-motor model | 98.24 | 3.85 | 0.69 | 0.14 | 0.14 |
| Moving-average noise model | 99.99 | 98.86 | 0.91 | 0.05 | 0.05 |
| Loaded voltage divider | 99.95 | 19.58 | 2.04 | 0.07 | 0.07 |
| Ideal RC charging | 99.80 | 7.13 | 0.11 | 0.04 | 0.04 |
| Group difference and confidence interval | 99.90 | 8.06 | 0.53 | 0.05 | 0.05 |

The unchanged rise-time and optocoupler sources scored 1.53 and 31.10. Retaining them is part of the workflow, not an editing improvement.

The initial frozen comparison contained 23 measurements: nine sources and seven alternatives in two representations. Seven PDF extractions were then measured as a separate export check. An exploratory follow-up added fourteen controls: the seven sources with just the informative title added, and the seven reorganized report bodies without the title. One source-aware clarification of the filter report was measured again in all three representations, bringing the total to **47 verified website measurements**. The table shows that final report's scores; its earlier scores, 0.98/0.08/0.08, remain in the archive.

A title alone brought five of seven sources below 50. The bodies without titles had six scores below 50; the aliasing body remained at 99.01. However, a blind reviewer rejected the title-free filter control because removing its heading also removed the explicit definition of the averaging operation. That low score is not counted as a qualified success. Five of the six remaining body controls were below 50.

The full filter report had named the operation in its title. Its final version now also states it explicitly in the body, and both reviewers approved that clarification before selection. The new text and its actual PDF extraction were measured again. This distinction matters: removing a heading can change content as well as presentation.

These exploratory controls show that the effects depend on the complete input and its presentation. They do not isolate a universal stylistic feature or establish that tables are always necessary. The workflow therefore retains useful smaller changes before a full rewrite.

## Content, readability and coverage

Two separate blind LLM contexts compared every initial source/candidate pair without model labels or detector scores. They checked claims in both directions, numerical precision and associations, operators, assumptions, negations, uncertainty, work status, completeness, language and paired readability. Identical-source controls were mixed in. Both contexts approved the fourteen full report representations, with readability and register matching their own source ratings. The subsequent heading/body controls received a separate source comparison.

These were model reviews, not human technical peer review, a human-reader study or a proof of semantic equivalence. The three new fixtures were written for this pilot; they are not independently authored held-out material. Generation used Codex; native Claude generation was not tested.

All 47 inputs were checked with the live page's cleaner and the same-version browser tokenizer with truncation disabled: they used 226–377 tokens, below the website's 1024-token limit. The complete input echo, source hash and settled visible result were verified for each measurement. No material was hidden outside the scored input. The PDF extraction comparison preserved the complete word sequence.

The loaded 91,423,784-byte FP16 model had SHA-256 `3131fdf3cf47aa95ee883f20d9cfea7c6c8d37ee0c5023459debb752266163b9`. The live inline inference module had SHA-256 `3fd27994c0ed76a4a97666f6e93d4d5bba276b066e9ccbd7b321a92070d91c2a`. The [site source](https://github.com/pegesund/norsk-ai-detektor/blob/main/index.html) documents its normalization, token limit and model loading. Those public refs may change; the hashes identify what this session used.

## What the result does not establish

- General performance on long reports, already-titled documents, prose-only assignments or other subject areas.
- Transfer to Copyleaks, Sapling, Pangram, Turnitin or another detector. No new result on those services is included here.
- Identical behavior across PDF extractors, Word exports or school submission systems. Only the stated PDF pipeline was checked.
- A causal release advantage over 1.3.2, superiority to another humanizer, or a guarantee for future generations.
- Human authorship, watermark removal or absence of AI assistance.

Tables and titles are choices of report presentation. Use them when appropriate for the reader and assignment. Preserve a good source, and retain a faithful earlier version when a proposed revision is less readable or lacks a verified improvement.

The release's optional evaluation archive contains the synthetic sources, exact report texts, scores, hashes and review records. It is separate from the installable skill. Earlier versions and their results remain preserved.
