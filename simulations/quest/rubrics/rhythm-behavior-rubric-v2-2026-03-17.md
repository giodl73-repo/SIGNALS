Written to `simulations/quest/rubrics/rhythm-behavior-rubric-v2-2026-03-17.md`.

---

**What changed from v1 to v2:**

Three new aspirational criteria extracted from the R1 scorecard's excellence signals, all sourced from V-05:

| Criterion | Category | Pattern |
|-----------|----------|---------|
| **C-10** Self-Documenting Ranking Label | format | Explicit sort label adjacent to ranked output ("Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW") makes C-03 self-evident without the reader inferring from position |
| **C-11** Active Coverage Confirmation | coverage | Post-findings confirmation statement naming one finding in each category -- converts C-04 from a static pass/fail check into a visible correction loop that re-examines sections if a category is missing |
| **C-12** At-Discovery Attribution | correctness | Sub-skill, finding type, and blast radius labels applied at the point of discovery inside sub-skill sections, not retrospectively during consolidation -- makes the consolidation step mechanical |

**Scoring formula updated**: aspirational denominator changes from 2 to 5, so aspirational_pass/5 * 10. A full-aspirational output now scores 100 (vs 90 at R1). The golden threshold (composite >= 80) is unchanged.
mat
- **Text**: The output must open with a declaration of the five sub-skills in execution order
  (flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions)
  before any simulation section begins. The simulation sections must appear in that declared
  order. Reordering without updating the declaration is a violation.
- **Pass condition**: A sequence declaration naming all five sub-skills in order appears
  before the first simulation section. The executed order matches. Fail if no declaration
  exists, if fewer than five sub-skills are named, or if the executed order diverges from
  the declared order.

### C-02 -- Single Unified Report
- **Weight**: essential
- **Category**: format
- **Text**: All five sub-skill simulation sections and the consolidated findings must be
  produced as one continuous output -- not as five separate outputs, not as a series of
  stubs with a promise to continue, not as a partial report. The full campaign result must
  be readable end-to-end without interruption.
- **Pass condition**: Output contains all five simulation sections and a consolidated
  findings section within a single continuous response. Fail if any section is absent,
  deferred, or referenced but not produced.

### C-03 -- Blast Radius Ranking Present
- **Weight**: essential
- **Category**: correctness
- **Text**: The consolidated findings section must rank findings by blast radius. Blast
  radius is the scope of impact if the finding is not addressed before implementation.
  Rankings must be explicit (e.g., numbered list, HIGH/MEDIUM/LOW labels, or ordinal
  position with stated rationale) -- not implied by prose order alone.
- **Pass condition**: Consolidated findings contain an explicit ranking mechanism applied
  to all findings. At minimum the top-blast-radius finding is identified and distinguishable
  from lower-ranked findings. Fail if findings are listed without any ranking signal.

### C-04 -- Spec Gap and Contract Violation Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output must surface at least one spec gap (missing, ambiguous, or
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
- **Origin**: R1 excellence signal -- V-05 "Sorted by Blast Radius: WIDE -> MEDIUM ->
  NARROW" label satisfied C-03 definitively without any other ranking mechanism. The label
  is the ranking evidence.

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
- **Origin**: R1 excellence signal -- V-05 "If either category is missing, go back and
  find at least one before closing the report" converted C-04 from a static check into an
  active correction loop. The highest-value C-04 enforcement pattern observed in Round 1.

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
- **Origin**: R1 excellence signal -- V-05 pre-opened findings table with append-throughout
  instruction embedded Sub-Skill, Finding Type, and Blast Radius at discovery time. This is
  the structural reason C-03/C-04/C-05 were satisfied without extra enforcement in
  consolidation.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric for rhythm-behavior (successor to narrate-behavior) |
| v2 | 2026-03-17 | Added C-10/C-11/C-12 from R1 excellence signals (V-05 patterns); updated aspirational denominator from 2 to 5 in scoring formula |
