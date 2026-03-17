Here is the complete updated rubric:

---

```markdown
---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 2
---

# flow-dataflow Rubric — v2

## Purpose

Score a `flow-dataflow` skill output: a data lineage trace covering source,
transformation stages, and destination for a Finance, Operations, or Commerce
pipeline scenario.

---

## Scoring Formula

composite = (essential_pass/N_essential * 60)
          + (recommended_pass/N_recommended * 30)
          + (aspirational_pass/N_aspirational * 10)

Golden threshold: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total — must all pass)

| ID   | Criterion                        | Category    | Pass Condition |
|------|----------------------------------|-------------|----------------|
| C-01 | Data lineage chain               | correctness | Every in-scope data item has an unbroken source => stage(s) => destination chain. No item appears at a destination without an identified origin. |
| C-02 | Boundary error handling          | correctness | Each inter-stage boundary is annotated: either the error-handling mechanism or an explicit "no handling — risk accepted" flag. Silence fails. |
| C-03 | Data loss point identification   | coverage    | At least one concrete, named data loss point per pipeline stage. Generic "errors may occur" does not qualify. |
| C-04 | Schema state at each stage       | correctness | The schema at each stage entry/exit is described or diffed. A stage that alters field names, types, or cardinality with no annotation fails. |

---

## Recommended Criteria (weight: 30 pts total — 10 pts each)

| ID   | Criterion                  | Category | Pass Condition |
|------|----------------------------|----------|----------------|
| C-05 | Latency characterization   | depth    | Every stage carries a latency annotation: value, range, or characterization (real-time / micro-batch / hourly / daily). |
| C-06 | Stale data windows         | depth    | At least one stale window quantified. Failure-mode staleness addressed separately from normal-operation staleness. |
| C-07 | Domain framing             | format   | Domain entity names (Invoice, PurchaseOrder, SKU, LedgerEntry, etc.) appear in the chain. A trace using only "data" or "records" throughout fails. |

---

## Aspirational Criteria (weight: 10 pts total — 2 pts each)

| ID   | Criterion                            | Category    | Pass Condition |
|------|--------------------------------------|-------------|----------------|
| C-08 | Recovery prescriptions               | depth       | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion naming the mechanism and boundary. Generic advice does not qualify. |
| C-09 | Pattern trade-off analysis           | behavior    | A named alternative pattern with >=2 explicitly stated trade-off dimensions, at least one quantified or qualified in domain terms. |
| C-10 | Pre-trace entity inventory           | structure   | All in-scope domain entities are enumerated and named in a dedicated inventory step before the first stage is traced. The trace references only entities from this inventory. An entity introduced mid-trace without prior declaration fails. |
| C-11 | Systematic boundary labeling         | structure   | Every inter-stage boundary receives a named label (e.g., B1->2, B2->3) forming a complete inventory. C-02 and C-08 annotations reference these labels by name. A labeled boundary with no corresponding annotation is a visible, scorable gap. |
| C-12 | Verified-unchanged schema assertion  | correctness | Any stage asserting no schema change must carry an explicit verification statement (e.g., "verified: no field added, removed, renamed, or retyped"). A bare "unchanged" with no verification claim fails. |

---

## Changelog

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-15 | Initial — 4 essential, 3 recommended, 2 aspirational |
| v2      | 2026-03-15 | Added C-10, C-11, C-12 from Round 2 excellence signals; aspirational weight adjusted to 2 pts/criterion |
```

---

**Three patterns extracted and why each earns aspirational status:**

| New ID | Source signal | Upgrades which existing criterion | Why aspirational not essential |
|--------|---------------|-----------------------------------|-------------------------------|
| C-10 | V-01 Step 1 + V-03 Phase 0 — both top scorers gate the trace on an upfront entity list | C-07 (domain framing) — makes compliance structural, not reactive | Entity names *can* appear inline and still satisfy C-07; the inventory is a quality amplifier, not a baseline requirement |
| C-11 | V-03 Phase 2 cited as "strongest C-02 driver" — B1→2 labels turn coverage into a checklist | C-02 (boundary error handling) — makes omissions visible by construction | Boundaries can be annotated correctly without labels; labeling is a discipline that forces completeness, not a correctness floor |
| C-12 | V-01 "verified-unchanged" rule cited as "strongest C-04 driver" | C-04 (schema state) — adds a verification assertion to pass-through stages | C-04 passes with any schema description; the verification claim is a trust signal, not a minimum obligation |
