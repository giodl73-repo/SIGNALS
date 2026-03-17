Reading the scorecard carefully — the Axis Coverage Recap surface-labels five axes, three of which are not captured by any v5 criterion, and one (decomposed boundary latency in V-03's 7-column table) extends C-19 in a way worth naming distinctly.

**Round 6 Pattern 1 — Systematic trigger ID scheme (V-01, V-05)**
NH-NN and LP-NN identifiers are assigned at definition and cited by number in all downstream recovery references. C-02/C-03 require annotations; C-08/C-18 require paired prescriptions. Neither requires a stable identifier that makes the link machine-checkable across sections.

**Round 6 Pattern 2 — Stage-exit entity declaration (V-02, V-05)**
Every stage explicitly declares which entities it emits at exit. C-17 requires an entity-at-risk per boundary drawn from inventory or vocabulary; V-02/V-05 strengthen this by requiring the citation to trace to the upstream stage-exit declaration, not just the global inventory — tighter provenance than C-17 enforces alone.

**Round 6 Pattern 3 — Decomposed boundary latency (V-03)**
The 7-column boundary table breaks boundary latency into at least two additive components. C-19 requires a latency annotation per boundary (value, range, or characterization); this requires that annotation to be decomposed into sub-components that sum to the total.

**Round 6 Pattern 4 — Verification index (V-04, V-05)**
A dedicated cross-reference table maps every schema verification claim, entity-at-risk annotation, and recovery baseline citation to its source evidence row. C-13 enforces structural visibility of gaps within a single table; this is a meta-structural surface that makes gaps visible across all tables simultaneously.

---

```markdown
---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 6
---

# flow-dataflow Rubric — v6

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

## Aspirational Criteria (weight: 10 pts total — 10/N_aspirational pts each)

| ID   | Criterion                              | Category    | Pass Condition |
|------|----------------------------------------|-------------|----------------|
| C-08 | Recovery prescriptions                 | depth       | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion naming the mechanism and boundary. Generic advice does not qualify. |
| C-09 | Pattern trade-off analysis             | behavior    | A named alternative pattern with >=2 explicitly stated trade-off dimensions, at least one quantified or qualified in domain terms. |
| C-10 | Pre-trace entity inventory             | structure   | All in-scope domain entities are enumerated and named in a dedicated inventory step before the first stage is traced. The trace references only entities from this inventory. An entity introduced mid-trace without prior declaration fails. |
| C-11 | Systematic boundary labeling           | structure   | Every inter-stage boundary receives a named label (e.g., B1->2, B2->3) forming a complete inventory. C-02 and C-08 annotations reference these labels by name using the B[N]->[N+1] format explicitly. A labeled boundary with no corresponding annotation is a visible, scorable gap. |
| C-12 | Verified-unchanged schema assertion    | correctness | Any stage asserting no schema change must carry an explicit verification statement (e.g., "verified: no field added, removed, renamed, or retyped"). A bare "unchanged" with no verification claim fails. |
| C-13 | Structural completeness enforcement    | structure   | At least one mandatory section (boundary inventory, schema diffs, or loss points) is organized as a table or inline protocol gate where a missing entry is structurally visible — a blank cell, a missing row, or a missing gate block constitutes an explicit gap. Prose-only requirements do not qualify. The table or gate must map directly to a scorable requirement (C-02, C-03, or C-04). |
| C-14 | Incumbent baseline anchoring           | depth       | At least one recovery prescription from C-08 explicitly names the pre-automation operational process (the process that existed before the pipeline) as the default fallback, grounded in the domain scenario (e.g., "manual AP clerk reconciliation," "manual inventory count process"). Generic terms such as "manual review" or "human intervention" without a named operational process do not qualify. |
| C-15 | Structured incumbent baseline table    | structure   | The pre-automation operational process is presented as a named table with at minimum three columns: step identifier or name, responsible actor or role, and elapsed time or frequency. A prose paragraph or bullet list does not qualify. The table must be referenceable from recovery prescriptions by row — each step must have a name or identifier that downstream entries can cite individually. |
| C-16 | Full recovery-to-baseline traceability | depth       | Every recovery prescription (C-08) cites a specific named step or row from the incumbent baseline (C-14 or C-15) as its fallback anchor. A prescription that names only the process category without a specific step identifier does not qualify. "At least one" citation (C-14 pass condition) is insufficient — all recovery entries must carry step-level citations. |
| C-17 | Entity-at-risk annotation per boundary | coverage    | Every inter-stage boundary in the boundary inventory (C-11) carries an explicit named domain entity annotation identifying which entity is at risk of loss or corruption at that boundary. The entity must be drawn from the C-10 inventory or C-07 vocabulary. Generic labels ("data," "records," "payload") do not qualify. A boundary label with no entity-at-risk annotation fails. |
| C-18 | Structured recovery audit table        | structure   | All recovery prescriptions (C-08) are organized as a named table with at minimum three columns: triggering condition (the specific "no handling" annotation or named loss point being addressed), recovery mechanism, and the boundary or stage reference. A prose recovery section does not qualify. Every "no handling" annotation and every named loss point must have a corresponding row — a missing row is structurally visible as a gap, exactly as C-13 enforces for C-02/C-03/C-04. |
| C-19 | Per-boundary latency annotation        | depth       | The boundary inventory (C-11) includes a latency annotation for each boundary — value, range, or characterization — distinct from the per-stage latency required by C-05. A boundary with no latency annotation fails. A boundary latency column embedded in the boundary table satisfies this criterion; a standalone prose note per boundary also qualifies. |
| C-20 | Systematic trigger ID scheme           | structure   | Every "no handling" annotation (C-02) and every named loss point (C-03) receives a sequential identifier at definition — NH-01, NH-02, … for no-handling entries and LP-01, LP-02, … for loss points. All downstream references in recovery prescriptions (C-08), recovery audit table rows (C-18), and verification entries cite these identifiers by number rather than by description. A recovery entry that references an annotation by prose description without a corresponding NH-NN or LP-NN identifier fails. A recovery audit table row with no trigger ID in its triggering-condition cell fails. |
| C-21 | Stage-exit entity declaration          | coverage    | Every stage in the lineage carries an explicit exit declaration naming which domain entities it produces or passes forward, positioned at stage exit and distinct from the global C-10 inventory. Entity names must match the C-10 inventory exactly. C-17 entity-at-risk annotations at each downstream boundary must cite the upstream stage-exit declaration as their source — citing only the global inventory (C-10) without tracing through the stage-exit declaration does not qualify. A boundary whose entity-at-risk annotation cannot be traced to the immediately upstream stage-exit declaration fails. |
| C-22 | Decomposed boundary latency            | depth       | The per-boundary latency annotation required by C-19 is broken into at least two named, additive sub-components (e.g., queue wait time + transformation processing time; network transit + write confirmation latency). A single aggregate latency figure, even if precise, does not qualify. The decomposition must be presented as an explicit breakdown — labeled sub-components that sum to the total boundary latency — either as columns within the boundary table or as a structured annotation block per boundary. |
| C-23 | Verification index                     | structure   | A dedicated, named verification index — a referenceable cross-reference table — is present as a top-level section. It must map every schema verification claim (C-12), every entity-at-risk annotation (C-17), and every recovery baseline citation (C-16) to its source evidence by section identifier and row or line reference. The index must contain at minimum two columns: claim type and source reference. A verification claim that appears in the trace body but has no corresponding entry in the index is a structurally visible gap. The index must cover all three claim types; an index that covers only one or two types does not pass. |
```
