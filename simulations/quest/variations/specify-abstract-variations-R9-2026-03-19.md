**R9 variations written** to `simulations/quest/variations/specify-abstract-variations-R9-2026-03-19.md`.

---

## R9 Variations Summary

**Base**: V-05 R8 (100/100 on v8). All five are complete prompt bodies targeting the three new v9 ceiling criteria.

| ID | Axis | Gate | Pass 3 | Amendment 1 | v9 Predicted |
|----|------|------|--------|-------------|-------------|
| **V-01** | C-29 isolation | anonymous | CAN+CANNOT | Why-embedded | ~96 (fail C-31, C-32) |
| **V-02** | C-31 isolation | anonymous | CANNOT-only | dedicated block | ~96 (fail C-29, C-32) |
| **V-03** | C-32 isolation | named-per-path | CANNOT-only | Why-embedded | ~96 (fail C-29, C-31) |
| **V-04** | C-29 + C-31 | anonymous | CAN+CANNOT | dedicated block | ~98 (fail C-32 only) |
| **V-05** | Full synthesis | named-per-path | CAN+CANNOT + process-level | dedicated block | ~100 (confirms V-05 R8) |

**Design rationale**: V-05 R8 already satisfies all three v9 ceiling criteria (C-29 tightened, C-31 new, C-32 new). R9's single-axis variations reverse-isolate each criterion by holding two others out, establishing clean pass/fail boundaries. V-05 R9 is a faithful reproduction of V-05 R8 to confirm it scores 100 on the new rubric. If confirmed, no new ceiling behavior needs to be synthesized — v9 closes cleanly on V-05 R8 as canonical.
 only |
| **V-04** | C-29 + C-31 | Gate reverted to anonymous. Pass 3 keeps CAN+CANNOT; Amendment 1 keeps dedicated block. | C-29 + C-31 |
| **V-05** | Full synthesis | V-05 R8 unchanged: CAN+CANNOT + process-level impossibility at Pass 3, dedicated block at Amendment 1, named-per-path gate. | C-29 + C-31 + C-32 |

### Key structural argument for each axis

**V-01 (C-29)**: C-29 v9 requires both sides of the asymmetry. V-01 keeps the CAN+CANNOT Pass 3 rationale from V-05 R8 but reverts Amendment 1 to the Why-embedded form and uses an anonymous gate. Expected: PASS C-29, FAIL C-31, FAIL C-32.

**V-02 (C-31)**: C-31 requires the positive search space to appear as a separately labeled block structurally distinct from the Why constraint block. V-02 keeps the dedicated block but reverts Pass 3 to CANNOT-only (failing C-29 v9 tightened) and uses an anonymous gate (failing C-32). Expected: FAIL C-29, PASS C-31, FAIL C-32.

**V-03 (C-32)**: C-32 requires the aggregation gate to name all three canonical paths at the closure event. V-03 keeps the named-per-path gate but reverts Pass 3 to CANNOT-only and Amendment 1 to Why-embedded. Expected: FAIL C-29, FAIL C-31, PASS C-32.

**V-04**: Tests C-29 + C-31 additivity without C-32. Gate is anonymous. Expected: PASS C-29 + C-31, FAIL C-32.

**V-05**: V-05 R8 with all three ceiling criteria active. Confirms synthesis score. Expected: PASS C-29 + C-31 + C-32.

**Predicted v9 scores:**

| Variation | v9 Predicted | C-29 | C-31 | C-32 | Notes |
|-----------|-------------|------|------|------|-------|
| V-01 | ~96 | PASS | FAIL | FAIL | -2 (C-31) -2 (C-32) |
| V-02 | ~96 | FAIL | PASS | FAIL | -2 (C-29) -2 (C-32) |
| V-03 | ~96 | FAIL | FAIL | PASS | -2 (C-29) -2 (C-31) |
| V-04 | ~98 | PASS | PASS | FAIL | -2 (C-32) |
| V-05 | ~100 | PASS | PASS | PASS | Confirms V-05 R8 canonical |

---

## V-01 -- C-29 Isolation: CAN+CANNOT Asymmetry in Pass 3 Only

**Variation axis**: Output format (Pass 3 structural asymmetry rationale retains CAN+CANNOT bidirectional framing; Amendment 1 reverts to Why-embedded form without dedicated block; inertia gate reverts to anonymous)
**Hypothesis**: V-05 R8 satisfies all three v9 ceiling criteria simultaneously. V-01 isolates C-29 by keeping the bidirectional structural asymmetry argument at Pass 3 while reverting Amendment 1 to embedded-positive-space form (failing C-31) and using an anonymous gate (failing C-32). Expected: C-29 passes because both CAN-side and CANNOT-side are present; C-31 fails because positive search space targets are embedded in the Why block rather than in a separately labeled block; C-32 fails because the gate does not name each canonical path at the closure event.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and explicit structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories. Pass 3 integration column requires verbatim quoted evidence: a Y/N status can be prefilled before the merge exists; a quoted extract cannot. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and close the set before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
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

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

*Why quoted evidence rather than Y/N -- structural asymmetry:* A Y/N integration status can be assigned in the same cognitive pass as Pass 1 coupling and Pass 2 bridge composition -- before the merge has been executed. Filling in Y does not require the merged paragraph to exist; it can be done at any point before, during, or after the merge. A verbatim extract from merged prose cannot be written before the merge is executed: the text does not yet exist. This asymmetry is the structural reason for the format change -- not to add audit overhead, but to close the pre-fill window entirely. An extract is evidence that the merge was completed and the paragraph was read; a Y is not.

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

---

## V-02 -- C-31 Isolation: Dedicated Positive Search Space Block in Amendment 1 Only

**Variation axis**: Role sequence (Amendment 1 includes a dedicated `*Where to look instead -- positive search space:*` block structurally distinct from the Why block; Pass 3 reverts to CANNOT-only rationale; gate reverts to anonymous)
**Hypothesis**: C-31 requires the positive search space to appear as a separately labeled block -- not as inline content in the Why block. V-02 keeps the dedicated block from V-05 R8 while reverting Pass 3 to CANNOT-only (failing C-29 v9's requirement for both sides) and using an anonymous gate (failing C-32). Expected: C-31 passes because the dedicated block is structurally distinct with its own label; C-29 fails because the asymmetry argument states only the CANNOT-side; C-32 fails because the gate does not name each path at closure.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with an enumerated positive search space naming where to look. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and close the set before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
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

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*
- **Background epistemic register**: Does the Background use observational or domain-survey language when the paper type is theoretical? Does it use conceptual-landscape language when the paper type is empirical? A register mismatch signals a paper type that has not propagated into the draft.
- **Claim scope relative to Method**: Is the Claim stronger than what the Method and Result can establish? A Claim of "we demonstrate that X causes Y" requires causal evidence; "we found X associated with Y" does not. Overclaiming in the Claim section is a reviewer flag that survives all four targeted amendments.
- **Contribution incrementality framing**: Would a reviewer read the Claim as "the authors did more of something" rather than "the authors resolved something that prior work could not resolve"? Does the abstract communicate the necessity of this paper, not just its content?
- **Method scope adequacy**: Is the stated scope (sample size, dataset characteristics, model type) sufficient to support the Claim's strength? Scope inadequacy makes the Result uninterpretable regardless of quantification.

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

## V-03 -- C-32 Isolation: Named-Per-Path Aggregation Gate Only

**Variation axis**: Inertia framing (aggregation gate names all three canonical paths by term at the closure event; Pass 3 reverts to CANNOT-only rationale; Amendment 1 reverts to Why-embedded form without dedicated block)
**Hypothesis**: C-32 requires the gate to name each canonical path by its canonical term at the gate event itself. V-03 keeps the named-per-path gate from V-05 R8 while reverting Pass 3 to CANNOT-only (failing C-29 v9) and Amendment 1 to Why-embedded form (failing C-31). Expected: C-32 passes because all three canonical path names appear at the closure event in the gate line itself; C-29 fails because only the CANNOT-side of the asymmetry is stated; C-31 fails because positive targets are embedded in the Why block rather than in a dedicated labeled block.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path and closed by canonical name in an aggregation gate -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and then close all three by canonical name before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to Phase 0.

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

---

## V-04 -- C-29 + C-31: Explicit Asymmetry + Dedicated Positive Search Space (No Named Gate)

**Variation axes**: Output format (Pass 3 CAN+CANNOT structural asymmetry -- C-29) + Role sequence (Amendment 1 dedicated positive search space block -- C-31); inertia gate reverts to anonymous
**Hypothesis**: V-04 tests C-29 and C-31 in combination while leaving C-32 unimplemented. Pass 3 retains the bidirectional asymmetry argument (CAN-side + CANNOT-side); Amendment 1 retains the dedicated `*Where to look instead -- positive search space:*` block; gate uses anonymous "All three paths closed. Proceed." Expected: PASS C-29 (both sides of asymmetry present), PASS C-31 (dedicated labeled block structurally distinct from Why block), FAIL C-32 (gate does not name each canonical path at the closure event).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and explicit structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with an enumerated positive search space. Pass 3 integration column requires verbatim quoted evidence: a Y/N status can be prefilled before the merge; a quoted extract cannot be written before the paragraph exists. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and close the set before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
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

**Boundary quality card -- Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

*Why quoted evidence rather than Y/N -- structural asymmetry:* A Y/N integration status can be assigned in the same cognitive pass as Pass 1 coupling and Pass 2 bridge composition -- before the merge has been executed. A Y entry does not require the merged paragraph to exist; it can be filled in at any point before, during, or after the merge. A verbatim extract from merged prose cannot be written before the merge is executed: the text does not yet exist. This asymmetry is the structural reason for the format change -- not to add audit overhead, but to close the pre-fill window entirely. When the integration column requires a quoted extract, completing it in the same pass as Pass 1 and Pass 2 is structurally impossible. A quoted extract is evidence that the merge was completed and the paragraph was read; a Y is not.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*
- **Background epistemic register**: Does the Background use observational or domain-survey language when the paper type is theoretical? Does it use conceptual-landscape language when the paper type is empirical? A register mismatch signals a paper type that has not propagated into the draft.
- **Claim scope relative to Method**: Is the Claim stronger than what the Method and Result can establish? A Claim of "we demonstrate that X causes Y" requires causal evidence; "we found X associated with Y" does not. Overclaiming in the Claim section is a reviewer flag that survives all four targeted amendments.
- **Contribution incrementality framing**: Would a reviewer read the Claim as "the authors did more of something" rather than "the authors resolved something that prior work could not resolve"? Does the abstract communicate the necessity of this paper, not just its content?
- **Method scope adequacy**: Is the stated scope (sample size, dataset characteristics, model type) sufficient to support the Claim's strength? Scope inadequacy makes the Result uninterpretable regardless of quantification.

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

## V-05 -- Full Synthesis: C-29 + C-31 + C-32 (Confirms V-05 R8 as v9 Canonical)

**Variation axes**: All three v9 ceiling criteria active: output format (CAN+CANNOT bidirectional asymmetry + process-level impossibility at Pass 3 -- C-29), role sequence (dedicated positive search space block at Amendment 1 -- C-31), inertia framing (named-per-path aggregation gate -- C-32)
**Hypothesis**: V-05 R8 implements all three v9 ceiling criteria simultaneously. V-05 R9 is a faithful reproduction of V-05 R8 confirming it scores 100/100 on v9 criteria. The three criteria operate at structurally independent lifecycle positions: C-32 at pre-Phase 0, C-29 at Pass 3 (pre-Phase 4), C-31 at Amendment 1 (Phase 5). No cross-phase interference predicted. Expected: PASS C-29 (full asymmetry argument with process-level impossibility claim), PASS C-31 (dedicated labeled block structurally distinct from Why block), PASS C-32 (gate names all three canonical paths at the closure event).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path and closed by canonical name in an aggregation gate -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with an enumerated positive search space. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three ceiling criteria active: bidirectional pre-fill impossibility asymmetry at Pass 3 (C-29), dedicated positive diagnostic targets at Amendment 1 (C-31), named-per-path aggregation gate at inertia close (C-32).

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and then close all three by canonical name before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to Phase 0.

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

*Why quoted evidence rather than Y/N -- structural asymmetry:* A Y/N integration status can be assigned in the same cognitive pass as Pass 1 coupling and Pass 2 bridge composition -- before the merge has been executed. The Y/N columns can be prefilled in advance; they do not require the merged paragraph to exist. A verbatim extract from merged prose cannot be written before the merge is executed: the text does not yet exist. This asymmetry is the structural reason for the format change. When the integration column requires a quoted extract from merged prose, completing all four columns in a single pre-merge pass is structurally impossible -- the extract column cannot be filled until after Phase 3 is complete. A quoted extract is evidence that the merge was completed and the paragraph was read; a Y checkbox is not.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*
- **Background epistemic register**: Does the Background use observational or domain-survey language when the paper type is theoretical? Does it use conceptual-landscape language when the paper type is empirical? A register mismatch signals a paper type that has not propagated into the draft.
- **Claim scope relative to Method**: Is the Claim stronger than what the Method and Result can establish? A Claim of "we demonstrate that X causes Y" requires causal evidence; "we found X associated with Y" does not. Overclaiming in the Claim section is a reviewer flag that survives all four targeted amendments.
- **Contribution incrementality framing**: Would a reviewer read the Claim as "the authors did more of something" rather than "the authors resolved something that prior work could not resolve"? Does the abstract communicate the necessity of this paper, not just its content?
- **Method scope adequacy**: Is the stated scope (sample size, dataset characteristics, model type) sufficient to support the Claim's strength? Scope inadequacy makes the Result uninterpretable regardless of quantification.

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
