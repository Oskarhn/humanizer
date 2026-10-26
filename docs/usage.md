# Using Humanizer

Tell the agent what you are writing, who will read it, and how much change you want. Supply the original text or the facts needed for a new draft. A brief that names the important constraints is more useful than asking for a high human score.

## Invoke it

In Codex:

```text
Use $humanizer to revise the report below. Keep the technical detail,
citations, and uncertainty. Return only the report.
```

In Claude Code, put the command at the start:

```text
/humanizer Revise the report below. Keep the technical detail,
citations, and uncertainty. Return only the report.
```

Ordinary wording such as “Use the humanizer skill” also communicates the request. Available selectors and command presentation depend on the client.

## Automatic selection

The skill description names documents, reports, articles, emails, and requests to revise AI-sounding prose. Automatic selection is allowed: there is no explicit-only setting in the supplied metadata. A client can choose it when the task matches that description, but relevance matching is not a guarantee that every report will load it.

For dependable task intent, name Humanizer at the start of a new writing task. You normally do not need to repeat that instruction for each correction to the same document. It is not a background service that rewrites every response or watches files.

If you want a standing project convention, add a scoped instruction to your own project's `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code:

```text
Use the humanizer skill when drafting or revising reports and other
substantial reader-facing prose. Preserve technical meaning and evidence.
```

The skill must also be installed where that client can discover it. A project instruction expresses a requirement; it does not install the files or certify that a model followed them.

## Choose the amount of editing

| Request | Expected work |
| --- | --- |
| Light edit | Repair local problems; keep good wording and structure |
| Standard edit | Improve reasoning flow, syntax, and tone within the existing brief |
| Deep rewrite | Reorganize expression and sections where useful; retain the argument and facts |
| Review only | Explain actual problems and suggest changes without replacing the document |
| Draft from notes | Write from supplied facts, keeping gaps and unresolved decisions visible |
| Match my voice | Use recurring traits in comparable samples without importing their biography |

“Deep” changes the expression and organization, not the evidence. The skill should not add a measurement, an experience, or a causal explanation just because it makes a paragraph more convincing.

## Academic and technical reports

```text
Use humanizer for a restrained edit of this methods section.
Keep equations, units, sample sizes, source-to-claim links, and limitations.
Do not add an operator where the source does not identify one.
```

Formality is compatible with natural prose. Passive voice can be appropriate when the procedure or unknown operator is the point. Stable component names can be clearer than several synonyms.

In engineering reports, specify whether values are calculations, simulations, bench measurements, or field observations. A better sentence cannot turn any of them into certification. Keep proposed tests separate from completed work.

## English, Bokmål, and Nynorsk

```text
Use humanizer to edit this in natural Nynorsk. Keep the language variety,
technical terms, decimal commas, and the limits of the simulation.
```

The source language stays unless you request a translation. English instructions do not require English output. A language-specific example is guidance for that language, not a reason to translate its wording into a blacklist elsewhere.

## Review without rewriting

```text
Use humanizer to review this discussion. Do not rewrite it yet.
Identify the three most consequential issues, quote the affected spans,
and explain what information or change would resolve each one.
```

A review should distinguish an awkward sentence from a claim needing new evidence. If the source has no baseline or measurement, the editor can identify that gap; it cannot supply a plausible result as though it were recorded.

## Files and protected material

Say whether you want replacement prose in chat or an actual file edit. For a document edit, name the file and the material to protect: quotations, formulas, code, tables, citation fields, headings, or a template.

The skill does not provide its own Word/PDF editor. The host needs an appropriate document workflow to preserve file formatting. If only extracted text was available, the agent should state that coverage rather than claim it verified the original layout.

## What a result establishes

Judge the revision against the original: does it say the same thing more clearly, in a voice and register that fit? A short passage may need almost no change.

Detector scores and statistical watermark verification are separate questions. Humanizer does not promise that a rewrite will pass a detector or carry no watermark. If those questions matter, read the [provenance reference](../references/watermarks-and-provenance.md) and agree on a separate evaluation scope.
