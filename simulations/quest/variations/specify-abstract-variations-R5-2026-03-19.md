Written to `simulations/quest/variations/specify-abstract-variations-R5-2026-03-19.md`.

---

## R5 Variations Summary

**Context**: V-05 R4 scores 100/100 under v5. R5 variations probe for v6 candidates by pushing past the current ceiling.

| ID | Axis | Signal probed |
|----|------|---------------|
| **V-01** | Lifecycle: **Phase 2c structured revision directive** | When WEAK/REVISE status is found, open-ended "revise the weaker section" is replaced by a named Boundary/Deficient-section/Deficiency/Before/After/Re-verify directive. Parallel format to Phase 5 amendments. v6 candidate: C-21 enforcement depth. |
| **V-02** | Output format: **Phase 3b bridge integration audit** | After merge, a new Phase 3b table verifies each Phase 2b bridge phrase survived the merge step — flags bridges replaced by stock connectors. v6 candidate: bridge-to-prose integration as a named criterion. |
| **V-03** | Lifecycle: **5th self-diagnosis amendment** | Phase 5 gains a terminal Amendment 5: model reads the post-amendment abstract and diagnoses the single weakest remaining element, unconstrained by fixed categories. v6 candidate: open-ended terminal quality sweep. |
| **V-04** | V-01 + V-02 | Structured coupling revision + bridge integration audit. Pre-merge enforcement and post-merge verification tested together. |
| **V-05** | Full synthesis | All three axes on V-05 R4 base. Tests whether Phase 2c depth + Phase 3b integration + Amendment 5 sweep are additive or any is redundant at the ceiling. |

**Key design decisions:**
- All variations preserve the full V-05 R4 mechanism set to hold v5 score at 100
- V-01's revision directive mirrors the Phase 5 amendment format (Boundary / Deficient section / Deficiency / Before / After / Re-verify) — deliberate parallel structure
- V-02's Phase 3b is ordered between Phase 3 and Phase 4 — bridge verification happens before journal adjustment, so journal adaptation applies to a bridge-faithful merge
- V-03's Amendment 5 explicitly must not repeat a target already resolved by amendments 1-4 — prevents rote self-affirmation
- V-05 is the longest prompt of any round; attention load at Phase 5 is the predicted binding constraint
ter / Re-verify) — parallel structure reduces cognitive load
- V-02's Phase 3b is ordered after Phase 3 and before Phase 4 — verification precedes journal adjustment so journal adaptation applies to a bridge-faithful merge
- V-03's 5th amendment is terminal — it runs after amendments 1-4 and operates on the post-amendment text, not the pre-amendment draft
- V-05 is the longest prompt of any round — V-01 + V-02 + V-03 extensions sit on top of the full V-05 R4 body

**Predicted v5 scores:**

| Variation | v5 Predicted | New signals probed |
|-----------|-------------|---------------------|
| V-01 | ~100 | C-21 enforcement depth — does structured WEAK/REVISE directive improve section coupling quality? |
| V-02 | ~100 | Bridge-to-prose integration — are Phase 2b bridges systematically dropped at merge? |
| V-03 | ~100 | Post-amendment residual — do fixed amendment targets leave a diagnosable weakness? |
| V-04 | ~100 | Pre-merge enforcement + post-merge verification combination |
| V-05 | ~100 | All three axes — additive vs. redundant at the V-05 R4 ceiling |

**Key trade-offs:** V-01 adds Phase 2c verbosity; risk is that structured directive becomes rote when all boundaries are COUPLED (which is the common case post-gap-first). V-02 adds a Phase 3b table; risk is that bridge phrases that were incorporated in modified form are flagged as N when they should be Y. V-03 adds a 5th amendment; risk is that the self-diagnosis repeats a target already covered by amendments 1-4 when the model lacks genuine self-awareness of residual weakness. V-05 is the longest prompt — attention load at Phase 5 may compress amendment quality.

---

## V-01 — Phase 2c Structured Revision Directive

**Variation axis**: Lifecycle emphasis (Phase 2c WEAK/REVISE response structured as a formal before/after directive — parallel format to Phase 5 amendments)
**Hypothesis**: C-21 requires that WEAK/REVISE status triggers section-level revision before bridge composition. The V-05 R4 instruction is open-ended: "revise the weaker section before proceeding." An open-ended instruction is complied with nominally — a minimal word change counts as revision. The structured directive forces: name the deficient section, state what property it lacks, show Before/After, and re-verify the coupling status. This parallels Phase 5's amendment format, which demonstrably improves revision quality (C-07, C-13). Probes: does structured enforcement at Phase 2c produce measurable improvement in section coupling quality beyond what gap-first order alone provides? v6 candidate: structured revision directive as a named coupling-enforcement mechanism.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling with structured revision directives when misalignment is found, composes explicit connective bridges with semantic type labels, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. The coupling verification catches and structures any fixes before bridges are composed.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

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
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Phase 2c — Section coupling verification with structured revision directives.** After drafting all six sections and before composing bridges, verify semantic coupling at each adjacent section boundary. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a different or more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding to bridge composition:

> Boundary: [name the boundary pair, e.g. Gap -> Claim]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

If the re-verified status is still WEAK: revise again and re-verify before proceeding. Do not proceed to bridge composition until all boundaries are COUPLED.

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

---

## V-02 — Phase 3b Bridge Integration Audit

**Variation axis**: Output format (Phase 3b added after merge — a bridge-to-prose integration audit that verifies each Phase 2b bridge phrase survived the merge step)
**Hypothesis**: Phase 2b forces deliberate bridge composition (C-20 mechanism). Phase 3 uses those phrases as "merge glue." But there is currently no verification that the bridge phrases were actually incorporated — a merge that substitutes stock connectors ("however", "therefore") for planned bridge phrases satisfies Phase 3's instruction surface without executing the intent. Phase 3b adds a five-row audit table: for each boundary, record the Phase 2b phrase, the actual connective used in the merged paragraph, and an integration flag. Any N triggers a paragraph revision restoring the bridge phrase. Probes: does systematic bridge drop-off occur during merge? v6 candidate: bridge-to-prose integration as a named post-merge criterion.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling at each boundary, composes explicit connective bridges with semantic type labels, audits bridge integration after merge, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. The bridge audit ensures that planned logical connections survive the merge step and appear in the final paragraph.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

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
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Phase 2c — Section coupling verification.** After drafting all six sections and before composing bridges, verify semantic coupling at each adjacent section boundary. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a different or more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

If any boundary is WEAK: revise the weaker of the two sections before proceeding to bridge composition. If REVISE: rewrite the weaker section now, then re-verify before continuing.

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

**Phase 3b — Bridge integration audit.** Verify that each Phase 2b bridge phrase was incorporated into the merged paragraph. For each boundary, identify the actual connective words used at that position in the merged text.

| Boundary | Phase 2b bridge phrase | Integrated? | Actual connective used in merged text |
|----------|------------------------|-------------|---------------------------------------|
| Background -> Gap | [phrase from Phase 2b] | Y / N | [the words appearing at this boundary in the merged paragraph] |
| Gap -> Claim | [phrase] | Y / N | [actual text] |
| Claim -> Method | [phrase] | Y / N | [actual text] |
| Method -> Result | [phrase] | Y / N | [actual text] |
| Result -> Implication | [phrase] | Y / N | [actual text] |

Integration is Y if the bridge phrase was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

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

## V-03 — 5th Self-Diagnosis Amendment

**Variation axis**: Lifecycle emphasis (Phase 5 gains a fifth amendment slot — model reads the post-amendment abstract, diagnoses the single weakest remaining element, and runs a targeted fix not constrained to a fixed category)
**Hypothesis**: Amendments 1-4 target fixed categories (Gap, Result, Implication, Prose). When the draft already satisfies these targets at a baseline level, the amendments become nominally compliant: a minor wording change earns Non-trivial: Y. The self-diagnosis amendment operates on the post-amendment text and identifies whatever weakness actually remains — it is not constrained to the four named categories. This catches systematic residuals: a Claim that is grammatically present but epistemically vague, a Method that names a technique but not a scope, a Background that is accurate but too generic. Probes: do fixed amendment targets leave a diagnosable residual? v6 candidate: open-ended terminal quality sweep as a named Phase 5 extension.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling at each boundary, composes explicit connective bridges with semantic type labels, then runs a hardened five-amendment pass: four targeted amendments plus a self-diagnosis sweep of the post-amendment abstract. The fifth amendment targets whatever weakness the model identifies after the first four are complete.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

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
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Phase 2c — Section coupling verification.** After drafting all six sections and before composing bridges, verify semantic coupling at each adjacent section boundary. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a different or more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

If any boundary is WEAK: revise the weaker of the two sections before proceeding to bridge composition. If REVISE: rewrite the weaker section now, then re-verify before continuing.

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

**Phase 5 — Five-amendment pass.** Amendments 1-4 are targeted at fixed categories. Amendment 5 is a self-diagnosis sweep of the post-amendment abstract. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial.

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

**Amendment 5 — Self-diagnosis**
Read the abstract after amendments 1-4. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. This should not repeat a target already fully resolved by amendments 1-4.
> Diagnosis: [name the weakest remaining element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]

---

## V-04 — Structured Revision Directive + Bridge Integration Audit

**Variation axes**: Lifecycle emphasis (Phase 2c structured revision directive — V-01 axis) + output format (Phase 3b bridge integration audit — V-02 axis)
**Hypothesis**: V-01 hardens Phase 2c enforcement: when WEAK/REVISE, a named before/after directive ensures the revision addresses a specific deficiency rather than a nominal word change. V-02 hardens Phase 3: a post-merge audit table checks that planned bridge phrases survived the merge step. The two axes operate at adjacent lifecycle positions (Phase 2c is pre-merge, Phase 3b is post-merge) with complementary concerns — coupling enforcement ensures the sections are semantically connected before bridges are composed; bridge integration verification ensures the connection is expressed in the final prose. The combination tests whether pre-merge structural integrity + post-merge connection fidelity are jointly necessary, or whether one subsumes the other.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling with structured revision directives when misalignment is found, composes explicit connective bridges with semantic type labels, audits bridge integration after merge, then runs a hardened four-amendment pass to reach final quality. Pre-merge: coupling is structurally verified and fixed. Post-merge: bridge integration is verified and restored if lost.

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

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
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Phase 2c — Section coupling verification with structured revision directives.** After drafting all six sections and before composing bridges, verify semantic coupling at each adjacent section boundary. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a different or more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

Do not proceed to bridge composition until all boundaries are COUPLED.

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

**Phase 3b — Bridge integration audit.** Verify that each Phase 2b bridge phrase was incorporated into the merged paragraph.

| Boundary | Phase 2b bridge phrase | Integrated? | Actual connective used in merged text |
|----------|------------------------|-------------|---------------------------------------|
| Background -> Gap | [phrase from Phase 2b] | Y / N | [text at this boundary in the merged paragraph] |
| Gap -> Claim | [phrase] | Y / N | [actual text] |
| Claim -> Method | [phrase] | Y / N | [actual text] |
| Method -> Result | [phrase] | Y / N | [actual text] |
| Result -> Implication | [phrase] | Y / N | [actual text] |

Integration is Y if the bridge phrase was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector that does not express the intended type relationship.

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

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

## V-05 — Full Synthesis: Structured Revision Directive + Bridge Integration Audit + 5th Self-Diagnosis Amendment

**Variation axes**: All three new single-axis additions combined: lifecycle emphasis (Phase 2c structured revision directive — V-01) + output format (Phase 3b bridge integration audit — V-02) + lifecycle emphasis (5th self-diagnosis amendment — V-03) — on V-05 R4 base (all-section Why:, gap-first, bridge semantic types, Phase 0, Phase 2c, hardened 4-amendment)
**Hypothesis**: The three new axes operate at three distinct lifecycle positions — Phase 2c (pre-bridge coupling enforcement), Phase 3b (post-merge bridge verification), and Phase 5 terminal (post-amendment quality sweep). None conflicts with the R4 V-05 base mechanisms. V-01 hardens the coupling check already present; V-02 audits a transition the current prompt leaves unverified; V-03 adds a terminal sweep after fixed amendments complete. If all three are load-bearing, this variation surfaces the highest-fidelity prompting pattern and generates the richest v6 candidate signals. Risk: this is the longest prompt of any round — Phase 2c directive format, Phase 3b table, and Amendment 5 stack on top of the already-substantial V-05 R4 body. Attention load at Phase 5 may produce compressed self-diagnosis quality.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling with structured revision directives when misalignment is found, composes explicit connective bridges with semantic type labels, audits bridge integration after merge, then runs a hardened five-amendment pass: four targeted amendments plus a self-diagnosis sweep. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three enforcement layers: coupling (Phase 2c), bridge integration (Phase 3b), and self-diagnosis (Amendment 5).

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

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
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Phase 2c — Section coupling verification with structured revision directives.** After drafting all six sections and before composing bridges, verify semantic coupling at each adjacent section boundary. Answer COUPLED, WEAK, or REVISE.

| Boundary | Coupling question | Status |
|----------|-----------------|--------|
| Background -> Gap | Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area? | [COUPLED / WEAK / REVISE] |
| Gap -> Claim | Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question? | [COUPLED / WEAK / REVISE] |
| Claim -> Method | Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field? | [COUPLED / WEAK / REVISE] |
| Method -> Result | Does Result report the finding produced by **this** Method — not a different or more general finding? | [COUPLED / WEAK / REVISE] |
| Result -> Implication | Does Implication name what **this** Result enables — not a general insight the field already knew? | [COUPLED / WEAK / REVISE] |

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

Do not proceed to bridge composition until all boundaries are COUPLED.

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

**Phase 3b — Bridge integration audit.** Verify that each Phase 2b bridge phrase was incorporated into the merged paragraph.

| Boundary | Phase 2b bridge phrase | Integrated? | Actual connective used in merged text |
|----------|------------------------|-------------|---------------------------------------|
| Background -> Gap | [phrase from Phase 2b] | Y / N | [text at this boundary in the merged paragraph] |
| Gap -> Claim | [phrase] | Y / N | [actual text] |
| Claim -> Method | [phrase] | Y / N | [actual text] |
| Method -> Result | [phrase] | Y / N | [actual text] |
| Result -> Implication | [phrase] | Y / N | [actual text] |

Integration is Y if the bridge phrase was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector that does not express the intended type relationship.

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Five-amendment pass.** Amendments 1-4 are targeted at fixed categories. Amendment 5 is a self-diagnosis sweep of the post-amendment abstract. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

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

**Amendment 5 — Self-diagnosis**
Read the abstract after amendments 1-4. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. This should not repeat a target already fully resolved by amendments 1-4.
> Diagnosis: [name the weakest remaining element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]
