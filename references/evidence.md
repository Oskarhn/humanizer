# Evidence and limits

Research snapshot: 25–26 October 2026; watermark/provenance update on 26 October. This is a targeted, critically screened evidence review, not a systematic review or a meta-analysis. Twenty-two entries combine research, provider documentation, implementation documentation, and a language authority; they are not twenty-two independent experiments. Eight distinct papers were supplied as PDFs. A resubmission of the R02 PDF is byte-identical, and R16's Nature link was already covered. Access limits are stated below.

## What this evidence supports

1. AI and human corpora can differ at lexical, grammatical, rhetorical, affective, and content levels. Which signals matter depends on model, task, language, corpus, and processing.
2. Perceived naturalness, stylistic similarity, semantic fidelity, originality, authorship, and detector response are different outcomes. Improving one need not improve the others.
3. Direct examples and relevant context are worth using, but do not replace the author's own ideas or a source comparison.
4. A good editing workflow should preserve voice and content while addressing actual weaknesses. Population averages do not prescribe an individual's style.
5. Strong detector results in one setting coexist with false positives and poor transfer elsewhere. Neither “all detectors work” nor “all detectors are useless” follows.

**What is not established:** No cited study validates this complete skill, proves that a generic prompt can make arbitrary text undetectable, or establishes a universal formula for human writing. The four-pass workflow, priority order, examples, and preservation checks are design choices informed by the literature and editorial practice. They require behavioral evaluation. Norwegian guidance is primarily language-specific editorial guidance, not an empirically validated detector intervention.

## Evidence-to-decision map

| Design decision | Relevant evidence | Strength of inference |
| --- | --- | --- |
| Inspect genre and grammar, not only words | R08 | Direct corpus support; editorial application |
| Preserve consequential detail, bounded claims, and costs | R01 | Exploratory detector analysis; not a causal editing trial |
| Use real samples and context; check meaning afterwards | R05 | Direct result in social-reply simulation; transfer to documents is uncertain |
| Protect individual voice from generic polish | R09 | Large multi-dataset evidence of homogenization |
| Do not use intuition or a word list as proof of authorship | R04, R10, R11, R13 | Strong reason for caution within the studied settings |
| Keep formatting that serves the document | R03, R06 | Formatting signals can be learned; not a reason to damage presentation |
| Give fiction its own structural checks | R07, R15, R18 | Relevant creative-writing evidence; not universal plot rules |
| Separate watermarking from stylistic detection | R02, R16 | Different mechanisms and evaluation designs |
| Separate cleanup, rewriting, and actual watermark verification | R19–R22 | Mechanism-based inference; no new removal experiment |
| Test actual edits and preserve content | R05, R18 | Empirical motivation; this skill's exact procedure remains unvalidated |
| Avoid universal language-specific thresholds | R08, R12, R17 | Domain and language differences; guidance-based adaptation |

## The original PDF set

### R01 — IdeaLens

Rajendhran et al. (2026), *IdeaLens: Detecting AI Ideas in Long-form Writing*. [arXiv v1](https://arxiv.org/abs/2610.06778v1). Preprint; not represented here as peer-reviewed.

**Design and finding:** Approximately one million FineWeb documents labeled by a prose detector are converted to paraphrased outlines. Evaluation separates prose and idea provenance. Qualitative analysis of roughly 90,000 item predictions identifies consequential versus generic detail, usable versus apparent specificity, bounded versus overextended claims, and preserved versus erased costs.

**Limits:** Silver labels are inherited from Pangram rather than direct records of thinking. Outline extraction uses proprietary models; mixed ideation does not fit a clean binary label. A human-written/AI-plan study covers only 50 stories. Statistical provenance estimates are not proof about an individual. Pangram research credits are disclosed.

**Use:** Diagnose generic substance and erased trade-offs. Do not claim that an editor can change idea provenance or safely invent “human” details. See main pp. 7–9 and limitations appendix.

Supplied file: `2610.06778v1.pdf` (53 PDF pages).

### R02 — The Invisible Watermark

Bulut et al. (2026), *The Invisible Watermark: A Pilot Study on the Verifiability Gap in AI Text Watermarking*. Applied Sciences 16, 10335. [Publisher](https://www.mdpi.com/2076-3417/16/20/10335), [DOI](https://doi.org/10.3390/app162010335). Published journal article; explicitly a pilot.

**Design and finding:** Provider-document analysis plus small-backbone SynthID-Text experiments, initially 20 watermarked and 20 unwatermarked samples, with additional held-out tests and replications. Severe word corruption weakens the measured watermark signal.

**Limits:** GPT-2 and Pythia-410M, a single scheme, predominantly untrained scoring, and synthetic deletion/substitution are not modern commercial-system editing. A 50% corruption stress test is not ordinary humanization. Do not conflate same-sample threshold selection with held-out validation. The provider-policy discussion is time-sensitive; Anthropic's explanation and OpenAI's provenance material were checked directly in the update (R19/R22). This does not independently validate the paper's legal analysis or all provider-table classifications.

**Use:** Keep watermark evidence separate from prose style and avoid guarantees about watermark removal. Read alongside R16 and R19–R22, not as a stand-alone description of production robustness. The resubmitted PDF's hash matches the original; it is not counted as a second study.

Supplied file: `applsci-16-10335.pdf` (38 pages); abstract, methods, results, and limitations inspected locally. Publisher access was initially rate-limited.

### R03 — Artifact reliance

Voznyuk and Grabovoy (2026), *Measuring Artifact Reliance in Machine-Generated Text Detectors*. [arXiv v1](https://arxiv.org/abs/2610.13583v1). ArXiv record reports acceptance to the DocInsights workshop at EMNLP 2026.

**Design and finding:** Ten scientific-document subsets from six resources; superficial feature probes and content-preserving formatting counterfactuals. Newline and extraction artifacts explain substantial separability in some subsets. Detector sensitivity differs.

**Limits:** Scientific-document benchmarks and selected public detectors do not establish behavior of every commercial system. The paper distinguishes conditional decision flips from unconditioned margins; its abstract's 20–27% shorthand should not be conflated with the 42–58% conditional reversals discussed in §7.2. Surface separability does not itself predict transfer failure (§7.3).

**Use:** Treat PDF extraction and formatting as possible evaluation confounds. Never damage typography to imitate an artifact. A classifier responding to line wrapping has not identified a universal human writing trait.

Supplied file: `2610.13583v1.pdf` (12 pages).

### R04 — Style as a confound

Park, Jeong, and Kim (2026), *Style as a Confound: False Positives in AI Detection of Non-Native Academic Writing*. EMNLP 2026 Industry Track, pp. 1872–1887. [ACL record](https://aclanthology.org/2026.emnlp-industry.109/), [author preprint](https://arxiv.org/abs/2608.26710).

**Design and finding:** 135,389 original/edited manuscript pairs from a professional editing service, 2018–2025; thirteen public detectors. The same human edits can move detector scores in opposite directions. Only seven of thirteen score shifts meet the paper's practical-effect threshold.

**Limits:** Non-native academic English and one service; one author is affiliated with that service. Human authorship/content preservation depends on provenance and service procedures, especially after ChatGPT. No matched AI-generated editing controls. Absolute false-positive rates depend on thresholds and normalization. Correlation does not identify a single causal style feature.

**Use:** Do not equate polish with AI authorship or assume that clearer writing always reduces AI scores.

Supplied file: `2026.emnlp-industry.109.pdf` (16 pages); main text and limitations inspected. ACL page fetch failed in this review; the matching preprint's identity was verified. The conference header is not evidence that the event has finished.

### R05 — Conversational Human Authenticity Test

Pagan et al. (2026), *AI-generated language remains systematically distinguishable from human communication*. PNAS 123, e2531748123. [Publication record](https://pubmed.ncbi.nlm.nih.gov/42863061/), [DOI](https://doi.org/10.1073/pnas.2531748123).

**Design and finding:** Nine open-weight models, five calibration strategies, X/Bluesky/Reddit reply data. Stylistic examples and context retrieval produce more consistent improvements than abstract persona descriptions; affective differences persist. Lower detectability can coincide with reduced semantic similarity to actual replies.

**Limits:** Social simulation and replies, not unrestricted document editing; tested models and platform distributions limit transfer. Similarity to one observed reply is not a complete measure of truth or meaning. Human responses are not a unique correct answer. Changes in classification accuracy do not provide a per-document authorship certificate.

**Use:** Prefer concrete samples and context to vague personas. Compare the rewritten meaning to the original rather than optimizing a naturalness impression alone. Do not add hostility just because toxic language differs between corpora.

Supplied file: `pagan-et-al-2026-ai-generated-language-remains-systematically-distinguishable-from-human-communication.pdf` (12 pages); especially calibration and semantic-similarity discussion, pp. 5–8.

### R06 — Auditable detectors with sparse autoencoders

Dugan et al. (2026), *Building Auditable AI Text Detectors with Sparse Autoencoders*. [arXiv v1](https://arxiv.org/abs/2610.30006v1). Preprint.

**Design and finding:** SAE features, automated interpretations, fidelity filtering, and sparse classifiers; evaluated on open-domain and peer-review data. Features include very specific wording, punctuation, formatting, and domain signals. Feature-guided edits can alter the tested classifiers' decisions more than generic humanization prompts.

**Limits:** Auto-interpretations can have high recall but low precision, missing contextual dependencies. A detector feature is not necessarily a causal property of machine authorship. Prompted edit limits and observed edit distances differ in the adversarial experiment. Flipping these detectors does not establish transfer to other systems, semantic fidelity, or writing quality. Several authors are affiliated with DeepMind.

**Use:** Examine clusters of patterns in context. Do not turn a feature description, punctuation mark, or coefficient into a universal blacklist or claim of undetectability.

Supplied file: `2610.30006v1.pdf` (50 pages); methods, qualitative analysis, adversarial experiment, and limitations inspected.

### R07 — StoryScope

Russell et al. (2026), *StoryScope: Investigating idiosyncrasies in AI fiction*. [arXiv v6](https://arxiv.org/abs/2604.03136v6). PDF identifies itself as a COLM 2026 conference paper; the exact supplied revision is the evidence anchor.

**Design and finding:** A reported 61,608 long stories from human authors and five LLM families, across 10,272 prompts; 304 extracted features. Narrative-only classification achieves 93.2% macro-F1 in its evaluation. AI stories tend toward explicit themes, tidy causal structures, and less narrative diversity. Surface edits leave much narrative signal intact.

**Limits:** Literary excerpts and generated counterparts are not all real-world fiction. Automated feature extraction and provenance assumptions matter. Corpus statistics do not make nonlinear plots, ambiguity, or unhappy endings intrinsically better. Model-specific fingerprints are version-specific. The paper discloses credits from Pangram and Google.

**Use:** Inspect narrative choices only when creative-development scope permits it; do not claim lexical editing establishes originality. Bibliographic details for other works were checked independently rather than copied from this PDF's reference list.

Supplied file: `2604.03136v6.pdf` (30 pages).

## Additional research and language guidance

### R08 — Grammatical and rhetorical variation

Reinhart et al. (2025), *Do LLMs write like humans? Variation in grammatical and rhetorical styles*. PNAS 122, e2422455122. [DOI](https://doi.org/10.1073/pnas.2422455122), [author version](https://arxiv.org/abs/2410.16107).

Two parallel English corpora contain 66,320 and 76,920 chunks after filtering, including human context and six model continuations. Instruction-tuned models favor certain noun-heavy and participial constructions and struggle with genre variation. Cross-register/model transfer is imperfect.

**Limit and use:** Studied GPT-4o/Llama 3 generations are not a measurement of every current model. Inspect grammatical fit; do not ban nominalizations, participles, or passive voice. Main-text methods/results were available through the publisher's indexed text; PMC direct access intermittently challenged the fetch.

### R09 — Homogenization at scale

Sourati et al. (2026), *The shrinking landscape of linguistic diversity in the age of large language models*. Nature Human Behaviour. [DOI](https://doi.org/10.1038/s41562-026-02550-0), [publication record](https://pubmed.ncbi.nlm.nih.gov/42637911/), [preprint](https://arxiv.org/abs/2502.11266).

The published abstract reports three studies, seven datasets, and over 880,000 texts; rewriting/polishing reduces writing-complexity variance and can suppress individual differences while retaining core content.

**Limit and use:** Population variance is not an individual-text quality score or an optimal target. Preserve author-specific traits instead of imposing one polished voice. The published abstract, identity, and data/code statements were verified; the complete published methods were not accessible in this review, so precise mechanisms and effect estimates are not used as operational thresholds.

### R10 — Excess vocabulary in biomedical abstracts

Kobak et al. (2025), *Delving into LLM-assisted writing in biomedical publications through excess vocabulary*. Science Advances 11, eadt3813. [DOI](https://doi.org/10.1126/sciadv.adt3813), [author version v5](https://arxiv.org/abs/2406.07016v5), [record](https://pubmed.ncbi.nlm.nih.gov/40601754/).

More than fifteen million abstracts from 2010–2024 reveal population-level changes in certain style words after LLM adoption.

**Limit and use:** Aggregate excess vocabulary estimates do not establish authorship of one abstract or validate a banned-word list. Inspect inflated or repetitive vocabulary only in context. Do not mix early partial-2024 preprint statistics with the final version. Publication identity and the author abstract were checked; no aggregate prevalence estimate is used to score text here.

### R11 — Human heuristics

Jakesch, Hancock, and Naaman (2023), *Human heuristics for AI-generated language are flawed*. PNAS 120, e2208839120. [DOI](https://doi.org/10.1073/pnas.2208839120), [author version](https://arxiv.org/abs/2206.07271).

Six experiments with 4,600 participants study self-presentations. People rely on misleading cues such as first-person pronouns, contractions, and family topics.

**Limit and use:** Earlier models, self-presentation contexts, and human judgments do not measure current detector performance across genres. Natural-sounding text is not proof of human authorship; inserting fake personal details is not an evidence-based quality improvement. Publication text/abstract and identity were checked.

### R12 — RAID robustness benchmark

Dugan et al. (2024), *RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors*. ACL 2024. [Primary record and paper](https://aclanthology.org/2024.acl-long.674/).

Over six million generations span eleven models, eight domains, eleven adversarial attacks, and four decoding strategies. Twelve detectors show weaknesses under distribution and attack changes.

**Limit and use:** Benchmark size does not ensure representation of today's deployed systems. Treat detector evaluation as version- and domain-dependent. An attack success rate is not a writing-quality score. The ACL primary abstract and benchmark specification were checked; its attacks are not included as a rewrite recipe.

### R13 — Bias against non-native English writing

Liang et al. (2023), *GPT detectors are biased against non-native English writers*. Patterns 4, 100779. [DOI](https://doi.org/10.1016/j.patter.2023.100779), [author preprint](https://arxiv.org/abs/2304.02819).

Detectors tested on native/non-native English samples show substantial false-positive differences and sensitivity to language choices.

**Limit and use:** Early detectors and population differences limit transfer and causal interpretation. Do not equate simpler or second-language writing with AI. Do not impose native-speaker sophistication as a condition of credible authorship. Main-text introduction/discussion and publication record were checked; R04 supplies a newer paired-document comparison.

### R14 — Limits of reliable detection

Sadasivan et al., *Can AI-Generated Text be Reliably Detected?* TMLR; author version last revised January 2025. [Primary author version v4](https://arxiv.org/abs/2303.11156v4).

Experiments stress-test several detector families using paraphrasing; theory relates distinguishability to differences between human and model distributions.

**Limit and use:** Theoretical assumptions and adversarial settings do not prove all deployed detectors are useless, nor that every rewrite can evade them. Do not promise universal detection resistance. The revised primary abstract and publication status were checked; older summaries using stronger impossibility language were not adopted.

### R15 — Creativity and collective diversity

Doshi and Hauser (2024), *Generative AI enhances individual creativity but reduces the collective diversity of novel content*. Science Advances 10, eadn5290. [DOI](https://doi.org/10.1126/sciadv.adn5290).

An experiment with AI story-idea assistance finds higher assessed creativity for some writers alongside greater similarity across AI-assisted stories.

**Limit and use:** Short-story ideation is not a trial of this editing workflow or all long-form writing. Retain the user's own substantive choices; do not manufacture originality by randomizing style. Primary abstract and publication identity were checked. This DOI was verified independently because the supplied StoryScope bibliography gives inconsistent details for this work.

### R16 — Production-scale SynthID-Text

Dathathri et al. (2024), *Scalable watermarking for identifying large language model outputs*. Nature 634, 818–823. [Primary paper](https://www.nature.com/articles/s41586-024-08025-4).

Describes SynthID-Text sampling/detection and a live quality assessment across nearly twenty million responses. Detection is a generation-time statistical mechanism, distinct from judgments about prose style.

**Limit and use:** Model, length, entropy, key access, and detector settings matter. Production feedback about quality is not an adversarial editing trial. Authors disclose Google funding/affiliations and patent applications. Do not infer current product coverage or guarantee watermark removal. Main-text mechanisms, evaluation, limitations, and disclosures were inspected.

### R17 — Norwegian plain-language guidance

Språkrådet, [Generelle skriveråd](https://sprakradet.no/klarsprak/om-skriving/generelle-skriverad-bokmal/), [Skriveråd for ulike teksttypar](https://sprakradet.no/klarsprak/om-skriving/skriverad-for-ulike-teksttypar/), accessed October 2026.

Norway's language authority recommends audience-appropriate structure, concrete language, useful verbs, and clarity about actors.

**Limit and use:** Authoritative editorial guidance, not an AI-detection experiment. Apply Norwegian idiom and register without presenting English corpus findings as a Norwegian detector formula. The guidance pages were read; examples in this skill are newly authored rather than copied from those pages.

### R18 — Expert-informed editing

Chakrabarty, Laban, and Wu (2025), *Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits*. CHI 2025. [DOI](https://doi.org/10.1145/3706598.3713559), [author full text v5](https://arxiv.org/html/2409.14509v5).

The LAMP corpus contains 1,057 paragraphs edited by professional writers using a seven-category taxonomy. Automatic editing improves preference outcomes over raw generation, while experts generally prefer expert edits.

**Limit and use:** Creative-domain paragraphs and tested model/prompt combinations do not prove whole-document or scientific-writing improvements; hallucination risk was not evaluated. Use local diagnosis plus revision, then assess the outcome. Speculative explanations about opaque model training data are not adopted here. The primary abstract, taxonomy, evaluation discussion, and limitations were inspected. This skill does not redistribute the LAMP corpus.

## Watermark/provenance update — 26 October 2026

### R19 — Anthropic's explanation

Anthropic (2026), *How Claude's text watermark works*, published 14 August, updated 1 September. [Primary announcement](https://www.anthropic.com/news/claude-text-watermark).

Describes a SynthID-derived token-choice signal, not inserted characters. It reports private-preview detection access, limited short/constrained-text evidence, and marking of generated translations. Detection does not separate drafting from heavy editing or establish human authorship.

**Limit and use:** Provider documentation, not an independent experiment or proof about this session. Launch statements do not establish coverage of every historical model. Read in full; keep appearance and keyed provenance separate. The new reference applies these distinctions without repeating a provider FAQ in ordinary edits.

### R20 — SynthID source and tournament design

Google DeepMind, [repository README](https://github.com/google-deepmind/synthid-text/blob/07c83fea815b78d9454f9df18fdef8d940803e7c/README.md) and Tor Lattimore, [tournament design](https://github.com/google-deepmind/synthid-text/blob/07c83fea815b78d9454f9df18fdef8d940803e7c/docs/tournament.md). Reviewed at commit `07c83fea815b78d9454f9df18fdef8d940803e7c` (23 October 2026).

**Limit and use:** Primary implementation documentation, not a new independent study. Distinguish reference code from production design, random-key guarantees from fixed-key calibration, and example keys from provider keys. Snapshotting the commit makes the mutable `main` links reproducible. The README and design were read, not installed or executed; no compatible provider detector or watermark-removal test is claimed.

### R21 — textGrain technical report

Li et al. (2026), *textGrain: Entropy-Calibrated Watermarking for Language Model Text*, dated 5 October. [Official report](https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf).

**Identity:** The supplied `2604.031316v6.pdf` is a 20-page textGrain report, not the earlier 30-page StoryScope `2604.03136v6.pdf`. Its bytes match the PDF linked directly by OpenAI (R22). The filename is not treated as a verified arXiv ID or version.

**Design:** Entropy-calibrated coupling of token blocks and keyed randomness using optimal transport, with a numerical solver and explicit assumptions. Preserving probabilities averaged over keys/columns does not guarantee unchanged entropy for every response. Detection needs matching key/configuration, but not generation-time model probabilities or the entropy budget.

**Limits and use:** Technical report, not described here as peer-reviewed. Main construction/detection and relevant theorem conditions were inspected; proofs were not independently verified and experiments were not reproduced. Ideal null calibration and conditional sequence-preservation claims retain their assumptions. The report supplies no empirical head-to-head performance benchmark. Use these distinctions to prevent a “more varied words means no watermark” fallacy, not as a recipe for rewriting percentages.

### R22 — OpenAI's provenance announcement and help

OpenAI (5 October 2026), [Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance/), and [Provenance signals in OpenAI-generated content](https://help.openai.com/en/articles/8912793-provenance-signals-in-openai-generated-content), accessed 26 October.

**Limit and use:** Provider claims and product/access documentation, not independent validation. The announcement directly links R21 and separates regional app rollout, API opt-in, and restricted detector access. A public paper does not confer detector access or prove that open sourcing has occurred. No live deployment is inferred for this user. Empirical results in the announcement are separate from R21's mathematical report; neither establishes a universal removal guarantee.

## Source selection and maintenance

Prioritize original papers, author preprints, publisher records, and language authorities. Check identity, revision, sample construction, controls, model dates, outcome definition, limitations, and conflicts of interest. A large sample can make a biased estimate precise; it cannot repair confounding or weak ground truth.

Excluded as evidence for operational promises: humanizer-vendor marketing, unsupported word lists, detector leaderboard claims without methods, search-result summaries treated as full papers, and legal/product statements copied from secondary discussions. Search also surfaced smaller genre-specific studies; those were not needed to justify broad rules and were not used to imply universal transfer.

The local PDF manifest records hashes and exact supplied files in [supplied-pdfs.json](supplied-pdfs.json). The [update record](source-update-20261026.json) documents duplicate detection, official-PDF identity, and the repository revision. Original PDFs and extracted paper/code text are not redistributed with the skill. Source licenses remain with their rights holders; the project's MIT license covers its original instructions, scripts, tests, and examples.

When updating: verify the relevant primary version, revise only the rule supported by the new evidence, add a counterexample if it changes behavior, and rerun behavioral tests. An updated detector result alone does not justify degrading prose.
