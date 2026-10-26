# Contributing

A useful change starts with a concrete problem: a qualification disappeared, a passage became harder to read, a client could not find the skill, or a local script reported the wrong result.

Include a small synthetic or shareable example, the request, the actual result, and the result you expected. Identify the client, model, skill version, and relevant settings when available. Remove personal information from reports. Do not supply an invented model identity when the client did not expose one.

## Work locally

Python 3.10 or later is sufficient for the supplied tools. They use the standard library; there is no package installation step.

```text
python scripts/validate_package.py
python -m unittest discover -s tests -v
python scripts/build_release.py
```

The [architecture guide](docs/architecture.md) explains the runtime files. Keep the core instructions focused. Put a substantial genre-specific decision in its relevant reference, and explain when the agent should read it.

Use Humanizer when writing documentation. Edit for clear reasoning and precise claims. Do not copy an external author's personal facts into a sample or turn a preferred wording into a universal language rule.

## Test the behavior you change

A structural check cannot show whether a rewrite preserved meaning. For an editorial change, add a realistic case to `evals/cases.json`, or use `evals/watermark-cases.json` for a provenance-reasoning case. Use a unique ID, source text, request, and explicit expectations.

Give the generator only the request and source. Have a separate reviewer compare the actual output with the original and the expectations. Include a baseline when testing an improvement, allow ties, and keep failed outputs. See the [evaluation protocol](evals/README.md).

A case is useful when it catches a meaningful failure. Tests that require one preferred sentence, equate brevity with quality, or label normal formal writing as AI do not establish a better editor. Do not add a detector service or upload private text as part of a routine test.

## Scope and attribution

Keep changes proportional to the problem. Correct a demonstrated weakness before expanding the catalog. Preserve the distinction between research findings, editorial interpretation, and untested proposals.

Link primary sources for new evidence and state the language, task, models, and limitations. Obtain permission before adding private writing or licensed material. The repository does not distribute the source PDFs or external skill snapshots.

Contributions are made under the project's [MIT license](LICENSE). If a change incorporates another project's licensed text or code, include the required notices and describe the adaptation. A source link alone does not replace a license obligation.

## Publish a release

Follow [publishing](docs/publishing.md). Create release notes from the final change and actual validation results. Report model/client limits separately from package checks. Do not claim that a newly configured workflow passed on GitHub before seeing a completed hosted run.
