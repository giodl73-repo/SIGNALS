## Scoring — org-build Variate R18 (Rubric v13, Denominator 30)

---

### V-01 — Lifecycle Emphasis: maximal phase-gate machinery

**Essential (5/5)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | org-chart.md with ASCII box/line hierarchy in output skeleton |
| C-02 | PASS | Phase 3 Sub-step C: all five fields explicitly enumerated in every role file |
| C-03 | PASS | inertia-advocate MUST be present in Phase 3 Sub-step C |
| C-04 | PASS | Phase 3 Sub-step A: standard 20–30 / deep 50+ conditional floor |
| C-05 | PASS | Phase 4 Task: all five columns including Decides and Escalates |

**Recommended (3/3)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | .craft/roles/{area}/ structure, minimum 2 subdirectories |
| C-07 | PASS | 3+ distinct rhythm rows (ROB + shiproom + governance), charter with Quorum as N of M |
| C-08 | PASS | FLAT-CASE-PRESSURE: + single verdict in Phase 4 Task Steps item 7 |

**Aspirational (30/30)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | PASS | Row 1 headcount threshold, Row 2 different category; FORBIDDEN dual headcount |
| C-10 | PASS | "Every 'Why It Applies Here' cell MUST open with [element name] (cat-N) --" |
| C-11 | PASS | IA scope keyed to T2-PRESSURE via VERBATIM-IA-SCOPE-TEMPLATES in constants |
| C-12 | PASS | ANTI-PATTERN-CATEGORY-DERIVATION keyed to T2-VERDICT; structural derivation explicit |
| C-13 | PASS | "Only one verdict. Both is an error." |
| C-14 | PASS | T1-DEPTH-FLAG, T2-PRESSURE/T2-VERDICT, T3-ROLE-OUTCOME/T3-AREA-COUNT named + consumed |
| C-15 | PASS | FORBIDDEN both + FORBIDDEN neither present in Phase 2 and Phase 4 |
| C-16 | PASS | "Every Mitigation cell MUST contain a specific remediation action" + FORBIDDEN format guidance |
| C-17 | PASS | "MUST be copied character-for-character"; FORBIDDEN: paraphrasing/adapting/summarizing |
| C-18 | PASS | ANTI-PATTERN-CATEGORY-DERIVATION table has REQUIRED and FORBIDDEN columns both populated |
| C-19 | PASS | No advisory language in any constraint context; MUST/FORBIDDEN uniformly used |
| C-20 | PASS | All four phase gates emit named typed outputs; all consuming phases declare Input Contracts |
| C-21 | PASS | Every named gate variable bound by MUST/FORBIDDEN in downstream Input Contract |
| C-22 | PASS | OUTPUT SKELETON with {{T2-PRESSURE}}, {{T2-VERDICT}}, {{VERBATIM-IA-SCOPE-TEMPLATES[T2-PRESSURE]}}, {{T3-AREA-1}} |
| C-23 | PASS | "FORBIDDEN: executing Phase N+1 before emitting Phase N record block" at every boundary |
| C-24 | PASS | === RECORD: PHASE-N === blocks with named typed fields after every gate |
| C-25 | PASS | Outbound FORBIDDEN in Constraints + inbound FORBIDDEN in each consuming phase Input Contract |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field unifies declaration + anchor + materialization in one construct |
| C-27 | PASS | Phase 3 Sub-step A: "T1-DEPTH-FLAG = standard → MUST enumerate 20–30; deep → MUST enumerate 50+" inside phase instruction |
| C-28 | PASS | PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins... as first entry inside every record block |
| C-29 | PASS | All prohibitions use FORBIDDEN: keyword; no "do not", "never", "avoid" forms found |
| C-30 | PASS | ### Task Steps and ### Constraints structurally separate in every phase |
| C-31 | PASS | T1-DEPTH-FLAG: [standard\|deep], T2-PRESSURE: [NONE\|LOW\|...], T3-ROLE-OUTCOME: [composite]; count fields use [integer >= N] — bounded and self-documenting |
| C-32 | PASS | ### Input Contract and ### Constraints as separate labeled sections in all consuming phases |
| C-33 | PASS | Input Contract names every upstream variable, source phase, and MUST/FORBIDDEN binding — standalone audit unit |
| C-34 | PASS | ANTI-PATTERN-CATEGORY-DERIVATION table: Verdict | REQUIRED | FORBIDDEN columns side-by-side |
| C-35 | PASS | Phase 2 = Inertia Assessment before Phase 3 = Role Enumeration; verdict is gate output consumed by Phase 3 Input Contract |
| C-36 | PASS | CONSTANTS section before Phase 1 declares both lookup tables; phase instructions reference by name only |
| C-37 | PASS | Phase 2: FORBIDDEN Sub-step B before A (named). Phase 3: FORBIDDEN Sub-step B before A + FORBIDDEN Sub-step C before B (all named both sides) |
| C-38 | PASS | T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET\|DEEP-FLOOR-MET\|FLOOR-MISS]; T1-DEPTH-FLAG absent from Phase 3 record block; note explains composite semantics |

**Score:** 5/5 × 60 + 3/3 × 30 + 30/30 × 10 = **100.0**

---

### V-02 — Role Sequence: inertia-first

**Essential (5/5)** — all PASS (same coverage as V-01)
**Recommended (3/3)** — all PASS

**Aspirational (29/30)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09–C-21 | PASS | All match V-01 coverage |
| C-22 | FAIL | No OUTPUT SKELETON section present; variation ends at Phase 5 verification |
| C-23–C-21 | PASS | — |
| C-25 | PASS | Phase 2 Input Contract: "FORBIDDEN: executing this phase before PHASE-1 record block is emitted" |
| C-26–C-38 | PASS | Same discipline as V-01; C-37 sub-step guards present in Phase 1 (Sub-steps A/B) and Phase 3 (Sub-steps A/B/C); C-38 composite token T3-ROLE-OUTCOME with no residual T2-DEPTH-FLAG in Phase 3 record block |

**Score:** 60 + 30 + (29/30) × 10 = **99.7**

---

### V-03 — Output Format: table-driven constraints

**Essential (5/5)** — all PASS
**Recommended (3/3)** — all PASS

**Aspirational (28/30)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09–C-21 | PASS | Constraint tables surface all required MUST/FORBIDDEN items; C-18/C-34 satisfied by table structure |
| C-22 | FAIL | No OUTPUT SKELETON; variation ends at Phase 5 verification |
| C-23 | PASS | FORBIDDEN: Phase 4/5 start in Constraints table rows |
| C-24 | PASS | === RECORD === blocks present |
| C-25 | FAIL | Input Contract tables use "MUST be present before this phase executes" — not FORBIDDEN. Inbound guard is advisory-strength MUST, not FORBIDDEN. C-25 requires FORBIDDEN at the inbound contract |
| C-26–C-38 | PASS | Record blocks have PHASE-ORDERING-GUARD; C-37 sub-step guards in constraint table rows; C-38 composite token correct |

**Score:** 60 + 30 + (28/30) × 10 = **99.3**

---

### V-04 — Phrasing Register: keyword-first

**Essential (5/5)** — all PASS
**Recommended (3/3)** — all PASS

**Aspirational (29/30)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09–C-21 | PASS | MUST:/FORBIDDEN: as first token on every instruction line; C-19 strongly satisfied |
| C-22 | FAIL | No OUTPUT SKELETON; variation ends at Phase 5 verification |
| C-23 | PASS | "FORBIDDEN: beginning Phase N before emitting Phase N-1 record block" present in every Constraints block |
| C-24 | PASS | === RECORD === blocks present |
| C-25 | PASS | Input Contract explicitly: "FORBIDDEN: executing Phase N before PHASE-N-1 record block is emitted" at every consuming phase |
| C-26–C-38 | PASS | Record blocks structurally unified; C-37 sub-step guards with FORBIDDEN:/named-substep form in Phase 2 and Phase 3; C-38 composite token correct, T1-DEPTH-FLAG only in Phase 1 record block |

**Score:** 60 + 30 + (29/30) × 10 = **99.7**

---

### V-05 — Combination: inertia as organizing principle + full gate machinery

**Essential (5/5)** — all PASS
**Recommended (3/3)** — all PASS

**Aspirational (30/30)**

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09–C-21 | PASS | Full gate machinery plus verdicted-artifacts framing drives C-08/C-11/C-17/C-35 coherence explicitly |
| C-22 | PASS | OUTPUT SKELETON with {{AREA-1}}, {{T2-PRESSURE}}, {{T2-VERDICT}}, {{VERBATIM-IA-SCOPE-TEMPLATES[T2-PRESSURE]}}; all main gate variables have named slots |
| C-23–C-24 | PASS | Per-boundary FORBIDDEN ordering guards; record blocks materialized |
| C-25 | PASS | Inbound FORBIDDEN at every consuming phase Input Contract |
| C-26–C-29 | PASS | Structural unification in record blocks; all prohibitions via FORBIDDEN: |
| C-30–C-34 | PASS | Task/Constraint segmentation; closed-set annotations; Input Contract structurally distinct from Constraints; independently auditable; side-by-side derivation table |
| C-35 | PASS | Phase 2 = Inertia Assessment (PRIMARY GATE); Phase 3 = Role Enumeration (VERDICTED); T2-VERDICT is named gate output consumed by Phase 3 Input Contract |
| C-36 | PASS | CONSTANTS section pre-phase; phase instructions reference by name |
| C-37 | PASS | Phase 2: FORBIDDEN Sub-step B (VERDICT LOCK) before Sub-step A (STRUCTURAL SCAN — T2-PRESSURE recorded). Phase 3: FORBIDDEN Sub-step B (AREA) before Sub-step A (COUNT — includes inertia-advocate); FORBIDDEN Sub-step C (GENERATE) before Sub-step B (AREA — all roles assigned) |
| C-38 | PASS | T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET\|DEEP-FLOOR-MET\|FLOOR-MISS]; semantics note present; T1-DEPTH-FLAG only in Phase 1 record block |

**Score:** 60 + 30 + 30/30 × 10 = **100.0**

---

## Ranking

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| **1** | **V-01** | **100.0** | — |
| **1** | **V-05** | **100.0** | — |
| 3 | V-02 | 99.7 | C-22 (no output skeleton) |
| 3 | V-04 | 99.7 | C-22 (no output skeleton) |
| 5 | V-03 | 99.3 | C-22 + C-25 (MUST not FORBIDDEN at inbound guards) |

---

## Excellence Signals from Top-Scoring Variations

**From V-05 (distinct from V-01):**
The "verdicted artifacts" preamble frame — declaring Phase 2 the PRIMARY GATE in the skill preamble and labeling every downstream output (org-chart, role files, anti-pattern categories, IA scope) as a "verdicted artifact" — propagates verdict-coherence as an architectural identity rather than a per-phase constraint. A reader scanning only phase headers sees "VERDICTED" in Phase 3 and Phase 4 titles and immediately understands the causal chain without reading the inertia assessment phase. This framing simultaneously strengthens C-08, C-11, C-17, and C-35 coherence without adding any constraint text to those phases.

**From V-01 and V-05 (differentiator over V-02/V-03/V-04):**
Output Skeleton with named gate-variable placeholder slots is the structural affordance that converts a phase-gate prompt into a self-documenting contract for the end user. When `{{T2-PRESSURE}}` and `{{T2-VERDICT}}` appear in the skeleton, the user sees exactly where gate variables land in the final artifact without cross-referencing the gate schema — satisfying C-22 as a natural consequence of good prompt design rather than a compliance checkbox.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Verdicted-artifacts preamble: labeling Phase 2 as PRIMARY GATE and all downstream outputs as verdicted artifacts in the skill preamble propagates verdict-coherence as architectural identity — phase headers read VERDICTED and readers reconstruct the causal chain without reading the inertia phase", "Output Skeleton as gate-variable landing map: named placeholder slots keyed to typed gate variables ({{T2-PRESSURE}}, {{T2-VERDICT}}, {{VERBATIM-IA-SCOPE-TEMPLATES[T2-PRESSURE]}}) convert C-22 from a compliance checkbox into a user-facing contract that shows where each gate value appears in the final artifact"]}
```
