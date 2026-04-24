Written to `simulations/quest/variations/simulate-derivation-variations-R5-2026-03-20.md`.

---

## R5 Variations Summary

**Base**: V-05-R4 (160/160 under v5 -- Exemplary)

**R5 thesis**: V-05-R4 satisfies C-20/C-21/C-22 by having the correct text in the correct template locations. The v5 rubric's R5 objective is to encode those patterns as **independently verifiable first-principles commitments** -- design invariants the LLM can self-apply in novel contexts, not just copy from templates.

**Three single axes:**

| Variation | Axis | What changes | Risk |
|-----------|------|-------------|------|
| V-01 | Gate design principle (C-20) | Named principle added to Phase 2 preamble: "every mandatory gate names the BLOCKED verdict token, not the corrective action" | Minimal -- ~40 words, no template changes |
| V-02 | Axis-label alignment principle (C-21) | Named principle + distinguishing test added before Phase 1b table; axis A and C labels extended to name exact operations | Low -- additive, increases label density |
| V-03 | Unconditional ordering principle (C-22) | Ordering principle with WHY added before Phase 4 Amend rule: "conditional chains leave subordinate tiers implicit" | Minimal -- ~50 words, no structural change |
| V-04 | V-01 + V-03 (safe combined) | Gate + ordering principles in phase-local positions | Low -- two isolated additions |
| V-05 | All three in consolidated preamble | `## STRUCTURAL COMMITMENTS` block before Phase 1; axis labels extended; Phase 4 cross-references preamble | Moderate -- ~120 pre-Phase-1 words; V-04 is fallback |

**Key design decision for V-05**: The preamble means the LLM builds its compliance model from all three principles *before* reading any phase template. The gate principle makes the LLM check whether any gate in the skill names a blocked verdict. The label principle gives the LLM a test to apply to every axis label it writes. The ordering principle tells the LLM why unconditional enumeration is required -- not just what form to use.

**V-05 is V-07 in the overall variation lineage** (R1: base, R2: V-01-V-05 core structure, R3: V-03-V-05 gateway + APPROX, R4: V-01-V-05 SOUND BLOCKED + ordering + labeling, R5: V-01-V-05 first-principles encoding).
he right R5 target:**

V-05-R4 satisfies C-20 because "SOUND BLOCKED" appears in the APPROX template. But the LLM has no principle governing gate construction -- in a novel gate context it has no basis to name a blocked verdict. Similarly, "NEW-tagged fault detection" satisfies C-21 by label text alone, and "P1 first, then P2, then P3" satisfies C-22 by sentence form alone. In each case the LLM copied the correct pattern without understanding why it is required. First-principles encoding gives the LLM: (1) the invariant as a named principle, (2) the distinguishing test for compliance, and (3) the WHY -- enabling self-verification in edge cases not covered by any template.

**Expected R5 ceiling with V-05**: 160/160 with structural robustness that was absent in R4's V-05. V-04 is the fallback if the consolidated preamble in V-05 adds cognitive load and causes Phase 1 or Phase 2 compression on long derivations.

**Risk analysis:**
- V-01: minimal risk -- adds ~40 words to Phase 2 preamble, no template changes
- V-02: low risk -- axis label extensions are additive; the label principle paragraph adds ~50 words
- V-03: minimal risk -- adds ~50 words before existing ordering rule, no structural change
- V-04: low risk -- two isolated additions, no interaction
- V-05: moderate risk -- preamble adds ~120 words before Phase 1; long derivations may compress; V-04 is fallback

---

## V-01 -- Gate Design Principle (C-20 first-principles)

**Axis**: Consequence-naming gate principle declared as a universal structural invariant, not as a template patch
**Hypothesis**: V-05-R4 adds "SOUND BLOCKED" in the APPROX template satisfying C-20 by having the correct text at one specific location. But the LLM has no principle governing gate construction in general -- in a novel gate context it would not know to name a blocked verdict. Adding a named gate principle in the Phase 2 preamble declares the invariant once: every mandatory gate in this skill names the verdict token that is blocked, not merely the corrective action required. The LLM can then apply this principle to any gate it encounters (APPROX, Phase 1b axis-commitment, future extensions) independently, without needing to read a specific template text. C-20's "independently verifiable" dimension should improve.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step -- the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## PHASE 1 -- DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity -- the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). A step with an unexplained jump may not be labeled EXACT.
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically -- the Justification cell must state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0," "incompressible flow," "quasi-static process")

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 1b -- STEP EXPANSION PASS

After completing the derivation map, scan each row for compressed steps -- any step where the paper jumps from one expression to a significantly different one without showing the intermediate algebra.

For each compressed step you identify:
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if more sub-steps are needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 1b COMPLETION CHECK

Before proceeding to Phase 2, confirm that all three structural axes are active. Fill each Status cell with ACTIVE or ABSENT.

| Axis | Requirement | Status |
|------|-------------|--------|
| A -- Sub-step expansion | At least one interpolated sub-step inserted, OR "No compressed steps identified -- C-10 auto-passes" explicitly stated above | |
| B -- Prose reasoning | Prose-per-check rule (YES -- [sentence] / NO -- [sentence]) will apply to every check in every verification block in Phase 2 | |
| C -- NEW-tagged fault detection | Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive a "NEW: not acknowledged by paper" tag in the fault register | |

All present axes must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all present axes show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

**Gate design principle**: Every mandatory gate in this skill names the verdict token that is blocked until compliance -- not merely the corrective action that is required. The gate instruction states "X BLOCKED for this step" or "An X verdict may not be recorded while [condition] remains." This principle applies to every gate in this skill. At any gate, the question to answer is not "did I perform the required action?" but "has the condition blocking X been cleared?"

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block fails this rule.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring]
  CONDITIONAL -- [state the condition that must hold and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply here]

Sign check:
  Does the sign of every term make physical or mathematical sense?
  YES -- [state the physical or mathematical principle that governs the expected sign]
  NO -- [identify the specific term, state the expected sign, and give the reasoning]

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly in the tracer's own words -- do not merely quote the paper]
  Under what conditions does this approximation hold?
    [name the domain regime, physical principle, or first-principles argument --
     e.g., "small-angle regime," "quasi-static assumption," "low Reynolds number."
     Do not paraphrase the source sentence; ground the statement in domain knowledge.]
  Source-removal test: if the source sentence describing this approximation were removed
    entirely, could you support your validity condition from domain knowledge alone?
    YES (independent) / NO (paraphrase)
    If NO: SOUND BLOCKED for this step. You must replace (b) with a statement grounded
    in a named domain principle or first-principles argument before proceeding. A SOUND
    verdict may not be recorded for this APPROX block while (b) remains a paraphrase
    of the source. Correct (b) now, then continue to the step verdict line.
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]

Source acknowledgment (complete only when verdict is WEAK or BROKEN):
  Does the source paper flag or acknowledge this specific issue anywhere --
  main text, footnotes, discussion section, or stated limitations? YES / NO
  If NO: this fault is a NEW finding -- the paper does not acknowledge it.
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes. C-17 auto-passes."

---

## PHASE 3 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** -- algebraically wrong
- **P2** -- approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** -- correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column.

---

## PHASE 4 -- GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section -- do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3.

Severity ordering rule: order all three fixes by severity -- P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-02 -- Axis-Label Alignment Principle (C-21 first-principles)

**Axis**: Commitment table axis-label precision stated as a named design principle with distinguishing test; axis A and C labels extended to match
**Hypothesis**: V-05-R4 relabels axis C to "NEW-tagged fault detection" satisfying C-21 by having the correct label text. But the LLM has no principle governing label quality -- if prompted to add a new axis it would default to general-category language. Adding a named axis-label principle immediately before the completion check table declares the invariant with its distinguishing test ("could a non-compliant behavior satisfy this label by reasonable reading?"). The LLM can apply this test to every label it writes, not just copy the one example. Axis A is also extended to "Interpolated sub-step expansion with S-NNa/S-NNb labeling" (names the exact format) and axis C is extended to "NEW-tagged fault detection for unacknowledged errors" (names the exact condition and tag text), making both independently testable against the principle.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step -- the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## PHASE 1 -- DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity -- the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). A step with an unexplained jump may not be labeled EXACT.
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically -- the Justification cell must state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0," "incompressible flow," "quasi-static process")

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 1b -- STEP EXPANSION PASS

After completing the derivation map, scan each row for compressed steps -- any step where the paper jumps from one expression to a significantly different one without showing the intermediate algebra.

For each compressed step you identify:
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if more sub-steps are needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 1b COMPLETION CHECK

**Axis-label principle**: Each row label in this table names the precise mechanistic operation being committed to -- specific enough that a non-compliant behavior cannot satisfy the label by reasonable reading. Distinguishing test: "Could a different, non-compliant behavior satisfy this label by a reasonable reading?" If yes, the label is too general. Passing labels name the exact operation and, where relevant, the exact format or condition required.

Before proceeding to Phase 2, confirm that all three structural axes are active. Fill each Status cell with ACTIVE or ABSENT.

| Axis | Requirement | Status |
|------|-------------|--------|
| A -- Interpolated sub-step expansion with S-NNa/S-NNb labeling | At least one interpolated sub-step inserted using the S-NNa/S-NNb format, OR "No compressed steps identified -- C-10 auto-passes" explicitly stated above | |
| B -- Prose-per-check reasoning in all verification blocks | Prose-per-check rule (YES -- [sentence] / NO -- [sentence]) will apply to every check in every verification block in Phase 2 | |
| C -- NEW-tagged fault detection for unacknowledged errors | Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive the exact tag "NEW: not acknowledged by paper" in the fault register Description column | |

All present axes must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all present axes show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block fails this rule.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring]
  CONDITIONAL -- [state the condition that must hold and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply here]

Sign check:
  Does the sign of every term make physical or mathematical sense?
  YES -- [state the physical or mathematical principle that governs the expected sign]
  NO -- [identify the specific term, state the expected sign, and give the reasoning]

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly in the tracer's own words -- do not merely quote the paper]
  Under what conditions does this approximation hold?
    [name the domain regime, physical principle, or first-principles argument --
     e.g., "small-angle regime," "quasi-static assumption," "low Reynolds number."
     Do not paraphrase the source sentence; ground the statement in domain knowledge.]
  Source-removal test: if the source sentence describing this approximation were removed
    entirely, could you support your validity condition from domain knowledge alone?
    YES (independent) / NO (paraphrase)
    If NO: SOUND BLOCKED for this step. You must replace (b) with a statement grounded
    in a named domain principle or first-principles argument before proceeding. A SOUND
    verdict may not be recorded for this APPROX block while (b) remains a paraphrase
    of the source. Correct (b) now, then continue to the step verdict line.
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]

Source acknowledgment (complete only when verdict is WEAK or BROKEN):
  Does the source paper flag or acknowledge this specific issue anywhere --
  main text, footnotes, discussion section, or stated limitations? YES / NO
  If NO: this fault is a NEW finding -- the paper does not acknowledge it.
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes. C-17 auto-passes."

---

## PHASE 3 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** -- algebraically wrong
- **P2** -- approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** -- correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column.

---

## PHASE 4 -- GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section -- do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3.

Severity ordering rule: order all three fixes by severity -- P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-03 -- Unconditional Ordering Principle (C-22 first-principles)

**Axis**: Severity ordering rule declared as a design principle with explicit explanation of why conditional chains are insufficient
**Hypothesis**: V-05-R4 states "P1 fixes first, then P2 fixes, then P3 fixes" satisfying C-22 by having the correct unconditional enumeration. But the LLM has no principle explaining WHY this form is required. Adding the ordering principle before the rule -- "a conditional chain states the top tier leads but leaves all subordinate-tier ordering implicit" -- gives the LLM the WHY. The LLM can now check its own output for hidden conditional reasoning: an Amend with P2 and P3 faults but a P3 fix before a P2 fix satisfies the conditional form while violating the unconditional rule. With the principle stated, the LLM can self-verify the ordering against the WHY, not just check whether the sentence form matches.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step -- the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## PHASE 1 -- DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity -- the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). A step with an unexplained jump may not be labeled EXACT.
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically -- the Justification cell must state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0," "incompressible flow," "quasi-static process")

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 1b -- STEP EXPANSION PASS

After completing the derivation map, scan each row for compressed steps -- any step where the paper jumps from one expression to a significantly different one without showing the intermediate algebra.

For each compressed step you identify:
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if more sub-steps are needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 1b COMPLETION CHECK

Before proceeding to Phase 2, confirm that all three structural axes are active. Fill each Status cell with ACTIVE or ABSENT.

| Axis | Requirement | Status |
|------|-------------|--------|
| A -- Sub-step expansion | At least one interpolated sub-step inserted, OR "No compressed steps identified -- C-10 auto-passes" explicitly stated above | |
| B -- Prose reasoning | Prose-per-check rule (YES -- [sentence] / NO -- [sentence]) will apply to every check in every verification block in Phase 2 | |
| C -- NEW-tagged fault detection | Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive a "NEW: not acknowledged by paper" tag in the fault register | |

All present axes must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all present axes show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block fails this rule.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring]
  CONDITIONAL -- [state the condition that must hold and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply here]

Sign check:
  Does the sign of every term make physical or mathematical sense?
  YES -- [state the physical or mathematical principle that governs the expected sign]
  NO -- [identify the specific term, state the expected sign, and give the reasoning]

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly in the tracer's own words -- do not merely quote the paper]
  Under what conditions does this approximation hold?
    [name the domain regime, physical principle, or first-principles argument --
     e.g., "small-angle regime," "quasi-static assumption," "low Reynolds number."
     Do not paraphrase the source sentence; ground the statement in domain knowledge.]
  Source-removal test: if the source sentence describing this approximation were removed
    entirely, could you support your validity condition from domain knowledge alone?
    YES (independent) / NO (paraphrase)
    If NO: SOUND BLOCKED for this step. You must replace (b) with a statement grounded
    in a named domain principle or first-principles argument before proceeding. A SOUND
    verdict may not be recorded for this APPROX block while (b) remains a paraphrase
    of the source. Correct (b) now, then continue to the step verdict line.
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]

Source acknowledgment (complete only when verdict is WEAK or BROKEN):
  Does the source paper flag or acknowledge this specific issue anywhere --
  main text, footnotes, discussion section, or stated limitations? YES / NO
  If NO: this fault is a NEW finding -- the paper does not acknowledge it.
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes. C-17 auto-passes."

---

## PHASE 3 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** -- algebraically wrong
- **P2** -- approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** -- correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column.

---

## PHASE 4 -- GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section -- do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3.

**Ordering principle**: Every multi-tier ordering rule in this skill is stated as a single unconditional enumeration naming all tiers in order. A conditional chain ("if P1 faults exist, fix P1 first; if no P1 but P2 exist, fix P2 first") states the top tier leads but leaves all subordinate-tier ordering implicit -- an Amend with P2 and P3 faults can satisfy the conditional form while placing a P3 fix before a P2 fix. The unconditional enumeration makes every tier relationship explicit in a single declarative statement, leaving no gap invisible.

Severity ordering rule: order all three fixes by severity -- P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-04 -- Combined: Gate Principle + Ordering Principle (V-01 + V-03)

**Axes**: V-01 (C-20 gate principle in Phase 2 preamble) + V-03 (C-22 ordering principle in Phase 4 preamble)
**Hypothesis**: Gate principle and ordering principle are structurally isolated (Phase 2 preamble vs Phase 4 preamble) with no interaction. Together they encode C-20 and C-22 as first-principles commitments. V-02's axis-label principle is excluded as a fallback strategy -- the extended axis labels in V-02 are additive but add visual density to the completion check table. V-04 is the preferred fallback if V-05's consolidated preamble causes Phase 1 or Phase 2 compression on long derivations.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step -- the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## PHASE 1 -- DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity -- the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). A step with an unexplained jump may not be labeled EXACT.
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically -- the Justification cell must state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0," "incompressible flow," "quasi-static process")

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 1b -- STEP EXPANSION PASS

After completing the derivation map, scan each row for compressed steps -- any step where the paper jumps from one expression to a significantly different one without showing the intermediate algebra.

For each compressed step you identify:
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if more sub-steps are needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 1b COMPLETION CHECK

Before proceeding to Phase 2, confirm that all three structural axes are active. Fill each Status cell with ACTIVE or ABSENT.

| Axis | Requirement | Status |
|------|-------------|--------|
| A -- Sub-step expansion | At least one interpolated sub-step inserted, OR "No compressed steps identified -- C-10 auto-passes" explicitly stated above | |
| B -- Prose reasoning | Prose-per-check rule (YES -- [sentence] / NO -- [sentence]) will apply to every check in every verification block in Phase 2 | |
| C -- NEW-tagged fault detection | Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive a "NEW: not acknowledged by paper" tag in the fault register | |

All present axes must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all present axes show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

**Gate design principle**: Every mandatory gate in this skill names the verdict token that is blocked until compliance -- not merely the corrective action that is required. The gate instruction states "X BLOCKED for this step" or "An X verdict may not be recorded while [condition] remains." This principle applies to every gate in this skill. At any gate, the question to answer is not "did I perform the required action?" but "has the condition blocking X been cleared?"

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block fails this rule.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring]
  CONDITIONAL -- [state the condition that must hold and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply here]

Sign check:
  Does the sign of every term make physical or mathematical sense?
  YES -- [state the physical or mathematical principle that governs the expected sign]
  NO -- [identify the specific term, state the expected sign, and give the reasoning]

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly in the tracer's own words -- do not merely quote the paper]
  Under what conditions does this approximation hold?
    [name the domain regime, physical principle, or first-principles argument --
     e.g., "small-angle regime," "quasi-static assumption," "low Reynolds number."
     Do not paraphrase the source sentence; ground the statement in domain knowledge.]
  Source-removal test: if the source sentence describing this approximation were removed
    entirely, could you support your validity condition from domain knowledge alone?
    YES (independent) / NO (paraphrase)
    If NO: SOUND BLOCKED for this step. You must replace (b) with a statement grounded
    in a named domain principle or first-principles argument before proceeding. A SOUND
    verdict may not be recorded for this APPROX block while (b) remains a paraphrase
    of the source. Correct (b) now, then continue to the step verdict line.
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]

Source acknowledgment (complete only when verdict is WEAK or BROKEN):
  Does the source paper flag or acknowledge this specific issue anywhere --
  main text, footnotes, discussion section, or stated limitations? YES / NO
  If NO: this fault is a NEW finding -- the paper does not acknowledge it.
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes. C-17 auto-passes."

---

## PHASE 3 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** -- algebraically wrong
- **P2** -- approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** -- correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column.

---

## PHASE 4 -- GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section -- do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3.

**Ordering principle**: Every multi-tier ordering rule in this skill is stated as a single unconditional enumeration naming all tiers in order. A conditional chain ("if P1 faults exist, fix P1 first; if no P1 but P2 exist, fix P2 first") states the top tier leads but leaves all subordinate-tier ordering implicit -- an Amend with P2 and P3 faults can satisfy the conditional form while placing a P3 fix before a P2 fix. The unconditional enumeration makes every tier relationship explicit in a single declarative statement, leaving no gap invisible.

Severity ordering rule: order all three fixes by severity -- P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-05 -- Full Ceiling: Consolidated Structural Commitments Preamble (V-07 in overall lineage)

**Axes**: All three principles (C-20 gate, C-21 label, C-22 ordering) consolidated into a single "## STRUCTURAL COMMITMENTS" block before Phase 1; Phase 1b completion check table note + extended axis labels per V-02; Phase 4 ordering rule cross-references preamble
**Hypothesis**: V-01 through V-03 embed each principle at the phase where it is first needed. This means the LLM reads the gate principle only when it reaches Phase 2, the label principle only at Phase 1b, and the ordering principle only at Phase 4. Consolidating all three into a preamble means the LLM reads all three structural commitments before any phase template -- building its compliance model from the principles first. Benefits:
1. The LLM can verify compliance with all three principles independently before generating any template output
2. The principles govern each other: knowing the label principle makes the LLM check the gate label ("SOUND BLOCKED") against the label quality test; knowing the gate principle makes the LLM check whether any future ordering rule names a blocked verdict
3. A single preamble is auditable in one pass -- an evaluator can check all three commitments without scanning phase-specific locations

**Risk**: Preamble adds ~120 words before Phase 1; long derivations may compress Phase 2 or Phase 3. V-04 is the fallback (gate + ordering principles in phase-local positions, no preamble).

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step -- the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## STRUCTURAL COMMITMENTS

Three design principles govern all gates, axis labels, and ordering rules in this skill. Read these before beginning Phase 1. They apply to every phase.

**Gate principle**: Every mandatory gate in this skill names the verdict token that is blocked until compliance -- not merely the corrective action required. The gate instruction states "X BLOCKED for this step" or "An X verdict may not be recorded while [condition] remains." The verification question at any gate is: "Has the condition blocking X been cleared?" not "Did I perform the required action?" A recovery instruction that states only what to do, without naming what cannot happen, does not satisfy this principle.

**Axis-label principle**: Each row label in every commitment table names the precise mechanistic operation being committed to -- specific enough that a non-compliant behavior cannot satisfy the label by reasonable reading. Distinguishing test: "Could a different, non-compliant behavior satisfy this label?" If yes, replace the label with one that names the exact operation and, where relevant, the exact format or condition required.

**Ordering principle**: Every multi-tier ordering rule in this skill is stated as a single unconditional enumeration naming all tiers in order. Conditional chains ("if P1 exists, fix P1; if no P1 but P2 exists, fix P2") state the top tier leads but leave all subordinate-tier ordering implicit. The unconditional enumeration makes every tier relationship explicit in a single declarative statement, leaving no gap invisible.

---

## PHASE 1 -- DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity -- the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). A step with an unexplained jump may not be labeled EXACT.
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically -- the Justification cell must state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0," "incompressible flow," "quasi-static process")

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 1b -- STEP EXPANSION PASS

After completing the derivation map, scan each row for compressed steps -- any step where the paper jumps from one expression to a significantly different one without showing the intermediate algebra.

For each compressed step you identify:
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if more sub-steps are needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 1b COMPLETION CHECK

Before proceeding to Phase 2, confirm that all three structural axes are active. Fill each Status cell with ACTIVE or ABSENT.

(Axis labels follow the axis-label principle from Structural Commitments: each names the precise mechanistic operation, not the general category.)

| Axis | Requirement | Status |
|------|-------------|--------|
| A -- Interpolated sub-step expansion with S-NNa/S-NNb labeling | At least one interpolated sub-step inserted using the S-NNa/S-NNb format, OR "No compressed steps identified -- C-10 auto-passes" explicitly stated above | |
| B -- Prose-per-check reasoning in all verification blocks | Prose-per-check rule (YES -- [sentence] / NO -- [sentence]) will apply to every check in every verification block in Phase 2 | |
| C -- NEW-tagged fault detection for unacknowledged errors | Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive the exact tag "NEW: not acknowledged by paper" in the fault register Description column | |

All present axes must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all present axes show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block fails this rule.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring]
  CONDITIONAL -- [state the condition that must hold and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply here]

Sign check:
  Does the sign of every term make physical or mathematical sense?
  YES -- [state the physical or mathematical principle that governs the expected sign]
  NO -- [identify the specific term, state the expected sign, and give the reasoning]

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly in the tracer's own words -- do not merely quote the paper]
  Under what conditions does this approximation hold?
    [name the domain regime, physical principle, or first-principles argument --
     e.g., "small-angle regime," "quasi-static assumption," "low Reynolds number."
     Do not paraphrase the source sentence; ground the statement in domain knowledge.]
  Source-removal test: if the source sentence describing this approximation were removed
    entirely, could you support your validity condition from domain knowledge alone?
    YES (independent) / NO (paraphrase)
    If NO: SOUND BLOCKED for this step. You must replace (b) with a statement grounded
    in a named domain principle or first-principles argument before proceeding. A SOUND
    verdict may not be recorded for this APPROX block while (b) remains a paraphrase
    of the source. Correct (b) now, then continue to the step verdict line.
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]

Source acknowledgment (complete only when verdict is WEAK or BROKEN):
  Does the source paper flag or acknowledge this specific issue anywhere --
  main text, footnotes, discussion section, or stated limitations? YES / NO
  If NO: this fault is a NEW finding -- the paper does not acknowledge it.
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes. C-17 auto-passes."

---

## PHASE 3 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** -- algebraically wrong
- **P2** -- approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** -- correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column.

---

## PHASE 4 -- GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section -- do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3.

Severity ordering rule (unconditional enumeration per the ordering principle in Structural Commitments): order all three fixes by severity -- P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]
