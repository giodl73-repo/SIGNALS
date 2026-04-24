# topic-new Rubric — v15

> Bumped from v14 (2026-03-15). Two new aspirational criteria from Round 16 excellence signals.

---

## v15 — two new criteria from R16 excellence signals

| ID | Name | Sharpens | Source |
|----|------|----------|--------|
| C-47 | Independence gate provides a concrete worked example of sequential-treatment failure output — a specific output string that sequential checking would accept but independent checking would reject — making the failure recognizable by output inspection rather than by reasoning about what sequential treatment produces | C-33 | R16 C-33 PASS+ cluster (V-01/V-02/V-03) |
| C-48 | Pipeline consequence column entries are backed by a named PHASE CONSEQUENCE REGISTRY (PCR-NN IDs); the pipeline overview cites PCR-NN IDs in its consequence column rather than embedding prose directly; consequence definitions live in one authoritative location and are auditable by reference rather than by content matching | C-29 | R16 V-02/V-05 PCR citation pattern |

**Aspirational denominator**: 38 → 40

**Scoring formula**: `aspirational_pass / 40 * 10`

---

**Gap logic per criterion:**

- **C-47** — C-33 requires the independence gate to name the specific sequential-treatment failure mode (e.g., "Sequential checking produces row-count acceptance without column-completeness verification"). Naming a failure mode is necessary but not sufficient: the model can acknowledge the named pattern abstractly without having a recognizable output target to match against when checking its own work at the gate. C-47 closes the **failure-recognition gap**: a concrete worked example shows the model exactly what wrong-but-seemingly-valid output looks like at the moment of checking. The example — e.g., "'3 rows, columns empty' reads as compliant — this is wrong" — makes the failure detectable by output inspection rather than by abstract reasoning about what sequential treatment produces. A gate that names the failure mode (satisfying C-33) but provides only the abstract name and no concrete output example does not satisfy C-47.

- **C-48** — C-29 requires the pipeline overview to carry a consequence column, and C-32 requires those entries to use first-person framing. Both criteria are satisfied when consequence prose is embedded directly in the pipeline overview cells. But direct embedding creates a **consequence-drift channel**: when a consequence changes, it must be updated everywhere it appears — in the pipeline overview, in any phase narrative that references it, and in any review or scoring rubric that quotes it. Drift between display sites is invisible to structural inspection. C-48 closes this channel by requiring a named PHASE CONSEQUENCE REGISTRY (PCR-NN) where consequence definitions live in one authoritative location; the pipeline overview cites PCR-NN IDs rather than embedding prose. This makes consequence definitions maintainable by ID, auditable by reference, and immune to display-layer drift. C-48 is the pipeline-level analog of C-23 (schema rows carry IDs for gate citation) applied to the consequence column: a pipeline overview satisfying C-29 with embedded prose consequences does not satisfy C-48 unless the consequence column cites PCR-NN IDs backed by a registry.

---

## v14 — two new criteria from R15 excellence signals

| ID | Name | Sharpens | Source |
|----|------|----------|--------|
| C-45 | Phase bodies contain zero inline prose constraints; every constraint lives exclusively in a named schema row; phase text consists solely of schema-ID references, fill-in slots, and structural navigation | C-16, C-18, C-23, C-27 | V-01 PASS+ cluster |
| C-46 | INERTIA REGISTER includes a "Stakeholder Most Harmed" column naming the role category most vulnerable to each inertia default; per-phase override directives reproduce both IR-NN ID and the role name; exit gate verbatim reproductions include the role name alongside the full IR-NN text | C-43, C-44 | V-02 ES-1/ES-2/ES-3 |

**Aspirational denominator (v14)**: 36 → 38

---

**Gap logic — v14 criteria:**

- **C-45** — C-16 requires every constraint to be enforced by a structural element. C-18 requires schemas to exist with consequence columns. Neither forbids inline prose restatements of schema rules inside phase bodies. A prompt can satisfy C-16 and C-18 while still restating rules as prose within phase text — creating a dual-truth channel where schema and prose can diverge on revision without a mechanical signal. C-45 closes the **schema-drift channel**: phase bodies carry no constraint prose; the schema is the sole and exclusive truth. When schema and execution point share no prose, drift is detectable by structural inspection rather than content comparison.

- **C-46** — C-44 requires the full IR-NN text reproduced verbatim at exit gates. But IR-NN text typically describes an inertia *pattern* (what the default behavior is) without naming who bears the cost when the override is skipped. A model at the gate sees the inertia text but may not have the role-vulnerability mapping in active context. C-46 requires the INERTIA REGISTER to carry a "Stakeholder Most Harmed" column, and for that role name to travel with IR-NN citations at phase override directives and at exit gate reproductions. Closes the **role-abstraction axis**: inertia text is present but stakeholder vulnerability is abstract, so the model can evaluate the gate without knowing whose outcome depends on it.

---

## Essential Criteria (60% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | artifact | `simulations/TOPICS.md` contains a row for the new topic with at least: topic name, status, and strategy path |
| C-02 | Strategy file at correct path | artifact | Strategy written to `simulations/{topic}/strategy.md` — not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row includes all five required fields: namespace, skill, item name, owner role, priority |
| C-04 | Priority values are valid | correctness | Every signal priority is one of: essential / recommended / optional — no other values present |
| C-05 | At least one essential signal planned | coverage | Strategy contains at least one signal marked essential — a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | Planned signals reference at least 2 distinct namespaces from: scout, draft, review, flow, trace, prove, listen, program, topic |
| C-07 | Strategy includes a narrative rationale | depth | Strategy file contains a prose section (>= 2 sentences) explaining why this topic needs investigation and what decision it informs |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles appear across the planned signals (e.g., PM, engineer, designer, researcher) — signals should not all default to a single generic role |

---

## Aspirational Criteria (10% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines a commit gate | depth | Strategy explicitly states the minimal signal set required before design commit rather than leaving the gate implicit |
| C-10 | Signal item names follow artifact naming convention | format | All item names follow the `{topic}-{signal}-{date}.md` pattern or are expressed as parameterized templates matching that convention |
| C-11 | Prompt includes checkbox-gate before phase transition | structure | Prompt contains a pre-transition checklist that forces coverage self-verification before the model proceeds to the next phase — eliminates silent criterion omissions |
| C-12 | Invalid vocabulary framed as operational consequence | framing | Prompt states the harm of invalid priority values in terms of downstream failure ("strategy cannot be used as a commit gate") rather than as a style preference or generic warning |
| C-13 | Each aspirational criterion has a dedicated section | structure | C-09 and C-10 each appear as their own named section or heading in the prompt template — not as inline reminders or parenthetical notes |
| C-14 | Consequence framing applied pervasively | framing | Every enforced constraint in the prompt (not just priority vocabulary) carries its downstream failure mode — each rule that can be violated states what breaks if it is |
| C-15 | Prompt opens with stakeholder-risk enumeration | structure | Prompt contains a WHO IS AT RISK or equivalent section that enumerates role categories and their risk exposure before signal planning begins — role differentiation emerges from the opener rather than being imposed by a late checklist |
| C-16 | Every criterion is enforced by a structural mechanism | structure | Every criterion (essential through aspirational) is enforced by a structural element — section header, checkbox, template field, or table column — not by prose instruction alone; this is the property that makes structural compression possible |
| C-17 | Stakeholder-risk section is an active fill-in output step | structure | The stakeholder-risk opener (C-15) is implemented as a required fill-in table that the model must produce as its first output — not as a static prose paragraph; owner roles in the signal plan must trace back to rows in that table, so role differentiation is derived from the model's own first output rather than imposed by a late checklist |
| C-18 | Constraints are partitioned into named schemas with consequence columns | structure | The prompt separates field-level constraints (namespace, skill, item name, owner role, priority) from coverage-level constraints (essential count, namespace count, role count) into two named schemas — each schema contains a consequence column; pre-write gate checkboxes cite schema rows by reference rather than restating rules inline; this two-tier structure gives every constraint exactly one structural home and makes C-14 and C-16 co-satisfiable without prose elaboration |
| C-19 | FIELD SCHEMA includes a Stakeholder traceability column | structure | FIELD SCHEMA contains a dedicated Stakeholder column (distinct from Owner Role) that requires each signal row to reference a specific row from the Stakeholders fill-in table — this makes opener-to-plan traceability auditable at row level rather than at aggregate count level; C-08 is then satisfied by structural inspection rather than by counting distinct values across the table |
| C-20 | Consequence columns are temporally layered | framing | Every consequence column in FIELD SCHEMA and COVERAGE SCHEMA is split into two temporal tiers — Immediate failure (what breaks at schema-validation time) and Downstream effect (what breaks in production or for the team when the strategy is used) — making each constraint's cascade of harm visible at both its point of violation and its downstream impact; a single-column consequence satisfies C-14 and C-18 but does not satisfy this criterion |
| C-21 | Per-phase exit gates at every phase boundary | structure | Every phase or step in the prompt has its own exit gate — a named condition or checklist that must be satisfied before the model is permitted to advance to the next phase; a single pre-write gate (C-11) is necessary but not sufficient; this criterion requires gate-per-boundary so that silent skips are structurally impossible at any pipeline step, not just at the final pre-write checkpoint; a phase that produces structured output requires both an entry gate before writing and an exit gate after writing |
| C-22 | Stakeholder fill-in table has a quantified minimum row count gate | structure | The Phase 1 stakeholder fill-in table (C-17) carries an explicit minimum row count enforced as an exit gate — e.g., "do not advance until this table has at least 3 rows" — preventing a degenerate one-row or two-row table from satisfying C-17; this makes minimum stakeholder breadth structurally enforced rather than implicitly assumed; a table without a minimum row count gate satisfies C-17 but does not satisfy this criterion |
| C-23 | Schema constraints carry row-level identifiers for gate citation | structure | Every row in FIELD SCHEMA and COVERAGE SCHEMA carries a stable row-level identifier (e.g., F-01, F-02, COV-01, COV-02) that gate checkpoints cite directly — so the coupling between constraint definition and enforcement checkpoint is mechanical, not prose-based; a gate that cites "F-01 through F-05" is compact and cannot drift from the schema definition; a gate that restates rules in prose satisfies C-18 but does not satisfy C-23 |
| C-24 | Pipeline declares all exit gates in a summary table before phase content | structure | The prompt opens with a pipeline overview or summary table that has an Exit Gate column listing every phase's gate condition before any phase content is presented — so all gate conditions are visible in one place architecturally before execution begins, then reinforced inline per phase; a prompt satisfying C-21 via inline-only gates (no upfront declaration table) does not satisfy C-24 |
| C-25 | Commit Gate occupies a dedicated phase separate from signal plan production | structure | The commit gate definition (C-09) is implemented as its own phase with its own entry and exit gates, structurally separated from the signal plan production phase — so the signal plan phase has both an entry gate (before writing rows) and an exit gate (after writing rows, before advancing to the commit gate phase); a prompt satisfying C-09 and C-13 via a named section inside the signal plan phase does not satisfy C-25 |
| C-26 | Pipeline overview carries an explicit "read before executing" meta-instruction | structure | The pipeline overview table (C-24) includes an explicit sequencing directive instructing the model to read the entire table before beginning Phase 1 — for example: "Read this entire table before executing Phase 1. All exit gate conditions are declared here." This directive transforms the overview from a passive reference into a required prerequisite step; a prompt satisfying C-24 via a well-formed overview table with no read-before-execute instruction does not satisfy C-26 |
| C-27 | Schema row IDs cited independently at multiple gate boundaries | structure | The schema row IDs established by C-23 (F-N, COV-N) appear as explicit citations at more than one independent gate boundary within the prompt — so the mechanical coupling between schema definitions and gate checkpoints is verified redundantly, not only at a single checkpoint; a prompt satisfying C-23 with ID citations present at exactly one gate boundary does not satisfy C-27 |
| C-28 | Fill-in table exit gate enforces column completeness independently of row count | structure | The Phase 1 stakeholder fill-in table exit gate (C-22) states column completeness as a separately listed condition from the minimum row count — e.g., both ">= 3 rows filled" and "all four columns populated" appear as discrete checkbox items; a prompt satisfying C-22 with only a row-count condition (no column completeness condition) does not satisfy C-28 |
| C-29 | Pipeline overview table carries a per-row consequence column | structure | The pipeline overview table (C-24) includes a dedicated consequence column — labeled "If Skipped," "Cost of Skipping," or equivalent — that states the consequence of bypassing each phase as a row-level entry alongside the Exit Gate column; a model reading the overview before Phase 1 sees both what must be satisfied and what breaks if each phase is skipped; a prompt satisfying C-24 via a gate-declarative overview table without a per-row consequence column does not satisfy C-29 |
| C-30 | Gate independence stated as an explicit semantic instruction | structure | When the exit gate of the Phase 1 stakeholder fill-in table (C-28) lists two conditions (row count and column completeness), the prompt includes an explicit semantic instruction at the enforcement point stating that those conditions must be checked independently — for example: "Check these two items independently" as a label preceding the checkboxes, followed by "Do not advance until both are checked separately" as a closing enforcement statement; a prompt satisfying C-28 via two distinct checkbox items without an explicit independence instruction does not satisfy C-30 |
| C-31 | Priority column placed first in signal table column order | structure | The signal planning table places the Priority column as the leftmost column — before Namespace, Skill, Item Name, Owner Role, and Stakeholder Ref columns; a model filling a table left-to-right reaches the priority field before namespace or skill values can anchor contextual framing that might induce "high/medium/low" substitution; a prompt satisfying C-04 via valid-vocabulary enforcement with a non-leading priority column does not satisfy C-31 |
| C-32 | [Prior-round criterion] | — | Carries forward from v10 baseline |
| C-33 | [Prior-round criterion] | — | Carries forward from v10 baseline |
| C-34 | [Prior-round criterion] | — | Carries forward from v10 baseline |
| C-35 | [Prior-round criterion] | — | Carries forward from v10 baseline |
| C-36 | [Prior-round criterion] | — | Carries forward from v10 baseline |
| C-37 | [Prior-round criterion] | — | Carries forward from v10 baseline |
| C-38 | Team-inertia default column present in signal table | structure | Signal planning table includes a Team-Default column capturing the inertia pattern each role typically exhibits; pipeline phase descriptions acknowledge these defaults inline |
| C-39 | [Prior-round criterion] | — | Carries forward from v11 baseline |
| C-40 | [Prior-round criterion] | — | Carries forward from v11 baseline |
| C-41 | [Prior-round criterion] | — | Carries forward from v12 baseline |
| C-42 | Team inertia defaults collected in named INERTIA REGISTER block with stable IR-NN IDs; pipeline team-default column references by ID | structure | A pre-pipeline INERTIA REGISTER block exists with stable IR-NN IDs for each named inertia default; the signal table's team-default column carries `→ IR-NN` references rather than inline prose; a prompt satisfying C-38 via inline prose in the team-default column does not satisfy C-42 |
| C-43 | Each phase carries an explicit "This phase overrides IR-NN" directive at execution time | structure | Every phase that overrides an inertia default includes the directive "This phase overrides IR-NN" at its execution point — not only in the pre-pipeline register; a prompt satisfying C-42 with a well-formed INERTIA REGISTER but no per-phase restatement does not satisfy C-43 |
| C-44 | Phase consequence warnings reproduce the full IR-NN text verbatim at the exit gate | structure | At every phase exit gate where an inertia override applies, the complete text of the relevant IR-NN entry is reproduced verbatim alongside the standard gate conditions — not cited by ID alone; a prompt satisfying C-43 with per-phase override directives that cite only the ID (not the full text) does not satisfy C-44 |
| C-45 | Phase bodies contain zero inline prose constraints | structure | Phase bodies contain no inline prose restatements of constraints that exist in named schema rows; every constraint lives exclusively in FIELD SCHEMA, COVERAGE SCHEMA, or STAKEHOLDER SCHEMA; phase text consists solely of schema-ID references, fill-in slots, and structural navigation directives; a prompt satisfying C-16 and C-18 while still restating schema rules as prose within phase bodies does not satisfy C-45 — prose restatements create a dual-truth channel where schema and phase text can diverge on revision without a mechanical signal |
| C-46 | INERTIA REGISTER includes a "Stakeholder Most Harmed" column; role name travels with all IR-NN citations | structure | The INERTIA REGISTER (C-42) contains a dedicated "Stakeholder Most Harmed" column naming the role category most vulnerable to each inertia default; per-phase override directives (C-43) reproduce both the IR-NN ID and the role name; exit gate verbatim reproductions (C-44) include the "Stakeholder Most Harmed" role name alongside the full IR-NN text; a prompt satisfying C-42/C-43/C-44 with no role-vulnerability column in the register does not satisfy C-46 — IR-NN text may describe the inertia pattern without making concrete whose outcome depends on the override |
| C-47 | Independence gate provides a concrete worked example of sequential-treatment failure output | structure | The gate instruction that enforces independent checking (C-30) includes a concrete output example — a specific string or table state that sequential checking would accept but independent checking would reject (e.g., "'3 rows, columns empty' reads as compliant — this is wrong") — so the failure is recognizable by output inspection at the gate rather than by abstract reasoning about what sequential treatment produces; a prompt satisfying C-33 by naming the failure mode in abstract without showing a concrete failure output does not satisfy C-47 |
| C-48 | Pipeline consequence column entries backed by a named PHASE CONSEQUENCE REGISTRY (PCR-NN IDs) | structure | A named PHASE CONSEQUENCE REGISTRY (PCR) exists with stable IDs (PCR-01, PCR-02, etc.) defining each phase-skip consequence; the pipeline overview's consequence column cites PCR-NN IDs rather than embedding consequence prose directly; the PCR serves as the sole authoritative consequence-definition layer — making consequence definitions maintainable by ID and immune to display-layer drift; a prompt satisfying C-29 with consequence prose embedded directly in the pipeline overview cells does not satisfy C-48; this is the pipeline-level analog of C-23 applied to consequence definitions |

---

## Summary of changes v14 → v15

| Delta | Detail |
|-------|--------|
| +C-47 | Independence gate provides concrete worked example of sequential-treatment failure output — closes failure-recognition gap above C-33; C-33 requires naming the failure mode, C-47 requires demonstrating it as a recognizable output example |
| +C-48 | Pipeline consequence column backed by named PHASE CONSEQUENCE REGISTRY (PCR-NN) — closes consequence-drift channel above C-29; C-29 requires a consequence column, C-48 requires consequence definitions to live in a registry cited by ID rather than embedded as prose |
| Denominator | 38 → 40 |
| Formula | `aspirational_pass / 40 × 10` |
