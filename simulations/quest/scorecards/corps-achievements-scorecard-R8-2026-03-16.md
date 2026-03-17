Now I have all five variations. Let me score them.

---

# corps-achievements — R8 Scorecard

**Rubric version**: 7 | **Date**: 2026-03-16 | **New criteria**: C-24, C-25, C-26 (aspirational pool: 18)

---

## Scoring Formula

```
score = (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/18 × 20)
PARTIAL = 0.5 weight
```

---

## Per-Criterion Evidence

### ESSENTIAL (5) — all variations

All five variations carry the full R7 baseline. Essential checks are present in each.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variations.**

---

### RECOMMENDED (3) — all variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 | PASS — `## Earned Achievements` / `## Locked Achievements` explicit separation | PASS | PASS | PASS | PASS |
| C-07 | PASS — two labeled category sections | PASS | PASS | PASS | PASS |
| C-08 | PASS — `date: {{date}}` in frontmatter, Step 8 writes artifact | PASS | PASS | PASS | PASS |

**Recommended: 3/3 all variations.**

---

### ASPIRATIONAL (18) — R7 baseline C-09–C-23

All variations carry the R7 baseline at 100%. The following applies uniformly to C-09 through C-23 across all five variations:

| ID | All Variations | Evidence |
|----|---------------|----------|
| C-09 | PASS | `## Almost There — 1-Away Gaps` section with dedicated table |
| C-10 | PASS | Step 7 / Phase 3B requires specific values and topic/contributor names |
| C-11 | PASS | Pre-write gates before achievements section and leaderboard |
| C-12 | PASS | `→ Unlocks [Achievement] → Breaks [PATTERN]` format enforced |
| C-13 | PASS | `**TEAM INSIGHT — [descriptive name]:**` format required |
| C-14 | PASS | Registry label syntax enforced; ACTIONS GATE sub-step (3)/(4) explicitly checks no invented labels |
| C-15 | PASS | All failure messages name the specific instance that triggered them |
| C-16 | PASS | Formula `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)` defined and used |
| C-17 | PASS | Labels SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL, ORPHAN_TOPIC — all semantic |
| C-18 | PASS | 1-AWAY table has four explicit columns: topic/milestone, achievement, gap, exact action |
| C-19 | PASS | FORMULA CORRECTION GATE sub-step (1) renders worked example for Rank 1 |
| C-20 | PASS | All gate labels carry criterion ID references in bracket notation |
| C-21 | PASS | FORMULA CORRECTION GATE sub-step (3) instructs correction when mismatch found |
| C-22 | PASS | INSIGHT GATE sub-step (3) requires derivability elimination; Step B runs per-topic YES/NO test |
| C-23 | PASS | All gates use numbered sub-step format `(1) ... (2) ... (3) ...` |

**Baseline aspirational: 15/15 all variations.**

---

### ASPIRATIONAL — R8 New Criteria: C-24, C-25, C-26

#### C-24: Cross-phase gate threading

**C-24 requires**: At least one later-phase gate explicitly asks whether prior-phase findings alter the current phase's output.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **FAIL** | Sequential steps (SETUP + STEP 1–8), no named phases. No gate can reference "prior phase findings" — no phase structure exists. |
| V-02 | **FAIL** | Sequential steps. Same as V-01. No phase structure. |
| V-03 | **PASS** | PHASE 1 → PHASE 2 → PHASE 3 structure. Phase 3C `CROSS-PHASE GATE [C-24/C-01/C-02]` sub-step (2): "Did Phase 2's milestone gaps surface any topic names not present in Phase 1's topic list?" — explicit retroactive question. Sub-step (4) instructs correction. Phase 2 STATE record named and structured for interrogation. |
| V-04 | **PASS** | Same three-phase structure as V-03. `CROSS-PHASE GATE [C-24/C-01/C-02]` at Phase 3C is identical in form — same seven sub-steps, Phase 2 STATE record, correction loop. |
| V-05 | **PASS** | Same three-phase structure. `CROSS-PHASE GATE [C-24/C-01/C-02]` at Phase 3C. Phase 2D records `PHASE 2 STATE` explicitly for Phase 3's interrogation. |

---

#### C-25: Multi-criterion gate clustering with enumerated label

**C-25 requires**: When a single gate covers multiple interdependent criteria simultaneously, the gate label enumerates all criterion IDs it covers. A gate label naming only one ID for a multi-criterion check fails.

Key distinction: V-02 and V-05 introduce a **LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — explicitly bundling C-16 (formula-driven scoring) into the gate. V-01/V-03/V-04 have `FORMULA CORRECTION GATE [C-19/C-21]` that covers C-19 and C-21 but leaves C-16 outside any gate check (C-16 is defined in the step body, not verified by a gate condition). This means in V-01/V-03/V-04 the dependency between C-16, C-19, and C-21 is not made explicit via gate clustering — partial satisfaction of the criterion's intent.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **PARTIAL** | ACTIONS GATE [C-05/C-12/C-14/C-20] with sub-step (5) self-verifying enumeration — the four-criterion cluster is explicit. But FORMULA CORRECTION GATE [C-19/C-21] covers only C-19/C-21; C-16 (formula-driven, not raw count) is defined in the step but not in any gate condition. C-16/C-19/C-21 interdependency not gate-visible. |
| V-02 | **PASS** | Two named super-gates: `LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]` — intro prose "This gate covers three interdependent leaderboard criteria simultaneously" with C-16 explicitly in sub-step (1). `ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]` with sub-step (5) self-verifying. Both cluster labels enumerate all member criterion IDs. |
| V-03 | **PARTIAL** | ACTIONS GATE [C-05/C-12/C-14/C-20] sub-step (5) self-verifies enumeration. FORMULA CORRECTION GATE [C-19/C-21] leaves C-16 outside gate coverage. Same gap as V-01. |
| V-04 | **PARTIAL** | ACTIONS GATE [C-05/C-12/C-14/C-20] sub-step (5) self-verifies. FORMULA CORRECTION GATE [C-19/C-21] covers only C-19/C-21. C-16/C-19/C-21 cluster not gate-visible. |
| V-05 | **PASS** | `LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]` with sub-step (6): "This gate label [C-16/C-19/C-21] enumerates all criterion IDs it covers. [C-25]" — intra-gate enumeration self-verification. `ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]` with sub-step (6): "This gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers. [C-25]" — both super-gates self-verify their enumeration from within the gate. |

---

#### C-26: Meta-verification gate for structural compliance

**C-26 requires**: At least one gate condition that verifies whether all other gate labels in the skill carry criterion ID references — making C-20 compliance self-enforcing.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **PASS** | `SETUP — PRE-FLIGHT STRUCTURAL AUDIT [C-20/C-26]` before Step 1. Sub-steps (1)–(4): list every gate label, confirm each carries `[C-XX]`, report violations as findings in frontmatter `preflight_gate_violations: [n]`. Pre-flight audits intent before any output is written. |
| V-02 | **FAIL** | No meta-verification gate anywhere. Gates carry criterion IDs (C-20 satisfied) but no gate audits whether other gates carry IDs. |
| V-03 | **FAIL** | No meta-verification gate. Three-phase structure with no structural audit gate. |
| V-04 | **PASS** | `FINAL — STRUCTURAL AUDIT GATE [C-20/C-26]` after all phases, before artifact write. Sub-steps (1)–(5): scan back through output, list every gate label executed, confirm each carries `[C-XX]`, report count. Post-execution audit verifies what the model actually produced, not just the instruction labels. Violations recorded in frontmatter. |
| V-05 | **PASS** | `3D — STRUCTURAL AUDIT GATE [C-20/C-26]` at Phase 3D. Sub-steps (1)–(6): lists all gate labels, checks criterion IDs, and sub-step (3) specifically names both super-gates: `'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]'` — confirm label enumerates C-16, C-19, C-21; `'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]'` — confirm label enumerates C-05, C-12, C-14, C-20. Targeted by expected enumeration content, not just by presence of any ID. |

---

## Composite Scores

| Variation | Essential (60) | Recommended (20) | Aspirational (20) | **Total** |
|-----------|---------------|-----------------|-------------------|-----------|
| V-01 | 60 | 20 | 16.5/18 × 20 = **18.33** | **98.33** |
| V-02 | 60 | 20 | 16/18 × 20 = **17.78** | **97.78** |
| V-03 | 60 | 20 | 16.5/18 × 20 = **18.33** | **98.33** |
| V-04 | 60 | 20 | 17.5/18 × 20 = **19.44** | **99.44** |
| V-05 | 60 | 20 | 18/18 × 20 = **20.00** | **100.00** |

*Aspirational detail: V-01: C-09–C-23 (15) + C-24 (0) + C-25 (0.5) + C-26 (1) = 16.5. V-02: 15 + 0 + 1 + 0 = 16. V-03: 15 + 1 + 0.5 + 0 = 16.5. V-04: 15 + 1 + 0.5 + 1 = 17.5. V-05: 15 + 1 + 1 + 1 = 18.*

---

## Rankings

| Rank | Variation | Score | Axes Satisfied |
|------|-----------|-------|---------------|
| 1 | **V-05** | **100** | C-24 + C-25 + C-26 |
| 2 | **V-04** | **99** | C-24 + C-26 |
| 3 | **V-01** | **98** | C-26 only |
| 3 | **V-03** | **98** | C-24 only |
| 5 | **V-02** | **98** | C-25 only |

*V-04 beats the single-axis variations because having both C-24 (phases) and C-26 (post-execution audit) outweighs having either plus partial C-25. V-05's full integration adds the complete leaderboard cluster, closing the final C-25 gap.*

---

## Excellence Signals from V-05

Two patterns in V-05 go beyond what C-24/C-25/C-26 codify:

**Signal E-01 — Expected-enumeration audit (named super-gate content check)**

V-05's structural audit gate (3D) sub-step (3) names each super-gate by its full label and specifies which criterion IDs should appear in it:
> `"'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21. 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20."`

V-04's structural audit gate only checks presence (does any ID appear?). V-05's audit checks content-correctness — it can detect wrong-enumeration failures (a label that says `[C-16/C-19]` when `[C-16/C-19/C-21]` is expected) that a presence-only check cannot catch. C-26 as written only requires checking that gates carry criterion ID references; V-05 requires that named super-gates carry the specific expected IDs.

**Signal E-02 — Enumeration verification recorded in pass confirmation**

V-05 super-gate pass messages explicitly name the enumeration verification as a line item:
- LEADERBOARD CLUSTER GATE pass: `"Label enumeration (C-25): [C-16/C-19/C-21] verified."`
- ACTIONS CLUSTER GATE pass: `"Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."`

V-02 has per-criterion confirmation in its pass messages (`"Formula used (C-16): confirmed. Rank-1 example (C-19): {total}. Correction (C-21): [applied/not needed]."`) but does not name enumeration verification as a separate artifact in the pass record. V-05 records WHICH criterion IDs were verified in the label — making the run output an auditable log of C-25 compliance without re-reading the gate body.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Expected-enumeration audit — structural audit gate names each super-gate by label and specifies the exact criterion IDs expected in it, catching wrong-enumeration failures (missing or extraneous IDs) that a generic presence check cannot detect", "Enumeration-in-pass-record — super-gate pass confirmation messages explicitly record which criterion IDs were verified in the label as a named line item, making C-25 compliance auditable from the pass record alone without re-reading the gate body"]}
```
