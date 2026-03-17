---
skill: quest-rubric
skill_target: narrate-behavior
date: 2026-03-17
version: 1
---

# narrate-behavior Rubric — v1

**Skill**: `narrate-behavior`
**Namespace**: narrate
**Audience**: dev+architect
**Description**: Run the full technical simulation campaign. Orchestrates: flow-lifecycle,
flow-conversation, trace-state, trace-contract, trace-permissions in sequence. Output:
simulation findings report ranked by blast radius. Use before implementation to find spec
gaps and contract violations.

**Artifact**: `simulations/campaign/{topic}-simulate-{date}.md`

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 points total, 20 pts each)

### C-01 — Sub-Skill Execution Sequence Preserved
- **Weight**: essential
- **Category**: correctness
- **Text**: The five sub-skills execute in the declared sequence: flow-lifecycle →
  flow-conversation → trace-state → trace-contract → trace-permissions. The report structure
  must reflect this order — each sub-skill has its own section, and the sections appear in
  sequence. No sub-skill may be silently skipped without an explicit disposition.
- **Pass condition**: Report contains five sub-skill sections in the correct order. Each
  section is labeled with the sub-skill name. Fail if the sequence is reordered, if any
  sub-skill section is absent without a "skipped" declaration, or if sections are merged
  without identifying their constituent sub-skills.

### C-02 — Unified Findings Report Produced
- **Weight**: essential
- **Category**: format
- **Text**: A single consolidated findings report document is output as the campaign artifact.
  It must synthesize results across all sub-skills into one artifact — not five separate
  outputs stapled together. The report must include: a title, the topic context, the date,
  and a multi-skill findings section.
- **Pass condition**: Output is a single report with title, date, topic context, and a
  findings section that draws from multiple sub-skills. Fail if the output is a raw dump of
  five independent sub-skill outputs without synthesis, or if no consolidated findings
  section exists.

### C-03 — Blast Radius Ranking Applied
- **Weight**: essential
- **Category**: correctness
- **Text**: Findings are ranked by blast radius — the scope of downstream impact if the
  finding is not addressed before implementation. High blast radius = many flows, components,
  or contracts affected; low blast radius = isolated, contained impact. The ranking must be
  explicit, not implied by position alone.
- **Pass condition**: Report contains a ranked findings list (numbered or tiered) with blast
  radius as the stated sort key. At least one finding is labeled or annotated with its blast
  radius scope. Fail if findings are unranked, sorted alphabetically, or sorted by any key
  other than blast radius without justification.

### C-04 — At Least One Spec Gap or Contract Violation Identified
- **Weight**: essential
- **Category**: coverage
- **Text**: The report surfaces at least one concrete spec gap (something underspecified or
  absent from the target spec) or contract violation (a boundary condition where caller and
  callee assumptions diverge). The finding must name the specific spec location or contract
  boundary affected.
- **Pass condition**: Report contains at least one finding with: (a) finding type labeled as
  spec-gap or contract-violation, (b) a specific reference to where in the spec the gap or
  violation occurs, (c) a description of what is missing or mismatched. Fail if all findings
  are vague observations without spec anchoring.

---

## Recommended Criteria (30 points total, 10 pts each)

### C-05 — Finding Schema: Source + Location + Impact
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes three fields as distinct labeled entries: (1) source
  sub-skill that discovered it, (2) spec or contract location where it was found, (3) impact
  description of what breaks if the finding is unresolved before implementation. Impact must
  be a standalone labeled field — merging impact into the problem description does not
  satisfy this criterion.
- **Pass condition**: At least 80% of findings include all three fields as separately labeled
  entries. Pass if the report uses a consistent finding schema (e.g., table or structured
  list) that captures source, location, and impact as distinct columns or fields. Partial
  pass (half credit) if fields are present but inconsistently populated, or if impact is
  merged with the problem description.

### C-06 — Cross-Sub-Skill Coverage
- **Weight**: recommended
- **Category**: coverage
- **Text**: The ranked findings list draws from at least three of the five sub-skills,
  demonstrating that the campaign exercised the full skill set rather than concentrating
  findings in one area. Sub-skill attribution must be explicit — each finding identifies
  which sub-skill surface produced it.
- **Pass condition**: Findings section attributes results to three or more distinct
  sub-skills by name. Fail if all findings are attributed to one or two sub-skills, or if
  sub-skill attribution is absent. Partial pass (half credit) if attribution is present for
  exactly two sub-skills.

### C-07 — Remediation Guidance Present
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes a remediation field — a concrete recommended action, spec
  update, or contract clarification that would close the finding before implementation. The
  remediation must be a standalone labeled field, not folded into the impact or problem
  description.
- **Pass condition**: At least 80% of findings include a populated remediation field as a
  distinct labeled entry. Partial pass (half credit) if remediation is present but merged
  with impact, or is a generic placeholder ("address this") rather than a concrete action.

---

## Aspirational Criteria (10 points total, 5 pts each)

### C-08 — Severity Classification Applied
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each finding carries an explicit severity label (e.g., critical/high/medium/low
  or an equivalent named scale). The scale must be defined or cited in the report before
  it is applied. Severity enables readers to triage findings without reading the full blast
  radius rationale.
- **Pass condition**: All findings have a severity label from a declared scale. The scale
  definition appears in the report header or a preamble section. Fail if severity is absent
  from any finding, or if the scale is applied inconsistently without a definition.

### C-09 — Empty Sub-Skill Disposition Declared
- **Weight**: aspirational
- **Category**: format
- **Text**: Sub-skills that produce no findings explicitly declare "no findings" with a brief
  rationale (e.g., "scope clean under current spec version") rather than being silently
  omitted. Silent omission is indistinguishable from a skipped execution — an explicit
  disposition is needed for the report to be auditable.
- **Pass condition**: Every sub-skill section — including zero-finding sub-skills — contains
  an explicit disposition. Fail if any sub-skill section is absent or blank. Partial pass
  (half credit) if a "no findings" declaration is present but carries no rationale.

---

## Version History

| Version | Criteria | Essential | Recommended | Aspirational | Raw Max |
|---------|----------|-----------|-------------|--------------|---------|
| v1      | C-01–C-09 | C-01–C-04 | C-05–C-07   | C-08–C-09    | C-04×3 + C-07×3 + C-09×2 = ~100 |
