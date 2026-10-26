# Working on Humanizer

Use the Humanizer instructions in [SKILL.md](SKILL.md) when drafting or revising prose in this repository. Read the relevant editing, language, and genre references. Keep documentation in English. Preserve the language and exact contents of recorded source passages, quotations, and evaluation outputs.

Keep editorial claims tied to the evidence. Do not turn local LLM judgments into a scientific benchmark or treat an archive/install check as successful native-client execution. Preserve failed trials and explain corrections.

The runtime skill is shared by Codex and Claude Code. Keep client-specific setup in documentation or `agents/openai.yaml`; do not add provider-dependent tools to ordinary editing. Do not change active user installations while working on this repository unless requested.

Validate changes from the repository root:

```text
python scripts/validate_package.py
python -m unittest discover -s tests -v
python scripts/build_release.py
```

Keep private text, credentials, downloaded PDFs, local backups, and generated release files out of Git. A release archive belongs in `dist/`, which is ignored. See [CONTRIBUTING.md](CONTRIBUTING.md) for behavioral evaluation and publication practices.
