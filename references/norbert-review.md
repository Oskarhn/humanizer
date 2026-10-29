# Measured editing for Bokmål reports

Use this optional local mode when the user requests Bokmål detector-focused editing and a compatible NorBERT detector is available. The separately documented transfer check also applies to English when the requested service supports it. Keep the ordinary editing workflow and English guidance unchanged. A provider/model-specific measurement is not a guarantee about Pangram, Copyleaks, Sapling, authorship, or watermarks.

## Establish the test

Keep the source and its claim ledger. Record the exact detector artifacts, preprocessing, language, threshold and coverage. The optional local helper uses a pinned Norwegian AI classifier fine-tuned from NorBERT-4-small. Its downloaded weights and author preprocessor keep their own CC BY-SA license and are not bundled with this skill. Do not silently install packages or substitute an incompatible model. Use existing authorized tools, or explain the missing setup.

Keep the source, current draft and any previously accepted version separately. Check the source or accepted version before creating another rewrite. If it already meets the writing brief and the measured target on the requested detector, retain it. Do not introduce a new revision just to produce visibly different wording.

When changes are needed, score the source, normal revision and supplied accepted reference on the same detector/configuration. Preserve those exact texts and their results throughout the comparison. The source is the factual authority; a supplied accepted reference still needs to match the current claims and brief. A low score does not make either text correct or readable.

## Build meaningful alternatives

When substantive changes are authorized, split the source into paragraph-sized claim groups. Preserve order where required by the method. Before search, source-check each group alternative and remove new awkward phrasing. For each group, supply three complete, grammatical alternatives that retain every distinct fact, numeric association, qualification, exclusion, recommendation and work status. Keep protected quotes, code, formulas, citations and terminology accurate.

Start from the source claim ledger when the existing wording keeps producing weak alternatives. Write a complete report for the same reader before adjusting local wording. Explore result-first and method-first explanations, clause order and sentence boundaries. Use ordinary technical Bokmål; keep passive voice where it fits, but do not manufacture impersonal nominalizations as a detector tactic. Keep the requested Bokmål/Nynorsk variety. Do not add a persona, anecdote, typo, rare synonym, irrelevant detail, invisible character or padding merely to affect a score. Do not remove an inconvenient limitation. Missing evidence remains missing evidence; it does not become an assertion that the work was never performed.

The supplied helper can rank full-text combinations with bounded beam search. Its default budget is four retained paths, two passes and at most 256 actual local inferences per document. It records cache reuse separately and keeps evaluated source, search baseline and any supplied accepted reference in `protected_references`, outside beam pruning and the three-candidate shortlist. This is a local search over authored alternatives, not a replication of token-level adversarial decoding or model training.

## Gate before accepting a low score

The helper's numeric and length screens do not establish meaning preservation. Review each shortlisted complete text against the original in both directions: every source claim needs a counterpart, and every revised claim needs source support. Inspect evidence status, modality, causality and citation attachment explicitly. Reject drifting candidates before selection. Where available, a separate blind source review adds confidence; it does not replace the author's factual review.

Read the surviving texts for coherence, register and voice. Compare readability directly with the normal revision and the previously accepted version. A lower detector score does not justify a heavier or less natural report. If a review calls two texts equally readable but gives the revision a lower clarity rating or identifies new awkward phrasing, resolve that inconsistency before accepting it. Retain the comparison text while the quality judgment remains unresolved. Check frequency/value lists and other ordered associations aloud: write an explicit mapping when compressed wording makes the reader reconstruct it. A disjoint combination of individually correct paragraphs is not an acceptable report. If a source-only repair is needed, score the repaired final text again. Do not present the pre-repair score as its result.

When detection is the user's stated priority, first retain only faithful versions that match or improve the comparison text's readability. Then choose among those by measured target score. If three paragraph alternatives all share a weak construction, generate a small set of complete source-ledger redrafts rather than repeating that construction through more search passes. Review complete redrafts as whole texts; the existing helper's score command can measure them directly. Keep the comparison text as an evaluated fallback. Retain the normal revision or source if no acceptable improvement exists. Report that outcome rather than manufacturing a pass. Do not average percentages from unrelated detectors or optimize a named detector through an unvalidated proxy.

## Transfer checks for Bokmål and English

Keep a frozen regression set containing earlier good outputs and their original sources. Compare exact input identities, not case names reused in different studies. A version claim needs the same source/brief, language, detector/model/settings, input route and coverage, plus a shared quality criterion. Repeated generations can differ under one unchanged skill; disclose that variation rather than presenting the lowest sample as a release effect.

Use immutable source and output hashes, and record text encoding/line endings, generation replicate, workflow mode and provider score field. Keep ordinary editing separate from optional search and experimental methods. If settings or the source change, start a new comparison. Do not silently replace an old successful text with a newly generated approximation.


Treat every requested detector as a separate test. Freeze the comparison and selected full texts after source and readability checks, then submit those exact versions through an authorized interface. Record the input hash, provider output field, configuration, date and observed model version. Check that displayed results belong to the current input and have settled. Where an authorized interface exposes the actual response, verify the visible score agrees with that response. A stale result, loading value or animated gauge is not a new measurement. Preserve discrepancies as unverified attempts, not performance evidence.

Use supported languages for efficacy claims. Sapling's published language list does not include Norwegian, so use English for its meaningful comparison. A Norwegian number from an unsupported service is at most exploratory. A local NorBERT gain does not establish a Copyleaks or Sapling gain. Keep a separate best eligible reference per requested provider; do not discard a good result on one because another uses a different scale. Report trade-offs instead of calling them a general upgrade. Do not average their different score fields into a single “human percentage.”

Keep unsuccessful and unchanged cases. Identical before/after text can share one recorded result; label reuse rather than counting a second scan. Respect free limits and stop on a quota or human-verification gate. Record missing comparisons as unavailable. Do not replace a missing baseline with a guessed score, reset a profile to obtain more scans, or silently create a paid/account-dependent workflow.

For an explicitly requested bounded detector comparison, this reference supplies the alternative-search procedure in place of text-hygiene's ordinary one-revision default. It does not authorize endless score chasing, unrequested translation, or extra edits after the writing brief and target are met.

## Coverage and delivery

The author-recommended inference context is 1,024 total tokens. The helper refuses silent truncation. Explicit windowed mode checks the whole text and reports the worst window; that aggregation is a stated protocol choice, not the original author's whole-document probability. Never bury questionable text outside the scored portion.

Return the requested prose. For a requested audit, include the final text hash, exact artifact/version, configuration, whole-text coverage, observed scores/verdict and any remaining uncertainty. The helper never certifies factual equivalence or assigns a human-authorship percentage. Ordinary writing tasks need neither this experiment nor an appended detector report.

## Setup and command reference

Ordinary Humanizer use requires no Python, model download or detector. This helper is an optional local measurement step for Norwegian text. It scores supplied text or searches among alternatives you have already written; it does not generate edits. English writing keeps its ordinary workflow.

### Install an optional runtime

The helper uses Python 3.10+ syntax. The exact dependency set below requires **Python 3.12+** because NumPy 2.5.4 requires it; the tested runtime was Python 3.12.14 on Windows. Other Python/platform combinations have not been established by this setup check.

Create and select a dedicated virtual environment. In these examples, `python` means that environment's interpreter; use its full executable path if necessary.

```sh
python -m venv .venv-norbert
# Activate .venv-norbert using your shell, then:
python -X utf8 -m pip install numpy==2.5.4 onnxruntime==1.31.1 tokenizers==0.23.3
python -X utf8 -m pip install huggingface_hub==2.4.0
```

These four versions were verified in the installed runtime. `huggingface_hub` is needed for the optional download example, not for offline scoring.

### Obtain separately licensed artifacts

Use model repository `pegesund/norwegian-ai-detector` at commit `0df563e67066e1eadd08eaceac80f1db4ed71f90`. Download only these three artifacts, preserving their relative paths:

```text
path/to/norbert-model/
  onnx/detector_int8.onnx
  tokenizer.json
  clean_text.py
```

The [upstream model card](https://huggingface.co/pegesund/norwegian-ai-detector/blob/0df563e67066e1eadd08eaceac80f1db4ed71f90/README.md) declares CC BY-SA 4.0. Credit **LTG-UiO for NorBERT-4 and Petter Egesund for fine-tuning**. The model artifacts and cleaner are separately supplied upstream material; they are not bundled or relicensed under the helper's MIT license. Follow the upstream license when sharing or adapting that material.

The official Hugging Face [`snapshot_download` API](https://huggingface.co/docs/huggingface_hub/guides/download) supports a pinned revision and an exact file allowlist. Replace the destination before running:

```sh
python -X utf8 -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='pegesund/norwegian-ai-detector', revision='0df563e67066e1eadd08eaceac80f1db4ed71f90', allow_patterns=['onnx/detector_int8.onnx', 'tokenizer.json', 'clean_text.py'], local_dir='path/to/norbert-model')"
```

This command downloads repository files without importing or executing repository Python code. It needs network access. The helper itself has no download or network step. Do not use a model-loading command with `trust_remote_code` for this setup.

The helper requires these exact SHA-256 values:

| Artifact | SHA-256 |
| --- | --- |
| `onnx/detector_int8.onnx` | `7a4096d8a720129520d0fb90792aee5ff27cc88e23039199aa93ed399ed338e7` |
| `tokenizer.json` | `5c1c0abf91d5944d039872765d7b36c889640ceb5b99ebc601d02873cfbcb600` |
| `clean_text.py` | `cbc68efcaeae508f7478030f6bd5bc4ba4989e6486e6c86e78b8f199d5589582` |

It rejects mismatches. At scoring time it compiles and executes only the cleaner source bytes it has just hash-verified; it does not load cleaner `.pyc` caches or execute packet text. Cleaning affects model input only. Returned/delivered text remains the original raw candidate.

### Score a JSON batch

Run the commands from the installed skill folder. Save UTF-8 `score-input.json` as an array with unique, nonempty string IDs:

```json
[
  {"id": "draft-a", "text": "Båten kom klokken 08.00. Vi ventet på kaia."},
  {"id": "draft-b", "text": "Klokken 08.00 kom båten. Vi ventet på kaia."}
]
```

```sh
python -X utf8 scripts/norbert_local.py score --model-dir path/to/norbert-model --input score-input.json --output score-results.json
```

Scores on these short schema examples do not establish writing quality or detector accuracy. The output includes raw text, so choose a local destination suitable for your text's sensitivity.

### Search reviewed alternatives

Save UTF-8 `search-input.json`. `source` is the factual source against which the host reviews fidelity. `baseline` is the starting draft assembled from the paragraph groups. Optional `accepted_reference` is an earlier retained text for the same source and brief; it is not script-certified approval. All distinct supplied references are measured and retained before search. Joining every group's `original` with exactly `\n\n` must equal `baseline`, byte for byte after JSON decoding. Every group requires exactly three alternatives, giving four choices including its original.

```json
[
  {
    "id": "draft-1",
    "language": "nb",
    "source": "Båten kom klokken 08.00. Vi ventet på kaia.",
    "baseline": "Klokken 08.00 kom båten.\n\nVi ventet på kaia.",
    "accepted_reference": "Båten kom klokken 08.00. Vi ventet på kaia.",
    "groups": [
      {
        "original": "Klokken 08.00 kom båten.",
        "alternatives": [
          "Båten kom klokken 08.00.",
          "Båten ankom klokken 08.00.",
          "Klokken 08.00 ankom båten."
        ]
      },
      {
        "original": "Vi ventet på kaia.",
        "alternatives": [
          "På kaia ventet vi.",
          "Det var på kaia vi ventet.",
          "Vi ventet der, på kaia."
        ]
      }
    ]
  }
]
```

```sh
python -X utf8 scripts/norbert_local.py search --model-dir path/to/norbert-model --input search-input.json --output search-results.json --guard-numbers
```

Search accepts explicit Norwegian language tags (`no`, `nb`, `nn`, `Norwegian`, `Bokmål`, `Nynorsk`). Each evaluated substitution is scored as the full assembled document, with deterministic caching and deduplication. Defaults are beam width 4, two passes and at most 256 actual model inference calls **per document**, including all protected-reference windows. This bounded search does not guarantee the globally best combination.

| Flag | Effect |
| --- | --- |
| `--beam-width 4` | Number of retained beam candidates. |
| `--passes 2` | Number of passes across paragraph groups. |
| `--max-inferences 256` | Actual inference-call budget per document; configurable from 1 to 256. |
| `--threads 1` | ORT intra-operation CPU threads; inter-operation threads remain 1. |
| `--guard-numbers` | Preserve literal numeric forms/counts, including signs, exponents and explicit uncertainty. This does not check unit association or meaning. |
| `--guard-word-bounds` | Require candidate word count from 150 through floor(110% of source word count). Omit for the tiny schema example above. |
| `--windowed` | Explicitly enable full-coverage, nonoverlapping windows for long model inputs. |

`protected_references` keeps every distinct `source`, `baseline` and supplied `accepted_reference`, with all shared role names when texts are identical. Numeric/length guard rejection, beam pruning and the three-candidate limit do not remove them. They have no paragraph-choice path unless the groups actually assemble that text. Every reference still carries `NOT_PERFORMED_BY_SCRIPT` for fidelity.

All reference windows count toward the budget. If their total cannot fit, the helper fails before any inference with `budget_too_small_for_protected_references`, leaving existing output intact. Search uses the remaining budget and reuses identical raw texts. A budget stop returns only already measured candidates; it never promotes an unmeasured candidate.

### Read results and review the text

Output schema is `norbert-local-helper-v1`. Score rows include raw text/SHA-256, both logits, `ai_probability`, `ai_minus_human_margin`, token counts and window details. Search returns the measured baseline, up to three assembled alternatives, their actual paragraph choices, all `protected_references`, `best_measured_sha256`, a search log and actual inference/cache counts. Resolve the best hash across both generated candidates and protected references. It denotes the lowest measured detector margin, not the best or factually approved prose. Provenance records model revision/hashes, runtime versions, CPU provider and thread settings. Numeric-only per-document completion progress goes to stderr; it contains no text or IDs.

Ranking minimizes the AI-minus-human logit margin. `ai_probability` is the model's two-class softmax score, **not** a calibrated authorship probability, percent AI-written, watermark test or fidelity measurement. Search logs describe measured candidates; they do not explain causal writing features.

By default, inputs exceeding 1,024 tokens after cleaning/tokenization are rejected rather than silently truncated. `--windowed` covers all content tokens, scores windows separately and reports the worst window's AI margin/score/logits. This is labelled `worst_window_AI_margin_NONSTANDARD`; it is a separate document aggregation, not the author's single-input protocol, and loses cross-window context.

The host must review claims, numbers and their units, attribution, uncertainty, readability and source fidelity before accepting any result. Search marks fidelity `NOT_PERFORMED_BY_SCRIPT`. Repair factual or readability problems first, then rescore the repaired full text; an earlier score does not transfer to a new draft. A low detector score alone is insufficient grounds to accept an edit.

The helper writes JSON atomically and rejects an identical input/output file. Check its exit status: a failed run commits no new report, so any existing report at the destination may belong to an earlier run.

### Optional machine profile and Windows/WSL

An installation may provide `~/.config/humanizer/norbert.json` with a `python` argument array, `model_dir`, `job_dir` and `path_style`. The host may read that profile to locate an existing optional runtime; the helper does **not** auto-read it or install missing components. Use the helper script from the currently loaded package. Treat profile paths as machine-specific, never as portable package defaults.

On Windows, native Python needs Windows paths. Native WSL Python needs Linux/WSL paths. When WSL invokes a Windows Python executable, convert **all** file arguments to Windows paths first (for example with `wslpath -w`), including script, model, input and output. Preserve the profile's argument array as separate arguments; do not concatenate it into an executable shell string. Select one runtime/path style consistently for each run.
