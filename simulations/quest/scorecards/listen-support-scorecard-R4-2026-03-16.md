Now I have the full R4 golden file. Let me score all five variations against the v4 rubric.

---

## listen-support Quest Scorecard — Round 4

**Rubric:** v4 (C-01–C-18, max 140 pts)
**Date:** 2026-03-16
**Base:** V-05 R3 — C-01 through C-16 at ceiling; C-05 PARTIAL (gate >=6); C-17/C-18 absent

---

### Rubric Reference

| Tier | Criteria | Pts/PASS | Pts/PARTIAL |
|------|----------|----------|-------------|
| Essential ×5 | C-01 to C-05 | 12 | 6 |
| Recommended ×3 | C-06 to C-08 | 10 | 5 |
| Aspirational ×10 | C-09 to C-18 | 5 | 2 |

**Golden gate:** all_essential_pass = TRUE AND composite >= 80

PARTIAL on any Essential = all_essential_pass FALSE (golden blocked regardless of composite).

---

### V-01: Single-Axis — Output Format (Phase-Severity Keyed Lookup Table)

**Axis:** STEP 1 restructured as PHASE-SEVERITY LOOKUP TABLE with explicit KEY DECLARATION.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card template at STEP 7 has `Title: [descriptive subject line]` as a discrete named field |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | STEP 4 VOCABULARY DECLARATION table; VALIDATION TRACE enforces values |
| **C-03 First-person voice throughout** | PASS (12) | STEP 7: "Write as me -- first person throughout. No role titles in body text." |
| **C-04 Gap analysis with three named sections** | PASS (12) | STEP 9 GAP ANALYSIS TABLE requires Doc/Design/Operational rows each with named artifact |
| **C-05 Minimum ticket count enforced** | **PARTIAL (6)** | STEP 3 constraint: "Total >= 6". VALIDATION TRACE: "(required: >= 6)". Gate present but threshold is >=6, not >=7. |
| C-06 Persona diversity | PASS (10) | STEP 6 VALIDATION TRACE requires distinct personas >= 2; STEP 5 voice table covers multiple personas |
| C-07 Phase distribution coverage | PASS (10) | STEP 3 phase distribution target; all three phases required non-zero; STEP 8 confirmation check |
| C-08 Validation trace before body generation | PASS (10) | VALIDATION TRACE block in STEP 6 with Overall: PASS gate before STEP 7 |
| C-09 Phase as named card field | PASS (5) | Card template includes Phase field with controlled values |
| C-10 Persona voice table (3-column) | PASS (5) | STEP 5 has Operational / Frustration / Framing columns |
| C-11 Phase as card field | PASS (5) | Confirmed — Phase field present in card template |
| C-12 Fallback-grounded severity | PASS (5) | STEP 1 Lookup Table has edge-case rules for P0 (activation blocker rationale required) |
| C-13 Mid-output verification block | PASS (5) | STEP 8 POST-GENERATION PHASE CONFIRMATION block |
| C-14 Phase+Title coexistence | PASS (5) | Card template carries both Phase and Title as discrete named fields |
| C-15 Temporal adoption window severity | PASS (5) | STEP 1 Lookup Table has Window column (Day 0-30, Day 31-60, Day 61-90) binding severity ranges |
| C-16 Prior-tool coverage in verification | PASS (5) | STEP 2 STATUS QUO ANCHOR maps prior tools; VALIDATION TRACE checks "Phase-severity consistent with STEP 1 Lookup Table" |
| **C-17 Phase-as-severity-key declaration** | **PASS (5)** | KEY DECLARATION block in STEP 1 header: "Phase is the lookup key for severity assignment. No override path exists." Both required phrases present as explicit structural constraints. |
| **C-18 Gate minimum correct at >=7** | **FAIL (0)** | STEP 3 constraint says Total >= 6. No TABLE CHECK block. VALIDATION TRACE says "(required: >= 6)". Gate threshold is wrong. |

**V-01 Composite:** 12+12+12+12+6 + 10+10+10 + 5+5+5+5+5+5+5+5 + 5+0 = **129/140**
**all_essential_pass:** FALSE (C-05 PARTIAL)
**Golden:** BLOCKED

---

### V-02: Single-Axis — Lifecycle Emphasis (Phase-as-Key Embedded in Card Template)

**Axis:** STEP 1 retains prose gradient prior; Phase-as-key embedded in card template field definition.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card template has Title field as discrete line |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | STEP 4 vocabulary table; STEP 6 validation trace enforces values |
| **C-03 First-person voice throughout** | PASS (12) | STEP 7: "Write as me -- first person throughout." |
| **C-04 Gap analysis with three named sections** | PASS (12) | STEP 9 requires Doc/Design/Operational rows each with named artifact |
| **C-05 Minimum ticket count enforced** | **PARTIAL (6)** | STEP 3: "Total >= 6". VALIDATION TRACE: "(required: >= 6)". Gate present at wrong threshold. |
| C-06 through C-16 | PASS (75) | All R3 base mechanisms preserved (persona diversity, phase distribution, validation gate, voice table, temporal window, prior-tool coverage) |
| **C-17 Phase-as-severity-key declaration** | **PASS (5)** | Card template at STEP 7: `Phase: [Phase 1 / Phase 2 / Phase 3]   <- lookup key for severity (see STEP 1)` and `Severity: [P0/P1/P2/P3 -- derived from Phase-Severity Gradient Prior, STEP 1 -- no override path]`. Both required phrases present — "lookup key for severity" on the Phase line, "no override path" on the Severity line. Rubric accepts card template definition as satisfying site. |
| **C-18 Gate minimum correct at >=7** | **FAIL (0)** | STEP 3: "Total >= 6". No TABLE CHECK block. VALIDATION TRACE threshold is >=6. |

**V-02 Composite:** 48+6 + 30 + 40 + 5+0 = **129/140**
**all_essential_pass:** FALSE (C-05 PARTIAL)
**Golden:** BLOCKED

---

### V-03: Single-Axis — Phrasing Register (TABLE CHECK Gate at >=7)

**Axis:** TABLE CHECK block appended to STEP 3 enforcing Total >= 7; constraint line corrected throughout.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card template has Title field |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | STEP 4 vocabulary table; validation trace enforces |
| **C-03 First-person voice throughout** | PASS (12) | "Write as me -- first person throughout." |
| **C-04 Gap analysis with three named sections** | PASS (12) | STEP 9 with Doc/Design/Operational sections + GAP CLASSIFICATION COVERAGE block |
| **C-05 Minimum ticket count enforced** | **PASS (12)** | STEP 3 constraint: "Total >= 7". TABLE CHECK block: "Required minimum: 7 / Check: Total >= 7 -> YES / NO / Do not proceed to STEP 4 until this check shows YES." VALIDATION TRACE also says "(required: >= 7)". Full structural gate at correct threshold. |
| C-06 through C-16 | PASS (75) | All R3 base mechanisms preserved unchanged |
| **C-17 Phase-as-severity-key declaration** | **FAIL (0)** | STEP 1 retains prose gradient prior: "PHASE-SEVERITY PRIOR: Phase 1 (Day 0-30): typical P2/P3..." — this is probabilistic guidance, not a structural key declaration. No explicit statement "Phase is the lookup key" or "No override path exists" in STEP 1 or card template. VALIDATION TRACE says "Phase-severity consistent with prior" — references prose prior, not a named key. |
| **C-18 Gate minimum correct at >=7** | **PASS (5)** | TABLE CHECK block present in STEP 3 with halt instruction. Threshold is exactly >=7. |

**V-03 Composite:** 60 + 30 + 40 + 0+5 = **135/140**
**all_essential_pass:** TRUE
**Golden:** PASS (all_essential_pass TRUE, composite 135 >= 80)

---

### V-04: Combined (V-01 + V-03) — Keyed Lookup Table + TABLE CHECK at >=7

**Axes:** PHASE-SEVERITY LOOKUP TABLE with KEY DECLARATION (V-01) + TABLE CHECK gate at >=7 (V-03).

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Present |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | STEP 4 vocabulary table; validation trace |
| **C-03 First-person voice throughout** | PASS (12) | Explicit instruction present |
| **C-04 Gap analysis with three named sections** | PASS (12) | STEP 9 with classification table + GAP CLASSIFICATION COVERAGE |
| **C-05 Minimum ticket count enforced** | **PASS (12)** | STEP 3: "Total >= 7". TABLE CHECK block: halt instruction enforcing >=7. VALIDATION TRACE: "(required: >= 7)". Triple-layer enforcement at correct threshold. |
| C-06 through C-16 | PASS (75) | All R3 mechanisms + STEP 1 lookup table cross-reference in VALIDATION TRACE ("Phase-severity consistent with STEP 1 Lookup Table") |
| **C-17 Phase-as-severity-key declaration** | **PASS (5)** | KEY DECLARATION in STEP 1: "Phase is the lookup key for severity assignment. No override path exists." Both required phrases as explicit structural constraint. VALIDATION TRACE cross-references "STEP 1 Lookup Table" by name. |
| **C-18 Gate minimum correct at >=7** | **PASS (5)** | TABLE CHECK in STEP 3 with halt instruction. Threshold exactly >=7. VALIDATION TRACE checks "(required: >= 7)". |

**V-04 Composite:** 60 + 30 + 40 + 5+5 = **140/140**
**all_essential_pass:** TRUE
**Golden:** PASS — ceiling achieved

---

### V-05: Full Synthesis — All Three Axes + Full R3 Baseline

**Axes:** Lookup table + KEY DECLARATION (V-01) + card template annotation (V-02) + TABLE CHECK >=7 (V-03) + assumption audit step + column-attributed marker citation.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card template has Title field as discrete named line |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | STEP 5 vocabulary table with explicit "No free-form variants" instruction |
| **C-03 First-person voice throughout** | PASS (12) | "Write as me -- first person throughout. No role titles in body text." |
| **C-04 Gap analysis with three named sections** | PASS (12) | STEP 10 unified table with Doc/Design/Operational; "Sections missing named artifact" coverage check |
| **C-05 Minimum ticket count enforced** | **PASS (12)** | STEP 4: "Total >= 7" + TABLE CHECK halt block. VALIDATION TRACE: "(required: >= 7)". Dual-gate: TABLE CHECK is procedural halt before generation; VALIDATION TRACE is post-hoc check. |
| C-06 through C-16 | PASS (75) | All R3 mechanisms present. Column-attributed marker citation (`operational=[term] / frustration=[phrase] / framing=[pattern]`) in card template exceeds C-16 baseline. |
| **C-17 Phase-as-severity-key declaration** | **PASS (5)** | Dual-site: (1) KEY DECLARATION in STEP 1: "Phase is the lookup key for severity assignment. No override path exists." (2) Card template at STEP 8: `Phase: ... <- lookup key for severity (see STEP 1)` and `Severity: ... derived from STEP 1 Phase-Severity Lookup Table -- no override path`. Both sites independently satisfy the criterion. |
| **C-18 Gate minimum correct at >=7** | **PASS (5)** | TABLE CHECK in STEP 4 (procedural halt). VALIDATION TRACE in STEP 7 independently checks "(required: >= 7)". Dual-gate pattern. |

**V-05 Composite:** 60 + 30 + 40 + 5+5 = **140/140**
**all_essential_pass:** TRUE
**Golden:** PASS — ceiling achieved

---

### Round Summary

| Variation | Composite | all_essential_pass | Golden | C-05 | C-17 | C-18 |
|-----------|-----------|-------------------|--------|------|------|------|
| V-01 | 129/140 | FALSE | BLOCKED | PARTIAL | PASS | FAIL |
| V-02 | 129/140 | FALSE | BLOCKED | PARTIAL | PASS | FAIL |
| V-03 | 135/140 | TRUE | PASS | PASS | FAIL | PASS |
| **V-04** | **140/140** | **TRUE** | **PASS** | PASS | PASS | PASS |
| **V-05** | **140/140** | **TRUE** | **PASS** | PASS | PASS | PASS |

---

### Excellence Signals

V-04 and V-05 both achieve the ceiling (140/140). V-05 implements additional structural mechanisms beyond what the current rubric captures:

**Signal 1 — Dual-site Phase-as-key enforcement**

V-05 places the KEY DECLARATION at two independent structural locations: (1) the STEP 1 table header at definition time — "Phase is the lookup key for severity assignment. No override path exists." — and (2) the card template at STEP 8 per-ticket use time — both the Phase line annotated `<- lookup key for severity (see STEP 1)` and the Severity line annotated `derived from STEP 1 Phase-Severity Lookup Table -- no override path`. A model that forgets the STEP 1 declaration encounters the card reminder before writing each Severity field; a model that skips the card annotation still violates the explicitly named STEP 1 constraint. V-04 passes C-17 with single-site only. C-17 does not distinguish single-site from dual-site — V-05's additional enforcement depth is not captured.

**Signal 2 — Assumption audit with post-generation back-reference closure**

V-05 adds STEP 3 as a named analytical step that chains: Incumbent behavior that created assumption → Imported expectation → What this feature does instead → Resulting failure mode → Ticket ID (fill after STEP 8). The "Ticket ID" column creates a forward-reference that closes post-generation: after completing STEP 8, the model returns to STEP 3 and back-fills ticket IDs for each failure mode. This creates a bidirectional traceability loop between pre-generation analysis and generated artifacts — neither direction is achievable by the gap analysis (C-04) or the STATUS QUO ANCHOR (C-15) alone. No existing criterion captures the back-reference closure mechanism.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Dual-site Phase-as-key enforcement — KEY DECLARATION fires at STEP 1 (definition time) and card template annotation fires at STEP 8 (use time); two independent enforcement sites prevent upstream forgetting and per-card drift beyond what single-site C-17 captures", "Assumption-audit back-reference closure — a named analytical step chains incumbent behavior to failure mode with a Ticket ID column left blank until post-generation, then back-filled; creates forward/backward traceability between pre-generation analysis and generated artifacts, distinct from gap analysis or status quo anchor"]}
```
