Three new aspirational criteria from the R3 excellence signals: **C-16** (3-slot rationale format), **C-17** (CROSS-SKILL inheritance rule), **C-18** (closing confirmation multi-gate). Aspirational denominator bumps 8 → 11.

---

# rhythm-behavior Rubric — v4

**Skill**: `rhythm:behavior`
**Purpose**: Evaluate outputs from the rhythm-behavior orchestration skill, which runs five sub-skills (flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions) in declared order and produces a consolidated findings report ranked by blast radius.

**Scoring formula**:
```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/11 * 10)
```
- Essential ceiling: 60 | Recommended ceiling: 30 | Aspirational ceiling: 10
- Maximum composite: 100
- Golden threshold: all 4 essential criteria pass AND composite >= 80

---

## Essential Criteria

| # | Name | Category |
|---|------|----------|
| C-01 | Declared Execution Sequence | format |
| C-02 | Single Unified Report | format |
| C-03 | Blast Radius Ranking Present | correctness |
| C-04 | Spec Gap and Contract Violation Coverage | coverage |

## Recommended Criteria

| # | Name | Category |
|---|------|----------|
| C-05 | Per-Finding Sub-Skill Attribution | correctness |
| C-06 | Actionable Next Step for Top Finding | depth |
| C-07 | Sub-Skill Section Completeness | coverage |

## Aspirational Criteria

| # | Name | Category | Origin |
|---|------|----------|--------|
| C-08 | Blast Radius Justification | depth | — |
| C-09 | Cross-Sub-Skill Synthesis | depth | — |
| C-10 | Self-Documenting Ranking Label | format | R1 V-05 |
| C-11 | Active Coverage Confirmation | coverage | R1 V-05 |
| C-12 | At-Discovery Attribution | correctness | R1 V-05 |
| C-13 | Dedicated Synthesis Step | depth | R2 |
| C-14 | Rationale Column Enforcement | depth | R2 |
| C-15 | CROSS-SKILL Findings as First-Class Table Citizens | correctness | R2 |
| **C-16** | **3-Slot Rationale Format** | **depth** | **R3** |
| **C-17** | **CROSS-SKILL Blast Radius Inheritance Rule** | **correctness** | **R3** |
| **C-18** | **Closing Confirmation Multi-Gate Enforcement** | **format** | **R3** |

---

## Criterion Definitions

### Essential Criteria

#### C-01 — Declared Execution Sequence
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output names the five sub-skills in declared order before any findings appear (flow-lifecycle → flow-conversation → trace-state → trace-contract → trace-permissions). Order and completeness must both be present.

#### C-02 — Single Unified Report
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output is one continuous document with no promise to continue in a later response. Any split across responses is an automatic fail.

#### C-03 — Blast Radius Ranking Present
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: All findings in the consolidated report are sorted by blast radius (WIDE first, NARROW last). The sort must be labeled. Findings in unsorted or unlabeled order fail this criterion.

#### C-04 — Spec Gap and Contract Violation Coverage
- **Weight**: essential
- **Category**: coverage
- **Pass condition**: The consolidated report contains at least one finding classified as a spec gap (missing, ambiguous, or underspecified requirement) and at least one classified as a contract violation (a behavior that breaks a declared interface, pre/post condition, or permission boundary). These categories must be distinguishable by label, section, or explicit classification. Fail if all findings are of a single type or the two categories are indistinguishable.

---

### Recommended Criteria

#### C-05 — Per-Finding Sub-Skill Attribution
- **Weight**: recommended
- **Category**: correctness
- **Pass condition**: Each finding in the consolidated report cites the sub-skill that produced it (e.g., "trace-contract: …"). Attribution must be present at the finding level, not only in section headers.

#### C-06 — Actionable Next Step for Top Finding
- **Weight**: recommended
- **Category**: depth
- **Pass condition**: The highest-ranked finding (first after blast-radius sort) includes one concrete, specific next step a developer can execute before writing implementation code. The step must name an exact spec section, boundary, or component — not a generic directive like "review the spec."

#### C-07 — Sub-Skill Section Completeness
- **Weight**: recommended
- **Category**: coverage
- **Pass condition**: Every sub-skill section is present in the report. Sections with no findings must say so explicitly (e.g., "no findings" or "none identified"). Silently omitted sections fail.

---

### Aspirational Criteria

#### C-08 — Blast Radius Justification
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: Every finding in the consolidated table includes a rationale column entry that names specific flows, contracts, or permission boundaries affected — not a generic phrase. An empty rationale cell or a phrase like "affects multiple callers" without naming them fails.

#### C-09 — Cross-Sub-Skill Synthesis
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: The output contains a dedicated SYNTHESIS section that identifies findings whose scope spans more than one sub-skill, labels them CROSS-SKILL, and inserts them as rows in the consolidated findings table.

#### C-10 — Self-Documenting Ranking Label
- **Weight**: aspirational
- **Category**: format
- **Origin**: R1 V-05
- **Pass condition**: The sorted findings table carries an explicit label adjacent to it stating the sort order (e.g., "Sorted by Blast Radius: WIDE → MEDIUM → NARROW"). The label must be structurally attached to the table, not only mentioned in prose.

#### C-11 — Active Coverage Confirmation
- **Weight**: aspirational
- **Category**: coverage
- **Origin**: R1 V-05
- **Pass condition**: The output includes a closing confirmation step that explicitly checks whether at least one spec gap and at least one contract violation are present in the report. A passive recap does not satisfy this — the check must be conditional (e.g., a correction loop fires if either category is absent).

#### C-12 — At-Discovery Attribution
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R1 V-05
- **Pass condition**: Sub-skill attribution is assigned at the moment a finding is added to the table, not retroactively in a consolidation pass. This is structurally satisfied when the table is pre-opened before sub-skills run and rows are appended as findings are discovered.

#### C-13 — Dedicated Synthesis Step
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R2
- **Pass condition**: The SYNTHESIS section appears as a structurally isolated step between the last sub-skill section and the consolidation/ranking step — not embedded in either. This isolation gives the model a comparison moment before it must also rank; conflating synthesis and ranking degrades C-09 quality.

#### C-14 — Rationale Column Enforcement
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R2
- **Pass condition**: The rationale requirement is enforced via a mandatory table column (pre-opened before sub-skills run), not via inline prose annotation. An empty cell is structurally visible as an omission; an inline annotation is silently skippable in dense output.

#### C-15 — CROSS-SKILL Findings as First-Class Table Citizens
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R2
- **Pass condition**: CROSS-SKILL findings appear as rows in the shared findings table (Sub-Skill = CROSS-SKILL), making them automatically subject to C-11 coverage confirmation and C-03 blast radius ranking. CROSS-SKILL findings surfaced only in prose or in a separate list fail this criterion.

#### C-16 — 3-Slot Rationale Format
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R3
- **Pass condition**: Blast radius rationale entries follow the 3-slot structure `[LEVEL] because [boundary] propagates to [caller/component], [effect]`. The format is declared once in the "what to look for" instruction and once in the closing confirmation gate. Generic phrases (e.g., "affects multiple callers") cannot satisfy this format because all three named slots must be filled independently. Pass if the 3-slot structure is present in both enforcement sites and rationale entries contain all three elements; fail if the format is open-ended or if any slot is merged or omitted.

#### C-17 — CROSS-SKILL Blast Radius Inheritance Rule
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R3
- **Pass condition**: CROSS-SKILL findings assign a blast radius of at least `max(contributors)` — no downgrade from the highest-contributing sub-skill finding is permitted. The rationale entry must include a provenance annotation in the form `Inherited [LEVEL] from [sub-skill-X] ([F-ID])` identifying the source finding. This makes scope assignment auditable and detectable in the closing confirmation gate. Fail if a CROSS-SKILL finding carries a blast radius below the highest contributor or if the provenance annotation is absent.

#### C-18 — Closing Confirmation Multi-Gate Enforcement
- **Weight**: aspirational
- **Category**: format
- **Origin**: R3
- **Pass condition**: The closing confirmation step is a structured checklist that enforces all three quality axes in a single location: (1) coverage check — at least one spec gap and one contract violation present; (2) format compliance check — every rationale entry satisfies the 3-slot structure; (3) inheritance compliance check — every CROSS-SKILL blast radius is at or above `max(contributors)`. A closing section that recaps findings without conditional gating on each axis fails. Pass if all three gates are present and each triggers a correction loop on failure.

---

## What Changed from v3 to v4

Three new aspirational criteria from the R3 excellence signals:

| Criterion | Category | Pattern |
|-----------|----------|---------|
| **C-16** 3-Slot Rationale Format | depth | `[LEVEL] because [boundary] propagates to [caller/component], [effect]` enforced at two sites (what-to-look-for + closing confirmation) eliminates vague rationales without per-section repetition — generic phrases cannot fill three independently named slots |
| **C-17** CROSS-SKILL Blast Radius Inheritance Rule | correctness | `max(contributors)` floor with provenance annotation `Inherited [LEVEL] from [sub-skill-X] ([F-ID])` makes CROSS-SKILL scope assignment auditable and verifiable in the closing gate — prevents silent downgrade |
| **C-18** Closing Confirmation Multi-Gate Enforcement | format | Concentrating coverage + format compliance + inheritance compliance in one structured checklist is the minimal-surface-area enforcement pattern — all three quality axes gated in a single location |

**Scoring formula updated**: aspirational denominator 8 → 11 (`aspirational_pass/11 * 10`). Full-aspirational output still scores 100. Golden threshold unchanged (>= 80).

**R3 ship decision**: V-05 confirmed both quality upgrades (C-16 + C-17) survive at minimal prompt footprint, matching V-04 on all 15 criteria.
