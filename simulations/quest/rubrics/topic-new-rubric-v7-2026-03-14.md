Written to `simulations/quest/rubrics/topic-new-rubric-v7-2026-03-14.md`.

---

## v7 summary

Three new aspirational criteria extracted from R7 excellence signals:

| ID | Name | Source | Sharpens |
|----|------|--------|----------|
| C-23 | Schema constraints carry row-level identifiers for gate citation | V-04 | C-18 |
| C-24 | Pipeline declares all exit gates in a summary table before phase content | V-03 | C-21 |
| C-25 | Commit Gate occupies a dedicated phase separate from signal plan production | V-05 | C-09, C-13 |

**Aspirational denominator**: 14 → 17

**Scoring formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 17 * 10)
```

**Key distinctions**:
- C-23 vs C-18: C-18 requires schemas + consequence columns + gate-by-reference. C-23 requires stable row IDs (F-N, COV-N) so the coupling is mechanical — a gate citing "F-01 through F-05" cannot drift from the schema.
- C-24 vs C-21: C-21 requires inline gates at every boundary. C-24 requires an upfront pipeline overview table that declares all gate conditions architecturally before phase execution begins, then reinforced inline.
- C-25 vs C-13: C-13 requires C-09/C-10 as named sections or headings. C-25 requires the commit gate to be a separate *phase* from signal production — guaranteeing both an entry and exit gate on the production phase, eliminating the V-02 entry-only failure mode structurally.
: the pipeline overview table listed every phase's exit condition before the model encountered Phase 1; each phase then carried its own inline gate as a second layer. The dual-layer (overview declaration + inline gate) makes gate omission structurally impossible even if the model skips a phase section. A prompt satisfying C-21 via inline-only gates does not satisfy C-24.

**C-25 — Commit Gate occupies a dedicated phase separate from signal plan production** (`structure`)
Sharpens C-09 and C-13. C-09 requires an explicit commit gate; C-13 requires it as a dedicated section or heading. C-25 requires the commit gate to be a separate phase from signal row production — each phase having its own entry and exit gates. V-05 demonstrated this as Phase 8 (Commit Gate) following Phase 7 (signal plan production), each independently gated. This separation eliminates V-02's failure mode structurally: when signal production and commit gate naming share one phase, the phase entry gate (C-11) does not constitute an exit gate after output is produced, leaving the post-production boundary ungated. When they are separate phases, the Phase 7 exit gate verifies signal rows before the model advances to Phase 8, making the V-02 omission architecturally impossible. A prompt satisfying C-09 and C-13 via a named section inside the signal plan phase does not satisfy C-25.

**Scoring formula updated**: aspirational denominator 14 → 17.
- **5 Essential (C-01--C-05):** TOPICS.md entry exists, strategy at correct path, all 5 signal fields present, valid priority vocabulary, at least one essential signal
- **3 Recommended (C-06--C-08):** Multi-namespace coverage, narrative rationale, differentiated owner roles
- **17 Aspirational (C-09--C-25):** Explicit commit gate, artifact naming convention, checkbox-gate before transition, operational-consequence framing for invalid vocabulary, dedicated sections per aspiration, pervasive consequence framing across all constraints, stakeholder-risk-first opener, structural enforcement over prose elaboration, stakeholder-risk section as active fill-in output, schema separation as constraint registry, FIELD SCHEMA stakeholder traceability column, temporally layered consequence columns, per-phase exit gates at every boundary, stakeholder fill-in minimum row count gate, schema constraints carry row-level identifiers, pipeline declares all exit gates upfront in summary table, commit gate occupies a dedicated phase separate from signal production

The hardest failure mode to catch is C-04 -- models tend to substitute "high/medium/low" for the canonical essential/recommended/optional vocabulary. C-05 catches the degenerate case where everything is optional and there's no actual commit gate implied. **C-11--C-13 are structural excellence signals from R1**: they do not change whether a strategy is valid, but they predict whether the prompt will reliably produce valid strategies across diverse inputs. **C-14--C-16 are structural excellence signals from R2**: they represent the next tier -- C-14 generalizes consequence framing beyond priority vocabulary, C-15 generates role differentiation organically rather than enforcing it as a checklist, and C-16 identifies when structure (not prose) is doing the enforcement work. **C-17--C-18 are structural excellence signals from R3**: C-17 sharpens C-15 -- a static stakeholder-risk paragraph does not satisfy the criterion; the section must be an active fill-in step so role differentiation is derived from the model's own first output. C-18 identifies the compact two-tier schema structure that makes C-14 and C-16 co-satisfiable without prose bloat. **C-19--C-20 are structural excellence signals from R4**: C-19 sharpens C-17 -- a Stakeholder column in FIELD SCHEMA makes opener-to-plan traceability auditable at row level rather than at aggregate count level, so C-08 is satisfied by structural inspection rather than by counting distinct values. C-20 sharpens C-14 and C-18 -- splitting each consequence column into two temporal tiers (Immediate failure / Downstream effect) makes the cascade of harm visible at both the point of violation and its downstream impact, elevating each constraint from a warning to an operational weight. **C-21--C-22 are structural excellence signals from R6**: C-21 sharpens C-11 -- a single pre-write gate is necessary but not sufficient; gating every phase boundary individually prevents silent advancement at any pipeline step, not just the final one. C-22 sharpens C-17 -- an active fill-in table without a minimum row count allows a degenerate one-row table to pass; a quantified exit gate (>= N rows before advancing) makes minimum stakeholder breadth structurally enforced rather than implicitly assumed. **C-23--C-25 are structural excellence signals from R7**: C-23 sharpens C-18 -- schema row-level identifiers (F-N, COV-N) create mechanical coupling between constraint definitions and gate checkpoints so gates cite rules by canonical ID rather than paraphrase, eliminating drift. C-24 sharpens C-21 -- declaring all exit gates in a pipeline overview table before any phase content makes gate conditions visible architecturally before execution begins, then reinforced inline per phase; a prompt satisfying C-21 via inline-only gates does not satisfy C-24. C-25 sharpens C-09 and C-13 -- isolating the Commit Gate in its own dedicated phase from signal row production guarantees that the signal-plan phase has both an entry gate and an exit gate, structurally eliminating the V-02 failure mode where an entry-only gate left the post-production boundary ungated.

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
| C-21 | Per-phase exit gates at every phase boundary | structure | Every phase or step in the prompt has its own exit gate -- a named condition or checklist that must be satisfied before the model is permitted to advance to the next phase; a single pre-write gate (C-11) is necessary but not sufficient; this criterion requires gate-per-boundary so that silent skips are structurally impossible at any pipeline step, not just at the final pre-write checkpoint; a phase that produces structured output requires both an entry gate before writing and an exit gate after writing |
| C-22 | Stakeholder fill-in table has a quantified minimum row count gate | structure | The Phase 1 stakeholder fill-in table (C-17) carries an explicit minimum row count enforced as an exit gate -- e.g., "do not advance until this table has at least 3 rows" -- preventing a degenerate one-row or two-row table from satisfying C-17; this makes minimum stakeholder breadth structurally enforced rather than implicitly assumed; a table without a minimum row count gate satisfies C-17 but does not satisfy this criterion |
| C-23 | Schema constraints carry row-level identifiers for gate citation | structure | Every row in FIELD SCHEMA and COVERAGE SCHEMA carries a stable row-level identifier (e.g., F-01, F-02, COV-01, COV-02) that gate checkpoints cite directly -- so the coupling between constraint definition and enforcement checkpoint is mechanical, not prose-based; a gate that cites "F-01 through F-05" is compact and cannot drift from the schema definition; a gate that restates rules in prose satisfies C-18 but does not satisfy C-23; this criterion sharpens C-18 by requiring the schema row IDs that make gate citations unambiguous and derivable from schema structure rather than authored separately |
| C-24 | Pipeline declares all exit gates in a summary table before phase content | structure | The prompt opens with a pipeline overview or summary table that has an Exit Gate column listing every phase's gate condition before any phase content is presented -- so all gate conditions are visible in one place architecturally before execution begins, then reinforced inline per phase; the dual-layer (overview declaration + inline gate) makes gate omission structurally impossible even if a phase section is skimmed; a prompt satisfying C-21 via inline-only gates (no upfront declaration table) does not satisfy C-24 |
| C-25 | Commit Gate occupies a dedicated phase separate from signal plan production | structure | The commit gate definition (C-09) is implemented as its own phase with its own entry and exit gates, structurally separated from the signal plan production phase -- so the signal plan phase has both an entry gate (before writing rows) and an exit gate (after writing rows, before advancing to the commit gate phase); this separation eliminates the V-02 failure mode where signal production and commit gate naming shared one phase, leaving the post-production boundary ungated; a prompt satisfying C-09 and C-13 via a named section inside the signal plan phase does not satisfy C-25 |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 17 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Changes from v6

### Two changes from v5 -> v6 (carried forward)

- **C-21** (per-phase exit gates at every phase boundary): sharpens C-11 -- C-11 requires a pre-transition checklist before the final write phase, which eliminates the most common silent skip; C-21 requires gate-per-boundary so that every phase individually enforces its own exit condition; V-03 (R6) demonstrated this as a distinct structural form -- each phase's exit gate was both a self-verification step and a hard stop, not merely a reminder at the end of the pipeline; aspirational denominator updated from 12 to 14
- **C-22** (stakeholder fill-in minimum row count gate): sharpens C-17 -- C-17 requires the stakeholder-risk section to be an active fill-in table rather than a static paragraph, but does not prevent a minimal one-row response from satisfying it; C-22 requires an explicit numeric threshold (>= N rows) enforced as an exit gate so that stakeholder breadth is structurally enforced; V-03 (R6) demonstrated this with "Phase 1 exit gate verifies >= 3 rows before advancing" -- the count transforms the fill-in from a format requirement into a coverage requirement

### Three changes from v6 -> v7

- **C-23** (schema constraints carry row-level identifiers for gate citation): sharpens C-18 -- C-18 requires schema separation and consequence columns with gate checkpoints citing schema rows by reference; C-23 requires each schema row to carry a stable row-level identifier (F-N, COV-N) so that gate citations are canonical and mechanically coupled to definitions rather than paraphrased in prose; V-04 (R7) demonstrated this as the cleanest mechanical solution -- no other variation achieved this coupling; aspirational denominator updated from 14 to 15
- **C-24** (pipeline declares all exit gates in a summary table before phase content): sharpens C-21 -- C-21 requires gates at every boundary; C-24 requires those gates to also be declared upfront in a pipeline overview table with an Exit Gate column before any phase content appears; V-03 (R7 excellence signal) demonstrated this as architectural gate declaration -- all conditions visible in one place before execution, then reinforced inline per phase; aspirational denominator updated from 15 to 16
- **C-25** (commit gate occupies a dedicated phase separate from signal plan production): sharpens C-09 and C-13 -- C-09 requires an explicit commit gate; C-13 requires it as a dedicated section or heading; C-25 requires the commit gate to be a fully separate phase from signal row production, each phase having its own entry and exit gates; V-05 (R7) demonstrated this as Phase 8 following Phase 7, structurally eliminating the V-02 failure mode (entry-only gate on output-producing step leaves post-production boundary ungated); aspirational denominator updated from 16 to 17
