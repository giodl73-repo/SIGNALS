---
skill: campaign-simulate
round: 8
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v8-2026-03-16.md
---

# campaign-simulate -- Round 8 Variations

**Context**: R7 V-04 and V-05 tied at 96.5 under v7 rubric. V-05 was architecturally superior
in two ways not captured by v7: (1) enforcement rules used "structural violation" framing when
naming breach conditions (C-26 signal), and (2) the T-1 ANNEX carried a self-characterization
statement declaring its epistemic status as additive rather than authoritative (C-27 signal).
These patterns were codified as C-26 and C-27 in rubric v8.

**Under v8**: raw max 118, divisor 1.18. R7 V-05 under v8 scores approximately 114/118 = 96.6
because C-26 fires fully (structural violation framing exists in the checklist sub-claim rule
and T-1 ANNEX prohibition) and C-27 fires fully for the T-1 ANNEX block. However, C-26 partial
coverage exists -- not every axis enforcement rule names its failure mode as a structural
violation; only the checklist sub-claim rule and T-1 ANNEX rule do. C-27 covers the T-1 ANNEX
but not other aggregation blocks (EXECUTION LOG, CANDIDATE OBSERVATIONS AND FILTER LOG, RANKED
FINDINGS, CROSS-SKILL COMPARISON Step 3). Additionally, two persistent gaps remain from all
prior rounds: C-09 (Severity -- 2pts) and C-15 (Lifecycle Labels -- 2pts). Together these four
gaps explain the ceiling at 96.6. To reach 100/100 under v8 all four must close.

**Round 8 axes chosen:**
- Single-axis: V-01 (C-26 -- systematic structural violation framing for ALL enforcement rules,
  not just the checklist sub-claim rule), V-02 (C-27 -- self-characterization statements on ALL
  aggregation blocks, not just T-1 ANNEX), V-03 (C-09 + C-15 -- severity field and lifecycle
  label added to finding schema with declared scales)
- Combined: V-04 (C-26 + C-27 on R7 V-05 base), V-05 (full integration: C-26 + C-27 + C-09 +
  C-15 on R7 V-05 base -- all four remaining gaps closed)

---

## V-01 -- Systematic Structural Violation Framing for All Enforcement Rules (C-26)

**Variation axis:** Phrasing register -- every enforcement rule in the prompt that names a
compliance expectation must also name what a breach looks like as a "structural violation" (or
"axis breach"). The change is systematic and uniform: finding schema FAILURE annotations become
STRUCTURAL VIOLATION annotations; each structural axis row in the declaration table includes an
explicit failure-mode sentence; each enforcement statement in OBSERVATIONAL DISCIPLINE names the
structural violation that non-compliance constitutes. C-26 passes by construction because every
enforcement rule is testable: a reader can ask "did this structural violation occur?" and get a
binary answer.

**Hypothesis:** C-26 passes because all axis enforcement rules name their failure mode as a
structural violation. Every STRUCTURAL VIOLATION annotation in the finding schema, every
failure-mode sentence in the axis declaration rows, and every enforcement statement in
OBSERVATIONAL DISCIPLINE follows the same pattern: [condition that was not met] is a structural
violation of [named axis or rule]. C-27 is not directly targeted -- T-1 ANNEX
self-characterization from R7 V-05 is preserved, but other aggregation blocks (EXECUTION LOG,
RANKED FINDINGS, CROSS-SKILL COMPARISON Step 3) receive no new self-characterization. C-09 and
C-15 are not addressed. Risk: adding structural violation framing to every enforcement statement
may lengthen the axis declaration rows significantly; the model must not abbreviate the
Observable Output column to compensate.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes -- each row names three independently-verifiable observables AND the structural violation
that constitutes non-compliance. The last section verifies all five fired using sub-claim
decomposition for multi-part rows; binary verdicts for multi-part rows are a structural
violation. Both sections are written by the model into the output artifact -- not the prompt
text you are reading.

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
  justify that every candidate is anchored to a named spec location and scoped to at least
  one downstream component."
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
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output in this report. Reason: [why the mechanism did not fire].
  Impact on report validity: [whether the omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with structural violation conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 STRUCTURAL VIOLATION: vague reference without named location is a
                 structural violation of the finding schema; finding is not elevatable]
Summary:        [one sentence, problem only --
                 STRUCTURAL VIOLATION: merging Impact into Summary is a structural
                 violation of field separation; C-06 fails for this finding]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 STRUCTURAL VIOLATION: blank Impact or Impact merged with Summary is a
                 structural violation of field separation; C-06 fails for this finding]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 STRUCTURAL VIOLATION: wide-scope finding without BR rationale is a
                 structural violation of blast radius accountability]
Remediation:    [REQUIRED HERE: specific action at named target --
                 STRUCTURAL VIOLATION: "fix the spec" or remediation folded into Impact
                 is a structural violation of field separation; C-08 fails for this finding]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All five rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column plus an explicit
failure-mode statement for non-compliance.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated. STRUCTURAL VIOLATION: an Elevate? column absent from the filter log table or a Filter Log Resolution block absent from the report is an axis breach of the filtering axis. |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1. STRUCTURAL VIOLATION: a blank section with no empty-state template, or a section omitted without explanation, is a structural violation of the empty-state axis. |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict. STRUCTURAL VIOLATION: proceeding to Step 3 without Steps 1 and 2 present, or omitting any step entirely, is a structural violation of the cross-skill comparison axis. |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; (3) evidence column in checklist cites actual section names and counts, not template text. STRUCTURAL VIOLATION: a Structural Compliance Checklist absent from the report, or a Structural Axis Declaration that does not appear as the first section, is a structural violation of the declaration-compliance axis. |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason (or T-1 RECALIBRATION). STRUCTURAL VIOLATION: a per-scope gate table missing the Disposition column is a structural violation of the observational discipline axis regardless of section presence; a T-1 ANNEX that names a withheld-T1 observation absent from any per-scope Disposition column is a structural violation of the T-1 ANNEX summary role. |

The structural violation statements above are enforceable: an evaluator can ask "did this
structural violation occur?" for each named condition and produce a binary answer.

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
Disposition: withheld-T1 at the per-scope gate. STRUCTURAL VIOLATION: an observation
elevated to the Findings Table that fails either T-1 condition is a structural violation of
the T-1 threshold rule.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
An evaluator can verify every T-1 decision from the per-scope gate tables without reading
the T-1 ANNEX. STRUCTURAL VIOLATION: omitting the Disposition column from any per-scope
gate table is a structural violation of the observational discipline axis. If zero
withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION immediately below that
gate table.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope name.
STRUCTURAL VIOLATION: a T-1 ANNEX that names a withheld-T1 observation absent from any
per-scope Disposition column is a structural violation -- it would introduce evidence that
was never recorded at execution scope.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
declared schema. The Disposition column is structural -- do not omit it or rename it.

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

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table before advancing to the next sub-skill.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate observations with Disposition: elevated from all five per-scope gate tables.
Observations with Disposition: withheld-T1 or withheld-rule (pre-gate) do not appear here.

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
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met: no named
>   spec location / no concrete implementation consequence / other] -- per-scope record in
>   [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none -- all five scopes produced at least one
>   withheld-T1 row"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 (Disposition: elevated at per-scope gate) and all four
filter rules (Elevate?: yes in filter log).

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

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

If no compounding pairs: apply the cross-skill-patterns empty-state template. The template
requires citing every pair from Step 2 and their verdicts.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names and
evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or more
independently-verifiable observables declared in the declaration table), the Status column
must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. A partial overall verdict names the specific failing sub-claim inline. Binary
PASS or FAIL for a multi-part row is a structural violation of this checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding pattern or empty-state citing Step 2 pairs) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present with three observables each; Sub-claim 2: each row names a structural violation for non-compliance; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires with structural violation named; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- for each scope, cite sub-skill name and whether Disposition column is populated with at least one withheld-T1 row (or T-1 SCOPE RECALIBRATION invoked); T-1 ANNEX confirmed as summary aggregator citing per-scope source records; partial verdict names the sub-skill whose Disposition column is absent or the T-1 ANNEX that introduced evidence without per-scope counterpart | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (five sub-skills, each with co-located per-scope gate table using
Disposition schema) > Candidate Observations and Filter Log > Filter Log Resolution (Template
A or B, then T-1 ANNEX as summary aggregator) > Findings Table > Execution Log > Ranked
Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Per-scope Disposition column is present for all five sub-skills -- absent column is a
   structural violation of the observational discipline axis (C-25)
2. T-1 ANNEX summarizes per-scope Disposition data -- introducing new evidence is a
   structural violation of the T-1 ANNEX summary role (C-25)
3. Compliance checklist uses sub-claim decomposition for all multi-part rows -- binary
   verdict for a multi-part row is a structural violation of this checklist (C-24)
4. A partial compliance verdict names the specific failing sub-claim inline (C-24)
5. Five structural axis rows with equal depth appear before any execution evidence (C-22)
6. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
7. Every enforcement rule names its failure mode as a structural violation (C-26)

---

## V-02 -- Self-Characterization on All Aggregation Blocks (C-27)

**Variation axis:** Output format -- every section that aggregates evidence from per-scope
or per-step execution records must carry a self-characterization statement declaring its
epistemic status: authoritative (primary record; per-scope records derive from this) or
additive (supplements per-scope records; per-scope records are authoritative). The five
aggregation blocks receiving self-characterization: (1) T-1 ANNEX (already has it from R7
V-05), (2) CANDIDATE OBSERVATIONS AND FILTER LOG, (3) EXECUTION LOG, (4) RANKED FINDINGS,
(5) CROSS-SKILL COMPARISON Step 3. Each block opens with a standardized self-characterization
sentence using the pattern: "This [block name] [aggregates/reorders/summarizes] [what it
aggregates] from [source sections]. It is [authoritative/additive] -- [implication for
reader]."

**Hypothesis:** C-27 passes because every aggregation block in the report carries a
self-characterization statement that explicitly labels it as authoritative or additive.
A reader who encounters any aggregation block can immediately determine whether to treat it
as the primary record or look upstream for the authoritative source. C-26 is not directly
targeted -- structural violation framing exists in the checklist sub-claim rule and T-1
ANNEX prohibition from R7 V-05 but is not systematically extended to every enforcement rule.
C-09 and C-15 are not addressed. Risk: self-characterization sentences on sections like
RANKED FINDINGS (which reorders rather than aggregates) may appear redundant; the model
must not omit them on grounds of perceived redundancy.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes with equal structural depth. Each axis names three independently-verifiable observables.
The last section verifies all five fired using sub-claim decomposition; binary verdicts for
multi-part rows are a structural violation. Every aggregation block in this report carries a
self-characterization statement declaring whether it is authoritative or additive with respect
to the per-scope evidence it covers. Both sections are written by the model into the output
artifact -- not the prompt text you are reading.

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
  justify that every candidate is anchored to a named spec location and scoped to at least
  one downstream component."
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
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
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
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All five rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural, its absence fails this axis; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing the per-scope record by scope name (or T-1 RECALIBRATION) |

The per-scope gate table schema in row 5 is structural. Omitting or reformulating the
Disposition column fails the observational discipline axis regardless of section presence.

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

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
An evaluator can verify every T-1 decision from the per-scope gate tables without reading
the T-1 ANNEX. If zero withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION
immediately below that gate table.

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope name.
A T-1 ANNEX that names a withheld-T1 observation absent from any per-scope Disposition
column is a structural violation.

**Aggregation block self-characterization rule**: Every section in this report that
aggregates, reorders, or summarizes evidence from per-scope or per-step execution records
must open with a self-characterization statement of the form: "Self-characterization: This
[block name] [aggregates/reorders/summarizes] [what] from [source]. It is [authoritative /
additive] -- [implication]." The aggregation blocks that require this statement are:
CANDIDATE OBSERVATIONS AND FILTER LOG, T-1 ANNEX, EXECUTION LOG, RANKED FINDINGS, and
CROSS-SKILL COMPARISON Step 3. A block that is additive declares that the per-scope records
are authoritative and the aggregation is for navigation convenience. A block that is
authoritative declares that the per-scope records derive from or depend on it.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
declared schema. The Disposition column is structural -- do not omit it or rename it.

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

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table before advancing to the next sub-skill.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Self-characterization: This log aggregates observations with Disposition: elevated from all
five per-scope gate tables. It is additive -- the authoritative T-1 decisions reside in the
per-scope Disposition columns co-located with each sub-skill's execution results. This log
does not introduce new observations; it collects elevated observations for filter-rule
evaluation. Observations with Disposition: withheld-T1 do not appear here.

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

**T-1 ANNEX** (required immediately after Template A or B):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> Self-characterization: This ANNEX aggregates Disposition: withheld-T1 records from per-scope
> gate tables in the Execution Sequence. It is additive -- the authoritative withheld-T1 record
> is in each sub-skill's per-scope Disposition column. This ANNEX does not substitute for
> per-scope records; a withheld-T1 observation named here must appear in the corresponding
> per-scope Disposition column.
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met: no named
>   spec location / no concrete implementation consequence / other] -- per-scope record in
>   [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none -- all five scopes produced at least one
>   withheld-T1 row"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 (Disposition: elevated at per-scope gate) and all four
filter rules (Elevate?: yes in filter log).

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

Self-characterization: This log aggregates execution status and finding counts from all five
sub-skill sections. It is additive -- the authoritative execution evidence for each sub-skill
resides in that sub-skill's section (including per-scope gate table and any findings). This
log is a navigation summary; a discrepancy between this log and a sub-skill section should
be resolved by reading the sub-skill section.

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Self-characterization: This section reorders elevated findings from the Findings Table by
blast radius. It is additive -- the authoritative finding record is in the Findings Table;
the ranked presentation here is for prioritization convenience. All finding fields are
inherited from the Findings Table and must not be modified in this section.

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

Self-characterization: This declaration aggregates compounding verdicts from Step 2. It is
additive -- the authoritative verdict record is in the Step 2 table; this declaration names
patterns that emerge from Step 2 verdicts and does not modify or supersede them.

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

If no compounding pairs: apply the cross-skill-patterns empty-state template. The template
requires citing every pair from Step 2 and their verdicts.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names and
evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or more
independently-verifiable observables declared in the declaration table), the Status column
must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. A partial overall verdict names the specific failing sub-claim inline. Binary
PASS or FAIL for a multi-part row is a structural violation of this checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX self-characterization statement present declaring additive status | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present with self-characterization statement | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present; Sub-claim 2: each row has three independently-verifiable observables in the Observable Output column; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- for each scope, cite sub-skill name and whether Disposition column is populated with at least one withheld-T1 row (or T-1 SCOPE RECALIBRATION invoked); T-1 ANNEX confirmed as summary aggregator with self-characterization statement; partial verdict names the sub-skill whose Disposition column is absent or the T-1 ANNEX that introduced evidence without per-scope counterpart | fired / partial [name failing sub-claim] / not fired |
| Aggregation block self-characterization | CANDIDATE OBSERVATIONS AND FILTER LOG, EXECUTION LOG, T-1 ANNEX, RANKED FINDINGS, CROSS-SKILL COMPARISON Step 3 | Sub-claim 1: CANDIDATE OBSERVATIONS self-characterization present (additive, per-scope source named); Sub-claim 2: EXECUTION LOG self-characterization present (additive, sub-skill sections authoritative); Sub-claim 3: RANKED FINDINGS and Step 3 self-characterization statements present (additive, Findings Table authoritative) | fired / partial [name the block missing self-characterization] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (five sub-skills, each with co-located per-scope gate table using
Disposition schema) > Candidate Observations and Filter Log (with self-characterization) >
Filter Log Resolution (Template A or B, then T-1 ANNEX with self-characterization) >
Findings Table > Execution Log (with self-characterization) > Ranked Findings (with
self-characterization) > Cross-Skill Comparison Protocol (Steps 1, 2, Step 3 with
self-characterization) > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Per-scope Disposition column is present for all five sub-skills (C-25)
2. T-1 ANNEX summarizes per-scope Disposition data; it does not introduce new evidence (C-25)
3. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
4. A partial compliance verdict names the specific failing sub-claim inline (C-24)
5. Five structural axis rows with equal depth appear before any execution evidence (C-22)
6. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
7. Every aggregation block carries a self-characterization statement (C-27)

---

## V-03 -- Severity Field and Lifecycle Label in Finding Schema (C-09 + C-15)

**Variation axis:** Output format -- two new fields are added to the finding schema: Severity
([critical / high / medium / low] with a declared scale) and Lifecycle ([new / confirmed /
amended / closed] with a declared schema). These fields have been persistent fails across all
prior rounds. Adding them does not touch C-26 or C-27 architecture. The severity scale and
lifecycle schema are declared in the OBSERVATIONAL DISCIPLINE section before any sub-skill
fires, making them structural commitments rather than optional annotations.

**Hypothesis:** C-09 and C-15 both pass by construction. Severity is a standalone required
field in every finding with a declared four-point scale; a finding without a severity label
is incomplete under the finding schema. Lifecycle is a standalone required field with a
declared four-state schema; round-over-round tracking is enabled by construction. C-26 and
C-27 are not directly targeted -- R7 V-05 architecture is otherwise preserved. Risk: adding
two new required fields increases finding schema complexity. The model must populate both
fields without merging them into adjacent fields (Impact or Summary).

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes with equal structural depth. Each axis names three independently-verifiable observables.
The last section verifies all five fired using sub-claim decomposition; binary verdicts for
multi-part rows are a structural violation. Both sections are written by the model into the
output artifact -- not the prompt text you are reading.

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
  justify that every candidate is anchored to a named spec location and scoped to at least
  one downstream component."
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
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
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
Severity:       [critical / high / medium / low] -- REQUIRED STANDALONE FIELD
                 See severity scale declared in OBSERVATIONAL DISCIPLINE.
                 FAILURE: blank Severity or Severity merged with Impact fails C-09.
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 FAILURE: wide-scope finding without rationale fails C-10]
Lifecycle:      [new / confirmed / amended / closed] -- REQUIRED STANDALONE FIELD
                 See lifecycle schema declared in OBSERVATIONAL DISCIPLINE.
                 FAILURE: blank Lifecycle or Lifecycle merged with any other field fails C-15.
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All five rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms) including severity scale and lifecycle schema; T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural, its absence fails this axis; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason (or T-1 RECALIBRATION) |

The per-scope gate table schema in row 5 is structural. Omitting or reformulating the
Disposition column fails the observational discipline axis regardless of section presence.

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

**Severity scale** (declared before any sub-skill fires; required for all elevated findings):
- critical -- blocks implementation; unresolved finding invalidates the spec for this area
- high -- causes incorrect behavior in common paths; high probability of defect if shipped
- medium -- causes incorrect behavior in edge cases or under specific conditions
- low -- cosmetic, documentation, or preference; does not cause behavioral defects

Every finding must carry a Severity field populated from this scale. Severity is independent
of Blast Radius -- a system-wide finding may be low severity if the impact is informational;
an isolated finding may be critical if it blocks implementation of a core invariant.

**Lifecycle schema** (declared before any sub-skill fires; required for all elevated findings):
- new -- finding appears for the first time in this simulation round
- confirmed -- finding appeared in a prior round and is independently verified here
- amended -- finding appeared in a prior round and its scope, impact, or remediation has
  changed based on new evidence
- closed -- finding was present in a prior round and is now resolved (remediation applied)

Every finding must carry a Lifecycle field populated from this schema. For a first-run
simulation (no prior round), all findings carry Lifecycle: new.

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
summary, not a primary evidence source. It must cite per-scope source records by scope name.
A T-1 ANNEX that names a withheld-T1 observation absent from any per-scope Disposition
column is a structural violation.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
declared schema. The Disposition column is structural -- do not omit it or rename it.

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

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table before advancing to the next sub-skill.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate observations with Disposition: elevated from all five per-scope gate tables.
Observations with Disposition: withheld-T1 do not appear here.

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
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met: no named
>   spec location / no concrete implementation consequence / other] -- per-scope record in
>   [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none -- all five scopes produced at least one
>   withheld-T1 row"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 (Disposition: elevated at per-scope gate) and all four
filter rules (Elevate?: yes in filter log).

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Severity | Blast Radius | Lifecycle | Remediation |
|------|-----------|------|--------------|---------|--------|----------|-------------|-----------|-------------|

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
[findings with severity and lifecycle labeled, downstream rationale, or: ranked-tier
empty-state template]

**Tier 2 -- Cross-Skill**
[findings with severity and lifecycle labeled, shared root cause rationale, or: empty-state]

**Tier 3 -- Component-Wide**
[findings with severity and lifecycle labeled, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings with severity and lifecycle labeled, or: apply ranked-tier empty-state template]

For top three ranked findings: state blast radius rationale and severity rationale (why this
severity level was assigned, not just the label).

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

If no compounding pairs: apply the cross-skill-patterns empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names and
evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or more
independently-verifiable observables declared in the declaration table), the Status column
must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. A partial overall verdict names the specific failing sub-claim inline. Binary
PASS or FAIL for a multi-part row is a structural violation of this checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding pattern or empty-state citing Step 2 pairs) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present with three observables each; Sub-claim 2: equal Observable Output depth confirmed; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary including severity scale and lifecycle schema -- cite two structural labels; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each scope and whether at least one withheld-T1 row appeared (or T-1 SCOPE RECALIBRATION invoked); T-1 ANNEX confirmed as summary aggregator citing per-scope source records | fired / partial [name failing sub-claim] / not fired |
| Severity and Lifecycle fields | Findings Table | Sub-claim 1: Severity field populated for all findings with values from declared scale (critical/high/medium/low); Sub-claim 2: Lifecycle field populated for all findings with values from declared schema (new/confirmed/amended/closed); Sub-claim 3: both fields are standalone -- not merged with Impact or Summary | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline
(including severity scale and lifecycle schema) > Execution Sequence > Candidate
Observations and Filter Log > Filter Log Resolution (Template A or B, then T-1 ANNEX) >
Findings Table (with Severity and Lifecycle columns) > Execution Log > Ranked Findings
(with severity and lifecycle on each finding) > Cross-Skill Comparison Protocol > Structural
Compliance Checklist.

Structural commitments that must hold in every report:
1. Per-scope Disposition column is present for all five sub-skills (C-25)
2. T-1 ANNEX summarizes per-scope Disposition data; it does not introduce new evidence (C-25)
3. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
4. A partial compliance verdict names the specific failing sub-claim inline (C-24)
5. Five structural axis rows with equal depth appear before any execution evidence (C-22)
6. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
7. Every finding carries a Severity field from the declared four-point scale (C-09)
8. Every finding carries a Lifecycle field from the declared four-state schema (C-15)

---

## V-04 -- Combined: C-26 + C-27 on R7 V-05 Base

**Variation axes combined:**
1. Systematic structural violation framing for all enforcement rules (V-01 axis) -- C-26:
   every axis row in the declaration table names its failure mode as a structural violation;
   finding schema uses STRUCTURAL VIOLATION annotations; every enforcement statement in
   OBSERVATIONAL DISCIPLINE names the structural violation that non-compliance constitutes
2. Self-characterization on all aggregation blocks (V-02 axis) -- C-27: CANDIDATE
   OBSERVATIONS AND FILTER LOG, T-1 ANNEX, EXECUTION LOG, RANKED FINDINGS, and CROSS-SKILL
   COMPARISON Step 3 each carry a self-characterization statement declaring authoritative or
   additive status; the compliance checklist adds a row verifying all five blocks
3. All prior R7 V-05 mechanisms: filtering, empty-state, cross-skill comparison,
   declaration-compliance (C-17/C-18), co-equal axis row depth (C-22), T-1 rejection
   obligation (C-23), sub-claim architecture in compliance checklist (C-24), per-scope
   Disposition column as primary T-1 evidence (C-25)

**Hypothesis:** C-26 and C-27 both pass by construction. C-26: every enforcement rule in
the prompt names its failure mode as a structural violation -- in the axis declaration rows,
in the finding schema annotations, and in OBSERVATIONAL DISCIPLINE enforcement statements.
C-27: every aggregation block in the report carries a self-characterization statement that
explicitly labels it as additive (per-scope records are authoritative) or authoritative.
All C-01--C-25 mechanisms are unchanged. Risk: structural violation framing combined with
self-characterization statements on all aggregation blocks increases total prompt length.
The structural axis declaration rows are the most likely place for abbreviation under
pressure -- the row-level structural violation sentences must be preserved verbatim.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes -- each row names three independently-verifiable observables AND the structural violation
that constitutes non-compliance. The last section verifies all five fired using sub-claim
decomposition; binary verdicts for multi-part rows are a structural violation. Every
aggregation block in this report carries a self-characterization statement declaring whether
it is authoritative or additive with respect to the per-scope evidence it covers. Both
sections are written by the model into the output artifact -- not the prompt text you are
reading.

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
  justify that every candidate is anchored to a named spec location and scoped to at least
  one downstream component."
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
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output in this report. Reason: [why the mechanism did not fire].
  Impact on report validity: [whether the omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with structural violation conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 STRUCTURAL VIOLATION: vague reference without named location is a
                 structural violation of the finding schema; finding is not elevatable]
Summary:        [one sentence, problem only --
                 STRUCTURAL VIOLATION: merging Impact into Summary is a structural
                 violation of field separation; C-06 fails for this finding]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 STRUCTURAL VIOLATION: blank Impact or Impact merged with Summary is a
                 structural violation of field separation; C-06 fails for this finding]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 STRUCTURAL VIOLATION: wide-scope finding without BR rationale is a
                 structural violation of blast radius accountability]
Remediation:    [REQUIRED HERE: specific action at named target --
                 STRUCTURAL VIOLATION: "fix the spec" or remediation folded into Impact
                 is a structural violation of field separation; C-08 fails for this finding]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All five rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column plus an explicit
structural violation for non-compliance.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated, with self-characterization (additive); (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated. STRUCTURAL VIOLATION: an absent Elevate? column or absent Filter Log Resolution block is an axis breach of the filtering axis. |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1. STRUCTURAL VIOLATION: a blank section with no empty-state template is a structural violation of the empty-state axis. |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration with self-characterization (additive, Step 2 authoritative), compounding patterns or empty-state. STRUCTURAL VIOLATION: Step 3 absent or Steps 1+2 bypassed is a structural violation of the cross-skill comparison axis. |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables + structural violation each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition; (3) evidence column cites actual section names and counts, not template text. STRUCTURAL VIOLATION: Structural Compliance Checklist absent from the report is a structural violation of the declaration-compliance axis. |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator with self-characterization) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if with structural violation named; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason, Filter rule -- Disposition column is structural; (3) T-1 ANNEX with self-characterization (additive, per-scope records authoritative): names at least one withheld-T1 observation by scope and reason (or T-1 RECALIBRATION). STRUCTURAL VIOLATION: per-scope gate table missing Disposition column is a structural violation of observational discipline axis; T-1 ANNEX introducing evidence absent from per-scope records is a structural violation. |

The structural violation statements above are enforceable: an evaluator can ask "did this
structural violation occur?" for each named condition and produce a binary answer.

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
Disposition: withheld-T1 at the per-scope gate. STRUCTURAL VIOLATION: an observation
elevated to the Findings Table that fails either T-1 condition is a structural violation of
the T-1 threshold rule.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
An evaluator can verify every T-1 decision from the per-scope gate tables without reading
the T-1 ANNEX. STRUCTURAL VIOLATION: omitting the Disposition column from any per-scope
gate table is a structural violation of the observational discipline axis. If zero
withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION immediately below that
gate table.

**Aggregation block self-characterization rule**: Every section that aggregates, reorders,
or summarizes evidence from per-scope or per-step execution records must carry a
self-characterization statement declaring its epistemic status. A block that is additive
declares that per-scope records are authoritative and the aggregation is for navigation
convenience. The blocks requiring self-characterization in this report: CANDIDATE
OBSERVATIONS AND FILTER LOG (additive), T-1 ANNEX (additive), EXECUTION LOG (additive),
RANKED FINDINGS (additive), CROSS-SKILL COMPARISON Step 3 (additive).

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope name.
STRUCTURAL VIOLATION: a T-1 ANNEX that names a withheld-T1 observation absent from any
per-scope Disposition column is a structural violation -- it would introduce evidence that
was never recorded at execution scope.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
declared schema. The Disposition column is structural -- do not omit it or rename it.

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

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table before advancing to the next sub-skill.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Self-characterization: This log aggregates observations with Disposition: elevated from all
five per-scope gate tables. It is additive -- the authoritative T-1 decisions reside in the
per-scope Disposition columns co-located with each sub-skill's execution results. This log
does not introduce new observations.

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

**T-1 ANNEX** (required immediately after Template A or B):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> Self-characterization: This ANNEX aggregates Disposition: withheld-T1 records from
> per-scope gate tables in the Execution Sequence. It is additive -- the authoritative
> withheld-T1 record is in each sub-skill's per-scope Disposition column. A withheld-T1
> observation named here must appear in the corresponding per-scope Disposition column;
> introducing evidence absent from any per-scope record is a structural violation.
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met: no named
>   spec location / no concrete implementation consequence / other] -- per-scope record in
>   [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 (Disposition: elevated) and all four filter rules.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

Self-characterization: This log aggregates execution status and finding counts from all five
sub-skill sections. It is additive -- the authoritative execution evidence resides in each
sub-skill's section. This log is a navigation summary; discrepancies resolve to sub-skill
section.

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Self-characterization: This section reorders elevated findings from the Findings Table by
blast radius. It is additive -- the authoritative finding record is in the Findings Table.
Finding fields must not be modified in this section.

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

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply comparison-step empty-state template.

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

Self-characterization: This declaration aggregates compounding verdicts from Step 2. It is
additive -- the authoritative verdict record is in the Step 2 table; this declaration names
patterns that emerge from Step 2 verdicts and does not modify them.

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

If no compounding pairs: apply the cross-skill-patterns empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names and
evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or more
independently-verifiable observables declared in the declaration table), the Status column
must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. A partial overall verdict names the specific failing sub-claim inline. Binary
PASS or FAIL for a multi-part row is a structural violation of this checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total, named example with scope + reason, per-scope source cited (or RECALIBRATION); Sub-claim 3: T-1 ANNEX self-characterization present (additive, no new evidence) | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present with self-characterization | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present, each with three observables and a structural violation statement; Sub-claim 2: structural violation framing covers all five axes; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels; Sub-claim 2: T-1 rule stated as if-and-only-if with structural violation named; Sub-claim 3: per-scope Disposition columns present for all five sub-skills (cite each; T-1 SCOPE RECALIBRATION invoked if zero withheld-T1); T-1 ANNEX confirmed as additive summary aggregator with self-characterization; partial verdict names the absent Disposition column or structural violation | fired / partial [name failing sub-claim] / not fired |
| Aggregation block self-characterization | CANDIDATE OBSERVATIONS, EXECUTION LOG, T-1 ANNEX, RANKED FINDINGS, CROSS-SKILL COMPARISON Step 3 | Sub-claim 1: CANDIDATE OBSERVATIONS and EXECUTION LOG self-characterization present (additive); Sub-claim 2: RANKED FINDINGS self-characterization present (additive, Findings Table authoritative); Sub-claim 3: Step 3 self-characterization present (additive, Step 2 authoritative) and T-1 ANNEX self-characterization present (additive, per-scope records authoritative) | fired / partial [name the block missing self-characterization] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution Sequence (per-scope gate tables with Disposition schema) > Candidate Observations
and Filter Log (with self-characterization) > Filter Log Resolution (Template A or B, then
T-1 ANNEX with self-characterization) > Findings Table > Execution Log (with
self-characterization) > Ranked Findings (with self-characterization) > Cross-Skill
Comparison Protocol (Step 3 with self-characterization) > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Per-scope Disposition column is present for all five sub-skills -- absence is a
   structural violation of the observational discipline axis (C-25)
2. T-1 ANNEX summarizes per-scope Disposition data and does not introduce new evidence --
   new evidence in T-1 ANNEX is a structural violation (C-25)
3. Compliance checklist uses sub-claim decomposition for all multi-part rows -- binary
   verdict for a multi-part row is a structural violation (C-24)
4. A partial compliance verdict names the specific failing sub-claim inline (C-24)
5. Five structural axis rows with structural violation framing appear before execution (C-22)
6. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
7. Every enforcement rule names its failure mode as a structural violation (C-26)
8. Every aggregation block carries a self-characterization statement (C-27)

---

## V-05 -- Full Integration: C-26 + C-27 + C-09 + C-15

**Variation axes combined:**
1. Systematic structural violation framing (C-26): every axis enforcement rule names its
   failure mode as a structural violation -- axis declaration rows, finding schema annotations,
   OBSERVATIONAL DISCIPLINE enforcement statements
2. Self-characterization on all aggregation blocks (C-27): CANDIDATE OBSERVATIONS AND FILTER
   LOG, T-1 ANNEX, EXECUTION LOG, RANKED FINDINGS, CROSS-SKILL COMPARISON Step 3 each carry
   a self-characterization statement; compliance checklist adds a verification row
3. Severity field (C-09): added to finding schema as required standalone field; four-point
   scale (critical/high/medium/low) declared in OBSERVATIONAL DISCIPLINE before any sub-skill
   fires; severity rationale required for top three ranked findings
4. Lifecycle label (C-15): added to finding schema as required standalone field; four-state
   schema (new/confirmed/amended/closed) declared in OBSERVATIONAL DISCIPLINE before any
   sub-skill fires; enables multi-round campaign tracking
5. All prior R7 V-05 mechanisms: filtering, empty-state, cross-skill comparison,
   declaration-compliance (C-17/C-18), co-equal axis row depth (C-22), T-1 rejection
   obligation (C-23), sub-claim architecture (C-24), per-scope Disposition column (C-25)

**Hypothesis:** All six new/persistent gap criteria pass by construction: C-26 (structural
violation framing systematic), C-27 (self-characterization on all five aggregation blocks),
C-09 (severity field with declared scale), C-15 (lifecycle field with declared schema). All
C-01--C-25 mechanisms are unchanged. Risk: this is the most structurally demanding variation.
Severity and lifecycle fields in the finding schema increase per-finding output. Structural
violation sentences in every axis declaration row increase declaration table length. Self-
characterization sentences on five aggregation blocks add line count. The compliance checklist
adds two new rows. The model must not abbreviate any field under structural pressure; the
STRUCTURAL VIOLATION annotations in the finding schema are the enforcement mechanism.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes -- each row names three independently-verifiable observables AND the structural violation
that constitutes non-compliance. The last section verifies all five fired using sub-claim
decomposition; binary verdicts for multi-part rows are a structural violation. Every
aggregation block carries a self-characterization statement. Every finding carries Severity
and Lifecycle fields from declared scales. Both structural declaration and compliance
verification are written by the model into the output artifact -- not the prompt text you
are reading.

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
  justify that every candidate is anchored to a named spec location and scoped to at least
  one downstream component."
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
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs
  compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output in this report. Reason: [why the mechanism did not fire].
  Impact on report validity: [whether the omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with structural violation conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 STRUCTURAL VIOLATION: vague reference without named location is a
                 structural violation of the finding schema; finding is not elevatable]
Summary:        [one sentence, problem only --
                 STRUCTURAL VIOLATION: merging Impact into Summary is a structural
                 violation of field separation; C-06 fails for this finding]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 STRUCTURAL VIOLATION: blank Impact or Impact merged with Summary is a
                 structural violation of field separation; C-06 fails for this finding]
Severity:       [critical / high / medium / low] -- REQUIRED STANDALONE FIELD
                 Scale declared in OBSERVATIONAL DISCIPLINE. Severity is independent of
                 Blast Radius -- a system-wide finding may be low; an isolated finding
                 may be critical.
                 STRUCTURAL VIOLATION: blank Severity or Severity merged with Impact is
                 a structural violation of the finding schema; C-09 fails for this finding]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 STRUCTURAL VIOLATION: wide-scope finding without BR rationale is a
                 structural violation of blast radius accountability]
Lifecycle:      [new / confirmed / amended / closed] -- REQUIRED STANDALONE FIELD
                 Schema declared in OBSERVATIONAL DISCIPLINE. For first-run simulations
                 all findings carry Lifecycle: new.
                 STRUCTURAL VIOLATION: blank Lifecycle or Lifecycle merged with any other
                 field is a structural violation of the finding schema; C-15 fails for
                 this finding]
Remediation:    [REQUIRED HERE: specific action at named target --
                 STRUCTURAL VIOLATION: "fix the spec" or remediation folded into Impact
                 is a structural violation of field separation; C-08 fails for this finding]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently from its named sub-observables, and (c) identify the exact schema
of each gate table before reading any execution. All five rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column plus an explicit
structural violation for non-compliance.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated, with self-characterization (additive); (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated. STRUCTURAL VIOLATION: an absent Elevate? column or absent Filter Log Resolution block is an axis breach of the filtering axis. |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1. STRUCTURAL VIOLATION: a blank section with no empty-state template is a structural violation of the empty-state axis. |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration with self-characterization (additive, Step 2 authoritative). STRUCTURAL VIOLATION: Step 3 absent or Steps 1+2 bypassed is a structural violation of the cross-skill comparison axis. |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, three observables + structural violation each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition; binary verdict for multi-part row is a structural violation; (3) evidence column cites actual section names and counts. STRUCTURAL VIOLATION: Structural Compliance Checklist absent from the report is a structural violation of the declaration-compliance axis. |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary including severity scale and lifecycle schema) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator with self-characterization, not new evidence) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms), severity scale, and lifecycle schema declared; T-1 rule stated as if-and-only-if with structural violation named; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason, Filter rule -- Disposition column is structural; (3) T-1 ANNEX with self-characterization (additive): names at least one withheld-T1 observation by scope and reason (or T-1 RECALIBRATION). STRUCTURAL VIOLATION: per-scope gate table missing Disposition column is a structural violation of observational discipline axis; T-1 ANNEX naming evidence absent from per-scope records is a structural violation; finding with blank Severity or Lifecycle is a structural violation of the finding schema. |

The structural violation statements above are enforceable: an evaluator can ask "did this
structural violation occur?" for each named condition and produce a binary answer.

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

**Severity scale** (declared before any sub-skill fires; required standalone field in every
elevated finding):
- critical -- blocks implementation; unresolved finding invalidates the spec for this area
- high -- causes incorrect behavior in common paths; high probability of defect if shipped
- medium -- causes incorrect behavior in edge cases or under specific conditions
- low -- cosmetic, documentation, or preference; does not cause behavioral defects
Severity is independent of Blast Radius. STRUCTURAL VIOLATION: a finding with blank Severity
or Severity merged into another field is a structural violation of the finding schema.

**Lifecycle schema** (declared before any sub-skill fires; required standalone field in every
elevated finding):
- new -- finding appears for the first time in this simulation round
- confirmed -- finding appeared in a prior round and is independently verified here
- amended -- finding appeared in a prior round and its scope, impact, or remediation changed
- closed -- finding was present in a prior round and is now resolved
For first-run simulations (no prior round): all findings carry Lifecycle: new. STRUCTURAL
VIOLATION: a finding with blank Lifecycle or Lifecycle merged into another field is a
structural violation of the finding schema.

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1 at the per-scope gate. STRUCTURAL VIOLATION: an observation
elevated to the Findings Table that fails either T-1 condition is a structural violation of
the T-1 threshold rule.

**Per-scope Disposition rule (structural commitment)**: Each per-scope gate table includes
a Disposition column as the primary record of T-1 application at that scope. The column is
populated at execution time, co-located with the sub-skill that produced the observation.
An evaluator can verify every T-1 decision from the per-scope gate tables without reading
the T-1 ANNEX. STRUCTURAL VIOLATION: omitting the Disposition column from any per-scope
gate table is a structural violation of the observational discipline axis. If zero
withheld-T1 rows appear for a scope: apply T-1 SCOPE RECALIBRATION immediately below that
gate table.

**Aggregation block self-characterization rule**: Every section that aggregates, reorders,
or summarizes evidence from per-scope or per-step execution records must carry a
self-characterization statement declaring its epistemic status. The blocks requiring
self-characterization: CANDIDATE OBSERVATIONS AND FILTER LOG (additive -- per-scope
Disposition columns authoritative), T-1 ANNEX (additive -- per-scope Disposition records
authoritative), EXECUTION LOG (additive -- sub-skill sections authoritative), RANKED
FINDINGS (additive -- Findings Table authoritative), CROSS-SKILL COMPARISON Step 3
(additive -- Step 2 table authoritative).

**T-1 ANNEX role (summary aggregator only)**: The T-1 ANNEX in Filter Log Resolution
aggregates Disposition: withheld-T1 records from all five per-scope gate tables. It is a
summary, not a primary evidence source. It must cite per-scope source records by scope name.
STRUCTURAL VIOLATION: a T-1 ANNEX that names a withheld-T1 observation absent from any
per-scope Disposition column is a structural violation -- it would introduce evidence that
was never recorded at execution scope.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
declared schema. The Disposition column is structural -- do not omit it or rename it.

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

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table before advancing to the next sub-skill.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Self-characterization: This log aggregates observations with Disposition: elevated from all
five per-scope gate tables. It is additive -- the authoritative T-1 decisions reside in the
per-scope Disposition columns co-located with each sub-skill's execution results. This log
does not introduce new observations; it collects elevated observations for filter-rule
evaluation.

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

**T-1 ANNEX** (required immediately after Template A or B):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> Self-characterization: This ANNEX aggregates Disposition: withheld-T1 records from per-scope
> gate tables in the Execution Sequence. It is additive -- the authoritative withheld-T1
> record is in each sub-skill's per-scope Disposition column. This ANNEX does not substitute
> for per-scope records. STRUCTURAL VIOLATION: a withheld-T1 observation named in this ANNEX
> that is absent from any per-scope Disposition column is a structural violation.
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met: no named
>   spec location / no concrete implementation consequence / other] -- per-scope record in
>   [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none -- all five scopes produced at least one
>   withheld-T1 row"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 (Disposition: elevated) and all four filter rules.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Severity | Blast Radius | Lifecycle | Remediation |
|------|-----------|------|--------------|---------|--------|----------|-------------|-----------|-------------|

---

**EXECUTION LOG**

Self-characterization: This log aggregates execution status and finding counts from all five
sub-skill sections. It is additive -- the authoritative execution evidence resides in each
sub-skill's section. Discrepancies between this log and a sub-skill section resolve to the
sub-skill section.

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Self-characterization: This section reorders elevated findings from the Findings Table by
blast radius. It is additive -- the authoritative finding record including Severity and
Lifecycle fields is in the Findings Table. Finding fields must not be modified here.

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with Severity and Lifecycle labeled, downstream rationale, or: empty-state]

**Tier 2 -- Cross-Skill**
[findings with Severity and Lifecycle labeled, shared root cause rationale, or: empty-state]

**Tier 3 -- Component-Wide**
[findings with Severity and Lifecycle labeled, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings with Severity and Lifecycle labeled, or: apply ranked-tier empty-state template]

For top three ranked findings: state blast radius rationale AND severity rationale (why this
severity level was assigned relative to the declared scale, not just the label).

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

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

Self-characterization: This declaration aggregates compounding verdicts from Step 2. It is
additive -- the authoritative verdict record is in the Step 2 table; this declaration names
patterns that emerge from Step 2 verdicts and does not modify them.

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

If no compounding pairs: apply the cross-skill-patterns empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names and
evidence from the report you just produced.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or more
independently-verifiable observables declared in the declaration table), the Status column
must declare sub-claim-level statuses using `fired / partial / not-fired` per named
sub-claim. A partial overall verdict names the specific failing sub-claim inline. Binary
PASS or FAIL for a multi-part row is a structural violation of this checklist.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total, named example with scope + reason, per-scope source cited (or RECALIBRATION); Sub-claim 3: T-1 ANNEX self-characterization present (additive, structural violation for new evidence named) | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration with self-characterization present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present, each with three observables and a structural violation statement; Sub-claim 2: structural violation framing covers all five axes (cite one example per axis); Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary including severity scale and lifecycle schema -- cite two labels; Sub-claim 2: T-1 rule stated as if-and-only-if with structural violation named; Sub-claim 3: per-scope Disposition columns present for all five sub-skills (cite each; T-1 SCOPE RECALIBRATION invoked if zero withheld-T1); T-1 ANNEX confirmed as additive summary with self-characterization and structural violation named; partial verdict names absent Disposition column or structural violation | fired / partial [name failing sub-claim] / not fired |
| Severity and Lifecycle fields | Findings Table | Sub-claim 1: Severity field populated for all findings from declared scale (critical/high/medium/low); Sub-claim 2: Lifecycle field populated for all findings from declared schema (new/confirmed/amended/closed); Sub-claim 3: both fields are standalone -- not merged with any other field; structural violation would occur if either field were merged | fired / partial [name failing sub-claim] / not fired |
| Aggregation block self-characterization | CANDIDATE OBSERVATIONS, EXECUTION LOG, T-1 ANNEX, RANKED FINDINGS, CROSS-SKILL COMPARISON Step 3 | Sub-claim 1: CANDIDATE OBSERVATIONS and EXECUTION LOG self-characterization present (additive, per-scope source named); Sub-claim 2: RANKED FINDINGS self-characterization present (additive, Findings Table authoritative, fields not modified); Sub-claim 3: Step 3 and T-1 ANNEX self-characterization present with structural violation named for ANNEX | fired / partial [name the block missing self-characterization] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline
(severity scale + lifecycle schema + aggregation self-characterization rule declared) >
Execution Sequence (per-scope gate tables with Disposition schema) > Candidate Observations
and Filter Log (with self-characterization) > Filter Log Resolution (Template A or B, then
T-1 ANNEX with self-characterization and structural violation named) > Findings Table (with
Severity and Lifecycle columns) > Execution Log (with self-characterization) > Ranked
Findings (with self-characterization, Severity + Lifecycle on each finding, severity
rationale on top three) > Cross-Skill Comparison Protocol (Step 3 with self-characterization)
> Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Per-scope Disposition column is present for all five sub-skills -- absence is a
   structural violation of the observational discipline axis (C-25)
2. T-1 ANNEX summarizes per-scope Disposition data and does not introduce new evidence --
   new evidence in T-1 ANNEX is a structural violation (C-25)
3. Compliance checklist uses sub-claim decomposition for all multi-part rows -- binary
   verdict for a multi-part row is a structural violation (C-24)
4. A partial compliance verdict names the specific failing sub-claim inline (C-24)
5. Five structural axis rows with structural violation framing appear before execution (C-22)
6. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
7. Every enforcement rule names its failure mode as a structural violation (C-26)
8. Every aggregation block carries a self-characterization statement (C-27)
9. Every finding carries a Severity field from the declared four-point scale (C-09)
10. Every finding carries a Lifecycle field from the declared four-state schema (C-15)
