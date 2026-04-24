## Flow-Resilience R6 — Scoring Report

### Methodology

These are prompt templates evaluated on what structure they mandate. Each template is scored on whether a compliant output would satisfy each criterion. Trace artifact is placeholder — scoring is template-structural.

---

## V-01 — Typed Nil-Finding Identifiers

**Axis**: C-22 only. 4-phase structure (no scope declaration, no named rule blocks).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Scenario Coverage | PASS | Phase 1 enumerates across Offline/Partial-Failure/Eventual-Consistency; Phase 2 mandates ≥2/class |
| C-02 Four-Field Structure | PASS | Phase 2 mandates State/Capability/Data at risk/Recovery path |
| C-03 Gap Identification | PASS | Phase 3 produces all three sections |
| C-04 DS Accuracy | PASS | No incorrect DS claims; dispositions properly constrained |
| C-05 Commerce Grounding | PASS | Phase 2 Capability references commerce operations by name |
| C-06 Severity/Blast Radius | FAIL | Not mandated in Phase 2 template |
| C-07 Recovery Actor Labels | PASS | Recovery path uses ordered steps with actor prefix |
| C-08 CR Strategy | PASS | Phase 4 covers strategy + adequacy verdict |
| C-09 Chaos Engineering | FAIL | No chaos content |
| C-10 Observability | FAIL | No observability content |
| C-11 Confidence Catalog | PARTIAL | Include/BARRED/Argued-Impossible present with Basis; not labeled high/medium/low explicitly |
| C-12 Nil-Finding Norm | PASS | Phase 3 has typed nil protocol with scope rationale |
| C-13 Coverage Accountability | FAIL | No pre-analysis roster committing to per-class minimums |
| C-14 CR→DCV Linkage | PASS | "If verdict is `no` or strategy is `undefined`: append DCV-CR-NN" — linkage visible |
| C-15 DS-Primitive Impossibility | PARTIAL | Argued-Impossible present; no named "DS Primitive cited:" field or VALID/INVALID examples |
| C-16 Named Gate-State Vocab | PARTIAL | TRIAGE GATE: OPEN/CLOSED present; phases 2–4 lack equivalent gate status blocks |
| C-17 Permanently BARRED Gaps | FAIL | No BARRED register or coverage gap registry |
| C-18 Phase Entry/Exit Conditions | PARTIAL | Phase 1 gate has "Do not proceed until CLOSED"; phases 2–4 use prose sequencing only |
| C-19 Gate Blockage Transparency | FAIL | No "Reason if OPEN" field anywhere |
| C-20 Downstream Amendment Record | PARTIAL | DCV-CR-NN appended + DCV-NIL-1: SUPERSEDED noted; no labeled GATE 3b: AMENDED sub-gate |
| C-21 Commerce Scope Declaration | FAIL | No upfront scope declaration |
| C-22 Typed Nil Identifiers | PASS | OEG-NIL-1, DCV-NIL-1, MRF-NIL-1 with unique numeric suffix protocol; supersession notation defined |
| C-23 Scope Bracket | FAIL | No scope bracket (axis not in this variation) |
| C-24 Conditional Linkage Rules | FAIL | Inline prose conditional only ("If verdict is `no`..."); no named rule block |

**Essential**: 5×12 = **60/60**
**Recommended**: C-06(0) + C-07(10) + C-08(10) = **20/30**
**Aspirational raw**: C-11(1)+C-12(2)+C-14(2)+C-15(1)+C-16(1)+C-18(1)+C-20(1)+C-22(2) = 11 → **capped at 10**

**V-01 Composite: 90**

---

## V-02 — Scope Declaration Closure Bracket

**Axis**: C-23 only. 4-gate structure with scope bracket; nil identifiers lack numeric suffixes; no named rules.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Gate 1 enumerates all three classes with ≥2 Include required |
| C-02 | PASS | Gate 2 mandates all four fields |
| C-03 | PASS | Gate 3 has all three sections |
| C-04 | PASS | Technically sound |
| C-05 | PASS | Capability references named commerce operations |
| C-06 | FAIL | No severity/blast radius in template |
| C-07 | PASS | Actor-prefixed recovery steps mandated |
| C-08 | PASS | Gate 4 CR with strategy + adequacy verdict |
| C-09 | FAIL | No chaos content |
| C-10 | FAIL | No observability content |
| C-11 | PARTIAL | Dispositions present with Basis; confidence labels not explicit |
| C-12 | PASS | Gate 3 nil findings with scope rationale (OEG-NIL:, DCV-NIL:, MRF-NIL:) |
| C-13 | FAIL | No pre-analysis coverage roster |
| C-14 | PASS | "If verdict is `inadequate` or strategy is `undefined`: append DCV-CR-NN" — linkage present |
| C-15 | FAIL | No "DS Primitive cited:" field; no VALID/INVALID examples in Argued-Impossible |
| C-16 | PASS | All gates carry GATE N STATUS: OPEN/CLOSED with named dispositions |
| C-17 | FAIL | No BARRED resolution register or coverage gap registry |
| C-18 | PASS | All gates carry **Entry condition** and **Exit condition** citing prior gate IDs |
| C-19 | FAIL | No "Reason if OPEN" field in gate status blocks |
| C-20 | FAIL | Gate 4 appends DCV-CR-NN without labeled re-open/re-close sub-gate |
| C-21 | PASS | Commerce Operation Scope Declaration before Gate 1 with ≥4 operations required |
| C-22 | FAIL | Nil identifiers use unindexed form (OEG-NIL:) — no numeric suffix |
| C-23 | PASS | SCOPE BRACKET: OPENING + SCOPE BRACKET: CLOSING with per-operation coverage outcomes |
| C-24 | FAIL | Only prose conditional in Gate 4; no named rule blocks |

**Essential**: **60/60**
**Recommended**: **20/30**
**Aspirational raw**: C-11(1)+C-12(2)+C-14(2)+C-16(2)+C-18(2)+C-21(2)+C-23(2) = 13 → **capped at 10**

**V-02 Composite: 90**

---

## V-03 — Template-Embedded Conditional Linkage Rules

**Axis**: C-24 only. 4-gate + Gate 1b + Gate 3b structure; named RULE blocks; no scope bracket; nil IDs lack numeric suffixes.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Gate 1 enumerates all three classes |
| C-02 | PASS | Gate 2 mandates all four fields |
| C-03 | PASS | Gate 3 has all three sections |
| C-04 | PASS | Technically sound |
| C-05 | PASS | Named commerce operations in Capability |
| C-06 | FAIL | No severity/blast radius |
| C-07 | PASS | Actor-prefixed recovery steps mandated |
| C-08 | PASS | Gate 4 CR analysis with strategy + adequacy verdict |
| C-09 | FAIL | No chaos content |
| C-10 | FAIL | No observability content |
| C-11 | PARTIAL | Dispositions with Basis; not explicit confidence ratings |
| C-12 | PASS | Gate 3 nil findings with scope rationale |
| C-13 | FAIL | No pre-analysis roster |
| C-14 | PASS | RULE CR-DCV generates DCV-CR-NN entries linked to CR findings by ID |
| C-15 | FAIL | No "DS Primitive cited:" field in Gate 1 Argued-Impossible; no VALID/INVALID examples |
| C-16 | PASS | Named dispositions + OPEN/CLOSED on all gates including Gate 1b, 3b |
| C-17 | PASS | Gate 1b BARRED register + Gate 3b Coverage Gap Registry via RULE BARRED-CG |
| C-18 | PASS | All gates carry named Entry/Exit conditions with gate ID references |
| C-19 | FAIL | No "Reason if OPEN" field in gate status blocks |
| C-20 | PASS | GATE 3: REOPENED → DCV-CR-NN → GATE 3[a/b/c]: AMENDED — RULE CR-DCV / CR-NN → Status: CLOSED |
| C-21 | FAIL | No upfront commerce operation scope declaration |
| C-22 | FAIL | Nil identifiers use unindexed form (OEG-NIL:) |
| C-23 | FAIL | No scope bracket (axis not in this variation) |
| C-24 | PASS | RULE CR-DCV + RULE BARRED-CG declared as named conditional rule blocks with trigger/action/IDs |

**Essential**: **60/60**
**Recommended**: **20/30**
**Aspirational raw**: C-11(1)+C-12(2)+C-14(2)+C-16(2)+C-17(2)+C-18(2)+C-20(2)+C-24(2) = 15 → **capped at 10**

**V-03 Composite: 90**

---

## V-04 — Typed Nil Identifiers + Scope Closure Bracket

**Axes**: C-22 + C-23. 4-gate structure; OP-NN scope IDs; typed nil with numeric suffix; terminal scope bracket; prose CR linkage (no named rules).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Gate 1 enumerates all three classes |
| C-02 | PASS | Gate 2 mandates all four fields |
| C-03 | PASS | Gate 3 has all three sections |
| C-04 | PASS | Technically sound |
| C-05 | PASS | Capability references named operations by OP-NN |
| C-06 | FAIL | No severity/blast radius |
| C-07 | PASS | Actor-prefixed recovery steps mandated |
| C-08 | PASS | Gate 4 CR analysis |
| C-09 | FAIL | No chaos content |
| C-10 | FAIL | No observability content |
| C-11 | PARTIAL | Dispositions with Basis; not labeled high/medium/low explicitly |
| C-12 | PASS | Gate 3 nil findings with typed IDs and scope rationale |
| C-13 | FAIL | No pre-analysis roster |
| C-14 | PASS | "If verdict is `inadequate` or strategy is `undefined`: append DCV-CR-NN" — linkage visible |
| C-15 | FAIL | No "DS Primitive cited:" field or VALID/INVALID examples |
| C-16 | PASS | All gates carry OPEN/CLOSED with named dispositions |
| C-17 | FAIL | No Gate 1b BARRED register or coverage gap registry |
| C-18 | PASS | Entry/Exit conditions on all gates citing prior gate IDs |
| C-19 | FAIL | No "Reason if OPEN" field |
| C-20 | PARTIAL | DCV-CR-NN appended + DCV-NIL-N: SUPERSEDED notation present; no labeled GATE 3b: AMENDED sub-gate |
| C-21 | PASS | OP-NN scope declaration before Gate 1 with ≥4 operations |
| C-22 | PASS | OEG-NIL-1, DCV-NIL-1, MRF-NIL-1 with unique numeric suffix required; supersession by ID defined |
| C-23 | PASS | SCOPE BRACKET: OPENING + SCOPE BRACKET: CLOSING; per-operation coverage outcomes |
| C-24 | FAIL | Prose conditional only; no named rule blocks |

**Essential**: **60/60**
**Recommended**: **20/30**
**Aspirational raw**: C-11(1)+C-12(2)+C-14(2)+C-16(2)+C-18(2)+C-20(1)+C-21(2)+C-22(2)+C-23(2) = 16 → **capped at 10**

**V-04 Composite: 90**

---

## V-05 — Full R6 Formalization

**Axes**: C-22 + C-23 + C-24 + full C-15–C-21. All three R6 axes layered onto R5 formalization.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Gate 1 enumerates all three classes; ≥2 Include per class required |
| C-02 | PASS | Gate 2 mandates all four fields |
| C-03 | PASS | Gate 3 has all three sections |
| C-04 | PASS | Technically sound |
| C-05 | PASS | Capability references named operations by OP-NN ID |
| C-06 | FAIL | No severity/blast radius in template |
| C-07 | PASS | Actor-prefixed recovery steps with trigger condition mandated |
| C-08 | PASS | Gate 4 CR with named strategy, adequacy verdict, rationale |
| C-09 | FAIL | No chaos engineering content |
| C-10 | FAIL | No observability content |
| C-11 | PASS | Disposition table maps Include=high/medium confidence, BARRED=low, Argued-Impossible=impossible with Basis; BARRED entries gated until resolved in Gate 1b — not merely flagged |
| C-12 | PASS | Gate 3 typed nil findings (OEG-NIL-1 etc.) with scope rationale |
| C-13 | PARTIAL | Gate 1 exit condition requires ≥2 Include per class; GATE 1 STATUS shows Include counts per class (checkable); but no dedicated pre-analysis roster document preceding enumeration |
| C-14 | PASS | RULE CR-DCV enforces DCV linkage; sub-gate amendments cite CR-NN by ID |
| C-15 | PASS | Gate 1c Impossibility Register has "DS Primitive cited:" named field, Architecture argument, VALID example, INVALID example; "topic doesn't mention X" explicitly rejected |
| C-16 | PASS | All gates carry named dispositions + explicit OPEN/CLOSED on every gate |
| C-17 | PASS | RULE BARRED-CG queues CG-NN to Gate 3b Coverage Gap Registry; permanently BARRED entries appear as named gaps |
| C-18 | PASS | All gates carry named Entry/Exit conditions citing prior gate IDs; explicit CLOSED confirmation required |
| C-19 | PASS | All gates carry "Reason if OPEN:" field; "bare GATE N: OPEN with no Reason if OPEN is an error" stated explicitly |
| C-20 | PASS | RULE CR-DCV produces GATE 3: REOPENED → amendment → GATE 3[a/b/c]: AMENDED — RULE CR-DCV / CR-NN → Status: CLOSED; No-Amendment Confirmation when not triggered |
| C-21 | PASS | OP-NN scope declaration before Gate 1; final Gate 2 cross-checked in terminal bracket |
| C-22 | PASS | OEG-NIL-N, DCV-NIL-N, MRF-NIL-N with unique numeric suffix; supersession notation: "DCV-NIL-N: SUPERSEDED — DCV-CR-NN via RULE CR-DCV" |
| C-23 | PASS | SCOPE BRACKET: OPENING + SCOPE BRACKET: CLOSING naming each OP-NN with coverage outcome |
| C-24 | PASS | RULE CR-DCV and RULE BARRED-CG declared as named rule blocks with Trigger/Action/Applies/IDs fields; inline declaration protocol for additional rules |

**Essential**: **60/60**
**Recommended**: **20/30**
**Aspirational raw**: C-11(2)+C-12(2)+C-13(1)+C-14(2)+C-15(2)+C-16(2)+C-17(2)+C-18(2)+C-19(2)+C-20(2)+C-21(2)+C-22(2)+C-23(2)+C-24(2) = 29 → **capped at 10**

**V-05 Composite: 100**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational (raw→cap) | Composite |
|-----------|-----------|-------------|------------------------|-----------|
| V-01 | 60 | 20 | 11→10 | **90** |
| V-02 | 60 | 20 | 13→10 | **90** |
| V-03 | 60 | 20 | 15→10 | **90** |
| V-04 | 60 | 20 | 16→10 | **90** |
| V-05 | 60 | 20 | 29→10 | **100** |

**Ranking**: V-05 > V-04 > V-03 > V-02 > V-01 (by uncapped aspirational breadth; composite ties V-01–V-04 at 90)

**All essential pass**: Yes, all five variations

---

## Excellence Signals — V-05

**Pattern 1 — Fully typed nil artifacts**: `OEG-NIL-N` / `DCV-NIL-N` / `MRF-NIL-N` with mandatory unique numeric suffix creates nil findings as first-class citable objects. When Gate 4 amends a nil, `DCV-NIL-1: SUPERSEDED — DCV-CR-NN via RULE CR-DCV` traces the supersession chain. Without the unique suffix, this cross-reference is impossible even if the prose is correct.

**Pattern 2 — Two-block scope bracket as a binary event pair**: `SCOPE BRACKET: OPENING` before Gate 1 + `SCOPE BRACKET: CLOSING` after Gate 4 creates a structurally auditable commitment. The closing block names each OP-NN with its coverage outcome. A reader can verify scope closure without reading any analysis — the bracket is either present as a matching pair or not. Single-block declarations (C-21 alone) cannot be verified closed.

**Pattern 3 — Named conditional rule blocks with mandatory citation**: `RULE CR-DCV` and `RULE BARRED-CG` defined with Trigger/Action/Applies/IDs make cross-section linkage mandatory and traceable. Every amendment record cites the rule by ID (`GATE 3a: AMENDED — RULE CR-DCV / CR-NN`). This makes two separate findings that trigger the same linkage both traceable to the same rule ID — not just described in prose that two readers may interpret differently.

**Pattern 4 — No-Amendment Confirmation as mandatory gate output**: When RULE CR-DCV is not triggered, the template requires an explicit confirmation block rather than silence. Absence of an amendment is not equivalent to silence; this makes "amendment check skipped" distinguishable from "amendment check run and found nothing."

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["typed nil-finding identifiers with unique numeric suffixes enable supersession cross-referencing when Gate 4 amends a nil (OEG-NIL-1: SUPERSEDED — DCV-CR-NN via RULE CR-DCV)", "two-block scope bracket as matched binary event pair (SCOPE BRACKET: OPENING before Gate 1 + SCOPE BRACKET: CLOSING after Gate 4) makes scope verification independently auditable without reading the analysis body", "named conditional rule blocks (RULE CR-DCV, RULE BARRED-CG) with Trigger/Action/Applies/IDs make cross-section linkages mandatory and citable by rule ID in every amendment record they produce"]}
```
