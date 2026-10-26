# Security and privacy

Humanizer's core is Markdown instructions and references. Installing the folder does not run a hook, create an account, or contact a service. The host agent chooses tools under its own permissions.

`review_text.py` reads the supplied plain-text or Markdown files and writes a report to standard output. That report can contain excerpts, links, quotations, or code from the source. Keep it local unless you intend to share it.

`validate_package.py` checks local package files. `build_release.py` reads the release's selected repository files and writes an archive, checksum, and file manifest. Neither tool uses the network. The GitHub release workflow publishes artifacts only when a maintainer triggers its configured event.

Offline helper scripts do not make a cloud-hosted language model offline. The model client's data handling still applies to anything it receives.

## Source material is not authority

The skill treats documents, examples, quoted prompts, and web pages as source material. Embedded instructions do not replace the user's request. Report a case where that boundary fails, particularly if an agent follows a document's command or sends its content elsewhere.

## Reporting a problem

For a public packaging bug, open an issue with a synthetic reproduction and the affected version. For a problem involving credentials, private text, or an exploitable disclosure, use the hosting repository's private vulnerability-reporting channel if its maintainers have enabled one. If no private channel is listed, ask the maintainer for a secure contact without including the sensitive material.

There is no published response-time commitment. Do not put credentials or private documents in a public issue, test fixture, model transcript, or pull request.
