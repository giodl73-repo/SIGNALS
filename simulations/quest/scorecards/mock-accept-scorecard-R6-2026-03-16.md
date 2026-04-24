Now I have everything needed. Let me score all five variations.

---

# Scorecard: mock-accept Round 6

**Rubric:** v6 | **Date:** 2026-03-16
**Baseline:** R5 V-05 (all C-01–C-23 satisfied)
**Variations scored:** V-01 through V-05

---

## Criteria Reference

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 to C-05 (12 pts each) | 60 |
| Recommended | C-06 to C-08 (10 pts each) | 30 |
| Aspirational | C-09 to C-23 (1.25 pts each × 15) | 18.75 |
| **Ceiling** | | **108.75** |

---

## V-01 — Role Sequence (Coverage Analyst / Decision Authority Split)

### Essential (C-01–C-05)

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | FORBIDDEN OUTPUTS TRIAD + completeness check + AUTO-RULE CONTAMINATION GUARD | **PASS** | All three triad labels present with explicit "A two-of-three set does not satisfy this gate." AUTO-RULE CONTAMINATION named with void consequence. |
| C-02 | [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] all labeled | **PASS** | All three bracket labels present in PHASE GATE block. |
| C-03 | Status written back in-place + CANARY ASSERTION | **PASS** | STEP 8 uses Edit tool on `{mock-artifact-path}`; CANARY GATE Branch A/B present with mutual exclusion. |
| C-04 | Review artifact with required structure (4-col table, P1/P2/P3, urgency labels) | **PASS** | STEP 7 writes to `simulations/mock/{topic}-accept-{date}.md`; ordering rule, P1/P2/P3, urgency present. |
| C-05 | MOCK-ACCEPTED two-slot positive argument | **PASS** | Slot 2 (Contrast) and Slot 1 (Structural position) structurally separate; reason-code enumeration exact. |

**Essential: 60/60**

### Recommended (C-06–C-08)

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-06 | Entity-naming grammar on all sub-questions | **PASS** | "Yes/no answers do not satisfy entity-naming sub-question requirements." in STEP 3. |
| C-07 | Step sequencing + guard compliance + two-list partition | **PASS** | Arch-blocked list, Proceeding list, ARCH-GUARD-BYPASS, STRATEGY-TO-PM-GUARD-BYPASS all named at guard sites. |
| C-08 | REAL-REQUIRED template with all seven fields | **PASS** | trigger, Failing evaluation, Failing verdict, Claim, Subject-check, Error-code, Artifact state all present. |

**Recommended: 30/30**

### Aspirational (C-09–C-23)

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09–C-16 | R3 inherited patterns (all 8) | **PASS ×8** | All R3 guard structures, trigger field at fixed position, two-list partition, cross-step guards intact; no regression. |
| C-17 | `Semantics: SUCCESS` labeled field in Branch B | **PASS** | Line 364: "Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode." Present. |
| C-18 | CANARY TERMINOLOGY TABLE as dedicated non-conflation structure | **PASS** | Named table block with CANARY SUPPRESSED / CANARY-FALSE-POSITIVE rows, structurally separate. |
| C-19 | Subject-check metacognitive sub-step on Error-code | **PASS** | Subject-check is a named, non-skippable sub-step with explicit conditional logic, not a parenthetical. |
| C-20 | Branch-anchor exemplars on both Subject-check branches | **PASS** | SUBJECT-CHECK EXAMPLES TABLE present with VERDICT-ECHO branch (named example) and NONE branch (named example). |
| C-21 | Enforcement note following CANARY TERMINOLOGY TABLE | **PASS** | ENFORCEMENT NOTE block structurally separate from table, follows immediately. |
| C-22 | Count-anchored completeness assertion after CROSS-TEMPLATE RELATIONSHIP BLOCK | **PASS** | Lines 263–264: "Verify: all 7 field rows above are mapped before filling either template. Count: 7 rows defined. Confirm 7 rows present before proceeding." |
| C-23 | Named `Violation:` field inside ENFORCEMENT NOTE block | **PASS** | Lines 350–352: `Violation: Emitting CANARY ASSERTION when one or more Status fields remain as "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.` |

**Aspirational: 15/15 × 1.25 = 18.75/18.75**

**Note on C-17:** The variate axis-assignment plan flags "C-17 is PARTIAL in those three [V-01/V-02/V-03]; V-04/V-05 recover it via the role header instruction." This references a per-namespace `SUBJECT OF EVALUATION:` line from R5 V-05 — a v4/v5 rubric artifact. Under v6, C-17 is redefined as `Semantics: SUCCESS` in Branch B. All 5 variations have it. Score reflects v6 rubric. The per-namespace SUBJECT OF EVALUATION: pattern should be tracked as a separate candidate (C-27 or absorbed into C-24 framing) if the variate author intends it as a structural requirement.

**New axis probe: C-24 (ROLE-SEPARATION GATE with ANALYST-PREMATURE-DECISION) — PRESENT.** Decision labels prohibited from Steps 1–5 output; gate check verifies zero MOCK-ACCEPTED / REAL-REQUIRED labels before Decision Authority; AUTHORITY-REREAD named error present.

### V-01 Total: **108.75 / 108.75**

---

## V-02 — Inertia Framing (Per-Namespace Cost-of-MOCK Statement)

### Essential (C-01–C-05)

| # | Result | Evidence |
|---|--------|----------|
| C-01 | **PASS** | FORBIDDEN OUTPUTS TRIAD with completeness check present; AUTO-RULE CONTAMINATION GUARD named. |
| C-02 | **PASS** | All three bracket labels present. |
| C-03 | **PASS** | STEP 8 with Edit tool; CANARY GATE Branch A/B. ENFORCEMENT NOTE with Violation: present. |
| C-04 | **PASS** | STEP 7 with 4-col Coverage Review table, P1/P2/P3 ordering, urgency labels. |
| C-05 | **PASS** | Slot 1 and Slot 2 present and structurally separate; reason codes enumerated exactly. |

**Essential: 60/60**

### Recommended (C-06–C-08)

| # | Result | Evidence |
|---|--------|----------|
| C-06 | **PASS** | Entity-naming requirement stated in STEP 3. |
| C-07 | **PASS** | Two-list partition, ARCH-GUARD-BYPASS, STRATEGY-TO-PM-GUARD-BYPASS all present. |
| C-08 | **PASS** | All seven REAL-REQUIRED fields present. V-02 adds `Inertia validation:` as an eighth field (structural bonus above minimum). |

**Recommended: 30/30**

### Aspirational (C-09–C-23)

All C-09–C-23 carry from R5 V-05 base with no regression. Specific checks:

| # | Result | Evidence |
|---|--------|----------|
| C-17 | **PASS** | `Semantics: SUCCESS` in Branch B (line 688). |
| C-18 | **PASS** | CANARY TERMINOLOGY TABLE present and named. |
| C-19 | **PASS** | Subject-check named sub-step. |
| C-20 | **PASS** | SUBJECT-CHECK EXAMPLES TABLE with both branch exemplars. |
| C-21 | **PASS** | ENFORCEMENT NOTE follows CANARY TERMINOLOGY TABLE. |
| C-22 | **PASS** | "Count: 7 rows defined. Confirm 7 rows present before proceeding." (lines 579–580). |
| C-23 | **PASS** | `Violation:` field inside ENFORCEMENT NOTE (lines 675–676). |

**Aspirational: 18.75/18.75**

**New axis probe: C-25 (per-namespace inertia cost named in decision block) — PRESENT.** `Cost-of-MOCK:` field in MOCK-ACCEPTED template with COST-UNSPECIFIED error code; `Inertia validation:` with Lift condition and LIFT-UNSPECIFIED error code in REAL-REQUIRED template. Both fields enforce named tier decision, not generic adequacy.

No ROLE-SEPARATION GATE → C-24 absent. No numeric scoring → C-26 absent.

### V-02 Total: **108.75 / 108.75**

---

## V-03 — Output Format (Numeric Pre-Decision Coverage Score 0–3)

### Essential (C-01–C-05)

All essential criteria PASS. STEP 8 unchanged; CANARY structure complete with C-22/C-23. Coverage Review table and STEP 7 structure identical to R5 V-05. MOCK-ACCEPTED template has both slots; reason codes present.

**Essential: 60/60**

### Recommended (C-06–C-08)

| # | Result | Evidence |
|---|--------|----------|
| C-06 | **PASS** | Entity-naming grammar in STEP 3. |
| C-07 | **PASS** | Two-list partition, both guard names present. |
| C-08 | **PASS** | All seven REAL-REQUIRED fields present. V-03 adds `Failing score: [{0|1}]` as an eighth field distinguishing which score caused threshold failure. |

**Recommended: 30/30**

### Aspirational (C-09–C-23)

All C-09–C-23 carry. No regression. C-17 through C-23 confirmed PASS.

**Aspirational: 18.75/18.75**

**New axis probe: C-26 (numeric pre-decision coverage score) — PRESENT.** `Arch Score`, `Strategy Score`, `PM Score` columns added to evaluation tables (COVERAGE SCORE SCALE defined with 0–3 anchors); COVERAGE SCORE TABLE emitted after STEP 5 with Lowest Score and Preliminary columns; SCORE-AFTER-VERDICT named error enforces score-before-verdict invariant; `Failing score:` in REAL-REQUIRED identifies the disqualifying score value.

No ROLE-SEPARATION GATE → C-24 absent. No inertia framing → C-25 absent.

### V-03 Total: **108.75 / 108.75**

---

## V-04 — Combined: Role Sequence + Inertia Framing

### Essential (C-01–C-05): 60/60

All PASS. FORBIDDEN OUTPUTS TRIAD complete; CANARY structure complete; STEP 7/8 structure intact.

### Recommended (C-06–C-08): 30/30

All PASS. REAL-REQUIRED template now has nine fields (all seven base + `Inertia validation:` + ROLE-SEPARATION GATE context in preamble).

### Aspirational (C-09–C-23)

All C-17–C-23 PASS. Structural inventory confirms no regression.

Notable in V-04: ROLE-SEPARATION GATE now includes third check — "Confirm: Inertia Note is present for every non-auto-flagged namespace." Named error: `INERTIA-NOTE-MISSING`. The gate summary emits `Inertia Notes: {N_notes} recorded.` — both axes tightly integrated.

**Aspirational: 18.75/18.75**

**New axis probes: C-24 + C-25 both PRESENT.**
- C-24: ROLE-SEPARATION GATE includes ANALYST-PREMATURE-DECISION + INERTIA-NOTE-MISSING checks; Decision Authority instruction explicitly sources Cost-of-MOCK from Coverage Analyst Inertia Note ("From Coverage Analyst Inertia Note").
- C-25: Cost-of-MOCK: field in MOCK-ACCEPTED; Inertia validation: with Lift condition in REAL-REQUIRED. Causal chain from observation → decision is complete.

No numeric scoring → C-26 absent.

### V-04 Total: **108.75 / 108.75**

---

## V-05 — Full Integration: Role Sequence + Inertia Framing + Numeric Scoring

### Essential (C-01–C-05): 60/60

All PASS. Full R5 V-05 base preserved.

### Recommended (C-06–C-08): 30/30

All PASS. C-08 now has ten fields in REAL-REQUIRED (all base + `Inertia validation:` + `Failing score:`). All seven required fields confirmed present.

### Aspirational (C-09–C-23)

Full audit:

| # | Result | Evidence |
|---|--------|----------|
| C-09–C-16 | **PASS ×8** | All R3 patterns carried; no structural regression from R5 V-05. |
| C-17 | **PASS** | `Semantics: SUCCESS` in Branch B (line 1373 equivalent). |
| C-18 | **PASS** | CANARY TERMINOLOGY TABLE named and present. |
| C-19 | **PASS** | Subject-check non-skippable named sub-step. |
| C-20 | **PASS** | SUBJECT-CHECK EXAMPLES TABLE with both branch exemplars; no truncation observed — triple-axis structure did not cause length-pressure degradation. |
| C-21 | **PASS** | ENFORCEMENT NOTE follows CANARY TERMINOLOGY TABLE, structurally separate. |
| C-22 | **PASS** | "Count: 7 rows defined. Confirm 7 rows present before proceeding." (lines 1638–1639). |
| C-23 | **PASS** | `Violation:` field inside ENFORCEMENT NOTE. |

**Aspirational: 18.75/18.75**

**New axis probes: C-24 + C-25 + C-26 all PRESENT.**
- C-24: ROLE-SEPARATION GATE with three checks (ANALYST-PREMATURE-DECISION, INERTIA-NOTE-MISSING, SCORE-AFTER-VERDICT); gate summary emits `Inertia Notes: {N_notes} recorded. Coverage Scores: {N_scores} recorded.` — tightest gate in any round.
- C-25: Cost-of-MOCK: in MOCK-ACCEPTED with COST-UNSPECIFIED error code; Inertia validation: in REAL-REQUIRED sourcing from Coverage Analyst Inertia Note; Lift condition requirement.
- C-26: Score columns in all three evaluation tables; COVERAGE SCORE TABLE emitted before ROLE-SEPARATION GATE (inside Coverage Analyst phase); `Failing score:` in REAL-REQUIRED. Triple-axis integration did NOT cause truncation of C-20.

### V-05 Total: **108.75 / 108.75**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | **Total** | C-24 | C-25 | C-26 |
|-----------|-----------|-------------|--------------|-----------|------|------|------|
| V-01 | 60 | 30 | 18.75 | **108.75** | PASS | fail | fail |
| V-02 | 60 | 30 | 18.75 | **108.75** | fail | PASS | fail |
| V-03 | 60 | 30 | 18.75 | **108.75** | fail | fail | PASS |
| V-04 | 60 | 30 | 18.75 | **108.75** | PASS | PASS | fail |
| V-05 | 60 | 30 | 18.75 | **108.75** | PASS | PASS | PASS |

**All 5 variations hit the v6 ceiling. No regression from R5 V-05.**

---

## Rankings

All variations tie at 108.75 under v6 rubric. Secondary ranking by structural depth of new-criterion probing:

1. **V-05** — all three new axes; ceiling probe confirms no length-pressure degradation; ROLE-SEPARATION GATE extended to three checks; `Failing score:` field adds forward trace to score decisions
2. **V-04** — two new axes with tight causal integration (Inertia Note → Cost-of-MOCK chain)
3. **V-01, V-02, V-03** — one new axis each; tied; each probes an independent structural location

---

## Excellence Signals from V-05

**Signal 1 — Tri-check ROLE-SEPARATION GATE**: V-01 gates on two conditions (ANALYST-PREMATURE-DECISION, AUTHORITY-REREAD). V-05 adds a third gate check — SCORE-AFTER-VERDICT — at the role boundary itself, not just at the evaluation step level. The gate summary emits both a note count and a score count, making the Coverage Analyst output a fully auditable record. This is the first gate in any round that checks three independent invariants.

**Signal 2 — Per-namespace inertia causal chain**: V-02 adds Cost-of-MOCK and Inertia validation as independent decision fields. V-05 closes the chain: Coverage Analyst records Inertia Note in the evaluation table → Decision Authority sources Cost-of-MOCK from that Inertia Note with explicit attribution ("From Coverage Analyst Inertia Note"). If the Inertia Note was INERTIA-UNSPECIFIED, the Cost-of-MOCK field must supply the named decision. This creates a traceable obligation from observation to decision block.

**Signal 3 — Score-gated binary verdicts with summary table**: The COVERAGE SCORE TABLE emits inside the Coverage Analyst phase (before the ROLE-SEPARATION GATE), making score data available as a compact pre-decision summary. The `Failing score:` field in REAL-REQUIRED identifies which score caused the threshold failure — adding backward traceability from decision to evidence. SCORE-AFTER-VERDICT is elevated from a per-table check to a gate-level invariant, increasing its enforcement authority.

---

## Rubric v7 — Candidate Criteria

| Candidate | Axis | Pattern | Source variation |
|-----------|------|---------|-----------------|
| C-24 | role-sequence | ROLE-SEPARATION GATE with ANALYST-PREMATURE-DECISION named error; Coverage Analyst produces zero decision labels; Decision Authority instruction prohibits re-read of input artifact | V-01, V-04, V-05 |
| C-25 | inertia-framing | Per-namespace inertia cost named in decision blocks: `Cost-of-MOCK:` in MOCK-ACCEPTED with COST-UNSPECIFIED error code; `Inertia validation:` with Lift condition in REAL-REQUIRED | V-02, V-04, V-05 |
| C-26 | output-format | Numeric pre-decision coverage score (0–3) per evaluation role; COVERAGE SCORE TABLE; SCORE-AFTER-VERDICT named error; `Failing score:` in REAL-REQUIRED | V-03, V-05 |

Aspirational denominator for v7: 15 → 18. Max aspirational: 18 × 1.25 = 22.50. Ceiling: 112.50.

---

```json
{"top_score": 108.75, "all_essential_pass": true, "new_patterns": ["ROLE-SEPARATION GATE with ANALYST-PREMATURE-DECISION named error — Coverage Analyst produces observations only (Steps 1-5); Decision Authority works from completed observation record only; gate checks zero decision labels before authority begins", "Per-namespace inertia causal chain — Coverage Analyst Inertia Note names unvalidated tier decision per namespace; Decision Authority Cost-of-MOCK field sources from Inertia Note with explicit attribution; Lift condition in REAL-REQUIRED names exact structural change to unblock MOCK", "Score-gated binary verdicts with COVERAGE SCORE TABLE — numeric Score 0-3 per evaluation role precedes binary verdict; COVERAGE SCORE TABLE emitted in Coverage Analyst phase before gate; Failing score in REAL-REQUIRED traces which score caused threshold failure; SCORE-AFTER-VERDICT elevated to gate-level invariant"]}
```
