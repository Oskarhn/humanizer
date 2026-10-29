# Humanizer

A writing skill for **Codex and Claude Code**, with particular attention to reports, academic work, and English/Norwegian prose. It helps make the writing clearer while preserving facts, uncertainty, citations, and the author's voice.

English, Norwegian Bokmål, and Nynorsk have specific guidance. No Python, API key, or external service is required by the skill.

## Why choose this Humanizer?

Choose it when a fluent rewrite must preserve what the document actually establishes. Its instructions focus on decisions that matter in reports:

- **Keep the evidence intact.** A simulation stays a simulation. Missing data do not become proof that nothing happened. Measurements, units, citations, and qualifications stay attached to their claims.
- **Write natural Norwegian as well as English.** Dedicated guidance covers Bokmål/Nynorsk, decimal commas, compounds, English calques, and the writer's established word forms.
- **Keep the right register.** A methods section can remain formal. Useful passive voice, technical terms, headings, and conclusions can stay. There is no universal ban on particular words or punctuation.
- **Improve the argument before swapping words.** The skill examines paragraph purpose, repetition, and logical connections, then compares the revision with the source.
- **Match the author without inventing a persona.** Writing samples guide expression; they do not supply new experiences or opinions. The default result is one revised text, with an explanation when requested.
- **Handle character cleanup in context.** An optional inspection pass protects code, quotations, mathematical notation, and meaningful multilingual characters. It keeps Unicode cleanup separate from claims about statistical watermarks.

It is a good fit for technical and academic reports, school assignments, and other documents where precision matters. You can also use it for articles and emails. A clear passage may need almost no change.

## An example

**Before**

> During the implementation of the evaluation process, a simulation of the regulator was carried out. It showed 5.02 V at a load of 0.40 A. It is important to emphasize that no physical prototype has been tested. These results should therefore be viewed as preliminary.

**After**

> The regulator simulation showed 5.02 V at a load of 0.40 A. No physical prototype has been tested, so the results remain preliminary.

The padding is removed; the values, simulation status, and limit on the result remain. [More worked examples](references/examples.md) show language, voice, and preservation decisions.

## How it compares

These are the orientations of the versions reviewed on 26 October 2026. Several alternatives also protect facts and voice; those ideas are not exclusive to this project.

| Skill | Particularly relevant when you want |
| --- | --- |
| **This Humanizer** | English/Norwegian report editing, explicit technical distinctions, and a simple default deliverable |
| [Academic Humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | A workflow focused on English papers and funding proposals |
| [Hannsxpeter](https://github.com/hannsxpeter/humanizer) | Detailed voice matching, restraint checks, and an editing report |
| [Blader](https://github.com/blader/humanizer) | A broad catalog of AI-writing patterns and examples |
| [Milock](https://github.com/milock/humanizer) | Channel-specific editing and author/brand profiles |
| [Stop Slop](https://github.com/hardikpandya/stop-slop) | A short, strongly prescriptive style guide |

The local comparison did **not** establish this skill as the universal winner. Academic Humanizer and Hannsxpeter had no recorded fidelity issues in fourteen tasks; this project's older 1.1.0 had one minor issue. The reason to choose it is the combination of language coverage, document-specific preservation rules, and output style. Read the [comparison and its limits](COMPARISON.md) before treating the numbers as a ranking.

The [background](BACKGROUND.md) explains the editing workflow and how research informed it. Neither page requires you to download the development files or test data.

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

For a character audit or detector-focused task, say what you want checked. The [text-hygiene reference](references/text-hygiene.md) explains the extra pass and what its results can establish. It does not add a background service or automatic metadata removal.

```text
Use humanizer to inspect this report for unintended hidden characters.
Preserve code, quotations, equations, and meaningful language characters.
Keep all claims if you rewrite, and tell me what was actually checked.
```

Both clients can select the skill automatically when relevant. Name it explicitly when you want to ensure it is requested. A local installation does not upload the skill to Claude.ai or another cloud account.

## Update

From the installed `humanizer` directory, review any local changes, then run:

```sh
git pull --ff-only
```

## What is included

[SKILL.md](SKILL.md) contains the workflow. The five files in `references/` cover editing decisions, language and voice, genres, examples, and optional text hygiene. `agents/openai.yaml` supplies Codex display metadata.

The skill improves writing; it does not certify authorship, guarantee undetectability, or verify watermark removal. Research notes and earlier evaluations remain in the [project history](https://github.com/Oskarhn/humanizer/tree/304f74ebe1c57e5b58bed384cb286e20206eb950).

[MIT license](LICENSE).
