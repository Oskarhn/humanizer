# Initial behavioral smoke test — 26 October 2026

This is a small, synthetic, LLM-generated and LLM-reviewed regression run. It is not a human preference study, blinded A/B comparison, detector benchmark, or evidence of undetectability.

## Conditions and artifacts

- Skill: `humanizer` 1.0.0, during initial development.
- Generation: two Codex subagent contexts, twelve requests per context. Agents received the skill, applicable references, and requests/source text without the evaluation expectations. Cases were grouped, not twenty-four fully isolated sessions.
- Review: a separate Codex subagent compared the actual outputs against source, request, and expectations. The exact model identifier was not exposed in the test record and is not inferred here.
- Side effects: local reading and writing synthetic output artifacts only. No external detector was called. Artifact review cannot independently prove the absence of every possible generation-time tool action.
- First-run artifacts: [H01–H12](first-run-1.json), [H13–H24](first-run-2.json), and [independent judgments](first-review.json).
- Focused retest: a fresh generation context received H14 and H18 without previous outputs or judgments; the independent reviewer then assessed the new outputs. See [retest outputs](retest-outputs.json) and [retest judgments](retest-review.json).

## Observed results

| Stage | PASS | FAIL | PARTIAL |
| --- | ---: | ---: | ---: |
| Initial 24 cases | 22 | 1 | 1 |
| Focused H14/H18 retest | 2 | 0 | 0 |

H14 weakened “not evidence of equivalence” into “does not establish equivalence.” The instructions now explicitly protect evidence-versus-proof distinctions. H18 removed the source's challenging/rewarding assertion as generic framing. The instructions now distinguish empty signposting from a familiar sentence that still carries a distinct assertion or stance.

Both new outputs preserve those meanings. The other twenty-two cases were not rerun after these narrow instruction changes. Do not describe this record as a fresh 24/24 run of the final package or as a statistically estimated success rate.

The H14 expectation was clarified after the first review to name the evidence-versus-proof distinction explicitly; its source and request were unchanged. The initial failure was retained. This is transparent regression development, not a preregistered experiment.

## Separate technical checks

Twenty-three standard-library unit/package tests passed on Windows Python 3.12.14 and Ubuntu Python 3.10.12. The skill-creator frontmatter validator passed in Ubuntu. These check packaging and helper behavior, not editorial quality. A Windows attempt to run that external validator lacked PyYAML; running the validator in the existing Ubuntu environment resolved that check without adding dependencies to this package.

Native Claude Code model execution was attempted in the installation environment but authentication was unavailable. No Claude-generated writing result or Claude behavioral pass is claimed. Filesystem installation and matching content hashes were verified separately. The GitHub Actions workflow is included but was not executed on GitHub during this local run.

## Remaining work for stronger claims

Evaluate fresh held-out material with independent human readers, a fixed baseline, random treatment labels, and several genres and languages. Include realistic long documents and repeated independent trials. Report fidelity failures separately from preference. New model/client versions require fresh checks. These are future evaluation opportunities, not completed work.
