# Norwegian editing with an actual local detector

Use this optional mode only when the user requests Norwegian detector-focused editing and a compatible local NorBERT detector is available. Keep the ordinary editing workflow and English guidance unchanged. A provider/model-specific measurement is not a guarantee about Pangram, Copyleaks, Sapling, authorship, or watermarks.

## Establish the test

Keep the source and its claim ledger. Record the exact detector artifacts, preprocessing, language, threshold and coverage. The optional local helper uses a pinned Norwegian AI classifier fine-tuned from NorBERT-4-small. Its downloaded weights and author preprocessor keep their own CC BY-SA license and are not bundled with this skill. Do not silently install packages or substitute an incompatible model. Use existing authorized tools, or explain the missing setup.

First score the complete source and a normal source-checked revision. If the ordinary revision already satisfies the user's measured target and writing brief, finish the source check; do not keep rewriting a satisfactory document.

## Build meaningful alternatives

When substantive changes are authorized, split the source into paragraph-sized claim groups. Preserve order where required by the method. For each group, produce three complete, grammatical alternatives that retain every distinct fact, numeric association, qualification, exclusion, recommendation and work status. Keep protected quotes, code, formulas, citations and terminology accurate.

Vary real expression: result-centered reporting, conventional impersonal academic phrasing, clause order and sentence boundaries. Keep the requested Bokmål/Nynorsk variety. Do not add a persona, anecdote, typo, rare synonym, irrelevant detail, invisible character or padding merely to affect a score. Do not remove an inconvenient limitation. Missing evidence remains missing evidence; it does not become an assertion that the work was never performed.

The supplied helper can rank full-text combinations with bounded beam search. Its default budget is four retained paths, two passes and at most 256 actual local inferences per document. It records cache reuse separately and always retains an evaluated original option. This is a local search over authored alternatives, not a replication of token-level adversarial decoding or model training.

## Gate before accepting a low score

The helper's numeric and length screens do not establish meaning preservation. Review each shortlisted complete text against the original in both directions: every source claim needs a counterpart, and every revised claim needs source support. Inspect evidence status, modality, causality and citation attachment explicitly. Reject drifting candidates before selection. Where available, a separate blind source review adds confidence; it does not replace the author's factual review.

Read the surviving texts for coherence, register and voice. A disjoint combination of individually correct paragraphs is not an acceptable report. If a source-only repair is needed, score the repaired final text again. Do not present the pre-repair score as its result.

When detection is the user's stated priority, choose the lowest measured target score among faithful, clear versions that still meet the writing brief. Retain the normal revision or source if no acceptable improvement exists. Report that outcome rather than manufacturing a pass. Do not average percentages from unrelated detectors or optimize a named detector through an unvalidated proxy.

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

Save UTF-8 `search-input.json`. `source` is the original source/seed against which the host reviews fidelity. `baseline` is the starting edited draft. Joining every group's `original` with exactly `\n\n` must equal `baseline`, byte for byte after JSON decoding. Every group requires exactly three alternatives, giving four choices including its original.

```json
[
  {
    "id": "draft-1",
    "language": "nb",
    "source": "Båten kom klokken 08.00. Vi ventet på kaia.",
    "baseline": "Klokken 08.00 kom båten.\n\nVi ventet på kaia.",
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

Search accepts explicit Norwegian language tags (`no`, `nb`, `nn`, `Norwegian`, `Bokmål`, `Nynorsk`). Each evaluated substitution is scored as the full assembled document, with deterministic caching and deduplication. Defaults are beam width 4, two passes and at most 256 actual model inference calls **per document**, including baseline/windows. This bounded search does not guarantee the globally best combination.

| Flag | Effect |
| --- | --- |
| `--beam-width 4` | Number of retained beam candidates. |
| `--passes 2` | Number of passes across paragraph groups. |
| `--max-inferences 256` | Actual inference-call budget per document; configurable from 1 to 256. |
| `--threads 1` | ORT intra-operation CPU threads; inter-operation threads remain 1. |
| `--guard-numbers` | Preserve literal numeric forms/counts, including signs, exponents and explicit uncertainty. This does not check unit association or meaning. |
| `--guard-word-bounds` | Require candidate word count from 150 through floor(110% of source word count). Omit for the tiny schema example above. |
| `--windowed` | Explicitly enable full-coverage, nonoverlapping windows for long model inputs. |

The baseline remains available even if an optional guard would reject it. A budget stop returns only already measured candidates; it never promotes an unmeasured candidate. A baseline needing more calls than the budget fails the run.

### Read results and review the text

Output schema is `norbert-local-helper-v1`. Score rows include raw text/SHA-256, both logits, `ai_probability`, `ai_minus_human_margin`, token counts and window details. Search returns the measured baseline, up to three distinct alternatives, their paragraph choices, `best_measured_sha256`, a search log and actual inference/cache counts. Provenance records model revision/hashes, runtime versions, CPU provider and thread settings. Numeric-only per-document completion progress goes to stderr; it contains no text or IDs.

Ranking minimizes the AI-minus-human logit margin. `ai_probability` is the model's two-class softmax score, **not** a calibrated authorship probability, percent AI-written, watermark test or fidelity measurement. Search logs describe measured candidates; they do not explain causal writing features.

By default, inputs exceeding 1,024 tokens after cleaning/tokenization are rejected rather than silently truncated. `--windowed` covers all content tokens, scores windows separately and reports the worst window's AI margin/score/logits. This is labelled `worst_window_AI_margin_NONSTANDARD`; it is a separate document aggregation, not the author's single-input protocol, and loses cross-window context.

The host must review claims, numbers and their units, attribution, uncertainty, readability and source fidelity before accepting any result. Search marks fidelity `NOT_PERFORMED_BY_SCRIPT`. Repair factual or readability problems first, then rescore the repaired full text; an earlier score does not transfer to a new draft. A low detector score alone is insufficient grounds to accept an edit.

The helper writes JSON atomically and rejects an identical input/output file. Check its exit status: a failed run commits no new report, so any existing report at the destination may belong to an earlier run.

### Optional machine profile and Windows/WSL

An installation may provide `~/.config/humanizer/norbert.json` with a `python` argument array, `model_dir`, `job_dir` and `path_style`. The host may read that profile to locate an existing optional runtime; the helper does **not** auto-read it or install missing components. Use the helper script from the currently loaded package. Treat profile paths as machine-specific, never as portable package defaults.

On Windows, native Python needs Windows paths. Native WSL Python needs Linux/WSL paths. When WSL invokes a Windows Python executable, convert **all** file arguments to Windows paths first (for example with `wslpath -w`), including script, model, input and output. Preserve the profile's argument array as separate arguments; do not concatenate it into an executable shell string. Select one runtime/path style consistently for each run.
