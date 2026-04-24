Written to `simulations/quest/rubrics/campaign-simulate-rubric-v8-2026-03-16.md`.

---

**Two patterns extracted from Round 7:**

**C-26 — Enforcement Rules Name Their Failure Mode as a Structural Violation**
Source: V-05 vs V-04 delta. Both score 96.5, but V-05 uses "structural violation" framing when naming what a breach looks like — making the enforcement rule falsifiable in place. V-04's enforcement language uses positive framing only ("the report must...") with no named failure mode. Gap over C-17: C-17 requires declared axes to be fulfilled in execution. C-26 requires that each axis rule also names its failure mode, so both the pass state and fail state are named and a reader can test "did a structural violation occur?" rather than "was this done well enough?"

**C-27 — Aggregation Blocks Carry a Self-Characterization Statement**
Source: V-05 vs V-04 delta. V-05's ANNEX contains a self-characterization statement declaring its relationship to per-scope evidence ("aggregates per-scope T-1 evidence and does not substitute for it"). V-04's ANNEX is structurally present but makes no meta-claim about its own role. Without self-characterization a reader cannot tell whether the block is authoritative (replaces per-scope records) or additive (supplements them). Gap over C-25: C-25 requires per-scope T-1 evidence to exist; C-27 requires the aggregation block to declare its epistemic status so the reader knows where the authoritative record lives.

**Scoring update:**
- 17 → 19 aspirational criteria
- Raw max: 114 → 118
- Divisor: 1.14 → 1.18
- Normalized max: 100 (unchanged)
ycle →
  flow-conversation → trace-state → trace-contract → trace-permissions. Later findings
  may reference earlier ones but not vice versa.
- **Pass condition**: Section headers or execution log shows the five skills in order with
  no reordering. Fail if the sequence is shuffled or if later skills appear before earlier
  ones in the report structure.

### C-03 — Findings Report Produced
- **Weight**: essential
- **Category**: format
- **Text**: A consolidated findings report document is output. It must be a single unified
  artifact (not five separate skill outputs) that synthesizes results across all
  sub-skills.
- **Pass condition**: Output is a single report with a title, date, topic context, and a
  multi-skill findings section. Fail if the output is a raw dump of five independent
  skill outputs without synthesis.

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
- **Text**: The report surfaces at least one concrete spec gap (something underspecified
  or missing from the target spec) or contract violation (a boundary condition where
  caller and callee assumptions diverge). The finding must name the specific spec location
  or contract boundary affected.
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
  description of what breaks if unresolved. Impact must be a standalone labeled field —
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
  sub-skills by name. Fail if all findings are attributed to one or two sub-skills or if
  sub-skill attribution is absent. Partial pass (half credit) if attribution is present
  for exactly two sub-skills.

### C-08 — Remediation Guidance Present
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes a remediation field — a concrete recommended action,
  spec update, or contract clarification that would close the finding. The remediation
  must be a standalone labeled field, not folded into the impact or description field.
- **Pass condition**: At least 80% of findings include a populated remediation field as a
  distinct labeled entry. Partial pass (half credit) if remediation is present but merged
  with impact or is a generic placeholder ("address this") rather than a concrete action.

---

## Aspirational Criteria (38 points total, 2 pts each)

### C-09 — Severity Classification Applied
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each finding carries an explicit severity label (e.g., critical/high/medium/
  low or equivalent named scale). The scale is defined or cited in the report.
- **Pass condition**: All findings have a severity label from a declared scale. Fail if
  severity is absent or if the scale is applied inconsistently without a definition.

### C-10 — Finding Count by Sub-Skill Reported
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The report includes a summary table or section listing finding counts per
  sub-skill, including sub-skills that produced zero findings.
- **Pass condition**: A count table or equivalent section is present with a row or entry
  for each of the five sub-skills, including zeroes. Fail if any sub-skill is absent from
  the summary.

### C-11 — Empty Sub-Skill Handling Declared
- **Weight**: aspirational
- **Category**: format
- **Text**: Sub-skills that produce no findings explicitly declare "no findings" with a
  brief rationale (e.g., "scope clean under current spec") rather than being silently
  omitted.
- **Pass condition**: Every sub-skill section — including zero-finding sub-skills —
  contains an explicit disposition. Fail if any sub-skill section is absent or contains
  only a blank space (a "no findings" declaration without rationale is a partial pass for
  half credit).

### C-12 — Filter Log Present
- **Weight**: aspirational
- **Category**: format
- **Text**: The report includes a filter log (or observation log) that records evidence
  units evaluated but not elevated to findings, so the elevation decision is auditable.
- **Pass condition**: A filter log section is present with at least one entry. The log
  must show: item observed, sub-skill source, and reason not elevated. Fail if the filter
  log is absent or contains no entries (even a single-entry log satisfies the criterion).

### C-13 — Discriminating Rejection Evidence Present
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The filter log contains at least one entry where an observation was evaluated
  and explicitly rejected from finding status, with the rejection reason stated. The
  rejection reason must discriminate — it must explain why this observation did not meet
  the elevation threshold, not merely note it was reviewed.
- **Pass condition**: At least one filter log entry shows an item that was evaluated,
  failed elevation, and carries a specific rejection reason tied to the threshold
  condition. Fail if every log entry either auto-elevates or gives a generic "not
  significant" dismissal.

### C-14 — Scope Attribution in Filter Log
- **Weight**: aspirational
- **Category**: format
- **Text**: Each filter log entry is attributed to the sub-skill scope in which it was
  observed. Scope attribution enables cross-scope filtering patterns to be identified.
- **Pass condition**: Every filter log entry carries a sub-skill scope label. Partial pass
  (half credit) if attribution is present for the majority of entries but missing for
  some.

### C-15 — Finding Lifecycle Labels Applied
- **Weight**: aspirational
- **Category**: depth
- **Text**: Findings are labeled with lifecycle status (e.g., new, confirmed, amended,
  closed) to support multi-round campaign tracking. The label schema is declared or cited
  in the report.
- **Pass condition**: All findings carry a lifecycle label from a declared schema. Partial
  pass (half credit) if labels are present but the schema is undeclared.

### C-16 — Structural Symmetry Across Sub-Skills
- **Weight**: aspirational
- **Category**: format
- **Text**: Each of the five sub-skill sections uses the same structural template — same
  section headings, same field labels, same empty-state language. A reader should be
  unable to tell which sub-skill section they are reading based on structural variation
  alone.
- **Pass condition**: All five sub-skill sections share identical heading structure and
  field labels. Fail if any sub-skill section uses different headings or omits fields
  present in others.

### C-17 — Structural Declaration Table Matches Execution
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every structural commitment declared in the Structural Axis Declaration table
  (C-01) is demonstrably fulfilled in the execution log or findings section. The
  declaration and the execution must be consistent — a declared axis that is absent from
  execution is a structural lie.
- **Pass condition**: Each row in the Structural Axis Declaration table has a
  corresponding artifact or section in the body of the report that fulfills the declared
  commitment. Fail if any declared axis is absent from execution.

### C-18 — Compliance Checklist Present and Enforced
- **Weight**: aspirational
- **Category**: format
- **Text**: The report concludes with a compliance checklist that maps declared structural
  axes to pass/fail verdicts with evidence citations. The checklist is not decorative — at
  least one row must cite a specific artifact location (section, table, or finding ID) as
  evidence.
- **Pass condition**: A compliance checklist is present with rows for each declared
  structural axis and at least one row containing a specific artifact citation. Fail if
  the checklist is absent or if all rows are binary pass/fail without evidence.

### C-19 — Domain Vocabulary Coherence
- **Weight**: aspirational
- **Category**: format
- **Text**: The entire report — headers, field labels, empty-state templates, log entries
  — uses vocabulary from a single named genre. The report should be genre-identifiable
  from its structure alone. Partial pass for genre-coherent structural sections with
  mixed prose. The gap C-19 closes: C-16/C-17/C-18 enforce structural symmetry and
  declaration, but a structurally symmetric report with mixed vocabulary (half "findings",
  half "deficiencies", half "observations") signals incoherent authorial intent.
- **Pass condition**: A genre declaration section or row names the vocabulary genre and
  cites at least two structural examples (e.g., specific headers or labels) that trace to
  the declared genre. Fail if vocabulary is mixed without declaration. Partial pass (half
  credit) if structural sections are genre-coherent but prose sections are mixed.

### C-20 — Observation-to-Finding Qualification Threshold as Structural Rule
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The threshold separating observations from findings must be stated as a named
  rule (T-1 or equivalent), not implied by clean output. The rule must be stated as a
  falsifiable if-and-only-if condition: an observation becomes a finding if and only if
  [named condition]. Gap over C-05: C-05 requires one anchored finding; C-20 requires
  the anchoring requirement to be an explicit rule that is falsifiable. A gate with a
  stated rule can be violated and detected; a gate implied by quality output cannot.
- **Pass condition**: Report contains a named threshold rule (e.g., T-1) stated as an
  if-and-only-if condition before any sub-skill fires. The rule must be findable as a
  standalone declaration, not reconstructed from examples. Fail if the threshold is
  implied by output quality alone.

### C-21 — Per-Scope Filter Gate Embedding
- **Weight**: aspirational
- **Category**: format
- **Text**: Each sub-skill scope carries its own embedded filter gate co-located with its
  evidence, not deferred to a centralized table. Gap over C-13: C-13 requires
  discriminating rejection evidence to exist somewhere; C-21 requires it at each scope
  boundary so cross-scope filtering patterns are visible.
- **Pass condition**: Each of the five sub-skill sections contains its own embedded filter
  gate section with at least one entry (or an explicit "gate passed — no observations
  withheld" declaration). Fail if filtering is handled only by a centralized log with
  no per-scope gate sections. Partial pass (half credit) if per-scope gates are present
  for three or more sub-skills but not all five.

### C-22 — Observational Discipline Declared as Unified Structural Axis
- **Weight**: aspirational
- **Category**: format
- **Text**: The three observational discipline properties (genre vocabulary coherence C-19,
  observation-to-finding threshold rule C-20, per-scope filter gate embedding C-21) are
  declared as a single named structural axis in the Structural Axis Declaration table —
  not as three independent post-hoc checks. A row for observational discipline appears
  co-equally alongside the other structural axes before execution begins. Gap over
  C-19+C-20+C-21 each passing independently: those three can each be satisfied while
  remaining architecturally scattered across the report. C-22 requires integration — one
  axis declaration row that commits to all three as a unified system, so violations of
  any one are detectable as a structural axis failure rather than a floating aspirational
  miss.
- **Pass condition**: The Structural Axis Declaration table (C-01) contains a row for
  observational discipline (or equivalent name) that explicitly references or subsumes
  genre coherence, threshold rule, and per-scope gates as its three sub-claims. The row
  must appear before execution. Fail if the three properties are scattered across
  post-execution sections with no unified axis declaration. Partial pass (half credit) if
  an observational discipline section exists but is not declared as a structural axis row
  in the declaration table.

### C-23 — T-1 Application Demonstrated by Rejection Citation
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The compliance checklist or filter log includes at least one concrete citation
  of an observation that was evaluated against the T-1 threshold, failed, and was
  withheld from the findings list — with the specific observation named and the T-1 test
  result stated. Gap over C-20: C-20 requires T-1 to be declared as a named rule; C-23
  requires evidence the rule was applied. A T-1 rule with no rejection citations is
  unfalsified — it could be a dead declaration that was never tested against actual
  evidence.
- **Pass condition**: At least one named observation appears in the filter log or
  checklist with an explicit T-1 evaluation result (e.g., "T-1: not met — observation
  lacks specific spec location") that results in withholding from the findings list. The
  observation must be named (not described generically) and the T-1 failure reason must
  be specific. Fail if no T-1 rejections are cited anywhere in the report. Partial pass
  (half credit) if a T-1 rejection is cited but the reason is generic rather than tied
  to the specific observation.

### C-24 — Compliance Checklist Uses Sub-Claim Architecture for Multi-Part Axes
- **Weight**: aspirational
- **Category**: format
- **Text**: For any structural axis that commits to multiple sub-claims (e.g., observational
  discipline's three sub-observables: genre section, T-1 filter log, per-scope gates), the
  compliance checklist row must decompose its verdict into independently-verifiable sub-claim
  statuses — using a scheme such as fired/partial/not-fired or equivalent. A partial overall
  verdict must name the specific failing sub-claim. Gap over C-18: C-18 requires a
  compliance checklist with evidence citations. C-24 requires that rows for multi-part axes
  break down to sub-claim granularity so that a partial compliance verdict is self-documenting
  rather than opaque. A single binary PASS/FAIL for a multi-part axis obscures which
  sub-claim failed and cannot be audited without re-reading the body.
- **Pass condition**: Every compliance checklist row that covers a multi-part structural
  axis declares sub-claim-level statuses (at least two named sub-claims with independent
  verdicts). A partial overall verdict must identify the failing sub-claim by name. Fail if
  multi-part axis rows use binary verdicts with no sub-claim decomposition. Partial pass
  (half credit) if sub-claim decomposition is present but a partial verdict does not name
  the failing sub-claim.

### C-25 — T-1 Evidence Co-Located at Execution Scope
- **Weight**: aspirational
- **Category**: correctness
- **Text**: T-1 filtering evidence must be embedded at each per-scope gate where evaluation
  occurred, not consolidated exclusively in a post-execution block. Each sub-skill scope that
  evaluated observations against T-1 must carry a local Disposition column or equivalent
  (e.g., elevated / withheld-T1 / withheld-rule) so the filter decision is verifiable at the
  point of execution. A summary aggregation (T-1 EVALUATION SUMMARY or equivalent) is
  permitted and encouraged, but it must summarize locally-present evidence, not substitute
  for it. Gap over C-23: C-23 requires evidence that T-1 fired (at least one named
  rejection, anywhere in the report). C-25 requires that evidence to be traceable to the
  execution scope where the evaluation occurred — a post-hoc ANNEX satisfies C-23 but
  fails C-25 if it contains rejections with no corresponding per-scope record.
- **Pass condition**: Each sub-skill section that evaluated observations against T-1 contains
  an embedded Disposition field or column showing per-observation T-1 outcomes. A T-1
  EVALUATION SUMMARY may aggregate across scopes, but the primary evidence must reside
  within each scope's section. Fail if T-1 rejection evidence exists only in a post-execution
  block with no per-scope counterparts. Partial pass (half credit) if per-scope embedding
  is present for three or more sub-skills but not all five, or if the Disposition column
  is present but unpopulated for scopes that evaluated observations.

### C-26 — Enforcement Rules Name Their Failure Mode as a Structural Violation
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each structural axis enforcement rule must name what a breach looks like by
  calling it a structural violation — not a quality shortfall, a missed expectation, or
  an aspirational miss. Framing a breach as a structural violation makes the rule
  testable: a reader can ask "did this structural violation occur?" and get a binary
  answer. A rule expressed only as a quality expectation ("should be thorough") cannot be
  falsified in place. Gap over C-17: C-17 requires that every declared axis is fulfilled
  in execution (declaration-execution consistency). C-26 requires that each axis rule also
  names its failure mode — a declared axis that is fulfilled says nothing about what it
  means to fail. C-26 ensures both the pass state and the fail state are named,
  transforming enforcement rules from aspirational guidance into auditable structural
  constraints.
- **Pass condition**: Each structural axis row in the Structural Axis Declaration table
  (or its associated enforcement language) includes an explicit failure-mode statement
  using the term "structural violation" (or equivalent — "axis breach", "structural
  constraint violated") that describes what non-compliance looks like. Fail if enforcement
  rules use only positive framing ("the report must...") with no named failure mode.
  Partial pass (half credit) if failure modes are named for the majority of axes but
  missing for at least one.

### C-27 — Aggregation Blocks Carry a Self-Characterization Statement
- **Weight**: aspirational
- **Category**: format
- **Text**: Any section that aggregates evidence collected at per-scope execution points
  (e.g., T-1 EVALUATION SUMMARY, ANNEX, cross-skill comparison block) must include a
  self-characterization statement — a sentence or labeled row that declares the block's
  relationship to the per-scope records it summarizes. The statement must answer: is this
  block authoritative (replaces per-scope records) or additive (supplements them)? Without
  self-characterization, a reader cannot determine whether a missing per-scope record is
  an oversight or intentional delegation to the aggregation block. Gap over C-25: C-25
  requires per-scope T-1 evidence to be present. C-27 requires that the aggregation block
  itself declare its role — so that the reader knows whether to trust the ANNEX alone or
  must verify against per-scope sections. V-05's ANNEX self-characterization ("This ANNEX
  aggregates per-scope T-1 evidence and does not substitute for it") is the signal: it
  makes the ANNEX's epistemic status explicit rather than requiring the reader to infer it
  from structure.
- **Pass condition**: Every aggregation block in the report contains a self-characterization
  statement that explicitly labels the block as authoritative or additive with respect to
  the per-scope evidence it covers. The statement must use clear framing (e.g., "aggregates
  locally-present evidence", "does not substitute for per-scope records", "primary source
  for..."). Fail if aggregation blocks are present but contain no self-characterization.
  Partial pass (half credit) if self-characterization is present but does not clearly
  state whether the block is authoritative or additive.

---

## Version History

| Version | New Criteria | Source Round | Aspirational Count | Raw Max |
|---------|-------------|--------------|-------------------|---------|
| v1 | C-01–C-08 | — | 0 | 80 |
| v2 | C-09–C-12 | R1/R2 | 4 | 88 |
| v3 | C-13–C-15 | R2/R3 | 7 | 94 |
| v4 | C-16–C-18 | R3 | 10 | 100 |
| v5 | C-19–C-21 | R4 | 13 | 106 |
| v6 | C-22–C-23 | R5 | 15 | 110 |
| v7 | C-24–C-25 | R6 | 17 | 114 |
| **v8** | **C-26–C-27** | **R7** | **19** | **118** |
