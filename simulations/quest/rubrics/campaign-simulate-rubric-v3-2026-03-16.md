Rubric v3 written to `simulations/quest/rubrics/campaign-simulate-rubric-v3-2026-03-16.md`.

---

**Three new aspirational criteria (C-14, C-15, C-16):**

**C-14 — Vacuous-Filter Acknowledgment** (from R2 Pattern 2)
The counterpart to C-12's vacuous-pass: when the rejection gate fires but produces *zero* rejections, the log must explicitly flag the empty-rejection state for recalibration rather than silently accepting it as evidence of filtering. A structurally complete gate that happens to reject nothing is not evidence of filtering judgment — it's a schema pass with no behavioral content.

**C-15 — Active Negative Comparison in Cross-Skill Sections** (from R2 Pattern 3)
When no compounding patterns are found, the section must name at least one candidate pairing that was *compared before being declared non-compounding*. "No patterns detected" without named comparisons is passive omission; naming F-01 vs. F-03 and stating why they don't share a root cause proves active negative work was performed. Passes vacuously when C-09 fires.

**C-16 — Structural Coverage Symmetry** (from R2 Pattern 1)
When multiple aspirational axes are targeted, both the filtering axis (C-13: gate with named rules) and the empty-state axis (C-11: templates across all section types) must be structurally enforced — not one structural and one relying on model judgment. Mixed-mode coverage makes the judgment-dependent axis the dominant failure path under distribution. Partial credit when one axis is structural and the other is not.

**Scoring updated**: aspirational pool expands from 10 to 16 pts (8 criteria × 2 pts), total max 96, normalization divisor 0.96.
 C-03 — Findings Report Produced
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
- **Text**: Findings are ranked by blast radius -- the scope of downstream impact if the
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

## Recommended Criteria (30 points total, 10 pts each)

### C-06 — Finding Depth: Source + Location + Impact
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes three fields as distinct labeled entries: (1) source
  sub-skill that discovered it, (2) spec/contract location where it was found, (3) impact
  description of what breaks if unresolved. Impact must be a standalone labeled field --
  merging impact into the problem description field does not satisfy this criterion.
- **Pass condition**: At least 80% of findings include all three fields as separately
  labeled entries. Pass if the report uses a consistent finding schema (e.g., table or
  structured list) that captures source, location, and impact as distinct columns or
  fields. Partial pass (half credit) if fields are present but inconsistently populated
  or if impact is merged with the problem description.

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
- **Text**: Each finding includes a remediation note -- a specific action the spec author
  or implementer should take to resolve the gap or violation. Guidance must be concrete
  (e.g., "add error state X to flow-lifecycle spec section 3") not generic ("fix the spec").
  The remediation rule applies at the finding level, not only in a closing summary section.
- **Pass condition**: At least 60% of findings include a remediation note with a named
  target (spec section, contract boundary, or interface) and a described action. Fail if
  remediations are absent, consist only of generic advice, or appear only in a summary
  section without being attached to individual findings.

---

## Aspirational Criteria (16 points total, 2 pts each)

### C-09 — Cross-Skill Pattern Detection
- **Weight**: aspirational
- **Category**: depth
- **Text**: The report identifies at least one finding that compounds across multiple
  sub-skills -- a root cause that shows up in flow AND trace, or a contract gap that
  affects both state and permissions. These compounding findings are flagged separately
  as higher-priority.
- **Pass condition**: Report contains a "compounding findings" or "cross-skill patterns"
  section with at least one finding explicitly linked to two or more sub-skills and
  elevated in the blast radius ranking because of the compounding effect. An empty
  cross-skill patterns section must explicitly state that no compounding patterns were
  detected and briefly why.

### C-10 — Blast Radius Rationale Documented
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The blast radius ranking is not just asserted -- each high-blast finding
  includes a rationale explaining which downstream flows, components, or contracts are
  affected and why the scope is wide. Excellence: rationale appears as a field on the
  finding record itself (for system-wide and cross-skill findings), not only appended
  in the ranked output section.
- **Pass condition**: At least the top three ranked findings include explicit blast radius
  rationale (e.g., "affects all flows that call X because Y"). Fail if rankings are
  present but unexplained.

### C-11 — Empty-State Discipline Across All Sections
- **Weight**: aspirational
- **Category**: format
- **Text**: Every structured section of the report -- sub-skill sections, cross-skill
  patterns, summary tables, execution logs -- explicitly acknowledges its state when
  empty. No section is blank or absent without a stated reason. Empty is acceptable;
  silent is not. This extends C-01's "no findings must say why" rule to all report
  sections, not only sub-skill sections.
- **Pass condition**: Any section with zero entries includes an explicit empty-state
  statement (e.g., "No cross-skill patterns detected -- findings from each sub-skill
  describe distinct root causes"). Fail if any structured section is blank or omitted
  without acknowledgment.

### C-12 — Compounding Elevation Documentation
- **Weight**: aspirational
- **Category**: depth
- **Text**: When a finding's blast radius is elevated because it compounds across
  sub-skills (C-09), the report documents the elevation explicitly: what scope the
  finding would carry in isolation versus what scope it receives due to the cross-skill
  root cause. Not just "this is a compounding finding" but "this finding is promoted
  from component-wide to system-wide because the same root cause manifests in
  trace-state and flow-lifecycle."
- **Pass condition**: Any compounding finding (C-09) that was elevated in blast radius
  includes an explicit before/after scope annotation or a "promoted to" statement with
  rationale. Passes vacuously when no compounding findings exist (C-09 did not fire) --
  see evaluator note.

### C-13 — Discriminating Rejection of Weak Observations
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The report demonstrates that weak observations -- those that could not be
  anchored to a spec location or ranked by blast radius -- were actively evaluated and
  rejected, not silently dropped. A brief note (e.g., "observations not elevated to
  findings" or "excluded: could not name spec location") shows the model applied the
  anchoring rules with judgment rather than just happening to produce anchored findings.
- **Pass condition**: Report contains at least one instance of explicit filtering language
  showing that a candidate observation was evaluated and rejected because it failed an
  anchoring rule (no spec location, no blast radius scope, or vague problem statement).
  Fail if the report contains only final findings with no signal that weaker observations
  were considered and filtered.

### C-14 — Vacuous-Filter Acknowledgment
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a rejection gate (C-13) fires but produces zero rejections -- all
  candidate observations passed the anchoring rules -- the filter log must explicitly
  flag this as an unusual state requiring re-evaluation rather than accepting it as
  evidence of filtering. Zero rejections from a well-calibrated gate is plausible but
  statistically uncommon; silently accepting it closes the loop without validating
  whether the gate rules were well-scoped. A note such as "Filter applied -- all N
  candidates passed. Revisit: verify gate rules are not underspecified" closes the
  vacuous-pass trap.
- **Pass condition**: If and only if the rejection gate produces zero rejections, the
  log includes an explicit re-evaluation note acknowledging the empty-rejection result
  and flagging it for recalibration. Passes vacuously when at least one rejection is
  logged (the vacuous-pass trap cannot fire). Fail if the filter log ends with zero
  rejections and no acknowledgment of that state.

### C-15 — Active Negative Comparison in Cross-Skill Sections
- **Weight**: aspirational
- **Category**: depth
- **Text**: When no compounding patterns are found, the cross-skill patterns section
  must name at least one candidate pairing that was actively compared and declared
  non-compounding, with a brief reason. Passive absence ("no patterns detected") does
  not prove the comparison was made; naming the candidates that were evaluated and
  explaining why they were not elevated does. This forces active negative work -- the
  model must demonstrate it looked before reporting nothing, not simply omit the section.
- **Pass condition**: A cross-skill patterns section that concludes with no compounding
  findings includes at least one explicit comparison entry (e.g., "F-01 and F-03
  compared -- distinct root causes; F-01 is a state gap, F-03 is a contract boundary
  mismatch with no shared origin"). Passes vacuously when C-09 fires and at least one
  compounding pattern is reported (active work is demonstrated by the finding itself).
  Fail if the cross-skill patterns section declares no patterns without naming any
  candidates considered.

### C-16 — Structural Coverage Symmetry
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When the report targets multiple aspirational criteria simultaneously, the
  structural mechanisms used must cover both the filtering axis (C-13: explicit rejection
  gate with named rules) and the empty-state axis (C-11: templates or discipline for all
  section types) rather than one axis being structurally enforced while the other is left
  to model judgment. Mixed-mode coverage -- structural on one axis, judgment-dependent on
  the other -- creates asymmetric confidence: the axis relying on judgment becomes the
  dominant failure path under distribution. Both axes must be verifiable from the report
  structure alone without assuming model compliance.
- **Pass condition**: The report provides observable structural evidence for both the
  filtering axis (a gate log or filtering schema with named rules, not just clean output)
  and the empty-state axis (explicit null-result statements or typed templates across all
  section types, not only sub-skill sections). Partial pass (half credit) if one axis is
  structural and the other relies on model judgment with no structural trace. Fail if
  neither axis has structural evidence.

---

## Scoring Formula

```
raw        = essential_score + recommended_score + aspirational_score
           = (C-01..C-05 at 10 pts each)
           + (C-06..C-08 at 10 pts each)
           + (C-09..C-16 at 2 pts each)
           max = 50 + 30 + 16 = 96

normalized = raw / 0.96
```

> PASS = full points, PARTIAL = half points, FAIL = 0.

**Golden threshold**: All 5 essential criteria pass AND normalized score >= 80.

| Score Range | Interpretation |
|-------------|----------------|
| 100         | Golden -- ship as reference output |
| 80-99       | Passes -- meets bar for golden with minor gaps |
| 60-79       | Partial -- essential gaps present, needs revision |
| < 60        | Fail -- essential criteria not met |

---

## Evaluator Notes

- **C-01 empty sections**: A sub-skill may legitimately find nothing. An empty section is
  acceptable if it explicitly states "no findings" and briefly why -- silence is a fail.
- **C-04 blast radius**: Ranking by severity alone is not sufficient. The key concept is
  *downstream scope* -- how many other parts of the system are affected if this is ignored.
- **C-05 anchoring**: "The spec is unclear" without a location reference is not a pass.
  The finding must point to a specific section, step, or contract edge. A finding without
  a spec location is not a finding -- it is a guess.
- **C-06 impact isolation**: Impact folded into a combined "what is wrong" field is a
  partial pass, not a full pass. A reader must be able to scan the impact field alone to
  understand consequences without re-reading the problem description.
- **C-07 coverage risk**: Blast-radius-first framing can cause authors to skip low-blast
  sub-skills. Evaluators should check whether low-blast sub-skills (trace-permissions,
  trace-contract) have genuine "no findings" explanations vs. were silently omitted
  because their findings would rank poorly.
- **C-08 remediation location**: Remediation notes must attach to individual findings, not
  only appear in a closing summary. A single "recommendations" section at the end does not
  satisfy C-08 if individual findings lack remediation fields.
- **C-09 compounding**: Two findings that happen to come from two skills but describe
  different problems do not count. The finding must describe a single root cause that
  manifests in multiple skills.
- **C-10 schema vs. ranked section**: The stronger form (rationale as a field on the
  finding record for high-scope findings) is the excellence target. The minimum pass is
  rationale present on the top-3 ranked findings anywhere in the report.
- **C-12 vacuous pass**: When no compounding findings exist (C-09 did not fire), C-12
  passes vacuously -- there is no elevation to document. Evaluators should note this so
  it does not inflate scores in campaigns with no cross-skill patterns.
- **C-13 filtering language**: The note does not need to be lengthy. One line ("two
  observations excluded -- no spec location could be named") satisfies the criterion.
  The absence of any such note when findings seem unusually clean is a signal to probe.
- **C-14 vacuous-filter trap**: Zero rejections from a gate is the structural analogue
  of the vacuous-pass problem in C-12. Both arise when a structural mechanism satisfies
  its schema while providing no positive evidence of the behavior it is meant to enforce.
  The pattern: when the structural mechanism's output is empty (no rejections, no
  elevation), require an explicit acknowledgment that the empty result was noticed and
  validated -- not just accepted.
- **C-15 active negative work**: The criterion is failed most often by passive omission --
  the model writes "no cross-skill patterns detected" without naming what it compared.
  Evaluators should treat the absence of named comparisons as a judgment signal: a model
  that names the comparisons it made demonstrates it ran the process; a model that only
  reports the conclusion may have skipped it.
- **C-16 symmetry check**: The evaluator should identify which aspirational axes the
  variation targets, then check whether each has a structural trace. A filter log with
  named rules is structural evidence for the filtering axis. Six section-type templates
  is structural evidence for the empty-state axis. "The model happened to produce anchored
  findings" is not structural evidence for either. Partial credit applies when one axis is
  demonstrably structural and the other is not.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational (C-09, C-10) |
| v2 | 2026-03-16 | +C-11 empty-state all sections; +C-12 compounding elevation; +C-13 discriminating rejection; C-06 impact isolation clarified; C-08 remediation location clarified; aspirational pool 10 pts across 5 criteria (2 pts each) |
| v3 | 2026-03-16 | +C-14 vacuous-filter acknowledgment (R2 Pattern 2); +C-15 active negative comparison (R2 Pattern 3); +C-16 structural coverage symmetry (R2 Pattern 1); aspirational pool 16 pts across 8 criteria (2 pts each); normalization divisor updated to 0.96 |
