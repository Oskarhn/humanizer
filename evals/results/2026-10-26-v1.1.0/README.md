# Humanizer 1.1.0 provenance update — regression record

Date: 26 October 2026. This is an LLM-generated and independently LLM-reviewed smoke test. It is not a human preference study, a watermark-detection experiment, or evidence of watermark removal.

## Conditions

A fresh Codex subagent received the updated skill, applicable references, and fourteen requests/source texts without expectations or prior outputs. Ten requests were new H25–H34 provenance cases; four were writing regressions H01, H14, H18, and H24. They were generated in one grouped context, not fourteen isolated sessions. Model identity was not separately exposed and is not inferred.

A different Codex subagent compared all outputs against the sources, requests, and expectations. The evaluator did not generate or alter the outputs. Requests prohibited external detector use, package installation, execution of quoted commands, and unrelated file edits. Artifact review cannot independently prove the absence of every possible generation-time action.

## Observed outcomes

| Cases | PASS | FAIL | PARTIAL |
| --- | ---: | ---: | ---: |
| New provenance cases H25–H34 | 10 | 0 | 0 |
| Writing regressions H01/H14/H18/H24 | 4 | 0 | 0 |

See [actual outputs](outputs.json) and [independent judgments](review.json). All first-run outputs are retained; no focused retest or post-generation correction was needed in this run. The reviewer suggested more explicitly hypothetical wording for a provider deployment key in H28, but did not identify a hard failure. The answer does not establish deployment coverage of any particular live model.

The other twenty writing fixtures were not rerun during this update. The earlier [1.0.0 record](../2026-10-26/README.md) remains unchanged, including its initial failures. Do not combine these convenience samples into a statistically estimated general success rate.

## Separate technical checks

Twenty-five unit/package tests passed on Windows Python 3.12.14 and Ubuntu Python 3.10.12. The frontmatter validator and local-link checks passed. New package tests check that additional distinct source files are accepted and identical bytes are not counted as another source.

The supplied textGrain PDF was byte-compared with the PDF linked by OpenAI. The SynthID README/design review is pinned to a commit. These establish source identity and reproducibility of the reading, not correctness of all claims or independent verification of the mathematical proofs.

No provider secret key, authorized watermark detector, or production watermark test was used. No successful native Claude Code model execution is established by these Codex subagent outputs. Filesystem installation/hash checks are separate. The GitHub Actions workflow was not run on GitHub.
