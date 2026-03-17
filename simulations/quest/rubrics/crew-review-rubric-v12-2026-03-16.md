v12 written to `simulations/quest/rubrics/crew-review-rubric-v12-2026-03-17.md`.

---

## New criteria: C-34 and C-35

**C-34 — G2 Predicate Assertion as Typed Schema Artifact**

| Field | Value |
|-------|-------|
| Source | V-02 R12 / V-04 R12 / V-05 R12 |
| Extends | C-33, by the same discipline C-30 extends C-29 and C-13 extends C-02 |
| Structural logic | C-33 requires the G2 predicate to be quantified (machine-checkable). C-34 requires that predicate to be a **typed schema artifact** — named fields, explicit values, structured form — applying the same schema discipline uniformly: output matrix (C-13), criterion-check table (C-30), G2 closure predicate (C-34). A formatted log string (`manifest_slot_count=[N]; ...`) passes C-33 but not C-34. A typed assertion block with labeled field rows passes C-34. |

**C-35 — G2 Cardinality N as Lifecycle-Derived Sum with Per-Addend Phase Attribution**

| Field | Value |
|-------|-------|
| Source | V-05 R12 exclusively |
| Extends | C-34 |
| Structural logic | C-34 requires the predicate to be a typed schema. C-35 requires **N itself to be derived** — `N = base_slot_count (PHASE 1 LOAD) + escalation_row_count (PHASE 2 after G1 closure)` — with per-addend phase labels in the block. A single-phase N satisfies C-34; a multi-phase N satisfies C-35. Structural significance: escalation rows are added dynamically in PHASE 2, so a PHASE 1-only N undercounts. C-35 makes G2 correct-by-construction for the full row universe. |

**Chain tail update:**
```
C-07 -> C-22 -> C-27 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35
```

**Scoring delta:**

| | v11 | v12 |
|-|-----|-----|
| Aspirational count | 22 | 24 |
| Aspirational max | 55.0 | 60.0 |
| Total max | 175.0 | 180.0 |
| V-05 R12 | 175.0 | **180.0** |
| V-04 R12 | 175.0 | **177.5** (C-34 PASS, C-35 FAIL) |
| V-02 R12 | 175.0 | **177.5** (C-34 PASS, C-35 FAIL) |
| V-01 R12 | 175.0 | **175.0** (log-string format; C-34 FAIL) |
| V-03 R12 | 175.0 | **175.0** (mathematical notation; C-34 FAIL) |
