# How it works and what informed it

Humanizer is a reusable editing workflow, implemented as instructions and references that Codex or Claude Code can read. It is not a separate model. Its usefulness depends on the host model, the source material, and the writing brief.

## The editing process

1. **Establish what must survive.** Identify claims, figures, qualifications, source links, author voice, and required structure.
2. **Find the consequential problems.** Look for unclear reasoning, repeated paragraph jobs, empty claims, awkward syntax, or the wrong register.
3. **Revise to the requested depth.** A light edit can stay local; a deep rewrite can reorganize expression while preserving the argument and evidence.
4. **Compare with the source.** Check what changed in content, accountability, voice, readability, and delivery. Inspect new connectors as well as individual facts.

For example, “No temperature measurement is available” does not establish “The temperature was never measured.” A change from passive voice to “we measured” can add an operator the source did not identify. These are editorial distinctions the skill explicitly asks the model to protect, not guarantees that a model will never make an error.

## What the research contributes

Research on human and model writing helps identify questions worth asking. It does not supply a universal recipe for good prose.

- **Grammar and genre:** Reinhart and colleagues examine grammatical and rhetorical variation in human and model text. The editorial response is to inspect how a sentence fits its genre while retaining legitimate terminology and syntax. [Paper and author version](https://arxiv.org/abs/2410.16107).
- **Vocabulary in context:** Kobak and colleagues study excess vocabulary across biomedical abstracts. Population-level word shifts do not identify the author of one paragraph or justify banning the words. [Author version](https://arxiv.org/abs/2406.07016v5).
- **Norwegian clarity:** Språkrådet's guidance supports reader-appropriate structure, concrete language, and useful verbs. This informs the Norwegian reference; it is language guidance, not a detector-evasion experiment. [Writing advice](https://sprakradet.no/klarsprak/om-skriving/generelle-skriverad-bokmal/).

The earlier [research notes](https://github.com/Oskarhn/humanizer/blob/304f74ebe1c57e5b58bed384cb286e20206eb950/references/evidence.md) document the broader reading and access limits. The review includes research papers, provider documentation, and language guidance; those are different kinds of evidence. No cited study validates this complete skill or establishes a Norwegian detector-resistance effect.

## What the package promises

The instructions prioritize meaning, author intent, genre, and natural expression. They do not impose a human persona, intentional mistakes, sentence-length quotas, or a universal punctuation blacklist. The four supporting references supply practical editing, language, genre, and example guidance.

The result should be assessed against the original and the brief. A natural-sounding revision does not certify authorship, establish that a detector will accept it, or verify the absence of a statistical watermark. See the [comparison](COMPARISON.md) for the actual local evaluation and its limitations.
