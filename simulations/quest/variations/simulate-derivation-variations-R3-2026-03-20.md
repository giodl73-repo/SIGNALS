Written to `simulations/quest/variations/simulate-derivation-variations-R3-2026-03-20.md`.

---

## Summary — simulate-derivation R3 Variations

**Base**: V-05-R2 (proven ceiling at 110/130 under v3 scoring)

**R3 gaps targeted** (all scored 0/5 in R2 since rubric didn't exist yet):

| Variation | Axis | Single change | Target |
|-----------|------|---------------|--------|
| **V-01** | Independence gate | Source-removal test added to APPROX sub-block (b): "if the source sentence were removed, could you support this from domain knowledge alone? YES/NO" | C-14 |
| **V-02** | Axis-stacking self-check | Three-row completion checkpoint table after Phase 1b: axes A/B/C must all show ACTIVE before Phase 2 begins | C-15 |
| **V-03** | Uniform prose density | Density uniformity rule added to Phase 2 preamble: rich APPROX prose in a block requires rich primary checks in that same block | C-16 |
| **V-04** | V-01 + V-03 | Independence gate + density uniformity (complementary: C-14 raises APPROX bar, C-16 pulls primary checks up to match) | C-14 + C-16 |
| **V-05** | All three + C-07 fix | Full stack + P1/P2 priority rule in Phase 4 Amend ("first fix must address P1 if any exist") | C-14 + C-15 + C-16 + C-07 residual |

**Key structural observations:**
- V-01 changes only the APPROX (b) sub-question (inside the block template)
- V-02 inserts a checkpoint table between phases (no Phase 2 changes)
- V-03 adds a rule paragraph before the block template (no template changes)
- None of the three touch the same prompt location — stacking is clean
- V-05 is the ceiling test; V-04 is the safer combined bet if V-02's checkpoint adds overhead cost

**Expected R3 ceiling with V-05**: 127-130 if the LLM sustains all four axes without phase-dropping.
in the tracer's own words" -- the v3 rubric tightens this to "demonstrably independent of source phrasing." A paraphrase with different words still fails. The source-removal test ("if the source sentence were removed, could you still support this from domain knowledge?") is the distinguishing operation. V-01 makes this test explicit rather than implied.

**The axis-stacking check in V-02 (C-15):** C-15 fails when one axis silently degrades while others are active -- e.g., interpolated sub-steps appear but lack verification blocks, or prose rule reverts in some blocks. The checkpoint forces the LLM to assert all three axes active before entering Phase 2. This is a commitment device, not new logic.

**The density uniformity rule in V-03 (C-16):** The R2 prose rule applied globally to "all checks" but did not address within-block inconsistency. The LLM could produce rich APPROX sub-block prose and bare YES/NO primary checks in the same step block. V-03 makes the per-block uniformity constraint explicit: mixed density within a block fails, regardless of whether individual verdicts are correct.

**C-07 residual gap (V-05 only):** The R2 Amend instruction said "cite an F-ID from Phase 3" but did not enforce P1/P2 priority ordering. V-05 adds the explicit priority rule: if P1 faults exist, the first fix must address one. This was the remaining gap in recommended scoring.

**V-05 is the ceiling test:** Maximum instruction density across all four gaps. If the LLM handles all axes without truncating Phase 2 or dropping the expansion pass, it should approach 127-130. If it cannot sustain all four simultaneously, V-04 (C-14 + C-16, no axis-stacking check) will likely outperform.

---

## V-01 -- Independence Gate for APPROX Validity

**Axis**: Independence gate framing
**Hypothesis**: The v2 prompt instructs "state in the tracer's own words" but the v3 C-14 rubric requires reasoning demonstrably independent of source phrasing -- not just differently worded paraphrase. Making the source-removal test an explicit sub-question ("could you support this from domain knowledge if the source sentence were removed?") forces the LLM to distinguish between paraphrase and independent domain reasoning, which the implicit "own words" instruction did not reliably trigger.

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
- **EXACT**: exact algebraic identity
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

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

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

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
    If NO: replace (b) with a domain-principle-grounded statement before recording your verdict.
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
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes."

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

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3:
1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-02 -- Axis-Stacking Self-Check

**Axis**: Axis-stacking self-check
**Hypothesis**: C-15 fails when one structural axis silently degrades while the others are active -- interpolated sub-steps appear without verification blocks, or the prose rule reverts in some step blocks. Adding an explicit three-axis inventory checkpoint immediately after Phase 1b forces the LLM to commit to all three axes as active before entering Phase 2. This is a commitment device: the LLM cannot passively drop an axis it has just confirmed as ACTIVE.

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
- **EXACT**: exact algebraic identity
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

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
| C -- Source acknowledgment | Source acknowledgment gate will execute for every WEAK or BROKEN step verdict in Phase 2 | |

All three must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all three show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

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
    [state the validity condition in the tracer's own words -- e.g., "valid when kT << E_gap"]
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
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes."

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

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3:
1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-03 -- Uniform Prose Density Rule

**Axis**: Uniform prose density rule
**Hypothesis**: The R2 prose rule applied globally ("do not write bare YES or NO") but did not prevent within-block density mismatch -- APPROX sub-block with rich explanatory prose while the primary checks in the same block remained bare YES/NO tokens. The v3 C-16 rubric specifically catches this two-tier pattern as a "token-budget leak." Adding an explicit per-block uniformity constraint -- "within any single step block, prose density must match across APPROX sub-block and primary checks" -- closes this gap without changing any other instruction.

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
- **EXACT**: exact algebraic identity
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

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

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence -- not a bare YES or NO. The reverse also applies: if the primary checks in a block are bare tokens, the APPROX sub-block must also be bare. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block -- rich APPROX prose alongside bare primary checks, or vice versa -- fails this rule.

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
    [state the validity condition in the tracer's own words -- e.g., "valid when kT << E_gap"]
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
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes."

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

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3:
1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-04 -- Combined: Independence Gate + Uniform Density

**Axes**: V-01 (independence gate framing) + V-03 (uniform prose density rule)
**Hypothesis**: C-14 and C-16 both concern the quality and consistency of APPROX sub-block reasoning -- C-14 requires the validity condition to be demonstrably independent of source phrasing; C-16 requires it to be no richer or sparser than the primary checks in the same block. These two criteria are complementary: C-14 raises the bar on what goes in the APPROX (b) field, while C-16 ensures the primary checks are brought up to match. Stacking them has no structural conflict -- V-01 adds a sub-question inside the APPROX field, V-03 adds a rule paragraph above the block template. Combined they should recover both C-14 and C-16 without the axis-stacking overhead of V-02.

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
- **EXACT**: exact algebraic identity
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

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

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block -- rich APPROX prose alongside bare primary checks, or vice versa -- fails this rule.

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
    If NO: replace (b) with a domain-principle-grounded statement before recording your verdict.
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
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes."

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

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3:
1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-05 -- Full Ceiling: All Three R3 Axes + C-07 Priority Fix

**Axes**: V-01 (independence gate) + V-02 (axis-stacking check) + V-03 (uniform density rule) + C-07 P1/P2 priority rule in Phase 4
**Hypothesis**: All four gaps that separate 110/130 from 127-130 are addressed simultaneously. V-01 recovers C-14, V-02 recovers C-15, V-03 recovers C-16, and the Phase 4 priority rule recovers the C-07 residual gap (Amend first fix must address the highest-severity fault). None of these changes conflict structurally: V-01 modifies the APPROX sub-block (b) field, V-02 adds a checkpoint table after Phase 1b, V-03 adds a rule paragraph before Phase 2's block template, and the C-07 fix adds a priority sentence before the Amend list. If the LLM sustains all four simultaneously without truncating Phase 2 or dropping the expansion pass, this should be the ceiling prompt for v3.

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
- **EXACT**: exact algebraic identity
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

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
| C -- Source acknowledgment | Source acknowledgment gate will execute for every WEAK or BROKEN step verdict in Phase 2 | |

All three must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all three show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block -- rich APPROX prose alongside bare primary checks, or vice versa -- fails this rule.

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
    If NO: replace (b) with a domain-principle-grounded statement before recording your verdict.
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
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes."

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

Priority rule: if P1 faults exist in the register, your first fix must address a P1 fault. If no P1 faults exist but P2 faults exist, at least one fix must address a P2 fault. Highest-severity issue leads the Amend section.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]
