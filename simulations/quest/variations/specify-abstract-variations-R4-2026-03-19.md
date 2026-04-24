Written to `simulations/quest/variations/specify-abstract-variations-R4-2026-03-19.md`.

---

## R4 Variations Summary

**Context**: V-05 R3 already scores 100/100 under the v4 rubric (the new C-17 and C-18 mechanisms were already present in V-05 R3). R4 variations are not competing for v4 score improvements — they are probing for **v5 candidate signals**.

| ID | Axis | New signal probed |
|----|------|-------------------|
| **V-01** | Lifecycle: **Phase 0 pre-flight paper type declaration** | Paper type as a planning parameter for all 6 sections (not just a Claim tense mechanism). Background register, Gap framing, Implication form all shift with type. v5 candidate. |
| **V-02** | Output format: **bridge semantic type labeling** (Phase 2b gains Type column) | Constrained vocabulary (contrast / causation / resolution / escalation / application) forces relationship identification before phrase composition. This is the C-19 candidate: labeled boundary pairs with semantic type. |
| **V-03** | Role sequence: **Phase 2c section coupling verification** | After drafting, before bridging — a 5-row checklist verifies each section pair is semantically coupled, not just locally correct. Catches drift that gap-first order cannot prevent. |
| **V-04** | Combination: V-01 + V-02 axes | Pre-flight type planning + bridge semantic precision. Tests whether type-aware drafting makes the bridge type assignments more natural. |
| **V-05** | Full synthesis: all three new axes on V-05 R3 base | Tests whether Phase 0 + Phase 2c + Phase 2b extension are additive or whether any is redundant when gap-first + constraint reasoning are already present. |

**Key design decisions:**
- All 5 variations preserve the full V-05 R3 mechanism set to hold v4 score at 100
- Phase 2c (coupling verification) is ordered **before** Phase 2b (bridges) — verification must complete before bridge composition begins
- The semantic type vocabulary is constrained to 5 types with non-overlap guidance to prevent formulaic assignment
- V-05 is explicitly flagged as the longest prompt of any round — Phase 5 attention load is the predicted binding constraint
distinguish — predicted v4 score is 100 for all five. The signal value is in what v4 does NOT capture.

| Variation | v4 Predicted | New signals probed |
|-----------|-------------|---------------------|
| V-01 | ~100 | Paper-type as planning parameter for all sections, not just Claim |
| V-02 | ~100 | Semantic bridge type labeling — labeled-boundary C-19 candidate |
| V-03 | ~100 | Section coupling verification — catches misalignment before merge |
| V-04 | ~100 | Type-planning + bridge precision combination |
| V-05 | ~100 | All three axes — additive vs. redundant at the ceiling |

**Key trade-offs:** V-01 adds Phase 0 length but no structural risk — type declaration is fully separable from signal acquisition. V-02 extends Phase 2b with a type column; risk is formulaic type assignment (every boundary labeled "causation"). V-03 adds Phase 2c with a coupling checklist; risk is rote self-affirmation rather than substantive revision. V-05 is the longest prompt of any round — Phase 0 + Phase 2c + Phase 2b expansion on top of the full V-05 R3 body. Attention load at Phase 5 may be the binding constraint.

---

## V-01 — Pre-flight Paper Type Declaration

**Variation axis**: Lifecycle emphasis (Phase 0 added before signal acquisition — paper type declared as the first act, before any content is read or written)
**Hypothesis**: V-02 and V-04 (R3) showed that a forced "Paper type: empirical / theoretical" declaration at the Claim step earns C-09 full PASS (C-18). But the declaration comes after the draft has already begun. Declaring paper type as Phase 0 makes it a planning parameter: Background register, Gap framing strength, Method scope, and Implication form all differ between empirical and theoretical papers. The pre-flight declaration gives the entire draft a consistent epistemic register, not just correct Claim tense. Probes whether section-level quality improves when type is declared first — v5 candidate: paper type as planning parameter (not just Claim mechanism).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — composes explicit connective bridges between all section boundaries, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs tense, register, and framing for the entire abstract.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question feel important. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

Declare paper type now. Write: `Paper type: empirical` or `Paper type: theoretical`.

> Paper type: [empirical / theoretical]

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 — do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim — a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? Name one concrete enabling action. For empirical papers: name a practitioner decision enabled. For theoretical papers: name a research or design question now tractable.

> [Implication sentence]

---

**Phase 2b — Bridge composition.** Before merging, compose one short connective phrase (3-8 words) for each of the five section boundaries. These are the logical handoffs between sections — compose them as purposeful transitions, not stock connectors ("however", "in this paper").

| Boundary | Bridge phrase |
|----------|--------------|
| Background -> Gap | [names the specific gap tension created by Background] |
| Gap -> Claim | [names what this paper does in response to the Gap] |
| Claim -> Method | [connects the contribution claim to the how] |
| Method -> Result | [transitions from approach to finding] |
| Result -> Implication | [moves from what was found to what it enables] |

These bridge phrases are the merge glue for Phase 3. Incorporate them at section boundaries during the merge step.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
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

## V-02 — Bridge Semantic Type Labeling

**Variation axis**: Output format (Phase 2b bridge table gains a Type column — each bridge phrase is tagged with a constrained semantic relationship type before the phrase is written)
**Hypothesis**: V-03 and V-05 (R3) proved Phase 2b is the structural mechanism for C-12 PASS. The current Phase 2b instruction warns against stock connectors but does not specify what makes a connector non-stock. Adding a constrained type vocabulary (contrast / causation / resolution / escalation / application) forces the model to identify the logical relationship before composing the phrase — preventing the pattern where a phrase is syntactically original but semantically generic. This is the C-19 candidate mechanism noted in the v4 rubric: "bridge table with labeled boundary pairs." The type-first instruction creates a structural constraint, not just a stylistic suggestion.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals — Gap first so Background scaffolds toward a known target — composes explicit connective bridges with semantic type labels between all section boundaries, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. The draft phase targets coverage only. The bridge phase produces typed logical glue for merge. The amendment phase carries the full precision load.

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Identify paper type, then write: active voice, past tense if empirical ("we found"), present tense if theoretical ("we show").
> Paper type: empirical / theoretical
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim — a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? Name one concrete enabling action.

> [Implication sentence]

---

**Phase 2b — Bridge composition with semantic type labeling.** Before merging, compose one short connective phrase (3-8 words) for each of the five section boundaries. For each boundary, identify the semantic relationship type first — it constrains what phrase is appropriate. Choose from the vocabulary below.

**Semantic type vocabulary:**
- **contrast** — The prior section established something; the next section names what it fails to explain, resolve, or predict. ("yet it remains unclear whether", "but the mechanism remains unknown")
- **causation** — The prior section created the exact conditions that make the next section's claim necessary or direct. ("we therefore demonstrate that", "this directly enables")
- **resolution** — The prior section named a problem or question; the next section names the specific mechanism or tool used to address it. ("using a controlled experiment with", "by applying X to")
- **escalation** — The prior section stated what was expected or sufficient; the next section names a finding that exceeds or sharpens that baseline. ("finding not merely X but Y", "extending beyond X to")
- **application** — The prior section reported a finding; the next section converts it to a concrete action, decision, or design implication. ("enabling practitioners to", "allowing designers to now")

| Boundary | Type | Bridge phrase |
|----------|------|--------------|
| Background -> Gap | [contrast / causation / resolution / escalation / application] | [phrase that expresses this relationship] |
| Gap -> Claim | [type] | [phrase] |
| Claim -> Method | [type] | [phrase] |
| Method -> Result | [type] | [phrase] |
| Result -> Implication | [type] | [phrase] |

Do not use the same type for more than two consecutive boundaries. If a boundary fits two types, choose the one that produces the more specific phrase.

These bridge phrases are the merge glue for Phase 3. Incorporate them at section boundaries during the merge step.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-03 — Section Coupling Verification

**Variation axis**: Role sequence (Phase 2c added after draft, before bridge composition — verifies semantic coupling at each adjacent section boundary before bridges are composed)
**Hypothesis**: Gap-first draft order (C-14) ensures Background is written toward a known target, but does not verify that the finished Background actually creates the gap it was aimed at. Thin signal coverage or topic drift can produce sections that are locally correct but semantically disconnected at the boundary. Phase 2c adds a five-row coupling checklist: for each adjacent section pair, one diagnostic question checks whether the upstream section creates the exact conditions the downstream section requires. WEAK or REVISE ratings trigger targeted revision before bridge composition. This catches structural misalignment earlier than Amendment 4 (prose coherence), which operates after merge and cannot revise section content.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals — Gap first so Background scaffolds toward a known target — verifies semantic coupling at each section boundary before composing bridges, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. The draft phase targets coverage only. The coupling check catches structural misalignment before merge. The bridge phase produces the logical glue for merge. The amendment phase carries the full precision load.

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Identify paper type, then write: active voice, past tense if empirical ("we found"), present tense if theoretical ("we show").
> Paper type: empirical / theoretical
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim — a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? Name one concrete enabling action.

> [Implication sentence]

---

**Phase 2c — Section coupling verification.** After drafting all six sections and before composing bridges, verify that each adjacent section pair is semantically coupled. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a different or more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

If any boundary is WEAK: revise the weaker of the two sections before proceeding to bridge composition. If REVISE: rewrite the weaker section now, then re-verify before continuing.

---

**Phase 2b — Bridge composition.** Before merging, compose one short connective phrase (3-8 words) for each of the five section boundaries. These are the logical handoffs between sections — compose them as purposeful transitions, not stock connectors ("however", "in this paper").

| Boundary | Bridge phrase |
|----------|--------------|
| Background -> Gap | [names the specific gap tension created by Background] |
| Gap -> Claim | [names what this paper does in response to the Gap] |
| Claim -> Method | [connects the contribution claim to the how] |
| Method -> Result | [transitions from approach to finding] |
| Result -> Implication | [moves from what was found to what it enables] |

These bridge phrases are the merge glue for Phase 3. Incorporate them at section boundaries during the merge step.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-04 — Pre-flight Paper Type + Bridge Semantic Labels

**Variation axes**: Lifecycle emphasis (Phase 0 paper type pre-flight — V-01 axis) + output format (Phase 2b semantic type column — V-02 axis)
**Hypothesis**: V-01 makes paper type a planning parameter across all six sections. V-02 forces semantic precision at each bridge boundary. The two axes operate in different phases (Phase 0 vs. Phase 2b) with no structural overlap. The combination tests whether type-informed section drafting produces bridge phrases that are naturally more semantically purposeful — i.e., whether Phase 0 reduces the effort required by Phase 2b's type labeling, or whether they operate independently. If paper type is declared as a planning parameter, the Background-to-Gap boundary should more reliably produce a contrast relationship and the Result-to-Implication boundary should more reliably produce an application relationship.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — composes explicit connective bridges with semantic type labels between all section boundaries, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs tense, register, and framing for the entire abstract.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue"). Implication names what the framework makes tractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now.
> Paper type: [confirmed from Phase 0]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim — a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision. For theoretical: name a research question now tractable.

> [Implication sentence]

---

**Phase 2b — Bridge composition with semantic type labeling.** Before merging, compose one short connective phrase (3-8 words) for each of the five section boundaries. Identify the semantic type first — it constrains what phrase is appropriate.

**Semantic type vocabulary:**
- **contrast** — Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** — Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** — Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** — Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** — Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

| Boundary | Type | Bridge phrase |
|----------|------|--------------|
| Background -> Gap | [type] | [phrase] |
| Gap -> Claim | [type] | [phrase] |
| Claim -> Method | [type] | [phrase] |
| Method -> Result | [type] | [phrase] |
| Result -> Implication | [type] | [phrase] |

Do not use the same type for more than two consecutive boundaries.

These bridge phrases are the merge glue for Phase 3. Incorporate them at section boundaries during the merge step.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
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

## V-05 — Full Synthesis: Pre-flight Type + Bridge Semantic Labels + Coupling Verification

**Variation axes**: All three new single-axis additions combined: lifecycle emphasis (Phase 0 type declaration — V-01) + output format (Phase 2b semantic type column — V-02) + role sequence (Phase 2c coupling verification — V-03) — on V-05 R3 base (all-section Why:, gap-first, bridge phase, paper-type forced declaration, hardened 4-amendment)
**Hypothesis**: The three new axes operate in independent phases: Phase 0 (pre-draft planning), Phase 2c (post-draft verification), and Phase 2b extension (bridge precision). None conflicts with the R3 V-05 base. If all three are load-bearing, this variation surfaces the highest-fidelity prompting pattern and generates the richest v5 candidate signals. If the coupling check (V-03) is redundant when gap-first + constraint reasoning are both present, that is also a finding. Risk: this is the longest prompt of any round — Phase 0, Phase 2c, and Phase 2b expansion sit on top of the full V-05 R3 body. Attention load at Phase 5 may be the binding constraint.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling at each boundary, composes explicit connective bridges with semantic type labels, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. The coupling verification catches misalignment before bridges are composed. The bridge phase produces typed logical glue for merge. The amendment phase carries the full precision load.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue"). Implication names what the framework makes tractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now.
> Paper type: [confirmed from Phase 0]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim — a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision. For theoretical: name a research question now tractable.

> [Implication sentence]

---

**Phase 2c — Section coupling verification.** After drafting all six sections and before composing bridges, verify semantic coupling at each adjacent section boundary. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism used to establish the Claim — not a generic description? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

If any boundary is WEAK: revise the weaker section before proceeding. If REVISE: rewrite the weaker section now.

---

**Phase 2b — Bridge composition with semantic type labeling.** Compose one short connective phrase (3-8 words) for each of the five section boundaries. Identify the semantic type first — it constrains what phrase is appropriate.

**Semantic type vocabulary:**
- **contrast** — Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** — Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** — Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** — Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** — Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

| Boundary | Type | Bridge phrase |
|----------|------|--------------|
| Background -> Gap | [type] | [phrase] |
| Gap -> Claim | [type] | [phrase] |
| Claim -> Method | [type] | [phrase] |
| Method -> Result | [type] | [phrase] |
| Result -> Implication | [type] | [phrase] |

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]