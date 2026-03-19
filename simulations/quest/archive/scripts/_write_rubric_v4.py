path = 'C:/src/sim/simulations/quest/rubrics/campaign-simulate-rubric-v4-2026-03-17.md'

rubric = """\
# campaign-simulate --- Evaluation Rubric v4

**Version**: v4
**Date**: 2026-03-17
**Skill evaluated**: /quest:campaign-simulate
**Max score**: 100
**Golden threshold**: all of C-01--C-05 pass AND composite >= 80

---

## What changed from v3 to v4

Three new aspirational criteria extracted from Round 4 scorecard excellence signals:

| ID | New Criterion | Source Pattern |
|----|---------------|----------------|
| C-19 | Finding Type drawn from closed vocabulary | R4 C-03 evidence: V-02/V-04/V-05 Type Vocabulary Map + copy-from-map for Type field |
| C-20 | Blast radius rationale for top-tier findings | R4 C-02 evidence: V-04/V-05 blast radius rationale required for top-tier findings |
| C-21 | Exception path coverage tracked in named column | R4 C-06 evidence: V-01 Entity List 4 requires explicit Exception Path column |

**Scoring adjustment**: aspirational tier expanded from 10 to 13 criteria; section remains
capped at 10 pts. Passing any 10 of 13 aspirational criteria saturates the bucket.
Max score unchanged at 100.

**Key design decisions:**

- C-19 is the companion to C-14. C-14 closes the System Boundary field to a 5-label
  vocabulary; the Finding Type field carries the same hallucination risk. A pre-defined
  type vocabulary (e.g., spec-gap, contract-violation, missing-guard, unreachable-state,
  caller-callee-mismatch) eliminates model judgment from both fields simultaneously.
  A Type Vocabulary Map that covers both System Boundary and Type closes two C-03
  dimensions in one artifact.
- C-20 makes blast-radius tier assignments auditable. C-02 requires an explicit
  blast-radius column; C-20 requires at least one rationale sentence per CRITICAL/
  system-wide finding. Without a rationale, system-wide is an assertion; with one, it
  is a verifiable claim.
- C-21 promotes exception path coverage from an output requirement (C-06: find at least
  two) to a structural requirement: the findings table or entity manifest must contain a
  named column that makes per-row exception path status visible by inspection. C-06
  passes when prose mentions exception paths; C-21 passes only when a named column
  tracks them.
- V-04/V-05 from Round 4 would still score 100/100 on v4 -- all three new criteria were
  already present in their outputs. The rubric caught up to the Round 4 gold standard.

---

## Essential Criteria (60 points)

### C-01 . All Five Sub-Skills Execute
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: The simulation must execute all five sub-skills: flow-lifecycle, flow-conversation,
  trace-state, trace-contract, and trace-permissions. Each must produce distinct findings, not
  be silently skipped or collapsed into one pass.
- **Pass condition**: Output contains a labeled section or findings block for each of the five
  sub-skills by name. Absence of any one sub-skill = fail.

---

### C-02 . Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: format
- **Points**: 12
- **Text**: The final findings report must present findings in ranked order using blast radius as
  the sort key. Blast radius must be explicit -- not implied by placement -- and must distinguish
  at minimum high / medium / low (or equivalent severity tiers).
- **Pass condition**: A ranked findings list exists with an explicit blast-radius or severity
  column/label. Unranked flat lists = fail.

---

### C-03 . System Boundary and Severity per Finding
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: Every finding must identify (a) the system boundary where it was detected (e.g., state
  machine, contract surface, permission check, lifecycle phase) and (b) a severity rating. These
  must appear per finding, not as a summary average.
- **Pass condition**: Each finding entry includes both a boundary label and a severity. Findings
  missing either field = fail.

---

### C-04 . At Least One Spec Gap or Contract Violation Surfaced
- **Weight**: essential
- **Category**: coverage
- **Points**: 12
- **Text**: The primary use case of campaign-simulate is to find what breaks before writing code.
  The output must contain at least one concrete spec gap (underspecified behavior, missing
  precondition) or contract violation (expected vs. actual mismatch) with enough detail to act on.
- **Pass condition**: At least one finding is classified as a spec gap or contract violation with a
  description of what is missing or mismatched. A report with only all-clear findings = fail.

---

### C-05 . Single Synthesized Report (Not Five Separate Outputs)
- **Weight**: essential
- **Category**: format
- **Points**: 12
- **Text**: The output must be one unified simulation findings report, not five disconnected
  sub-skill outputs pasted together. Sub-skill results are inputs to synthesis; the artifact is
  the synthesized document.
- **Pass condition**: Output has a single report structure (header, findings table or list, summary
  section) that integrates all five sub-skills. Raw concatenation of five separate outputs with no
  integration = fail.

---

## Recommended Criteria (30 points)

### C-06 . Exception Paths and Edge Cases Identified
- **Weight**: recommended
- **Category**: depth
- **Points**: 10
- **Text**: The simulation should go beyond the happy path. flow-lifecycle and flow-conversation
  findings should include at least one exception flow, dead-end, loop risk, or edge case per
  sub-skill that ran.
- **Pass condition**: At least two exception paths or edge cases are named across the report
  (not just implied). A report covering only normal operation = does not pass.

---

### C-07 . Findings Cross-Reference Source Sub-Skill
- **Weight**: recommended
- **Category**: coverage
- **Points**: 10
- **Text**: Each finding should cite which sub-skill surfaced it (e.g., [trace-state],
  [flow-lifecycle]). This allows readers to trace a finding back to its simulation context and
  helps prioritize re-runs.
- **Pass condition**: >= 80% of findings carry a sub-skill citation. Findings without any
  attribution = does not pass.

---

### C-08 . State Machine Anomalies Explicitly Called Out
- **Weight**: recommended
- **Category**: depth
- **Points**: 10
- **Text**: The trace-state sub-skill should produce findings about state machine behavior --
  unreachable states, invalid transitions, or violated invariants -- not just a confirmation
  that the state machine was traversed.
- **Pass condition**: At least one state machine anomaly (unreachable state, invalid transition,
  invariant violation, or missing guard) is named in the trace-state findings. No anomalies
  found is acceptable only if the rationale is given.

---

## Aspirational Criteria (10 points, capped)

Each criterion contributes 1 pt. The aspirational section maximum is 10 pts. Passing any 10
of 13 criteria saturates the bucket. Max score = 100.

### C-09 . Test Scenario Baseline Derived from Findings
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The report derives a set of test scenarios (or scenario seeds) directly from its
  findings. Each high or medium blast-radius finding becomes a named test scenario with a brief
  description of what to exercise. This converts simulation output into implementation test
  scaffolding.
- **Pass condition**: The report includes a Test Scenario Baseline section with >= 3 named
  scenarios linked to specific findings.

---

### C-10 . Finding IDs Assigned (F-NN Pattern)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Findings use the F-NN identifier pattern (F-01, F-02, ...) to enable cross-referencing
  in downstream artifacts (spec amendments, test plans, topic-echo). IDs make findings traceable
  through the full finding lifecycle (finding -> DCR/amendment -> spec update -> scenario update).
- **Pass condition**: All findings in the report carry an F-NN ID. Findings without IDs = does not
  pass this criterion.

---

### C-11 . At Least One CRITICAL or HIGH Finding per Trace Sub-Skill
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each of the three trace sub-skills (trace-state, trace-contract, trace-permissions)
  contributes at least one CRITICAL or HIGH severity finding to the report. When all three trace
  budgets are met, >= 3 HIGH/CRITICAL findings exist in the corpus upstream of the test scenario
  baseline -- C-09 passes by construction without requiring an explicit scenario count floor.
  Guarantee the inputs; the output floor follows.
- **Pass condition**: trace-state, trace-contract, and trace-permissions each have at least one
  finding rated CRITICAL or HIGH attributed to them. Missing severity budget on any one trace
  sub-skill = does not pass.

---

### C-12 . Findings Presented in Structured Table (No Blank Cells)
- **Weight**: aspirational
- **Category**: format
- **Text**: All findings appear in a structured table with explicit columns for at minimum:
  Finding ID, Sub-skill, System Boundary, Severity, Description. No cell in any finding row is
  blank. The table format makes C-03 and C-07 failures structurally visible -- a missing boundary
  label or sub-skill citation cannot be buried in prose.
- **Pass condition**: A findings table exists with all required columns populated for every row.
  Prose-only findings lists or a table with blank cells = does not pass.

---

### C-13 . Flow Findings Explicitly Reference Trace Context
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one flow sub-skill finding (flow-lifecycle or flow-conversation) explicitly
  references or builds on a specific trace finding -- e.g., a lifecycle finding cites a state
  invariant violation from trace-state, or a conversation finding references a contract mismatch
  from trace-contract. This cross-reference is the measurable output signature of trace-first
  execution ordering: trace context fed into flow simulations rather than five sub-skills running
  in isolation.
- **Pass condition**: At least one flow finding explicitly names a trace finding by ID or by
  content description. Flow findings that are fully isolated from trace context = does not pass.

---

### C-14 . System Boundary Vocabulary Pre-Assigned per Sub-Skill
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The five system boundary labels must be statically mapped to their owning sub-skills
  and used verbatim in the findings table. Boundary labeling that requires the model to infer
  context from prose is subject to hallucination; pre-assigned labels make C-03 compliance a
  mechanical transcription rather than a judgment call. The fixed map is: trace-state = state
  machine, trace-contract = contract surface, trace-permissions = permission check,
  flow-lifecycle = lifecycle phase, flow-conversation = conversation state.
- **Pass condition**: All System Boundary values in the findings table match the pre-defined
  label for the attributed sub-skill. A boundary value not drawn from the five-label vocabulary,
  or attributed to the wrong sub-skill, = does not pass.

---

### C-15 . Universal Sentinel Rule Across All Columns
- **Weight**: aspirational
- **Category**: format
- **Text**: The no-blank-cell contract from C-12 must extend to every column without exception,
  including optional and conditional fields. When a field does not apply to a given row, the cell
  must contain N/A -- [reason] rather than be left empty. This generalizes C-12 required-column
  enforcement into a complete no-blank contract: there is no column exempt from the rule.
- **Pass condition**: No cell in any finding row is blank. Optional fields contain either a value
  or a filled N/A -- [reason] sentinel. A blank cell in any column, including optional ones,
  = does not pass.

---

### C-16 . No-Findings Sentinel Rows for Clean Sub-Skills
- **Weight**: aspirational
- **Category**: format
- **Text**: When a sub-skill execution produces no findings, the findings table must still contain
  a fully-populated row for that sub-skill. The sentinel row uses Summary = No findings detected
  and fills all other columns per the universal sentinel rule (C-15). An absent row for a clean
  sub-skill is indistinguishable from an execution gap -- silence cannot be used as evidence of a
  clean run.
- **Pass condition**: The findings table contains at least one row attributed to every sub-skill
  that executed. A sub-skill with zero findings must appear as a sentinel row, not be absent from
  the table. Missing sub-skill row = does not pass, regardless of whether the execution log
  mentions a clean result.

---

### C-17 . Pre-Output Blank-Cell Verification Gate
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output must include a named final verification step confirming that no blank cells
  exist in the findings table before the report is written. This step must be labeled or documented
  as a gate, not implied by the absence of blank cells. The gate converts the no-blank contract
  from a style instruction into an explicit checklist item whose outcome is visible in the artifact.
- **Pass condition**: Output contains a named verification gate (e.g., a labeled section, a
  checklist item marked PASSED, or an inline assertion) that confirms table completeness before
  the report is finalized. Reports with no verification gate = does not pass.

---

### C-18 . Unified Schema Closes C-03, C-07, C-10, and C-13 Simultaneously
- **Weight**: aspirational
- **Category**: format
- **Text**: The findings table schema must include at minimum these columns: F-ID (satisfies C-10),
  Sub-Skill (satisfies C-07), System Boundary (satisfies C-03), Severity (satisfies C-03), Blast
  Radius (satisfies C-02 sorting), Trace Link (satisfies C-13), and Description. A single table
  with this schema makes it possible to verify C-03, C-07, C-10, and C-13 by inspection of one
  artifact. Multi-schema designs -- separate tables per sub-skill, or per-phase schemas that omit
  required columns -- fail this criterion even if the data is correct across all tables.
- **Pass condition**: A single findings table exists whose column set includes F-ID, Sub-Skill,
  System Boundary, Severity, Blast Radius, Trace Link, and Description. A multi-table design that
  requires aggregation to verify any of C-03, C-07, C-10, or C-13 = does not pass.

---

### C-19 . Finding Type Drawn from Closed Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The Finding Type field carries the same hallucination risk as System Boundary (C-14):
  free-form type labels allow invented or misattributed categories that silently fail C-04. A
  pre-defined Type Vocabulary Map closes the field to a fixed set (e.g., spec-gap,
  contract-violation, missing-guard, unreachable-state, caller-callee-mismatch,
  undefined-behavior, invariant-violation, permission-gap) and makes type assignment a copy
  operation. The vocabulary map should appear as a named artifact in the output -- either a
  standalone section or as additional columns in the Type Vocabulary Map table alongside the
  System Boundary map from C-14.
- **Pass condition**: All Type values in the findings table are drawn from a named, pre-defined
  vocabulary. Type values not present in the vocabulary, or a findings table with no accompanying
  vocabulary artifact, = does not pass.

---

### C-20 . Blast Radius Rationale for Top-Tier Findings
- **Weight**: aspirational
- **Category**: depth
- **Text**: Findings rated CRITICAL or system-wide must include an explicit rationale sentence
  explaining why the blast radius reaches that tier -- e.g., system-wide because the missing
  permission check applies to all callers regardless of role. Without a rationale, the tier
  assignment is an assertion; with one, it is a verifiable claim that reviewers can challenge or
  confirm. C-02 requires blast-radius labels; C-20 requires audit sentences for the highest-tier
  assignments.
- **Pass condition**: Each finding rated CRITICAL or classified as system-wide blast radius
  includes at least one sentence explaining the basis for that tier assignment. Top-tier findings
  with no rationale = does not pass.

---

### C-21 . Exception Path Coverage Tracked in Named Column
- **Weight**: aspirational
- **Category**: depth
- **Text**: C-06 requires at least two named exception paths across the report. C-21 requires that
  exception path coverage be tracked in a named structural column in the findings table or entity
  manifest -- e.g., an Exception Path column that is populated per finding row. A structural
  column makes coverage verifiable by inspection: counting non-null Exception Path cells is
  sufficient evidence. Prose mention of exception paths satisfies C-06 but not C-21.
- **Pass condition**: The findings table or entity manifest contains a named Exception Path column
  (or structural equivalent) populated for each finding row. Exception paths mentioned only in
  prose, or implied by finding descriptions, = does not pass.

---

## Scoring Summary Table

| ID   | Criterion                                              | Weight       | Category    | Points |
|------|--------------------------------------------------------|--------------|-------------|--------|
| C-01 | All five sub-skills execute                            | essential    | correctness | 12     |
| C-02 | Findings ranked by blast radius                        | essential    | format      | 12     |
| C-03 | System boundary + severity per finding                 | essential    | correctness | 12     |
| C-04 | At least one spec gap or contract violation            | essential    | coverage    | 12     |
| C-05 | Single synthesized report                              | essential    | format      | 12     |
| C-06 | Exception paths and edge cases                         | recommended  | depth       | 10     |
| C-07 | Findings cross-reference source sub-skill              | recommended  | coverage    | 10     |
| C-08 | State machine anomalies called out                     | recommended  | depth       | 10     |
| C-09 | Test scenario baseline derived from findings           | aspirational | behavior    | 1      |
| C-10 | Finding IDs assigned (F-NN pattern)                    | aspirational | behavior    | 1      |
| C-11 | CRITICAL/HIGH budget met per trace sub-skill           | aspirational | depth       | 1      |
| C-12 | Structured findings table, no blank cells              | aspirational | format      | 1      |
| C-13 | Flow findings reference trace context                  | aspirational | depth       | 1      |
| C-14 | System boundary vocabulary pre-assigned                | aspirational | correctness | 1      |
| C-15 | Universal sentinel rule across all columns             | aspirational | format      | 1      |
| C-16 | No-findings sentinel rows for clean sub-skills         | aspirational | format      | 1      |
| C-17 | Pre-output blank-cell verification gate                | aspirational | behavior    | 1      |
| C-18 | Unified schema closes C-03/C-07/C-10/C-13             | aspirational | format      | 1      |
| C-19 | Finding Type drawn from closed vocabulary              | aspirational | correctness | 1      |
| C-20 | Blast radius rationale for top-tier findings           | aspirational | depth       | 1      |
| C-21 | Exception path coverage tracked in named column        | aspirational | depth       | 1      |

**Essential subtotal**: 60 pts (5 criteria x 12)
**Recommended subtotal**: 30 pts (3 criteria x 10)
**Aspirational subtotal**: 10 pts max (13 criteria x 1 pt each, capped at 10)
**Max score**: 100
**Golden threshold**: all of C-01--C-05 pass AND composite >= 80

---

## Usage Notes

- Run this rubric against outputs from /quest-variate to compare prompt variations.
- A run that passes C-01--C-05 but scores 60--79 is useful but shallow -- C-06 through
  C-08 are the depth signal.
- C-09 through C-21 are structural markers worth 1 pt each, capped at 10 pts total.
  Passing all 13 earns 10 pts (same as passing any 10). The cap means the last 3 passed
  represent excellence beyond the rubric ceiling, not extra score.
- C-11 is the upstream guarantee: when all three trace sub-skills each contribute a
  CRITICAL/HIGH finding, C-09 closes by construction.
- C-12/C-15 are the no-blank-cell contract at two levels: required columns (C-12) and
  every column without exception (C-15). C-15 fails if any optional column is blank.
- C-14/C-19 are the closed-vocabulary pair: C-14 closes System Boundary to 5 labels,
  C-19 closes Finding Type to a named vocabulary. Together they eliminate model judgment
  from the two fields most susceptible to hallucination.
- C-16 is the silent-skip detector: an absent row for a clean sub-skill is treated as
  evidence of a skip, not a clean run.
- C-17 is the process gate: the verification step must appear in the output, not just be
  implied by clean cells.
- C-18 is the schema integrity test: one table whose column set alone satisfies four other
  criteria. Multi-table designs fail C-18 regardless of per-table data correctness.
- C-20 is the blast radius audit trail: C-02 proves ranking happened; C-20 proves the
  top-tier assignments are defensible.
- C-21 promotes C-06 from prose coverage to structural coverage: a named Exception Path
  column makes per-row exception path status verifiable by inspection.
- C-13 captures the trace-first cross-reference output; C-21 captures exception path
  structural tracking; together they make the two key simulation disciplines
  (trace-informed flow, exception-path completeness) verifiable by column scan rather
  than by reading prose.
- Common failure modes: silent sub-skill skipping (C-01), five separate outputs with no
  synthesis (C-05), findings without severity labels (C-03), boundary labels inferred
  from prose (C-14), finding types not drawn from vocabulary (C-19), clean sub-skills
  absent from table (C-16), top-tier blast radius with no rationale (C-20).
- v2 change: aspirational criteria expanded from 2 to 5; per-criterion points reduced
  from 5 to 2.
- v3 change: aspirational criteria expanded from 5 to 10; per-criterion points reduced
  from 2 to 1. Max score unchanged at 100.
- v4 change: aspirational criteria expanded from 10 to 13; section capped at 10 pts.
  Max score unchanged at 100.
"""

with open(path, 'w') as f:
    f.write(rubric)
print('written', len(rubric.splitlines()), 'lines')
