Reading the Round 3 scorecard for excellence patterns not yet captured by C-08 through C-12.

**Two patterns consistently emerge above the rubric baseline:**

**Pattern 1 — Structural completeness enforcement (V-02, V-03)**
Both top scorers (96 pts) make omissions *structurally visible*, not just scorably bad. V-02's boundary and schema-diff tables use "blank cell = structural gap." V-03's inline boundary gate uses "Stage N+1 does not open until BOUNDARY GATE is fully stated — omission is a protocol violation." Neither V-01 nor V-04 employs this; their requirements live in prose where gaps can be buried.

**Pattern 2 — Incumbent baseline anchoring (V-04)**
V-04 distinguishes itself on C-08 and C-09 by naming the pre-automation operational process as the explicit fallback and comparison anchor. Generic recovery terms ("retry", "manual review") without grounding in the named baseline don't qualify. No other variant does this.

**Why both earn aspirational, not essential:**
Structural enforcement is a quality amplifier — tables and gates make existing required content impossible to omit silently, but the content itself is already required by C-02/C-03/C-04. Baseline anchoring deepens C-08 and C-09 beyond their pass conditions but does not invalidate responses that meet those conditions via other means.

---

```markdown
---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 3
---

# flow-dataflow Rubric — v3

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

## Aspirational Criteria (weight: 10 pts total — 10/9 pts per criterion)

| ID   | Criterion                            | Category    | Pass Condition |
|------|--------------------------------------|-------------|----------------|
| C-08 | Recovery prescriptions               | depth       | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion naming the mechanism and boundary. Generic advice does not qualify. |
| C-09 | Pattern trade-off analysis           | behavior    | A named alternative pattern with >=2 explicitly stated trade-off dimensions, at least one quantified or qualified in domain terms. |
| C-10 | Pre-trace entity inventory           | structure   | All in-scope domain entities are enumerated and named in a dedicated inventory step before the first stage is traced. The trace references only entities from this inventory. An entity introduced mid-trace without prior declaration fails. |
| C-11 | Systematic boundary labeling         | structure   | Every inter-stage boundary receives a named label (e.g., B1->2, B2->3) forming a complete inventory. C-02 and C-08 annotations reference these labels by name using the B[N]->[N+1] format explicitly. A labeled boundary with no corresponding annotation is a visible, scorable gap. |
| C-12 | Verified-unchanged schema assertion  | correctness | Any stage asserting no schema change must carry an explicit verification statement (e.g., "verified: no field added, removed, renamed, or retyped"). A bare "unchanged" with no verification claim fails. |
| C-13 | Structural completeness enforcement  | structure   | At least one mandatory section (boundary inventory, schema diffs, or loss points) is organized as a table or inline protocol gate where a missing entry is structurally visible — a blank cell, a missing row, or a missing gate block constitutes an explicit gap. Prose-only requirements do not qualify. The table or gate must map directly to a scorable requirement (C-02, C-03, or C-04). |
| C-14 | Incumbent baseline anchoring         | depth       | At least one recovery prescription from C-08 explicitly names the pre-automation operational process (the process that existed before the pipeline) as the default fallback, grounded in the domain scenario (e.g., "manual AP clerk reconciliation," "manual inventory count process"). Generic terms such as "manual review" or "human intervention" without a named operational process do not qualify. |

---

## Changelog

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-15 | Initial — 4 essential, 3 recommended, 2 aspirational |
| v2      | 2026-03-15 | Added C-10, C-11, C-12 from Round 2 excellence signals; aspirational weight adjusted to 2 pts/criterion |
| v3      | 2026-03-15 | Added C-13, C-14 from Round 3 excellence signals; C-13 from V-02/V-03 structural table and gate enforcement pattern; C-14 from V-04 incumbent baseline anchoring pattern; aspirational weight now 10/9 per criterion |
```

---

**Source mapping for the two new criteria:**

| New ID | Source variants | What they demonstrated | Why aspirational not essential |
|--------|-----------------|------------------------|-------------------------------|
| C-13 | V-02 (boundary + schema-diff tables, "blank cell = structural gap"), V-03 (inline boundary gate, "omission is a protocol violation") | Structural layout enforces completeness — gaps cannot be hidden in prose | C-02/C-03/C-04 already require the *content*; tables and gates are a quality amplifier, not the baseline |
| C-14 | V-04 (C-08 recovery requires "Operations INCUMBENT BASELINE as identified fallback"; C-09 trade-off grounds comparison against INCUMBENT BASELINE total latency) | Pre-automation process named explicitly as operational anchor for both recovery and trade-off | C-08 passes with any named mechanism and boundary; baseline anchoring deepens grounding but does not invalidate other valid recovery approaches |
