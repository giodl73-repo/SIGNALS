Written to `simulations/quest/variations/simulate-derivation-variations-R2-2026-03-20.md`.

---

## 5 Variations -- simulate-derivation R2

All inherit the V-04-R1 proven base (compressed acquisition, expanded APPROX sub-block with a/b/c in verification block, token-budget-redirect, `[F-ID] [severity]: [fix]` Amend format). Each adds exactly one new mechanism targeting the gaps from R1 scoring.

| ID | Axis | Single change from V-04-R1 base | Target criteria |
|----|------|---------------------------------|----------------|
| **V-01** | Fault attribution framing | "acknowledged by paper?" gate after WEAK/BROKEN verdict + `NEW:` tag in fault register | C-09 (0/5 in R1) |
| **V-02** | Step resolution | Phase 1b expansion pass with `(interpolated)` sub-step notation | C-10 (0/5 in R1) |
| **V-03** | Verification verbosity | Prose-required per check: `YES -- [sentence]` instead of bare `YES` | C-13 + C-11 |
| **V-04** | Combined: V-01 + V-02 | Phase 1b + source acknowledgment gate (no structural conflict -- different insertion points) | C-09 + C-10 |
| **V-05** | Combined: all three | Phase 1b + source acknowledgment + prose-per-check | C-09 + C-10 + C-13 + C-11 |

---

### Design decisions

**Why all three single-axis axes are independent:**
- V-01 inserts 2 lines *inside* existing verification blocks at the verdict point
- V-02 inserts a standalone *pre-verification* phase between Phase 1 and Phase 2
- V-03 changes the *format* of check lines already present

None of these touch the same part of the prompt. V-04 and V-05 are straightforward stacks.

**The 10 free points from R1 (C-09 + C-10):** V-01 and V-02 are the minimum-change bets. If the LLM follows the gate instruction, C-09 should recover nearly full points. If it follows the expansion instruction, C-10 should recover most points. V-04 tests whether both hold simultaneously.

**V-03's indirect effect:** The prose-per-check rule forces token budget into reasoning. This also strengthens C-11 (tracer's own words on APPROX validity) because the APPROX sub-block prose format is now consistent with the rest of the block -- no more behavioral inconsistency between bare-YES/NO primary checks and prose-required APPROX checks.

**V-05 is the ceiling test:** Maximum instruction density. If the LLM handles all three axes without truncating output, it should be the highest scorer. If the prompt becomes too demanding and the LLM drops phases, V-04 (simpler combination) will outperform it.
ACT**: exact algebraic identity
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID, produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

```
S-[NN]: [description of what this step does]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly? YES / NO / CONDITIONAL
  If CONDITIONAL: state the condition explicitly.
  If NO: describe the exact error (wrong sign, missing term, incorrect exponent, etc.).

Dimensional consistency check:
  Are the units on LHS equal to units on RHS? YES / NO / NOT APPLICABLE
  If NO: identify which side has incorrect dimensions and why.

Sign check:
  Does the sign of every term make physical or mathematical sense? YES / NO
  If NO: identify the term and the expected sign with reasoning.

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly -- e.g., "x << 1 so sin(x) approx x", "weakly-coupled limit so cross-terms drop"]
  Under what conditions does this approximation hold?
    [state the validity condition -- e.g., "valid when kT << E_gap", "holds for Re < 1"]
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN

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

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column. This marks your independent contribution -- a fault the paper itself did not flag.

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

## V-02 -- Step Resolution: Compressed-Step Expansion

**Axis**: Step resolution
**Hypothesis**: Adding an explicit step-expansion pass immediately after the derivation map -- with (interpolated) sub-step notation and a no-compressed-steps confirmation -- prompts the tracer to surface the intermediate expressions the paper skips. Every R1 variation scored 0/5 on C-10 because none asked for it. The expansion pass is a pre-verification scan that does not conflict with any other phase.

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
- Mark the sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

Example: if S-04 jumps from `f(t) = a * exp(-bt) * cos(ct)` to `f(t) approx a(1 - bt)` in one step, expand as:
- S-04a (interpolated): apply first-order Taylor to exp(-bt) -> `a * (1 - bt + ...) * cos(ct)`
- S-04b (interpolated): truncate higher-order terms and small-angle cos(ct) approx 1 -> `a * (1 - bt)`

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps. They may surface their own faults.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly? YES / NO / CONDITIONAL
  If CONDITIONAL: state the condition explicitly.
  If NO: describe the exact error (wrong sign, missing term, incorrect exponent, etc.).

Dimensional consistency check:
  Are the units on LHS equal to units on RHS? YES / NO / NOT APPLICABLE
  If NO: identify which side has incorrect dimensions and why.

Sign check:
  Does the sign of every term make physical or mathematical sense? YES / NO
  If NO: identify the term and the expected sign with reasoning.

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly -- e.g., "x << 1 so sin(x) approx x", "weakly-coupled limit so cross-terms drop"]
  Under what conditions does this approximation hold?
    [state the validity condition -- e.g., "valid when kT << E_gap", "holds for Re < 1"]
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]
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

## V-03 -- Prose-per-check Verification

**Axis**: Verification verbosity
**Hypothesis**: Replacing bare YES/NO verdict tokens with required one-sentence reasoning per check forces the LLM to reason through each check rather than pattern-match to a token. This directly satisfies C-13 (substantive prose in verification blocks), strengthens C-11 (independent APPROX validity statement in the tracer's own words), and reduces the risk of confident-but-wrong verdicts. The APPROX sub-block already uses prose format in V-04-R1 -- this variation extends that pattern to all three primary checks.

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

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID, produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

```
S-[NN]: [description of what this step does]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring, etc.]
  CONDITIONAL -- [state the condition that must hold, and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply: pure algebraic, dimensionless ratio, etc.]

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

## V-04 -- Combined: Fault Attribution + Step Expansion

**Axes**: V-01 (fault attribution framing) + V-02 (step resolution)
**Hypothesis**: C-09 and C-10 target completely independent gaps with no structural conflict -- the NEW-fault gate adds two lines inside existing verification blocks; the expansion pass adds one standalone phase before verification. Stacking both on V-04-R1 should recover up to 10 aspirational points (C-09 + C-10) without the axes interfering with each other or the existing APPROX sub-block structure.

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
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly? YES / NO / CONDITIONAL
  If CONDITIONAL: state the condition explicitly.
  If NO: describe the exact error (wrong sign, missing term, incorrect exponent, etc.).

Dimensional consistency check:
  Are the units on LHS equal to units on RHS? YES / NO / NOT APPLICABLE
  If NO: identify which side has incorrect dimensions and why.

Sign check:
  Does the sign of every term make physical or mathematical sense? YES / NO
  If NO: identify the term and the expected sign with reasoning.

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly -- e.g., "x << 1 so sin(x) approx x", "weakly-coupled limit so cross-terms drop"]
  Under what conditions does this approximation hold?
    [state the validity condition -- e.g., "valid when kT << E_gap", "holds for Re < 1"]
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN

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

## V-05 -- Combined: All Three New Axes

**Axes**: V-01 (fault attribution) + V-02 (step expansion) + V-03 (prose-per-check)
**Hypothesis**: The three axes target non-overlapping gaps -- C-09 (NEW-fault labeling), C-10 (interpolated sub-steps), C-13/C-11 (prose reasoning per check). None conflict structurally: V-01 adds lines at the verdict point, V-02 adds a standalone pre-verification phase, V-03 changes how existing check lines are formatted. Combined they address all five new/zero-score criteria simultaneously at the cost of a more demanding prompt. If the LLM follows all instructions, this should approach the ceiling of what a prompt can recover from the v2 aspirational criteria.

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
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. A block containing only YES or NO tokens for any check fails the minimum standard.

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

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue, append "NEW: not acknowledged by paper" to the Description column.

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
