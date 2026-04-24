Rubric written to `simulations/quest/rubrics/rhythm-behavior-rubric-2026-03-17.md`.

**Summary:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential | 4 | C-01 sequence declaration, C-02 unified report, C-03 blast radius ranking, C-04 spec gap + contract violation coverage |
| Recommended | 3 | C-05 per-finding sub-skill attribution, C-06 actionable next step for top finding, C-07 sub-skill section completeness |
| Aspirational | 2 | C-08 blast radius justification, C-09 cross-sub-skill synthesis |

**Scoring**: composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10). Golden = all 4 essential pass + composite ≥ 80.

The two hardest essential criteria are C-03 (explicit ranking, not just prose order) and C-04 (both categories present and distinguishable) — these catch the most common failure modes for orchestration skills: unlabeled findings and category collapse.
 flow-conversation, trace-state, trace-contract, trace-permissions)
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

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric for rhythm-behavior (successor to narrate-behavior) |
