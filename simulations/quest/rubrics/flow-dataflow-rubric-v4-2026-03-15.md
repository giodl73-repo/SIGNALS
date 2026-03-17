The axis coverage table is the signal source. Two patterns emerge above v3 baseline, visible from two columns that didn't exist in Round 3:

**Round 4 Pattern 1 — Structured incumbent baseline table (V-03, V-05)**
C-14 passes when a recovery prescription names the pre-automation process. V-03 and V-05 go further: the baseline itself is a formal table (4-col, named rows) — making it queryable and citation-ready rather than a prose section. V-02's baseline is also a prose section. The table form is structurally distinct: each manual step has an identifier that downstream recovery entries can reference precisely.

**Round 4 Pattern 2 — Per-entry recovery-to-baseline citation (V-03, V-05)**
The axis column "Per-row citation requirement" shows V-03 and V-05 as "yes (Manual Step value)" vs V-02's "no." C-14 requires at least one recovery entry to name a baseline process. These variants require every recovery entry to cite a specific step from the baseline table — full traceability rather than a single anchor.

**Why aspirational, not essential:**
The structured baseline table amplifies C-14 but doesn't invalidate responses that name the process in prose. Per-entry citation extends C-08 + C-14 pass conditions without making them fail — a response with strong baseline naming but no per-row step IDs still satisfies both parent criteria.

---

```markdown
---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 4
---

# flow-dataflow Rubric — v4

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
| C-15 | Structured incumbent baseline table  | structure   | The pre-automation operational process is presented as a named table with at minimum three columns: step identifier or name, responsible actor or role, and elapsed time or frequency. A prose paragraph or bullet list does not qualify. The table must be referenceable from recovery prescriptions by row — each step must have a name or identifier that downstream entries can cite individually. |
| C-16 | Full recovery-to-baseline traceability | depth     | Every recovery prescription (C-08) cites a specific named step or row from the incumbent baseline (C-14 or C-15) as its fallback anchor. A prescription that names only the process category without a specific step identifier does not qualify. "At least one" citation (C-14 pass condition) is insufficient — all recovery entries must carry step-level citations. |

---

## Changelog

### v4 — 2026-03-15

Two new aspirational criteria extracted from Round 4 axis coverage signals.

**C-15: Structured incumbent baseline table**
V-03 and V-05 present the baseline as a 4-column named table (step, actor, duration, identifier) rather than a prose section. V-02's C-14 pass uses a prose section that names manual steps; the table form makes each step individually referenceable. This is a quality amplifier for C-14, not a C-14 replacement — prose baseline anchoring still satisfies C-14. Aspirational because C-14 pass conditions remain valid without it.

**C-16: Full recovery-to-baseline traceability**
The "Per-row citation requirement" axis column shows V-03 and V-05 as "yes (Manual Step value)" — every recovery entry in the recovery table cites a specific step from the baseline, not merely the process name. V-02 requires only "at least one entry" to reference a named step (C-14 pass). V-03/V-05 extend this to full-row coverage. Aspirational because C-08 and C-14 pass without per-entry step IDs; this criterion rewards exhaustive traceability.

### v3 — 2026-03-15

Two new aspirational criteria extracted from Round 3 scorecard excellence signals.

**C-13: Structural completeness enforcement**
V-02 and V-03 (96 pts) used tables and inline boundary gates to make omissions structurally visible — blank cell or missing gate block constitutes an explicit gap. V-01 and V-04 embed requirements in prose where gaps can be buried. Amplifies C-02/C-03/C-04 without invalidating prose-based responses that meet those conditions.

**C-14: Incumbent baseline anchoring**
V-04 distinguished itself on C-08 and C-09 by naming the pre-automation operational process as the explicit fallback and comparison anchor. Generic recovery terms without grounding in a named baseline do not qualify. Deepens C-08 and C-09 beyond their pass conditions but does not invalidate responses meeting those conditions by other means.
```

---

Two new criteria, reasoning documented. C-15 and C-16 are structurally tight: C-15 upgrades the baseline artifact from prose to table; C-16 upgrades baseline citation from one-to-many to one-to-one. A response can pass C-14 without C-15, and pass C-16 only if it has a citable baseline (C-14 or C-15) — but C-16 doesn't formally depend on C-15 passing since a well-labeled prose baseline with named steps can also satisfy it.
