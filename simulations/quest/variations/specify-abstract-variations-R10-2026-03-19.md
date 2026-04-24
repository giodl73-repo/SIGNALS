**R10 variations written** to `simulations/quest/variations/specify-abstract-variations-R10-2026-03-19.md`.

---

## R10 Summary

Since V-05 R9 is already at 100/100 on v9, R10 probes for new ceiling behaviors above the established C-29/C-31/C-32 layer. Three single-axis variations, one double, one full synthesis:

| ID | Axis | New behavior | v9 Predicted | v10 Candidate |
|----|------|-------------|--------------|---------------|
| **V-01** | Lifecycle emphasis | **Phase sequence lock** -- pre-Phase-0 block commits to sequential phase execution and names the incremental card fill order | ~100 | C-33 |
| **V-02** | Output format | **Positive-space structural asymmetry** -- CAN/CANNOT argument in the `*Where to look instead*` block header, explaining why independent auditability requires the separate block | ~100 | C-34 |
| **V-03** | Role sequence | **Per-excluded-category verification** -- after naming the weakness, confirm "This is NOT Gap sharpening: confirmed..." for each excluded slot (mirrors per-path inertia confirmation at Amendment 1) | ~100 | C-35 |
| **V-04** | V-01 + V-02 | Phase seq lock + positive-space asymmetry; category verif absent | ~100 | C-33 + C-34 |
| **V-05** | Full synthesis | All three R10 behaviors active alongside C-29/C-31/C-32 | ~100 | All three |

**R10 decision rule**: If scoring distinguishes any variation from V-05, the differentiating behavior becomes a v10 criterion candidate. If all five score identically, v9 is confirmed as the terminal rubric and V-05 R9 is the production skill.
| **V-01** | Phase sequence lock | YES | NO | NO | ~100 | Potential C-33 |
| **V-02** | Positive-space asymmetry | NO | YES | NO | ~100 | Potential C-34 |
| **V-03** | Category verification step | NO | NO | YES | ~100 | Potential C-35 |
| **V-04** | V-01 + V-02 | YES | YES | NO | ~100 | C-33 + C-34 |
| **V-05** | Full synthesis | YES | YES | YES | ~100 | All three |

**R10 scoring strategy**: All five variations start from V-05 R9 (100/100 on v9). If the new structural behaviors reveal rubric gaps -- e.g., a scorer can distinguish V-01 from V-05 on a dimension not captured by v9 criteria -- that gap becomes a v10 rubric update. If all five score identically, R10 confirms the rubric is at ceiling.

---

## V-01 -- Phase Sequence Lock: Explicit Ordering Guarantee Before Phase 0

**Variation axis**: Lifecycle emphasis (a pre-Phase-0 ordering guarantee block declares all five phases execute in declared sequence and no phase may be entered before its predecessor is complete; this is structurally distinct from the inertia declaration which addresses which paths are avoided -- the sequence lock addresses the order in which the phases run)
**Hypothesis**: V-05 R9 confirms path selection (inertia declaration) and positive search space (Amendment 1 block) and integration evidence (Pass 3). A phase sequence lock targets a different lifecycle risk: running phases out of order or skipping a phase entirely (writing the abstract before acquiring signals; running the merge before all five coupling boundaries are resolved). A dedicated sequence lock block -- positioned between the inertia declaration and Phase 0 -- names the five phases in order and requires explicit commitment to sequential execution. Expected: all v9 criteria still pass (the lock is an addition, not a replacement); new behavior introduced that v9 cannot score.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist and a phase sequence lock -- both closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with an enumerated positive search space. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three ceiling criteria active: bidirectional pre-fill impossibility asymmetry at Pass 3 (C-29), dedicated positive diagnostic targets at Amendment 1 (C-31), named-per-path aggregation gate at inertia close (C-32).

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and then close all three by canonical name before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to phase sequence lock.

---

**Phase sequence lock -- execution order commitment.** Before Phase 0 begins, confirm the five phases execute in declared sequence. A phase may not begin before its predecessor is complete. This lock addresses execution order risk -- distinct from path selection risk (addressed above). The five phases in required order:

1. **Phase 0** -- Paper type declaration. Must complete before Phase 1.
2. **Phase 1** -- Signal acquisition. Must complete before Phase 2.
3. **Phase 2** -- Coverage draft (gap-first order). Must complete before Pass 1.
4. **Pass 1 / Pass 2 / Pass 3** -- Boundary quality card (three incremental passes). All three passes must complete before Phase 4.
5. **Phase 4** -- Journal variant. Must complete before Phase 5.

*Why a phase sequence lock matters:* The three-pass boundary quality card is designed to be filled incrementally -- Pass 1 fills coupling, Pass 2 fills bridge type and phrase, Pass 3 fills integration with quoted evidence. A card completed in a single pre-merge pass defeats the C-26 and C-29 ceilings by pre-filling all columns before the merged paragraph exists. Committing to sequential execution before Phase 0 closes the batch-fill shortcut at the process level, not just at the column level.

> Confirm you will NOT execute phases out of declared sequence: [I will complete each phase before beginning the next. The boundary quality card columns will be filled one pass at a time in the sequence: coupling (Pass 1) -> bridge type and phrase (Pass 2) -> integration with quoted evidence (Pass 3).]

> Phase sequence lock: closed. Proceed to Phase 0.

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

---

## V-02 -- Positive-Space Structural Asymmetry: CAN/CANNOT Argument for the Dedicated Block

**Variation axis**: Output format (Amendment 1 positive search space block includes a C-29-style structural asymmetry argument explaining WHY the block must be structurally separate from the Why constraint block -- a Why block CAN be read together with the exclusion constraint in a single pass; the positive-space block CANNOT serve as the Why block without collapsing the two cognitive tasks into one)
**Hypothesis**: C-31 requires the positive search space to appear as a dedicated named block. V-02 adds an explicit structural asymmetry argument explaining the separation -- mirroring the C-29 argument at Pass 3. The argument is: a Why block that embeds positive targets CAN be satisfied without independently auditing the positive search space (both tasks are done in one pass); a dedicated block CANNOT be bypassed when auditing the constraint rationale (they are independently auditable events). Expected: all v9 criteria still pass; new behavior introduced at Amendment 1 that v9's C-31 does not score (C-31 requires a dedicated block; the asymmetry argument explaining why the block is separate is above C-31).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path and closed by canonical name in an aggregation gate -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block and asymmetry argument. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three ceiling criteria active: bidirectional pre-fill impossibility asymmetry at Pass 3 (C-29), dedicated positive diagnostic targets with structural independence argument at Amendment 1 (C-31 extended), named-per-path aggregation gate at inertia close (C-32).

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with structurally independent positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. When both are in the same block, a reader auditing the constraint rationale is simultaneously auditing the positive targets -- the two tasks cannot be independently verified. A dedicated block makes the positive search space independently auditable: a reader can confirm the constraint is stated and separately confirm the positive targets are named, without the two audits interfering.

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

## V-03 -- Self-Diagnosis Category Verification Step: Explicit Per-Category Confirmation

**Variation axis**: Role sequence (Amendment 1 adds a structured per-category verification step after the Weakness category is named -- "Verify this is NOT Gap sharpening: confirmed. Verify this is NOT Result quantification: confirmed." etc. -- an explicit confirmation per excluded category rather than a single constraint statement)
**Hypothesis**: C-25 requires the weakness to fall outside the four fixed categories; C-31 requires the positive search space as a dedicated block. V-03 adds a structured per-category verification step above both: after naming the weakness category, verify per excluded category that the named weakness is not in that slot. This mirrors the per-path confirmation structure of the inertia declaration (C-27) at the Amendment 1 level. Expected: all v9 criteria still pass; new behavior introduced that v9 cannot score (C-25 requires the diagnosis to be outside fixed categories but does not require explicit per-category exclusion confirmation).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist -- three named paths confirmed per path and closed by canonical name in an aggregation gate -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a dedicated positive search space block and per-excluded-category verification. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three ceiling criteria active: bidirectional pre-fill impossibility asymmetry at Pass 3 (C-29), dedicated positive diagnostic targets at Amendment 1 (C-31), named-per-path aggregation gate at inertia close (C-32).

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with per-excluded-category verification)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Name the weakness category first. Then verify per excluded category that the named weakness is not in that slot.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Per-excluded-category verification:*
> This is NOT Gap sharpening (the named weakness does not target the Gap sentence's specificity): [confirmed / explain if uncertain]
> This is NOT Result quantification (the named weakness does not target the Result's numeric evidence): [confirmed / explain if uncertain]
> This is NOT Implication tightening (the named weakness does not target modal hedges or vague enabling actions): [confirmed / explain if uncertain]
> This is NOT Prose coherence (the named weakness does not target transition quality or flow): [confirmed / explain if uncertain]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch. Per-excluded-category verification closes the ambiguity case: a weakness named "the claim is not sufficiently specific" could be heard as Gap sharpening or as Claim scope. Verifying per category requires the named weakness to be distinguished from each slot independently, not just stated as "other."

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

## V-04 -- Phase Sequence Lock + Positive-Space Asymmetry (V-01 + V-02 Combined)

**Variation axes**: Lifecycle emphasis (phase sequence lock from V-01) + Output format (positive-space structural asymmetry argument from V-02); per-excluded-category verification not active
**Hypothesis**: V-04 tests the two process-level additions (phase sequence lock + positive-space asymmetry argument) in combination without the per-category verification. Both operate at structurally independent lifecycle positions: phase sequence lock is at pre-Phase-0, positive-space asymmetry is at Amendment 1. Expected: PASS all v9 criteria + V-01 new behavior (phase sequence lock) + V-02 new behavior (positive-space CAN/CANNOT argument); V-03 new behavior (per-category verification) absent.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist and a phase sequence lock -- both closed before Phase 0 -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block and asymmetry argument. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three ceiling criteria active: bidirectional pre-fill impossibility asymmetry at Pass 3 (C-29), dedicated positive diagnostic targets with structural independence argument at Amendment 1 (C-31 extended), named-per-path aggregation gate at inertia close (C-32). Phase sequence lock active as new process-level commitment device.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and then close all three by canonical name before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to phase sequence lock.

---

**Phase sequence lock -- execution order commitment.** Before Phase 0 begins, confirm the five phases execute in declared sequence. A phase may not begin before its predecessor is complete. This lock addresses execution order risk -- distinct from path selection risk (addressed above). The five phases in required order:

1. **Phase 0** -- Paper type declaration. Must complete before Phase 1.
2. **Phase 1** -- Signal acquisition. Must complete before Phase 2.
3. **Phase 2** -- Coverage draft (gap-first order). Must complete before Pass 1.
4. **Pass 1 / Pass 2 / Pass 3** -- Boundary quality card (three incremental passes). All three passes must complete before Phase 4.
5. **Phase 4** -- Journal variant. Must complete before Phase 5.

*Why a phase sequence lock matters:* The three-pass boundary quality card is designed to be filled incrementally -- Pass 1 fills coupling, Pass 2 fills bridge type and phrase, Pass 3 fills integration with quoted evidence. A card completed in a single pre-merge pass defeats the C-26 and C-29 ceilings by pre-filling all columns before the merged paragraph exists. Committing to sequential execution before Phase 0 closes the batch-fill shortcut at the process level, not just at the column level.

> Confirm you will NOT execute phases out of declared sequence: [I will complete each phase before beginning the next. The boundary quality card columns will be filled one pass at a time in the sequence: coupling (Pass 1) -> bridge type and phrase (Pass 2) -> integration with quoted evidence (Pass 3).]

> Phase sequence lock: closed. Proceed to Phase 0.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with structurally independent positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Those categories are covered by Amendments 2-5. Name the weakness category first, then the specific element.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. When both are in the same block, a reader auditing the constraint rationale is simultaneously auditing the positive targets -- the two tasks cannot be independently verified. A dedicated block makes the positive search space independently auditable: a reader can confirm the constraint is stated and separately confirm the positive targets are named, without the two audits interfering.

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

## V-05 -- Full Synthesis: Phase Sequence Lock + Positive-Space Asymmetry + Category Verification

**Variation axes**: All three R10 new behaviors active: lifecycle emphasis (phase sequence lock -- V-01), output format (positive-space structural asymmetry argument -- V-02), role sequence (per-excluded-category verification step -- V-03). All three v9 ceiling criteria also active (C-29, C-31, C-32).
**Hypothesis**: V-05 combines all three R10 novel structural behaviors simultaneously. The three new behaviors operate at structurally independent lifecycle positions: phase sequence lock (pre-Phase-0 between inertia close and Phase 0), positive-space asymmetry (Amendment 1, in the Where-to-look block header), per-category verification (Amendment 1, after the Weakness category is named). No cross-phase interference predicted. Expected: PASS all v9 criteria + all three R10 new behaviors. If the rubric is at ceiling (no new criteria extractable from these behaviors), this confirms v9 as the terminal rubric version. If any R10 behavior is distinguishable at scoring time, it becomes a v10 candidate criterion.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist and a phase sequence lock -- both closed before Phase 0 -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block (with asymmetry argument) and per-excluded-category verification. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. All ceiling criteria active: C-29 (bidirectional asymmetry at Pass 3), C-31 (dedicated positive-space block with independence argument at Amendment 1), C-32 (named-per-path gate at inertia close). R10 additions: phase sequence lock, positive-space structural asymmetry argument, per-excluded-category verification.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and then close all three by canonical name before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to phase sequence lock.

---

**Phase sequence lock -- execution order commitment.** Before Phase 0 begins, confirm the five phases execute in declared sequence. A phase may not begin before its predecessor is complete. This lock addresses execution order risk -- distinct from path selection risk (addressed above). The five phases in required order:

1. **Phase 0** -- Paper type declaration. Must complete before Phase 1.
2. **Phase 1** -- Signal acquisition. Must complete before Phase 2.
3. **Phase 2** -- Coverage draft (gap-first order). Must complete before Pass 1.
4. **Pass 1 / Pass 2 / Pass 3** -- Boundary quality card (three incremental passes). All three passes must complete before Phase 4.
5. **Phase 4** -- Journal variant. Must complete before Phase 5.

*Why a phase sequence lock matters:* The three-pass boundary quality card is designed to be filled incrementally -- Pass 1 fills coupling, Pass 2 fills bridge type and phrase, Pass 3 fills integration with quoted evidence. A card completed in a single pre-merge pass defeats the C-26 and C-29 ceilings by pre-filling all columns before the merged paragraph exists. Committing to sequential execution before Phase 0 closes the batch-fill shortcut at the process level, not just at the column level.

> Confirm you will NOT execute phases out of declared sequence: [I will complete each phase before beginning the next. The boundary quality card columns will be filled one pass at a time in the sequence: coupling (Pass 1) -> bridge type and phrase (Pass 2) -> integration with quoted evidence (Pass 3).]

> Phase sequence lock: closed. Proceed to Phase 0.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with per-excluded-category verification and structurally independent positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Name the weakness category first. Then verify per excluded category that the named weakness is not in that slot.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Per-excluded-category verification:*
> This is NOT Gap sharpening (the named weakness does not target the Gap sentence's specificity): [confirmed / explain if uncertain]
> This is NOT Result quantification (the named weakness does not target the Result's numeric evidence): [confirmed / explain if uncertain]
> This is NOT Implication tightening (the named weakness does not target modal hedges or vague enabling actions): [confirmed / explain if uncertain]
> This is NOT Prose coherence (the named weakness does not target transition quality or flow): [confirmed / explain if uncertain]

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch. Per-excluded-category verification closes the ambiguity case: a weakness named "the claim is not sufficiently specific" could be heard as Gap sharpening or as Claim scope. Verifying per category requires the named weakness to be distinguished from each slot independently, not just stated as "other."

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. When both are in the same block, a reader auditing the constraint rationale is simultaneously auditing the positive targets -- the two tasks cannot be independently verified. A dedicated block makes the positive search space independently auditable: a reader can confirm the constraint is stated and separately confirm the positive targets are named, without the two audits interfering.

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

## Predicted v9 Scores and v10 Criterion Candidates

| Variation | v9 Predicted | C-29 | C-31 | C-32 | R10 new behavior | Notes |
|-----------|-------------|------|------|------|------------------|-------|
| V-01 | ~100 | PASS | PASS | PASS | Phase seq lock | +phase sequence lock block between inertia close and Phase 0 |
| V-02 | ~100 | PASS | PASS | PASS | Pos-space asymmetry | +CAN/CANNOT argument in pos-space block header |
| V-03 | ~100 | PASS | PASS | PASS | Category verif | +per-excluded-category verification after weakness named |
| V-04 | ~100 | PASS | PASS | PASS | V-01 + V-02 | seq lock + asymmetry combined; verif absent |
| V-05 | ~100 | PASS | PASS | PASS | All three | Full synthesis |

**v10 criterion candidates** (if R10 scoring distinguishes variations):

- **C-33 (potential)**: Phase sequence lock names all card passes in declared fill order at a pre-Phase-0 commitment event. Mirrors C-32 (named-per-path gate) at the process-ordering level. The CAN/CANNOT structural argument: batch-filling the card CAN happen without a sequence lock (all columns are individually fillable at any point); batch-filling CANNOT happen when the sequence lock names the pass order and requires commitment before Phase 0. Source: V-01 signal.

- **C-34 (potential)**: Positive-space block includes a structural asymmetry argument explaining why the block is independently auditable. Mirrors C-29 (Pass 3 CAN/CANNOT argument) at the Amendment 1 positive-space block. The argument: a Why block that embeds positive targets CAN be read in one pass; a dedicated block CANNOT collapse the two tasks (auditing the exclusion constraint and auditing the positive targets are independently verifiable events). Source: V-02 signal.

- **C-35 (potential)**: Self-diagnosis category verification names each excluded category and confirms the weakness is not in that slot -- a per-category closure event. Mirrors C-27 (per-path inertia confirmation) at the Amendment 1 category-selection level. The argument: stating "outside the four categories" CAN be satisfied by assertion without per-category examination; per-category verification CANNOT be bypassed without independently confirming each slot. Source: V-03 signal.

**If all five score identically at v9**: v9 is the terminal rubric. V-05 R9 (canonical 100/100) is the production skill. No v10 update warranted. The three R10 new behaviors are additive quality improvements that do not create new auditable signals distinct from existing criteria.
