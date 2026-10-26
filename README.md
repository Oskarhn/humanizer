# Humanizer

A writing skill for **Codex and Claude Code**. Draft or revise natural prose while preserving facts, uncertainty, citations, and the author's voice. Use it for reports, academic writing, articles, and emails.

English, Norwegian Bokmål, and Nynorsk have specific guidance. No Python, API key, or external service is required by the skill.

## Install with Git

Choose the command for your client. The destination must not already contain an installation.

**Linux, macOS, or WSL:**

```sh
# Codex
git clone --depth 1 https://github.com/Oskarhn/humanizer.git "$HOME/.agents/skills/humanizer"

# Claude Code
git clone --depth 1 https://github.com/Oskarhn/humanizer.git "$HOME/.claude/skills/humanizer"
```

**Windows PowerShell:**

```powershell
# Codex
git clone --depth 1 https://github.com/Oskarhn/humanizer.git "$env:USERPROFILE\.agents\skills\humanizer"

# Native Windows Claude Code
git clone --depth 1 https://github.com/Oskarhn/humanizer.git "$env:USERPROFILE\.claude\skills\humanizer"
```

If Claude runs in WSL, install inside WSL. Check for an existing copy in another discovered skill directory before adding one. Start a fresh client session if the skill does not appear.

You can also download the [release ZIP](https://github.com/Oskarhn/humanizer/releases/latest), extract it, and copy the `humanizer` folder into the appropriate skill directory shown above.

To download the files without installing them:

```sh
git clone --depth 1 https://github.com/Oskarhn/humanizer.git
```

## Use it

**Codex:**

```text
Use $humanizer to revise this report. Keep the technical detail,
numbers, citations, and uncertainty. Return only the revised text.
```

**Claude Code:**

```text
/humanizer Revise this report. Keep the technical detail,
numbers, citations, and uncertainty. Return only the revised text.
```

You can request a light edit, a deep rewrite, a review without rewriting, or a new draft from supplied facts. Add a writing sample when matching your own voice matters.

Both clients can select the skill automatically when relevant. Name it explicitly when you want to ensure it is requested. A local installation does not upload the skill to Claude.ai or another cloud account.

## Update

From the installed `humanizer` directory, review any local changes, then run:

```sh
git pull --ff-only
```

## What is included

[SKILL.md](SKILL.md) contains the workflow. The four files in `references/` provide editing decisions, language and voice guidance, genre guidance, and worked examples. `agents/openai.yaml` supplies Codex display metadata.

The skill improves writing; it does not certify authorship, guarantee undetectability, or verify watermark removal. Research notes and earlier evaluations remain in the [project history](https://github.com/Oskarhn/humanizer/tree/304f74ebe1c57e5b58bed384cb286e20206eb950).

[MIT license](LICENSE).
