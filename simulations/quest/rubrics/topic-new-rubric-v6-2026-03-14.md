Written to `simulations/quest/rubrics/topic-new-rubric-v6-2026-03-14.md`.

---

## Changes: v5 → v6

Two new aspirational criteria extracted from V-03 (R6):

**C-21 — Per-phase exit gates at every phase boundary** (`structure`)
Sharpens C-11. C-11 requires one pre-write checkpoint, which catches the final silent skip. C-21 requires a gate at *every* phase boundary — so mid-pipeline silent advancement is also structurally impossible. V-03's six-phase lifecycle demonstrated this: each phase had a named exit condition that had to be met before the next phase could begin, not just a consolidation gate at the end.

**C-22 — Stakeholder fill-in table has a quantified minimum row count gate** (`structure`)
Sharpens C-17. C-17 requires an active fill-in table rather than static prose, but doesn't prevent a degenerate one-row table from satisfying it. C-22 requires an explicit `>= N rows` threshold enforced as an exit gate on Phase 1. V-03's "Phase 1 exit gate verifies >= 3 rows before advancing" converts the fill-in from a format requirement into a coverage requirement — a table with one stakeholder row cannot pass.

**Scoring formula updated**: aspirational denominator 12 → 14.
 strategy at correct path, all 5 signal fields present, valid priority vocabulary, at least one essential signal
- **3 Recommended (C-06--C-08):** Multi-namespace coverage, narrative rationale, differentiated owner roles
- **14 Aspirational (C-09--C-22):** Explicit commit gate, artifact naming convention, checkbox-gate before transition, operational-consequence framing for invalid vocabulary, dedicated sections per aspiration, pervasive consequence framing across all constraints, stakeholder-risk-first opener, structural enforcement over prose elaboration, stakeholder-risk section as active fill-in output, schema separation as constraint registry, FIELD SCHEMA stakeholder traceability column, temporally layered consequence columns, per-phase exit gates at every boundary, stakeholder fill-in minimum row count gate

The hardest failure mode to catch is C-04 -- models tend to substitute "high/medium/low" for the canonical essential/recommended/optional vocabulary. C-05 catches the degenerate case where everything is optional and there's no actual commit gate implied. **C-11--C-13 are structural excellence signals from R1**: they do not change whether a strategy is valid, but they predict whether the prompt will reliably produce valid strategies across diverse inputs. **C-14--C-16 are structural excellence signals from R2**: they represent the next tier -- C-14 generalizes consequence framing beyond priority vocabulary, C-15 generates role differentiation organically rather than enforcing it as a checklist, and C-16 identifies when structure (not prose) is doing the enforcement work. **C-17--C-18 are structural excellence signals from R3**: C-17 sharpens C-15 -- a static stakeholder-risk paragraph does not satisfy the criterion; the section must be an active fill-in step so role differentiation is derived from the model's own first output. C-18 identifies the compact two-tier schema structure that makes C-14 and C-16 co-satisfiable without prose bloat. **C-19--C-20 are structural excellence signals from R4**: C-19 sharpens C-17 -- a Stakeholder column in FIELD SCHEMA makes opener-to-plan traceability auditable at row level rather than at aggregate count level, so C-08 is satisfied by structural inspection rather than by counting distinct values. C-20 sharpens C-14 and C-18 -- splitting each consequence column into two temporal tiers (Immediate failure / Downstream effect) makes the cascade of harm visible at both the point of violation and its downstream impact, elevating each constraint from a warning to an operational weight. **C-21--C-22 are structural excellence signals from R6**: C-21 sharpens C-11 -- a single pre-write gate is necessary but not sufficient; gating every phase boundary individually prevents silent advancement at any pipeline step, not just the final one. C-22 sharpens C-17 -- an active fill-in table without a minimum row count allows a degenerate one-row table to pass; a quantified exit gate (>= N rows before advancing) makes minimum stakeholder breadth structurally enforced rather than implicitly assumed.

---

## Essential Criteria (60% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | artifact | `simulations/TOPICS.md` contains a row for the new topic with at least: topic name, status, and strategy path |
| C-02 | Strategy file at correct path | artifact | Strategy written to `simulations/{topic}/strategy.md` -- not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row includes all five required fields: namespace, skill, item name, owner role, priority |
| C-04 | Priority values are valid | correctness | Every signal priority is one of: essential / recommended / optional -- no other values present |
| C-05 | At least one essential signal planned | coverage | Strategy contains at least one signal marked essential -- a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | Planned signals reference at least 2 distinct namespaces from: scout, draft, review, flow, trace, prove, listen, program, topic |
| C-07 | Strategy includes a narrative rationale | depth | Strategy file contains a prose section (>= 2 sentences) explaining why this topic needs investigation and what decision it informs |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles appear across the planned signals (e.g., PM, engineer, designer, researcher) -- signals should not all default to a single generic role |

---

## Aspirational Criteria (10% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines a commit gate | depth | Strategy explicitly states the minimal signal set required before design commit rather than leaving the gate implicit |
| C-10 | Signal item names follow artifact naming convention | format | All item names follow the `{topic}-{signal}-{date}.md` pattern or are expressed as parameterized templates matching that convention |
| C-11 | Prompt includes checkbox-gate before phase transition | structure | Prompt contains a pre-transition checklist that forces coverage self-verification before the model proceeds to the next phase -- eliminates silent criterion omissions |
| C-12 | Invalid vocabulary framed as operational consequence | framing | Prompt states the harm of invalid priority values in terms of downstream failure ("strategy cannot be used as a commit gate") rather than as a style preference or generic warning |
| C-13 | Each aspirational criterion has a dedicated section | structure | C-09 and C-10 each appear as their own named section or heading in the prompt template -- not as inline reminders or parenthetical notes |
| C-14 | Consequence framing applied pervasively | framing | Every enforced constraint in the prompt (not just priority vocabulary) carries its downstream failure mode -- each rule that can be violated states what breaks if it is |
| C-15 | Prompt opens with stakeholder-risk enumeration | structure | Prompt contains a WHO IS AT RISK or equivalent section that enumerates role categories and their risk exposure before signal planning begins -- role differentiation emerges from the opener rather than being imposed by a late checklist |
| C-16 | Every criterion is enforced by a structural mechanism | structure | Every criterion (essential through aspirational) is enforced by a structural element -- section header, checkbox, template field, or table column -- not by prose instruction alone; this is the property that makes structural compression possible |
| C-17 | Stakeholder-risk section is an active fill-in output step | structure | The stakeholder-risk opener (C-15) is implemented as a required fill-in table that the model must produce as its first output -- not as a static prose paragraph; owner roles in the signal plan must trace back to rows in that table, so role differentiation is derived from the model's own first output rather than imposed by a late checklist |
| C-18 | Constraints are partitioned into named schemas with consequence columns | structure | The prompt separates field-level constraints (namespace, skill, item name, owner role, priority) from coverage-level constraints (essential count, namespace count, role count) into two named schemas -- each schema contains a consequence column; pre-write gate checkboxes cite schema rows by reference rather than restating rules inline; this two-tier structure gives every constraint exactly one structural home and makes C-14 and C-16 co-satisfiable without prose elaboration |
| C-19 | FIELD SCHEMA includes a Stakeholder traceability column | structure | FIELD SCHEMA contains a dedicated Stakeholder column (distinct from Owner Role) that requires each signal row to reference a specific row from the Stakeholders fill-in table -- this makes opener-to-plan traceability auditable at row level rather than at aggregate count level; C-08 is then satisfied by structural inspection rather than by counting distinct values across the table |
| C-20 | Consequence columns are temporally layered | framing | Every consequence column in FIELD SCHEMA and COVERAGE SCHEMA is split into two temporal tiers -- Immediate failure (what breaks at schema-validation time) and Downstream effect (what breaks in production or for the team when the strategy is used) -- making each constraint's cascade of harm visible at both its point of violation and its downstream impact; a single-column consequence satisfies C-14 and C-18 but does not satisfy this criterion |
| C-21 | Per-phase exit gates at every phase boundary | structure | Every phase or step in the prompt has its own exit gate -- a named condition or checklist that must be satisfied before the model is permitted to advance to the next phase; a single pre-write gate (C-11) is necessary but not sufficient; this criterion requires gate-per-boundary so that silent skips are structurally impossible at any pipeline step, not just at the final pre-write checkpoint |
| C-22 | Stakeholder fill-in table has a quantified minimum row count gate | structure | The Phase 1 stakeholder fill-in table (C-17) carries an explicit minimum row count enforced as an exit gate -- e.g., "do not advance until this table has at least 3 rows" -- preventing a degenerate one-row or two-row table from satisfying C-17; this makes minimum stakeholder breadth structurally enforced rather than implicitly assumed; a table without a minimum row count gate satisfies C-17 but does not satisfy this criterion |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Changes from v5

### Two changes from v4 -> v5 (carried forward)

- **C-19** (FIELD SCHEMA stakeholder traceability column): sharpens C-17 -- C-17 requires that roles trace back to the opener table, but does not mandate the structural column that enforces this at row level; C-19 requires FIELD SCHEMA to carry a dedicated Stakeholder column so that each signal row cites a specific opener-table row, making traceability auditable by inspection rather than by counting across the table; V-01 and V-05 (R4) both demonstrated that this column makes C-08 self-satisfying structurally
- **C-20** (temporally layered consequence columns): sharpens C-14 and C-18 -- C-14 requires pervasive consequence framing and C-18 requires consequence columns, but neither specifies temporal depth; C-20 requires each consequence entry to carry two tiers -- Immediate failure and Downstream effect -- so the cascade of harm is visible at both the violation point and its downstream impact; aspirational denominator updated from 10 to 12

### Two changes from v5 -> v6

- **C-21** (per-phase exit gates at every phase boundary): sharpens C-11 -- C-11 requires a pre-transition checklist before the final write phase, which eliminates the most common silent skip; C-21 requires gate-per-boundary so that every phase individually enforces its own exit condition; V-03 (R6) demonstrated this as a distinct structural form -- each phase's exit gate was both a self-verification step and a hard stop, not merely a reminder at the end of the pipeline; aspirational denominator updated from 12 to 14
- **C-22** (stakeholder fill-in minimum row count gate): sharpens C-17 -- C-17 requires the stakeholder-risk section to be an active fill-in table rather than a static paragraph, but does not prevent a minimal one-row response from satisfying it; C-22 requires an explicit numeric threshold (>= N rows) enforced as an exit gate so that stakeholder breadth is structurally enforced; V-03 (R6) demonstrated this with "Phase 1 exit gate verifies >= 3 rows before advancing" -- the count transforms the fill-in from a format requirement into a coverage requirement
