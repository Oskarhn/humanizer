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

## Source and scope

The separation of cleanup and rewriting, inspection before/after, and multilingual preservation checks were adapted from the MIT-licensed [watermarks-remover project](https://github.com/guillaumemeyer/watermarks-remover/tree/5c180932a00c793261177f79aee21db8929f3fe2), reviewed on 29 October 2026. The guidance is written for this skill; no upstream code or scripts are bundled. The upstream copyright notice is retained in [LICENSE](../LICENSE).

Its [SynthID benchmark documentation](https://github.com/guillaumemeyer/watermarks-remover/blob/5c180932a00c793261177f79aee21db8929f3fe2/docs/synthid-text-benchmark.md) describes a controlled MarkLLM reimplementation. That does not establish failure of Google's production detector or removal of textGrain. Its stylometry estimator, lexical-distance selection, and broad punctuation rules are not adopted as quality gates here. A provider-specific removal experiment was not run as part of this integration.
