---
skill: campaign-simulate
round: 8
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v7-2026-03-17.md
---

# campaign-simulate -- Round 8 Variations

**Context**: All five R7 variations scored 100/100 under the v7 rubric at the time of
scoring. R7 V-05 is the base for R8: it carries sub-claim compliance architecture (C-24),
per-scope Disposition column as primary T-1 evidence (C-25), and the full six-mechanism
Structural Axis Declaration. Three new criteria were added to rubric v7 post-convergence:
C-29 (Propagation Coverage Gate), C-30 (Confidence-Stratified Action List), C-31
(Type-constrained Remediation Verb). R7 V-05 does not satisfy any of them.

**Under rubric v7 with C-29/C-30/C-31 active**: raw max 123, divisor 1.23. R7 V-05
without C-29/C-30/C-31 = 114/123 = 92.7 normalized. To reach 100: must pass all three.

**Round 8 axes chosen:**
- Single-axis: V-01 (C-29 -- Cross-Skill Dependency Map + Propagation Coverage Gate),
  V-02 (C-30 -- Confidence-Stratified Action List: HIGH/LOW confidence x blast-radius
  quadrant), V-03 (C-31 -- Finding Classification + type-constrained Remediation Verb)
- Combined: V-04 (C-29 + C-30 on R7 V-05 base), V-05 (full integration: dependency map
  + confidence stratification + type-constrained verbs + all R7 V-05 mechanisms)

---

## V-01 -- Cross-Skill Dependency Map + Propagation Coverage Gate (C-29)

**Variation axis:** Output format -- before execution, the model must declare a
Cross-Skill Dependency Map: a numbered list of dependency rules describing which
sub-skill outputs feed downstream sub-skills or which findings from one scope are
expected to constrain another. After synthesis, the model must run a Propagation
Coverage Gate: for each rule in the dependency map, confirm whether a finding was
recorded that covers that rule, or log an OPEN PROPAGATION GAP with the rule ID
cited. A dependency map that lists N rules but silently processes fewer fails C-29
even if ELEVATED annotations are present in the ranked table.

**Hypothesis:** C-29 passes by construction. Every rule declared in the dependency
map is either (a) associated with a recorded finding by rule ID, or (b) logged as
OPEN PROPAGATION GAP [DR-NN] in the Propagation Coverage Gate section. No rule
vanishes silently after synthesis. C-30 and C-31 are not targeted -- blast-radius
ranking remains flat (C-02 satisfied), and the Remediation field uses free-form
action verbs (C-08 satisfied but not C-31).

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares
all six axes. The last section verifies all six fired using sub-claim decomposition
for multi-part axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not
leave any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined:
  [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list.
  Either (a) name at least one observation that should be rejected under the filter
  rules, or (b) justify that every candidate is genuinely anchored to a named spec
  location and scoped to at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation
  that was considered and failed T-1 for this scope, or confirm scope is clean and
  state why T-1 did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX:
  Zero withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION
  REQUIRED: Either identify a withheld-T1 observation in any scope, or confirm all
  scopes are clean and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules
  or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available
  for pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration
  but did not produce observable output in this report. Reason: [why the mechanism did
  not fire]. Impact on report validity: [whether the omission affects any findings]."
- **Propagation Coverage Gate no gaps**: "Propagation Coverage Gate: [N] dependency
  rules declared. All [N] rules accounted for by recorded findings: [list rule IDs and
  corresponding F-IDs]. No OPEN PROPAGATION GAPs."
- **Propagation Coverage Gate no rules**: "Dependency map produced zero dependency
  rules. DEPENDENCY MAP RECALIBRATION REQUIRED: Either declare at least one rule
  describing how findings from one sub-skill scope constrain or feed another, or
  confirm that this topic has no cross-skill dependencies and state why."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap /
                 flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 FAILURE: vague reference without named location fails this field]
Summary:        [one sentence, problem only --
                 FAILURE: merging Impact into Summary fails C-06]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 FAILURE: blank or merged with Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 FAILURE: wide-scope finding without rationale fails C-10]
Dependency rule:[OPTIONAL: if this finding covers a declared dependency rule, cite its
                 ID here -- e.g., DR-02. Used by Propagation Coverage Gate.]
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails
                 C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading
only this section must be able to (a) predict every structural section in the report,
(b) verify each axis independently from its named sub-observables, and (c) identify
the exact schema of each gate table before reading any execution. All six rows must
have equal depth: three independently-verifiable sub-observables in the Observable
Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural, its absence fails this axis; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing the per-scope record by scope name |
| Propagation coverage axis | C-29 | Cross-Skill Dependency Map (declared before execution, numbered DR-01 through DR-NN) + Propagation Coverage Gate (after synthesis, one row per dependency rule: covered by finding or OPEN PROPAGATION GAP) | (1) Cross-Skill Dependency Map section before execution: numbered rules DR-01 through DR-NN with rule text; (2) Propagation Coverage Gate section after synthesis: one row per rule -- Rule ID, Rule text, Coverage status (Finding F-ID / OPEN PROPAGATION GAP), Evidence; (3) zero silent drops -- every declared rule appears in the gate table |

The propagation coverage axis in row 6 is a structural commitment. A dependency map
that declares N rules must produce a Propagation Coverage Gate table with exactly N
rows. Missing rows fail C-29 regardless of annotation density in the ranked table.

---

**CROSS-SKILL DEPENDENCY MAP**

Write this section immediately after the Structural Axis Declaration, before
Observational Discipline. Declare every rule describing how findings from one
sub-skill scope constrain or feed another scope. Number rules DR-01 through DR-NN.

Rules typically arise from:
- A gap in flow-lifecycle that would, if undetected, produce a state anomaly in
  trace-state (state feeds from lifecycle outcomes)
- A contract violation in trace-contract that would cause trace-permissions to
  fail to enforce the expected boundary
- A conversation dead-end in flow-conversation that traces to a missing state
  transition in trace-state

| Rule ID | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|---------|------|-----------------|-----------------|--------------------------|

If fewer than two rules can be declared: apply the Propagation Coverage Gate no rules
empty-state template and state why the topic has minimal cross-skill dependency.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Cross-Skill Dependency Map, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout (minimum four terms declared):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings
  Table
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; does not enter global filter log
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters
  filter log with rule citation; does not enter Findings Table directly

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1 at the per-scope gate.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. The column
is populated at execution time, co-located with the sub-skill that produced the
observation. An evaluator can verify every T-1 decision from the per-scope gate tables
without reading the T-1 ANNEX. If zero withheld-T1 rows appear for a scope: apply T-1
SCOPE RECALIBRATION immediately below that gate table.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is
a summary, not a primary evidence source. It must cite per-scope source records by scope
name. A T-1 ANNEX that names a withheld-T1 observation absent from any per-scope
Disposition column is a structural violation.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using
the declared schema. The Disposition column is structural -- do not omit it or rename it.
Where a finding covers a declared dependency rule, populate the Dependency rule field in
the Finding Schema.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero
withheld-T1 template immediately below the gate table before advancing.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate observations with Disposition: elevated from all five per-scope gate tables.
Observations with Disposition: withheld-T1 or withheld-rule do not appear here.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

Declare the gate state. This block is required in every report.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief
> reason for each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED:
> [apply template text; justify that every candidate is anchored].

**T-1 ANNEX** (required immediately after Template A or B -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met] --
>   per-scope record in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 (Disposition: elevated at per-scope gate) and all
four filter rules (Elevate?: yes in filter log).

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|----------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

For top three ranked findings: state blast radius rationale (name downstream flows,
components, or contracts affected and explain why scope reaches that far).

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills
sharing surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply comparison-step empty-state template.

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

If no compounding pairs: apply cross-skill-patterns empty-state template. The template
requires citing every pair from Step 2 and their verdicts.

---

**PROPAGATION COVERAGE GATE**

Write this section after Cross-Skill Comparison Protocol and before the Structural
Compliance Checklist. For each dependency rule declared in the Cross-Skill Dependency
Map, confirm coverage status. This section converts the dependency map from a planning
artifact into a verifiable execution contract.

| Rule ID | Rule (abbreviated) | Coverage Status | Evidence |
|---------|--------------------|----------------|----------|
| DR-01   | [rule text]        | Covered by [F-ID] / OPEN PROPAGATION GAP | [finding summary or gap reason] |

**Coverage Status values**:
- `Covered by [F-ID]` -- a recorded finding accounts for this dependency rule
- `OPEN PROPAGATION GAP [DR-NN]` -- no finding covers this rule; the rule was examined
  and found non-triggering for this topic (state why) or was not reachable given the
  spec input (state why the spec does not trigger this dependency)

Every rule declared in the dependency map must appear in this table. A rule that does
not appear here is a silent drop -- a structural violation of C-29 regardless of
ELEVATED annotation presence elsewhere.

If zero dependency rules were declared: apply the Propagation Coverage Gate no rules
empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section
names and evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or
more independently-verifiable observables declared in the declaration table), the Status
column must declare sub-claim-level statuses using `fired / partial / not-fired` per
named sub-claim. A partial overall verdict names the specific failing sub-claim inline.
Binary PASS or FAIL for a multi-part row is a structural violation of this checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding pattern or empty-state citing Step 2 pairs) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables in the Observable Output column; Sub-claim 3: section appears before any execution evidence -- confirmed by section ordering | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires -- cite OBSERVATIONAL DISCIPLINE section; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- for each scope, cite sub-skill name and whether Disposition column is populated with at least one withheld-T1 row (or T-1 SCOPE RECALIBRATION invoked); T-1 ANNEX confirmed as summary aggregator citing per-scope source records | fired / partial [name failing sub-claim] / not fired |
| Propagation coverage axis | Cross-Skill Dependency Map + Propagation Coverage Gate | Sub-claim 1: dependency map declared before execution -- cite rule count (DR-01 through DR-NN); Sub-claim 2: Propagation Coverage Gate table has exactly one row per declared rule -- cite row count and rule IDs; Sub-claim 3: zero silent drops -- every rule is either covered by a named finding (F-ID cited) or logged as OPEN PROPAGATION GAP with rule ID cited | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Cross-Skill Dependency Map >
Observational Discipline > Execution Sequence (five sub-skills, each with co-located
per-scope gate table using Disposition schema) > Candidate Observations and Filter Log >
Filter Log Resolution (Template A or B, then T-1 ANNEX as summary aggregator) > Findings
Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3)
> Propagation Coverage Gate > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Cross-Skill Dependency Map declared before execution with at least one rule (C-29)
2. Propagation Coverage Gate table has one row per declared rule; zero silent drops (C-29)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope Disposition data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
6. A partial compliance verdict names the specific failing sub-claim inline (C-24)
7. Six structural axis rows with equal depth appear before any execution evidence (C-22)
8. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)

---

## V-02 -- Confidence-Stratified Action List (C-30)

**Variation axis:** Output format -- the Ranked Findings section must be split into two
named action tracks using a blast-radius x confidence grid. Track 1: HIGH-confidence /
HIGH-blast findings require no spec clarification before implementation -- fix immediately.
Track 2: LOW-confidence / HIGH-blast findings require spec interpretation to be confirmed
before implementation begins. Merging both tracks into a single sorted list satisfies
C-02 (explicit blast-radius column) but fails C-30 (no stratification). This variation
adds a Confidence field to the Finding Schema and splits Ranked Findings into the two
tracks.

**Hypothesis:** C-30 passes by construction. The final action list names both tracks
explicitly. HIGH-confidence / HIGH-blast findings carry a rationale for why implementation
can proceed without confirmation. LOW-confidence / HIGH-blast findings carry a confirmation
question that must be answered before implementation. C-29 and C-31 are not targeted --
no dependency map is declared, and the Remediation field uses free-form verbs (C-08
satisfied but not C-31).

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all
five axes. The last section verifies all five fired using sub-claim decomposition for
multi-part axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined:
  [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list.
  Either (a) name at least one observation that should be rejected under the filter
  rules, or (b) justify that every candidate is genuinely anchored to a named spec
  location and scoped to at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation
  that was considered and failed T-1 for this scope, or confirm scope is clean and state
  why T-1 did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION
  REQUIRED: Either identify a withheld-T1 observation in any scope, or confirm all scopes
  are clean and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or
  no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] empty. [Reason: no HIGH-blast findings at this
  confidence level, or no HIGH-blast findings in report.]"
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration
  but did not produce observable output in this report. Reason: [why the mechanism did
  not fire]. Impact on report validity: [whether the omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 FAILURE: vague reference without named location fails this field]
Summary:        [one sentence, problem only --
                 FAILURE: merging Impact into Summary fails C-06]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 FAILURE: blank or merged with Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 FAILURE: wide-scope finding without rationale fails C-10]
Confidence:     [HIGH / LOW -- HIGH: finding is grounded in a named spec contract with
                 no interpretive ambiguity; LOW: finding depends on spec interpretation
                 that has not been explicitly confirmed]
Conf rationale: [one sentence: why this confidence rating -- what spec evidence anchors
                 HIGH, or what interpretive question makes LOW --
                 FAILURE: blank or "obvious" fails this field]
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b)
verify each axis independently from its named sub-observables, and (c) identify the exact
schema of each gate table before reading any execution. All five rows must have equal
depth: three independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1, action tracks |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing per-scope record |

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout (minimum four terms declared):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings
  Table
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; does not enter global filter log
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters
  filter log with rule citation; does not enter Findings Table directly

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1 at the per-scope gate.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
An evaluator can verify every T-1 decision from the per-scope gate tables without reading
the T-1 ANNEX. If zero withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION
immediately below that gate table.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope
name. A T-1 ANNEX that names a withheld-T1 observation absent from any per-scope
Disposition column is a structural violation.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write its per-scope gate table using the declared
schema. The Disposition column is structural -- do not omit it or rename it.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero
withheld-T1 template immediately below the gate table before advancing.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate observations with Disposition: elevated from all five per-scope gate tables.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

Declare the gate state.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief
> reason for each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after Template A or B -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met] --
>   per-scope record in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Confidence | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-----------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Sort findings within each tier by blast radius: system-wide > cross-skill > component-wide
> isolated. Then split every HIGH-blast finding (system-wide or cross-skill) into two
named action tracks by confidence. LOW-blast findings (component-wide or isolated) are
listed in Tiers 3-4 without track splitting.

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Applies to all HIGH-blast findings (Tier 1 and Tier 2). LOW-blast findings are not
stratified.

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

These findings are grounded in explicit, unambiguous spec contracts. No spec
clarification is needed before implementation begins. For each finding:

| F-ID | Blast Tier | Confidence rationale | Action |
|------|------------|---------------------|--------|

If no HIGH-confidence / HIGH-blast findings: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

These findings depend on spec interpretation that has not been explicitly confirmed.
A wrong interpretation could cause unnecessary implementation work or an incorrect
fix. For each finding, state the confirmation question before implementation is
authorized.

| F-ID | Blast Tier | Interpretive question (confirm before implementing) | Action after confirmation |
|------|------------|-----------------------------------------------------|--------------------------|

If no LOW-confidence / HIGH-blast findings: apply action-track-empty template.

**Track decision rationale**: A finding is HIGH-confidence when its Spec Location names
a concrete contract, interface, or invariant that leaves no room for interpretation. A
finding is LOW-confidence when the spec is silent, ambiguous, or the violation depends
on an assumption about intended behavior that has not been stated explicitly.

---

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

For top three ranked findings across all tiers: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills
sharing surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: If compounding pairs found, name the pattern. If
none: apply cross-skill-patterns empty-state template.

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism, the Status
column must declare sub-claim-level statuses using `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL for a multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- each cited by sub-skill name | fired / partial [name failing sub-claim] / not fired |
| Confidence-stratified action list | CONFIDENCE-STRATIFIED ACTION LIST | Sub-claim 1: Track 1 present with label "Implement Now (HIGH-confidence / HIGH-blast)"; Sub-claim 2: Track 2 present with label "Confirm Spec First (LOW-confidence / HIGH-blast)"; Sub-claim 3: each HIGH-blast finding appears in exactly one track -- no finding in both, none in neither | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (five sub-skills, each with co-located per-scope gate table) >
Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) >
Findings Table > Execution Log > Ranked Findings (Tiers 1-4) > Confidence-Stratified
Action List (Track 1 and Track 2) > Cross-Skill Comparison Protocol (Steps 1, 2, 3) >
Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Every HIGH-blast finding (Tier 1 or Tier 2) appears in exactly one of Track 1 or
   Track 2 -- no merging, no omission (C-30)
2. Track 2 findings carry a confirmation question before any action is authorized (C-30)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)

---

## V-03 -- Type-Constrained Remediation Verb (C-31)

**Variation axis:** Output format -- each finding must carry a Finding Classification
field (GAP / CONTRADICTION / ASSUMPTION) that constrains the Remediation Verb vocabulary.
GAP-classified findings must use verb "add" or "remove." CONTRADICTION-classified findings
must use verb "resolve." ASSUMPTION-classified findings must use verb "confirm." An
ASSUMPTION finding with Verb="add" fails C-31 even if the row is structurally complete.
The constraint makes remediation self-auditing: an out-of-vocabulary verb signals
mis-classification or mis-remediation. C-29 and C-30 are not targeted.

**Hypothesis:** C-31 passes by construction. Every finding has a Classification field
populated as GAP/CONTRADICTION/ASSUMPTION, and every Remediation entry decomposes into
Verb / Target / Location / Conformance columns. The Verb in each row is constrained by
the Classification: GAP -> "add" or "remove"; CONTRADICTION -> "resolve"; ASSUMPTION ->
"confirm". A reviewer can audit every remediation row without reading context.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all
five axes. The last section verifies all five fired using sub-claim decomposition for
multi-part axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined:
  [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped to
  at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation
  that was considered and failed T-1 for this scope, or confirm scope is clean and state
  why T-1 did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes are clean
  and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or
  no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration
  but did not produce observable output in this report. Reason: [why the mechanism did not
  fire]. Impact on report validity: [whether the omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:             [sequential: F-01, F-02, ...]
Sub-skill:        [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                   trace-permissions]
Type:             [spec-gap / contract-violation / state-anomaly / permission-gap /
                   flow-gap]
Classification:   [GAP / CONTRADICTION / ASSUMPTION --
                   GAP: spec is silent or missing; CONTRADICTION: spec has conflicting
                   statements; ASSUMPTION: behavior was assumed but not specified --
                   FAILURE: blank or wrong classification causes Remediation verb
                   violation in C-31]
Spec location:    [REQUIRED: named section, boundary, or interface --
                   FAILURE: vague reference without named location fails this field]
Summary:          [one sentence, problem only --
                   FAILURE: merging Impact into Summary fails C-06]
Impact:           [STANDALONE FIELD: what breaks if unresolved --
                   FAILURE: blank or merged with Summary fails C-06]
Blast radius:     [isolated / component-wide / cross-skill / system-wide]
BR rationale:     [REQUIRED for cross-skill or system-wide --
                   FAILURE: wide-scope finding without rationale fails C-10]
Remediation:
  Verb:           [constrained by Classification:
                   GAP -> "add" or "remove" ONLY
                   CONTRADICTION -> "resolve" ONLY
                   ASSUMPTION -> "confirm" ONLY
                   FAILURE: out-of-vocabulary verb fails C-31 even if row is complete]
  Target:         [the specific artifact, section, or interface to act on]
  Location:       [where in the spec or implementation the action takes place]
  Conformance:    [what passing looks like after the remediation is applied]
```

**Remediation verb vocabulary** (mandatory constraint):

| Classification | Permitted Verbs | Example |
|---------------|----------------|---------|
| GAP | add, remove | "add: missing error state definition to Section 3.2 state table" |
| CONTRADICTION | resolve | "resolve: conflicting timeout values in Section 2.1 and Section 4.3" |
| ASSUMPTION | confirm | "confirm: whether retry is silent or visible in Section 5 lifecycle spec" |

An ASSUMPTION finding with Verb="add" fails C-31 even if the Verb/Target/Location/
Conformance columns are all populated. The classification drives the verb; the verb
does not retroactively determine the classification.

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. All five rows must have
equal depth: three independently-verifiable sub-observables in the Observable Output
column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- Disposition column structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason |

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout (minimum four terms declared):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings
  Table
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; does not enter global filter log
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters
  filter log with rule citation; does not enter Findings Table directly

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. If zero
withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION immediately.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It must
cite per-scope source records by scope name and introduces no new evidence.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write the per-scope gate table. Classify each
elevated observation as GAP / CONTRADICTION / ASSUMPTION at elevation time.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | Classification (if elevated) | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|------------------------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`
Classification values (elevated only): `GAP` | `CONTRADICTION` | `ASSUMPTION`

If zero withheld-T1 rows: apply Per-scope Disposition zero withheld-T1 template.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate observations with Disposition: elevated from all five per-scope gate tables.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Classification | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|---------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason]).
> Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [condition not met] --
>   per-scope record in [sub-skill section name]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Classification | Spec Location | Summary | Impact | Blast Radius | Remediation Verb | Remediation Target | Location | Conformance |
|------|-----------|------|---------------|--------------|---------|--------|-------------|-----------------|-------------------|----------|-------------|

**Remediation verb audit**: Before closing the Findings Table, confirm that every row
satisfies the type-constraint rule:
- GAP rows: Verb is "add" or "remove" -- circle any row where Verb is not in this set
- CONTRADICTION rows: Verb is "resolve" -- circle any row where Verb differs
- ASSUMPTION rows: Verb is "confirm" -- circle any row where Verb differs

A circled verb is a structural violation. Correct the Classification or the Verb before
finalizing the table.

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: compounding patterns named, or empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism, Status must
declare sub-claim-level statuses using `fired / partial / not-fired` per named sub-claim.
Binary PASS or FAIL for a multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited with rejection count; Sub-claim 2: T-1 ANNEX present with named withheld-T1 example (or RECALIBRATION); Sub-claim 3: T-1 ANNEX characterizes itself as summary | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table; Sub-claim 2: Step 2 table; Sub-claim 3: Step 3 declaration | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present; Sub-claim 2: three observables per row; Sub-claim 3: appears before any execution | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each per-scope section] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary; Sub-claim 2: T-1 rule stated as if-and-only-if; Sub-claim 3: per-scope Disposition columns present for all five sub-skills | fired / partial [name failing sub-claim] / not fired |
| Type-constrained remediation axis | Findings Table | Sub-claim 1: every finding has a Classification field (GAP/CONTRADICTION/ASSUMPTION) -- cite classification distribution; Sub-claim 2: every GAP finding has Verb "add" or "remove" -- cite count verified; Sub-claim 3: every CONTRADICTION finding has Verb "resolve" AND every ASSUMPTION finding has Verb "confirm" -- cite count verified; partial verdict names the specific F-ID with out-of-vocabulary verb | fired / partial [name F-ID with violation] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (five sub-skills, each with co-located per-scope gate table) >
Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings
Table (with Remediation verb audit) > Execution Log > Ranked Findings > Cross-Skill
Comparison Protocol > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Every finding has Classification: GAP / CONTRADICTION / ASSUMPTION (C-31)
2. Remediation Verb is constrained by Classification -- out-of-vocabulary verb is a
   structural violation detected at finding table completion (C-31)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)

---

## V-04 -- Combined: Dependency Map Gate + Confidence Stratification (C-29 + C-30)

**Variation axis:** Combined -- V-01 (C-29: Cross-Skill Dependency Map + Propagation
Coverage Gate) plus V-02 (C-30: Confidence-Stratified Action List with two named tracks).
Neither C-31 nor free-verb remediation is modified. This combination tests whether
C-29 and C-30 interact: does confidence stratification interact with propagation coverage
accounting? Specifically: can an OPEN PROPAGATION GAP finding be LOW-confidence (the
dependency rule describes a path that was unverifiable), and does the action track for
that gap correctly require spec confirmation before the gap is resolved?

**Hypothesis:** C-29 and C-30 both pass by construction. Every dependency rule is
accounted for in the Propagation Coverage Gate. Every HIGH-blast finding is placed in
Track 1 or Track 2 by confidence. OPEN PROPAGATION GAP entries that are HIGH-blast
must also appear in a track. C-31 is not targeted.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all
six axes. The last section verifies all six fired using sub-claim decomposition for
multi-part axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined:
  [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped
  to at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation
  that was considered and failed T-1 for this scope, or confirm scope is clean and state
  why T-1 did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or
  no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] empty. Reason: [no HIGH-blast findings at this
  confidence level]."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration
  but did not produce observable output in this report. Reason: [why]. Impact: [whether
  the omission affects any findings]."
- **Propagation Coverage Gate no gaps**: "Propagation Coverage Gate: [N] dependency rules
  declared. All [N] rules accounted for by recorded findings. No OPEN PROPAGATION GAPs."
- **Propagation Coverage Gate no rules**: "Dependency map produced zero rules. DEPENDENCY
  MAP RECALIBRATION REQUIRED."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE FIELD: what breaks if unresolved]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Dependency rule:[OPTIONAL: DR-NN if this finding covers a declared rule]
Confidence:     [HIGH / LOW]
Conf rationale: [one sentence: what anchors HIGH or what question creates LOW]
Remediation:    [specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. Six rows. Three
independently-verifiable sub-observables per row.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A/B) | (1) Filter Log table with Elevate? and Rejection Reason columns; (2) Filter Log Resolution with template letter and rejection count; (3) filter rules 1-4 listed before evaluation begins |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template text in any empty section; (2) template cited in compliance checklist; (3) coverage includes ranked tiers, action tracks, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1 table: F-ID pairs; (2) Step 2 table: verdicts with reasons; (3) Step 3: compounding patterns named or empty-state citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first, six rows, three observables each) + Structural Compliance Checklist (last, sub-claim architecture) | (1) This Structural Axis Declaration before any execution; (2) Compliance Checklist as final section with sub-claim decomposition for all multi-part rows; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope Disposition columns + T-1 ANNEX (summary only) | (1) OBSERVATIONAL DISCIPLINE: vocabulary glossary (four terms), T-1 rule; (2) five per-scope gate tables with structural Disposition column; (3) T-1 ANNEX: summary aggregator citing per-scope records by scope name |
| Propagation coverage axis | C-29 | Cross-Skill Dependency Map (before execution, DR-01 through DR-NN) + Propagation Coverage Gate (after synthesis, one row per rule) | (1) Dependency map: numbered rules before execution; (2) Coverage Gate: one row per rule -- coverage status and evidence; (3) zero silent drops: every rule present in gate table |

---

**CROSS-SKILL DEPENDENCY MAP**

Write this section immediately after the Structural Axis Declaration, before
Observational Discipline.

| Rule ID | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|---------|------|-----------------|-----------------|--------------------------|

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Cross-Skill Dependency Map.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary:
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed a filter rule

**T-1 threshold rule**: An observation is elevated if and only if it names a specific spec
location AND describes a gap or violation that would cause incorrect implementation
behavior.

**Per-scope Disposition rule**: Each per-scope gate table includes a Disposition column.
If zero withheld-T1 rows for a scope: apply T-1 SCOPE RECALIBRATION immediately.

**T-1 ANNEX role (summary aggregator only)**: Aggregates withheld-T1 records from per-
scope gate tables. Cites per-scope sources. Introduces no new evidence.

---

**EXECUTION SEQUENCE**

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

Filter rules: (1) no spec location (2) no blast radius (3) style preference (4) duplicate

---

**FILTER LOG RESOLUTION**

**Template A**: > Filter gate applied. [N] observations evaluated. [M] rejected (Rule
[number]: [reason]). Gate operating normally.

**Template B**: > Filter gate applied. [N] observations evaluated. Zero rejected.
RECALIBRATION REQUIRED.

**T-1 ANNEX** (summary aggregator):

> T-1 ANNEX (per-scope withheld-T1 records summary -- not new evidence):
> - Total withheld-T1: [N] (source: [scope names])
> - Named example: [scope, Obs #] withheld-T1: [reason] -- per-scope record in [section]
> [If zero: T-1 ANNEX RECALIBRATION]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule | Confidence | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|----------|-----------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings, or empty-state template]

**Tier 2 -- Cross-Skill**
[findings, or empty-state template]

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Applies to all HIGH-blast findings (Tier 1 and Tier 2). OPEN PROPAGATION GAPs that are
HIGH-blast must also be placed in a track.

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

| F-ID or Gap ID | Blast Tier | Confidence rationale | Action |
|----------------|------------|---------------------|--------|

If empty: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

| F-ID or Gap ID | Blast Tier | Interpretive question | Action after confirmation |
|----------------|------------|----------------------|--------------------------|

If empty: apply action-track-empty template.

**Track decision rationale**: HIGH-confidence: finding grounded in a concrete, unambiguous
contract. LOW-confidence: finding depends on spec interpretation requiring confirmation.
OPEN PROPAGATION GAPs that could not be anchored to a spec location default to Track 2.

---

**Tier 3 -- Component-Wide**
[findings, or empty-state template]

**Tier 4 -- Isolated**
[findings, or empty-state template]

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: compounding patterns or empty-state.

---

**PROPAGATION COVERAGE GATE**

Write after Cross-Skill Comparison Protocol, before Structural Compliance Checklist.

| Rule ID | Rule (abbreviated) | Coverage Status | Evidence |
|---------|--------------------|----------------|----------|

Coverage Status values:
- `Covered by [F-ID]` -- a recorded finding accounts for this rule
- `OPEN PROPAGATION GAP [DR-NN]` -- no finding covers this rule; state why

All declared rules must appear. Zero silent drops.

**Confidence track assignment for gaps**: Any OPEN PROPAGATION GAP that would be
HIGH-blast if confirmed must appear in Track 2 of the Confidence-Stratified Action List
with a confirmation question. A gap that cannot be blast-estimated may be listed here
with a note that it bypasses track assignment pending spec clarification.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Final section of the report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section] | [observations, rule-by-rule rejections] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter cited; Sub-claim 2: T-1 ANNEX with named withheld-T1 example; Sub-claim 3: T-1 ANNEX characterizes itself as summary | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each fired section] | [template type and first clause per section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section] | Sub-claim 1: Step 1 table present; Sub-claim 2: Step 2 table present; Sub-claim 3: Step 3 declaration | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: three observables per row; Sub-claim 3: appears before execution | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [per-scope sections + T-1 ANNEX] | Sub-claim 1: vocabulary glossary declared; Sub-claim 2: T-1 rule as if-and-only-if before execution; Sub-claim 3: Disposition columns present for all five sub-skills | fired / partial [name failing sub-claim] / not fired |
| Propagation coverage axis | Dependency Map + Coverage Gate | Sub-claim 1: dependency map present before execution -- rule count; Sub-claim 2: Coverage Gate has one row per declared rule -- row count matches rule count; Sub-claim 3: zero silent drops -- all rules either covered by F-ID or OPEN PROPAGATION GAP with rule ID cited | fired / partial [name failing sub-claim] / not fired |
| Confidence-stratified action list | CONFIDENCE-STRATIFIED ACTION LIST | Sub-claim 1: Track 1 labeled "Implement Now (HIGH-confidence / HIGH-blast)"; Sub-claim 2: Track 2 labeled "Confirm Spec First (LOW-confidence / HIGH-blast)"; Sub-claim 3: every HIGH-blast finding (and every HIGH-blast OPEN PROPAGATION GAP) appears in exactly one track -- none missing, none duplicated | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Cross-Skill Dependency Map >
Observational Discipline > Execution Sequence (five sub-skills with per-scope gate tables)
> Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings
Table > Execution Log > Ranked Findings (Tiers 1-4) > Confidence-Stratified Action List
(Track 1 and Track 2) > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Propagation
Coverage Gate > Structural Compliance Checklist.

Structural commitments:
1. Dependency map declared before execution; gate has one row per rule; zero drops (C-29)
2. Every HIGH-blast finding in exactly one confidence track; Track 2 has confirmation
   question; OPEN PROPAGATION GAPSs that are HIGH-blast included (C-30)
3. Per-scope Disposition columns present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)

---

## V-05 -- Full Integration: Dependency Map + Confidence Stratification + Type-Constrained Verbs (C-29 + C-30 + C-31)

**Variation axis:** Full integration -- V-01 (C-29) + V-02 (C-30) + V-03 (C-31) applied
simultaneously to the R7 V-05 base. This variation tests whether all three new mechanisms
compose without contradiction. The key interaction to test: a finding that is ASSUMPTION-
classified (C-31: Verb must be "confirm") and is also LOW-confidence (C-30: Track 2,
confirmation question required) should reinforce itself -- the C-31 verb "confirm" aligns
with the C-30 track requirement. A GAP-classified finding that is HIGH-confidence should
appear in Track 1 with Verb "add" or "remove." This is the proposed golden prompt for R8.

**Hypothesis:** C-29, C-30, and C-31 all pass by construction. The dependency map is
declared and gated. Action tracks are split by confidence. Remediation verbs are constrained
by finding classification. The three mechanisms reinforce rather than contradict each other
because ASSUMPTION-classified findings naturally map to Track 2 (confirm spec first) and
GAP/CONTRADICTION-classified findings with explicit spec citations naturally map to Track 1
or Track 2 based on whether the spec contract is unambiguous.

---

Simulate the technical behavior of: {{topic}}

This report enforces seven structural axes simultaneously. The first section declares all
seven axes. The last section verifies all seven fired using sub-claim decomposition for
multi-part axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined:
  [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped
  to at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation
  that was considered and failed T-1 for this scope, or confirm scope is clean and state
  why T-1 did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes are clean
  and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or
  no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] empty. Reason: [no HIGH-blast findings at this
  confidence level, or all HIGH-blast findings are in the other track]."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration
  but did not produce observable output in this report. Reason: [why]. Impact: [whether
  the omission affects any findings]."
- **Propagation Coverage Gate no gaps**: "Propagation Coverage Gate: [N] dependency rules
  declared. All [N] rules accounted for by recorded findings. No OPEN PROPAGATION GAPs."
- **Propagation Coverage Gate no rules**: "Dependency map produced zero rules. DEPENDENCY
  MAP RECALIBRATION REQUIRED: Either declare at least one rule, or confirm this topic has
  no cross-skill dependencies and state why."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:             [sequential: F-01, F-02, ...]
Sub-skill:        [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                   trace-permissions]
Type:             [spec-gap / contract-violation / state-anomaly / permission-gap /
                   flow-gap]
Classification:   [GAP / CONTRADICTION / ASSUMPTION --
                   GAP: spec is silent or missing something required
                   CONTRADICTION: spec has two conflicting statements
                   ASSUMPTION: behavior was assumed but not specified]
Spec location:    [REQUIRED: named section, boundary, or interface]
Summary:          [one sentence, problem only]
Impact:           [STANDALONE FIELD: what breaks if unresolved]
Blast radius:     [isolated / component-wide / cross-skill / system-wide]
BR rationale:     [REQUIRED for cross-skill or system-wide]
Dependency rule:  [OPTIONAL: DR-NN if this finding covers a declared dependency rule]
Confidence:       [HIGH / LOW]
Conf rationale:   [one sentence: what anchors HIGH or what question creates LOW]
Remediation:
  Verb:           [CONSTRAINED by Classification:
                   GAP    -> "add" or "remove" ONLY
                   CONTRADICTION -> "resolve" ONLY
                   ASSUMPTION    -> "confirm" ONLY]
  Target:         [specific artifact, section, or interface]
  Location:       [where in the spec or implementation]
  Conformance:    [what passing looks like after remediation]
```

**Classification-Confidence alignment guide** (advisory, not mandatory):
- GAP + HIGH-confidence: spec is unambiguously missing something; add/remove immediately
  (Track 1 natural fit)
- GAP + LOW-confidence: spec may be missing something, but intent is unclear; add/remove
  after confirmation (Track 2)
- CONTRADICTION + HIGH-confidence: two spec locations conflict with no ambiguity about
  which is wrong; resolve immediately (Track 1 natural fit)
- ASSUMPTION + LOW-confidence: behavior assumed without spec basis; confirm before
  implementing (Track 2 natural fit -- C-31 verb "confirm" aligns with C-30 track 2
  requirement)

**Remediation verb vocabulary** (mandatory constraint):

| Classification | Permitted Verbs | Example |
|---------------|----------------|---------|
| GAP | add, remove | "add: error state for expired-token path to Section 3.2 state table" |
| CONTRADICTION | resolve | "resolve: conflicting timeout values between Section 2.1 and 4.3" |
| ASSUMPTION | confirm | "confirm: whether retry visibility is intended in Section 5 lifecycle" |

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section, (b) verify each axis
independently, and (c) identify every gate table schema before reading any execution.
All seven rows must have equal depth: three independently-verifiable sub-observables.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A/B) | (1) Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution: template letter named with rejection count; (3) filter rules 1-4 listed before any row evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template text in any empty section; (2) template cited in compliance checklist by type and first clause; (3) coverage: sub-skill sections, ranked tiers, action tracks, comparison steps, execution log, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1 table: F-ID A, F-ID B, Surface similarity; (2) Step 2 table: Verdict and Reason per pair; (3) Step 3: compounding patterns named, or empty-state citing all Step 2 pairs and verdicts |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, seven rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) This Structural Axis Declaration before any execution; (2) Compliance Checklist as final section -- all multi-part rows use sub-claim decomposition; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope Disposition columns (primary T-1 record) + T-1 ANNEX (summary only) | (1) OBSERVATIONAL DISCIPLINE: vocabulary glossary (four terms), T-1 rule as if-and-only-if; (2) five per-scope gate tables -- Disposition column structural, schema: Obs #/What noticed/Disposition/Classification(if elevated)/T-1 reason/Filter rule; (3) T-1 ANNEX: summary aggregator characterizing itself as such, citing per-scope sources by scope name |
| Propagation coverage axis | C-29 | Cross-Skill Dependency Map (before execution, DR-01 through DR-NN) + Propagation Coverage Gate (after synthesis, one row per rule, zero silent drops) | (1) Dependency map section: numbered rules before any execution section; (2) Coverage Gate: one row per rule -- Rule ID, Coverage Status (F-ID or OPEN PROPAGATION GAP), Evidence; (3) gate row count equals dependency map rule count -- zero silent drops |
| Type-constrained remediation axis | C-31 | Finding Classification (GAP/CONTRADICTION/ASSUMPTION) + Remediation Verb vocabulary constraint + Remediation verb audit at Findings Table close | (1) every finding has Classification field in Findings Table -- cite distribution; (2) every GAP finding: Verb is "add" or "remove" -- cite count; (3) every CONTRADICTION finding: Verb "resolve" and every ASSUMPTION finding: Verb "confirm" -- cite counts; partial verdict names F-ID with out-of-vocabulary verb |

---

**CROSS-SKILL DEPENDENCY MAP**

Write this section immediately after the Structural Axis Declaration. Declare rules before
any observation work begins. Number rules DR-01 through DR-NN.

Dependency rule types:
- Sequential feed: a gap in sub-skill A creates a precondition violation in sub-skill B
- Shared boundary: both sub-skills trace through the same interface; a violation there
  compounds
- Contract-state coupling: a contract mismatch in trace-contract implies a state anomaly
  in trace-state

| Rule ID | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|---------|------|-----------------|-----------------|--------------------------|

If fewer than two rules can be declared: apply the Propagation Coverage Gate no rules
empty-state template and state why this topic has minimal cross-skill dependency.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Cross-Skill Dependency Map, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings
  Table with Classification assigned
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; no Classification assigned
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters
  filter log with rule citation; no Classification assigned at this stage

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column and a Classification column (Classification populated only for
elevated observations). These are the primary records of T-1 application and finding
classification at each scope. The columns are co-located with the sub-skill producing the
observations. An evaluator can verify every T-1 and Classification decision without reading
any post-execution block. If zero withheld-T1 rows for a scope: apply T-1 SCOPE
RECALIBRATION.

**T-1 ANNEX role (summary aggregator only)**: Aggregates Disposition: withheld-T1 records
from all five per-scope gate tables. Is a summary, not a primary source. Must cite
per-scope records by scope name. A T-1 ANNEX naming a withheld-T1 observation absent from
any per-scope Disposition column is a structural violation.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write the per-scope gate table using the declared
schema. Disposition column and Classification column are structural -- do not omit or
rename. Assign Classification at elevation time; note dependency rule if applicable.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located):

| Obs # | What was noticed | Disposition | Classification (if elevated) | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|------------------------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`
Classification (elevated only): `GAP` | `CONTRADICTION` | `ASSUMPTION`

If zero withheld-T1 rows: apply Per-scope Disposition zero withheld-T1 template.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate observations with Disposition: elevated from all five per-scope gate tables.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Classification | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|---------------|----------|-----------------|

Filter rules: (1) no spec location (2) no blast radius (3) style preference (4) duplicate

---

**FILTER LOG RESOLUTION**

**Template A (at least one rejection)**:
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason]).
> Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections)**:
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [condition not met] --
>   per-scope record in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations with Disposition: elevated that passed all four filter rules.

| F-ID | Sub-Skill | Type | Class | Spec Location | Summary | Impact | Blast Radius | Dep Rule | Conf | Verb | Target | Location | Conformance |
|------|-----------|------|-------|--------------|---------|--------|-------------|----------|------|------|--------|----------|-------------|

**Remediation verb audit**: Before closing the Findings Table, confirm type-constraint:
- Every GAP row: Verb is "add" or "remove"
- Every CONTRADICTION row: Verb is "resolve"
- Every ASSUMPTION row: Verb is "confirm"

A row where Verb is not in the permitted set for its Classification is a structural
violation. Correct the Classification or the Verb; do not proceed past the Findings Table
with a known verb violation.

**Classification-Confidence alignment check** (advisory): ASSUMPTION findings should
naturally be LOW-confidence. A HIGH-confidence ASSUMPTION is unusual -- confirm it is not
actually a GAP with unambiguous evidence.

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream rationale; include Classification and Confidence for each;
or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale; include Classification and Confidence;
or: apply ranked-tier empty-state template]

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Applies to all HIGH-blast findings (Tier 1 and Tier 2). OPEN PROPAGATION GAPs that are
HIGH-blast must appear here. LOW-blast findings do not require track assignment.

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

These findings are grounded in explicit spec contracts. No confirmation required.

| F-ID | Class | Blast Tier | Confidence rationale | Action (Verb Target Location) |
|------|-------|------------|---------------------|-------------------------------|

If empty: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

These findings depend on spec interpretation requiring confirmation before implementation.
ASSUMPTION-classified findings belong here by default (C-31 verb "confirm" aligns).

| F-ID | Class | Blast Tier | Confirmation question | Action after confirmation (Verb Target Location) |
|------|-------|------------|-----------------------|--------------------------------------------------|

If empty: apply action-track-empty template.

**Natural alignment rule**: ASSUMPTION findings in Track 2 have Verb "confirm" (C-31) and
a confirmation question (C-30). When an ASSUMPTION finding is in Track 2, its C-31 verb
and its C-30 confirmation question describe the same underlying spec clarification needed.
An evaluator can verify both criteria from the same row without cross-referencing sections.

---

**Tier 3 -- Component-Wide**
[findings; or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings; or: apply ranked-tier empty-state template]

For top three ranked findings across all tiers: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills
sharing surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply comparison-step empty-state template.

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Name compounding patterns, or apply cross-skill-
patterns empty-state template citing all Step 2 pairs.

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

---

**PROPAGATION COVERAGE GATE**

Write after Cross-Skill Comparison Protocol, before Structural Compliance Checklist.

| Rule ID | Rule (abbreviated) | Coverage Status | Evidence |
|---------|--------------------|----------------|----------|

Coverage Status values:
- `Covered by [F-ID]` -- a recorded finding accounts for this dependency rule
- `OPEN PROPAGATION GAP [DR-NN]` -- no finding covers this rule; state: (a) the rule was
  examined and found non-triggering for this topic (why), or (b) the spec input does not
  activate this dependency (why)

Every declared rule must appear. Zero silent drops. A gap that would be HIGH-blast if
confirmed must appear in Track 2 of the Confidence-Stratified Action List above.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names
and evidence from the report produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism, the Status
column must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. Binary PASS or FAIL for a multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding pattern or empty-state with Step 2 pairs cited) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: seven rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: appears before any execution evidence -- confirmed by section ordering | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite whether each has at least one withheld-T1 or T-1 SCOPE RECALIBRATION invoked; T-1 ANNEX confirmed as summary aggregator citing per-scope records | fired / partial [name failing sub-claim] / not fired |
| Propagation coverage axis | Cross-Skill Dependency Map + Propagation Coverage Gate | Sub-claim 1: dependency map declared before execution -- cite rule count and DR-IDs; Sub-claim 2: Coverage Gate has exactly one row per declared rule -- cite that row count equals rule count; Sub-claim 3: zero silent drops -- every rule is either covered by a named F-ID or logged as OPEN PROPAGATION GAP with rule ID cited | fired / partial [name failing sub-claim] / not fired |
| Type-constrained remediation axis | Findings Table + CONFIDENCE-STRATIFIED ACTION LIST | Sub-claim 1: every finding in Findings Table has Classification (GAP/CONTRADICTION/ASSUMPTION) -- cite distribution (e.g., "3 GAP, 1 CONTRADICTION, 2 ASSUMPTION"); Sub-claim 2: every GAP finding has Verb "add" or "remove" -- cite count verified; Sub-claim 3: every CONTRADICTION finding has Verb "resolve" AND every ASSUMPTION finding has Verb "confirm" -- cite counts verified; partial verdict names the specific F-ID with out-of-vocabulary verb | fired / partial [name F-ID with violation] / not fired |
| Confidence-stratified action list | CONFIDENCE-STRATIFIED ACTION LIST | Sub-claim 1: Track 1 labeled "Implement Now (HIGH-confidence / HIGH-blast)" with at least one entry or explicit empty-state template; Sub-claim 2: Track 2 labeled "Confirm Spec First (LOW-confidence / HIGH-blast)" with confirmation questions per finding or explicit empty-state template; Sub-claim 3: every HIGH-blast finding (and every HIGH-blast OPEN PROPAGATION GAP) appears in exactly one track -- none missing, none duplicated; ASSUMPTION findings in Track 2 have confirmation question that matches their C-31 Verb "confirm" | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Cross-Skill Dependency Map >
Observational Discipline > Execution Sequence (five sub-skills, each with co-located
per-scope gate table using Disposition + Classification schema) > Candidate Observations
and Filter Log > Filter Log Resolution (Template A or B, then T-1 ANNEX as summary
aggregator) > Findings Table (with Remediation verb audit) > Execution Log > Ranked
Findings (Tiers 1-4) > Confidence-Stratified Action List (Track 1 and Track 2) >
Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Propagation Coverage Gate >
Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Cross-Skill Dependency Map declared before execution; Propagation Coverage Gate has
   one row per rule; zero silent drops; OPEN PROPAGATION GAPSs logged with rule ID (C-29)
2. Every HIGH-blast finding and HIGH-blast OPEN PROPAGATION GAP in exactly one action
   track; Track 2 entries carry a confirmation question; ASSUMPTION findings are Track 2
   by default with Verb "confirm" aligning to the confirmation question (C-30)
3. Every finding has Classification GAP/CONTRADICTION/ASSUMPTION; Remediation Verb is
   constrained by Classification; out-of-vocabulary verb is a structural violation
   detected at Findings Table close (C-31)
4. Per-scope Disposition column + Classification column present for all five sub-skills;
   Classification assigned at elevation time, co-located (C-25 + C-31 alignment)
5. T-1 ANNEX summarizes per-scope Disposition data; introduces no new evidence (C-25)
6. Compliance checklist uses sub-claim decomposition for all multi-part rows; binary
   verdicts are structural violations (C-24)
7. Seven structural axis rows with equal depth appear before any execution evidence (C-22)
8. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
