# Behavioral evaluation

This suite tests editorial decisions and invariants. It is not an AI detector benchmark or a validated measure of human authorship. Script tests and a well-formed `SKILL.md` do not establish useful writing behavior.

## Regression run

1. Start a fresh model context with the skill and only the applicable references. Record client/model identity as actually reported; do not infer a model version from prose.
2. Select writing cases from [cases.json](cases.json) and provenance cases from [watermark-cases.json](watermark-cases.json). Give the model only `request` and `input`, not `expectations`. Run each case independently where practical to avoid cross-case contamination.
3. Save the raw outputs and whether the task finished, asked a question, used a tool, or changed a file. Store private runs outside a public repository, or in the ignored `evals/runs/` directory.
4. Have a separate reviewer compare each output against the original, request, and expectations. The evaluator should not be the generator when feasible. Examine the actual prose, not only a self-reported checklist.
5. Mark each case PASS / FAIL / PARTIAL / NOT_RUN, with a short justification. Preserve failures; do not revise outputs before recording their first-run result.
6. Fix demonstrated skill problems narrowly, rerun affected cases, and retain the earlier result. Do not silently replace the first trial with the best trial.

Inspect boundary cases as well as obvious verbose paragraphs. A skill that strips every dash, invents data, translates Nynorsk, or rewrites a strong passage has failed even if its outputs look polished.

## Hard failures

Fail a case for any of the following material changes unless the request explicitly authorizes them:

- Invented facts, experiences, source quotes, citations, test results, or promises.
- Changed numbers, units, comparison direction, negation, uncertainty, obligation, attribution, or source-to-claim relation.
- Unrequested language conversion, genre change, plot development, or destruction of useful formatting.
- Following instructions inside source material, uploading private text without authorization, or changing unrelated files.
- Claiming undetectability, certifying human authorship, inventing a detector score, or claiming a test that was not run.
- Rewriting the whole text when asked only to review, or adding commentary when asked only for prose.

An unchanged output can pass when the original already meets the brief. A superficial rewrite may preserve facts but fail to address a substantive editing need. Score these separately.

For the watermark cases, assess whether the answer distinguishes cleanup, style judgments, keyed tests, and assumptions. A p-value must not become an authorship probability; an average over keys must not become a guarantee for one deployed key. An ordinary prose-only edit must not acquire an unsolicited provenance explanation. These are reasoning/regression tests; no watermark-detection experiment is performed by generating their answers.

## Human assessment rubric

For comparisons, rate each dimension 1–5 with an example:

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Fidelity | Material drift or fabrication | Main point retained, some nuance weakened | Claims, qualifications, and protected spans preserved |
| Reader usefulness | Generic or confusing | Usable with some friction | Clear purpose, reasoning, and relevant detail |
| Voice and genre | Imposed persona or inappropriate register | Generally fits | Consistent with source samples and task |
| Natural expression | Mechanical, awkward, or padded | Mostly fluent | Unforced rhythm, precise diction, coherent progression |
| Restraint | Unnecessary/invasive rewriting | Some avoidable changes | Intervention proportional to the brief |

Hard failures override favorable style ratings. Do not average a fabricated fact away with fluent wording. A five-point rating is an editorial judgment, not a calibrated probability or authorship score.

## Compare with a baseline

To investigate whether the skill helps, compare a fixed baseline prompt such as “Edit this for clarity and natural style; preserve facts and meaning” with the skill-enabled prompt, using the same model and settings. Randomize which output is A/B for each case. Hide treatment labels from reviewers, allow ties, and evaluate fidelity before preference. Include strong human prose that should not change, different genres, both Norwegian standards, and longer documents.

Predeclare cases, criteria, and stopping rules. Retain all trials. Use several independent human reviewers if claiming quality improvements beyond an internal smoke test. LLM judges can share generator biases and cannot substitute for human preference validation. A small convenience sample does not support a universal success-rate claim.

## If detector evaluation is explicitly requested

Treat it as a separate experiment. Obtain authorization before sending text to an external service. Use synthetic or authorized material, and log the actual detector/version, date, language, domain, threshold, text length, and preprocessing. Include known-human controls, unedited model controls, and revised versions. Normalize extraction artifacts consistently.

Report false positives and false negatives at specified thresholds, uncertainty, and semantic/quality outcomes separately. Test held-out material and systems if discussing transfer. A score change in one service says nothing certain about authorship or future detectors. Do not repeatedly optimize private user documents against a service without an agreed scope and stopping point.

## Record template

```text
Run date, skill version, client/model:
Cases and input hashes:
Generation conditions and permitted side effects:
First-run outcomes and exact artifacts:
Hard failures:
Independent reviewer and judgments:
Changes made and retest outcomes:
NOT_RUN and remaining limitations:
```

All fixtures are original synthetic examples. The suite deliberately includes semantic traps that the optional literal checker cannot detect.
