Reading the scorecard carefully to identify what V-01 demonstrates beyond the existing criteria before writing the updated rubric.

The key new pattern in V-01 is structural: **"Every required output pre-declared as a named table"** — a complete table scaffold declared *before* the first stage trace begins, where no table may appear mid-trace without prior declaration. This is categorically distinct from C-13 (which only requires *at least one* table for a specific section) and from C-10 (which gates entity vocabulary). V-01 shows the scaffold itself functions as a protocol contract: every downstream cross-table reference (C-16, C-17, C-20, C-23) is navigable because the full table inventory was declared upfront.

That is the single new excellence pattern to promote to C-24.

```markdown
---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 9
---

# flow-dataflow Rubric — v9

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

| ID   | Criterion                               | Category    | Pass Condition |
|------|-----------------------------------------|-------------|----------------|
| C-08 | Recovery prescriptions                  | depth       | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion naming the mechanism and boundary. Generic advice does not qualify. |
| C-09 | Pattern trade-off analysis              | behavior    | A named alternative pattern with >=2 explicitly stated trade-off dimensions, at least one quantified or qualified in domain terms. |
| C-10 | Pre-trace entity inventory              | structure   | All in-scope domain entities are enumerated and named in a dedicated inventory step before the first stage is traced. The trace references only entities from this inventory. An entity introduced mid-trace without prior declaration fails. |
| C-11 | Systematic boundary labeling            | structure   | Every inter-stage boundary receives a named label (e.g., B1->2, B2->3) forming a complete inventory. C-02 and C-08 annotations reference these labels by name using the B[N]->[N+1] format explicitly. A labeled boundary with no corresponding annotation is a visible, scorable gap. |
| C-12 | Verified-unchanged schema assertion     | correctness | Any stage asserting no schema change must carry an explicit verification statement (e.g., "verified: no field added, removed, renamed, or retyped"). A bare "unchanged" with no verification claim fails. |
| C-13 | Structural completeness enforcement     | structure   | At least one mandatory section (boundary inventory, schema diffs, or loss points) is organized as a table or inline protocol gate where a missing entry is structurally visible — a blank cell, a missing row, or a missing gate block constitutes an explicit gap. Prose-only requirements do not qualify. The table or gate must map directly to a scorable requirement (C-02, C-03, or C-04). |
| C-14 | Incumbent baseline anchoring            | depth       | At least one recovery prescription from C-08 explicitly names the pre-automation operational process (the process that existed before the pipeline) as the default fallback, grounded in the domain scenario (e.g., "manual AP clerk reconciliation," "manual inventory count process"). Generic terms such as "manual review" or "human intervention" without a named operational process do not qualify. |
| C-15 | Structured incumbent baseline table     | structure   | The pre-automation operational process is presented as a named table with at minimum three columns: step identifier or name, responsible actor or role, and elapsed time or frequency. A prose paragraph or bullet list does not qualify. The table must be referenceable from recovery prescriptions by row — each step must have a name or identifier that downstream entries can cite individually. |
| C-16 | Full recovery-to-baseline traceability  | depth       | Every recovery prescription (C-08) cites a specific named step or row from the incumbent baseline (C-14 or C-15) as its fallback anchor. A prescription that names only the process category without a specific step identifier does not qualify. "At least one" citation (C-14 pass condition) is insufficient — all recovery entries must carry step-level citations. |
| C-17 | Entity-at-risk annotation per boundary  | coverage    | Every inter-stage boundary in the boundary inventory (C-11) carries an explicit named domain entity annotation identifying which entity is at risk of loss or corruption at that boundary. The entity must be drawn from the C-10 inventory or C-07 vocabulary. Generic labels ("data," "records," "payload") do not qualify. A boundary label with no entity-at-risk annotation fails. |
| C-18 | Structured recovery audit table         | structure   | All recovery prescriptions (C-08) are organized as a named table with at minimum three columns: triggering condition (the specific "no handling" annotation or named loss point being addressed), recovery mechanism, and the boundary or stage reference. A prose recovery section does not qualify. Every "no handling" annotation and every named loss point must have a corresponding row — a missing row is structurally visible as a gap, exactly as C-13 enforces for C-02/C-03/C-04. |
| C-19 | Typed stage-exit manifests              | structure   | At each stage exit, a typed manifest declares field count and key field type assertions using typed notation (e.g., `field_name: TYPE(precision)`). The manifest is the designated downstream authority: entity-at-risk field citations (C-17, C-20) and schema diff annotations (C-04) must be resolvable against manifest field names and types. A stage whose schema state is stated in prose only — without typed field assertions — does not qualify. A manifest that cannot be referenced by name from downstream annotations is not a typed manifest for this criterion. |
| C-20 | Field-level entity-at-risk traceability | coverage    | Entity-at-risk annotations (extending C-17) must name a specific entity AND a specific field from that entity's typed stage-exit manifest (C-19), using the format `entity.field_name — risk description`. A field citation not present in the corresponding manifest is an invalid citation. Entity-name-only annotations that satisfy the C-17 pass condition do not qualify for this criterion. |
| C-21 | Decomposed boundary latency             | depth       | Every inter-stage boundary in the boundary inventory (C-11) decomposes its latency into at minimum two named additive sub-components — Transport Latency and Processing Overhead — each in a separate column with an independent numeric value. A single aggregate "Boundary Latency" column does not qualify. "Negligible" is not an acceptable value; a numeric estimate in ms is required. The sum of sub-component columns must equal or account for any total latency stated in C-05 annotations. |
| C-22 | Cumulative SLA% with domination point   | depth       | The boundary inventory table carries two additional columns: "SLA% This Boundary" (the fraction of the total SLA budget consumed at this boundary alone) and "Cumulative SLA%" (the running total consumed through and including this boundary). A dedicated DOMINATION POINT statement follows the table, identifying the single boundary where the cumulative total first exceeds 50% of the SLA budget, the exact cumulative percentage at that boundary, and a one-sentence justification. A table with latency values but no percentage columns does not qualify. A domination point statement that names a boundary without citing the crossing percentage does not qualify. |
| C-23 | Structurally separate closure gate      | structure   | A dedicated closure gate section — structurally separate from the recovery audit table (C-18) and from all stage trace sections — performs a forward check confirming that every declared NH-NN and LP-NN identifier has exactly one corresponding row in the recovery audit table. The gate lists each identifier, its source boundary or stage, and a CLOSED / OPEN status. An identifier present in the boundary inventory or stage trace but absent from the recovery table must appear as OPEN in the gate. A recovery audit table that includes a summary count ("N of M rows covered") does not satisfy this criterion — a per-identifier status table is required. |
| C-24 | Pre-declared complete output scaffold   | structure   | Before the first stage trace entry, a dedicated scaffold section declares every output table that will appear in the response — by table number, table name, stated purpose, and which upstream tables it references. No table may appear for the first time mid-trace; any table not listed in the scaffold is an undeclared artifact and fails. The scaffold itself must be presented as a table or structured block where each row declares one output table. A prose list of table names does not qualify. The scaffold functions as the navigational contract for all cross-table references required by C-15, C-16, C-18, C-19, C-20, and C-23 — a cross-table citation that cannot be resolved by consulting the scaffold's declared table inventory is an invalid citation. |
```

---

**What changed in v9:**

C-24 promotes the V-01 axis — *table scaffolding imposed upfront* — to a scorable criterion. The key distinction from C-13 is directionality: C-13 requires *at least one* table for a specific section (backward-looking, permissive); C-24 requires the *complete set* of tables to be declared *before* any trace work begins (forward-looking, contractual). The scaffold also serves as the navigational anchor for all existing cross-table citation criteria (C-15, C-16, C-18, C-19, C-20, C-23), making those criteria stronger by requiring the reference target to be pre-declared rather than discovered.
