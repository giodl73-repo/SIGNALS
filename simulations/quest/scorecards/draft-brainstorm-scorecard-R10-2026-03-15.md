## draft-brainstorm — R10 Scorecard (Rubric v10)

---

### Scoring Baseline

All C-01 through C-28 pass in every variation (inherited from R9 bases). C-01..C-28 = 145 pts. The R10 scoring action falls entirely on R9 tier (C-29+C-30, 5 pts max) and R10 tier (C-31+C-32, 5 pts max).

---

### V-01 — Phrasing Register: Conversational (C-31 isolated FAIL)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-28 | PASS (inh) | All inherited from R9-V-01 base |
| C-29 | **PASS** | Dual-anchor satisfied: (a) Selected? column rule — "Once both gate conditions from Check B hold, you may proceed to Phase 3"; (b) Phase 3 opens — "Once both gate conditions from Check B hold, proceed here." Label-reference at phase entry, but anchor (b) is present. |
| C-30 | **PASS** | "if editing the candidate's rationale would make the comparison sentence completable, that desire confirms the replacement obligation applies" — causal mechanism (comparison-sentence incompletability) named explicitly. |
| C-31 | **FAIL** | Phase 3 entry "Once both gate conditions from Check B hold" — label-reference only. Selected? column name not written, "5 rows" not stated at transition point. Verbatim condition text absent. |
| C-32 | **PASS** | "the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" — negation frame ("not permission to reopen") and affirmation frame ("the signal the swap is mandatory") both present alongside C-30 causal trigger. |

**Scoring:**

| Tier | Pass/Total | Pts |
|------|-----------|-----|
| C-01..C-28 | 28/28 | 145.0 |
| R9 (C-29+C-30) | 2/2 | 5.0 |
| R10 (C-31+C-32) | 1/2 | 2.5 |
| **Total** | | **152.5** |

**Discrepancy note:** The variation expected 150, implicitly treating C-29 as FAIL (inherited). However, the R10-V-01 prompt adds "Once both gate conditions from Check B hold, proceed here." at Phase 3 entry — this is an anchor (b) per C-29's pass condition. C-29 transitions from FAIL (R9-V-01 had no phase-entry restatement) to PASS (R10-V-01 adds even a weak label-reference). The rubric-correct score is **152.5**. The C-29 repair is a side-effect of the design, not fully accounted for in the expected.

---

### V-02 — Lifecycle Emphasis: Dedicated GATE Block (C-32 isolated FAIL)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-28 | PASS (inh) | Inherited from R9-V-02 base |
| C-29 | **PASS** | Dual-anchor: (a) Selected? column rule explicitly names schema property with phase-3 lock; (b) Phase 3 opens with `> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:** (a) All 5 rows... (b) Selected? is blank...` — restatement at phase entry. |
| C-30 | **FAIL** | Prohibition B: "If you want to revise the rationale, treat that impulse as confirmation that the replacement obligation applies" — general revision impulse, not comparison-sentence incompletability as causal mechanism. C-30 requires the specific cause named. |
| C-31 | **PASS** | GATE PRECONDITIONS callout block at Phase 3 entry names verbatim: "(a) All 5 rows of the Peer-Comparison Registry are written in your output" and "(b) Selected? is blank across all 5 rows." Actual schema element names (Selected?, 5 rows) written at transition point. Callout-block format confirmed equivalent to inline prose for C-31. |
| C-32 | **FAIL** | "the desire to revise is not permission to reopen the comparison; it is evidence the swap is mandatory" — dual-frame phrasing present but C-30 prerequisite absent. C-32 requires the dual-frame to close the interpretation gap specifically for the comparison-failure causal mechanism; without C-30's specificity, the frame is misanchored. |

**Scoring:**

| Tier | Pass/Total | Pts |
|------|-----------|-----|
| C-01..C-28 | 28/28 | 145.0 |
| R9 (C-29+C-30) | 1/2 | 2.5 |
| R10 (C-31+C-32) | 1/2 | 2.5 |
| **Total** | | **150.0** |

---

### V-03 — Combination: Callout Gate Block (V-02) + Causal Dual-Frame (V-01)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-28 | PASS (inh) | Inherited from R9-V-03 base |
| C-29 | **PASS** | Dual-anchor: (a) Selected? column rule — "This column cannot hold any value, and Phase 3 cannot begin, until both preconditions hold simultaneously: (a) all 5 rows...AND (b) Selected? is blank across all 5 rows"; (b) Phase 3 GATE block — same conditions at phase entry. Both anchors fully verbatim. |
| C-30 | **PASS** | "If editing the candidate's rationale would make the comparison sentence completable, that desire confirms the replacement obligation applies" — comparison-sentence incompletability named as causal mechanism. |
| C-31 | **PASS** | GATE PRECONDITIONS callout block at Phase 3 entry: "(a) All 5 rows of the Peer-Comparison Registry are written in your output" + "(b) Selected? is blank across all 5 rows." Schema element names (Selected?, 5 rows) written verbatim at transition. Format-independent: callout block satisfies C-31 equivalently to prose restatement. |
| C-32 | **PASS** | "the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" — negation + affirmation both present alongside C-30 causal trigger. No interpretive gap remains. |

**Scoring:**

| Tier | Pass/Total | Pts |
|------|-----------|-----|
| C-01..C-28 | 28/28 | 145.0 |
| R9 (C-29+C-30) | 2/2 | 5.0 |
| R10 (C-31+C-32) | 2/2 | 5.0 |
| **Total** | | **155.0** |

---

### V-04 — Output Format: Numbered Steps + Verbatim GATE at Step 8 + Dual-Frame

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-28 | PASS (inh) | Inherited from R9-V-04 base |
| C-29 | **PASS** | Dual-anchor: (a) Step 5 Selected? column rule — "This column cannot hold any value until both preconditions hold: (a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows. Step 8 may begin only when both conditions are satisfied."; (b) Step 8 GATE block — same conditions verbatim at step entry. |
| C-30 | **PASS** | Rationalization Rule: "If editing the candidate's rationale would make the comparison sentence completable, that desire confirms the replacement obligation applies" — causal mechanism named. |
| C-31 | **PASS** | Step 8 GATE block: "(a) All 5 rows of the Peer-Comparison Registry (Step 5) are written in your output" + "(b) Selected? is blank across all 5 rows of that Registry." Verbatim schema elements (Selected?, 5 rows) at step entry. Numbered-step architecture confirmed as valid full-stack carrier for C-31. |
| C-32 | **PASS** | "the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" — negation + affirmation alongside causal trigger. Complete dual-frame. |

**Scoring:**

| Tier | Pass/Total | Pts |
|------|-----------|-----|
| C-01..C-28 | 28/28 | 145.0 |
| R9 (C-29+C-30) | 2/2 | 5.0 |
| R10 (C-31+C-32) | 2/2 | 5.0 |
| **Total** | | **155.0** |

---

### V-05 — Inertia Framing Prominence: Phase 0 + C-31 Verbatim + C-32 Dual-Frame

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-28 | PASS (inh) | Inherited from R9-V-03 base; pool-order reorganization does not affect any passing criterion |
| C-14 | **PASS (stronger form)** | Phase 0 ("STATUS QUO") is a dedicated pre-generation phase — framing paragraph and Do Nothing entry required before Phase 1 (GENERATE) may begin. Stronger than 1a placement (within generation phase): the inertia anchor is structurally prior to all alternatives, not merely first within the pool. |
| C-29 | **PASS** | Dual-anchor: (a) Selected? column rule — "This column cannot hold any value, and Phase 3 cannot begin, until both preconditions hold simultaneously: (a) all 5 rows...AND (b) Selected? is blank across all 5 rows"; (b) Phase 3 entry — "Only after both preconditions hold -- (a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows -- may Phase 3 begin." |
| C-30 | **PASS** | "If editing the candidate's rationale would make the comparison sentence completable, that desire confirms the replacement obligation applies" — causal mechanism (comparison-sentence incompletability) named. |
| C-31 | **PASS** | Phase 3 entry writes verbatim: "(a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows." Schema element names written out at transition point. Structurally identical to R9-V-03 which was the first 155. |
| C-32 | **PASS** | "the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" — negation + affirmation alongside C-30 causal trigger. |

**Scoring:**

| Tier | Pass/Total | Pts |
|------|-----------|-----|
| C-01..C-28 | 28/28 | 145.0 |
| R9 (C-29+C-30) | 2/2 | 5.0 |
| R10 (C-31+C-32) | 2/2 | 5.0 |
| **Total** | | **155.0** |

---

### Composite Ranking

| Rank | Variation | C-29 | C-30 | C-31 | C-32 | Score |
|------|-----------|------|------|------|------|-------|
| 1 (tie) | V-03 | PASS | PASS | PASS | PASS | **155.0** |
| 1 (tie) | V-04 | PASS | PASS | PASS | PASS | **155.0** |
| 1 (tie) | V-05 | PASS | PASS | PASS | PASS | **155.0** |
| 4 | V-01 | PASS | PASS | FAIL | PASS | **152.5** *(expected: 150)* |
| 5 | V-02 | PASS | FAIL | PASS | FAIL | **150.0** |

All essential criteria (C-01 through C-05) pass in all five variations.

---

### Excellence Signals from Top-Scoring Variations (V-03 / V-04 / V-05)

**What made 155 reproducible across three structurally different architectures:**

1. **Callout-block is a format-stable C-31 carrier.** V-03's `> **GATE PRECONDITIONS**` callout block satisfies C-31 equivalently to V-04/V-05's inline prose restatement. The criterion is purely about whether verbatim schema element names (Selected?, 5 rows, blank) appear at the phase entry — not about what syntactic form delivers them. Any visually distinct block or prose restatement with the named elements passes.

2. **Phase 0 is a structural-first C-14 form.** V-05 elevates inertia to a dedicated phase before GENERATE — stronger than 1a placement within the generation phase. "Phase 0 must complete before Phase 1 may begin" is an architectural sequencing constraint, making inertia-first a property of the prompt's state machine, not just the output order. This is a distinct and higher form of C-14 compliance.

3. **Dual-frame (C-32) is architecture-independent.** V-03 (Phase/Check), V-04 (numbered steps), and V-05 (Phase 0/1/2/3) all carry the identical Prohibition B clause and all pass C-32. The criterion is purely about whether "not permission to reopen" + "the signal the swap is mandatory" appear alongside the C-30 causal trigger — not about which heading or step-label contains them.

**Unexpected finding from V-01 (152.5 not 150):**

The label-reference addition ("Once both gate conditions from Check B hold, proceed here.") designed to demonstrate C-31 FAIL unexpectedly repaired C-29: a minimal label-reference at phase entry is sufficient for C-29's anchor (b). The R9-V-01 C-29 FAIL was due to complete absence of any phase-entry restatement. Even a label-reference passes C-29. This creates a 2.5-pt score gap the variation authors did not anticipate — confirming that C-29 and C-31 are independently assessable: label-reference → C-29 PASS, C-31 FAIL; verbatim → C-29 PASS, C-31 PASS.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["Label-reference at phase entry satisfies C-29 weak dual-anchor independently of C-31, creating an unexpected 152.5 score for V-01 (vs expected 150) — C-29 and C-31 decouple cleanly: any restatement at phase entry passes C-29, only verbatim schema names pass C-31", "Dedicated GATE PRECONDITIONS callout block is a format-stable alternative to inline prose restatement for C-31 — the criterion is property-based (schema element names present at transition) not form-based"]}
```
