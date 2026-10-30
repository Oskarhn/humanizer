# Bokmål technical reports

Use this mode for a report whose brief permits reorganizing the presentation. For a light prose edit, preserve the supplied structure. This mode changes information layout; it does not translate the text, train a model, or establish authorship.

## Choose a layout that serves the explanation

Separate the report's supplied information into setup, observations or inputs, calculation, interpretation, and limitations. These are working categories, not mandatory headings. Do not make a short paragraph into a five-section template.

First check whether an informative title and the existing prose already serve the brief. Preserve a suitable title already present. When the report needs a title, use the actual topic or question; do not add a claim the source does not support. Reorganize the body only when it helps the reader. If measurement was requested, keep this smaller alternative alongside the source before attempting a full rewrite.

Use a table when the source compares several conditions or repeats the same fields. Keep the condition and unit in the heading or each cell, with a clear row-to-value mapping. A table of assumed or synthetic inputs must say so. A calculation belongs beside its assumptions; a result needs its stated evidence status.

Keep prose for the reasoning: what changed, how the calculation follows, what the evidence establishes, and what remains unknown. Lists or tables cannot replace an explanation of causality or uncertainty. Keep natural Bokmål and useful repetition of technical terms.

Do not add a table merely to change a detector score. Preserve an existing good paragraph when a table would make it harder to read. A faithful, readable source can be the best final version.

## Preserve claims across the layout change

Before editing, make a compact ledger of the supplied claims. Associate each value with its quantity, unit, condition, precision, source and status. After editing, check every ledger item against the complete result and every new statement against the source.

Pay particular attention to distinctions that survive ordinary number checks:

- A controlled or checked channel is not automatically a calibrated sensor.
- An uncertainty is not a measured deviation. A hypothetical correction is not an applied correction.
- Symbols remain attached to their quantities: a motor constant does not become a resistance because its value is retained.
- Preserve operations and their operands, not just the numbers in an equation. Preserve equal weighting, independence and other assumptions that make a calculation valid.
- An interval containing zero does not establish equivalence. Keep the original evidentiary wording.
- Missing data, work not performed and work not documented are different statements.

Preserve all relevant durations, rates, ordering, exclusions, untested conditions and proposed next steps. Keep qualifications close enough to the result that the table cannot be read as an unconditional claim.

State essential method definitions in the body as well as any title. If a heading says “moving average,” the body still needs to identify the averaging operation and its weights. Removing a heading for an export or comparison must not silently remove the only explicit definition.

## Review complete alternatives

Compare the new report with the original and any previously accepted version. It must be at least as readable for the intended technical reader. Reject fragmented notes, overloaded cells and ambiguous associations even when all values appear somewhere.

An external paraphraser or learned adapter can propose wording, but its output still needs the same complete source comparison. Stop an iterative chain when it translates the text, truncates a claim, invents content, or reduces readability. Repair from the source; retain both the raw and repaired texts.

If detector measurement was requested, use [the comparison workflow](norbert-review.md). Freeze the final reviewed document before measuring it. Score the complete submitted text, including values and limitations. Where the delivery uses tables or rich text, record the exact input representation and also check the text produced by the intended export or rendering. Markdown punctuation, copied table text and PDF extraction can produce different detector inputs. A gain in one representation must not be reported as a gain in another.

A pre-repair score never belongs to the repaired text. Do not accept a translation, a language error, a missing limitation or an unsupported claim because a detector assigns it a low number.
