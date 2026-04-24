---
skill: campaign-simulate
round: 9
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v8-2026-03-17.md
---

# campaign-simulate -- Round 9 Variations

**Context**: R8 V-01 satisfies C-32 (DR-NN IDs throughout dependency map and Coverage Gate)
and C-33 (propagation coverage as Row 6 + Checklist row 7 with three sub-claims). R8 V-02
satisfies C-33 (confidence stratification axis row + Checklist row), C-34 (empty-state
templates for both action tracks), and C-35 (Conf rationale field in Finding Schema). No R8
variation satisfies all four simultaneously. R9 target: merge C-32 + C-33 + C-34 + C-35 in
a single variation built on the R8 V-05 base (which carries C-29 + C-30 + C-31).

**Under rubric v8**: aspirational pool is 27 criteria capped at 10 pts. Max score 100.
R8 V-05 without C-32/C-33/C-34/C-35 misses up to 4 aspirational criteria in the pool.
R9 V-05 targets all four plus preserves the C-29/C-30/C-31 mechanisms already in V-05.

**Round 9 axes chosen:**
- Single-axis: V-01 (C-32 -- three-point DR-NN citation chain; output format axis),
  V-02 (C-35 -- falsifiable Conf rationale sub-field; output format axis),
  V-03 (C-34 -- full empty-state coverage extending to Coverage Gate and Entity Coverage
  Matrix, not just action tracks; lifecycle emphasis axis)
- Combined: V-04 (C-32 + C-35 -- the two auditability axes merged on the R8 V-01/V-02
  base; output format + phrasing register), V-05 (full integration: C-32 + C-33 + C-34 +
  C-35 on R8 V-05 base; role sequence variation: trace runs before flow to surface
  dependency rules earlier)

---

## V-01 -- Three-Point DR-NN Citation Chain (C-32)

**Variation axis:** Output format -- the dependency rule identifier (DR-NN) must appear in
exactly three places to satisfy C-32: (1) the row in the Cross-Skill Dependency Map where
the rule is declared, (2) the Coverage Gate row that accounts for that rule, and (3) the
`Dep rule cite` field of any finding that instantiates the rule. Citing DR-NN in the map
but not in the Coverage Gate satisfies C-29 but fails C-32. Citing DR-NN in the Coverage
Gate but not in the finding's evidence field satisfies C-29 but fails C-32. The chain must
be complete: every DR-NN declared in step (1) must be traceable to step (2), and any
finding claiming to instantiate a dependency rule must close the chain at step (3).

**Hypothesis:** C-32 passes by construction. Every rule carries a DR-NN assigned at
declaration. Every Coverage Gate row cites the originating DR-NN. Every finding that
covers a dependency rule cites that DR-NN in its `Dep rule cite` field. A reviewer can
verify completeness with a set-membership check: {map DR-NNs} == {gate row DR-NNs union
gap log DR-NNs}, and {gate rows citing F-ID} == {findings with matching DR-NN in Dep rule
cite}. C-30 and C-31 are not targeted -- blast-radius ranking is flat (C-02 satisfied),
remediation uses free-form verbs (C-08 satisfied but not C-31).

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six
axes. The last section verifies all six fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped to
  at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  was considered and failed T-1 for this scope, or confirm scope is clean and state why T-1
  did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes are clean
  and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output in this report. Reason: [why the mechanism did not fire].
  Impact on report validity: [whether the omission affects any findings]."
- **Propagation Coverage Gate no gaps**: "Propagation Coverage Gate: [N] dependency rules
  declared (DR-01 through DR-[N]). All [N] rules accounted for by recorded findings. Rule
  ID to Finding ID map: [DR-NN -> F-NN for each]. No OPEN PROPAGATION GAPs."
- **Propagation Coverage Gate no rules**: "Dependency map produced zero dependency rules.
  DEPENDENCY MAP RECALIBRATION REQUIRED: Either declare at least one rule describing how
  findings from one sub-skill scope constrain or feed another, or confirm that this topic
  has no cross-skill dependencies and state why."

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
Dep rule cite:  [DR-NN if this finding instantiates a declared dependency rule;
                 leave blank if no dependency rule applies --
                 FAILURE: finding covers a declared dependency rule but omits DR-NN
                 here fails C-32; DR-NN cited here must match (1) map declaration row
                 and (2) Coverage Gate row for that rule]
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All six rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing per-scope record by scope name |
| DR-NN citation chain axis | C-29, C-32 | Cross-Skill Dependency Map (DR-01 through DR-NN assigned at declaration) + Propagation Coverage Gate (one row per rule, each row cites originating DR-NN) + Finding Dep rule cite field (each finding covering a dependency rule cites its DR-NN) | (1) Cross-Skill Dependency Map: each row has DR-NN assigned; rule count [N] declared; (2) Propagation Coverage Gate: each row cites originating DR-NN in Rule ID column; row count equals map rule count; (3) every finding with Dep rule cite populated cites a DR-NN that matches a declared rule; set-membership check: {map DR-NNs} == {gate rows union gap log entries} |

The DR-NN citation chain axis in row 6 is a three-point structural commitment. A dependency
map that assigns DR-NNs but produces a Coverage Gate without DR-NN backlinks satisfies C-29
but fails C-32. A finding that covers a dependency rule but omits the DR-NN in Dep rule cite
fails C-32 regardless of Coverage Gate completeness.

---

**CROSS-SKILL DEPENDENCY MAP**

Write this section immediately after the Structural Axis Declaration, before Observational
Discipline. Assign a DR-NN identifier to each rule at declaration time. The DR-NN is
permanent -- it does not change when findings are recorded. A rule declared as DR-03 is
DR-03 in the Coverage Gate and DR-03 in any finding that instantiates it.

| DR-NN | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|-------|------|-----------------|-----------------|--------------------------|

If fewer than two rules can be declared: apply the Propagation Coverage Gate no rules
empty-state template and state why the topic has minimal cross-skill dependency.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Cross-Skill Dependency Map, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout (minimum four terms declared):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; does not enter global filter log
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters filter
  log with rule citation; does not enter Findings Table directly

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1 at the per-scope gate.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes a
Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
An evaluator can verify every T-1 decision from the per-scope gate tables without reading
the T-1 ANNEX. If zero withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION
immediately below that gate table.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope name.
A T-1 ANNEX that names a withheld-T1 observation absent from any per-scope Disposition
column is a structural violation.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
declared schema. The Disposition column is structural -- do not omit it or rename it. Where
a finding covers a declared dependency rule, populate the Dep rule cite field in the Finding
Schema with the originating DR-NN.

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

Only observations that passed T-1 (Disposition: elevated) and all four filter rules
(Elevate?: yes in filter log).

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|--------------|-------------|

Dep Rule Cite: populate with DR-NN if this finding instantiates a declared dependency rule.
A finding with Dep Rule Cite = DR-02 must match: (1) DR-02 in the Cross-Skill Dependency Map
and (2) DR-02 in the Coverage Gate row. Mismatch in any of the three locations fails C-32.

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
Compliance Checklist. For each dependency rule in the Cross-Skill Dependency Map, confirm
coverage status. The Rule ID column must cite the originating DR-NN exactly as declared in
the map. A Coverage Gate row that substitutes prose rule text for the DR-NN identifier
fails C-32 even if the rule text matches.

| Rule ID (DR-NN) | Rule (abbreviated) | Coverage Status | Evidence |
|----------------|--------------------|----------------|----------|
| DR-01 | [rule text] | Covered by [F-ID] / OPEN PROPAGATION GAP | [finding summary or gap reason; if Covered, confirm F-ID's Dep rule cite field = this DR-NN] |

**Coverage Status values**:
- `Covered by [F-ID]` -- a recorded finding accounts for this dependency rule; the finding's
  Dep rule cite field must match this DR-NN (three-point citation check)
- `OPEN PROPAGATION GAP [DR-NN]` -- no finding covers this rule; state why the spec does
  not trigger this dependency

Every rule declared in the dependency map must appear in this table. A rule absent from
both this table and the gap log is a silent drop -- C-29 fail and C-32 fail.

If zero dependency rules were declared: apply the Propagation Coverage Gate no rules
empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names
and evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism, the Status
column must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. Binary PASS or FAIL for a multi-part row is a structural violation of this
checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding pattern or empty-state citing Step 2 pairs) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables in the Observable Output column; Sub-claim 3: section appears before any execution evidence -- confirmed by section ordering | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each scope by sub-skill name | fired / partial [name failing sub-claim] / not fired |
| DR-NN citation chain (C-32) | Cross-Skill Dependency Map + Propagation Coverage Gate + Findings Table | Sub-claim 1: every rule in the dependency map has a DR-NN assigned at declaration -- cite rule count and DR-NN range (DR-01 through DR-[N]); Sub-claim 2: every Coverage Gate row cites originating DR-NN in the Rule ID (DR-NN) column -- cite row count; Sub-claim 3: every finding with Dep rule cite populated names a DR-NN that matches both (a) a map declaration row and (b) the corresponding Coverage Gate row -- cite each F-ID with Dep rule cite and confirm three-point match | fired / partial [name failing sub-claim] / not fired |

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
1. DR-NN assigned to each dependency rule at declaration; same DR-NN used in Coverage Gate
   row and in any finding's Dep rule cite field (C-32 three-point chain)
2. Coverage Gate table has one row per declared rule; every row cites its DR-NN (C-29+C-32)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope Disposition data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
6. A partial compliance verdict names the specific failing sub-claim inline (C-24)
7. Six structural axis rows with equal depth appear before any execution evidence (C-22)
8. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)

---

## V-02 -- Falsifiable Conf Rationale Sub-Field (C-35)

**Variation axis:** Output format -- the Finding Schema `Conf rationale` field is upgraded
from a free-form explanation to a typed, falsifiable argument. For HIGH-confidence findings,
the rationale must name the spec artifact, section, or contract that removes all interpretive
ambiguity. For LOW-confidence findings, the rationale must state the interpretive question
that, when answered, would resolve the ambiguity and permit the rating to be raised to HIGH.
A rationale that states "HIGH -- this is obvious from the spec" does not name a verifiable
artifact and fails C-35. A rationale that states "LOW -- unclear" does not state a
falsifiable question and fails C-35. The format is: `HIGH -- [named spec artifact/section
that establishes the violation unambiguously]` or `LOW -- [the specific interpretive
question: if [X] is confirmed, confidence becomes HIGH]`.

**Hypothesis:** C-35 passes by construction. Every HIGH-blast finding assigned to a C-30
action track carries a Conf rationale citing a named spec artifact (HIGH) or a specific
interpretive question (LOW). A reviewer can check the rationale by locating the named
artifact or verifying that the question is genuine. C-29 is not targeted -- no Cross-Skill
Dependency Map is declared. C-31 is not targeted -- remediation uses free-form verbs.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six
axes. The last section verifies all six fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped to
  at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  was considered and failed T-1 for this scope, or confirm scope is clean and state why T-1
  did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes are clean
  and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] -- executed; zero findings qualified at this
  confidence tier. Reason: [no HIGH-blast findings reached this confidence level / no
  HIGH-blast findings in report]."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output in this report. Reason: [why the mechanism did not fire].
  Impact on report validity: [whether the omission affects any findings]."

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
Confidence:     [HIGH / LOW -- required for all HIGH-blast findings (Tier 1 and Tier 2);
                 HIGH: finding is grounded in a named spec contract with no interpretive
                 ambiguity; LOW: finding depends on spec interpretation not explicitly
                 confirmed -- FAILURE: blank for any HIGH-blast finding fails C-30]
Conf rationale: [REQUIRED for all HIGH-blast findings assigned to a C-30 action track.
                 Format options:
                 "HIGH -- [name the specific spec section/contract/interface that
                  establishes the violation unambiguously -- a reviewer must be able to
                  locate this artifact and confirm the violation without interpretation]"
                 "LOW -- [state the interpretive question: if [specific condition] is
                  confirmed, confidence becomes HIGH -- the question must be concrete
                  enough that answering YES/NO resolves the ambiguity]"
                 FAILURE: rationale does not name a spec artifact (HIGH) or does not
                 state a concrete answerable question (LOW) fails C-35;
                 "HIGH -- obvious", "LOW -- unclear" both fail C-35]
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All six rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1, action tracks |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing per-scope record by scope name |
| Confidence stratification axis | C-30, C-35 | Confidence field in Finding Schema (HIGH/LOW) + Conf rationale sub-field (typed falsifiable argument) + Confidence-Stratified Action List (Track 1: HIGH-confidence/HIGH-blast; Track 2: LOW-confidence/HIGH-blast) | (1) Finding Schema: Confidence field populated for all HIGH-blast findings; Conf rationale sub-field present and typed ("HIGH -- [spec artifact]" or "LOW -- [interpretive question]"); (2) CONFIDENCE-STRATIFIED ACTION LIST section: Track 1 and Track 2 present, each with named label; (3) every HIGH-blast finding appears in exactly one track; no HIGH-blast finding in neither track nor in both tracks |

The confidence stratification axis in row 6 formalizes C-35: the Conf rationale field is
not satisfied by a label. "HIGH -- spec section 4.2 defines the permission boundary" is a
verifiable claim; "HIGH" is an assertion. The typed format ensures reviewers can check the
rationale without reading context.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout (minimum four terms declared):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; does not enter global filter log
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters filter
  log with rule citation; does not enter Findings Table directly

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1 at the per-scope gate.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes a
Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
If zero withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION immediately
below that gate table.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope name.

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

If zero withheld-T1 rows: apply Per-scope Disposition zero withheld-T1 template immediately
below the gate table before advancing.

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

Declare the gate state. This block is required in every report.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason
> for each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after Template A or B -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met] --
>   per-scope record in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Confidence | Conf Rationale | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-----------|----------------|-------------|

Conf Rationale must follow the typed format: "HIGH -- [named spec artifact]" or
"LOW -- [concrete interpretive question]". Populate for all HIGH-blast findings.
LOW-blast findings (Tier 3, Tier 4) are exempt from Conf Rationale.

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

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Applies to all HIGH-blast findings (Tier 1 and Tier 2). LOW-blast findings are not
stratified.

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

These findings are grounded in explicit, unambiguous spec contracts. The Conf rationale
for each finding names the spec artifact that removes all interpretive uncertainty. No
clarification is needed before implementation begins.

| F-ID | Blast Tier | Conf Rationale (must name spec artifact) | Action |
|------|------------|------------------------------------------|--------|

If no HIGH-confidence / HIGH-blast findings: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

These findings depend on spec interpretation that has not been explicitly confirmed. The
Conf rationale for each finding states the interpretive question. Implementation is
authorized only after the question is answered YES.

| F-ID | Blast Tier | Conf Rationale (must state interpretive question) | Action after confirmation |
|------|------------|---------------------------------------------------|--------------------------|

If no LOW-confidence / HIGH-blast findings: apply action-track-empty template.

---

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

For top three ranked findings across all tiers: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Name compounding patterns, or apply cross-skill-patterns
empty-state template citing every pair from Step 2.

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Cite actual section names and evidence from this report.

**Sub-claim architecture rule**: Multi-part mechanism rows must declare sub-claim-level
statuses using `fired / partial / not-fired` per named sub-claim. Binary PASS or FAIL
for a multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason; Sub-claim 3: T-1 ANNEX characterizes itself as summary | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present; Sub-claim 2: Step 2 table present; Sub-claim 3: Step 3 declaration present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate section names] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills | fired / partial [name failing sub-claim] / not fired |
| Confidence stratification + Conf rationale (C-30/C-35) | CONFIDENCE-STRATIFIED ACTION LIST + Findings Table | Sub-claim 1: Track 1 present with label "Implement Now (HIGH-confidence / HIGH-blast)"; Sub-claim 2: Track 2 present with label "Confirm Spec First (LOW-confidence / HIGH-blast)"; Sub-claim 3: every HIGH-blast finding's Conf rationale follows typed format ("HIGH -- [named artifact]" or "LOW -- [concrete question]") -- no finding states only "HIGH" or "LOW" without a falsifiable argument | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (five sub-skills, each with co-located per-scope gate table) >
Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) >
Findings Table > Execution Log > Ranked Findings (Tiers 1-2) > Confidence-Stratified
Action List (Track 1 and Track 2) > Ranked Findings (Tiers 3-4) > Cross-Skill Comparison
Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Every HIGH-blast finding carries Confidence (HIGH/LOW) and a typed Conf rationale that
   names a spec artifact (HIGH) or states a concrete interpretive question (LOW) (C-35)
2. Every HIGH-blast finding appears in exactly one of Track 1 or Track 2 (C-30)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
6. Six structural axis rows with equal depth appear before any execution evidence (C-22)

---

## V-03 -- Full Empty-State Coverage Including Coverage Gate and Entity Coverage Matrix (C-34)

**Variation axis:** Lifecycle emphasis -- the empty-state template set is extended to cover
ALL structured output sections with a schema, not just action tracks. C-34 requires: action
tracks (C-30), Coverage Gate (C-29), T-1 ANNEX (C-23), and Entity Coverage Matrix (C-27).
R8 V-02 covered action tracks. This variation adds two new empty-state contexts: (1) the
Coverage Gate when all rules are covered with no gaps (not zero rules, but zero gaps), and
(2) the Entity Coverage Matrix when all entities in the Topic Entity Manifest show COVERED
or CLEAN status with no SKIPPED entries. The Structural Axis Declaration empty-state row
must enumerate all four section types by name. The Compliance Checklist must verify all
four contexts.

**Hypothesis:** C-34 passes by construction. No structured output section is silently absent.
Coverage Gate either contains rows or shows its empty-state template. Entity Coverage Matrix
either contains rows with at least one SKIPPED entry (treated as execution gap) or shows
its all-CLEAN template confirming the section executed and found no gaps. C-32 is not
targeted -- no DR-NN IDs in this variation. C-35 is not targeted -- Conf rationale is free
form.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six
axes. The last section verifies all six fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected, or (b) justify that every
  candidate is genuinely anchored to a named spec location."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  was considered and failed T-1 for this scope, or confirm scope is clean and state why."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes are clean
  and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] -- executed; zero findings qualified. Reason: [no
  HIGH-blast findings at this confidence level, or no HIGH-blast findings in report]."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output. Reason: [why]. Impact: [whether affects findings]."
- **Coverage Gate no rules**: "Dependency map produced zero dependency rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED: Either declare at least one rule, or confirm this topic has no
  cross-skill dependencies and state why."
- **Coverage Gate all rules covered (no gaps)**: "Propagation Coverage Gate -- executed.
  [N] dependency rules declared. All [N] rules accounted for by recorded findings: [list
  rule -> F-ID pairs]. No OPEN PROPAGATION GAPs. Section present to confirm execution;
  no gaps to report does not mean the gate was skipped."
- **Entity Coverage Matrix all clean (no SKIPPED entities)**: "Entity Coverage Matrix --
  executed. [N] entities from Topic Entity Manifest evaluated. Status: [list entity names
  with COVERED or CLEAN]. Zero SKIPPED entries. All entities reached by at least one
  sub-skill execution. Section present to confirm execution; absence of SKIPPED entries
  does not mean the matrix was skipped."

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
Confidence:     [HIGH / LOW for HIGH-blast findings -- required for Tier 1 and Tier 2]
Conf rationale: [one sentence: why this confidence rating]
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All six rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11, C-34 | Per-section empty-state templates for ALL structured output sections with a schema; silent sections prohibited for four named section types | (1) Named template text in any structured section with no qualifying content; (2) four section types guarded: (a) action tracks, (b) Coverage Gate, (c) T-1 ANNEX, (d) Entity Coverage Matrix -- each either contains content or displays its named empty-state template; (3) compliance checklist verifies all four section types by name |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column + T-1 ANNEX (summary aggregator only) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables with Disposition column as structural field; (3) T-1 ANNEX: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason |
| Confidence stratification axis | C-30 | Confidence field in Finding Schema (HIGH/LOW) + Confidence-Stratified Action List (Track 1: HIGH-confidence/HIGH-blast; Track 2: LOW-confidence/HIGH-blast) | (1) Confidence field populated for all HIGH-blast findings; (2) CONFIDENCE-STRATIFIED ACTION LIST section present with Track 1 and Track 2 labeled; (3) every HIGH-blast finding appears in exactly one track; each empty track displays its named action-track-empty template rather than being silently absent |

The empty-state axis in row 2 is extended by C-34 from action tracks only to four named
section types. The Coverage Gate and Entity Coverage Matrix must now demonstrate execution
even when their content is "no gaps" or "all clean" -- absence of problems does not excuse
absence of the section.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout (minimum four terms declared):
- "Candidate observation" -- an observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition value: passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- Disposition value: failed T-1; primary record in per-scope Disposition
  column; aggregated in T-1 ANNEX; does not enter global filter log
- "withheld-rule" -- Disposition value: passed T-1 but failed filter rule 1-4; enters filter
  log with rule citation; does not enter Findings Table directly

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1 at the per-scope gate.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes a
Disposition column as the primary record of T-1 application at that scope. If zero
withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION immediately below.

**T-1 ANNEX role (summary aggregator only)**: Aggregates Disposition: withheld-T1 records
from all five per-scope gate tables. Is a summary, not a primary evidence source. Must cite
per-scope source records by scope name.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write its per-scope gate table.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected. Gate operating normally.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total: [N] (source: [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [reason] -- per-scope record
>   in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**TOPIC ENTITY MANIFEST**

Before execution, list all entities in scope for this topic. Each entity will appear in the
Entity Coverage Matrix after synthesis with a COVERED / CLEAN / SKIPPED status.

| Entity # | Entity Name | Type (contract / state-machine / permission-boundary / lifecycle-phase) |
|----------|-------------|-------------------------------------------------------------------------|

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

**ENTITY COVERAGE MATRIX**

One row per entity from the Topic Entity Manifest. This section is always present.

| Entity # | Entity Name | Status | Sub-Skills that touched this entity | Notes |
|----------|-------------|--------|-------------------------------------|-------|

Status values:
- `COVERED` -- at least one finding was recorded for this entity
- `CLEAN` -- entity was examined; no findings elevated
- `SKIPPED` -- entity was not reached by any sub-skill execution; treated as execution gap

If all entities show COVERED or CLEAN with zero SKIPPED: apply Entity Coverage Matrix
all-clean empty-state template immediately below the table.
If any entity shows SKIPPED: annotate as execution gap in the Notes column.

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

---

**CONFIDENCE-STRATIFIED ACTION LIST**

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

| F-ID | Blast Tier | Confidence rationale | Action |
|------|------------|---------------------|--------|

If no HIGH-confidence / HIGH-blast findings: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

| F-ID | Blast Tier | Interpretive question (confirm before implementing) | Action after confirmation |
|------|------------|-----------------------------------------------------|--------------------------|

If no LOW-confidence / HIGH-blast findings: apply action-track-empty template.

---

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Name compounding patterns or apply cross-skill-patterns
empty-state template.

---

**PROPAGATION COVERAGE GATE**

Write after Cross-Skill Comparison Protocol. One row per dependency rule.

| Rule ID | Rule (abbreviated) | Coverage Status | Evidence |
|---------|--------------------|----------------|----------|

If Coverage Gate has no rows (no rules declared): apply Coverage Gate no rules
empty-state template.

If all rules are covered with no gaps: apply Coverage Gate all-rules-covered
empty-state template after the table to confirm the gate executed.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Sub-claim architecture rule applies to all multi-part rows.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total, named example, per-scope source; Sub-claim 3: T-1 ANNEX characterizes itself as summary | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates -- full C-34 coverage | [list all sections where any template fired] | Sub-claim 1: action track empty-state templates -- Track 1 and Track 2 each either contain findings or display named template (cite which tracks fired template, if any); Sub-claim 2: Coverage Gate empty-state -- section present with either content rows or named template (cite which template fired, if any); Sub-claim 3: T-1 ANNEX RECALIBRATION and Entity Coverage Matrix all-clean -- each section present with content or named template (cite which fired, if any) | fired / partial [name failing sub-claim] / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present; Sub-claim 2: Step 2 table present; Sub-claim 3: Step 3 declaration present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate section names] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills | fired / partial [name failing sub-claim] / not fired |
| Confidence stratification axis | CONFIDENCE-STRATIFIED ACTION LIST | Sub-claim 1: Track 1 present; Sub-claim 2: Track 2 present; Sub-claim 3: every HIGH-blast finding in exactly one track | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (five sub-skills with co-located per-scope gate tables) > Topic Entity
Manifest > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) >
Findings Table > Execution Log > Entity Coverage Matrix > Ranked Findings (Tiers 1-2) >
Confidence-Stratified Action List (Track 1 and Track 2) > Ranked Findings (Tiers 3-4) >
Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Propagation Coverage Gate > Structural
Compliance Checklist.

Structural commitments that must hold in every report:
1. Every structured output section with a schema is present with either content or its
   named empty-state template -- no section silently absent (C-34)
2. Four section types guarded by name: action tracks, Coverage Gate, T-1 ANNEX, ECM (C-34)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)

---

## V-04 -- DR-NN Three-Point Citation Chain + Falsifiable Conf Rationale (C-32 + C-35)

**Variation axis:** Output format + phrasing register -- the two auditability enhancements
combined. C-32 requires every dependency rule to carry a DR-NN identifier that appears in
three places: map declaration, Coverage Gate row, and finding's Dep rule cite field. C-35
requires every HIGH-blast finding's Confidence field to carry a Conf rationale sub-field
in typed falsifiable format. Together these two mechanisms make the dependency chain and the
confidence assignment independently auditable without reading context: the DR-NN chain
converts the Coverage Gate from prose to a set-membership lookup, and the typed Conf
rationale converts a label into an argument. C-34 is not targeted -- empty-state templates
cover action tracks and T-1 ANNEX only (R8 V-02 level). C-31 is not targeted.

**Phrasing register**: Structural commitments are stated imperatively in second person ("you
must", "do not") rather than the declarative "must be" form used in V-01 through V-03. This
variation tests whether register affects execution fidelity on complex multi-mechanism tasks.

**Hypothesis:** C-32 and C-35 both pass. The dependency map carries DR-NNs; the Coverage
Gate re-cites them; findings close the chain. Every HIGH-blast finding carries a typed Conf
rationale that a reviewer can check without reading the spec. C-33 also passes: the
Structural Axis Declaration has eight rows, one per targeted quality axis (propagation +
confidence stratification added to the base five), each with three sub-observables.

---

Simulate the technical behavior of: {{topic}}

You will enforce eight structural axes in this report. Write the declaration first, execution
last. Every structured section you commit to in the declaration must appear in the report.

---

**EMPTY-STATE TEMPLATES**

You must use these templates when a section has no content. Do not omit any section; do not
leave any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: revisit candidate list -- either name
  one observation that should be rejected, or justify every candidate is anchored."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: name one failing observation or
  confirm scope clean."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 across all scopes. RECALIBRATION
  REQUIRED: identify a withheld-T1 observation or confirm all scopes clean."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] -- executed; zero findings qualified. Reason: [reason]."
- **Comparison step with no pairs**: "No findings from multiple sub-skills for pairwise
  comparison."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list
  pairs and verdicts]."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but did not fire. Reason: [why].
  Impact: [whether affects findings]."
- **Propagation Coverage Gate no rules**: "Zero dependency rules declared. DEPENDENCY MAP
  RECALIBRATION REQUIRED: declare at least one rule or confirm no cross-skill dependencies."
- **Propagation Coverage Gate no gaps**: "Coverage Gate executed. All [N] rules covered.
  Rule-to-finding map: [DR-NN -> F-NN for each]. No OPEN PROPAGATION GAPs."

---

**FINDING SCHEMA**

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
Dep rule cite:  [DR-NN if this finding covers a declared dependency rule; blank if not.
                 You must use the exact DR-NN from the map declaration. The same DR-NN
                 must appear in: (1) the map declaration row, (2) the Coverage Gate row,
                 (3) this field. Do not use rule text in place of the ID.]
Confidence:     [HIGH / LOW -- required for Tier 1 and Tier 2 findings]
Conf rationale: [REQUIRED for Tier 1 and Tier 2 findings. You must use one of these
                 two formats exactly:
                 "HIGH -- [name the spec section/contract/interface that removes all
                  interpretive ambiguity -- a reviewer must be able to locate this]"
                 "LOW -- [state the interpretive question: if [X], then confidence
                  becomes HIGH -- the question must be answerable YES/NO]"
                 Do not write "HIGH" or "LOW" alone. Do not write vague explanations.
                 "HIGH -- the spec is clear" fails this field. "LOW -- ambiguous" fails.]
Remediation:    [REQUIRED: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this as the first section of your output. Eight rows. Equal depth: three
independently-verifiable sub-observables per row.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Filter Log table with Elevate? and Rejection Reason; (2) Filter Log Resolution: template letter named with rejection count; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section templates for all section types; silence prohibited | (1) Template text in any empty section; (2) template type and first clause in compliance checklist per fired section; (3) sections covered: sub-skill, ranked tiers, comparison steps, execution log, Disposition zero-withheld-T1, action tracks |
| Cross-skill comparison axis | C-15 | Three-step protocol (pairings, verdicts, patterns) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity; (2) Step 2 table with Verdict and Reason; (3) Step 3: pattern named or empty-state template citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, eight rows) + Compliance Checklist (last section, sub-claim architecture) | (1) This declaration: eight rows with three sub-observables each; (2) Compliance Checklist: last section, all multi-part rows use sub-claim decomposition; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator) | (1) OBSERVATIONAL DISCIPLINE: genre with vocabulary glossary, T-1 rule as if-and-only-if; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator, names at least one withheld-T1 by scope and reason |
| DR-NN citation chain axis | C-29, C-32 | Cross-Skill Dependency Map (DR-NN at declaration) + Coverage Gate (DR-NN in Rule ID column) + Finding Dep rule cite (DR-NN closes the chain) | (1) Dependency map: each rule has DR-NN; range DR-01 through DR-[N]; (2) Coverage Gate: each row's Rule ID column cites DR-NN exactly matching the map; (3) every finding with Dep rule cite populated has a DR-NN matching both map and gate -- three-point verification |
| Confidence stratification axis | C-30 | Confidence field (HIGH/LOW) + Confidence-Stratified Action List (Track 1 / Track 2) | (1) Confidence field populated for all HIGH-blast findings; (2) Track 1 and Track 2 present with named labels; (3) every HIGH-blast finding in exactly one track |
| Conf rationale auditability axis | C-35 | Conf rationale sub-field in typed falsifiable format ("HIGH -- [artifact]" or "LOW -- [question]") | (1) Conf rationale populated for every Tier 1 and Tier 2 finding; (2) every HIGH Conf rationale names a locatable spec artifact; (3) every LOW Conf rationale states an answerable YES/NO interpretive question |

---

**CROSS-SKILL DEPENDENCY MAP**

Write immediately after the Structural Axis Declaration, before Observational Discipline.
Assign DR-NN at declaration time. The DR-NN is permanent.

| DR-NN | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|-------|------|-----------------|-----------------|--------------------------|

---

**OBSERVATIONAL DISCIPLINE**

**Genre declaration**: This report is a pre-implementation simulation findings document.
Vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition: passed T-1 AND all four filter rules
- "withheld-T1" -- Disposition: failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- Disposition: passed T-1 but failed a filter rule

**T-1 threshold rule** (before any sub-skill fires): Elevated if and only if names a
specific spec location AND describes a gap/violation causing incorrect implementation.

**Per-scope Disposition rule**: Each gate table has a Disposition column as primary T-1
record. If zero withheld-T1 for a scope: apply T-1 SCOPE RECALIBRATION immediately.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by scope name. No new
evidence.

---

**EXECUTION SEQUENCE**

Run in order. Write per-scope gate table after each sub-skill. Where a finding covers a
dependency rule, populate Dep rule cite with the originating DR-NN.

1. flow-lifecycle    -- lifecycle trace with phase contracts and exception flows
2. flow-conversation -- conversational simulation with dead-end and loop detection
3. trace-state       -- state transition compilation with preconditions and invariants
4. trace-contract    -- expected vs actual comparison at contract boundaries
5. trace-permissions -- RBAC trace with privilege escalation detection

**Per-scope gate table**:

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

Filter rules: (1) no specific spec location; (2) no blast radius; (3) style preference;
(4) duplicates a higher-blast finding.

---

**FILTER LOG RESOLUTION**

Template A or Template B (required). T-1 ANNEX immediately after.

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Confidence | Conf Rationale | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|--------------|-----------|----------------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|

---

**RANKED FINDINGS**

Tier 1 -- System-Wide / Tier 2 -- Cross-Skill / Tier 3 -- Component-Wide / Tier 4 -- Isolated.
Apply ranked-tier empty-state template for any empty tier.

---

**CONFIDENCE-STRATIFIED ACTION LIST**

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

| F-ID | Blast Tier | Conf Rationale (cite spec artifact) | Action |
|------|------------|-------------------------------------|--------|

Apply action-track-empty template if no qualifying findings.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

| F-ID | Blast Tier | Conf Rationale (state interpretive question) | Action after confirmation |
|------|------------|----------------------------------------------|--------------------------|

Apply action-track-empty template if no qualifying findings.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Steps 1, 2, 3 -- complete all three. Step 3 requires Steps 1 and 2.

---

**PROPAGATION COVERAGE GATE**

| Rule ID (DR-NN) | Rule (abbreviated) | Coverage Status | Evidence |
|----------------|--------------------|----------------|----------|

Apply Coverage Gate no rules template or Coverage Gate no gaps template as applicable.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Sub-claim architecture rule: multi-part rows must use fired/partial/not-fired per named
sub-claim. Binary PASS or FAIL for any multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section] | [total obs, rejection counts by rule] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX -- total, example, per-scope source; Sub-claim 3: T-1 ANNEX as summary | fired / partial / not fired |
| Empty-state templates | [sections that fired] | [template type and first clause] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 present; Sub-claim 2: Step 2 present; Sub-claim 3: Step 3 present | fired / partial / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: eight rows present; Sub-claim 2: each row has three sub-observables; Sub-claim 3: section before any execution | fired / partial / not fired |
| Observational discipline | [per-scope sections] + T-1 ANNEX | Sub-claim 1: genre + vocabulary; Sub-claim 2: T-1 if-and-only-if stated; Sub-claim 3: Disposition column in all five per-scope gates | fired / partial / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: each map rule has DR-NN -- cite count and range; Sub-claim 2: each Coverage Gate row cites DR-NN in Rule ID (DR-NN) column -- cite row count; Sub-claim 3: each finding with Dep rule cite populated names a DR-NN matching both map and gate -- cite each F-ID and confirm | fired / partial / not fired |
| Confidence stratification (C-30) | CONFIDENCE-STRATIFIED ACTION LIST | Sub-claim 1: Track 1 present; Sub-claim 2: Track 2 present; Sub-claim 3: every HIGH-blast finding in exactly one track | fired / partial / not fired |
| Conf rationale typed format (C-35) | Findings Table | Sub-claim 1: every Tier 1 and Tier 2 finding has Conf rationale populated; Sub-claim 2: every HIGH Conf rationale names a locatable spec artifact (format: "HIGH -- [artifact name]"); Sub-claim 3: every LOW Conf rationale states a concrete YES/NO answerable question (format: "LOW -- [question]") | fired / partial / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Cross-Skill Dependency Map >
Observational Discipline > Execution Sequence > Candidate Observations and Filter Log >
Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Confidence-
Stratified Action List > Cross-Skill Comparison Protocol > Propagation Coverage Gate >
Structural Compliance Checklist.

Structural commitments:
1. DR-NN appears in exactly three places per rule: map declaration, Coverage Gate row,
   finding Dep rule cite (when applicable) -- three-point chain verified in checklist (C-32)
2. Conf rationale typed format: "HIGH -- [artifact]" or "LOW -- [question]" for all
   Tier 1 and Tier 2 findings (C-35)
3. Eight axis rows in declaration, each with three sub-observables (C-22, C-33)
4. Every HIGH-blast finding in exactly one action track (C-30)
5. Per-scope Disposition column in all five sub-skill gate tables (C-25)
6. Sub-claim decomposition in compliance checklist for all multi-part rows (C-24)

---

## V-05 -- Full Integration: C-32 + C-33 + C-34 + C-35 on R8 V-05 Base (All Four R8 Criteria)

**Variation axis:** Role sequence + full integration -- trace sub-skills run before flow
sub-skills to surface dependency rules in the platform layer (where contracts are clearest)
before the domain layer is examined. This allows the Cross-Skill Dependency Map to be
populated with high-confidence DR-NN rules before flow-lifecycle introduces domain-specific
ambiguity. Execution order: trace-state > trace-contract > trace-permissions > flow-lifecycle
> flow-conversation. All four R8 aspirational criteria are targeted simultaneously on the
full R8 V-05 base (which carries C-29, C-30, C-31 plus all essential criteria).

**What this variation adds vs R8 V-05:**
- C-32: DR-NN IDs required in three places (map + gate + finding Dep rule cite field); three-
  point citation chain verified in Compliance Checklist as a new row
- C-33: Structural Axis Declaration self-extends to nine rows -- one per targeted quality axis
  (base five + propagation/C-32 + confidence-stratification/C-35 + type-verb-binding/C-31 +
  empty-state-full-coverage/C-34); Compliance Checklist adds corresponding rows
- C-34: Empty-state templates extended to all four structured section types (action tracks,
  Coverage Gate, T-1 ANNEX, Entity Coverage Matrix); Structural Axis Declaration empty-state
  row explicitly names all four; Compliance Checklist C-34 row verifies all four by sub-claim
- C-35: Conf rationale sub-field uses typed falsifiable format ("HIGH -- [artifact]" or
  "LOW -- [question]"); Compliance Checklist C-35 row verifies format adherence

**Hypothesis:** All four R8 aspirational criteria pass. C-32: DR-NN chain has three-point
verification in the checklist. C-33: nine axis rows self-extended from base five by four
quality-axis additions, each with three sub-observables and a corresponding checklist row.
C-34: every structured section either has content or displays its named empty-state template;
checklist verifies all four section types by sub-claim. C-35: every HIGH-blast finding has
a typed Conf rationale verified by checklist sub-claim 2 and sub-claim 3.

---

Simulate the technical behavior of: {{topic}}

This report enforces nine structural axes simultaneously. The first section declares all nine
axes. The last section verifies all nine fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: revisit candidate list. Either (a) name
  at least one observation that should be rejected, or (b) justify that every candidate is
  genuinely anchored to a named spec location and scoped to at least one downstream
  component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  was considered and failed T-1, or confirm scope clean and state why T-1 did not fire."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes clean and
  state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Action track empty**: "Track [1/2] -- executed; zero findings qualified at this
  confidence tier. Reason: [no HIGH-blast findings at this confidence level / no HIGH-blast
  findings in report at all]."
- **Coverage Gate no rules**: "Dependency map produced zero dependency rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED: Either declare at least one rule describing cross-skill dependency,
  or confirm this topic has no cross-skill dependencies and state why."
- **Coverage Gate all rules covered (no gaps)**: "Propagation Coverage Gate -- executed. [N]
  rules declared (DR-01 through DR-[N]). All [N] rules covered. Rule-to-finding map:
  [DR-NN -> F-NN]. Zero OPEN PROPAGATION GAPs. Section present to confirm gate execution."
- **Entity Coverage Matrix all clean (no SKIPPED)**: "Entity Coverage Matrix -- executed.
  [N] entities evaluated. All show COVERED or CLEAN. Zero SKIPPED. Section present to
  confirm execution; absence of SKIPPED entries does not mean the matrix was skipped."
- **Comparison step with no pairs**: "No findings from multiple sub-skills for pairwise
  comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs and
  verdicts: [list]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but did not produce observable
  output. Reason: [why]. Impact on report validity: [whether affects findings]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:              [sequential: F-01, F-02, ...]
Sub-skill:         [trace-state / trace-contract / trace-permissions / flow-lifecycle /
                    flow-conversation]
Classification:    [GAP / CONTRADICTION / ASSUMPTION --
                    FAILURE: untyped finding fails C-31]
Type:              [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:     [REQUIRED: named section, boundary, or interface --
                    FAILURE: vague reference fails this field]
Summary:           [one sentence, problem only --
                    FAILURE: merging Impact into Summary fails C-06]
Impact:            [STANDALONE FIELD: what breaks if unresolved --
                    FAILURE: blank or merged with Summary fails C-06]
Blast radius:      [isolated / component-wide / cross-skill / system-wide]
BR rationale:      [REQUIRED for cross-skill or system-wide --
                    FAILURE: wide-scope finding without rationale fails C-10]
Dep rule cite:     [DR-NN if this finding instantiates a declared dependency rule; blank
                    if no dependency rule applies --
                    FAILURE: finding covers a declared rule but omits DR-NN here fails C-32;
                    DR-NN cited must match both the map declaration row and the Coverage Gate
                    row for that rule (three-point chain)]
Confidence:        [HIGH / LOW -- required for Tier 1 and Tier 2 findings --
                    FAILURE: blank for any HIGH-blast finding fails C-30]
Conf rationale:    [REQUIRED for Tier 1 and Tier 2 findings.
                    Use one of these formats exactly:
                    "HIGH -- [name the spec section/contract/interface that establishes
                     the violation unambiguously -- reviewer must be able to locate it]"
                    "LOW -- [state the interpretive question: if [condition X] is confirmed,
                     confidence becomes HIGH -- question must be answerable YES/NO]"
                    FAILURE: "HIGH" alone, "LOW -- unclear", or vague text fails C-35.
                    Tier 3 and Tier 4 findings are exempt from this field.]
Remediation verb:  [constrained by Classification:
                    GAP -> "add" or "remove" -- FAILURE: other verb fails C-31
                    CONTRADICTION -> "resolve" -- FAILURE: other verb fails C-31
                    ASSUMPTION -> "confirm" -- FAILURE: other verb fails C-31]
Target:            [specific target at which the Verb is applied]
Location:          [named location: function, module, interface, section]
Conformance:       [pass condition -- how to verify the remediation was applied correctly]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. Nine rows -- one per targeted
quality axis. An evaluator reading only this section must be able to (a) predict every
structural section in the report, (b) verify each axis independently, and (c) identify the
exact schema of each gate table. All nine rows must have equal depth: three independently-
verifiable sub-observables in the Observable Output column.

C-33 self-extension rule: the base five axes (filtering, empty-state, cross-skill comparison,
declaration-compliance, observational discipline) are supplemented by one row per quality
axis targeted by this simulation. This simulation targets C-29/C-32 (propagation + DR-NN),
C-30/C-35 (confidence + rationale), C-31 (type-verb), and C-34 (full empty-state). Each
produces one additional axis row. A fixed-depth template without these rows satisfies C-22
but fails C-33.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter named with rejection count; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state base axis | C-11 | Per-section templates for sub-skill, ranked-tier, comparison, execution log, and Disposition sections | (1) Template text in any empty section; (2) template type and first clause in compliance checklist per fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings, verdicts, patterns | (1) Step 1 table with F-ID A, F-ID B, Surface similarity; (2) Step 2 table with Verdict and Reason; (3) Step 3 declaration: pattern or empty-state template citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, nine rows) + Compliance Checklist (last section, sub-claim architecture) | (1) This declaration: nine rows before any execution; (2) Compliance Checklist: last section, sub-claim decomposition for all multi-part rows; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator) | (1) OBSERVATIONAL DISCIPLINE: genre with vocabulary glossary (four terms), T-1 rule as if-and-only-if; (2) five per-scope gates with Disposition column (structural); (3) T-1 ANNEX: summary aggregator, names at least one withheld-T1 by scope and reason |
| DR-NN citation chain axis | C-29, C-32 | Cross-Skill Dependency Map (DR-NN at declaration) + Coverage Gate (DR-NN in Rule ID column) + Finding Dep rule cite (DR-NN closes three-point chain) | (1) Dependency map: each rule assigned DR-NN at declaration; range DR-01 through DR-[N] stated; (2) Coverage Gate: each row's Rule ID (DR-NN) column cites exactly the DR-NN from the map; (3) each finding with Dep rule cite populated names a DR-NN matching both map and gate -- three-point chain verifiable by set membership |
| Confidence stratification + rationale axis | C-30, C-35 | Confidence field (HIGH/LOW) + typed Conf rationale sub-field ("HIGH -- [artifact]" or "LOW -- [question]") + Confidence-Stratified Action List (Track 1 / Track 2) | (1) Confidence and typed Conf rationale populated for all Tier 1 and Tier 2 findings; (2) Track 1 and Track 2 present with named labels; each empty track shows action-track-empty template; (3) every Tier 1/Tier 2 Conf rationale follows typed format -- reviewer can verify by locating artifact (HIGH) or checking question answerability (LOW) |
| Type-verb binding axis | C-31 | Classification field (GAP/CONTRADICTION/ASSUMPTION) + Remediation verb constrained by Classification | (1) Classification field populated for all findings: GAP / CONTRADICTION / ASSUMPTION; (2) Remediation verb in vocabulary for each type: GAP -> add/remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm; (3) Remediation Quality Gate table: Verb / Target / Location / Conformance columns with all rows populated |
| Full empty-state coverage axis | C-34 | Empty-state templates for all four structured output sections with schemas: action tracks, Coverage Gate, T-1 ANNEX, Entity Coverage Matrix | (1) Action tracks: Track 1 and Track 2 each either contain findings or display action-track-empty template -- no silent absence; (2) Coverage Gate: section present with content rows or Coverage Gate no-rules or Coverage Gate all-covered template -- no silent absence; (3) T-1 ANNEX and Entity Coverage Matrix: each present with content or named empty-state template -- no silent absence |

---

**CROSS-SKILL DEPENDENCY MAP**

Write immediately after the Structural Axis Declaration, before Observational Discipline.
Assign DR-NN at declaration. This simulation runs trace sub-skills first (trace-state,
trace-contract, trace-permissions), so dependency rules from the platform layer are known
before the domain layer (flow-lifecycle, flow-conversation) is examined. Anticipate rules
where platform findings constrain domain interpretation.

| DR-NN | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|-------|------|-----------------|-----------------|--------------------------|

If fewer than two rules can be declared: apply Propagation Coverage Gate no rules template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Cross-Skill Dependency Map, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition: passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- Disposition: failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- Disposition: passed T-1 but failed a filter rule

**T-1 threshold rule** (before any sub-skill fires): Elevated if and only if names a
specific spec location AND describes a gap or violation causing incorrect implementation.

**Per-scope Disposition rule**: Each gate table has a Disposition column as primary T-1
record. If zero withheld-T1 for a scope: apply T-1 SCOPE RECALIBRATION immediately.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by scope name. No
new evidence.

---

**EXECUTION SEQUENCE**

Run in this order (trace before flow -- platform before domain). After each sub-skill, write
its per-scope gate table. Where a finding instantiates a dependency rule, populate Dep rule
cite with the originating DR-NN.

1. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
2. trace-contract    -- expected vs actual comparison at contract boundaries
3. trace-permissions -- RBAC trace with privilege escalation detection
4. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
5. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1 rows: apply Per-scope Disposition zero withheld-T1 template immediately.

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

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason
> for each]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED:
> [apply template text; justify all candidates are anchored].

**T-1 ANNEX** (required immediately after -- summary aggregator):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met] --
>   per-scope record in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**TOPIC ENTITY MANIFEST**

List all entities in scope before synthesis. Entities appear in the Entity Coverage Matrix
with COVERED / CLEAN / SKIPPED status after execution.

| Entity # | Entity Name | Type (contract / state-machine / permission-boundary / lifecycle-phase) |
|----------|-------------|-------------------------------------------------------------------------|

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Classification | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Confidence | Conf Rationale | Remediation Verb | Target | Location | Conformance |
|------|-----------|---------------|------|--------------|---------|--------|-------------|--------------|-----------|----------------|-----------------|--------|----------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |

---

**ENTITY COVERAGE MATRIX**

| Entity # | Entity Name | Status | Sub-Skills that touched this entity | Notes |
|----------|-------------|--------|-------------------------------------|-------|

Status values: `COVERED` / `CLEAN` / `SKIPPED`

SKIPPED = execution gap. COVERED = at least one finding recorded. CLEAN = examined, no
findings elevated.

If all entities COVERED or CLEAN with zero SKIPPED: apply Entity Coverage Matrix all-clean
empty-state template immediately below the table.

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Applies to all HIGH-blast findings (Tier 1 and Tier 2).

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

These findings have Conf rationale in format "HIGH -- [named spec artifact]". No
clarification is needed.

| F-ID | Blast Tier | Conf Rationale (format: HIGH -- [spec artifact]) | Action |
|------|------------|--------------------------------------------------|--------|

If no qualifying findings: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

These findings have Conf rationale in format "LOW -- [interpretive question]". Implement
only after the question is answered YES.

| F-ID | Blast Tier | Conf Rationale (format: LOW -- [question]) | Action after confirmation |
|------|------------|---------------------------------------------|--------------------------|

If no qualifying findings: apply action-track-empty template.

---

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

For top three ranked findings: state blast radius rationale naming downstream flows,
components, or contracts affected.

---

**REMEDIATION QUALITY GATE**

One row per finding. Verb is constrained by Classification.

| F-ID | Classification | Verb | Target | Location | Conformance |
|------|---------------|------|--------|----------|-------------|

Verb vocabulary by type:
- GAP -> "add" or "remove"
- CONTRADICTION -> "resolve"
- ASSUMPTION -> "confirm"
Out-of-vocabulary Verb = C-31 fail.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply comparison-step empty-state template.

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Name compounding patterns or apply cross-skill-patterns
empty-state template citing Step 2 pairs and verdicts.

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

---

**PROPAGATION COVERAGE GATE**

| Rule ID (DR-NN) | Rule (abbreviated) | Coverage Status | Evidence |
|----------------|--------------------|----------------|----------|

Coverage Status values:
- `Covered by [F-ID]` -- finding's Dep rule cite = this DR-NN (three-point chain closed)
- `OPEN PROPAGATION GAP [DR-NN]` -- no finding covers this rule; state why

Every declared rule must appear in this table. Apply Coverage Gate no rules template or
Coverage Gate all-covered template as applicable.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this as the final section. Cite actual section names and evidence from this report.

**Sub-claim architecture rule**: Multi-part mechanism rows must declare sub-claim-level
statuses using `fired / partial / not-fired` per named sub-claim. Binary PASS or FAIL for
any multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total obs, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX -- withheld-T1 total, named example with scope + reason, per-scope source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates (base) | [list sections where templates fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (pattern or empty-state citing Step 2) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration (nine rows) | Structural Axis Declaration | Sub-claim 1: nine rows present (name all nine axis labels); Sub-claim 2: each row has three independently-verifiable sub-observables -- confirm for each row; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate section names] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural terms named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each by sub-skill name | fired / partial [name failing sub-claim] / not fired |
| DR-NN citation chain (C-32) | Cross-Skill Dependency Map + Propagation Coverage Gate + Findings Table | Sub-claim 1: every map rule has DR-NN at declaration -- cite count and range (DR-01 through DR-[N]); Sub-claim 2: every Coverage Gate row cites DR-NN in Rule ID (DR-NN) column matching the map -- cite row count and each DR-NN; Sub-claim 3: every finding with Dep rule cite populated has DR-NN matching both map row and Coverage Gate row -- cite each F-ID, DR-NN, and confirm three-point match | fired / partial [name failing sub-claim] / not fired |
| Confidence stratification (C-30) | CONFIDENCE-STRATIFIED ACTION LIST + Findings Table | Sub-claim 1: Track 1 present with label "Implement Now (HIGH-confidence / HIGH-blast)"; Sub-claim 2: Track 2 present with label "Confirm Spec First (LOW-confidence / HIGH-blast)"; Sub-claim 3: every HIGH-blast finding in exactly one track -- no finding in both or neither | fired / partial [name failing sub-claim] / not fired |
| Conf rationale typed format (C-35) | Findings Table | Sub-claim 1: every Tier 1 and Tier 2 finding has Conf rationale populated -- cite F-IDs; Sub-claim 2: every HIGH Conf rationale names a locatable spec artifact in format "HIGH -- [artifact name]" -- cite the artifact for each; Sub-claim 3: every LOW Conf rationale states a concrete YES/NO answerable question in format "LOW -- [question]" -- verify question answerability for each | fired / partial [name failing sub-claim] / not fired |
| Type-verb binding (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: all findings have Classification field populated -- cite count per type (GAP/CONTRADICTION/ASSUMPTION); Sub-claim 2: all Remediation verbs are in-vocabulary for their Classification -- cite each F-ID, Classification, Verb, and verdict (in-vocabulary / out-of-vocabulary); Sub-claim 3: Remediation Quality Gate table present with Verb/Target/Location/Conformance columns all populated | fired / partial [name failing sub-claim] / not fired |
| Full empty-state coverage (C-34) | CONFIDENCE-STRATIFIED ACTION LIST + Propagation Coverage Gate + T-1 ANNEX + Entity Coverage Matrix | Sub-claim 1: action tracks -- Track 1 and Track 2 each either contain findings or display action-track-empty template by name (not silent absence); cite which tracks fired template if applicable; Sub-claim 2: Coverage Gate -- section present with content rows, or Coverage Gate no-rules template, or Coverage Gate all-covered template; cite which applies; Sub-claim 3: T-1 ANNEX and Entity Coverage Matrix -- each present with content or named empty-state template; cite which template fired for each, if any; no section simply absent | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Cross-Skill Dependency Map >
Observational Discipline > Execution Sequence (five sub-skills in trace-first order: trace-
state, trace-contract, trace-permissions, flow-lifecycle, flow-conversation; each with
co-located per-scope gate table) > Topic Entity Manifest > Candidate Observations and
Filter Log > Filter Log Resolution (Template A or B + T-1 ANNEX) > Findings Table >
Execution Log > Entity Coverage Matrix > Ranked Findings (Tiers 1-2) > Confidence-
Stratified Action List (Track 1 and Track 2) > Ranked Findings (Tiers 3-4) > Remediation
Quality Gate > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Propagation Coverage Gate
> Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. DR-NN assigned at declaration; cited in Coverage Gate row; cited in finding's Dep rule
   cite field when applicable -- three-point chain verified in checklist (C-32)
2. Nine axis rows in Structural Axis Declaration, each extended from base five by quality
   axis: propagation/C-32, confidence/C-35, type-verb/C-31, full-empty-state/C-34 (C-33)
3. Four section types guarded by named empty-state templates: action tracks, Coverage Gate,
   T-1 ANNEX, Entity Coverage Matrix -- no silent absence (C-34)
4. Typed Conf rationale for all Tier 1 and Tier 2 findings: "HIGH -- [artifact]" or
   "LOW -- [question]" -- format verified in checklist sub-claims 2 and 3 (C-35)
5. Every HIGH-blast finding in exactly one of Track 1 or Track 2 (C-30)
6. Every finding has Classification (GAP/CONTRADICTION/ASSUMPTION); Remediation verb
   in-vocabulary for that type (C-31)
7. Per-scope Disposition column in all five sub-skill gate tables (C-25)
8. T-1 ANNEX as summary aggregator only (C-25)
9. Sub-claim decomposition in compliance checklist for all multi-part rows (C-24)
10. Trace sub-skills executed before flow sub-skills (V-05 role sequence)
