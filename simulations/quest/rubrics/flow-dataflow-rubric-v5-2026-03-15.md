Reading the scorecard carefully — two structural innovations appear in V-02 that aren't captured by any v4 criterion, plus V-01 surfaces a floor-level distinction worth naming explicitly.

**Round 5 Pattern 1 — Entity-at-risk annotation per boundary (V-02)**
The BOUNDARY TABLE gains an "Entity at Risk" column requiring a named domain entity at each boundary — extending C-07 (domain framing in chain) to per-boundary resolution. C-07 passes when entities appear *somewhere* in the trace; this requires them at each inter-stage junction.

**Round 5 Pattern 2 — Structured recovery audit table (V-02)**
Recovery prescriptions are organized as a pre-populated table (triggering condition | recovery mechanism | boundary reference), making missing C-08 entries structurally visible — a direct structural extension of C-13's principle into the recovery domain. C-13 covers C-02/C-03/C-04; this covers C-08.

**Round 5 Pattern 3 — Per-boundary latency column (V-02)**
The BOUNDARY TABLE carries a Boundary Latency column — extending C-05's per-stage latency mandate to per-boundary latency. Stage latency and boundary latency are independently observable.

All three are aspirational (not essential): V-01 through V-05 all clear essentials; the new patterns distinguish structural depth above the C-08/C-07/C-05/C-13 baseline already in place.

---

```markdown
---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 5
---

# flow-dataflow Rubric — v5

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

## Aspirational Criteria (weight: 10 pts total — 10/12 pts per criterion)

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

---

## Changelog

### v5 — Round 5 excellence signals

Three new aspirational criteria added from Round 5 scoring (V-02 patterns):

**Round 5 Pattern 1 — Entity-at-risk annotation per boundary (C-17, from V-02)**
V-02's BOUNDARY TABLE carries an "Entity at Risk" column that must name a domain
entity at each inter-stage boundary. C-07 passes when domain entities appear
anywhere in the trace; C-17 requires per-boundary resolution. Generic labels
disqualify. Aspirational, not essential: C-07 remains satisfiable without per-
boundary entity annotation, but the absence of a named entity at each boundary
is now a scorable structural gap.

**Round 5 Pattern 2 — Structured recovery audit table (C-18, from V-02)**
V-02 organizes all recovery prescriptions (C-08) as a pre-populated table with
triggering condition, recovery mechanism, and boundary reference columns. This
extends C-13's structural completeness principle into the recovery domain: a
missing recovery row becomes structurally visible rather than prose-buried.
C-13 covers C-02/C-03/C-04; C-18 covers C-08. Aspirational: strong prose
recovery still satisfies C-08, but the table form raises the precision bar.

**Round 5 Pattern 3 — Per-boundary latency annotation (C-19, from V-02)**
V-02's BOUNDARY TABLE includes a Boundary Latency column independently of the
per-stage latency required by C-05. Stage latency and boundary latency are
distinct observations: a stage may complete in milliseconds while the boundary
handoff (queue drain, network transfer, lock acquisition) dominates end-to-end
latency. Aspirational: C-05 remains satisfiable on stage latency alone, but
per-boundary latency is now a scorable depth signal.

---

### v4 — Round 4 excellence signals

**Round 4 Pattern 1 — Structured incumbent baseline table (C-15, from V-03, V-05)**
C-14 passes when a recovery prescription names the pre-automation process. V-03
and V-05 go further: the baseline itself is a formal table (4-col, named rows),
making it queryable and citation-ready. The table form is structurally distinct:
each manual step has an identifier that downstream recovery entries can reference
precisely.

**Round 4 Pattern 2 — Per-entry recovery-to-baseline citation (C-16, from V-03, V-05)**
C-14 requires at least one recovery entry to name a baseline process. V-03 and
V-05 require every recovery entry to cite a specific step from the baseline table.
Full traceability rather than a single anchor.
```
