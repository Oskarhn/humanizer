# Choosing a Humanizer skill

This comparison concerns the source versions reviewed on 26 October 2026. It helps explain this project's intended fit; it does not establish a best editor for every language or document. Other projects may have changed since those snapshots.

## Differences that affect everyday use

**This Humanizer** combines explicit English, Bokmål, and Nynorsk guidance with technical and academic preservation rules. It distinguishes calculations, simulations, measurements, and verified results; it also checks actors, obligations, uncertainty, and logical connections. Its default output is the revised prose. These priorities suit a report writer who wants an editor that protects the content while improving its expression.

**Academic Humanizer** is a strong alternative for English papers, theses, rebuttals, and funding proposals. Its instructions explicitly protect scholarly hedging, passive voice, and technical terms. Its academic specialization is useful. The reviewed source also contains tensions between preserving every citation and reducing citation clusters, and examples that add evidence absent from the before-text. Those are instruction-design concerns, not fabrications observed in our trial.

**Hannsxpeter** is a strong alternative for voice matching and restrained editing. Its reference on what not to flag is useful. The reviewed version also calls for a substantial output report and uses rough pattern-density categories. Those categories should not be read as verified authorship. Its outputs performed well in the local trial.

**Blader** provides a broad, concrete pattern catalog. It can be useful for learning what to inspect in generic prose. The reviewed version's strong dash rule and some examples need judgment in technical writing. Our trial preserved the explicitly protected range and code, so these source concerns should not be reported as observed range corruption.

**Milock** offers channel guidance, author/brand profiles, and structured reviews. That is useful for email, social, and publishing work. Its larger channel and reporting workflow may be more than a report writer needs. It also has substantive preservation rules; it is not simply a word blacklist.

**Stop Slop** is much shorter and more prescriptive. Its reviewed instructions ban adverbs and passive constructions. Those rules can conflict with a report's qualifications and unknown operators. In the trial, it repeatedly added an author-group actor where the source did not identify one.

## What the trial showed

Fourteen synthetic requests were run under each of six skills and a no-skill control: 98 final outputs. Separate LLM reviewers received anonymous labels shuffled per case, the original text, and explicit expectations. They assessed meaning before style.

| Condition | Outputs with no fidelity issue recorded |
| --- | ---: |
| Academic Humanizer | 14/14 |
| Hannsxpeter | 14/14 |
| This Humanizer **1.1.0** | 13/14 |
| Milock | 12/14 |
| No skill | 12/14 |
| Blader | 11/14 |
| Stop Slop | 5/14 |

The issue in local 1.1.0 was a connective that slightly changed the statistical reasoning. A later maintenance change made that check explicit. In a separate five-case paired regression, both 1.1.0 and 1.1.1 passed every case and all pairs tied. This did not demonstrate an improvement.

The comparison column must not be relabeled as a test of today's package. Later packaging and documentation changes are not new writing trials.

## How much confidence to place in it

This was a small local comparison, with one grouped generation context per condition. Exact model identifiers were not exposed. Four stress cases were added after partial inspection, two line-break fixtures were repaired and rerun, and an incorrect Nynorsk penalty was corrected against the language authority. Many outputs tied. Reviewers also differed in how they rated the severity of attribution changes.

There was no independent human-reader panel, repeated multi-model study, native-Claude writing result, detector-resistance experiment, or watermark test. The trial supports inspecting these concrete editorial failures; it does not provide general error rates or prove superiority.

The [archived comparison record](https://github.com/Oskarhn/humanizer/tree/304f74ebe1c57e5b58bed384cb286e20206eb950/evals/comparison-2026-10-26) contains the cases, outputs, corrections, and judgments. They remain outside the current user package.

## Additional provenance-tool review

[Watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover/tree/5c180932a00c793261177f79aee21db8929f3fe2), reviewed separately on 29 October 2026, combines character cleanup, statistical-rewrite tooling, and file-provenance tools. It was **not** a condition in the fourteen-task comparison above. Its controlled SynthID test setup does not establish commercial-detector evasion or textGrain removal. Humanizer adopts inspection and preservation ideas in its optional text-hygiene guidance, without bundling that project's service or using its stylometry scores as editing targets.

## Exact source versions in the original comparison

- [Academic Humanizer](https://github.com/AIScientists-Dev/academic-humanizer/tree/94b88b23703bed7df507acae7d6d5876209a0cdf)
- [Hannsxpeter](https://github.com/hannsxpeter/humanizer/tree/e8f1248a7d4919689c1f942e356ed95b102d9f07)
- [Blader](https://github.com/blader/humanizer/tree/8c307f367c91bd974002f10f2be2965d642c13df)
- [Milock](https://github.com/milock/humanizer/tree/ec66c203c0400481819fda9cb17a6f1c7977c975)
- [Stop Slop](https://github.com/hardikpandya/stop-slop/tree/8da1f030185bdfe8471220585162991eaeb970e9)

Choose the workflow that fits your documents. For this project, the practical case is explicit Norwegian support, technical precision, flexible editing depth, and a clean default response. For a specialized English grant-writing or channel-publishing workflow, another skill may fit better.
