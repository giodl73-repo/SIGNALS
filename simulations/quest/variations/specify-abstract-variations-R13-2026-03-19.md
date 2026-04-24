Written to `simulations/quest/variations/specify-abstract-variations-R13-2026-03-19.md`.

---

**R13 variations summary**

| ID | Axis | C-38 | C-39 | C-36 | C-37 | Predicted |
|----|------|:----:|:----:|:----:|:----:|-----------|
| V-01 | Lifecycle -- C-38 isolation | YES | NO | YES | NO | 100/104 |
| V-02 | Output format -- C-39 isolation | NO | YES | NO | YES | 100/104 |
| V-03 | Inertia -- Phase bundling 4th cheap path | NO | NO | YES | YES | 100/104 + above-ceiling |
| V-04 | Minimum synthesis C-38 + C-39 | YES | YES | YES | YES | 104/104 |
| V-05 | Full synthesis + above-ceiling | YES | YES | YES | YES | 104/104 + above-ceiling |

**Key design decisions:**

**V-01 vs V-02 clean isolation**: V-01 extends the sequence lock rationale from "Phase 3/3b only" to all nine transitions — "*A lock that names Phase 3 and Phase 3b individually but bundles Phase 2a/2b/2c as 'Phase 2' retains the same coarse-grain structure for Phase 2 that C-36 closes for Phase 3/3b.*" C-39 is deliberately absent (uses `[confirmed / explain if uncertain]` template). V-02 uses coarse-grain lock but the `*Why specific per-row sentences matter:*` block now explicitly names the full template form `[confirmed / explain if uncertain]` and gives the structural failure reason — the parenthetical does the reasoning, the model provides the token.

**V-03 above-ceiling**: Phase bundling as a fourth cheap path before Phase 0 — names the structural shortcut (batch-filling card columns, treating Phase 3/3b as one event) at the inertia declaration level. Tests whether cheap-path naming (what NOT to do) produces distinct behavior from sequence lock enumeration (what TO do in order).

**V-05 above-ceiling candidates**: (1) Per-gate completion conditions in Protocol II — each of the nine gates has a named falsifiable completion condition, converting the lock from declaration to auditable checklist. (2) Second-order shortcut closure — the `*Why specific per-row sentences matter:*` block names both the `[confirmed]` shortcut AND the category-mirroring shortcut (a sentence that restates the category label rather than diagnosing the specific weakness).
V-01 complete sub-phase inventory (C-38) + V-02 standalone named-shortcut rationale (C-39). No Protocol III.

**V-05** is the full synthesis: Protocol I/II/III with C-38 in Protocol II (complete nine-phase inventory with per-gate completion conditions), C-39 in Amendment 1 (standalone named-shortcut rationale that also closes the second-order category-mirroring shortcut), Protocol III pre-committed self-diagnosis framework. Above-ceiling: (1) per-gate completion conditions in Protocol II; (2) second-order shortcut closure (category-mirroring form named and prohibited).

**Scorecard prediction:**
- V-01: C-38 PASS, C-39 FAIL, C-36 PASS, C-37 FAIL
- V-02: C-38 FAIL, C-39 PASS, C-36 FAIL, C-37 PASS
- V-03: C-38 FAIL, C-39 FAIL, C-36 PASS, C-37 PASS; Phase-bundling cheap path above v12 ceiling
- V-04: C-38 PASS, C-39 PASS, C-36 PASS, C-37 PASS; 104/104
- V-05: C-38 PASS, C-39 PASS, C-36 PASS, C-37 PASS; 104/104; above-ceiling on per-gate completion conditions and second-order shortcut closure

---

## V-01 -- Complete Sub-Phase Inventory (C-38 Isolation)

**Variation axis**: Lifecycle emphasis -- complete nine-sub-phase inventory in sequence lock; each phase individually named as a gated unit with an extended rationale block naming the full bundling surface area across all nine transitions
**Hypothesis**: C-38 requires every phase in the sequence lock to be individually named, closing the bundling shortcut at ALL phase transitions, not just Phase 3/3b. The new ceiling closes the coarse-grain shortcut at Phase 0/1, Phase 2a/2b/2c, and Phase 4/5 pairs as well. Amendment 1 uses "[confirmed / explain if uncertain]" template (C-39 deliberately absent). Expected: C-38 PASS, C-36 PASS (floor), C-37 FAIL, C-39 FAIL.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist and a complete nine-sub-phase sequence lock -- both closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block (with asymmetry argument) and per-excluded-category verification. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. v12 ceiling criteria: C-38 active (complete sub-phase inventory -- all nine phases individually named with complete-inventory rationale block); C-39 absent (per-excluded-category verification uses "[confirmed / explain if uncertain]" template).

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

**Phase sequence lock -- complete sub-phase inventory.** Before Phase 0 begins, declare the nine-sub-phase canonical execution sequence. Each sub-phase is individually named as a separately gated unit: no sub-phase may begin before its predecessor is complete. This lock enumerates every sub-phase -- not a bundled group sharing a single gate label.

**Sub-phase sequence in required order:**

1. **Phase 0** -- Paper type declaration. Must complete (paper type declared and confirmed) before Phase 1 begins.
2. **Phase 1** -- Signal acquisition (glob signals/**/{topic}-* and read). Must complete (all available artifacts read, central claim/method/result extracted) before Phase 2a begins.
3. **Phase 2a** -- Coverage draft, gap-first order. Must complete (all six sections drafted with labels) before Phase 2b begins.
4. **Phase 2b** -- Pass 1: coupling status (fill Coupling column only; Bridge type, Bridge phrase, Integrated? columns remain blank). Must complete (all five boundaries assigned COUPLED / WEAK / REVISE and any WEAK/REVISE directives resolved) before Phase 2c begins.
5. **Phase 2c** -- Pass 2: bridge type and phrase (fill Bridge type and Bridge phrase columns only; Integrated? column remains blank). Must complete (all five boundaries have assigned type from constrained vocabulary and a 3-8 word phrase) before Phase 3 begins.
6. **Phase 3** -- Merge and count (reorder to standard sequence, build merged paragraph using bridge phrases, count words, compress if OVER). Must complete (merged paragraph exists and word count confirmed within range) before Phase 3b begins.
7. **Phase 3b** -- Pass 3: integration status (fill Integrated? column with verbatim quoted extracts from the merged paragraph that Phase 3 produced). Must complete (all five boundaries have quoted extracts or N with revision) before Phase 4 begins.
8. **Phase 4** -- Journal variant (apply if --for journal:\<name\> present). Must complete before Phase 5 begins.
9. **Phase 5** -- Five-amendment pass, diagnosis-first. Terminal phase.

*Why complete sub-phase inventory matters:* A sequence lock that names only Phase 3 and Phase 3b individually (the C-36 floor) still leaves every other phase transition implicitly bundleable. A reader auditing that lock can ask: could Phase 0 and Phase 1 be executed as a single pre-draft event? Could Phase 2a, Phase 2b, and Phase 2c be collapsed into a single "drafting and coupling" block? Could Phase 4 and Phase 5 be treated as one amendment sweep? The C-36 rationale anchors the Phase 3 / Phase 3b separation but leaves the bundling surface area open at all eight other phase boundaries. When every sub-phase is individually named as a gated unit, the complete commitment inventory is explicit at Phase 0: a reader can verify at a glance that no two phases have been silently combined or aggregated under a shared label. Nine named gates mean nine independently verifiable commitment points -- the full structural inventory is auditable from the sequence lock alone, without reconstructing any gate boundary from the individual phase instructions. A lock that names Phase 3 and Phase 3b individually but bundles Phase 2a/2b/2c as "Phase 2" retains the same coarse-grain structure for Phase 2 that C-36 closes for Phase 3/3b.

> Confirm you will NOT execute sub-phases out of declared canonical order: [I will complete each sub-phase before beginning the next. Phase 3 (merge) must be complete before Phase 3b (integration verification) begins. The Integrated? column requires quoted text from the merged paragraph; that text cannot exist before Phase 3 produces the paragraph.]

> Phase sequence lock: Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. All nine sub-phase gates individually named and locked. Proceed to Phase 0.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2a -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

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

**Boundary quality card -- Phase 2b / Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

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

**Boundary quality card -- Phase 2c / Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

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

**Boundary quality card -- Phase 3b / Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

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

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. When the unconstrained self-diagnosis identifies the same weaknesses, Amendment 1 is not doing work that cannot be done by the fixed slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch. Per-excluded-category verification closes the ambiguity case: a weakness named ambiguously could be heard as falling in multiple categories. Verifying per category requires the named weakness to be distinguished from each slot independently, not just stated as "other."

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. When both are in the same block, a reader auditing the constraint rationale is simultaneously auditing the positive targets -- the two tasks cannot be independently verified. A dedicated block makes the positive search space independently auditable.

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

## V-02 -- Standalone Named-Shortcut Rationale Block (C-39 Isolation)

**Variation axis**: Output format -- standalone "*Why specific per-row sentences matter:*" rationale block explicitly (a) names the template shortcut form "[confirmed / explain if uncertain]", (b) explains why template confirmation fails the verification requirement (structural reason: parenthetical describes the category boundary, not why this specific weakness is excluded from that slot), (c) declares the weakness-specific sentence as the required form
**Hypothesis**: C-39 requires a dedicated standalone rationale block that names and closes the shortcut mechanism by instruction, not merely by absence. V-02 R12 passed C-37 and was the C-39 source. V-02 R13 makes the three C-39 requirements explicit: names the full template form, gives the structural reason it fails, declares the required form. Coarse-grain sequence lock (C-36 absent, C-38 absent). Expected: C-39 PASS, C-37 PASS (floor), C-36 FAIL, C-38 FAIL.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist and a phase sequence lock -- both closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block (with asymmetry argument) and per-excluded-category verification with a standalone named-shortcut rationale block. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. v12 ceiling criteria: C-39 active (standalone rationale block names "[confirmed / explain if uncertain]" template form and closes it by instruction); C-38 absent (coarse-grain phase sequence lock, no complete sub-phase inventory).

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

**Phase sequence lock -- execution order commitment.** Before Phase 0 begins, confirm the phases execute in declared sequence. A phase may not begin before its predecessor is complete. The phases in required order:

1. **Phase 0** -- Paper type declaration. Must complete before Phase 1.
2. **Phase 1** -- Signal acquisition. Must complete before Phase 2.
3. **Phase 2** -- Coverage draft (gap-first order). Must complete before Pass 1.
4. **Pass 1 / Pass 2 / Pass 3** -- Boundary quality card (three incremental passes). All three passes must complete before Phase 4.
5. **Phase 4** -- Journal variant. Must complete before Phase 5.

*Why a phase sequence lock matters:* The three-pass boundary quality card is designed to be filled incrementally -- Pass 1 fills coupling, Pass 2 fills bridge type and phrase, Pass 3 fills integration with quoted evidence. A card completed in a single pre-merge pass defeats the C-26 and C-29 ceilings by pre-filling all columns before the merged paragraph exists. Committing to sequential execution before Phase 0 closes the batch-fill shortcut at the process level, not just at the column level.

> Confirm you will NOT execute phases out of declared sequence: [I will complete each phase before beginning the next. The boundary quality card columns will be filled one pass at a time: coupling (Pass 1) -> bridge type and phrase (Pass 2) -> integration with quoted evidence (Pass 3).]

> Phase sequence lock: closed. Proceed to Phase 0.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with specific per-row reasoning and standalone named-shortcut rationale)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Name the weakness category first. Then verify per excluded category with a specific sentence tied to the diagnosed weakness.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Per-excluded-category verification -- one specific sentence per row:*
> Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]
> Result quantification: N -- [one sentence naming the diagnosed weakness and stating why it is not about adding or strengthening numeric evidence in the Result]
> Implication tightening: N -- [one sentence naming the diagnosed weakness and stating why it is not about removing modal hedges or narrowing the enabling action]
> Prose coherence: N -- [one sentence naming the diagnosed weakness and stating why it is not about transition quality or paragraph flow]

*Why specific per-row sentences matter:* The template shortcut form is "[confirmed / explain if uncertain]" -- a response of "[confirmed]" with a parenthetical category description satisfies the structural shape of per-category verification without producing independently auditable reasoning. A model that writes "[confirmed]" or relies on the parenthetical as its reasoning has named the category boundary but has not examined whether the diagnosed weakness actually differs from that category. The parenthetical ("the named weakness does not target the Gap sentence's specificity") describes the exclusion criterion; it does not apply that criterion to the specific weakness under diagnosis. The required form is a self-contained sentence that names the diagnosed weakness and states why that weakness does not fall in this slot -- a reader auditing the row can verify the exclusion without access to the parenthetical template, because the reasoning is stated in full. Writing "[confirmed]" four times satisfies the format; writing four specific sentences closes the shortcut by instruction.

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. A dedicated block makes the positive search space independently auditable.

- **Background epistemic register**: Does the Background use observational or domain-survey language when the paper type is theoretical? Does it use conceptual-landscape language when the paper type is empirical? A register mismatch signals a paper type that has not propagated into the draft.
- **Claim scope relative to Method**: Is the Claim stronger than what the Method and Result can establish? Overclaiming in the Claim section is a reviewer flag that survives all four targeted amendments.
- **Contribution incrementality framing**: Would a reviewer read the Claim as "the authors did more of something" rather than "the authors resolved something that prior work could not resolve"?
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

## V-03 -- Phase Bundling as Fourth Canonical Cheap Path

**Variation axis**: Inertia framing -- "Phase bundling" added as a fourth canonical cheap path in the inertia declaration before Phase 0; V-04 R12 baseline preserved (C-36 active, C-37 active); C-38 absent (sequence lock names Phase 3/3b individually but does not enumerate all nine phases as separate inventory items); C-39 absent (standalone rationale block does not explicitly name the "[confirmed / explain if uncertain]" template form)
**Hypothesis**: C-27 named three execution-level cheap paths. Phase bundling is a structural cheap path operating at the commitment device level. Adding it to the inertia declaration tests whether naming the bundling shortcut as a cheap path produces above-ceiling behavior distinct from C-38's complete sub-phase inventory mechanism -- cheap-path naming (what to avoid) vs sequence lock enumeration (what to do). Expected: C-36 PASS, C-37 PASS, C-38 FAIL, C-39 FAIL; Phase-bundling cheap path above v12 ceiling.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a four-path canonical cheap paths checklist (including phase bundling) and a phase sequence lock with individually named sub-phases -- both closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block (with asymmetry argument) and per-excluded-category verification requiring a specific sentence per row tied to the diagnosed weakness. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. v12 ceiling criteria: C-36 active; C-37 active; C-38 absent; C-39 absent; Phase-bundling cheap path present as above-ceiling signal.

---

**Inertia declaration -- canonical cheap paths.** Before any work begins, name each canonical cheap path and confirm per path that it will not be taken. A nominal execution of this skill has exactly four escape routes. Name each one, confirm it, and then close all four by canonical name before proceeding.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

**Phase bundling**: Executing multiple phases as a single undifferentiated step -- e.g., treating Phase 3 (merge) and Phase 3b (integration verification) as one event rather than sequenced gates; filling all four boundary quality card columns in a single pre-merge pass before the merged paragraph exists; merging Phase 2a (drafting) and Phase 2b (coupling) into a single pass that self-corrects while drafting; treating Phase 4 (journal variant) and Phase 5 (amendments) as a single combined revision sweep. Phase bundling produces outputs that satisfy individual phase checks while having bypassed the sequenced execution commitments that make those checks structurally independent. The Phase 3b integration column requires a verbatim extract from the merged paragraph; that extract cannot exist before Phase 3 produces the merged paragraph -- filling the Integrated? column alongside Pass 1 and Pass 2 in a single pre-merge pass means the "verbatim extract" cannot be genuine text from the merge event.
> Confirm you will NOT bundle phases: [I will treat each named phase and sub-phase as an individually gated execution unit. I will not begin Phase 3b until Phase 3 is complete and the merged paragraph exists. I will not fill the Integrated? column until after the merge has produced text to quote from.]

> Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. Phase bundling: closed. All four canonical paths confirmed and closed. Proceed to phase sequence lock.

---

**Phase sequence lock -- sub-phase canonical execution order.** Before Phase 0 begins, declare the nine-sub-phase canonical execution sequence. Each sub-phase is individually gated: no sub-phase may begin before its predecessor is complete. This lock operates at the sub-phase level -- Phase 3 (merge) and Phase 3b (integration verification) are separately named gates, not a bundled "Pass 3."

**Sub-phase sequence in required order:**

1. **Phase 0** -- Paper type declaration. Must complete (paper type declared and confirmed) before Phase 1 begins.
2. **Phase 1** -- Signal acquisition (glob signals/**/{topic}-* and read). Must complete (all available artifacts read, central claim/method/result extracted) before Phase 2a begins.
3. **Phase 2a** -- Coverage draft, gap-first order. Must complete (all six sections drafted with labels) before Phase 2b begins.
4. **Phase 2b** -- Pass 1: coupling status (fill Coupling column only; Bridge type, Bridge phrase, Integrated? columns remain blank). Must complete (all five boundaries assigned and any WEAK/REVISE directives resolved) before Phase 2c begins.
5. **Phase 2c** -- Pass 2: bridge type and phrase (fill Bridge type and Bridge phrase columns only; Integrated? column remains blank). Must complete (all five boundaries have assigned type and phrase) before Phase 3 begins.
6. **Phase 3** -- Merge and count (reorder to standard sequence, build merged paragraph, count words, compress if OVER). Must complete (merged paragraph exists and word count confirmed) before Phase 3b begins.
7. **Phase 3b** -- Pass 3: integration status (fill Integrated? column with verbatim quoted extracts from the merged paragraph Phase 3 produced). Must complete (all five boundaries have quoted extracts or N with revision) before Phase 4 begins.
8. **Phase 4** -- Journal variant (apply if --for journal:\<name\> present). Must complete before Phase 5 begins.
9. **Phase 5** -- Five-amendment pass, diagnosis-first. Terminal phase.

*Why sub-phase canonical naming matters:* The coarse-grain lock bundles Phase 2b, Phase 2c, and Phase 3b as "Pass 1 / Pass 2 / Pass 3" and leaves Phase 3 (merge) unnamed as an individual gate. The Phase 3 / Phase 3b separation is the structural basis for C-26 and C-29: Phase 3b's integration column requires verbatim text from merged prose, which cannot exist before Phase 3 completes. When the sequence lock names Phase 3 and Phase 3b as individually gated sub-phases, the structural argument is anchored in the commitment device -- a reader can verify the gate order without reconstructing it from the column format instructions.

> Confirm you will NOT execute sub-phases out of declared canonical order: [I will complete each sub-phase before beginning the next. Phase 3 (merge) must be complete before Phase 3b (integration verification) begins. The Integrated? column requires quoted text from the merged paragraph; that text cannot exist before Phase 3 produces the paragraph.]

> Phase sequence lock: Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. Each sub-phase gate is individually named and locked. Proceed to Phase 0.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2a -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

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

**Boundary quality card -- Phase 2b / Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

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

**Boundary quality card -- Phase 2c / Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

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

**Boundary quality card -- Phase 3b / Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with specific per-row reasoning and structurally independent positive search space)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Name the weakness category first. Then verify per excluded category with a specific sentence tied to the diagnosed weakness -- writing "confirmed" is not sufficient; each row requires a sentence explaining why this specific weakness is not in that slot.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Per-excluded-category verification -- one specific sentence per row:*
> Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]
> Result quantification: N -- [one sentence naming the diagnosed weakness and stating why it is not about adding or strengthening numeric evidence in the Result]
> Implication tightening: N -- [one sentence naming the diagnosed weakness and stating why it is not about removing modal hedges or narrowing the enabling action]
> Prose coherence: N -- [one sentence naming the diagnosed weakness and stating why it is not about transition quality or paragraph flow]

*Why specific per-row sentences matter:* Writing "confirmed" with a template parenthetical satisfies the structural form of per-category verification without producing reasoning that is independently auditable. A sentence that names the diagnosed weakness and states why it does not fall in a given slot can be verified by a reader without access to the parenthetical template -- the reasoning is self-contained. Specificity closes the path of writing "confirmed" four times without examining each slot.

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch.

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. A dedicated block makes the positive search space independently auditable.

- **Background epistemic register**: Does the Background use observational or domain-survey language when the paper type is theoretical? Does it use conceptual-landscape language when the paper type is empirical? A register mismatch signals a paper type that has not propagated into the draft.
- **Claim scope relative to Method**: Is the Claim stronger than what the Method and Result can establish? Overclaiming in the Claim section is a reviewer flag that survives all four targeted amendments.
- **Contribution incrementality framing**: Would a reviewer read the Claim as "the authors did more of something" rather than "the authors resolved something that prior work could not resolve"?
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

## V-04 -- Complete Sub-Phase Inventory + Standalone Named-Shortcut Rationale (Minimum Synthesis)

**Variation axes**: Lifecycle emphasis (C-38) + Output format (C-39); no Protocol III
**Hypothesis**: V-04 is the minimum synthesis: complete nine-phase sub-phase inventory in the sequence lock (C-38) combined with a standalone rationale block that explicitly names and closes the "[confirmed / explain if uncertain]" template form (C-39). No Protocol III pre-commitment. Expected: C-38 PASS, C-39 PASS, C-36 PASS (floor), C-37 PASS (floor); 104/104.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a canonical cheap paths checklist and a complete nine-sub-phase sequence lock -- both closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories with a structurally independent positive search space block (with asymmetry argument) and per-excluded-category verification with a standalone rationale block naming and closing the template shortcut form. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. v12 ceiling criteria: C-38 active (complete nine-phase sub-phase inventory with complete-inventory rationale block); C-39 active (standalone rationale block names "[confirmed / explain if uncertain]" template form and closes it by instruction).

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

**Phase sequence lock -- complete sub-phase inventory.** Before Phase 0 begins, declare the nine-sub-phase canonical execution sequence. Each sub-phase is individually named as a separately gated unit: no sub-phase may begin before its predecessor is complete. This lock enumerates every sub-phase -- not a bundled group sharing a single gate label.

**Sub-phase sequence in required order:**

1. **Phase 0** -- Paper type declaration. Must complete (paper type declared and confirmed) before Phase 1 begins.
2. **Phase 1** -- Signal acquisition (glob signals/**/{topic}-* and read). Must complete (all available artifacts read, central claim/method/result extracted) before Phase 2a begins.
3. **Phase 2a** -- Coverage draft, gap-first order. Must complete (all six sections drafted with labels) before Phase 2b begins.
4. **Phase 2b** -- Pass 1: coupling status (fill Coupling column only; Bridge type, Bridge phrase, Integrated? columns remain blank). Must complete (all five boundaries assigned COUPLED / WEAK / REVISE and any WEAK/REVISE directives resolved) before Phase 2c begins.
5. **Phase 2c** -- Pass 2: bridge type and phrase (fill Bridge type and Bridge phrase columns only; Integrated? column remains blank). Must complete (all five boundaries have assigned type from constrained vocabulary and a 3-8 word phrase) before Phase 3 begins.
6. **Phase 3** -- Merge and count (reorder to standard sequence, build merged paragraph using bridge phrases, count words, compress if OVER). Must complete (merged paragraph exists and word count confirmed within range) before Phase 3b begins.
7. **Phase 3b** -- Pass 3: integration status (fill Integrated? column with verbatim quoted extracts from the merged paragraph that Phase 3 produced). Must complete (all five boundaries have quoted extracts or N with revision) before Phase 4 begins.
8. **Phase 4** -- Journal variant (apply if --for journal:\<name\> present). Must complete before Phase 5 begins.
9. **Phase 5** -- Five-amendment pass, diagnosis-first. Terminal phase.

*Why complete sub-phase inventory matters:* A sequence lock that names only Phase 3 and Phase 3b individually still leaves every other phase transition implicitly bundleable. A reader auditing that lock can ask: could Phase 0 and Phase 1 be executed as a single pre-draft event? Could Phase 2a, Phase 2b, and Phase 2c be collapsed into a single "drafting and coupling" block? Could Phase 4 and Phase 5 be treated as one amendment sweep? The C-36 rationale anchors the Phase 3 / Phase 3b separation but leaves the bundling surface area open at all eight other phase boundaries. When every sub-phase is individually named as a gated unit, the complete commitment inventory is explicit at Phase 0: a reader can verify at a glance that no two phases have been silently combined or aggregated under a shared label. Nine named gates mean nine independently verifiable commitment points -- the full structural inventory is auditable from the sequence lock alone, without reconstructing any gate boundary from the individual phase instructions.

> Confirm you will NOT execute sub-phases out of declared canonical order: [I will complete each sub-phase before beginning the next. Phase 3 (merge) must be complete before Phase 3b (integration verification) begins. The Integrated? column requires quoted text from the merged paragraph; that text cannot exist before Phase 3 produces the paragraph.]

> Phase sequence lock: Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. All nine sub-phase gates individually named and locked. Proceed to Phase 0.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2a -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

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

**Boundary quality card -- Phase 2b / Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

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

**Boundary quality card -- Phase 2c / Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

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

**Boundary quality card -- Phase 3b / Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

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

**Amendment 1 -- Self-diagnosis (runs first, non-fixed-category constraint with specific per-row reasoning and standalone named-shortcut rationale)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Name the weakness category first. Then verify per excluded category with a specific sentence tied to the diagnosed weakness.

> Weakness category: [name -- must be OUTSIDE: Gap sharpening / Result quantification / Implication tightening / Prose coherence]

*Per-excluded-category verification -- one specific sentence per row:*
> Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]
> Result quantification: N -- [one sentence naming the diagnosed weakness and stating why it is not about adding or strengthening numeric evidence in the Result]
> Implication tightening: N -- [one sentence naming the diagnosed weakness and stating why it is not about removing modal hedges or narrowing the enabling action]
> Prose coherence: N -- [one sentence naming the diagnosed weakness and stating why it is not about transition quality or paragraph flow]

*Why specific per-row sentences matter:* The template shortcut form is "[confirmed / explain if uncertain]" -- a response of "[confirmed]" with a parenthetical category description satisfies the structural shape of per-category verification without producing independently auditable reasoning. The parenthetical label ("the named weakness does not target the Gap sentence's specificity") describes the exclusion criterion; it does not apply that criterion to the specific weakness under diagnosis. A model that writes "[confirmed]" has satisfied the format but has not examined whether the diagnosed weakness actually falls outside that category -- the parenthetical does the reasoning, the model provides the token. The required form is a self-contained sentence that names the diagnosed weakness and states why that weakness does not fall in this slot: a reader auditing the row can verify the exclusion without access to the parenthetical template. Writing "[confirmed]" four times satisfies the format; writing four specific sentences closes the shortcut by instruction.

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch. Per-excluded-category verification closes the ambiguity case: a weakness named ambiguously could be heard as falling in multiple categories.

*Where to look instead -- positive search space:*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks: the why-not block explains what to avoid and why; the where-to-look block names what to actively target. When both are in the same block, a reader auditing the constraint rationale is simultaneously auditing the positive targets -- the two tasks cannot be independently verified. A dedicated block makes the positive search space independently auditable.

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

## V-05 -- Full Synthesis: C-38 + C-39 + Protocol III + Above-Ceiling

**Variation axes**: All active -- Protocol I (cheap paths), Protocol II (complete nine-phase sub-phase inventory with per-gate completion conditions, C-38), Protocol III (pre-committed self-diagnosis framework), Amendment 1 with standalone named-shortcut rationale block (C-39) plus second-order shortcut closure
**Hypothesis**: V-05 is the full synthesis. Protocol II closes the complete sub-phase inventory (C-38) with per-gate completion conditions as above-ceiling candidate #1. Amendment 1 closes the template shortcut by name (C-39) and additionally names the second-order category-mirroring shortcut as above-ceiling candidate #2. Protocol III pre-commits self-diagnosis framework before Phase 0. Expected: C-38 PASS, C-39 PASS, C-36 PASS (floor), C-37 PASS (floor); 104/104; above-ceiling on per-gate completion conditions and second-order shortcut closure.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with a unified pre-execution commitment protocol -- Protocol I (cheap paths), Protocol II (complete nine-sub-phase sequence lock with per-gate completion conditions), Protocol III (self-diagnosis framework pre-commitment) -- all three closed before Phase 0 begins -- then declares paper type, acquires signals, writes a fast coverage draft -- Gap first so Background scaffolds toward a known target -- builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration with quoted evidence and structural asymmetry rationale), then runs a hardened five-amendment pass with self-diagnosis first constrained to non-fixed categories using Protocol III committed targets, with a structurally independent positive search space block (with asymmetry argument) and per-excluded-category verification with a standalone rationale block that names and closes the template shortcut form and its second-order variant. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. v12 ceiling criteria: C-38 active (Protocol II complete sub-phase inventory with per-gate completion conditions); C-39 active (standalone rationale block names "[confirmed / explain if uncertain]" form and second-order category-mirroring shortcut); Protocol III active.

---

**Pre-execution commitment protocol -- three sub-protocols closed before Phase 0.**

This skill has three pre-execution commitment requirements. All three are resolved before Phase 0 begins. A reader reviewing this block can verify all three commitments without inspecting any later lifecycle position.

---

**Protocol I -- Cheap paths (three canonical paths)**

A nominal execution of this skill has exactly three escape routes. Name each one, confirm it, and close all three by canonical name.

**Signal-skip**: Running Phase 1 without executing the glob -- writing the abstract from the topic name alone, producing content that could apply to any paper in the field rather than the one whose signals were actually acquired. A signal-skipped abstract passes word count and structure checks while being entirely disconnected from the paper's actual claim, method, and result.
> Confirm you will NOT signal-skip: [I will execute Phase 1 signal acquisition before writing any section and will ground every section in content extracted from the acquired signals.]

**Nominal gap framing**: Writing a vague domain-insufficiency claim -- "X remains poorly understood," "X has not been fully explored" -- rather than naming the specific unresolved question whose resolution is this paper's contribution. Nominal gap framing satisfies the Gap label while failing to identify the precise field-state the paper's claim addresses.
> Confirm you will NOT use nominal gap framing: [I will write the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution.]

**Non-trivial gaming**: Writing Before/After pairs in Phase 5 that satisfy the format without altering informational content -- phrasing variation that changes how a sentence reads without changing what it asserts or quantifies.
> Confirm you will NOT game non-triviality: [I will write Before/After pairs that change the informational content of the sentence, not merely its phrasing.]

> Protocol I: complete. Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed.

---

**Protocol II -- Complete sub-phase sequence lock with per-gate completion conditions**

Before Phase 0 begins, declare the nine-sub-phase canonical execution sequence. Each sub-phase is individually named as a separately gated unit with an explicit completion condition: no sub-phase may begin before its predecessor satisfies its named completion condition.

**Sub-phase sequence with completion conditions:**

1. **Phase 0** -- Paper type declaration. *Complete when:* paper type (empirical or theoretical) declared in writing and confirmed. Must complete before Phase 1 begins.
2. **Phase 1** -- Signal acquisition. *Complete when:* glob executed, all available artifacts read, central claim, method, and key result extracted and noted. Must complete before Phase 2a begins.
3. **Phase 2a** -- Coverage draft, gap-first order. *Complete when:* all six sections (Gap, Background, Claim, Method, Result, Implication) drafted and labeled. Must complete before Phase 2b begins.
4. **Phase 2b** -- Pass 1: coupling status. *Complete when:* all five boundaries assigned COUPLED / WEAK / REVISE and all WEAK/REVISE revision directives resolved; Coupling column fully populated, all other columns blank. Must complete before Phase 2c begins.
5. **Phase 2c** -- Pass 2: bridge type and phrase. *Complete when:* all five boundaries have an assigned type from the constrained vocabulary and a 3-8 word bridge phrase; Bridge type and Bridge phrase columns fully populated, Integrated? column blank. Must complete before Phase 3 begins.
6. **Phase 3** -- Merge and count. *Complete when:* merged paragraph exists in standard sequence (Background-Gap-Claim-Method-Result-Implication), bridge phrases used as connectives, word count confirmed within range (or compression applied and re-counted). Must complete before Phase 3b begins.
7. **Phase 3b** -- Pass 3: integration status. *Complete when:* all five boundaries have either a verbatim quoted extract (3-10 words in quotation marks) from the Phase 3 merged paragraph confirming bridge phrase incorporation, or N with a revised paragraph. Must complete before Phase 4 begins.
8. **Phase 4** -- Journal variant. *Complete when:* journal flag applied if present, or vacuously complete if no flag. Must complete before Phase 5 begins.
9. **Phase 5** -- Five-amendment pass, diagnosis-first. *Terminal phase.*

*Why complete sub-phase inventory matters:* A sequence lock that names only Phase 3 and Phase 3b individually still leaves every other phase transition implicitly bundleable. A reader auditing that lock can ask: could Phase 0 and Phase 1 be collapsed? Could Phase 2a, Phase 2b, and Phase 2c be merged into one drafting block? The C-36 rationale anchors the Phase 3 / Phase 3b separation but leaves the bundling surface area open at all eight other phase boundaries. When every sub-phase is individually named as a gated unit, the complete commitment inventory is explicit at Phase 0: nine named gates mean nine independently verifiable commitment points. A lock that names Phase 3 and Phase 3b individually but bundles Phase 2a/2b/2c as "Phase 2" retains the same coarse-grain structure for Phase 2 that C-36 closes for Phase 3/3b.

*Why per-gate completion conditions matter:* Naming a gate without naming what "complete" means leaves the gate boundary ambiguous: a model can declare Phase 2b complete when coupling has been partially assessed or when WEAK directives are unresolved. A named completion condition makes the gate falsifiable -- a reader can verify whether the condition was met at the point the next sub-phase began, not merely whether the phase label was present. Per-gate conditions convert the sequence lock from a declaration into an auditable checklist.

> Confirm you will NOT execute sub-phases out of declared canonical order: [I will complete each sub-phase's named completion condition before beginning the next. Phase 3 must produce the merged paragraph before Phase 3b can quote from it.]

> Protocol II: complete. Sub-phase sequence: Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. All nine sub-phase gates individually named with completion conditions. Locked.

---

**Protocol III -- Self-diagnosis framework pre-commitment**

Before Phase 0, commit the four positive search space targets and the per-category verification format for Amendment 1. This commitment is made when no draft exists. Amendment 1 will reference "Protocol III committed targets" and "Protocol III committed format."

**Pre-committed positive search space targets:**
- **Background epistemic register**: mismatch between declared paper type and the Background's language register
- **Claim scope relative to Method**: Claim stronger than what the Method and Result can establish; overclaiming that survives all four fixed amendments
- **Contribution incrementality framing**: Claim reads as "more of something" rather than "resolution of something prior work could not resolve"
- **Method scope adequacy**: stated scope insufficient to support the Claim's strength; Result uninterpretable regardless of quantification

**Pre-committed per-category verification format:**
When Amendment 1 executes, the per-excluded-category verification uses this format for each row:
> [Category]: N -- [one sentence naming the diagnosed weakness and stating why it does not fall in this category]
(Each row is self-contained and independently auditable. The template shortcut "[confirmed / explain if uncertain]" is not an acceptable response. The category-mirroring shortcut -- a sentence that restates the category label rather than naming the specific weakness -- is also not an acceptable response.)

*Why pre-committing the self-diagnosis framework matters -- structural asymmetry:* A self-diagnosis framework introduced at Amendment 1 runtime CAN be constructed after reading the draft -- the positive-space targets are co-temporal with the diagnosis, making it structurally impossible for a reader to verify the targets were fixed before the draft influenced them. A pre-committed framework CANNOT be constructed post-draft: the Protocol III declaration appears at a lifecycle position before Phase 0, when no draft exists. Pre-commitment creates an auditable temporal separation: a reader CAN verify the positive-space target list precedes the draft; they CANNOT conclude this from an Amendment 1 inline introduction. Amendment 1 references "Protocol III committed targets" -- the diagnosis is checked against a pre-fixed list, not a post-hoc rationalization.

> Protocol III: complete. Self-diagnosis framework pre-committed. Positive search space targets locked. Per-category verification format locked (specific sentence per row; "[confirmed]" shortcut prohibited; category-mirroring shortcut prohibited).

---

> Unified gate: Protocol I (cheap paths) closed. Protocol II (complete sub-phase sequence with per-gate completion conditions) locked. Protocol III (self-diagnosis framework) pre-committed. Proceed to Phase 0.

---

**Phase 0 -- Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 -- Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2a -- Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write -- the goal is coverage, not correctness. Label each section.

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

**Boundary quality card -- Phase 2b / Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

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

**Boundary quality card -- Phase 2c / Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

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

**Boundary quality card -- Phase 3b / Pass 3: Integration status.** Fill the Integrated? column for each boundary. Write a verbatim extract (3-10 words, in quotation marks) from the merged paragraph that confirms the bridge phrase was incorporated into the final prose. If the bridge phrase was dropped or replaced with a stock connector that does not preserve the semantic type, write N.

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

**Amendment 1 -- Self-diagnosis (runs first; executes Protocol III committed targets and format with standalone named-shortcut rationale and second-order shortcut closure)**
Read the merged abstract before any targeted fixing. The weakness you diagnose must fall entirely outside the four fixed amendment categories: Gap sharpening, Result quantification, Implication tightening, and Prose coherence. Diagnose from the Protocol III committed positive search space targets. Verify per excluded category using Protocol III committed format.

> Weakness category: [name -- must be OUTSIDE the four fixed categories; must be drawn from Protocol III committed targets: Background epistemic register / Claim scope relative to Method / Contribution incrementality framing / Method scope adequacy]

*Per-excluded-category verification (Protocol III committed format -- one specific sentence per row):*
> Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]
> Result quantification: N -- [one sentence naming the diagnosed weakness and stating why it is not about adding or strengthening numeric evidence in the Result]
> Implication tightening: N -- [one sentence naming the diagnosed weakness and stating why it is not about removing modal hedges or narrowing the enabling action]
> Prose coherence: N -- [one sentence naming the diagnosed weakness and stating why it is not about transition quality or paragraph flow]

*Why specific per-row sentences matter -- named shortcut closure:* The first-order shortcut is the template form "[confirmed / explain if uncertain]" -- a response of "[confirmed]" with a parenthetical category description satisfies the structural shape of per-category verification without producing independently auditable reasoning. The parenthetical label describes the exclusion criterion; it does not apply that criterion to the specific weakness under diagnosis. The second-order shortcut is category-mirroring: a sentence that appears specific but merely restates the category label in other words (e.g., for the Gap sharpening row: "the weakness is about Background register, not the Gap sentence's specificity" -- this restates the category boundary without naming what about the diagnosed weakness makes it non-Gap). Both shortcuts satisfy the row format while bypassing independent reasoning. The required form names the diagnosed weakness concretely and states why that specific weakness does not fall in this slot -- a reader auditing the row can verify the exclusion without access to either the parenthetical template or the category label. The "[confirmed]" shortcut and the category-mirroring shortcut are both prohibited by Protocol III committed format.

*Why this constraint matters:* Amendments 2-5 address predictable weaknesses in four named slots. The diagnostic value of Amendment 1 is in identifying what the fixed slots cannot catch. The weakness category must be drawn from Protocol III committed targets.

*Where to look instead -- positive search space (Protocol III committed targets):*

*Why a separate block -- structural asymmetry:* A Why constraint block that embeds positive search targets CAN be satisfied in a single reading pass -- both the exclusion rationale and the positive targets are co-located and read together. A dedicated positive-space block CANNOT serve as the Why constraint block without collapsing the two cognitive tasks. A dedicated block makes the positive search space independently auditable.

- **Background epistemic register**: Does the Background use observational or domain-survey language when the paper type is theoretical? Does it use conceptual-landscape language when the paper type is empirical? A register mismatch signals a paper type that has not propagated into the draft.
- **Claim scope relative to Method**: Is the Claim stronger than what the Method and Result can establish? Overclaiming in the Claim section is a reviewer flag that survives all four targeted amendments.
- **Contribution incrementality framing**: Would a reviewer read the Claim as "the authors did more of something" rather than "the authors resolved something that prior work could not resolve"?
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
