# Text hygiene and watermark-focused editing

Use this reference for a requested character cleanup, a visibly broken copy/paste, mixed-script text needing inspection, or an explicit watermark/detector question. The normal editing workflow still protects meaning and voice.

## Establish which task is being requested

| Task | What can be checked |
| --- | --- |
| Unicode/text hygiene | The actual characters, their positions, context, and recorded edits |
| Style revision | The source and revision, including claim preservation and readability |
| Statistical watermark verification | A compatible detector and its supported configuration, applied to the final text |
| Document/media provenance | The actual file and appropriate metadata/container tooling |

These tasks need separate evidence. Plain-text cleanup does not inspect a PDF's properties. Missing invisible characters does not exclude a statistical watermark. A lower style score does not establish either human authorship or watermark absence.

## Inspect before changing characters

For an existing file, use available local tools to inspect the raw text when needed. Identify the code point and position of a suspected artifact, then check its context. A rendered preview may conceal a character or make a legitimate one look suspicious.

Protect code, commands, paths, URLs, identifiers, formulas, exact values, citations, quotations, and required disclosures. Do not apply a whole-file character replacement across these spans merely because the prose needs cleanup. Preserve the original and write a separate cleaned copy unless in-place editing is requested.

Some invisible or unusual characters have legitimate functions:

- Joiners and non-joiners can be part of Persian, Arabic, Indic, and other writing systems.
- Joiners and variation selectors can determine an emoji's appearance or sequence.
- Directional marks can make mixed right-to-left and left-to-right text readable.
- Nonbreaking, narrow, figure, or ideographic spaces can preserve layout and number/unit relationships.
- Combining marks and language-specific selectors can distinguish written forms.

Inspect suspicious zero-width insertions inside ordinary words, stray copy/paste controls, and lookalike characters in context. Remove only an identified artifact whose removal preserves the intended text. If its purpose is unclear, retain it or ask a focused question. Do not treat every invisible or non-ASCII character as an AI mark.

Avoid blanket ASCII conversion, compatibility normalization, homoglyph substitution, or removal of all format characters. In technical prose, a minus sign, superscript, unit symbol, or exact identifier may be load-bearing. Punctuation preferences are separate from hidden-character hygiene.

## Rewrite within the brief

When the user authorizes a substantial rewrite, change how the argument is expressed: paragraph function, clause order, sentence boundaries, and genuinely redundant transitions. Keep the original language, facts, evidence, limitations, required order, and author stance. A sequence required by the method stays in that sequence.

Replacing a few synonyms or punctuation marks does not establish that a token-sampling watermark was removed. A substantive rewrite can change a statistical signal, but a watermarked generation process may introduce a new one. Do not promise a particular effect on textGrain, SynthID, or a commercial classifier without a compatible test.

Use one source-checked revision, then repair actual remaining problems. Do not recursively paraphrase a satisfactory report to chase a number, shuffle its paragraphs randomly, or back-translate it without a translation brief. Extra passes can change the scientific claim while leaving a detector signal unresolved.

If alternatives are requested, reject versions that change meaning before comparing style. Choose by the user's brief and readability. Word-change distance, embedding similarity, and sentence-length variation do not establish factual equivalence; a single negation or source attachment can matter more than many preserved words.

## Inspect the result and describe only what happened

After an authorized cleanup, re-inspect the final file for the targeted artifacts and check protected spans. Record actual changes if an audit was requested. A result with no relevant character hits is a statement about that inspection, not a watermark-free certificate.

For a chat-only answer, do not claim a deterministic filter ran on the delivered message. If the tool cannot inspect the final raw representation, state that limit when reporting a character audit. Ordinary prose-only output does not need an appended checklist.

When an audit is requested, distinguish character edits, the prose rewrite, any actual detector test, and anything not verified. Report the detector/version, final text, supported configuration, language, and threshold only if a test really ran. Do not invent a before/after score or submit text to a service without authorization.

## Optional read-only audit helper

For actual UTF-8 files, `scripts/text_audit.py` provides an offline inspection and a protected-literal check. It uses Python 3.10+ and the standard library, changes no input file, performs no normalization, and calls no model or network service. Ordinary editing does not require it.

Run from the installed skill directory, replacing `python` with an existing Python launcher when needed:

```sh
python scripts/text_audit.py inspect report.txt
```

The JSON report identifies selected Unicode format/control characters, unusual spaces, selectors, private-use characters and Latin/Cyrillic/Greek mixtures. Offsets are zero-based Unicode code points; lines and columns are one-based. This is a review list: an emoji joiner, Persian non-joiner, mathematical formatting character or nonbreaking space may be necessary. A result with no findings covers only the stated inspection scope. Encoded HTML entities, statistical watermarks and document containers are not inspected.

For a revision with exact protected material, prepare a UTF-8 JSON manifest:

```json
{
  "source_sha256": "SHA-256 of the actual source file bytes",
  "literals": ["I = Is exp(V/(n Vt))", "10.0 mA", "[2]"]
}
```

```sh
python scripts/text_audit.py compare original.txt revised.txt --protect protected.json
```

Select source-backed equations, full technical definitions, identifiers, citations or verbatim passages that really must remain exact. The helper binds the manifest to the original file hash, escapes literals, and checks their counts with word-edge boundaries. It does not compare their order, attachments, causal role or surrounding negations. Protecting isolated numbers cannot establish that their associations survived. Complete the normal bidirectional claim and readability review even when every literal passes.

Exit codes are `0` for no findings or matching literal counts, `1` for review findings or a literal mismatch, and `2` for invalid input. None is an AI-authorship verdict. Reports go only to stdout; save them through the host's normal file workflow when requested. Inputs must be valid UTF-8 and at most 4 MiB; the manifest is limited to 64 KiB and 128 nonempty, unique literals. PDF, DOCX, binary files and UTF-16 need their appropriate extraction workflow first. The source hash and findings refer to the exact bytes inspected; do not apply a report to a later edit.

If the user authorizes character removal, review individual hits and make the smallest justified edit with the available editor, then inspect the actual final file again. This helper deliberately offers no blanket cleaning or global post-write hook.

## Source and scope

The separation of cleanup and rewriting, inspection before/after, and multilingual preservation checks were adapted from the MIT-licensed [watermarks-remover project](https://github.com/guillaumemeyer/watermarks-remover/tree/5c180932a00c793261177f79aee21db8929f3fe2), reviewed on 29 October 2026. The guidance is written for this skill; no upstream code or scripts are bundled. The upstream copyright notice is retained in [LICENSE](../LICENSE).

Its [SynthID benchmark documentation](https://github.com/guillaumemeyer/watermarks-remover/blob/5c180932a00c793261177f79aee21db8929f3fe2/docs/synthid-text-benchmark.md) describes a controlled MarkLLM reimplementation. That does not establish failure of Google's production detector or removal of textGrain. Its stylometry estimator, lexical-distance selection, and broad punctuation rules are not adopted as quality gates here. A provider-specific removal experiment was not run as part of this integration.

The 4 November 2026 refresh reviewed watermarks-remover at [`5a62be6338`](https://github.com/guillaumemeyer/watermarks-remover/tree/5a62be6338d2812372b1da440e55c82922f97d53). Only three dependency pins differed from the earlier reviewed revision; its text-cleaning and rewriting code had not changed. The new helper implements an independent, read-only version of the inspection-before/after principle. It does not bundle or launch the upstream service, hooks or removal engine.

The editing checks for paragraph purpose, unnecessary additions and unnecessary replacements draw on MIT-licensed [Sepia 0.13.0](https://github.com/Nanako0129/sepia/tree/0eb11d6c64c962fcc35f596c167c6e38045d6cb8), especially its professional and style passes. These are editorial applications. Fiction structure findings are not evidence for an engineering-report prescription, and a detector's ability to classify a corpus does not validate a proposed rewrite.

[Turnitout](https://github.com/AhmadHassan-BTed/Turnitout-Humanizer/tree/133de29d215ff30089a53004971256165aed1462) was reviewed for its documented protected-span workflow. Its core engine is absent from the public tree and its license is proprietary. No Turnitout code, dictionaries or engine are bundled or copied. The helper's independently written literal comparison supports the common preservation requirement; it does not reproduce or verify that engine's detection claims.
