**v3 written.** Here is the complete updated rubric:

---

# rhythm-behavior Rubric -- v3

**Skill**: `rhythm:behavior`
**Purpose**: Evaluate outputs from the rhythm-behavior orchestration skill, which runs five sub-skills (flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions) in declared order and produces a consolidated findings report ranked by blast radius.

**Scoring formula**:
```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
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
| **C-13** | **Dedicated Synthesis Step** | depth | **R2** |
| **C-14** | **Rationale Column Enforcement** | depth | **R2** |
| **C-15** | **CROSS-SKILL Findings as First-Class Table Citizens** | correctness | **R2** |

---

**What changed from v2 to v3:**

Three new aspirational criteria from the R2 excellence signals JSON:

| Criterion | Category | Pattern |
|-----------|----------|---------|
| **C-13** Dedicated Synthesis Step | depth | SYNTHESIS section between sub-skills and consolidation gives the model an isolated comparison moment -- without it C-09 fails because consolidation cannot rank and synthesize simultaneously |
| **C-14** Rationale Column Enforcement | depth | Table column > inline annotation: an empty cell is structurally visible as omission; annotation is silently skippable in dense prose (V-02 PARTIAL proved this) |
| **C-15** CROSS-SKILL Findings as First-Class Table Citizens | correctness | Cross-skill findings as table rows (Sub-Skill = CROSS-SKILL) are automatically included in C-11 coverage confirmation and C-03 blast radius ranking without extra instructions |

**Scoring formula updated**: aspirational denominator 5 -> 8 (`aspirational_pass/8 * 10`). Full-aspirational output still scores 100. Golden threshold unchanged (>= 80).
 one spec gap (missing, ambiguous, or
  underspecified requirement) and at least one contract violation (a behavior that breaks
  a declared interface, pre/post condition, or permission boundary) across the five
  simulation sections. These categories must be distinguishable in the output -- either
  by label, section, or explicit classification.
- **Pass condition**: At least one finding is classified (explicitly or by context) as a
  spec gap and at least one as a contract violation. Fail if all findings are of a single
  type, or if the output does not distinguish between the two categories.

---

## Recommended Criteria (output is better with these)

### C-05 -- Per-Finding Sub-Skill Attribution
- **Weight**: recommended
- **Category**: correctness
- **Text**: Each finding in the consolidated report cites the sub-skill that produced it
  (e.g., "trace-contract: ..."). Attribution must be present at the finding level, not only
  in section headers. This enables triage -- a reader must be able to trace any finding
  back to its simulation source without reading all five sections.
- **Pass condition**: Every finding in the consolidated report includes a sub-skill label
  or reference. Fail if any consolidated finding lacks attribution, or if attribution
  appears only at section level and not at finding level.

### C-06 -- Actionable Next Step for Top Finding
- **Weight**: recommended
- **Category**: depth
- **Text**: The highest blast-radius finding must include an actionable next step. The
  action must be specific to the finding (not a generic "investigate further") and must
  be addressable before implementation begins.
- **Pass condition**: The top-ranked finding includes a concrete, specific action (e.g.,
  "add a pre-condition guard to X", "clarify contract for Y in the spec", "resolve
  permission scope for Z"). Fail if the top finding has no action, or if the action is
  a generic placeholder.

### C-07 -- Sub-Skill Section Completeness
- **Weight**: recommended
- **Category**: coverage
- **Text**: Each of the five sub-skill simulation sections must contain at least one
  finding or a stated null result (explicit "no issues found in this sub-skill"). A
  section that is present but empty or that contains only a heading is not complete.
- **Pass condition**: All five sections have content -- either one or more findings or
  an explicit null-result declaration. Fail if any section is empty, heading-only, or
  skipped without a null-result statement.

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

### C-08 -- Blast Radius Justification
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each finding in the consolidated report includes a brief explanation of why
  it carries its assigned blast radius level. The justification must reference the scope
  of impact (e.g., which flows, contracts, or permission boundaries are affected) rather
  than stating blast radius as a bare label.
- **Pass condition**: Every finding includes a one-sentence rationale for its blast radius
  tier that names the affected scope. Fail if blast radius labels appear without
  justification, or if justification is present for the top finding only.

### C-09 -- Cross-Sub-Skill Synthesis
- **Weight**: aspirational
- **Category**: depth
- **Text**: The consolidated findings section identifies at least one finding that spans
  two or more sub-skills -- a pattern or conflict that only becomes visible when results
  from multiple sub-skills are read together. Cross-sub-skill findings must name the
  contributing sub-skills and explain the relationship.
- **Pass condition**: At least one finding in the consolidated report is explicitly labeled
  as cross-sub-skill, names the contributing sub-skills (two or more), and describes the
  relationship or compounding effect. Fail if all findings are traceable to a single
  sub-skill only.

### C-10 -- Self-Documenting Ranking Label
- **Weight**: aspirational
- **Category**: format
- **Text**: The consolidated findings section carries an explicit sort label stating the
  ranking direction (e.g., "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"). The label
  must appear adjacent to the ranked output -- in a table header, above the findings list,
  or as a section subheading -- making the ranking mechanism self-documenting without
  requiring the reader to infer it from position alone.
- **Pass condition**: An explicit sort-direction label is present adjacent to the
  consolidated findings ranking. Fail if the ranking is present but no label states the
  sort order, or if the label appears elsewhere in the output but not adjacent to the
  ranked list.
- **Origin**: R1 V-05 -- "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" label satisfied
  C-03 definitively without any other ranking mechanism. The label is the ranking evidence.

### C-11 -- Active Coverage Confirmation
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The consolidated findings section includes an explicit confirmation statement
  verifying that both required finding categories (spec-gap and contract-violation) are
  present. The confirmation must appear after the findings list as a meta-level check --
  not merely embedded in finding labels. If either category is absent, the output must
  re-examine prior sections before closing rather than proceeding with incomplete coverage.
  This converts C-04 from a passive structural requirement into a visible, active
  verification step.
- **Pass condition**: A confirmation statement appears after the findings list, naming at
  least one finding in each category. Fail if coverage confirmation is absent, if it
  appears only as a static label on individual findings without a summary-level check, or
  if the output closes without addressing a missing category.
- **Origin**: R1 V-05 -- "If either category is missing, go back and find at least one
  before closing the report" converted C-04 from a static check into an active correction
  loop.

### C-12 -- At-Discovery Attribution
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Findings carry their sub-skill, finding type (spec-gap or contract-violation),
  and blast radius labels within the sub-skill simulation sections where they are first
  discovered -- not only in the consolidated table. Attribution at the point of discovery
  makes the consolidation step mechanical rather than interpretive, and eliminates
  retrospective reclassification errors.
- **Pass condition**: Each finding in the sub-skill sections carries at minimum a blast
  radius indicator and a finding-type label at the point of discovery. Fail if attribution
  appears exclusively in the consolidated section and sub-skill sections contain only
  unlabeled narrative findings.
- **Origin**: R1 V-05 -- pre-opened findings table with append-throughout instruction
  embedded Sub-Skill, Finding Type, and Blast Radius at discovery time. Structural reason
  C-03/C-04/C-05 were satisfied without extra enforcement in consolidation.

### C-13 -- Dedicated Synthesis Step
- **Weight**: aspirational
- **Category**: depth
- **Text**: A named SYNTHESIS section appears between the last sub-skill section and the
  consolidated findings table. The section gives the model an isolated moment to identify
  cross-sub-skill patterns -- separate from the consolidation step, which must simultaneously
  rank all findings. Without a dedicated synthesis step, C-09 systematically fails because
  a consolidation pass cannot perform ranking and cross-skill comparison at the same time.
  A null result ("Synthesis: no cross-sub-skill patterns found") is a valid output and
  satisfies this criterion; the section must exist regardless of whether patterns are found.
- **Pass condition**: A SYNTHESIS section (or equivalently labeled step) appears after all
  five sub-skill sections and before the consolidated findings table. It contains at least
  one cross-sub-skill observation naming the contributing sub-skills, or an explicit
  null-result statement. Fail if no synthesis section exists, if it is merged into the
  consolidation section, or if it appears after the consolidated findings.
- **Origin**: R2 -- V-01/V-02 both FAIL C-09 (no SYNTHESIS section); V-03/V-04/V-05 all
  PASS (dedicated SYNTHESIS section present). "Without this step C-09 fails because
  consolidation cannot perform ranking and cross-skill synthesis simultaneously."

### C-14 -- Rationale Column Enforcement
- **Weight**: aspirational
- **Category**: depth
- **Text**: Blast radius justification (C-08) is enforced via a dedicated table column
  ("Blast Radius Rationale" or equivalent) rather than inline annotation embedded in prose.
  A missing inline annotation is invisible in dense output and can be silently omitted; an
  empty table cell is structurally visible as an omission. Column pressure forces every row
  to be filled and is categorically more reliable than annotation for complete rationale
  coverage across all findings.
- **Pass condition**: The consolidated findings table includes a named column for blast
  radius rationale. Every row has the column populated with a sentence naming the affected
  scope. Fail if rationale appears only as inline prose without a column structure, if the
  column exists but any row is empty, or if the column is absent and rationale appears only
  as embedded annotation.
- **Origin**: R2 -- V-02 scored PARTIAL on C-08 despite mandating inline annotation;
  V-01/V-04/V-05 all PASS via structural column. "Column pressure is categorically more
  reliable than inline annotation because a model cannot complete a table row without
  filling the column."

### C-15 -- CROSS-SKILL Findings as First-Class Table Citizens
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-sub-skill findings identified in the SYNTHESIS step must appear as rows
  in the consolidated findings table with Sub-Skill = CROSS-SKILL (or equivalent label) --
  structurally identical to per-sub-skill findings. Synthesis findings that exist only as
  prose in the SYNTHESIS section are invisible to the coverage confirmation (C-11) and blast
  radius ranking (C-03). Promoting them to table rows makes them automatically included in
  both verification passes without extra instructions.
- **Pass condition**: At least one finding row in the consolidated findings table carries a
  cross-skill sub-skill label (e.g., "CROSS-SKILL", "flow-lifecycle + trace-contract"). Fail
  if cross-sub-skill findings are described only in the SYNTHESIS section prose without a
  corresponding table entry, or if the findings table contains no cross-skill rows despite a
  non-null SYNTHESIS section.
- **Origin**: R2 -- "CROSS-SKILL Sub-Skill label makes synthesis findings first-class table
  citizens structurally consistent with per-sub-skill findings and verifiable in the coverage
  summary and closing confirmation check."

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric for rhythm-behavior (successor to narrate-behavior) |
| v2 | 2026-03-17 | Added C-10/C-11/C-12 from R1 excellence signals (V-05 patterns); aspirational denominator 2 -> 5 |
| v3 | 2026-03-17 | Added C-13/C-14/C-15 from R2 excellence signals; aspirational denominator 5 -> 8 |
