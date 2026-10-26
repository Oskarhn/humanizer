# Publishing a skill release

This repository is a standalone Agent Skill for Codex and Claude Code. Its public source can be hosted in an ordinary Git repository. A plugin marketplace wrapper is not required for directory-based installation.

Creating a local commit, creating a GitHub repository, and publishing a release are separate actions. The commands below describe publication; they do not mean those remote actions have already happened.

## Prepare the version

Read the version from SKILL.md metadata. Keep the changelog, release notes, and any new evaluation record consistent with that version. Do not relabel old outputs after changing the instructions.

Run from the repository root:

```text
python scripts/validate_package.py
python -m unittest discover -s tests -v
python scripts/build_release.py
```

The build produces `dist/humanizer-v1.1.1.zip` and `dist/humanizer-v1.1.1.zip.sha256` for the current version. Future versions use their own metadata value. The ZIP contains a `humanizer/` directory and a `RELEASE-MANIFEST.json` listing each source member's SHA-256 hash.

The archive is deterministic for the same input bytes and compression implementation: paths are sorted, timestamps and file modes are fixed, and no local time or user path is embedded. Git's LF text policy helps keep checkout bytes consistent. Different zlib versions can produce different compressed bytes; the member hashes remain useful independently.

The builder excludes Git history, caches, local runs, release outputs, PDFs, and archives. It rejects symlinks and unsupported file types in the selected release files. It does not overwrite a different existing release artifact; use a new output directory or intentionally manage an old local artifact yourself. Matching existing output is left intact.

## Review the artifact

Extract it into a temporary directory. Run its own package validator and inspect its root layout. Check that the source examples, evidence, license, and documentation are present. Confirm that no private text, credentials, local installation logs, downloaded external skills, or source PDFs entered the release.

The SHA-256 checksum and embedded manifest detect changes relative to their values. They are integrity records, not digital signatures proving who built the files.

## Create the remote repository

Choose the owner, name, and visibility explicitly. A public repository exposes committed files and history. Set the description to the actual capability, such as:

> A prose-editing skill for Codex and Claude Code that preserves facts, uncertainty, citations, and author voice.

Keep the root SKILL.md and supporting directories intact. Point installation links and repository topics at the actual hosted URL after it exists. Useful topics include `agent-skills`, `codex`, `claude-code`, `writing`, and `humanizer`.

Push the reviewed `main` branch to that repository using your normal Git workflow. The validation workflow runs on pushes and pull requests. Inspect the hosted result before calling it a passing CI run.

## Tag and publish

The release workflow runs when a `v*` tag is pushed. It validates the package, runs unit tests, checks that the tag matches the version, builds the archive, and creates a GitHub Release with the ZIP and checksum. It requires the repository's workflow token to have release-write permission, which the workflow requests.

For the current version:

```sh
git tag -a v1.1.1 -m 'Humanizer 1.1.1'
git push origin main
git push origin v1.1.1
```

If the tag already exists locally, verify that it points to the intended commit instead of recreating it. Pushing the tag is the publication step; do it after reviewing the actual repository and archive. Check the resulting Actions run and release page.

The initial repository comes with [release notes](release-notes/1.1.1.md). Add a matching notes file under `docs/release-notes/` for each later version. Hosted CI and repository permissions can still prevent publication; a local build does not establish that the remote release exists.

## Other distribution surfaces

Codex and Claude Code users can install the extracted directory using [installation](installation.md). Publishing on GitHub does not submit it to a curated directory, create a plugin listing, or upload it to Claude.ai. Follow each service's current submission or account-upload instructions if you choose to distribute there.

## Preserve the repository itself

A skill ZIP contains source files but not Git history. To transfer commits and tags without a remote:

```text
git bundle create dist/humanizer-repository.bundle --all
git bundle verify dist/humanizer-repository.bundle
```

A recipient can clone that bundle into a new checkout. Keep the bundle outside the tracked source; `dist/` is ignored.
