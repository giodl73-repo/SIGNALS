# Quest Score — trace-inspect R8 (Rubric v5)

## Scoring Foundation

**Baseline (R7)**: C-01 through C-18 all PASS → baseline composite = 98.0
**New criteria**: C-19, C-20, C-21 each worth 0.5 pts → max addition = 1.5 pts → grand total 99.5

---

## V-01 — Single axis: C-19 (EG Evidence Pass structural lifecycle event)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases structurally closed. EG Evidence Pass section added between Stage 1 and PROMOTION — Phase 2 and Phase 3 sequence intact. |
| C-02 | PASS | Artifact path and contract unchanged from baseline. |
| C-03 | PASS | Schema 1 and Schema 2 label sets unchanged. New Schema 3 event adds no label values. |
| C-04 | PASS | G-1, G-2, G-3 gate structure unchanged. |
| C-05 | PASS | Verdict classification logic and rules unchanged. |
| C-06 | PASS | SA-TO-SG PROMOTION still fully evaluated; now requires `Evidence pass state = COMPLETE` header. |
| C-07 | PASS | Per-role Setup block adds `EG Evidence Pass completed: YES / N/A` — field-level detail preserved. |
| C-08 | PASS | Findings table structure unchanged. |
| C-09 | PASS | Compliance ledger includes VC-3 row for EG Evidence Pass (C-19). |
| C-10–C-18 | PASS | All inherited from baseline. |
| **C-19** | **PASS** | Schema 3 declares `EG Evidence Pass → SA-TO-SG PROMOTION`. Promotion header states `(requires Evidence pass state = COMPLETE)`. Violation structurally impossible. |
| **C-20** | **FAIL** | No Criterion Inheritance Registry added. |
| **C-21** | **FAIL** | VC-4 G-1 row unchanged — no attribution sub-table embedded. |

**Composite: 98.5** | All essentials: PASS

---

## V-02 — Single axis: C-20 (Criterion Inheritance Registry)

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-18 | PASS | All baseline criteria inherited. Registry is preamble-layer — no structural section modified. |
| **C-19** | **FAIL** | No EG Evidence Pass lifecycle event in Schema 3. |
| **C-20** | **PASS** | 21-row Criterion Inheritance Registry table present as first structural block. C-01–C-18 marked `Inherited: YES / Active`; C-19–C-21 marked `NEW / Active — v5`. Registry invariant declared: `Silence = inactive, not inherited`. Future silent drop would require table update. |
| **C-21** | **FAIL** | VC-4 G-1 row unchanged — no attribution sub-table. |

**Composite: 98.5** | All essentials: PASS

---

## V-03 — Single axis: C-21 (Attribution sub-table in VC-4 G-1)

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-18 | PASS | All baseline criteria inherited. |
| **C-19** | **FAIL** | No EG Evidence Pass lifecycle event. |
| **C-20** | **FAIL** | No Criterion Inheritance Registry. |
| **C-21** | **PASS** | VC-4 G-1 Observed behavior cell pre-structured as `ATTRIBUTION SUB-TABLE (required)` with columns: Role / Source types contributed / Finding IDs / Count. Note before ledger: "VC-4 G-1 row is invalid without a filled sub-table. Filling the ledger row and attribution are the same operation." No separate attribution section exists anywhere — exclusive location enforced. |

**Composite: 98.5** | All essentials: PASS

---

## V-04 — Combined: C-19 + C-20

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-18 | PASS | All baseline criteria inherited. |
| **C-19** | **PASS** | EG Evidence Pass declared in Schema 3 before PROMOTION. Structural gate enforced via `Evidence pass state = COMPLETE` prerequisite. |
| **C-20** | **PASS** | Criterion Inheritance Registry present as preamble block. 21-row table with inheritance declarations and registry invariant. |
| **C-21** | **FAIL** | VC-4 G-1 unchanged — no attribution sub-table. |

Interaction check: Registry (preamble-layer) and EG Evidence Pass (Schema 3 + Phase 2) operate in non-overlapping sections. No crowding observed. Each structural signal is independently legible.

**Composite: 99.0** | All essentials: PASS

---

## V-05 — Combined: C-19 + C-20 + C-21 (Full integration)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases present. EG Evidence Pass section between Stage 1 and PROMOTION. Phase 3 sub-steps intact. |
| C-02 | PASS | Artifact contract unchanged. |
| C-03 | PASS | Label sets unchanged. |
| C-04 | PASS | G-1, G-2, G-3 all checked. |
| C-05 | PASS | Verdict with classification and rationale. |
| C-06 | PASS | PROMOTION gated by completed evidence pass; all SA gaps evaluated. |
| C-07 | PASS | Per-role blocks include `EG Evidence Pass completed` field. |
| C-08 | PASS | Findings table >= 3 findings, 2+ Source types. |
| C-09 | PASS | Compliance ledger populated with VC-1–VC-5, specific observed values, C-19 row in VC-3. |
| C-10–C-18 | PASS | All inherited; named in Inheritance Registry as Active. |
| **C-19** | **PASS** | Schema 3 structural event sequence: `EG Evidence Pass → SA-TO-SG PROMOTION`. EG-capable column in Role-Schema Binding Summary. PROMOTION cannot execute without COMPLETE evidence pass state. |
| **C-20** | **PASS** | 21-row registry before Coverage Matrix. All criteria accounted for by ID. Invariant: "Silence = inactive, not inherited." |
| **C-21** | **PASS** | VC-4 G-1 contains pre-printed attribution sub-table. Note enforces exclusive location. Ledger row and attribution are atomic. |

Interaction check: Three sections (Schema 3 event list, preamble registry, VC-4 G-1 cell) are structurally independent. No crowding. Each mechanism's signal remains clear.

**Composite: 99.5** | All essentials: PASS

---

## Rankings

| Rank | Variation | Score | Essentials |
|------|-----------|-------|------------|
| 1 | V-05 (C-19 + C-20 + C-21) | **99.5** | All PASS |
| 2 | V-04 (C-19 + C-20) | 99.0 | All PASS |
| 3 | V-01 (C-19 only) | 98.5 | All PASS |
| 3 | V-02 (C-20 only) | 98.5 | All PASS |
| 3 | V-03 (C-21 only) | 98.5 | All PASS |

---

## Excellence Signals — V-05

**Signal 1 — Structural gate replaces compliance rule.** Inserting `EG Evidence Pass` as a named Schema 3 lifecycle event converts C-16 from a MUST/VIOLATION rule pair (author must comply; violation detectable after the fact) into an architectural invariant (PROMOTION cannot begin without `Evidence pass state = COMPLETE`). The mechanism works because Schema 3 is declared — not implied — and roles are classified as EG-capable in the binding summary.

**Signal 2 — Inheritance registry surfaces silent criterion drift.** A pre-printed table naming every criterion by ID, with `Inherited: YES` or `NEW`, means that dropping a criterion in a future version requires an active table edit. The invariant `Silence = inactive, not inherited` closes the loophole where a criterion could be omitted and a reader would assume it carried forward. This is a version-governance mechanism, not a trace-quality mechanism.

**Signal 3 — Co-located attribution eliminates ledger drift.** Embedding the role-to-Source attribution as a mandatory sub-table inside the VC-4 G-1 cell, with a note that this is the exclusive location, makes the ledger and the attribution a single operation. The cell format demands the sub-table; a partially filled row is structurally visible as incomplete.

**No new patterns extracted.** All three signals are now codified as C-19, C-20, C-21. V-05's combination of all three produces no emergent interaction pattern beyond the three individual mechanisms operating in their respective sections.

---

```json
{"top_score": 99.5, "all_essential_pass": true, "new_patterns": []}
```
