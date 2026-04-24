Written to `simulations/quest/variations/specify-abstract-variations-R7-2026-03-19.md`.

---

## R7 Variations Summary

**Three axes, derived from the three new v7 criteria:**

| ID | Axis | Criterion Targeted |
|----|------|---------------------|
| **V-01** | Output format: **quoted bridge evidence in Pass 3** | C-26 — integration column cites actual merged prose (verbatim 3-10 word extract, not Y/N) |
| **V-02** | Role sequence: **non-fixed-category diagnosis constraint** | C-25 — self-diagnosis names weakness outside Gap/Result/Implication/Prose; exclusion explicitly stated in Amendment 1 |
| **V-03** | Inertia framing: **per-path canonical-term checklist** | C-27 strengthened — signal-skip / nominal gap framing / non-trivial gaming named as canonical terms with per-path confirmations replacing the omnibus narrative |
| **V-04** | V-01 + V-02 | C-26 + C-25 at independent lifecycle positions (Pass 3 vs. Amendment 1) |
| **V-05** | Full synthesis | All three R7 axes on V-05 R6 base — candidate for next canonical |

**Key structural decisions:**

- **V-01** is the cleanest gap: Y/N in Pass 3 is prefillable before merge; a quoted extract cannot be fabricated pre-merge. The column header changes from `Integrated? Y / N` to `Integrated? ("quoted extract" or N)` with a rationale block explaining why.

- **V-02** adds an exclusion constraint to Amendment 1 with a *Why this constraint matters* block listing the categories Amendment 1 is positioned to catch (Background framing, Claim epistemic type, Method scope, contribution incrementality). The constraint field is: `Weakness category: [must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]`.

- **V-03** restructures the inertia block from a single narrative paragraph into three labeled sections — **Signal-skip**, **Nominal gap framing**, **Non-trivial gaming** — each with a definition and a per-path confirmation line. No new mechanisms; format-only change from V-05 R6 base.

- **V-05** is the synthesis candidate. All three axes are at structurally independent positions and carry without conflict.
gnosis. This probes whether the "unconstrained" diagnosis in R6 was actually constrained by the model's anticipation of Amendments 2-5.
- V-03 does not add new mechanisms -- it restructures the inertia block from a narrative paragraph into a per-path checklist with canonical names. The hypothesis is that canonical naming (signal-skip / nominal gap framing / non-trivial gaming) produces more consistent commitment than narrative description.
- V-04 tests additivity of C-26 + C-25 at independent positions. No structural conflict: Pass 3 (pre-Phase 4) and Amendment 1 (Phase 5) are separated by Phase 4.
- V-05 is the longest prompt of any round and the candidate for the next canonical.

**Predicted v7 scores:**

| Variation | v7 Predicted | New signals probed |
|-----------|-------------|---------------------|
| V-01 | ~100 | Does quoted extract evidence structural post-merge execution? |
| V-02 | ~100 | Does exclusion constraint change what Amendment 1 identifies? |
| V-03 | ~100 | Does canonical naming strengthen commitment vs. narrative form? |
| V-04 | ~100 | Are C-26 + C-25 additive without structural conflict? |
| V-05 | ~100 | Are all three axes load-bearing at the ceiling? |

---

## V-01 -- Quoted Bridge Evidence in Pass 3 (C-26)

**Variation axis**: Output format (Pass 3 integration column format: from Y/N to verbatim quoted extract of 3-10 words from the merged paragraph)
**Hypothesis**: The current canonical asks for Y/N in the integration column. Y can be filled before the merge is complete -- it is structurally unverifiable. A verbatim quoted extract (3-10 words, in quotation marks) from the merged paragraph cannot be fabricated pre-merge; it requires the merged text to exist. This makes genuine post-merge execution verifiable: a quoted extract is evidence that the bridge phrase appears in the final prose. C-26 is the ceiling above C-23 (the Y/N floor). Single-axis test: does adding the quoted-extract requirement change execution quality, or does it add only audit overhead? v7 candidate: quoted integration evidence as a structural post-merge gate.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with an inertia declaration naming three shortcuts this run will not take, declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence), then runs a hardened five-amendment pass with self-diagnosis first. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Pass 3 integration column requires a verbatim quoted extract from the merged paragraph rather than Y/N -- this makes genuine post-merge execution verifiable.

---

**Inertia declaration.** Before any work begins, name what a minimal-effort execution of this skill would do instead. The purpose is not to describe a failure mode -- it is to commit, in advance, to the behaviors this run will not take.

> A nominal execution would: (1) skip signal acquisition and write the abstract from the topic name alone, producing generic content that could apply to any paper in the field; (2) frame the Gap section with a vague insufficiency claim ("X remains poorly understood") rather than naming the specific unresolved question the paper addresses; (3) comply nominally with the non-triviality guard by making surface wording changes that do not alter the informational content of the sentence.

> This run will instead: (1) execute Phase 1 signal acquisition and ground every section in the extracted content; (2) frame the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution; (3) show substantive Before/After changes in Phase 5 that alter the informational content of the amended sentence, not just its phrasing.

> Confirm: [I confirm the above commitment before proceeding.]

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

**Gap** (write first -- 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact -- a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap -- 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question -- no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 -- do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim -- a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Boundary quality card -- Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? ("quoted extract" or N) |
|----------|-----------------------------------|-------------|---------------------------|--------------------------------------|
| Background -> Gap | [fill now] | -- | -- | -- |
| Gap -> Claim | [fill now] | -- | -- | -- |
| Claim -> Method | [fill now] | -- | -- | -- |
| Method -> Result | [fill now] | -- | -- | -- |
| Result -> Implication | [fill now] | -- | -- | -- |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable -- not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap -- not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim -- not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method -- not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables -- not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify -- COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card -- Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** -- Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** -- Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** -- Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** -- Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** -- Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 -- Merge and count.** Reorder to standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not preserve the semantic type, write N.

*Why quoted evidence rather than Y/N:* A Y checkbox cannot confirm that Pass 3 was completed after the merge rather than before it. A verbatim extract from the merged paragraph is evidence that the merged text exists and has been read -- it cannot be written before the merge is complete. This prevents rote form-filling of the integration column in advance.

Complete card -- all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? ("quoted extract" or N) |
|----------|----------|-------------|---------------|--------------------------------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 -- Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 -- Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep -- it runs before the targeted amendments so the model reads the abstract without knowing which specific weaknesses will be fixed next. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 -- Self-diagnosis (runs first)**
Read the merged abstract before any targeted fixing. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. Name it as a specific one-sentence claim about the weakness -- not a general quality assessment.
> Diagnosis: [name the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 -- Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened -- names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 -- Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 -- Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 -- Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]

---

## V-02 -- Non-Fixed-Category Diagnosis Constraint (C-25)

**Variation axis**: Role sequence (Amendment 1 self-diagnosis is explicitly constrained to name a weakness whose category falls entirely outside the four fixed amendment slots: Gap sharpening, Result quantification, Implication tightening, Prose coherence)
**Hypothesis**: In V-05 R6, Amendment 1 asks the model to "identify the single sentence or element most likely to cause a reviewer to pause" without excluding categories that Amendments 2-5 will address. The model's unconstrained scan of the post-merge abstract may systematically identify weaknesses in Gap, Result, Implication, or Prose -- the same targets as Amendments 2-5. If so, Amendment 1 is pre-empting the targeted slots rather than finding genuinely distinct weaknesses. The exclusion constraint tests whether the "unconstrained" diagnosis was actually constrained by anticipated fixed slots. If the model fails the constraint (diagnoses a Gap/Result/Implication/Prose weakness anyway), the four fixed slots are so salient they dominate even when named as off-limits. If the model succeeds, Amendment 1 identifies weaknesses in Background framing, Claim epistemic clarity, Method scope adequacy, or contribution structure -- categories no targeted amendment covers. C-25 is the ceiling above C-24 (the "differs from prior targets" floor).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with an inertia declaration naming three shortcuts this run will not take, declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration), then runs a hardened five-amendment pass with self-diagnosis first. Amendment 1 self-diagnosis is constrained to name a weakness outside the four fixed amendment categories -- Gap, Result, Implication, Prose coherence are all covered by Amendments 2-5; Amendment 1 must find what they do not. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration.** Before any work begins, name what a minimal-effort execution of this skill would do instead. The purpose is not to describe a failure mode -- it is to commit, in advance, to the behaviors this run will not take.

> A nominal execution would: (1) skip signal acquisition and write the abstract from the topic name alone, producing generic content that could apply to any paper in the field; (2) frame the Gap section with a vague insufficiency claim ("X remains poorly understood") rather than naming the specific unresolved question the paper addresses; (3) comply nominally with the non-triviality guard by making surface wording changes that do not alter the informational content of the sentence.

> This run will instead: (1) execute Phase 1 signal acquisition and ground every section in the extracted content; (2) frame the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution; (3) show substantive Before/After changes in Phase 5 that alter the informational content of the amended sentence, not just its phrasing.

> Confirm: [I confirm the above commitment before proceeding.]

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

**Gap** (write first -- 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact -- a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap -- 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question -- no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 -- do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim -- a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Boundary quality card -- Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? Y / N |
|----------|-----------------------------------|-------------|---------------------------|-------------------|
| Background -> Gap | [fill now] | -- | -- | -- |
| Gap -> Claim | [fill now] | -- | -- | -- |
| Claim -> Method | [fill now] | -- | -- | -- |
| Method -> Result | [fill now] | -- | -- | -- |
| Result -> Implication | [fill now] | -- | -- | -- |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable -- not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap -- not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim -- not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method -- not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables -- not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify -- COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card -- Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** -- Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** -- Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** -- Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** -- Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** -- Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 -- Merge and count.** Reorder to standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column. Integration is Y if the bridge phrase from Pass 2 was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

Complete card -- all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? |
|----------|----------|-------------|---------------|-------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 -- Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 -- Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep -- it runs before the targeted amendments. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those four categories are covered by Amendments 2-5. If you diagnose a Gap, Result, Implication, or Prose weakness, you are pre-empting the targeted amendments -- that is not a self-diagnosis, it is a preview. Name the weakness category first, then the specific element.

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots -- it is merely reordering them. The diagnostic value of Amendment 1 is in identifying weaknesses outside the fixed slots: Background context over-framed or under-framed for the Gap; Claim epistemic type mismatched to paper type; Method scope too narrow to support the Claim; contribution framing that a reviewer would read as incremental rather than novel.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]
> Diagnosis: [one sentence naming the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 -- Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened -- names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 -- Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 -- Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 -- Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]

---

## V-03 -- Per-Path Canonical-Term Inertia Checklist (C-27 Strengthened)

**Variation axis**: Inertia framing (reformulation from narrative paragraph to per-path labeled checklist with canonical term names and per-path confirmation; each path gets its own header, definition, and confirmation line)
**Hypothesis**: The current canonical has a narrative inertia declaration listing three cheap paths in a single block with one omnibus confirmation. C-27 in v7 specifies that the canonical cheap path names be used: signal-skip, nominal gap framing, non-trivial gaming. Per-path checkboxes force one explicit acknowledgment per path -- a reader commitment of three separate acts rather than one omnibus. Single-axis test: does reformatting the narrative block as a canonical-term checklist with per-path confirmations change quality outcomes vs. the narrative form? This is a format-only change -- same three paths, same commitment, different structure. The hypothesis is that canonical naming (each path labeled before description) makes the commitment more specific and harder to satisfy with a generic confirmation.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths this run will not take, confirmed per path -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration), then runs a hardened five-amendment pass with self-diagnosis first. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one and close it.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract is field-generic; it passes the word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label and passes the gap-vs-goal check, but does not identify the precise field-state that the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution -- not a generic domain gap.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format -- two versions of a sentence -- without altering informational content. Phrasing variation is not an amendment. Surface coherence edits that touch a sentence without changing what it asserts are not amendments.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs in Phase 5 that change the informational content of the sentence -- what it asserts, what it quantifies, what it implies -- not merely its phrasing.]

> All three paths closed. Proceed.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

**Gap** (write first -- 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact -- a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap -- 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question -- no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 -- do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim -- a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Boundary quality card -- Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? Y / N |
|----------|-----------------------------------|-------------|---------------------------|-------------------|
| Background -> Gap | [fill now] | -- | -- | -- |
| Gap -> Claim | [fill now] | -- | -- | -- |
| Claim -> Method | [fill now] | -- | -- | -- |
| Method -> Result | [fill now] | -- | -- | -- |
| Result -> Implication | [fill now] | -- | -- | -- |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable -- not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap -- not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim -- not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method -- not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables -- not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify -- COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card -- Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** -- Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** -- Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** -- Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** -- Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** -- Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 -- Merge and count.** Reorder to standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column. Integration is Y if the bridge phrase from Pass 2 was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

Complete card -- all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? |
|----------|----------|-------------|---------------|-------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 -- Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 -- Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep -- it runs before the targeted amendments so the model reads the abstract without knowing which specific weaknesses will be fixed next. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 -- Self-diagnosis (runs first)**
Read the merged abstract before any targeted fixing. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. Name it as a specific one-sentence claim about the weakness -- not a general quality assessment.
> Diagnosis: [name the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 -- Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened -- names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 -- Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 -- Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 -- Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]

---

## V-04 -- Quoted Bridge Evidence + Non-Fixed-Category Diagnosis (C-26 + C-25)

**Variation axes**: Output format (Pass 3 integration column requires quoted extract -- V-01 R7) + Role sequence (Amendment 1 self-diagnosis constrained to non-fixed categories -- V-02 R7)
**Hypothesis**: V-01 R7 probes C-26 at the bridge integration lifecycle position (pre-Phase 4). V-02 R7 probes C-25 at the amendment lifecycle position (Phase 5 Amendment 1). The two axes are structurally independent -- no cross-phase interference. The combination tests whether both ceiling criteria are achievable simultaneously. Risk: the quoted extract requirement adds cognitive load at Pass 3, which may compress attention available for the non-fixed-category diagnosis constraint at Amendment 1. If both fail simultaneously in execution, the attention-budget hypothesis (structural ceiling flat for 4 consecutive rounds) would be confirmed. If both pass, the two criteria are independently achievable in a single execution pass. C-26 + C-25 is the two-criterion ceiling: quoted integration evidence AND categorically novel self-diagnosis.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with an inertia declaration naming three shortcuts this run will not take, declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence), then runs a hardened five-amendment pass with self-diagnosis first. Amendment 1 is constrained to name a weakness outside the four fixed amendment categories. Pass 3 integration column requires a verbatim quoted extract from the merged paragraph. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration.** Before any work begins, name what a minimal-effort execution of this skill would do instead. The purpose is not to describe a failure mode -- it is to commit, in advance, to the behaviors this run will not take.

> A nominal execution would: (1) skip signal acquisition and write the abstract from the topic name alone, producing generic content that could apply to any paper in the field; (2) frame the Gap section with a vague insufficiency claim ("X remains poorly understood") rather than naming the specific unresolved question the paper addresses; (3) comply nominally with the non-triviality guard by making surface wording changes that do not alter the informational content of the sentence.

> This run will instead: (1) execute Phase 1 signal acquisition and ground every section in the extracted content; (2) frame the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution; (3) show substantive Before/After changes in Phase 5 that alter the informational content of the amended sentence, not just its phrasing.

> Confirm: [I confirm the above commitment before proceeding.]

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

**Gap** (write first -- 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact -- a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap -- 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question -- no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 -- do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim -- a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Boundary quality card -- Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? ("quoted extract" or N) |
|----------|-----------------------------------|-------------|---------------------------|--------------------------------------|
| Background -> Gap | [fill now] | -- | -- | -- |
| Gap -> Claim | [fill now] | -- | -- | -- |
| Claim -> Method | [fill now] | -- | -- | -- |
| Method -> Result | [fill now] | -- | -- | -- |
| Result -> Implication | [fill now] | -- | -- | -- |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable -- not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap -- not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim -- not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method -- not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables -- not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify -- COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card -- Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** -- Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** -- Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** -- Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** -- Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** -- Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 -- Merge and count.** Reorder to standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

*Why quoted evidence rather than Y/N:* A Y checkbox cannot confirm that Pass 3 was completed after the merge rather than before it. A verbatim extract from the merged paragraph is evidence that the merged text exists and has been read -- it cannot be written before the merge is complete.

Complete card -- all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? ("quoted extract" or N) |
|----------|----------|-------------|---------------|--------------------------------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 -- Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 -- Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep -- it runs before the targeted amendments. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. Amendment 1's value is in identifying what the fixed slots cannot catch: Background framing relative to the Gap, Claim epistemic type relative to the paper type, Method scope relative to the Claim strength, contribution framing that reads as incremental rather than novel.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]
> Diagnosis: [one sentence naming the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 -- Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened -- names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 -- Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 -- Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 -- Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]

---

## V-05 -- Full Synthesis: Quoted Bridge Evidence + Non-Fixed-Category Diagnosis + Per-Path Inertia Checklist (C-26 + C-25 + C-27 Strengthened)

**Variation axes**: All three R7 axes combined on V-05 R6 base: output format (quoted bridge evidence in Pass 3 -- V-01 R7) + role sequence (non-fixed-category diagnosis constraint in Amendment 1 -- V-02 R7) + inertia framing (per-path canonical-term checklist -- V-03 R7)
**Hypothesis**: All three R6 mechanisms are formalized as aspirational criteria in v7. R7 axes probe the ceiling above the v7 floor. The three axes operate at structurally independent lifecycle positions: per-path inertia checklist is pre-Phase 0; quoted bridge evidence is Pass 3 (pre-Phase 4); non-fixed-category diagnosis is Amendment 1 (Phase 5). No axis interferes with the others. If all three are load-bearing, V-05 R7 implements C-25/C-26/C-27 at the ceiling in a single prompt. The highest-signal axis remains non-fixed-category diagnosis (C-25): if the model succeeds, it proves Amendment 1 was finding genuinely novel weaknesses unconstrained; if it fails, the four fixed slots dominate even with explicit exclusion. The highest-verification axis is quoted bridge evidence (C-26): the extract is either present or absent in the merged text. The highest-effort-per-gain axis is per-path inertia checklist (C-27): three named confirmations replace one omnibus. V-05 R7 is the candidate for the next canonical if all three axes pass.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three R6 enforcement layers (structured revision directive, bridge integration audit, self-diagnosis amendment) plus three R7 ceiling criteria (quoted bridge evidence, non-fixed-category diagnosis, per-path inertia commitment).

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one and close it.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> All three paths closed. Proceed.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

**Gap** (write first -- 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact -- a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap -- 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question -- no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 -- do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim -- a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Boundary quality card -- Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? ("quoted extract" or N) |
|----------|-----------------------------------|-------------|---------------------------|--------------------------------------|
| Background -> Gap | [fill now] | -- | -- | -- |
| Gap -> Claim | [fill now] | -- | -- | -- |
| Claim -> Method | [fill now] | -- | -- | -- |
| Method -> Result | [fill now] | -- | -- | -- |
| Result -> Implication | [fill now] | -- | -- | -- |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable -- not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap -- not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim -- not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method -- not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables -- not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify -- COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card -- Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** -- Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** -- Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** -- Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** -- Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** -- Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 -- Merge and count.** Reorder to standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase appears in the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

*Why quoted evidence rather than Y/N:* A Y checkbox cannot confirm Pass 3 was completed after the merge. A verbatim extract from the merged paragraph is evidence the merged text exists and has been read -- it cannot be written before the merge is complete. This makes genuine post-merge execution verifiable and prevents rote form-filling of all four card columns in a single pre-merge pass.

Complete card -- all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? ("quoted extract" or N) |
|----------|----------|-------------|---------------|--------------------------------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [3-10 quoted words from merged text, or N] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 -- Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 -- Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep -- it runs before the targeted amendments. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

*Why this constraint matters:* The diagnostic value of Amendment 1 is in identifying what Amendments 2-5 cannot catch: Background framing over- or under-scoped for the Gap; Claim epistemic type mismatched to paper type; Method scope too narrow to support the Claim strength; contribution framing that a reviewer would read as incremental rather than novel. If Amendment 1 identifies a Gap, Result, Implication, or Prose weakness, it is pre-empting the targeted slots -- the self-diagnosis position is not doing distinct work.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]
> Diagnosis: [one sentence naming the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 -- Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened -- names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 -- Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 -- Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 -- Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]
