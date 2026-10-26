# How the repository fits together

Humanizer has one shared instruction entrypoint, [SKILL.md](../SKILL.md). Codex and Claude Code can load that file with its supporting resources. There is no daemon, model checkpoint, service account, or provider API integration in the package.

## Discovery and loading

The name and description help the host decide whether the skill fits a request. When selected, the host reads the instructions. References are loaded when their topic is relevant; the full research review is not part of every copyedit.

`agents/openai.yaml` supplies Codex display metadata and a default prompt. It does not contain a second editing workflow or disable automatic selection. Claude Code uses the shared SKILL.md; this repository needs no separate slash-command file, plugin wrapper, or MCP server.

The root [AGENTS.md](../AGENTS.md) and [CLAUDE.md](../CLAUDE.md) guide agents working on the repository itself. They are contributor instructions, not substitutes for installing the skill in a consuming project.

## Runtime references

| File | Read when |
| --- | --- |
| [editing.md](../references/editing.md) | A standard or deep edit needs concrete editorial decisions |
| [languages-and-voice.md](../references/languages-and-voice.md) | Language variety or a supplied author sample matters |
| [genres.md](../references/genres.md) | The task is academic, technical, business, journalistic, or creative prose |
| [examples.md](../references/examples.md) | A difficult before/after decision needs a demonstration |
| [evidence.md](../references/evidence.md) | A research claim or disputed rule needs its source and limitations |
| [watermarks-and-provenance.md](../references/watermarks-and-provenance.md) | The user asks about a statistical watermark, provenance, or cleanup claim |

The source manifests identify supplied PDFs and the additional provenance reading. They support the research record. They do not require readers to possess those local files, and they do not redistribute them.

## Editing workflow

The four passes establish protected meaning, diagnose the largest problems, revise, then compare the result with the source. The source comparison protects uncertainty, attribution, obligations, citations, and the status of the work.

The workflow permits different registers and editing depths. It does not require a quota of fragments, a fixed sentence-length pattern, or a ban on ordinary words. Drafting uses the supplied facts; review-only work identifies issues without silently replacing the text.

## Optional tools and evaluation

- [review_text.py](../scripts/review_text.py) reports literal changes and a few places to inspect in plain text or Markdown.
- [validate_package.py](../scripts/validate_package.py) checks structure, local documentation links, source-record shape, and fixture shape.
- [build_release.py](../scripts/build_release.py) produces an archive and checksums from an explicit set of release directories and files.
- `tests/` checks the tools. `evals/` contains synthetic behavior cases, historical outputs, and their reviews.
- `.github/workflows/` contains hosted validation and release configuration. Adding those files does not run GitHub Actions locally.

The text-review tool is not part of the model's ordinary editing requirement. Its clean result does not establish meaning, quality, authorship, or watermark absence.

## Version boundaries

The editorial version is in SKILL.md metadata. The release builder reads that version. Root documentation and release tooling prepare the source package; they do not retroactively change the version used for a recorded evaluation.

The 98-output comparison used a local **1.1.0** snapshot. The five paired maintenance regressions compared **1.1.0 and 1.1.1**. Preserve those labels even though both records are distributed with the current repository.
