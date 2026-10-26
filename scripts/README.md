# Optional local text review

`review_text.py` uses Python 3.10+ and the standard library. It reads UTF-8 plain text or Markdown, optionally compares an original, and prints a report. It never rewrites the document, contacts a service, or computes an AI/human score.

From the skill directory:

```text
python scripts/review_text.py revised.md --original original.md
python scripts/review_text.py revised.txt --original original.txt --locks constraints.json --format text
```

Use `-` for one stdin input when convenient. The script accepts `.txt`, `.md`, and `.markdown`; extract other formats with an appropriate tool first. Inspect extraction quality, especially tables and citations. Do not mistake PDF line-wrap artifacts for author style.

Optional lock file:

```json
{
  "required_literals": ["42 users", "may indicate", "[7]"],
  "forbidden_literals": ["proves causation"],
  "min_words": 100,
  "max_words": 180
}
```

These are user-chosen constraints, not universal style targets. Required strings must appear at least once; they do not enforce exact occurrence counts or source-to-claim attachment. For exact quotations or legally fixed wording, put the complete protected span in `required_literals`. Matching is case-sensitive and whitespace-sensitive. Empty strings, invalid lengths, and unknown lock keys are rejected.

With an original, the script compares multisets of:

- Literal numeric tokens, including many signed, decimal, percentage, and scientific forms.
- HTTP(S) URLs, with common closing punctuation trimmed.
- Numeric bracket citations, Pandoc-style citation groups beginning with `@`, and Markdown footnote references.
- Fenced code blocks and backtick inline-code contents.

It also locates a small set of often-empty introductory phrases, repeated substantial paragraphs, and selected invisible/directional characters outside fenced code. These are places to inspect, not errors or signs of authorship. Legitimate repeated text and directional characters may be necessary in a multilingual document. The script does not identify all Unicode confusables.

An invisible-character flag is not evidence of SynthID or textGrain. Those statistical signals do not depend on added hidden characters. Removing a flag, changing punctuation, or exporting plain text does not verify watermark removal. This script has no provider key or compatible watermark test; see [watermarks and provenance](../references/watermarks-and-provenance.md).

Exit codes:

| Code | Meaning |
| --- | --- |
| 0 | No automatic flags; manual fidelity review is still required |
| 1 | Review flags present; inspect in context |
| 2 | Invalid input, configuration, or unreadable file |

## Important limits

“20%” to “20 percent” is a literal difference even if semantically equivalent. “Did not improve” to “improved” may pass these checks despite changing meaning. The same two numbers can trade places and preserve their multiset. Units, names, negations, actor identity, author-year citations, equations, table semantics, and reference attachment require manual review or explicit locks. Indented code, embedded HTML, unusual Markdown, and LaTeX are not fully parsed. This is a deliberately small aid, not a document parser or semantic validator.

Reports may contain source text, quotations, URLs, and code from the user's files. Keep them local unless the user authorizes sharing. “Offline” here describes this script; the host language model's data handling is governed by its client and provider.

`validate_package.py` is a separate maintainer check for package structure, local links, source-manifest shape, and evaluation-case shape. It neither executes a writing model nor assesses prose quality.

## Release tooling

`build_release.py` packages the selected repository files into a skill ZIP and writes a SHA-256 checksum. It adds a member-hash manifest inside the archive, fixes metadata used in ZIP creation, and refuses to replace a different existing artifact. It does not install the skill or publish a release.

```text
python scripts/build_release.py
python scripts/build_release.py --output-dir dist/review --check-tag v1.1.1
```

Use the actual version in SKILL.md for a tag check. See [publishing](../docs/publishing.md) for package contents, extraction checks, the determinism limit, and GitHub release steps.
