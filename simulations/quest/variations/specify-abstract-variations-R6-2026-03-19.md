Written to `simulations/quest/variations/specify-abstract-variations-R6-2026-03-19.md`.

---

## R6 Variations Summary

Three single-axis variations, one two-axis combination, one full synthesis. All built on V-05 R5 (which implements C-22/C-23/C-24). Base score held at 100 under v6 in all five.

| ID | Axis | v7 Candidate Signal |
|----|------|---------------------|
| **V-01** | Role sequence: **self-diagnosis as Amendment 1** | Does the unconstrained diagnosis identify structurally different weaknesses before targeted amendments narrow attention? If the diagnosed weakness changes based on order, the amendment sequence is causally significant. |
| **V-02** | Inertia framing: **named-skip declaration** | Does explicitly committing against three cheap paths (signal-skip, nominal gap, non-trivial gaming) improve aspirational scores without an enforcement step? Tests commitment devices as quality gates. |
| **V-03** | Output format: **unified boundary quality card** | Replaces Phase 2c + Phase 2b + Phase 3b with one five-row card annotated incrementally (coupling -> type+phrase -> integration). Does cross-phase information cohesion reduce bridge drop at merge? |
| **V-04** | V-03 + V-01 | Unified card (pre/post-merge restructure) + diagnosis-first (amendment reorder). Adjacent-lifecycle and amendment-order axes combined. |
| **V-05** | Full synthesis | All three R6 axes on V-05 R5 base. Identifies which axes are load-bearing at the ceiling vs. overhead. |

**Key design choices:**
- V-01's diagnosis-first creates an audit ambiguity: Amendment 1 names a weakness, then Amendments 2-5 may fix it. The Before for Amendment 1 is from the pre-targeted-fix state — its stale-ness is the signal.
- V-02's inertia declaration is a commitment device, not enforcement. The signal is whether aspirational criteria diverge from V-05 R5 with identical mechanisms but explicit framing.
- V-03's unified card builds incrementally — three passes over the same five rows rather than three independent tables. The risk is rote form-filling; the signal is whether row-level cross-reference catches inconsistencies the isolated tables miss.
- V-05 is the longest prompt of any round.
 have masked
- V-02's inertia declaration is positioned before Phase 0 so the named shortcuts are in working context when every subsequent phase executes — a commitment device, not an enforcement step
- V-03's unified boundary quality card builds incrementally: coupling column filled after drafting, type+phrase columns filled after bridge composition, integration column filled after merge — the card is a running audit record, not a summary table
- V-04 tests whether V-03's information cohesion and V-01's diagnosis order are additive or whether one subsumes the other
- V-05 is the longest prompt of any round — the unified card replaces three tables but changes format rather than reducing steps; inertia framing adds a block; diagnosis-first reorders Phase 5 without adding steps

**Predicted v6 scores:**

| Variation | v6 Predicted | New signals probed |
|-----------|-------------|---------------------|
| V-01 | ~100 | Diagnosis-first amendment order — does Amendment 5 diagnose different weaknesses before vs. after targeted fixes? |
| V-02 | ~100 | Inertia commitment device — does naming the cheap path change execution quality on aspirational criteria? |
| V-03 | ~100 | Unified boundary card — does information cohesion across phases reduce bridge integration failures? |
| V-04 | ~100 | V-03 + V-01 combination — unified card + diagnosis-first additive? |
| V-05 | ~100 | All three axes on V-05 R5 base — which axes are load-bearing at the ceiling? |

**Key trade-offs:** V-01's diagnosis-first order risks that the self-diagnosis identifies a weakness that amendments 2-5 then "fix" — making the Amendment 1 diagnosis stale; the amendment table becomes harder to audit as a causal chain. V-02's inertia framing risks adding cognitive overhead for runs that already execute the full mechanism set. V-03's unified card risks ambiguity in incremental fills — the model may conflate Phase 2c coupling with Phase 3b integration and fill both columns at once, collapsing two distinct lifecycle checks into one. V-05 is the longest prompt of any round.

---

## V-01 — Self-Diagnosis as Amendment 1 (Diagnosis-First)

**Variation axis**: Role sequence (Phase 5 amendment order: self-diagnosis runs first, before the four targeted amendments)
**Hypothesis**: In V-05 R5, Amendment 5 (self-diagnosis) runs after Gap sharpening, Result quantification, Implication tightening, and Prose coherence. By the time the model reads the post-targeted-fix abstract, four specific weaknesses have already been addressed. The self-diagnosis therefore operates on a draft where the most predictable weaknesses are gone — it is likely to identify only subtle residuals, or to report that the abstract is satisfactory. Running self-diagnosis as Amendment 1 forces the model to read the post-merge draft before any targeted fixing and name what it would most want to change unconstrained by category labels. The targeted amendments then apply after the self-diagnosis, potentially overriding or extending the diagnosed fix. This tests whether the self-diagnosis order changes what the model perceives as the dominant weakness. v7 candidate: diagnosis-first amendment structure as a named quality gate.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling with structured revision directives when misalignment is found, composes explicit connective bridges with semantic type labels, audits bridge integration after merge, then runs a hardened five-amendment pass: self-diagnosis first (unconstrained), then four targeted amendments. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three enforcement layers: coupling (Phase 2c), bridge integration (Phase 3b), and self-diagnosis (Amendment 1, before targeted fixes).

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

**Phase 3b — Bridge integration audit.** Verify that each Phase 2b bridge phrase was incorporated into the merged paragraph.

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

**Phase 5 — Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep — it runs before the targeted amendments so the model reads the abstract without knowing which specific weaknesses will be fixed next. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Self-diagnosis (runs first)**
Read the merged abstract before any targeted fixing. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. Name it as a specific one-sentence claim about the weakness — not a general quality assessment.
> Diagnosis: [name the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 — Prose coherence**
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

## V-02 — Named-Skip Inertia Declaration

**Variation axis**: Inertia framing (explicit commitment device before Phase 0 names the three shortcuts a nominal execution would take and requires the model to confirm it will not take them)
**Hypothesis**: Every quality criterion in this skill has a cheap path: signal acquisition can be skipped (write from the topic name), gap framing can be nominal ("X remains poorly understood"), amendment non-triviality can be gamed (minor wording changes). The V-05 R5 prompt enforces these via structural mechanisms (Phase 2c, Phase 3b, non-trivial guards), but the model never explicitly names the cheap paths. An inertia declaration block before Phase 0 names three specific shortcuts — signal-skipping, nominal gap framing, and non-trivial gaming — and requires the model to state it will avoid them. This is a commitment device: once named, the model has a prior declaration to maintain consistency with. Tests whether explicit naming of the status-quo competitor (writing a generic abstract from the topic name alone) improves execution quality on aspirational criteria without adding a new enforcement step. v7 candidate: commitment-device inertia framing as a named quality gate.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — verifies section coupling with structured revision directives when misalignment is found, composes explicit connective bridges with semantic type labels, audits bridge integration after merge, then runs a hardened five-amendment pass including self-diagnosis. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. The inertia declaration below names the three corners that would be cut in a nominal execution — this run avoids all three.

---

**Inertia declaration.** Before any work begins, name what a minimal-effort execution of this skill would do instead. The purpose is not to describe a failure mode — it is to commit, in advance, to the behaviors this run will not take.

> A nominal execution would: (1) skip signal acquisition and write the abstract from the topic name alone, producing generic content that could apply to any paper in the field; (2) frame the Gap section with a vague insufficiency claim ("X remains poorly understood") rather than naming the specific unresolved question the paper addresses; (3) comply nominally with the non-triviality guard by making surface wording changes that do not alter the informational content of the sentence.

> This run will instead: (1) execute Phase 1 signal acquisition and ground every section in the extracted content; (2) frame the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution; (3) show substantive Before/After changes in Phase 5 that alter the informational content of the amended sentence, not just its phrasing.

> Confirm: [I confirm the above commitment before proceeding.]

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

**Phase 3b — Bridge integration audit.** Verify that each Phase 2b bridge phrase was incorporated into the merged paragraph.

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

---

## V-03 — Unified Boundary Quality Card

**Variation axis**: Output format (Phase 2c coupling table + Phase 2b bridge table + Phase 3b integration table replaced by a single five-row boundary quality card that is annotated incrementally across three lifecycle positions)
**Hypothesis**: V-05 R5 distributes boundary information across three separate tables at three separate lifecycle positions. Each table sees only one property per boundary: Phase 2c sees coupling status, Phase 2b sees bridge type and phrase, Phase 3b sees integration status. There is no cross-reference between tables — a model that changes a bridge phrase during merge has no structural prompt to re-verify Phase 3b. A unified boundary quality card — five rows, one per boundary, with columns for all four properties — is annotated incrementally: coupling status is filled after Phase 2 drafting, bridge type and phrase are filled after Phase 2b composition, integration status is filled after Phase 3 merge. The card becomes a running audit record with causal chain visible: coupling -> bridge type -> bridge phrase -> integration. Any N in the integration column can be cross-referenced against the bridge phrase column in the same row. Tests whether information cohesion across phases reduces bridge loss and improves cross-phase consistency. v7 candidate: unified boundary card as a structural lifecycle criterion.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — then builds a unified boundary quality card incrementally: coupling status after drafting, bridge type and phrase after composition, integration status after merge. The card tracks all four boundary properties in one auditable record. Then five amendments: four targeted plus self-diagnosis. Each section instruction explains why its constraint exists.

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

**Boundary quality card — Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank — they are filled in subsequent passes.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? Y / N |
|----------|-----------------------------------|-------------|---------------------------|-------------------|
| Background -> Gap | [fill now] | — | — | — |
| Gap -> Claim | [fill now] | — | — | — |
| Claim -> Method | [fill now] | — | — | — |
| Method -> Result | [fill now] | — | — | — |
| Result -> Implication | [fill now] | — | — | — |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method — not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables — not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card — Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first — it constrains what phrase is appropriate.

**Semantic type vocabulary:**
- **contrast** — Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** — Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** — Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** — Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** — Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Update the card with type and phrase for all five boundaries. Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card — Pass 3: Integration status.** Fill the Integrated? column for each boundary. Integration is Y if the bridge phrase from Pass 2 was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

Update the complete card now — all five columns filled for all five rows:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? |
|----------|----------|-------------|---------------|-------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now: Y / N] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now: Y / N] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now: Y / N] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now: Y / N] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now: Y / N] |

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

---

## V-04 — Unified Boundary Card + Diagnosis-First

**Variation axes**: Output format (unified boundary quality card — V-03 R6) + Role sequence (self-diagnosis as Amendment 1 — V-01 R6)
**Hypothesis**: V-03 R6 restructures the pre-merge and post-merge boundary lifecycle into a single auditable record, reducing information fragmentation across phases. V-01 R6 repositions self-diagnosis before targeted amendments, testing whether unconstrained quality perception captures different weaknesses before the fixed slots have narrowed attention. The two axes operate at distinct lifecycle positions — V-03 affects Phase 2c/2b/3b (pre-merge and post-merge structure), V-01 affects Phase 5 (amendment order). Neither axis interferes with the other. Together they test whether information cohesion and diagnosis order are additive: does a model running unified-card + diagnosis-first produce different quality outcomes than a model running either axis alone? Risk: the card's incremental annotation adds cognitive overhead that may compress the quality of the diagnosis-first amendment if the model's attention budget is saturated.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill declares paper type first, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — builds a unified boundary quality card incrementally across three passes (coupling, bridge type+phrase, integration), then runs a hardened five-amendment pass with self-diagnosis first. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. The unified card keeps all boundary information in one auditable record; diagnosis-first captures unconstrained quality perception before targeted amendments narrow attention.

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

**Boundary quality card — Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? Y / N |
|----------|-----------------------------------|-------------|---------------------------|-------------------|
| Background -> Gap | [fill now] | — | — | — |
| Gap -> Claim | [fill now] | — | — | — |
| Claim -> Method | [fill now] | — | — | — |
| Method -> Result | [fill now] | — | — | — |
| Result -> Implication | [fill now] | — | — | — |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method — not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables — not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card — Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** — Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** — Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** — Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** — Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** — Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card — Pass 3: Integration status.** Fill the Integrated? column. Integration is Y if the bridge phrase from Pass 2 was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

Complete card — all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? |
|----------|----------|-------------|---------------|-------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep — it runs before the targeted amendments so the model reads the abstract without knowing which specific weaknesses will be fixed next. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Self-diagnosis (runs first)**
Read the merged abstract before any targeted fixing. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. Name it as a specific one-sentence claim about the weakness — not a general quality assessment.
> Diagnosis: [name the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 — Prose coherence**
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

## V-05 — Full Synthesis: Unified Boundary Card + Inertia Declaration + Diagnosis-First

**Variation axes**: All three R6 single axes combined on V-05 R5 base: output format (unified boundary quality card — V-03 R6) + inertia framing (named-skip declaration — V-02 R6) + role sequence (self-diagnosis as Amendment 1 — V-01 R6)
**Hypothesis**: All three R5 mechanisms (structured revision directive, bridge integration audit, self-diagnosis amendment) are now formalized as C-22, C-23, C-24. R6 axes probe what lies above the v6 ceiling. The three R6 axes are structurally independent: the unified card is a format change affecting pre-merge and post-merge tables; inertia framing is a commitment device affecting Phase 0 setup; diagnosis-first is an amendment order change affecting Phase 5. If all three are load-bearing, this variation surfaces new ceiling-pushing behavior across three independent dimensions simultaneously. The highest-risk axis is the unified card — incremental annotation across three passes may produce rote card-filling behavior if the model treats Pass 1/2/3 as a mechanical form rather than a live audit. The highest-signal axis is diagnosis-first — if the self-diagnosis order changes what weakness is identified, the order is causally significant and a v7 candidate. Inertia framing's signal will be visible only if aspirational criteria scores diverge between V-02 and V-05 R5 (same mechanisms, different framing); if they do not diverge, the commitment device is not load-bearing at this ceiling.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with an inertia declaration naming three shortcuts this run will not take, declares paper type, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration), then runs a hardened five-amendment pass with self-diagnosis first. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three R5 enforcement layers (structured revision directive, bridge integration audit, self-diagnosis amendment) and three R6 structural changes (unified card, commitment framing, diagnosis-first order).

---

**Inertia declaration.** Before any work begins, name what a minimal-effort execution of this skill would do instead. The purpose is not to describe a failure mode — it is to commit, in advance, to the behaviors this run will not take.

> A nominal execution would: (1) skip signal acquisition and write the abstract from the topic name alone, producing generic content that could apply to any paper in the field; (2) frame the Gap section with a vague insufficiency claim ("X remains poorly understood") rather than naming the specific unresolved question the paper addresses; (3) comply nominally with the non-triviality guard by making surface wording changes that do not alter the informational content of the sentence.

> This run will instead: (1) execute Phase 1 signal acquisition and ground every section in the extracted content; (2) frame the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution; (3) show substantive Before/After changes in Phase 5 that alter the informational content of the amended sentence, not just its phrasing.

> Confirm: [I confirm the above commitment before proceeding.]

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

**Boundary quality card — Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? Y / N |
|----------|-----------------------------------|-------------|---------------------------|-------------------|
| Background -> Gap | [fill now] | — | — | — |
| Gap -> Claim | [fill now] | — | — | — |
| Claim -> Method | [fill now] | — | — | — |
| Method -> Result | [fill now] | — | — | — |
| Result -> Implication | [fill now] | — | — | — |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method — not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables — not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card — Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** — Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** — Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** — Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** — Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** — Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card — Pass 3: Integration status.** Fill the Integrated? column. Integration is Y if the bridge phrase from Pass 2 was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

Complete card — all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? |
|----------|----------|-------------|---------------|-------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep — it runs before the targeted amendments so the model reads the abstract without knowing which specific weaknesses will be fixed next. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Self-diagnosis (runs first)**
Read the merged abstract before any targeted fixing. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. Name it as a specific one-sentence claim about the weakness — not a general quality assessment.
> Diagnosis: [name the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]
