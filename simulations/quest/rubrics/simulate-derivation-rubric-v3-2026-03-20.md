Written to `simulations/quest/rubrics/simulate-derivation-rubric-v3-2026-03-20.md`.

---

**What changed from v2:**

Three new aspirational criteria from Round 2 V-05 excellence signals:

| ID | New Criterion | Source Signal | What it catches |
|----|---------------|---------------|-----------------|
| C-14 | APPROX validity reasoning demonstrably independent | own-words-gate | Tracer paraphrases source instead of reasoning from first principles — the "[state explicitly]" vs "in your own words" phrase boundary |
| C-15 | All structural axes stack without phase-dropping | three-axis-no-degradation | One axis silently degrading when another is active — expanded sub-steps without verification blocks, or prose rule reverting in some blocks |
| C-16 | Prose reasoning density uniform across block types | prose-rule-synergy | APPROX sub-blocks rich with prose while primary checks are bare YES/NO — the token-budget leak from behavioral inconsistency |

**Point structure:** Essential 60 + Recommended 30 + Aspirational 40 = **130 total** (was 115). Aspirational expands from 5x5 to 8x5.

**Scoring bands updated:** Exemplary now 105-130 (was 100-115).

**R2 ceiling in v3 terms:** V-05's 110 maps to Proficient (110/130) since C-14/C-15/C-16 were untargeted. R3 objective is V-06 hitting all three new axes plus the C-07 P1/P2 priority fix. Expected ceiling: 127-130.
 all R2 variations — one line adding the
explicit P1/P2 priority rule in Phase 4 recovers that. C-14, C-15, C-16 are the new R3
aspirational targets. Expected R3 ceiling: 127-130.

---

## Essential Criteria (60 pts total)

### C-01 | Derivation map present and complete
- **Category**: correctness
- **Weight**: essential
- **Points**: 12
- **Pass condition**: A derivation map table is present with columns: S-ID, expression
  applied, resulting expression, justification, and type
  (EXACT / APPROX / DEFINITION / PHYSICAL). Every non-trivial derivation step in the
  source artifact has a corresponding row. At least 3 rows present (or all steps if
  fewer than 3 exist).

---

### C-02 | Step-by-step verification block for each step
- **Category**: correctness
- **Weight**: essential
- **Points**: 12
- **Pass condition**: Each S-ID in the derivation map has a corresponding verification
  block containing: algebraic correctness verdict (YES / NO / CONDITIONAL), dimensional
  consistency check (YES / NO / NOT APPLICABLE), sign check (YES / NO), and a final
  verdict (SOUND / WEAK / BROKEN). No S-ID is skipped.

---

### C-03 | Every APPROX step is explicitly flagged
- **Category**: correctness
- **Weight**: essential
- **Points**: 12
- **Pass condition**: For every step typed APPROX in the derivation map, the verification
  block states: (a) what quantity or relationship is being approximated, (b) the validity
  condition under which the approximation holds, and (c) whether the source paper states
  this approximation. If the paper has zero APPROX steps, this criterion auto-passes with
  a note confirming that fact.

---

### C-04 | Derivation Fault Register present and actionable
- **Category**: coverage
- **Weight**: essential
- **Points**: 12
- **Pass condition**: A fault register table exists with columns F-ID, S-ID, verdict,
  type, description, and fix. Every step with verdict WEAK or BROKEN appears in the
  fault register. Each fault has a severity label (P1 / P2 / P3): P1 = algebraically
  wrong, P2 = unstated approximation, P3 = notational/clarity issue. If no faults are
  found, the register explicitly states "No faults found" with a brief justification.

---

### C-05 | Artifact written with required frontmatter
- **Category**: format
- **Weight**: essential
- **Points**: 12
- **Pass condition**: The artifact is written to `signals/simulate/derivation/` (or the
  `--output` path if provided). Frontmatter contains exactly: `skill: simulate-derivation`,
  `topic`, `date`, `steps_traced` (integer), `p1_errors` (integer), `unstated_approx`
  (integer). Values are consistent with the derivation map and fault register.

---

## Recommended Criteria (30 pts total)

### C-06 | Overall derivation soundness verdict is explicit
- **Category**: depth
- **Weight**: recommended
- **Points**: 10
- **Pass condition**: The artifact states whether the derivation is globally sound. The
  verdict is one of: SOUND (all steps verified), CONDITIONALLY SOUND (all steps verified
  under stated approximations), or BROKEN (at least one P1 error blocks the conclusion).
  The verdict appears in a summary section, not buried in a step block.

---

### C-07 | Amend section maps to actual faults found
- **Category**: behavior
- **Weight**: recommended
- **Points**: 10
- **Pass condition**: The AMEND section provides exactly three targeted fixes. Each fix
  references a specific F-ID from the fault register. If P1 faults exist, at least one
  fix addresses a P1. If P2 faults exist, at least one fix addresses a P2. Fixes are
  specific enough to act on (not generic advice like "check the algebra").

---

### C-08 | Step types are correctly classified
- **Category**: correctness
- **Weight**: recommended
- **Points**: 10
- **Pass condition**: EXACT steps cite or sketch the algebraic identity that makes them
  exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). PHYSICAL steps
  state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0").
  Spot-check: at least 2 randomly selected EXACT or PHYSICAL steps have traceable
  justifications; none are labeled EXACT when they contain an unexplained jump.

---

## Aspirational Criteria (40 pts total)

### C-09 | Catches at least one fault not acknowledged by the paper
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Pass condition**: At least one fault in the fault register identifies an error,
  unstated approximation, or dimensional inconsistency not already flagged or caveated
  in the source paper itself. The fault register entry notes "not acknowledged by paper"
  or equivalent.

---

### C-10 | Expands compressed steps with intermediate lines
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Pass condition**: At least one step in the derivation map where the paper skips an
  intermediate algebraic step is expanded. The intermediate expression is supplied as a
  sub-step (S-03a, S-03b pattern) and marked as "(interpolated)" to distinguish it from
  the paper's own steps.

---

### C-11 | APPROX verification includes tracer's independent validity statement
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-04 excellence signal -- prose-required-approx-sub-block
- **Pass condition**: For each APPROX step, the tracer provides an independent
  substantive statement of (a) what is being approximated and (b) the conditions under
  which the approximation holds -- stated in the tracer's own words, derived from domain
  knowledge or first principles. Simply reporting whether the source paper states the
  approximation (YES/NO) does not satisfy this criterion. The paper's coverage is noted
  separately as (c). If the artifact has zero APPROX steps, this criterion auto-passes
  with a confirming note.

---

### C-12 | Fault severity labels appear inline in Amend fixes
- **Category**: behavior
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-04 excellence signal -- severity-inline-amend
- **Pass condition**: Each fix in the AMEND section includes the fault's severity label
  in the format "[F-ID] [P1/P2/P3]: [specific fix]", making severity triage visible at
  the point of recommended action, not only in the fault register. A fix that cites the
  F-ID but omits the severity label does not satisfy this criterion.

---

### C-13 | Verification blocks contain substantive prose per check
- **Category**: correctness
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-04 excellence signal -- token-budget-redirect (output translation)
- **Pass condition**: For at least half of the verification blocks, each of the three
  primary checks (algebraic, dimensional, sign) is accompanied by at least one sentence
  of reasoning -- not bare YES/NO verdicts. Example: "YES -- both sides have units of
  [kg/s]; the time derivative of mass is dimensionally consistent." Blocks providing
  only YES/NO with no explanation for any check do not satisfy this criterion.

---

### C-14 | APPROX validity reasoning is demonstrably independent of source phrasing
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-05 excellence signal -- own-words-gate
- **Pass condition**: For each APPROX step, the tracer's statement of (b) the validity
  condition uses vocabulary and framing that cannot be produced by lightly rewording the
  source sentence. The reasoning traces to a named domain principle (e.g., "small-angle
  regime," "quasi-static assumption," "low Reynolds number") or a first-principles
  argument that the tracer could have stated without reading the source sentence. A
  statement that paraphrases what the paper says -- even using different words -- does
  not satisfy this criterion. The distinguishing test: if the source sentence were
  removed, would the tracer's (b) statement still be fully supportable? If yes, it is
  independent. If no, it is paraphrase. If the artifact has zero APPROX steps, this
  criterion auto-passes with a confirming note.

---

### C-15 | All structural axes present simultaneously without phase-dropping
- **Category**: coverage
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-05 excellence signal -- three-axis-no-degradation
- **Pass condition**: If and only if the artifact contains all three structural axes --
  (a) interpolated sub-steps from a Phase 1b expansion pass, (b) NEW-tagged faults in
  the fault register identifying paper-unacknowledged errors, and (c) prose reasoning in
  verification blocks -- then all three must hold simultaneously with no silent
  degradation. Specifically: every interpolated sub-step has a corresponding verification
  block (no Phase 2 holes at expanded rows); every NEW-tagged fault has a complete fault
  register entry with F-ID, description, and fix; and the prose rule applies to both
  APPROX sub-blocks and primary checks with no block reverting to bare YES/NO. If fewer
  than all three axes are present in the artifact, this criterion scores 0 -- it rewards
  full integration only.

---

### C-16 | Prose reasoning density is uniform across APPROX sub-blocks and primary checks
- **Category**: correctness
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-05 excellence signal -- prose-rule-synergy
- **Pass condition**: The artifact does not exhibit a two-tier reasoning density where
  APPROX sub-blocks contain explanatory sentences but the primary verification checks
  (algebraic, dimensional, sign) in the same step are bare YES/NO tokens -- or vice
  versa. In any step block where the APPROX sub-block contains at least one sentence of
  reasoning, the primary checks in that same block must also contain at least one sentence
  of reasoning. Uniform density -- sparse throughout or rich throughout -- passes. Mixed
  density within a single step block fails. The behavioral inconsistency of
  prose-required APPROX alongside bare-allowed primary checks is a token-budget leak
  regardless of whether the individual check verdicts are technically correct.

---

## Quick Reference

| ID   | Criterion                                      | Weight       | Category    | Pts |
|------|------------------------------------------------|--------------|-------------|-----|
| C-01 | Derivation map present and complete            | essential    | correctness | 12  |
| C-02 | Verification block for each step               | essential    | correctness | 12  |
| C-03 | Every APPROX step explicitly flagged           | essential    | correctness | 12  |
| C-04 | Fault register present and actionable          | essential    | coverage    | 12  |
| C-05 | Artifact with required frontmatter             | essential    | format      | 12  |
| C-06 | Overall soundness verdict explicit             | recommended  | depth       | 10  |
| C-07 | Amend maps to actual faults                    | recommended  | behavior    | 10  |
| C-08 | Step types correctly classified                | recommended  | correctness | 10  |
| C-09 | Catches fault not in paper                     | aspirational | depth       | 5   |
| C-10 | Expands compressed steps                       | aspirational | depth       | 5   |
| C-11 | APPROX verified independently (prose)          | aspirational | depth       | 5   |
| C-12 | Severity labels inline in Amend fixes          | aspirational | behavior    | 5   |
| C-13 | Verification blocks contain prose reasoning    | aspirational | correctness | 5   |
| C-14 | APPROX reasoning independent of source         | aspirational | depth       | 5   |
| C-15 | All axes stack without phase-dropping          | aspirational | coverage    | 5   |
| C-16 | Prose density uniform across block types       | aspirational | correctness | 5   |
|      | **Total**                                      |              |             | **130** |

---

## Scoring Bands (v3)

| Band       | Score Range | Meaning                                                         |
|------------|-------------|-----------------------------------------------------------------|
| Exemplary  | 105-130     | All essential + recommended pass; 3+ aspirational earned        |
| Proficient | 80-104      | All essential pass; at least 2 recommended pass                 |
| Adequate   | 60-79       | All essential pass; recommended partially met                   |
| Failing    | < 60        | One or more essential criteria fail                             |

A score below 60 (any essential failure) is a failing output regardless of total points.

**R2 ceiling in v3 terms**: V-05 scored 110/115 under v2. Mapped to v3 (130 total), V-05
would score 110/130 -- Proficient -- since C-14, C-15, and C-16 were not targeted. The R3
objective is a V-06 prompt that adds: the own-words independence gate (C-14), axis stacking
completeness verification (C-15), uniform prose density rule (C-16), and the P1/P2 priority
rule in Phase 4 (C-07 residual gap). Expected R3 ceiling: 127-130.
