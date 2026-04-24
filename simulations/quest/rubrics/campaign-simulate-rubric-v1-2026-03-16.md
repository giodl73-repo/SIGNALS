---
skill: quest-rubric
skill_target: campaign-simulate
date: 2026-03-16
version: 1
---

# Scoring Rubric: campaign-simulate

## Skill Summary

Orchestrates five sub-skills in sequence — flow-lifecycle, flow-conversation, trace-state,
trace-contract, trace-permissions — and produces a unified simulation findings report with
findings ranked by blast radius. Used before implementation to surface spec gaps and
contract violations.

---

## Essential Criteria (60 points total, ~12 pts each)

### C-01 — All Five Sub-Skills Invoked
- **Weight**: essential
- **Category**: correctness
- **Text**: The output demonstrates that all five sub-skills were executed: flow-lifecycle,
  flow-conversation, trace-state, trace-contract, and trace-permissions. Each must appear
  as a named section or clearly attributed source in the report.
- **Pass condition**: Report contains findings or results attributed to each of the five
  sub-skills by name. A sub-skill section may be empty (no findings) but must be present
  and acknowledged. Fail if any sub-skill is absent or silently skipped.

### C-02 — Sequential Execution Order Respected
- **Weight**: essential
- **Category**: behavior
- **Text**: Sub-skills are executed and reported in the specified order: flow-lifecycle →
  flow-conversation → trace-state → trace-contract → trace-permissions. Later findings may
  reference earlier ones but not vice versa.
- **Pass condition**: Section headers or execution log shows the five skills in order with
  no reordering. Fail if the sequence is shuffled or if later skills appear before earlier
  ones in the report structure.

### C-03 — Findings Report Produced
- **Weight**: essential
- **Category**: format
- **Text**: A consolidated findings report document is output. It must be a single unified
  artifact (not five separate skill outputs) that synthesizes results across all sub-skills.
- **Pass condition**: Output is a single report with a title, date, topic context, and a
  multi-skill findings section. Fail if the output is a raw dump of five independent skill
  outputs without synthesis.

### C-04 — Blast Radius Ranking Applied
- **Weight**: essential
- **Category**: correctness
- **Text**: Findings are ranked by blast radius — the scope of downstream impact if the
  finding is ignored. High blast radius = many flows/components affected; low = isolated.
  The ranking must be explicit, not implied.
- **Pass condition**: Report contains a ranked findings list (numbered or tiered) with
  blast radius as the stated sort key. At least one finding is labeled or annotated with
  its blast radius scope. Fail if findings are unranked, alphabetical, or sorted by any
  other key without blast radius justification.

### C-05 — At Least One Spec Gap or Contract Violation Identified
- **Weight**: essential
- **Category**: coverage
- **Text**: The report surfaces at least one concrete spec gap (something underspecified or
  missing from the target spec) or contract violation (a boundary condition where caller
  and callee assumptions diverge). The finding must name the specific spec location or
  contract boundary affected.
- **Pass condition**: Report contains at least one finding with: (a) finding type labeled
  as spec-gap or contract-violation, (b) specific reference to where in the spec the gap
  or violation occurs, (c) description of what is missing or mismatched. Fail if all
  findings are vague observations without spec anchoring.

---

## Recommended Criteria (30 points total, ~10 pts each)

### C-06 — Finding Depth: Source + Location + Impact
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes three fields: (1) source sub-skill that discovered it,
  (2) spec/contract location where it was found, (3) impact description of what breaks
  if unresolved.
- **Pass condition**: At least 80% of findings include all three fields. Pass if the report
  uses a consistent finding schema (e.g., table or structured list) that captures source,
  location, and impact. Partial pass (half credit) if fields are present but inconsistently
  populated.

### C-07 — Cross-Sub-Skill Coverage (Findings Span Multiple Skills)
- **Weight**: recommended
- **Category**: coverage
- **Text**: The ranked findings list draws from at least three of the five sub-skills,
  demonstrating that the campaign exercised the full skill set rather than concentrating
  findings in one area.
- **Pass condition**: Findings section attributes results to three or more distinct
  sub-skills. Fail if all findings come from one or two sub-skills with the rest showing
  no results and no explanation of why.

### C-08 — Actionable Remediation Guidance
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes a remediation note — a specific action the spec author
  or implementer should take to resolve the gap or violation. Guidance must be concrete
  (e.g., "add error state X to flow-lifecycle spec section 3") not generic ("fix the spec").
- **Pass condition**: At least 60% of findings include a remediation note with a named
  target (spec section, contract boundary, or interface) and a described action. Fail if
  remediations are absent or consist only of generic advice.

---

## Aspirational Criteria (10 points total, ~5 pts each)

### C-09 — Cross-Skill Pattern Detection
- **Weight**: aspirational
- **Category**: depth
- **Text**: The report identifies at least one finding that compounds across multiple
  sub-skills — a root cause that shows up in flow AND trace, or a contract gap that
  affects both state and permissions. These compounding findings are flagged separately
  as higher-priority.
- **Pass condition**: Report contains a "compounding findings" or "cross-skill patterns"
  section with at least one finding explicitly linked to two or more sub-skills and
  elevated in the blast radius ranking because of the compounding effect.

### C-10 — Blast Radius Rationale Documented
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The blast radius ranking is not just asserted — each high-blast finding
  includes a rationale explaining which downstream flows, components, or contracts are
  affected and why the scope is wide.
- **Pass condition**: At least the top three ranked findings include explicit blast radius
  rationale (e.g., "affects all flows that call X because Y"). Fail if rankings are
  present but unexplained.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Score Range | Interpretation |
|-------------|---------------|
| 100         | Golden — ship as reference output |
| 80–99       | Passes — meets bar for golden with minor gaps |
| 60–79       | Partial — essential gaps present, needs revision |
| < 60        | Fail — essential criteria not met |

---

## Evaluator Notes

- **C-01 empty sections**: A sub-skill may legitimately find nothing. An empty section is
  acceptable if it explicitly states "no findings" — silence is a fail.
- **C-04 blast radius**: Ranking by severity alone is not sufficient. The key concept is
  *downstream scope* — how many other parts of the system are affected if this is ignored.
- **C-05 anchoring**: "The spec is unclear" without a location reference is not a pass.
  The finding must point to a specific section, step, or contract edge.
- **C-09 compounding**: Two findings that happen to come from two skills but describe
  different problems do not count. The finding must describe a single root cause that
  manifests in multiple skills.
