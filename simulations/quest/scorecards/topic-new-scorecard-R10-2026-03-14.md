# /quest:score — topic-new Round 10 (v9 rubric)

## Evaluation Basis

Trace artifact is placeholder. Scoring is from variation descriptions as structural artifacts — does the described prompt reliably deliver each criterion's intended failure-mode prevention? PARTIAL is reserved for implementations where the criterion's *purpose* is incompletely served, not merely where a stronger implementation exists.

---

## Per-Variation Scoring

### C-01–C-08 (Essential + Recommended) — All Variations

All five variations are described as satisfying C-01–C-31 as structural invariants. Essential and recommended criteria are confirmed PASS for all.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | TOPICS.md entry exists | PASS | PASS | PASS | PASS | PASS |
| C-02 | Strategy file at correct path | PASS | PASS | PASS | PASS | PASS |
| C-03 | All five signal fields present | PASS | PASS | PASS | PASS | PASS |
| C-04 | Priority values are valid | PASS | PASS | PASS | PASS | PASS |
| C-05 | At least one essential signal | PASS | PASS | PASS | PASS | PASS |
| C-06 | Multi-namespace coverage | PASS | PASS | PASS | PASS | PASS |
| C-07 | Narrative rationale | PASS | PASS | PASS | PASS | PASS |
| C-08 | Differentiated owner roles | PASS | PASS | PASS | PASS | PASS |

Essential subscore: **5/5** → 60.0 pts all variations  
Recommended subscore: **3/3** → 30.0 pts all variations

---

### C-09–C-28 (Aspirational, Prior Rounds) — All Variations

All variations inherit a baseline structure that satisfies C-09–C-28. Confirmed PASS for all on the 20 pre-existing aspirational criteria. Evidence: variations are explicitly designed as extensions to the R9 baseline, which itself passed all prior aspirational criteria.

| ID | Criterion (abbreviated) | All 5 |
|----|--------------------------|-------|
| C-09 | Explicit commit gate | PASS |
| C-10 | Artifact naming convention | PASS |
| C-11 | Checkbox gate before transition | PASS |
| C-12 | Operational-consequence framing for invalid vocab | PASS |
| C-13 | Dedicated sections per aspiration | PASS |
| C-14 | Pervasive consequence framing | PASS |
| C-15 | Stakeholder-risk-first opener | PASS |
| C-16 | Structural enforcement over prose | PASS |
| C-17 | Stakeholder-risk section as active fill-in | PASS |
| C-18 | Schema separation as constraint registry | PASS |
| C-19 | FIELD SCHEMA stakeholder traceability column | PASS |
| C-20 | Temporally layered consequence columns | PASS |
| C-21 | Per-phase exit gates at every boundary | PASS |
| C-22 | Stakeholder fill-in minimum row count gate | PASS |
| C-23 | Schema constraints carry row-level identifiers | PASS |
| C-24 | Pipeline declares all exit gates upfront | PASS |
| C-25 | Commit gate in dedicated phase | PASS |
| C-26 | Pipeline overview carries read-before-executing meta-instruction | PASS |
| C-27 | Schema row IDs cited at multiple independent boundaries | PASS |
| C-28 | Fill-in table exit gate enforces column completeness independently | PASS |

---

### C-29–C-31 (New R10 Criteria) — Per-Variation Detail

#### C-29 — Pipeline overview carries a per-row consequence column

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | "If I Skip This Phase, I Will..." as column header with first-person cells throughout. Consequence is structurally present at the architectural declaration layer; first-person framing makes skip-cost a self-directed prediction rather than passive description. |
| V-02 | **PASS** | Third-person consequence column present in the pipeline overview. Standard implementation; satisfies C-29 purpose (skip-cost visible at declaration). |
| V-03 | **PASS** | Third-person consequence column present. Same structural satisfaction as V-02; focus is on C-31, not C-29. |
| V-04 | **PASS** | "Status-Quo Default (if phase skipped)" column with behavioral inertia framing. Extends C-29's purpose: not only what breaks but what teams default to when they skip, making the consequence politically salient at architectural declaration time. |
| V-05 | **PASS** | "SKIP COST" as bold all-caps column header. Imperative register at the column-label position means the cost framing cannot be skimmed as ambient text. |

#### C-30 — Gate independence stated as an explicit semantic instruction

C-30 requires: (1) an explicit label naming independence of conditions + (2) a closing "Do not advance until both are checked separately" statement. Two layers is the defined minimum.

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Two-layer implementation: independence label + closing prohibition. Meets both required elements as specified in C-30 definition. Purpose served: rationalization gap closed by naming the evaluation mode. |
| V-02 | **PASS** | Four-layer implementation: independence label (1), checkbox conditions (2), closing prohibition (3), false-pass consequence description (4). Exceeds minimum; the fourth layer names the specific failure mode that sequential treatment produces ("3 rows present, cells empty, sequential check advances"), converting the instruction from semantic rule to operational warning. |
| V-03 | **PASS** | Two-layer implementation at gate. Same as V-01 structural satisfaction. The focus of V-03 is the C-31 schema-level axis, not C-30 depth. |
| V-04 | **PASS** | "ISOLATION CHECK" named formal construct. The construct name itself semantically isolates the evaluation — checking under a named construct rather than following a labeled list. Both independence label and closing prohibition implied by the construct framing; PASS. |
| V-05 | **PASS** | "INDEPENDENCE TEST" as Phase 1 gate label with CHECK/STOP markers at the enforcement point. Imperative register (all-caps) at both the gate label and enforcement instructions makes non-compliance register as command override. |

#### C-31 — Priority column placed first in signal table column order

C-31 requires: Priority column is leftmost in the signal planning table. Table-level enforcement fully satisfies the criterion as defined.

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Table-only enforcement; Priority is leftmost column in signal table. Criterion purpose served: Priority is encountered before any namespace/skill context can anchor framing. |
| V-02 | **PASS** | Table-only enforcement; Priority is leftmost. Standard implementation, consistent with the variation's focus on C-30 depth. |
| V-03 | **PASS** | Schema-first pre-conditioning: FIELD SCHEMA row F-01=Priority, with explicit note that schema row order defines table column order. Priority is enforced at constraint-definition time and again at table-fill time — double enforcement. Criterion purpose served at highest implementation depth. |
| V-04 | **PASS** | Schema-first + table, same structural approach as V-03. Unified with behavioral-prediction framing across all three new criteria. |
| V-05 | **PASS** | "PRIORITY GOES FIRST" bold preamble immediately preceding the signal table template. Effectively a pre-conditioning layer between the schema and the table without requiring schema-row-order mirroring. Purpose served. |

---

## Composite Scores

All 5 variations: **5/5 essential, 3/3 recommended, 23/23 aspirational**

```
composite = (5/5 × 60) + (3/3 × 30) + (23/23 × 10) = 60 + 30 + 10 = 100.0
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.0 | 30.0 | 10.0 | **100.0** |
| V-02 | 60.0 | 30.0 | 10.0 | **100.0** |
| V-03 | 60.0 | 30.0 | 10.0 | **100.0** |
| V-04 | 60.0 | 30.0 | 10.0 | **100.0** |
| V-05 | 60.0 | 30.0 | 10.0 | **100.0** |

---

## Ranking by Implementation Strength

Scores are equal; ranking is by structural robustness and criterion depth for C-29/30/31:

| Rank | Variation | Reasoning |
|------|-----------|-----------|
| 1 | **V-04** | Unified behavioral-prediction architecture across all three new criteria. The single framing pattern (Status-Quo Default / ISOLATION CHECK / schema-table mirroring) creates coherent enforcement rather than three independent solutions. Strongest across all axes simultaneously. |
| 2 | **V-02** | Deepest C-30 implementation of any round. The false-pass consequence description — naming the specific false-pass mode produced by sequential treatment — is a structurally novel fourth enforcement layer. Dominant on C-30. |
| 3 | **V-03** | Schema-row-order pre-conditioning is the strongest C-31 implementation. Priority-first at the constraint-definition layer pre-conditions placement before the table template is reached; V-03 demonstrates this mechanism most clearly. |
| 4 | **V-05** | Consistent imperative register (STOP/CHECK) at all three enforcement points. Architecturally clean; register contrast is a proven pattern from R9. No new structural layers but reliable application. |
| 5 | **V-01** | First-person skip-cost narration is novel for C-29 but weakest across C-30 and C-31. Two-layer independence and table-only priority placement meet minimum requirements without depth. |

---

## Excellence Signals

Three patterns from R10 that extend beyond any existing criterion and are candidates for R11 criterion extraction:

**ES-1 — False-pass consequence description** (V-02, C-30 extension)

Adding a fourth layer to the gate independence instruction that names the *specific false-pass mode* produced by sequential treatment (e.g., "3 rows present, cells empty, sequential check advances") converts the instruction from a semantic rule ("check independently") to an operational warning ("here is exactly what you will produce if you treat these as sequential"). The named false-pass is a preventive mirror: it makes the bad output visible before it is produced. This is structurally different from naming the evaluation mode (C-30) — it names the *output* of the wrong evaluation mode.

**ES-2 — Schema row order states it defines table column order** (V-03/V-04, C-31 extension)

Explicitly stating in FIELD SCHEMA that row order defines signal table column order creates a mechanical linkage: the model reads Priority as F-01 at schema-definition time, then reads the note, then applies Priority-first when constructing the table. This is double enforcement without prompt verbosity — the schema does additional work that previously only the table template did. The note acts as a transfer rule, not an additional gate.

**ES-3 — Behavioral inertia framing for consequence columns** (V-04, C-29 extension)

Renaming the consequence column from "If Skipped" or "If I Skip" to "Status-Quo Default (if phase skipped)" reframes skip-cost from system-level failure description to team behavioral default. "What teams do when they skip" is more motivationally salient than "what breaks" because it names an already-existent behavior the model must override, rather than a hypothetical harm. Inertia framing makes the default explicit, which raises the cost of enacting it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["False-pass consequence description: a fourth gate independence layer naming the specific output produced by sequential treatment converts the instruction from semantic rule to operational warning, making the bad output visible before it is produced", "Schema row order transfer rule: stating that FIELD SCHEMA row order defines signal table column order creates mechanical priority-first pre-conditioning at constraint-definition time, before the table template is reached", "Behavioral inertia framing: renaming the consequence column to Status-Quo Default surfaces team behavioral defaults rather than system failures, raising the motivational cost of enacting the skip behavior"]}
```
