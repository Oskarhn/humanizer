# Humanizer

Humanizer is a writing skill for **Codex and Claude Code**. It helps an agent draft or revise clear, natural prose while preserving facts, uncertainty, citations, and the author's voice.

Use it for reports, academic writing, articles, emails, or a draft that sounds generic. It supports English, Norwegian Bokmål, and Nynorsk explicitly. Documentation is in English; multilingual examples and evaluation data retain their source language.

The skill works without Python, an API key, a detector, or network access. The optional local review and release tools need Python 3.10 or later. Your host model still runs under its own client's permissions and data policies.

## Download with Git

```sh
git clone https://github.com/Oskarhn/humanizer.git humanizer
```

This downloads the source into a `humanizer` directory. To install directly into Codex or Claude Code, use the [client-specific Git commands](docs/installation.md#install-with-git).

## Start here

Install the `humanizer` folder in your client's skill directory. Keep the supporting files with `SKILL.md`; copying that file alone leaves its references unavailable.

| Client | Personal skill directory | Explicit use |
| --- | --- | --- |
| Codex | `~/.agents/skills/humanizer` | `Use $humanizer to revise this report.` |
| Claude Code | `~/.claude/skills/humanizer` | `/humanizer Revise this report.` |

On Windows, `~` means your user profile. In WSL, use the Linux home of the account running the client. Existing Codex setups may use a different discovered skill directory; keep one active copy per client rather than installing duplicate versions.

See [installation](docs/installation.md) for Windows, Linux, macOS, WSL, project installs, updates, and removal. These are local Codex/Claude Code instructions; a local installation does not upload the skill to Claude.ai or another cloud account.

Both clients can select a relevant skill automatically. Naming it explicitly is the most reliable way to request it for a particular task:

```text
Use $humanizer to edit this technical report in natural English.
Keep the measurements, citations, uncertainty, and formal register.
Return only the revised report.
```

```text
/humanizer Review this discussion section. Do not rewrite it yet.
Identify unsupported claims, unclear reasoning, and awkward phrasing.
```

You can also ask for a new draft from supplied facts:

```text
Use humanizer to draft a conclusion from these test notes.
Keep completed measurements separate from planned tests.
Do not invent results or resolve the unanswered questions.
```

For voice matching, supply a few comparable paragraphs you actually wrote. The skill borrows observable language choices, not the sample author's experiences or opinions. See [usage](docs/usage.md) and [examples](references/examples.md).

## What changes, and what stays

Humanizer examines the argument and organization before replacing words. It removes empty framing, repairs awkward syntax, and adjusts the level of editing to the request. A clear passage can remain unchanged.

Meaning comes first. A simulated result stays simulated. A suggestion stays a suggestion. Missing evidence does not become proof that nothing happened. Necessary terminology, passive constructions, headings, and conclusions can stay when they serve the document.

Humanizer does not classify authorship or guarantee undetectability. A natural-sounding rewrite, an AI-detector response, and a statistical watermark test are different outcomes. The [research review](references/evidence.md) and [watermark reference](references/watermarks-and-provenance.md) explain the evidence and its limits.

## Optional local check

For plain text or Markdown, the supplied script can flag changed literal numbers, links, citations, and code:

```text
python scripts/review_text.py revised.md --original original.md
```

It reads the files and prints a report. It does not rewrite, upload, or score them for AI authorship. It can miss a reversed claim and flag an equivalent number format, so a manual source comparison remains necessary. See the [script guide](scripts/README.md) for locks, supported formats, and exit codes.

## Repository guide

| Resource | What it explains |
| --- | --- |
| [SKILL.md](SKILL.md) | The shared editing contract and workflow |
| [Installation](docs/installation.md) | Client paths, installation, updates, and troubleshooting |
| [Usage](docs/usage.md) | Drafting, editing depth, review, voice, and automatic selection |
| [Architecture](docs/architecture.md) | How the files fit together and which ones the agent reads |
| [Research](references/evidence.md) | Twenty-two evidence/documentation entries, with source limits |
| [Evaluation guide](evals/README.md) | Behavioral cases and how to run a meaningful comparison |
| [Evaluation record](docs/evaluation.md) | Observed outcomes, failures, and untested claims |
| [Repository validation](docs/repository-validation.md) | Local platform checks and what they establish |
| [External-skill comparison](evals/comparison-2026-10-26/README.md) | The 98-output comparison and its raw artifacts |
| [Publishing](docs/publishing.md) | Validation, reproducible release archives, Git tags, and GitHub publication |
| [Contributing](CONTRIBUTING.md) | Development commands and useful bug reports |
| [Security and privacy](SECURITY.md) | What runs locally, what is shared, and how to report a problem |
| [Changelog](CHANGELOG.md) | Recorded changes through 1.1.1 |

## Development

Run these commands from the repository root:

```text
python scripts/validate_package.py
python -m unittest discover -s tests -v
python scripts/build_release.py
```

The build writes a versioned skill ZIP and checksum to `dist/`. It includes a manifest of the packaged files. Unit tests check the scripts and packaging; they do not measure writing quality. The checked-in GitHub workflows are configuration, not evidence that hosted CI has run.

## License and evidence

The project's original instructions, code, fixtures, and teaching examples use the [MIT license](LICENSE). Research papers and external projects retain their own licenses. Source PDFs, private documents, credentials, and downloaded third-party repositories are not bundled.

The evidence was reviewed on 25–26 October 2026. No cited study validates this entire skill. Recorded LLM evaluations are local regression checks, not a human preference study or a scientific detector-evasion result.
