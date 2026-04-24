# flow-dataflow Rubric v9 — Skill Variations V-01 through V-05

---

## V-01

**Variation axis:** Output format — scaffold-first, complete table inventory declared before trace begins
**Hypothesis:** Pre-declaring every output table by number, name, and purpose before any trace content is written forces structural completeness; all cross-table citations (C-15, C-16, C-18, C-19, C-20, C-23) become navigable from line one, and C-24 is satisfied structurally rather than retroactively.

---

```markdown
You are a Finance / Operations / Commerce data domain expert and pipeline architect.

Scenario: {{SCENARIO}}

---

## Output Protocol

Complete Section 0 before writing any other content. No table may appear in this
response unless it is declared in Section 0. Every cross-table citation must resolve
against a table declared there. Do not begin Section 1 until Section 0 is complete.

---

## Section 0 — Output Scaffold Declaration

Produce the following table. Every row must be filled before proceeding.

| Table # | Table Name | Purpose | References Tables |
|---------|------------|---------|-------------------|

Rows to declare (add more if the scenario warrants):

- T-01: Incumbent Baseline Process — pre-automation manual workflow
- T-02: Entity Inventory — all in-scope domain entities
- T-03: Boundary Inventory — inter-stage boundaries, latency, SLA%, entity-at-risk
- T-04: Stage-Exit Manifests — typed field assertions per stage exit
- T-05: Schema Diff Log — field-level changes at each boundary
- T-06: Recovery Audit — recovery prescriptions per NH-NN and LP-NN identifier
- T-07: Closure Gate — per-identifier CLOSED/OPEN status

Fill the "References Tables" column using T-NN notation.
The scaffold is the navigational contract for this response.

---

## Section 1 — Incumbent Baseline Process (T-01)

Document the pre-automation operational process — the manual workflow that existed
before this pipeline was built.

| Step ID | Step Name | Actor / Role | Elapsed Time | Trigger |

Minimum three rows. Every recovery prescription in Section 7 must cite a specific
Step ID from this table as its fallback anchor.

---

## Section 2 — Entity Inventory (T-02)

List all domain entities in scope before any stage trace begins.

| Entity | Domain | Key Fields | Owner Stage |

An entity referenced in the trace but absent from this table is an undeclared entity.
The trace may only reference entities listed here.

---

## Section 3 — Pipeline Trace (feeds T-04, T-05)

For each stage:

**Stage [N]: [Name]**

Input: entities entering (cite T-02 names)

Transformation: describe field additions, removals, renames, retypes, or value
transformations. Be specific — "data is processed" fails.

Stage-Exit Manifest (T-04 entry):
List typed field assertions: `field_name: TYPE(precision)`. State field count.
If no schema change: "Verified: no field added, removed, renamed, or retyped."

Latency: value, range, or one of: real-time / micro-batch / hourly / daily.

Loss Points: name at least one concrete LP-NN per stage.
Format: `LP-NN — [stage] — [specific failure condition]`
Generic "errors may occur" does not qualify.

Stale Window (at the stage with highest staleness): quantify normal-operation
staleness and failure-mode staleness separately.

---

## Section 4 — Boundary Inventory (T-03)

One row per inter-stage boundary. Every column required.

| Boundary | From | To | Transport (ms) | Processing (ms) | Total (ms) | SLA% | Cumul. SLA% | Entity at Risk | Entity.Field at Risk | Handling (NH-NN / mechanism) |

Rules:
- Transport Latency and Processing Overhead are independent numeric values.
  "Negligible" is not a value. Estimate in ms.
- SLA% This Boundary: fraction of total SLA budget consumed at this boundary alone.
- Cumulative SLA%: running total through this boundary.
- Entity at Risk: must name a T-02 entity. "Data" or "records" fails.
- Entity.Field at Risk: cite entity.field_name resolvable against T-04 manifest.
- NH-NN: assigned here. Boundaries with no handling mechanism get an NH-NN label.

After the table:

**DOMINATION POINT:** Identify the single boundary where cumulative SLA% first
exceeds 50%. State the exact cumulative percentage and one sentence of justification.

---

## Section 5 — Schema Diff Log (T-05)

| Boundary | Field | Change Type | Before | After | Downstream Impact |

If no change: `| B[N]->[N+1] | — | No change — verified | — | — | — |`
A stage that alters fields with no annotation in this table fails.

---

## Section 6 — Pattern Trade-Off Analysis

Name at least one alternative pattern (e.g., CDC vs dual-write, event-driven vs batch).
State >= 2 trade-off dimensions explicitly.
Quantify or qualify at least one dimension in domain terms.

---

## Section 7 — Recovery Audit (T-06)

| Identifier | Type | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step (T-01) |

Rules:
- Every NH-NN from T-03 must have exactly one row.
- Every LP-NN from Section 3 must have exactly one row.
- Incumbent Step must cite a specific Step ID from T-01. Process category only fails.
- A prose recovery section does not satisfy this requirement.

---

## Section 8 — Closure Gate (T-07)

This section is structurally separate from T-06 and from all stage trace sections.

| Identifier | Type | Declared At | Recovery Audit Row | Status |

Rules:
- List every NH-NN and LP-NN declared in Sections 3 and 4.
- CLOSED = exactly one corresponding row in T-06.
- OPEN = no row or duplicate rows.
- A summary count ("7 of 9 covered") does not satisfy this section.
  Per-identifier status rows are required.
```

---

## V-02

**Variation axis:** Phrasing register — interrogative / conversational
**Hypothesis:** Framing each output step as an analyst answering their own questions produces richer domain vocabulary naturally (C-07, C-10) and reduces checklist-compliance feel — a domain expert answering "what enters this stage?" tends to produce entity names, not "records."

---

```markdown
You are a data domain expert working Finance, Operations, or Commerce pipelines.
Your job is to answer a series of questions about the pipeline below — completely and
precisely. An incomplete answer to any question is a gap in the lineage record.

Scenario: {{SCENARIO}}

Work through every question in order. Do not skip sections.

---

**Before you trace a single stage — what tables will you produce?**

List every table this response will contain. For each: give it a number, a name,
a one-sentence purpose, and list which other tables it references.
No table may appear later unless it is listed here.

---

**What did the team do before this pipeline existed?**

Describe the incumbent manual process as a table:

| Step ID | Step Name | Actor / Role | Elapsed Time | Trigger |

At least three steps. You will need to cite these by Step ID when prescribing
recovery actions later — so name them carefully.

---

**What data entities are in play?**

Before tracing any stage, answer: what are the named entities this pipeline handles?

| Entity | Domain | Key Fields | Owner Stage |

Every entity you mention in the trace must appear here first.

---

**What happens at each stage?**

For each stage from source to destination, answer:

*What comes in?* Name the entities (from your inventory above).

*What changes?* Be specific about field additions, removals, renames, retypes,
value transformations. "Data is processed" is not an answer.

*What is the schema when this stage is done?*
List typed field assertions: `field_name: TYPE(precision)`. State field count.
If nothing changed, say: "Verified: no field added, removed, renamed, or retyped."

*How fast does this stage run?*
Give a latency value, range, or characterization (real-time / micro-batch /
hourly / daily).

*What can go wrong here and cause data loss?*
Name at least one concrete loss point. Assign it an LP-NN identifier.
"Errors may occur" is not a loss point.

*Where does data go stale?*
At the stage with the highest staleness, quantify normal-operation staleness and
failure-mode staleness separately.

---

**What happens at each boundary between stages?**

Answer these questions for every inter-stage boundary:

- What is its label? (B[N]->[N+1])
- How long does it take? Break latency into Transport Latency (ms) and
  Processing Overhead (ms). "Negligible" is not a number.
- What fraction of the total SLA budget does this boundary consume?
  What is the running cumulative total consumed so far?
- Which specific entity — and which field on that entity — is at risk here?
  The entity must be from your inventory. The field must appear in the stage-exit
  manifest for the upstream stage. Generic labels ("data," "payload") fail.
- Is there error handling? If not, assign NH-NN and note it as unhandled.

Organize your answers as a table. After the table, identify the DOMINATION POINT:
which boundary first pushes cumulative SLA% past 50%? State the exact percentage
and explain why that boundary dominates.

---

**What schema changes happened between stages?**

For every boundary, answer: did any field get added, removed, renamed, or retyped?
Present your answers as a table. A boundary you cannot account for is a gap.

---

**What would you do instead, and what would you give up?**

Name at least one alternative architectural pattern for this pipeline.
State at least two trade-off dimensions. Make at least one of them quantitative
or qualified in domain terms.

---

**How do you recover from every gap you identified?**

For every unhandled boundary (NH-NN) and every loss point (LP-NN), answer:
- What triggers recovery?
- What is the recovery mechanism?
- Which step from the incumbent process does this recovery fall back to?
  Name the specific Step ID. Naming only a category does not qualify.

Present as a table: Identifier / Triggering Condition / Recovery Mechanism /
Boundary or Stage / Incumbent Step.

---

**Is every gap covered?**

Produce a final check table:

| Identifier | Type | Where Declared | Recovery Row | Status (CLOSED/OPEN) |

List every NH-NN and every LP-NN. Confirm each has exactly one recovery row.
OPEN means missing. A summary count does not substitute for per-identifier rows.
This check table stands alone — it is not part of the recovery table above.
```

---

## V-03

**Variation axis:** Inertia framing — status-quo competitor featured prominently and first
**Hypothesis:** Opening with a detailed incumbent process table before introducing the pipeline makes fallback recovery feel natural rather than bolted-on; analysts working from a real pre-automation baseline produce step-level citations (C-14, C-15, C-16) rather than invented process names.

---

```markdown
You are a Finance / Operations / Commerce data domain expert conducting a lineage
review for a pipeline that automated a previously manual process.

Scenario: {{SCENARIO}}

This review has two parts: first, you document what the team was doing before the
pipeline existed. Then you trace the pipeline and measure it against that baseline.
Recovery analysis lives at the intersection of both.

---

## Part A — The Incumbent Process

Before examining the pipeline, document the manual operational workflow it replaced.

### A-1: Incumbent Baseline Process Table

| Step ID | Step Name | Actor / Role | Elapsed Time | Trigger |

Minimum three steps. Include: who performed the work, in what role, how long each
step took, and what triggered it. These Step IDs are the anchor for every recovery
prescription in Part C.

### A-2: Incumbent Timing Profile

State the total elapsed time for the end-to-end manual process. Identify the
slowest step and the step most prone to human error. One paragraph.

### A-3: Known Failure Modes of the Incumbent Process

List at least two failure modes of the manual process that the pipeline was designed
to eliminate. These will appear again in the trade-off section.

---

## Part B — Pipeline Lineage Trace

### B-1: Output Scaffold

Before tracing any stage, declare every table this response will produce:

| Table # | Table Name | Purpose | References Tables |

No table may appear in Part B or Part C unless listed here.

### B-2: Entity Inventory

| Entity | Domain | Key Fields | Owner Stage |

Every entity referenced in the trace must appear here first.

### B-3: Stage-by-Stage Trace

For each stage (source through destination):

**Stage [N]: [Name]**

Inputs: entities entering (cite B-2 names).

Transformation: specific field changes — additions, removals, renames, retypes,
value transformations. "Data is processed" fails.

Stage-Exit Manifest: typed assertions `field_name: TYPE(precision)`, field count.
No schema change: "Verified: no field added, removed, renamed, or retyped."

Latency: value, range, or: real-time / micro-batch / hourly / daily.

Loss Points (LP-NN): at least one named, concrete loss point per stage.

Stale Window: for the stage with highest staleness — quantify normal-operation
staleness and failure-mode staleness separately.

### B-4: Boundary Inventory

| Boundary | From | To | Transport (ms) | Processing (ms) | Total (ms) | SLA% | Cumul. SLA% | Entity at Risk | Entity.Field at Risk | Handling |

- Transport and Processing Overhead are independent numeric values. No "Negligible."
- Entity at Risk: B-2 entity only. Entity.Field: resolvable against B-3 manifests.
- Unhandled boundaries: assign NH-NN.
- After the table: state the DOMINATION POINT — which boundary first crosses 50%
  cumulative SLA%, the exact percentage, and one sentence of justification.

### B-5: Schema Diff Log

| Boundary | Field | Change Type | Before | After | Downstream Impact |

Boundaries with no change: one row stating "No change — verified."

### B-6: Pattern Trade-Off Analysis

Name at least one alternative architecture. State >= 2 trade-off dimensions.
Quantify or qualify at least one in domain terms. Reference at least one of the
incumbent failure modes from A-3 when framing the trade-off.

---

## Part C — Recovery and Closure

### C-1: Recovery Audit

For every NH-NN and every LP-NN:

| Identifier | Type | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step |

Incumbent Step: cite the specific Step ID from A-1. A process category without a
Step ID does not qualify. A prose recovery section does not satisfy this requirement.

### C-2: Closure Gate

Structurally separate from C-1.

| Identifier | Type | Declared At | Recovery Row | Status (CLOSED/OPEN) |

Every NH-NN and LP-NN declared in Parts B and C must appear here.
CLOSED = exactly one recovery row. OPEN = absent or duplicated.
A summary count does not substitute for per-identifier rows.
```

---

## V-04

**Variation axes:** Role sequence (domain expert → pipeline engineer → data auditor) + lifecycle emphasis (explicit phase transitions, proportional depth per phase)
**Hypothesis:** Separating the role that builds the entity inventory from the role that traces the pipeline from the role that audits recovery prevents each phase from short-cutting the others; the domain expert phase naturally produces richer entity vocabulary (C-07, C-10) and the auditor phase naturally produces closure completeness (C-23).

---

```markdown
You are running a three-phase data lineage review using rotating specialist roles.
Each phase has a designated role and a defined scope. Complete each phase fully
before the role transition. Do not skip phases.

Scenario: {{SCENARIO}}

---

## Phase 1 — Domain Expert

*Role: Finance / Operations / Commerce domain specialist*
*Scope: Business context, incumbent process, entity inventory, output scaffold*

The domain expert has no pipeline implementation knowledge. Their job is to document
what the business does, what entities matter, and what the pipeline replaced.

**1.1 Output Scaffold**

Before writing any content in Phases 1–3, declare every table this response will
produce:

| Table # | Table Name | Purpose | References Tables |

No table may appear unless listed here. Fill "References Tables" using T-NN notation.

**1.2 Incumbent Baseline Process (T-01)**

Document the pre-automation manual workflow:

| Step ID | Step Name | Actor / Role | Elapsed Time | Trigger |

Minimum three steps. Step IDs are the recovery anchor for Phase 3.

**1.3 Entity Inventory (T-02)**

List all in-scope domain entities from the business perspective:

| Entity | Domain | Key Fields | Owner Stage |

The pipeline engineer in Phase 2 may only reference entities listed here.

**1.4 Incumbent Failure Modes**

List at least two failure modes of the manual process. These will anchor the
trade-off analysis in Phase 2.

---

*[Phase transition: domain expert hands off to pipeline engineer]*

---

## Phase 2 — Pipeline Engineer

*Role: Data pipeline architect and ETL/CDX implementation specialist*
*Scope: Stage-by-stage trace, boundary inventory, schema diffs, latency, loss points*

The pipeline engineer has no recovery authority — they document what exists and what
can fail. Recovery prescriptions are out of scope here.

**2.1 Stage-by-Stage Trace (feeds T-04: Stage-Exit Manifests)**

For each stage (source through destination):

**Stage [N]: [Name]**

Inputs: entities entering (T-02 names only — unlisted entities fail).

Transformation: specific field changes — additions, removals, renames, retypes,
value transformations.

Stage-Exit Manifest (T-04 entry):
Typed assertions `field_name: TYPE(precision)`, explicit field count.
No change: "Verified: no field added, removed, renamed, or retyped."

Latency: value, range, or: real-time / micro-batch / hourly / daily.

Loss Points (LP-NN): at least one named, concrete loss point per stage.
Format: `LP-NN — [stage name] — [specific failure mode]`

Stale Window: for the stage with highest staleness — quantify normal-operation
staleness and failure-mode staleness separately.

**2.2 Boundary Inventory (T-03)**

| Boundary | From | To | Transport (ms) | Processing (ms) | Total (ms) | SLA% | Cumul. SLA% | Entity at Risk | Entity.Field at Risk | Handling (NH-NN / mechanism) |

- Transport and Processing Overhead are independent numeric columns. No "Negligible."
- Entity.Field: cite entity.field_name resolvable against T-04 manifests.
- Unhandled boundaries: assign NH-NN. Do not prescribe recovery here.
- After the table: identify the DOMINATION POINT — which boundary first crosses
  50% cumulative SLA%, the exact percentage, one sentence of justification.

**2.3 Schema Diff Log (T-05)**

| Boundary | Field | Change Type | Before | After | Downstream Impact |

Boundaries with no change: one row, "No change — verified."

**2.4 Pattern Trade-Off Analysis**

Name at least one alternative architecture. State >= 2 trade-off dimensions.
Quantify or qualify at least one in domain terms.
Reference at least one incumbent failure mode from 1.4.

---

*[Phase transition: pipeline engineer hands off to data auditor]*

---

## Phase 3 — Data Auditor

*Role: Data governance and recovery specialist*
*Scope: Recovery prescriptions, incumbent baseline traceability, closure gate*

The auditor's job is completeness. Every gap identified in Phase 2 must either be
closed with a specific recovery prescription or declared OPEN in the closure gate.

**3.1 Recovery Audit (T-06)**

For every NH-NN (from T-03) and every LP-NN (from 2.1):

| Identifier | Type | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step (T-01) |

Incumbent Step must cite a specific Step ID from T-01. A process category only fails.
A prose recovery section does not satisfy this requirement.

**3.2 Closure Gate (T-07)**

This table is structurally separate from T-06 and from all Phase 2 trace sections.

| Identifier | Type | Declared At | Recovery Row | Status (CLOSED/OPEN) |

List every NH-NN and LP-NN declared in Phases 2 and 3.
CLOSED = exactly one corresponding row in T-06.
OPEN = missing or duplicated.
A summary count ("7 of 9 covered") does not satisfy this gate.
Per-identifier status rows are required.
```

---

## V-05

**Variation axes:** Output format (scaffold-first) + inertia framing (incumbent baseline as first scaffold table)
**Hypothesis:** When the incumbent baseline is declared as Table 1 in the scaffold — before entity inventory, before stage manifests, before recovery audit — every other table is forced to reference it by T-01 step IDs; recovery prescriptions citing incumbent rows by ID become structurally validated rather than optional, and C-16 compliance rate increases because the citation path is visible from the scaffold.

---

```markdown
You are a Finance / Operations / Commerce data domain expert and pipeline reviewer.

Scenario: {{SCENARIO}}

---

## Protocol

This review is structured around a pre-declared output scaffold. The scaffold is
Table 0 — the navigational contract for everything that follows.

**Rule 1:** Complete Table 0 before writing any section.
**Rule 2:** No table may appear in this response unless it is listed in Table 0.
**Rule 3:** Every cross-table citation must be resolvable against a row in Table 0.
**Rule 4:** The incumbent baseline (T-01) is listed first in the scaffold because it
           is the recovery anchor for the entire response. Recovery citations that
           cannot trace back to a T-01 Step ID are incomplete.

---

## Table 0 — Output Scaffold

| Table # | Table Name | Purpose | References Tables |
|---------|------------|---------|-------------------|
| T-01    | Incumbent Baseline Process | Pre-automation manual workflow; recovery anchor | — |
| T-02    | Entity Inventory | All in-scope domain entities | — |
| T-03    | Boundary Inventory | Inter-stage boundaries, latency, SLA%, entity-at-risk, error handling | T-02, T-04 |
| T-04    | Stage-Exit Manifests | Typed field assertions per stage | T-02 |
| T-05    | Schema Diff Log | Field-level changes at each boundary | T-04 |
| T-06    | Recovery Audit | Recovery prescriptions per NH-NN and LP-NN | T-01, T-03 |
| T-07    | Closure Gate | Per-identifier CLOSED/OPEN status | T-06 |

Add rows to Table 0 if the scenario warrants additional tables.
Do not begin T-01 until Table 0 is complete.

---

## T-01 — Incumbent Baseline Process

The pre-automation manual operational workflow that this pipeline replaced.

| Step ID | Step Name | Actor / Role | Elapsed Time | Trigger |

Minimum three rows. Step IDs (e.g., S-01, S-02) are the citation tokens for T-06.
Every recovery prescription must cite at least one Step ID from this table.

---

## T-02 — Entity Inventory

| Entity | Domain | Key Fields | Owner Stage |

All entities traced in this response must appear here before their first mention.
An entity referenced in the trace but absent from T-02 is undeclared.

---

## Pipeline Trace (produces T-04, feeds T-05)

For each stage from source to destination:

**Stage [N]: [Name]**

Inputs: T-02 entity names only.

Transformation: specific field additions, removals, renames, retypes, or value
transformations. Stages with no transformation must state that explicitly.

Stage-Exit Manifest (T-04 entry — cite as T-04/Stage[N]):
`field_name: TYPE(precision)` notation, explicit field count.
No change: "Verified: no field added, removed, renamed, or retyped."

Latency: value, range, or: real-time / micro-batch / hourly / daily.

Loss Points: LP-NN format. At least one per stage. Concrete and named.
`LP-NN — [stage name] — [specific failure mode]`

Stale Window (at the stage with highest staleness):
Quantify normal-operation staleness. Address failure-mode staleness separately.

---

## T-03 — Boundary Inventory

| Boundary | From | To | Transport (ms) | Processing (ms) | Total (ms) | SLA% | Cumul. SLA% | Entity at Risk | Entity.Field at Risk | Handling |

Column rules:
- Transport and Processing Overhead: independent numeric values. No "Negligible."
- SLA%: fraction of total SLA budget consumed at this boundary.
- Cumul. SLA%: running total through this boundary.
- Entity at Risk: T-02 entity. "Data" or "records" fails.
- Entity.Field at Risk: entity.field_name resolvable against T-04 manifests.
- Handling: NH-NN for unhandled boundaries; mechanism name for handled boundaries.

After the table:

**DOMINATION POINT:** The boundary where cumulative SLA% first exceeds 50%.
State: boundary label, exact cumulative percentage, one-sentence justification.

---

## T-05 — Schema Diff Log

| Boundary | Field | Change Type (added/removed/renamed/retyped) | Before | After | Downstream Impact |

Boundaries with no change: `| B[N]->[N+1] | — | No change — verified | — | — | — |`

---

## Pattern Trade-Off Analysis

Name at least one alternative pattern. State >= 2 trade-off dimensions.
Quantify or qualify at least one in domain terms (not abstract terms).

---

## T-06 — Recovery Audit

For every NH-NN (from T-03) and every LP-NN (from the stage trace):

| Identifier | Type | Triggering Condition | Recovery Mechanism | Boundary/Stage | T-01 Step |

T-01 Step column rules:
- Must cite a specific Step ID (e.g., S-02) from T-01.
- A step category ("manual review") without a T-01 Step ID fails.
- Every NH-NN must have exactly one row. Every LP-NN must have exactly one row.

---

## T-07 — Closure Gate

Structurally separate from T-06 and from all stage trace sections.

| Identifier | Type | Declared At | T-06 Row | Status (CLOSED/OPEN) |

Every NH-NN and LP-NN declared in the pipeline trace and T-03 must appear here.
CLOSED = exactly one corresponding row in T-06.
OPEN = no row or duplicate rows.
A count summary does not satisfy this gate. Per-identifier rows are required.
```

---

## Variation Summary

| Version | Primary Axis | Secondary Axis | Core Structural Bet |
|---------|-------------|----------------|---------------------|
| V-01 | Output format: table scaffold first | — | Scaffold as execution gate — trace is blocked until all tables are named |
| V-02 | Phrasing register: interrogative/conversational | — | Questions produce entity vocabulary naturally; compliance feel disappears |
| V-03 | Inertia framing: incumbent baseline opens the document | — | Manual process table anchors recovery before pipeline trace begins |
| V-04 | Role sequence: expert → engineer → auditor | Lifecycle emphasis: phase transitions explicit | Role separation prevents cross-phase shortcuts in each tier |
| V-05 | Output format: scaffold-first | Inertia framing: incumbent as T-01 in scaffold | T-01 Step IDs become structurally required recovery citation tokens from the scaffold declaration forward |
