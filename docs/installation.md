# Installation

Humanizer is a directory-based skill. The same files work in Codex and Claude Code; no Python package, API key, hook, or MCP server is required for ordinary editing.

## Choose one installation per client

| Client and scope | Directory containing `SKILL.md` |
| --- | --- |
| Codex, personal | `~/.agents/skills/humanizer` |
| Codex, project | `<project>/.agents/skills/humanizer` |
| Claude Code, personal | `~/.claude/skills/humanizer` |
| Claude Code, project | `<project>/.claude/skills/humanizer` |

These locations follow the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills), checked on 26 October 2026. An existing client may also discover skills from another configured or legacy directory, such as `~/.codex/skills`. Check the client's skill list before adding a second copy.

A personal install is available across local projects. A project install can be committed for that team. Managed settings and client-specific visibility rules can restrict discovery.

## Get the files

Use a release ZIP built by this repository. It contains one top-level `humanizer` folder. Extract it to a temporary or downloads directory, then install that folder using the commands below. The examples start in the directory containing the extracted folder.

If you have a Git checkout, you can build the same package:

```text
python scripts/build_release.py
```

The archive and SHA-256 checksum appear in `dist/`. Build tooling needs Python 3.10 or later; using a downloaded skill does not. You can also copy the checkout's files while omitting `.git`, caches, and `dist/`.

Keep the directory structure intact. A correct installation has `humanizer/SKILL.md`, `humanizer/references/`, and the other packaged resources directly under `humanizer`, without another nested `humanizer` folder.

## Windows PowerShell

For a personal Codex install:

```powershell
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$destination = Join-Path $skillParent 'humanizer'
if (Test-Path -LiteralPath $destination) {
    throw 'Humanizer already exists here. Back it up before updating.'
}
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
Copy-Item -LiteralPath '.\humanizer' -Destination $destination -Recurse
Get-Item -LiteralPath (Join-Path $destination 'SKILL.md')
```

For native Windows Claude Code, use `.claude\skills` for `$skillParent` instead. For a project install, use that project's `.agents\skills` or `.claude\skills` directory. The existing-directory check is intentional: these commands do not overwrite a prior installation.

## Linux, macOS, or WSL

For a personal Codex install:

```sh
skill_parent="$HOME/.agents/skills"
if [ -e "$skill_parent/humanizer" ]; then
    printf '%s\n' 'Humanizer already exists here. Back it up before updating.' >&2
else
    mkdir -p "$skill_parent"
    cp -R ./humanizer "$skill_parent/humanizer"
    test -f "$skill_parent/humanizer/SKILL.md"
fi
```

For Claude Code, set `skill_parent="$HOME/.claude/skills"`. For a project installation, use the corresponding directory in the project instead.

Run the commands in the environment that runs the client. If a Windows shortcut launches Claude inside WSL, the effective personal directory is the Linux account's `~/.claude/skills`. A copy in the Windows profile alone does not establish discovery by that Linux process.

## Confirm discovery

Start a fresh session if the skill does not appear. In Codex, select or mention `humanizer` through the skill picker or `$humanizer`. In Claude Code, look for `/humanizer` in the command menu.

Try this synthetic check:

```text
Use humanizer to lightly edit this for a technical report. Return only the text:
It is important to note that the simulation returned 5.08 V at 0.25 A.
No physical prototype has been tested.
```

The result should retain both values, simulation status, and the untested prototype. A folder existing on disk does not prove that a running session loaded it. If authentication fails before the model runs, fix the client login separately.

## Update

Keep a copy of the old installation outside any active skill-discovery directory. Close sessions that are using it, move the old directory to your backup location, then install the new folder at the original path. Check the skill list and run the small example again.

Do not keep backups under another active skill folder name; a client may discover both. Do not overwrite one client's copy and assume a separate Windows, WSL, or project installation changed too.

## Remove

Remove only the `humanizer` directory you installed, after backing up anything you want to retain. Review personal and project locations separately. Installation and removal do not edit `AGENTS.md`, `CLAUDE.md`, account settings, or another client's skills.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Skill is absent | Effective client environment, installation path, one extra directory level, and a fresh session |
| Two versions appear | Personal, project, legacy, and configured skill roots |
| It is not selected automatically | Give the task clearly or invoke the skill explicitly; automatic matching is a model decision |
| Only part of it works | Supporting files were copied with `SKILL.md` |
| Claude reports authentication failure | The client account, independently of the skill files |
| It works locally but not in a cloud session | Cloud/account skills are a separate distribution surface; consult the provider's current documentation |
