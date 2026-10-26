# Language and voice

## Calibrate to evidence, not a persona

When a user provides samples, notice a small number of useful traits: register, directness, rhythm, paragraph scale, vocabulary, humour, stance, and relationship with the reader. Match traits that recur across comparable samples. One dash, swear word, or long sentence does not establish a general preference.

Use the source text as the default voice reference when there are no separate samples. If the draft is obviously generic and voice is unspecified, aim for an unobtrusive register suited to its audience. Do not invent an idiosyncratic personality to compensate for missing information.

Keep content and voice separate. A sample saying “I have managed this team for ten years” establishes neither the user's tenure nor permission to insert that claim. Borrow the degree of directness, not the biography.

For a long document, use a short working voice card, not a rigid style formula:

```text
Reader and purpose: ...
Register and stance: ...
Observed recurring traits: ...
Distinctive wording to retain: ...
Terms, claims, and structure to protect: ...
```

Do not expose the card unless useful or requested. Concrete examples and context have stronger empirical support than abstract persona prompts in the social-reply setting of [R05]. That finding does not establish a guaranteed effect for every genre or model.

## Norwegian: Bokmål and Nynorsk

Preserve the user's written standard, level of formality, and established word forms. Do not silently convert Nynorsk to Bokmål, moderate Bokmål to a different variety, or a personal message into public-sector prose. An isolated variation may be intentional; ask only when ambiguity affects a substantial task.

The following are editorial and plain-language guidance, supported in part by Språkrådet [R17], not a validated detector-evasion method for Norwegian:

- Put the relevant message early when the genre calls for it. A meeting request needs its request; a story may need a scene.
- Prefer a direct verb to an unnecessary noun construction: “vurdere” may replace “foreta en vurdering.” Retain technical nouns when they name the concept accurately.
- Keep a natural Norwegian relation between clauses. “Men,” “fordi,” “derfor,” and “likevel” can make reasoning easier to follow. Do not strip connective words merely to shorten the piece.
- Inspect literal English calques and presentation phrases: “adressere utfordringen,” “levere på,” “ta et dypdykk,” and “i dagens stadig skiftende landskap.” Keep them if they are established and precise in the actual context; otherwise say what happens.
- “Det er viktig å merke seg at” can often be removed so the important information leads the sentence. Keep explicit emphasis when the consequence would otherwise be missed.
- Avoid vague “i forhold til” when the intended meaning is “om,” “for,” or “når det gjelder.” Preserve it when it expresses a real comparison.
- Keep ordinary Norwegian compounds and correct word division. Do not imitate English title capitalization, insert decorative hyphens, or add English phrases for variety.
- Keep local number and date conventions unless conversion is requested. Do not silently reinterpret ambiguous dates or change decimal commas in measurements, formulas, or code.
- Do not inject “jo,” “vel,” “liksom,” “egentlig,” dialect spellings, or profanity to force informality. They can remain when the author uses them purposefully.

**Bokmål, source facts:**

> Det vil bli gjennomført en vurdering av søknaden innen 14 dager. Det er viktig å merke seg at manglende vedlegg kan medføre forsinkelser.

**Revision:**

> Søknaden blir vurdert innen 14 dager. Manglende vedlegg kan forsinke behandlingen.

The passive remains because the source does not identify the decision-maker. “Du får svar innen 14 dager” would invent a different promise.

**Nynorsk, source facts:**

> Vi vil gjennomføre ei vurdering av rutinen når prøveperioden er avslutta. Det er likevel ikkje avklart om vi kan halde fram med ordninga.

**Revision:**

> Vi vurderer rutinen etter prøveperioden. Det er likevel ikkje avklart om vi kan halde fram med ordninga.

The uncertainty stays. There is no reason to replace “ordninga” with a synonym simply for variation.

## English

Preserve the selected national variety and the document's terminology. Do not convert British spelling to American spelling because it is more familiar. Keep the technical sense of words even if a generic alternative sounds simpler.

- Use contractions when they fit a conversation or the writer's samples, not as a universal marker of humanity.
- Avoid noun stacks when the relationship can be stated clearly with a verb or preposition. Retain standard compound terms.
- Inspect repeated present-participial add-ons and nominalizations in dense prose. Decide whether a full clause would make the actor or inference clearer. This diagnostic is motivated by [R08]; it is not a ban.
- Keep natural, explicit linkages such as “because” and “although.” Removing every transition produces abrupt writing.
- Avoid swapping every repeated noun for a synonym. Precision and stable reference often matter more than variety.

**Source:**

> The implementation of the migration facilitated the optimization of response times, underscoring the transformative potential of the new architecture.

If the only verified fact is that response times improved:

> The migration improved response times.

Do not invent a percentage, causal mechanism, or measured architecture benefit. If the original's migration-to-improvement relation is itself uncertain, preserve that uncertainty instead.

## Other languages and mixed-language documents

The skill's content and fidelity checks transfer more safely than its surface examples. Apply the target language's own idiom and genre conventions. Do not translate the English warning words into a universal blacklist. Do not extrapolate English detector results into numerical claims about another language.

Preserve intentional code-switching, quotations, names, and technical terms. If the assignment is a translation, use translation fidelity as well as this editing workflow; do not treat localization as permission to replace facts.

Research IDs refer to the [archived research notes](https://github.com/Oskarhn/humanizer/blob/304f74ebe1c57e5b58bed384cb286e20206eb950/references/evidence.md).
