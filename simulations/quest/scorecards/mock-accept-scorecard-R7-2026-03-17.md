Now I have all five variation specs fully read. Let me score.

---

# Scorecard — mock-accept Round 7 (Rubric v7)

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v7 (C-01–C-30; C-29/C-30 new; denominator 22)
**Baseline:** R6 V-03/V-05 co-goldens (22/22)

---

## Scoring Model

- Essential (C-01–C-05): binary — all must pass. Part of 90-point base.
- Recommended (C-06–C-08): binary — part of 90-point base.
- Aspirational (C-09–C-30): `(passes / 22) × 10`. Max 10 pts.
- **Total = 90 + aspirational score** when all E+R pass.

---

## Criterion-Level Evaluation

### V-01 — Inertia Framing: DDP Placed Before STEP 3

**Structural change:** DDP block moved from preamble to between GATE B and STEP 3. STEP 1 and STEP 2 execute without a declared default position. All other elements from R6 V-05 baseline carried forward.

**Key observation:** DDP block appears after GATE B, immediately before `STEP 3 — ARCHITECT EVALUATION`. STEP 3 and STEP 4 both carry full `Cost-of-MOCK:` fields with CONSTRAINT and HALT.

| Tier | ID | Criterion | V-01 | Evidence |
|------|----|-----------|------|----------|
| Essential | C-01 | Artifact-as-subject form | PASS | Standing Rule at top with positive + forbidden forms |
| Essential | C-02 | Forbidden triad complete | PASS | Rule A/B/C all present, three-of-three enforced |
| Essential | C-03 | CANARY ASSERTION + SUPPRESSED branch | PASS | STEP 5 has both CANARY fields |
| Essential | C-04 | Single Write block for review | PASS | STEP 8 enforces one Write call |
| Essential | C-05 | Slot 1/Slot 2 separation, paraphrase named | PASS | STEP 6 has distinct Slot 1 and Slot 2 headers |
| Recommended | C-06 | Entity-naming in roles | PASS | STEP 3/4 each have Required artifact citation with verbatim form + CONSTRAINT |
| Recommended | C-07 | Accumulator lists + empty-list rule | PASS | Arch-blocked/Strategy-blocked with VERDICT-ECHO; "none" form required |
| Recommended | C-08 | 5-field eval template | PASS | Trigger/SQ/Artifact state/Verdict/Required action + VERDICT-ECHO |
| Aspirational | C-09 | Artifact-as-subject standing rule | PASS | Standing Rule at top with PASS/FAIL examples |
| Aspirational | C-10 | Tier sourcing | PASS | STEP 1 CONSTRAINT: "Tier: N (source: TOPICS.md | --tier | default)" |
| Aspirational | C-11 | Inline completeness gate | PASS | GATE A count assertion: "N + M = ___. Expected: 9." |
| Aspirational | C-12 | Reason-code at point of use | PASS | CONSTRAINT at each Reason field in STEP 3/4/6 |
| Aspirational | C-13 | Phase exit assertions | PASS | GATE A/B/C/D/E/F each have "Do not proceed" language |
| Aspirational | C-14 | Blank-line failure signal | PASS | `___` slots throughout; bracket notation absent |
| Aspirational | C-15 | Forbidden-form enumeration | PASS | Standing Rule lists "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…" |
| Aspirational | C-16 | Written-gate blocking language | PASS | All gates: "Do not proceed to STEP N until written" |
| Aspirational | C-17 | Named gate registry | PASS | GATE A, B, C, D, E, F — stable IDs |
| Aspirational | C-18 | Adjacent framed CONSTRAINT | PASS | Each CONSTRAINT block is a standalone framed line adjacent to its target |
| Aspirational | C-19 | Universal blank-slot enforcement | PASS | `___` in auto-flag rule outputs and CANARY ASSERTION |
| Aspirational | C-20 | Halt-on-violation instruction | PASS | Standing Rule: "HALT. Delete the violating line. Rewrite in PASS form." |
| Aspirational | C-21 | Per-section CONSTRAINT in Write block | PASS | STEP 8 has per-section CONSTRAINT at Coverage/Structural records/Risk/Next Steps |
| Aspirational | C-22 | Slot 1 paraphrase examples in revert | PASS | "sufficient coverage" and "domain realistic" quoted |
| Aspirational | C-23 | Three-step halt sequence | PASS | "HALT. Delete the violating line. Rewrite in PASS form." — three imperatives |
| Aspirational | C-24 | Gate-to-section traceability in GATE F | PASS | STEP 9 GATE F names all four sections explicitly |
| Aspirational | C-25 | Slot 2 paraphrase examples in revert | PASS | SLOT 2 VIOLATION TABLE with three quoted near-miss forms |
| Aspirational | C-26 | Halt co-location at each CONSTRAINT site | PASS | Every CONSTRAINT block followed by HALT throughout all steps |
| Aspirational | C-27 | GATE F as standalone dedicated step | PASS | STEP 9 is solely the GATE F completeness check |
| Aspirational | C-28 | Slot 2 violation table | PASS | Two-column table: Quoted near-miss form / Violation type |
| Aspirational | C-29 | Cost-of-MOCK in evaluation record | **PASS** | STEP 3 and STEP 4 both have `Cost-of-MOCK:` field with constrained "Without real data for..." format |
| Aspirational | C-30 | DEFAULT DECISION POSITION block | **PASS** | DDP block placed after GATE B, before STEP 3 header — satisfies "structurally present before the evaluation phase (STEP 3, STEP 4)" |

**Aspirational passes: 22/22**
**Aspirational score: (22/22) × 10 = 10.0**
**Total: 90 + 10.0 = 100.0**

> C-30 diagnostic confirmed: the minimum positional requirement is *before the evaluation phase* (before STEP 3), not before the entire spec. Mid-spec DDP satisfies. STEP 1/STEP 2 running without a declared default is operationally acceptable.

---

### V-02 — Lifecycle Emphasis: Cost-of-MOCK Relocated to STEP 6 Slot 3

**Structural change:** `Cost-of-MOCK:` field removed from STEP 3 and STEP 4 evaluation records entirely. Added as `--- Slot 3 — Cost-of-MOCK ---` in STEP 6 (MOCK-ACCEPTED POSITIVE ARGUMENT). DDP at preamble before STEP 1 (full-spec position, same as R6 V-05 baseline).

| Tier | ID | Criterion | V-02 | Evidence |
|------|----|-----------|------|----------|
| Essential | C-01–C-05 | All essential | PASS | Unchanged from baseline; DDP at preamble; Slot 1/Slot 2/Slot 3 each separately labeled |
| Recommended | C-06–C-08 | All recommended | PASS | STEP 3/4 eval template retains 5 core fields; accumulator lists present |
| Aspirational | C-09–C-28 | Unchanged criteria | PASS | No modifications to Standing Rule, gate structure, tokens, tables, or GATE F |
| Aspirational | C-29 | Cost-of-MOCK in evaluation record | **FAIL** | STEP 3 and STEP 4 have no `Cost-of-MOCK:` field. Evaluation record is two-part (Reason + Required action) only. MA-27: verdict collapses to two-part form without naming counterfactual validation risk in the evaluation record. Moving Cost-of-MOCK to STEP 6 Slot 3 places it in the documentation phase — structurally distinct from the verdict formation phase. |
| Aspirational | C-30 | DEFAULT DECISION POSITION block | PASS | DDP at preamble before STEP 1 — full-spec anchor satisfies both positional clauses |

**Aspirational passes: 21/22 (C-29 FAIL)**
**Aspirational score: (21/22) × 10 = 9.545**
**Total: 90 + 9.55 = 99.55**

> **Prediction discrepancy noted:** Variate document states "21/22, 99.09" — these are mathematically inconsistent. 21/22 × 10 = 9.545 → total 99.55, not 99.09. 99.09 requires 20/22 (two failures). Full spec review identifies only C-29 as failing. Scoring as 21/22, 99.55. The "99.09" appears to be a transcription error — the R6 V-04 score (99.09 from 20/22) was erroneously carried into the R7 V-02 prediction.

> **C-29 diagnostic confirmed:** Cost-of-MOCK in STEP 6 Slot 3 does not satisfy C-29. The criterion requires the field to appear inside the evaluation record at the moment of verdict formation (STEP 3/4). STEP 6 is the positive argument documentation phase — a cost statement there is C-05 territory, not C-29.

---

### V-03 — Inertia Framing: INERTIA LEDGER at Phase Gates

**Structural change:** DDP at preamble (unchanged). STEP 3 and STEP 4 retain Cost-of-MOCK fields. New **INERTIA LEDGER** block added within GATE C and GATE D:

```
INERTIA LEDGER — ARCHITECT PHASE EXIT
Namespaces still at REAL-REQUIRED default: ___
Namespaces that have earned MOCK-ACCEPTED against inertia: ___
CONSTRAINT: Sum must equal non-auto-flagged count from GATE B.
HALT. If sum does not equal non-auto-flagged count, recount before advancing.
```

Same structure at GATE D (Strategy phase exit).

| Tier | ID | Criterion | V-03 | Evidence |
|------|----|-----------|------|----------|
| Essential | C-01–C-05 | All essential | PASS | Unchanged; DDP at preamble; INERTIA LEDGER is additive content, not structural rewrite |
| Recommended | C-06–C-08 | All recommended | PASS | Eval templates unchanged |
| Aspirational | C-09–C-28 | Unchanged criteria | PASS | All baseline criteria satisfied; INERTIA LEDGER adds to GATE C/D but doesn't modify any criterion-governed surface |
| Aspirational | C-29 | Cost-of-MOCK in evaluation record | PASS | STEP 3 and STEP 4 each have `Cost-of-MOCK:` field with constrained format |
| Aspirational | C-30 | DEFAULT DECISION POSITION block | PASS | DDP at preamble before STEP 1 |
| — | C-31 | **INERTIA LEDGER (new candidate)** | **SIGNAL** | Per-gate running tally: "Namespaces still at REAL-REQUIRED default" vs "earned MOCK-ACCEPTED against inertia." Structurally distinct from C-29 (per-namespace eval record cost) and C-30 (initial state declaration). Verifiable count assertion at phase boundaries. |

**Aspirational passes: 22/22**
**Aspirational score: (22/22) × 10 = 10.0**
**Total: 90 + 10.0 = 100.0**
**Excellence signal: C-31 candidate detected**

---

### V-04 — Combined: DDP Mid-Spec + INERTIA LEDGER

**Structural change:** DDP block placed between GATE B and STEP 3 (V-01 axis). INERTIA LEDGER at GATE C and GATE D (V-03 axis). Cost-of-MOCK retained inline in STEP 3/STEP 4 (C-29 unchanged).

| Tier | ID | Criterion | V-04 | Evidence |
|------|----|-----------|------|----------|
| Essential | C-01–C-05 | All essential | PASS | STANDING RULE at top governs; DDP after GATE B |
| Recommended | C-06–C-08 | All recommended | PASS | Templates unchanged |
| Aspirational | C-09–C-28 | Unchanged criteria | PASS | All baseline criteria satisfied |
| Aspirational | C-29 | Cost-of-MOCK in evaluation record | PASS | STEP 3 and STEP 4 retain full `Cost-of-MOCK:` fields ("C-29 inline kept" — confirmed in spec) |
| Aspirational | C-30 | DEFAULT DECISION POSITION block | PASS | DDP placed before STEP 3 (after GATE B) — satisfies evaluation-phase-relative positional requirement |
| — | C-31 | INERTIA LEDGER | **SIGNAL** | GATE C and GATE D both carry INERTIA LEDGER with constrained sum assertion |

**Aspirational passes: 22/22**
**Aspirational score: (22/22) × 10 = 10.0**
**Total: 90 + 10.0 = 100.0**
**Excellence signal: C-31 candidate**

> **Interaction note:** Mid-spec DDP (after STEP 1/2) combined with per-gate INERTIA LEDGER does not create conflicting inertia-framing signals. The INERTIA LEDGER at GATE C operationalizes the default declared just before STEP 3 — they are sequential and consistent. No degradation of STEP 2 auto-flag form (Standing Rule governs STEP 1/2 without DDP, but the rule is sufficient to maintain artifact-as-subject form).

---

### V-05 — Full Integration: R6 V-05 + INERTIA LEDGER + MOCK COST REGISTER

**Structural change:** DDP at preamble (R6 V-05 full-spec position). INERTIA LEDGER at GATE C and GATE D. New **STEP 5 — MOCK COST REGISTER** inserted between GATE D and STATUS WRITEBACK. Original STEP 5–9 renumbered STEP 6–10.

STEP 5 structure:
```
STEP 5 — MOCK COST REGISTER
For each MOCK-ACCEPTED namespace (from GATE C and GATE D combined):
  Namespace / Phase (Architect | Strategy) / Cost-of-MOCK (verbatim copy)
COST REGISTER ASSERTION: Count entries. Expected: total MOCK-ACCEPTED.
GATE E-COST — COST REGISTER COMPLETE
```

| Tier | ID | Criterion | V-05 | Evidence |
|------|----|-----------|------|----------|
| Essential | C-01–C-05 | All essential | PASS | DDP at preamble; STANDING RULE active; Slot 1/Slot 2 in STEP 7; STEP 9 is single Write call |
| Recommended | C-06–C-08 | All recommended | PASS | STEP 3/4 templates unchanged; accumulator lists present |
| Aspirational | C-09–C-28 | Unchanged criteria | PASS | All 20 baseline aspirational criteria satisfied |
| Aspirational | C-29 | Cost-of-MOCK in evaluation record | PASS | STEP 3 and STEP 4 retain `Cost-of-MOCK:` fields; STEP 5 aggregates but does not replace them |
| Aspirational | C-30 | DEFAULT DECISION POSITION block | PASS | DDP at preamble before STEP 1 |
| Aspirational | C-27 | GATE F as standalone dedicated step | PASS | STEP 10 is solely the GATE F completeness check; renumbering does not break standalone status |
| — | C-31 | INERTIA LEDGER | **SIGNAL** | GATE C and GATE D carry per-phase running tally |
| — | C-32 | MOCK COST REGISTER | **SIGNAL** | STEP 5 is a dedicated aggregation step: collects all Cost-of-MOCK entries by namespace+phase, asserts count equals total MOCK-ACCEPTED, fires GATE E-COST. Transforms inline cost tracking into independently verifiable post-evaluation ledger. Not reducible to C-29 (inline per-namespace) or C-31 (per-phase inertia state). |

**Aspirational passes: 22/22**
**Aspirational score: (22/22) × 10 = 10.0**
**Total: 90 + 10.0 = 100.0**
**Excellence signals: C-31 + C-32 candidates**

> **Length-pressure risk observed:** V-05 is 10 steps vs 9 for V-01/V-03/V-04. HALT co-location (C-26) is the most repetitive surface across STEP 3/4 at 9 namespaces × 6+ CONSTRAINT/HALT pairs each = 108+ HALT instructions. Dropout risk is real at full namespace count. Not a criterion failure in the spec itself — but a production reliability flag for R8.

---

## Composite Scores

| Variation | Asp passes | Asp score | Total | New signals |
|-----------|-----------|-----------|-------|-------------|
| V-01 | 22/22 | 10.0 | **100.0** | C-30 positional boundary |
| V-02 | 21/22 | 9.55 | **99.55** | (diagnostic) |
| V-03 | 22/22 | 10.0 | **100.0** | C-31 |
| V-04 | 22/22 | 10.0 | **100.0** | C-31 |
| V-05 | 22/22 | 10.0 | **100.0** | C-31 + C-32 |

---

## Ranking

| Rank | Variation | Score | Rationale |
|------|-----------|-------|-----------|
| 1 | **V-05** | 100.0 | Two new criterion candidates; richest structure; INERTIA LEDGER + MOCK COST REGISTER both independently motivated |
| 2 | **V-03** | 100.0 | INERTIA LEDGER at baseline DDP position — cleanest single-axis C-31 signal, lowest interaction risk |
| 3 | **V-04** | 100.0 | C-31 signal + mid-spec DDP test; combination shows no degradation under DDP reposition + ledger |
| 4 | **V-01** | 100.0 | Confirms C-30 positional freedom; enables future specs to place DDP after auto-flag phase |
| 5 | **V-02** | 99.55 | Diagnostic value only: confirms C-29 evaluation-record binding |

---

## Excellence Signals

### From V-03 / V-04 / V-05 — C-31 Candidate: INERTIA LEDGER

**Pattern:** Within GATE C and GATE D, a named `INERTIA LEDGER — [PHASE] PHASE EXIT` block records:
- "Namespaces still at REAL-REQUIRED default: ___"
- "Namespaces that have earned MOCK-ACCEPTED against inertia: ___"
- Constrained sum assertion tied to gate count

**Why it's new:** C-30 declares initial state (every namespace starts REAL-REQUIRED). C-29 names the per-namespace cost inside the evaluation record. The INERTIA LEDGER is the third structural form: a *running phase-exit tally* that makes the progress of earned escapes observable at gate boundaries. The inertia framing is active throughout all three forms — but each addresses a different epistemic moment (before/during/after).

**C-31 independence test:** Not reducible to C-29 (no per-namespace cost statement) or C-30 (not an initial state declaration — it fires at gate exit, not spec preamble). The sum constraint is novel.

---

### From V-05 only — C-32 Candidate: MOCK COST REGISTER

**Pattern:** Dedicated STEP 5 inserted after GATE D, before STATUS WRITEBACK:
- Enumerates all MOCK-ACCEPTED namespaces (both Architect and Strategy phases)
- Copies `Cost-of-MOCK` entry verbatim from evaluation record
- Fires `COST REGISTER ASSERTION` with count ("Expected: N = total MOCK-ACCEPTED")
- Standalone gate: `GATE E-COST — COST REGISTER COMPLETE`

**Why it's new:** C-29 ensures the cost statement exists inline in each evaluation record. The MOCK COST REGISTER makes all costs aggregated, enumerable, and independently verifiable as a named step output — before writeback changes the state of the artifact. It creates a pre-writeback audit surface that C-29 alone cannot provide (inline costs are distributed across up to 9 evaluation records; the register consolidates them). Not reducible to C-29 (aggregation vs. inline), C-30 (initial state), or C-31 (phase inertia tally).

---

## Hypothesis Outcomes

| Hypothesis | Outcome | Evidence |
|------------|---------|----------|
| C-30 position: "before STEP 3" sufficient? | **CONFIRMED** (V-01) | DDP placed after GATE B passes C-30 |
| C-29 independence: STEP 6 substitution fails? | **CONFIRMED** (V-02) | Moving to STEP 6 Slot 3 → C-29 FAIL |
| INERTIA LEDGER is structurally distinct from C-29/C-30? | **CONFIRMED** (V-03) | Three-way structural independence established |
| Mid-spec DDP + LEDGER combination stable? | **CONFIRMED** (V-04) | No degradation; Standing Rule governs STEP 1/2 without DDP anchor |
| MOCK COST REGISTER is structurally distinct from C-29/C-31? | **CONFIRMED** (V-05) | Aggregation step with count assertion is novel surface |

---

## Variate Prediction Accuracy

| Variation | Predicted | Actual | Match |
|-----------|-----------|--------|-------|
| V-01 | 22/22, 100.0 | 22/22, 100.0 | Exact |
| V-02 | "21/22, 99.09" | 21/22, **99.55** | C-29 FAIL confirmed; score prediction error (99.09 = 20/22 math; actual is 21/22 = 99.55) |
| V-03 | 22/22, 100.0 | 22/22, 100.0 | Exact |
| V-04 | 22/22, 100.0 | 22/22, 100.0 | Exact |
| V-05 | 22/22, 100.0 | 22/22, 100.0 | Exact |

**V-02 prediction has an arithmetic inconsistency.** "21/22" and "99.09" are incompatible: 21/22 × 10 = 9.545 → total 99.55. The 99.09 value (= 20/22) was likely transcribed from the R6 V-04 score. Correction: V-02 = 21/22, 99.55.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["INERTIA LEDGER at phase gates: per-gate running tally of namespaces still at REAL-REQUIRED default vs. earned MOCK-ACCEPTED against inertia, with constrained sum assertion at GATE C and GATE D exit — C-31 candidate structurally distinct from C-29 (per-namespace cost) and C-30 (initial state declaration)", "MOCK COST REGISTER as dedicated post-evaluation step: aggregates all Cost-of-MOCK entries by namespace and phase into a named registry with COST REGISTER ASSERTION count check and standalone GATE E-COST before writeback — C-32 candidate structurally distinct from C-29 (inline), C-30 (initial state), and C-31 (phase tally)"]}
```
