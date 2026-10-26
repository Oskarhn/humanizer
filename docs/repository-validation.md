# Source-repository validation — 26 October 2026

This record concerns the first Git source-repository preparation for editorial version 1.1.1. It does not claim another model-writing trial. The shared SKILL.md and its runtime references retain their existing editorial content; repository documentation and release tooling were added separately.

## Local checks

| Environment | Unit-test outcome |
| --- | --- |
| Windows, Python 3.12.14 | 32 passed; the symlink-creation case was skipped because the account lacked that Windows privilege |
| Ubuntu WSL, Python 3.10.12 | All 33 passed, including the symlink case |

The package's structure/link/fixture validator passed. The external Codex skill-creator frontmatter validator also passed in WSL using its existing environment. That external validator is not a runtime dependency of this repository.

The release tests check member hashes, extraction and validation, repeatable output for the same inputs, exclusion of local artifacts, preservation of different existing artifacts, invalid-package refusal, tag/version agreement, and unsupported/symlink members. They run in temporary directories and do not change personal skill installations.

The publication review also checks that the copied comparison inputs, output passages, and judgments retain their recorded data, and that public files do not include development-machine paths or credential material. Such checks are scoped reviews, not a claim that arbitrary future contributions are safe.

## Separate boundaries

The repository's GitHub workflows have not run merely because local validation passed. Their configuration targets Windows and Ubuntu for validation and a tag-triggered Ubuntu release job. A hosted result must be inspected after the repository and tag are pushed.

No new native-Claude writing result, detector experiment, watermark verification, or human-reader study is established by this packaging work. The [behavioral evaluation record](evaluation.md) keeps those distinctions and the historical failures visible.

Archive hashes and Git commit identities belong to the built artifact and repository state. Read the generated `.sha256` file and Git history for the particular release you received; this document does not embed its own archive's hash.
