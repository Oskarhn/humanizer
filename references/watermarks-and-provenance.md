# Statistical watermarks and editing

Use this reference when the user asks about watermarks, detector guarantees, SynthID, textGrain, or the interpretation of a provenance result. It does not add a caveat to every ordinary writing task. Source IDs refer to [evidence.md](evidence.md).

## Identify the question before making a claim

| Question | Appropriate evidence | What it cannot establish alone |
| --- | --- | --- |
| Is this clear, natural writing for its reader? | The text, brief, and writer's voice | Who generated it or whether it carries a watermark |
| Does a style classifier flag it? | An actual result from that classifier/version | Presence or absence of a different keyed signal |
| Is a particular statistical watermark detected? | A compatible authorized test and configuration | Human contribution, truth, or universal provenance |
| Does a file carry credentials/metadata? | Inspection of that file and its credential mechanism | The status of statistical signals within its wording |

Text does not need visible oddities to carry a statistical signal. The existence of an invisible character also does not identify a watermark. The optional review script examines literals and surface cues; it does not implement a keyed statistical test.

## Consequences for this skill

Perform the requested edit while preserving content and voice. Do not substitute an arbitrary percentage of words, add errors, remove technical precision, or inflate “randomness” to meet an imagined watermark target. If a user asks for proof of removal, describe what was actually checked and leave the unmeasured property unresolved. A clean local review report supports only its stated checks.

**Inference from generation-time marking:** Rewriting through a service that marks its outputs can introduce a new signal in the new wording. Translation through such a service can likewise create marked output. Weakening an earlier signal is therefore different from establishing that the final text is unmarked. Do not offer repeated model round-trips as a verified removal procedure. No access to generation-time sampling or deployment keys is conferred by installing a prose-editing skill.

Anthropic describes a SynthID-derived method and says its translations can be marked. Its announcement also distinguishes heavy editing from original drafting: a result can indicate involvement without resolving that distinction [R19]. Treat product coverage and access statements as dated provider reports; refresh them before making a current deployment claim.

## textGrain: preserve the conditions of mathematical claims

The supplied technical report [R21] couples token selection to keyed randomness using block optimal transport. Its entropy budget concerns an **average** reduction in sampling entropy under the stated construction. It is not a quota for sentence-length variation, vocabulary diversity, or the percentage of words to edit.

Important distinctions when explaining or editing the report:

- Averaging over keys/columns can preserve a next-token distribution without guaranteeing identical entropy for every fixed key or response.
- The requested numerical budget differs from the solver's achieved loss. Finite precision, convergence, and unattainable targets must not disappear from a simplified account.
- Local distribution preservation is not automatically preservation of an entire generated sequence. The latter requires additional conditional-uniformity assumptions.
- Detection reconstructs scores using matching tokenizer, key, context rule, and block/column configuration. Not needing the generating model or its entropy budget does not mean not needing a key or compatible settings.
- Under the ideal null assumptions, the scored sum has a specified reference distribution. Fixed-key deployment still needs empirical calibration. A mathematical target error rate is not a measured rate for an arbitrary document population.

This is a technical report describing construction and guarantees, not a benchmark study proving universal superiority, readability, diversity, or detection resistance. Distinguish its mathematics from empirical claims in a separate provider announcement [R22].

## SynthID: do not merge distinct implementations

The Nature paper [R16], research code, and newer tournament documentation [R20] are related artifacts, not one interchangeable deployment. The repository calls its code a reference implementation, while the design document addresses serving-engine pseudocode. Its open code and example key do not supply a provider's deployed key. Fixed-key calibration is explicitly important. Do not transfer defaults, detector types, or guarantees between revisions without checking the exact artifact.

For example, a frequentist p-value is not the same output as a trained Bayesian detector's score. Do not describe either as “percent of the document written by AI.” A p-value is a tail probability under a null model, not the posterior probability that the text is AI-generated. An attractive-looking percentage is not a substitute for understanding the reported quantity.

## What an actual verification record would need

If detector testing is requested and access exists, record the exact final text, detector/version, supported watermark family, relevant configuration, threshold, language, usable scored length, and the result. State the actual scope: a specific watermark was or was not detected under those conditions. Do not expose secret keys in reports. Use synthetic or authorized text; external submission still requires authorization.

A negative result can reflect insufficient signal, unsupported configuration, editing, an absent watermark, or another generator. It is not a human-authorship certificate. Likewise, a positive watermark result cannot measure the author's creative contribution or decide whether a claim is true.

When comparing studies, keep watermark family, backbone model, detector training, text length, threshold, transformation, and outcome separate. A small-backbone corruption pilot [R02] does not validate a faithful rewrite against a commercial provider. Avoid carrying a removal percentage from one experiment into an operational editing instruction.
