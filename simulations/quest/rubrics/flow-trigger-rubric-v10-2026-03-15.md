**flow-trigger-rubric-v10** written to `simulations/quest/rubrics/flow-trigger-rubric-v10-2026-03-16.md`.

---

**Two new aspirational criteria (C-32–C-33), N_aspirational: 23 → 25, max (raw): 122.5 → 127.5:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-32 | V-04 advance — 8-column registry unifying status + refutation + contrast + activation + role in a single table | All Phase 0 obligation metadata co-located in one registry row: status, refutation condition, weaker alternative, failure mode, activation event, producing role. Each row is a complete self-audit record; cross-table navigation to assess any single obligation is eliminated. | C-25/C-27 (status column), C-28 (refutation condition column), C-29 (contrast columns), C-30 (activation event column), C-31 (producing role column) — unifies all six |
| C-33 | V-05 advance — INERTIA CONTRAST section naming "anonymous prohibition" and "anonymous artifact gap" as failure modes | Failure mode labels are specific enough to function as structural constraints: "anonymous prohibition" logically requires temporal-anchor attribution; "anonymous artifact gap" requires both role and phase to be named fields. Reading the failure mode derives the pass condition without consulting the rubric. | C-26 (the rationale section it makes prescriptive), C-29 (the inline columns it targets with constraint-grade labels) |

**Structural relationship:** C-32 resolves the navigation cost of satisfying C-25–C-31 through separate tables — one unified registry row carries every metadata type, and any future criterion adds a column rather than a table. C-33 resolves the explanatory-vs-prescriptive gap in C-26/C-29 — a failure mode that names the absent structural property ("anonymous [X]") forces the mechanism to make X explicit, whereas a failure mode that describes only the consequence ("ambiguity") leaves the implementation underconstrained. Together they complete the Phase 0 self-enforcement model at the integration layer: the six criteria are physically unified (C-32) and the rationale that motivates each column is strong enough to regenerate the column's requirements from the rationale alone (C-33).
