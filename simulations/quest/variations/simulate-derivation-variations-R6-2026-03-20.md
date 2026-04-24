Written to `simulations/quest/variations/simulate-derivation-variations-R6-2026-03-20.md`.

---

## R6 Variations Summary

**Base**: V-05-R5 (175/175 under v6)

**R6 thesis**: V-05-R5 satisfies C-23/C-24/C-25 by having the correct preamble architecture -- but every application site the LLM encounters was anticipated by the template. The APPROX gate is the only gate; Phase 4 is the only ordering site; the completion check is the only label site. R6 tests genuine generalization by adding **novel application contexts** the template did not anticipate.

---

### Variation map

| # | Axis | Decisive change | Risk |
|---|------|----------------|------|
| V-01 | Novel EXACT gate | Phase 1 type definitions add a mandatory gate: `EXACT BLOCKED` while the Justification cell names no algebraic rule. Gate principle must generalize beyond the APPROX context. | Minimal -- ~50 words in Phase 1 |
| V-02 | Explicit cross-evaluation block in preamble | STRUCTURAL COMMITMENTS adds a `**Cross-evaluation**` block showing each principle applied to another as a demonstration before Phase 1. C-25 becomes LLM-readable evidence, not inert design property. Includes a genuine boundary case: gate principle and ordering principle govern complementary domains (verdict tokens vs fix sequences). | Low -- ~80 words in preamble |
| V-03 | Saturated application-site cross-reference | Phase 2 APPROX gate adds `(per the gate principle in Structural Commitments...)`. V-05-R5 cross-references Phase 1b (axis-label) and Phase 4 (ordering); V-03 fills the missing Phase 2 site. All three major application sites now auditable in one pass. | Minimal -- one phrase |
| V-04 | V-01 + V-03 (fallback) | Novel EXACT gate + saturated cross-references. No preamble growth. Preferred fallback if V-05's ~130-word preamble expansion causes compression on long derivations. | Low |
| V-05 | Full ceiling (V-08 lineage) | All three: novel EXACT gate + cross-evaluation block + saturated cross-references. The decisive test: EXACT BLOCKED at Phase 1 has no worked example in V-05-R5 -- any correct application is principle generalization, not template following. | Moderate -- ~130 words added total; V-04 fallback |

---

### Key design decisions

**V-01's novel gate**: The EXACT gate is the most load-bearing test of principle generalization. The preamble says "X BLOCKED while [condition] remains" -- V-01 forces the LLM to apply that pattern at a type-classification site (Phase 1) it has never seen in any prior template. If the LLM writes `EXACT BLOCKED for any step where the algebraic rule remains unnamed`, that is evidence of first-principles application.

**V-02's cross-evaluation**: The block reveals a genuine structural boundary -- the gate principle governs verdict tokens, the ordering principle governs fix sequences. They are complementary, not redundant. This prevents false equivalences where the LLM treats both as "gate-like" and over-applies one principle to the other's domain.

**V-05 vs V-04**: V-05's preamble grows by ~130 words total. On a 10-step derivation, this is acceptable. On a 20-step derivation with dense Phase 2 blocks, context pressure may cause Phase 3 compression. V-04 is the fallback -- it sacrifices the cross-evaluation demonstration (V-02) but retains the novel gate test (V-01) and the cross-reference saturation (V-03).
ins.

**V-05 is V-08 in the overall variation lineage** (R1: base, R2: V-01-V-05 core structure, R3: V-03-V-05 gateway + APPROX, R4: V-01-V-05 SOUND BLOCKED + ordering + labeling, R5: V-01-V-05 first-principles encoding, R6: V-01-V-05 novel context application).

**Expected R6 ceiling with V-05**: 175/175 with demonstrated novel-context application that was structurally absent in R5's V-05. V-04 is the fallback if the cross-evaluation block in the preamble causes Phase 1 or Phase 2 compression on long derivations.

**Risk analysis:**
- V-01: minimal risk -- adds ~50 words to Phase 1 type section; EXACT gate is additive
- V-02: low risk -- adds ~80 words to preamble; the cross-evaluation block is declarative, not a required LLM output step
- V-03: minimal risk -- one phrase added to APPROX gate instruction; no structural change
- V-04: low risk -- two isolated additions, no preamble changes
- V-05: moderate risk -- preamble grows by ~80 words + Phase 1 grows by ~50 words; V-04 is fallback

---

## V-01 -- Novel EXACT Gate (C-25 novel application)

**Axis**: Gate principle applied at a type-classification site in Phase 1 -- a mandatory gate blocking EXACT labeling when the Justification cell names no algebraic rule. This is a novel application site not present in V-05's template; the gate principle must generalize from the APPROX context where it was first encoded.
**Hypothesis**: V-05-R5 encodes the gate principle in the preamble and applies it at the APPROX source-removal gate. But the APPROX gate is the only gate in the skill -- the LLM applies the gate principle by following a template example, not by generalizing it. Adding a mandatory EXACT-classification gate in Phase 1 forces the gate principle to be applied at a structurally different location (type assignment rather than approximation verification) using the same vocabulary ("EXACT BLOCKED while [condition] remains"). If the gate principle is truly a first-principles commitment, the LLM should correctly apply it at this novel site without a worked example at Phase 2. C-25 evidence should improve because the gate principle is applied to a context where the label principle's distinguishing test is relevant (does "EXACT BLOCKED" name a specific non-recordable action?).

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

**EXACT classification gate** (per the gate principle in Structural Commitments): A step may not be labeled EXACT while the Justification cell contains an unexplained jump -- a transition from one expression to a significantly different one with no named algebraic rule, identity, or substitution. If the Justification cell is blank, states only "see paper," or cites an equation number without naming the algebraic operation performed, EXACT is BLOCKED for that step. Relabel as APPROX if an approximation may be hiding the gap, DEFINITION if a symbol is introduced, or PHYSICAL if a physical assumption is encoded. EXACT BLOCKED for any step where the algebraic rule remains unnamed.

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

---

## V-02 -- Explicit Cross-Evaluation in Preamble (C-25 executable)

**Axis**: STRUCTURAL COMMITMENTS adds a "Cross-evaluation" block that explicitly applies each principle to another, as a demonstration the LLM reads before Phase 1. C-25 becomes an LLM-executed step rather than a passive design property.
**Hypothesis**: V-05-R5 satisfies C-25 because the principles are co-located and designed to be mutually applicable. But the preamble never demonstrates the mutual application -- the LLM must infer it. Adding an explicit cross-evaluation block does three things: (1) it gives the LLM a worked example of cross-principle reasoning at the highest-priority position in the skill (before any phase), (2) it reveals a genuine structural boundary between the gate principle and the ordering principle (they govern different action types -- verdicts vs fix sequences), which is domain knowledge the LLM can use to avoid false equivalences, and (3) it makes C-25 checkable in a single pass by any evaluator reading the preamble. The cross-evaluation block is declarative (the LLM reads it) not productive (the LLM is not asked to complete it) -- so it adds ~80 words to the preamble without adding an output requirement.

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

**Cross-evaluation** (these principles govern each other -- apply them before Phase 1):

- *Axis-label principle applied to the gate verdict token*: Does "SOUND BLOCKED" satisfy the distinguishing test -- could a non-compliant behavior (e.g., recording WEAK instead of SOUND) satisfy this label by reasonable reading? No -- "SOUND BLOCKED" names the exact verdict token that cannot be recorded; WEAK is a different token, not a compliance path. Passes.
- *Gate principle applied to the ordering rule*: If the ordering rule were formulated as a gate, would it name the blocked action? The ordering rule blocks a lower-severity fix from preceding a higher-severity fix in the Amend list -- the blocked action is a misordered fix sequence, not a verdict token. The gate principle and the ordering principle govern complementary domains (verdict recording vs fix sequencing); neither subsumes the other.
- *Ordering principle applied to this preamble*: Are the three principles listed as an unconditional enumeration? Gate, Axis-label, Ordering -- three named principles in fixed order. Passes.

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

---

## V-03 -- Saturated Application-Site Cross-Reference (C-24 extended)

**Axis**: The Phase 2 APPROX gate adds an explicit cross-reference to the gate principle by name -- "per the gate principle in Structural Commitments." V-05-R5 already cross-references the axis-label principle (Phase 1b table note) and the ordering principle (Phase 4 amend rule); V-03 saturates all three major application sites by adding the missing Phase 2 cross-reference.
**Hypothesis**: C-24 requires at least one application site to cross-reference its governing preamble principle. V-05-R5 satisfies C-24 with two cross-references (Phase 1b and Phase 4). V-03 asks: does adding the Phase 2 cross-reference improve output quality, or is the minimum sufficient? The Phase 2 APPROX gate is the most load-bearing gate in the skill -- the place where the gate principle does the most work. If the cross-reference is present at Phase 2, an LLM reading only Phase 2 (after a context compression or long derivation) can still trace back to the governing principle. Saturating all three sites makes the declaration-to-application chain auditable regardless of which section the LLM is currently generating. Risk is minimal -- one phrase added to an existing instruction.

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
    If NO: SOUND BLOCKED for this step (per the gate principle in Structural Commitments --
    the gate names the verdict token that is blocked until compliance, not merely the
    corrective action). You must replace (b) with a statement grounded in a named domain
    principle or first-principles argument before proceeding. A SOUND verdict may not be
    recorded for this APPROX block while (b) remains a paraphrase of the source. Correct
    (b) now, then continue to the step verdict line.
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

---

## V-04 -- Combined: Novel Gate + Saturated Cross-Reference (V-01 + V-03)

**Axes**: V-01 (novel EXACT gate in Phase 1 using gate-principle language) + V-03 (Phase 2 APPROX gate cross-references the gate principle by name). No preamble content changes. Fallback for V-05 if the cross-evaluation block adds too much cognitive load.
**Hypothesis**: Novel EXACT gate and saturated cross-references are structurally isolated (Phase 1 vs Phase 2) with no interaction. Together they test the gate principle at two application sites and make both cross-referable to the preamble. V-02's cross-evaluation block is excluded as a fallback strategy -- it is additive to the preamble but adds the most words (~80). V-04 is the preferred fallback if V-05's preamble growth causes Phase 1 or Phase 2 compression on long derivations.

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

**EXACT classification gate** (per the gate principle in Structural Commitments): A step may not be labeled EXACT while the Justification cell contains an unexplained jump -- a transition from one expression to a significantly different one with no named algebraic rule, identity, or substitution. If the Justification cell is blank, states only "see paper," or cites an equation number without naming the algebraic operation performed, EXACT is BLOCKED for that step. Relabel as APPROX if an approximation may be hiding the gap, DEFINITION if a symbol is introduced, or PHYSICAL if a physical assumption is encoded. EXACT BLOCKED for any step where the algebraic rule remains unnamed.

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
    If NO: SOUND BLOCKED for this step (per the gate principle in Structural Commitments --
    the gate names the verdict token that is blocked until compliance, not merely the
    corrective action). You must replace (b) with a statement grounded in a named domain
    principle or first-principles argument before proceeding. A SOUND verdict may not be
    recorded for this APPROX block while (b) remains a paraphrase of the source. Correct
    (b) now, then continue to the step verdict line.
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

---

## V-05 -- Full Ceiling: Novel Gate + Cross-Evaluation + Saturated Cross-Reference (V-08 in overall lineage)

**Axes**: V-01 (novel EXACT gate in Phase 1 using gate-principle language) + V-02 (cross-evaluation block in STRUCTURAL COMMITMENTS) + V-03 (Phase 2 APPROX gate cross-references gate principle by name). All three preamble-architecture patterns demonstrated simultaneously at contexts the V-05-R5 template did not anticipate.
**Hypothesis**: V-01 proves the gate principle generalizes beyond the APPROX context. V-02 makes C-25 an LLM-executed step by showing cross-principle evaluation as a demonstration in the preamble. V-03 saturates all three major application sites with cross-references, making the declaration-to-application chain auditable at every gate, table, and ordering rule. Together they test whether the skill produces the same structural behavior on a paper the template authors have not seen -- the LLM must apply gate-principle vocabulary at the EXACT gate (never demonstrated in V-05-R5), apply ordering-principle framing at Phase 4 (demonstrated), and apply axis-label-principle framing at the completion check (demonstrated). The novel EXACT gate is the decisive test: V-05-R5 has no worked example for this gate, so any correct EXACT BLOCKED label at Phase 1 is evidence of principle generalization, not template following.

**Risk**: Preamble grows by ~80 words (V-02 cross-evaluation block) + Phase 1 grows by ~50 words (V-01 EXACT gate) = ~130 words of added instruction before the first derivation map row. On a long derivation (10+ steps), this may cause compression in Phase 2 or Phase 3. V-04 is the fallback (novel EXACT gate + saturated cross-references, no preamble growth from cross-evaluation block).

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

**Cross-evaluation** (these principles govern each other -- apply them before Phase 1):

- *Axis-label principle applied to the gate verdict token*: Does "SOUND BLOCKED" satisfy the distinguishing test -- could a non-compliant behavior (e.g., recording WEAK instead of SOUND) satisfy this label by reasonable reading? No -- "SOUND BLOCKED" names the exact verdict token that cannot be recorded; WEAK is a different token, not a compliance path. Passes.
- *Gate principle applied to the ordering rule*: If the ordering rule were formulated as a gate, would it name the blocked action? The ordering rule blocks a lower-severity fix from preceding a higher-severity fix in the Amend list -- the blocked action is a misordered fix sequence, not a verdict token. The gate principle and the ordering principle govern complementary domains (verdict recording vs fix sequencing); neither subsumes the other.
- *Ordering principle applied to this preamble*: Are the three principles listed as an unconditional enumeration? Gate, Axis-label, Ordering -- three named principles in fixed order. Passes.

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

**EXACT classification gate** (per the gate principle in Structural Commitments): A step may not be labeled EXACT while the Justification cell contains an unexplained jump -- a transition from one expression to a significantly different one with no named algebraic rule, identity, or substitution. If the Justification cell is blank, states only "see paper," or cites an equation number without naming the algebraic operation performed, EXACT is BLOCKED for that step. Relabel as APPROX if an approximation may be hiding the gap, DEFINITION if a symbol is introduced, or PHYSICAL if a physical assumption is encoded. EXACT BLOCKED for any step where the algebraic rule remains unnamed.

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
    If NO: SOUND BLOCKED for this step (per the gate principle in Structural Commitments --
    the gate names the verdict token that is blocked until compliance, not merely the
    corrective action). You must replace (b) with a statement grounded in a named domain
    principle or first-principles argument before proceeding. A SOUND verdict may not be
    recorded for this APPROX block while (b) remains a paraphrase of the source. Correct
    (b) now, then continue to the step verdict line.
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
