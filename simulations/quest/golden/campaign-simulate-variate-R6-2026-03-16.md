---
skill: campaign-simulate
round: 6
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v6-2026-03-16.md
---

# campaign-simulate -- Round 6 Variations

**Context**: R5 V-04 and V-05 both scored 100/100 under v5 rubric. V-05 was architecturally superior
because it declared observational discipline as the fifth structural axis (row 5 in the axis table)
and added partial-compliance verdicability with three independently-verifiable sub-claims. These
excellence patterns were codified as C-22 (co-equal axis declaration — row 5 must be structurally
co-equal with rows 1-4, not just co-located) and C-23 (T-1 rejection evidence must appear in the
filter log as a named withheld observation, not merely as a rule declaration) in rubric v6.

**Under v6**: raw max 110, divisor 1.10. R5 V-05 without C-22/C-23 = 106/110 = 96.4 normalized.
To reach 100: must pass both C-22 and C-23.

**Round 6 axes chosen:**
- Single-axis: V-01 (C-22 — co-equal axis row depth), V-02 (C-23 — T-1 rejection obligation),
  V-03 (C-23 alternative — per-scope T-1 evaluation log)
- Combined: V-04 (C-22 + C-23 on R5 V-05 base), V-05 (full integration: co-equal axis + T-1
  rejection obligation + partial compliance verdicability hardened)

---

## V-01 -- Co-Equal Axis Row Depth (C-22)

**Variation axis:** Output format — the fifth structural axis row in the STRUCTURAL AXIS DECLARATION
table is upgraded to the same column depth as rows 1-4. The "Observable Output in This Report"
column for row 5 names three distinct, independently-checkable observables — one per sub-mechanism
of the observational discipline axis. An evaluator can verify C-22 from the declaration table alone
without reading any execution sections.

**Hypothesis:** C-22 passes by construction. The axis table has five rows of equal depth: every row
names the axis, the criteria it implements, the mechanism, and three or more distinct named
observables. Row 5 is not a soft row ("observational discipline section") but a structurally
co-equal row with the same Observable Output specificity as rows 1-4. C-23 is not directly targeted
here — the T-1 rule is declared but no explicit rejection obligation is added to the filter log.
Risk: Without a T-1 rejection obligation, C-23 may fail if the model produces a zero-T-1-rejection
filter log.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five axes
and their mechanisms. The last section verifies all five fired with evidence citations. Both sections
are written by the model into the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any
section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated.
  Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment --
  only that the schema ran. Required: revisit candidate list. Either (a) name at least one
  observation that should be rejected under the filter rules, or (b) provide explicit justification
  that every candidate is genuinely anchored to a named spec location and scoped to at least one
  downstream component."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise
  comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in
  Step 2: [list pairs and verdicts from the Step 2 table]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation of why this
  area produced no observable candidates]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did
  not produce observable output in this report. Reason: [why the mechanism did not fire]. Impact
  on report validity: [whether the omission affects any findings]."

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

Write this section as the first section of your output report. This section is part of your output
artifact -- not the prompt text. An evaluator reading only this section must be able to verify
each axis by checking its named observables without reading any execution section. Complete this
before writing any execution results.

Each row must name the axis, the criteria it implements, the mechanism, and the specific observable
output produced in this report. All five rows must have equal structural depth in the Observable
Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution block declaring Template A (normal: at least one rejection) or Template B (vacuous: zero rejections, recalibration required) | (1) Candidate Observations and Filter Log table with Elevate? and Rejection Reason columns; (2) Filter Log Resolution block naming the template letter and rejection count |
| Empty-state axis | C-11 | Per-section empty-state templates defined for all section types; silent empty sections are not permitted | Any structured section with no results: named template text appears in place of blank; sections: sub-skill sections, ranked tiers, comparison steps, execution log entries |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: candidate pairings (Step 1 table), pairwise verdicts (Step 2 table), pattern declaration (Step 3 -- requires Steps 1+2 to be present) | (1) Step 1 table with F-ID pairs and surface similarity; (2) Step 2 table with pairwise verdicts; (3) Step 3 declaration naming compounding patterns or citing Step 2 pairs and verdicts |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration section (before findings) + Structural Compliance Checklist section (after findings) with evidence citations | (1) Structural Axis Declaration (this section, five rows, equal depth); (2) Structural Compliance Checklist (final section, evidence column cites actual section names and counts) |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration naming the structural vocabulary used; T-1 threshold rule stated as if-and-only-if elevation criterion before any sub-skill fires; five per-scope gate tables embedded co-located with each sub-skill's execution evidence (not centralized) | (1) OBSERVATIONAL DISCIPLINE section (before execution): genre named, structural labels listed, T-1 stated; (2) five per-scope gate tables (one per sub-skill section): each names observations evaluated, T-1 outcome per observation; (3) compliance checklist row 5: three sub-claims checkable independently |

Mechanisms declared in this table that do not produce observable output receive "not fired" in the
compliance checklist. Do not declare mechanisms you do not use.

---

**OBSERVATIONAL DISCIPLINE**

Write this section immediately after the Structural Axis Declaration and before the Execution
Sequence. This section is part of the output artifact.

**Genre declaration**: This report is a pre-implementation simulation findings document. Structural
vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior worth evaluating for elevation
- "Elevated" -- observation passed T-1 and all four filter rules; appears in Findings Table
- "Withheld" -- observation failed T-1 or a named filter rule; appears only in Filter Log
- "T-1" -- the if-and-only-if elevation criterion defined below

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated to a finding
if and only if it names a specific spec location AND describes a gap or violation that would cause
incorrect implementation behavior. T-1 is satisfied by anchoring the observation to a named spec
section and identifying a concrete implementation consequence. T-1 is not satisfied by a vague
concern, a style preference, or an observation without a spec reference.

T-1 unfalsified warning: A report in which zero observations are withheld under T-1 has not
demonstrated filtering judgment at the elevation threshold. If no observation fails T-1, either
(a) name an observation that was considered and withheld because it lacked a spec reference, or
(b) explicitly state why this topic produced no observations below T-1 and what that says about
spec quality.

**Per-scope gates**: Five per-scope gate tables follow -- one per sub-skill, embedded within each
sub-skill's execution section. Each gate table lists the observations considered for that scope and
the T-1 outcome per observation. Per-scope gates are not centralized; each fires co-located with
its execution evidence.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write the per-scope gate table before advancing to the
next sub-skill.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

After each sub-skill: write the per-scope gate table for that sub-skill before advancing.

**Per-scope gate table format** (write one after each sub-skill):

| Obs # | What was noticed | T-1 Outcome | If withheld: reason |
|-------|-----------------|------------|---------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

After completing all five per-scope gate tables, aggregate the elevated observations into the
global filter log.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

Note: Observations already withheld at the per-scope T-1 gate do not appear in the global filter
log. The global filter log operates only on T-1-passing candidates.

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state. This block is required in every report.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief reason for
> each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: A gate
> that rejects nothing provides no evidence of filtering judgment -- it demonstrates only that the
> schema ran. Required: revisit candidate list. Either (a) name at least one observation that
> should be rejected under the filter rules, or (b) provide explicit justification that every
> candidate is genuinely anchored to a named spec location and scoped to at least one downstream
> component.

Template A applies when at least one filter log row is "no." Template B applies when all rows are
"yes." Template B is not a failure; silence about zero rejections is.

---

**FINDINGS TABLE**

Only observations that passed T-1 and all four filter rules. If none: apply the findings-table
empty-state template.

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

For top three ranked findings: state blast radius rationale (name downstream flows, components, or
contracts affected and explain why scope reaches that far).

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2 to be present.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills that share
surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply the comparison-step empty-state template.

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

For each compounding finding: "Promoted from [tier] to [tier] because [cross-skill root cause means
that X expands downstream scope from Y to Z]."

If no compounding pairs: apply the cross-skill-patterns empty-state template. The template requires
citing every pair from Step 2 and their verdicts -- a bare declaration without citing Step 2 pairs
fails C-15.

Steps 1 and 2 are required even when Step 3 concludes no patterns.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in the
STRUCTURAL AXIS DECLARATION, confirm whether it fired. Cite the actual report section by name and
provide evidence (actual counts, template names, pair counts). Do not write "fired" without a
section name and evidence drawn from the report you just produced.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "6 observations across 5 sub-skills; 2 rejected at Rule 1; 1 rejected at Rule 3"] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template A: cite letter and rejection count; Template B: cite the justification provided] | fired / not fired |
| Empty-state templates | [list each section where a template fired] | [for each: cite the template type and first clause] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [e.g., "3 candidate pairs in Step 1; 3 pairwise verdicts in Step 2"] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [e.g., "Five axes declared with equal column depth: filtering, empty-state, cross-skill comparison, declaration-compliance, observational discipline"] | fired / not fired |
| Observational discipline axis | [list: OBSERVATIONAL DISCIPLINE section + per-scope gate section names] | Sub-claim 1: genre named, structural labels listed; Sub-claim 2: T-1 rule stated with if-and-only-if condition; Sub-claim 3: five per-scope gate tables present, each co-located with its sub-skill section | fired / partial / not fired |

If a mechanism is marked "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline > Candidate
Observations and Filter Log (with embedded per-scope gate tables) > Filter Log Resolution >
Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2,
3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section. Structural Compliance Checklist is the last
section. Five axes -- filtering, empty-state, cross-skill comparison, declaration-compliance,
observational discipline -- must each produce observable output in the sections named in the
declaration table.

---

## V-02 -- T-1 Rejection Obligation in Filter Log (C-23)

**Variation axis:** Output format -- the filter log gains an explicit T-1 rejection obligation.
After the global filter log is complete, the Filter Log Resolution block includes a T-1 ANNEX:
the model must name at least one observation that was evaluated and withheld under T-1 (not under
filter rules 1-4), or invoke T-1 RECALIBRATION (analogous to Template B for zero general
rejections). The compliance checklist row for the observational discipline axis verifies that a
named T-1 rejection appears in the report.

**Hypothesis:** C-23 passes by construction. The T-1 ANNEX forces the model to either cite a
named T-1 rejection ("Observation [X] from [sub-skill] withheld because T-1 not satisfied: no spec
location named") or explicitly invoke T-1 RECALIBRATION ("Zero T-1 rejections. T-1 RECALIBRATION
REQUIRED: [reason why this topic produced no sub-T-1 observations]"). A report cannot close the
T-1 ANNEX with silence. C-22 is not directly targeted here -- the fifth axis row exists but
retains R5 V-05 depth rather than the equal-depth upgrade from V-01.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five axes.
The last section verifies all five fired. Both sections are written by the model into the output
artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any
section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated.
  Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment --
  only that the schema ran. Required: revisit candidate list. Either (a) name at least one
  observation that should be rejected under the filter rules, or (b) provide explicit justification
  that every candidate is genuinely anchored to a named spec location and scoped to at least one
  downstream component."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections)**: "T-1 ANNEX: Zero observations withheld
  under T-1 in this report. T-1 RECALIBRATION REQUIRED: A T-1 rule with no rejection citations is
  unfalsified. Either (a) identify an observation that was considered and withheld because it lacked
  a spec reference or a concrete implementation consequence, or (b) explicitly state why this topic
  produced no sub-T-1 observations and what that implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise
  comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in
  Step 2: [list pairs and verdicts from the Step 2 table]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation of why this
  area produced no observable candidates]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did
  not produce observable output in this report. Reason: [why the mechanism did not fire]. Impact
  on report validity: [whether the omission affects any findings]."

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

Write this section as the first section of your output report. Complete this before writing any
execution results.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution block (Template A or Template B) | Candidate Observations and Filter Log table; Filter Log Resolution block |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types | All structured sections with no results: template text appears in place of blank |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: Step 1 (pairings), Step 2 (verdicts), Step 3 (patterns) | Cross-Skill Comparison Protocol: Step 1 table, Step 2 table, Step 3 declaration |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (before findings) + Structural Compliance Checklist (after findings) with evidence citations | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 threshold rule (stated before execution) + T-1 ANNEX in Filter Log Resolution (at least one named T-1 rejection or T-1 RECALIBRATION invoked) + five per-scope gates co-located with execution evidence | OBSERVATIONAL DISCIPLINE section; per-scope gate tables (one per sub-skill); T-1 ANNEX block in Filter Log Resolution; compliance checklist row 5 |

---

**OBSERVATIONAL DISCIPLINE**

Write this section immediately after the Structural Axis Declaration and before the Execution
Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document. Structural
vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior worth evaluating
- "Elevated" -- observation passed T-1 and all four filter rules
- "Withheld under T-1" -- observation failed the elevation threshold (no spec location or no
  concrete implementation consequence); appears in T-1 ANNEX, not in filter log
- "Rejected" -- observation passed T-1 but failed a filter rule; appears in filter log with
  rejection reason

**T-1 threshold rule**: An observation is elevated if and only if it names a specific spec location
AND describes a gap or violation that would cause incorrect implementation behavior. Observations
failing either condition are withheld under T-1.

**T-1 ANNEX obligation**: After completing the global filter log, the Filter Log Resolution block
includes a T-1 ANNEX. The T-1 ANNEX must contain at least one named T-1 rejection:

> T-1 ANNEX: [N] observations considered and withheld under T-1 during execution. Withheld:
> - [Obs X, sub-skill]: withheld because [T-1 condition not met: no spec location / no concrete
>   implementation consequence]. This observation does not appear in the filter log.

If zero observations were withheld under T-1, apply the T-1 ANNEX RECALIBRATION template.

**Per-scope gates**: Five per-scope gate tables follow, one embedded per sub-skill section. Each
gate records observations considered for that scope and their T-1 outcome before they enter
(or are excluded from) the global filter log.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write the per-scope gate table before advancing.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (write one per sub-skill, co-located with execution results):

| Obs # | What was noticed | T-1: passed / withheld | If withheld: reason |
|-------|-----------------|----------------------|---------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate T-1-passing observations from all five per-scope gate tables.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state. This block is required in every report.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief reason]).
> Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: [see
> template above].

**T-1 ANNEX** (required in every report, immediately after Template A or B):

Name every observation withheld under T-1 during execution. These observations were considered but
did not reach the filter log because they failed the elevation threshold.

> T-1 ANNEX: [content per format above, or: apply T-1 ANNEX RECALIBRATION template]

---

**FINDINGS TABLE**

Only observations that passed T-1 and all four filter rules.

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

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

If no compounding pairs: apply the cross-skill-patterns empty-state template (must cite Step 2
pairs and verdicts).

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. Cite actual section names and
evidence from the report you just produced.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [counts and rule numbers] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template letter + rejection count or recalibration invoked] | fired / not fired |
| Empty-state templates | [list sections where templates fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [pair count and verdict summary] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [count of axes declared] | fired / not fired |
| Observational discipline axis (T-1 ANNEX) | T-1 ANNEX in Filter Log Resolution | [name the T-1 rejection cited: "Obs [X] from [sub-skill] withheld because [reason]", or: "T-1 RECALIBRATION invoked because [reason]"] | fired / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline > Execution
(with per-scope gate tables) > Candidate Observations and Filter Log > Filter Log Resolution (with
T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol
(Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section. Structural Compliance Checklist is the last
section. The T-1 ANNEX is required in every report; it may not be omitted even when all
observations pass T-1.

---

## V-03 -- Per-Scope T-1 Evaluation Log as C-23 Evidence (C-23 Alternative)

**Variation axis:** Output format -- instead of requiring a T-1 rejection in a centralized
T-1 ANNEX block, V-03 makes T-1 evaluation evidence per-scope and co-located with execution. Each
sub-skill's execution section produces a T-1 EVALUATION ROW in its per-scope gate table: explicitly
marking each observation as "elevated" (T-1 satisfied), "withheld-T1" (T-1 not satisfied), or
"withheld-rule" (T-1 satisfied but filter rule applied). A T-1 EVALUATION SUMMARY section fires
after all five scopes, aggregating T-1 outcomes. C-23 passes because the per-scope gate tables and
T-1 EVALUATION SUMMARY together constitute named, scope-attributed T-1 rejection evidence.

**Hypothesis:** C-23 passes by construction -- per-scope gate tables name each observation's T-1
outcome explicitly, and at least one "withheld-T1" row constitutes the named withheld observation
C-23 requires. If zero "withheld-T1" rows appear across all five scopes, the T-1 EVALUATION
SUMMARY invokes T-1 RECALIBRATION per scope, not as a global gate. This tests whether per-scope
T-1 evidence produces better C-23 coverage than the centralized T-1 ANNEX in V-02. Risk: the
distributed evidence may be harder to audit than a centralized annex; the compliance checklist must
cite five sections rather than one.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five axes.
The last section verifies all five fired. Both sections are written by the model into the output
artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated.
  Zero rejected. RECALIBRATION REQUIRED: revisit candidate list; see template text above."
- **T-1 withheld row zero (per scope)**: "T-1 evaluation for [sub-skill]: [N] observations
  considered. Zero withheld under T-1. T-1 SCOPE RECALIBRATION: Either name an observation that
  was considered and failed T-1 for this scope, or confirm this scope is unusually clean and state
  why no observation failed the elevation threshold."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise
  comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in
  Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but did not fire. Reason: [why]. Impact:
  [whether omission affects findings]."

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
Remediation:    [REQUIRED: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A or B) | Candidate Observations and Filter Log table; Filter Log Resolution block |
| Empty-state axis | C-11 | Per-section empty-state templates | All structured sections with no results: named template text |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol (Steps 1, 2, 3) | Cross-Skill Comparison Protocol sections |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section) + Structural Compliance Checklist (last section) | Structural Axis Declaration; Structural Compliance Checklist |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (OBSERVATIONAL DISCIPLINE section) + T-1 rule stated before execution + per-scope T-1 gate tables with explicit withheld-T1 / elevated labeling + T-1 EVALUATION SUMMARY | OBSERVATIONAL DISCIPLINE section; per-scope T-1 gate columns in each sub-skill section (5 tables); T-1 EVALUATION SUMMARY |

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
- "elevated" -- observation passed T-1 AND all four filter rules; appears in Findings Table
- "withheld-T1" -- observation failed T-1 (no spec location or no concrete consequence); noted
  in per-scope gate table; does not enter global filter log
- "withheld-rule" -- observation passed T-1 but failed a filter rule (1-4); noted in filter log
  with rejection reason

**T-1 threshold rule**: An observation is elevated if and only if it names a specific spec location
AND describes a gap or violation causing incorrect implementation behavior.

**Per-scope T-1 evaluation**: Each sub-skill execution produces a per-scope gate table with a
Disposition column. Every observation is labeled: elevated, withheld-T1, or withheld-rule. At
least one withheld-T1 row per scope is expected; if zero appear, the scope triggers T-1 SCOPE
RECALIBRATION. After all five scopes, a T-1 EVALUATION SUMMARY aggregates outcomes.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, written co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: elevated | withheld-T1 | withheld-rule

If zero withheld-T1 rows: apply T-1 SCOPE RECALIBRATION template for this sub-skill.

---

**T-1 EVALUATION SUMMARY**

Write after completing all five per-scope gate tables and before the global filter log.

| Sub-Skill | Observations considered | Withheld-T1 | Elevated to filter log | withheld-T1 example (name first one) |
|-----------|------------------------|------------|----------------------|--------------------------------------|
| flow-lifecycle | | | | |
| flow-conversation | | | | |
| trace-state | | | | |
| trace-contract | | | | |
| trace-permissions | | | | |

If any scope has zero withheld-T1: note which scopes and whether T-1 SCOPE RECALIBRATION was
invoked.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate elevated (T-1 passing) observations from all per-scope gate tables.

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
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason]).

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

---

**FINDINGS TABLE**

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

**Tier 1 -- System-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings, or: apply ranked-tier empty-state template]

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

**Step 3 -- Patterns declaration**: [compounding patterns, or empty-state template citing Step 2
verdicts]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section of your output report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section name] | [counts and rule numbers] | fired / not fired |
| Filter Log Resolution | [section name] | [Template letter + count] | fired / not fired |
| Empty-state templates | [sections] | [template type and first clause] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [pair count + verdict summary] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [axis count] | fired / not fired |
| Observational discipline axis (per-scope T-1) | [list all five per-scope gate section names] + T-1 EVALUATION SUMMARY | Sub-claim 1: genre declared (vocabulary listed); Sub-claim 2: T-1 rule stated before execution; Sub-claim 3: per-scope gate tables present for all five sub-skills; at least one withheld-T1 row cited (or RECALIBRATION invoked per scope) | fired / partial / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline > Execution
(with per-scope gate tables) > T-1 EVALUATION SUMMARY > Candidate Observations and Filter Log >
Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison
Protocol > Structural Compliance Checklist.

---

## V-04 -- Combined: C-22 + C-23 on R5 V-05 Base

**Variation axes combined:**
1. Co-equal axis row depth (V-01 axis) -- C-22: axis row 5 has equal column depth to rows 1-4;
   three independently-verifiable sub-observables named in the Observable Output column
2. T-1 rejection obligation (V-02 axis) -- C-23: Filter Log Resolution includes a required T-1
   ANNEX; named T-1 rejection or T-1 RECALIBRATION invoked; compliance checklist row cites the
   named T-1 rejection
3. All prior R5 V-05 mechanisms: filtering, empty-state, cross-skill comparison,
   declaration-compliance, observational discipline (C-19/C-20/C-21)

**Hypothesis:** C-22 and C-23 both pass by construction. C-22: the fifth axis row is structurally
co-equal with rows 1-4 -- the Observable Output column names three distinct sub-observables, each
checkable independently from the other four rows' observables. C-23: the T-1 ANNEX is a required
block in Filter Log Resolution; it names at least one T-1 withheld observation or invokes T-1
RECALIBRATION; a report cannot close Filter Log Resolution without completing the T-1 ANNEX. All
prior C-01--C-21 mechanisms are unchanged. Risk: this is the longest variation; two new structural
obligations (row depth + T-1 ANNEX) add overhead. If the model abbreviates either, the compliance
checklist row surfaces the partial state rather than silently degrading.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five axes
with equal structural depth. The last section verifies all five fired with evidence citations. Both
sections are written by the model into the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated.
  Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment --
  only that the schema ran. Required: revisit candidate list. Either (a) name at least one
  observation that should be rejected under the filter rules, or (b) justify that every candidate
  is genuinely anchored to a named spec location and scoped to at least one downstream component."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections)**: "T-1 ANNEX: Zero observations withheld
  under T-1 in this report. T-1 RECALIBRATION REQUIRED: A T-1 rule with no rejection citations is
  unfalsified. Either (a) identify an observation that was considered and withheld because it lacked
  a spec reference or concrete consequence, or (b) state why this topic produced no sub-T-1
  observations and what that implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise
  comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in
  Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did
  not produce observable output. Reason: [why]. Impact on report validity: [whether omission
  affects findings]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 FAILURE: vague reference fails this field]
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

Write this section as the first section of your output report. An evaluator reading only this
section must be able to (a) predict which structural sections appear in the report and (b) verify
each axis independently by checking its named sub-observables. All five rows must have equal
depth in the Observable Output column: each must name at least two distinct, independently-
checkable observables. Complete this before writing any execution results.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution block (Template A: normal / Template B: vacuous, recalibration required) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited |
| Empty-state axis | C-11 | Per-section empty-state templates defined for all section types; silent empty sections not permitted | (1) Any structured section with no results: named template text in place of blank; (2) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: candidate pairings (Step 1), pairwise verdicts (Step 2), pattern declaration (Step 3 -- requires Steps 1+2) | (1) Step 1 table: F-ID pairs and surface similarity; (2) Step 2 table: pairwise verdicts; (3) Step 3 declaration: compounding patterns named or Step 2 pairs and verdicts cited |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (before findings, five rows equal depth) + Structural Compliance Checklist (after findings, evidence column cites section names and counts) | (1) Structural Axis Declaration: this section, five rows, equal Observable Output depth; (2) Structural Compliance Checklist: final section, evidence column not left as template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 threshold rule stated before execution + T-1 ANNEX (named T-1 rejection or T-1 RECALIBRATION) + five per-scope gate tables co-located with execution evidence | (1) OBSERVATIONAL DISCIPLINE section: genre named with structural label glossary, T-1 rule stated as if-and-only-if; (2) five per-scope gate tables: one per sub-skill, co-located, each with T-1 outcome column; (3) T-1 ANNEX in Filter Log Resolution: names withheld observation or invokes T-1 RECALIBRATION |

Mechanisms declared above that do not produce observable output receive "not fired" in the
compliance checklist. Do not declare mechanisms you do not use.

---

**OBSERVATIONAL DISCIPLINE**

Write this section immediately after the Structural Axis Declaration and before the Execution
Sequence. This section is part of the output artifact.

**Genre declaration**: This report is a pre-implementation simulation findings document. Structural
vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior considered for elevation
- "Elevated" -- observation passed T-1 AND all four filter rules; appears in Findings Table
- "Withheld under T-1" -- observation failed T-1 (no spec location or no concrete consequence);
  noted in T-1 ANNEX; does not enter filter log
- "Rejected" -- observation passed T-1 but failed a filter rule (1-4); appears in filter log
  with rejection reason
- "T-1" -- the elevation threshold defined below

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if and only
if it names a specific spec location AND describes a gap or violation that would cause incorrect
implementation behavior. T-1 is not satisfied by a vague concern, a style preference, or an
observation without a named spec section.

**T-1 ANNEX obligation**: The Filter Log Resolution block includes a mandatory T-1 ANNEX. The T-1
ANNEX must name at least one observation withheld under T-1 ("Obs [X] from [sub-skill]: withheld
because [T-1 condition not met]") or invoke T-1 RECALIBRATION (apply the T-1 ANNEX RECALIBRATION
template). The T-1 ANNEX closes the falsifiability gap: a T-1 rule with no rejection citations is
a rule that has not been tested.

**Per-scope gates**: Five per-scope gate tables follow, one per sub-skill, embedded co-located with
execution evidence. Each records observations considered for that scope and their T-1 outcome.
Per-scope gates are not centralized -- each fires within its sub-skill section.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, write the per-scope gate table before advancing.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (write one per sub-skill, co-located with execution results):

| Obs # | What was noticed | T-1: passed / withheld | If withheld: which T-1 condition failed |
|-------|-----------------|----------------------|----------------------------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate T-1-passing observations from all five per-scope gate tables.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

Observations already withheld at the T-1 per-scope gate do not appear here.

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason]).
> Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after Template A or B):

> T-1 ANNEX: [N] observations considered and withheld under T-1 during execution.
> Withheld:
> - [Sub-skill, Obs #]: withheld because [T-1 condition not met: no named spec location /
>   no concrete implementation consequence / other]. This observation does not appear in the
>   filter log.
> [Repeat for each withheld-T1 observation, or apply T-1 ANNEX RECALIBRATION template if zero.]

---

**FINDINGS TABLE**

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

For top three ranked findings: state blast radius rationale (name downstream flows, components, or
contracts affected).

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

If compounding pairs:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

If no compounding pairs: apply the cross-skill-patterns empty-state template (must cite Step 2
pairs and verdicts -- a bare declaration fails C-15).

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Cite actual section names and evidence from this report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "7 observations across 5 sub-skills; 2 rejected at Rule 1: no spec location; 1 rejected at Rule 3: style preference"] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template letter + rejection count, or Template B + recalibration justification] | fired / not fired |
| Empty-state templates | [list each section where a template fired] | [for each: template type and first clause of text used] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [pair count in Step 1; verdict summary from Step 2] | fired / not fired |
| Structural Axis Declaration (five rows, equal depth) | Structural Axis Declaration | [e.g., "Five axes declared; each row names 2+ independently-checkable observables: filtering (2), empty-state (2), cross-skill (3), declaration-compliance (2), observational discipline (3)"] | fired / not fired |
| Observational discipline axis | [OBSERVATIONAL DISCIPLINE section + per-scope gate section names + T-1 ANNEX] | Sub-claim 1: genre named, structural label glossary present; Sub-claim 2: T-1 rule stated as if-and-only-if before execution; Sub-claim 3: T-1 ANNEX present in Filter Log Resolution -- name the cited T-1 rejection or confirm T-1 RECALIBRATION invoked | fired / partial / not fired |

A mechanism marked "not fired" is a structural compliance failure. Apply the not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline > Execution
(with per-scope gate tables embedded) > Candidate Observations and Filter Log > Filter Log
Resolution (with T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings > Cross-Skill
Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section (five rows, equal Observable Output depth).
Structural Compliance Checklist is the last section. T-1 ANNEX is required in every report;
it may not be omitted even when all observations pass T-1.

---

## V-05 -- Full Integration: Co-Equal Axis + T-1 Rejection Obligation + Hardened Partial Compliance

**Variation axes combined:**
1. Co-equal axis row depth (V-01) -- C-22
2. T-1 rejection obligation (V-02) -- C-23
3. Hardened partial-compliance verdicability: compliance checklist row 6 uses `fired / partial /
   not fired` with three independently-verifiable sub-claims; partial verdict names which sub-claim
   failed, making the weakest observational discipline mechanism immediately actionable
4. All prior R5 V-05 mechanisms: filtering, empty-state, cross-skill comparison,
   declaration-compliance, observational discipline

**Hypothesis:** C-22 and C-23 both pass by construction. C-22: five axis rows of equal depth,
Observable Output column names 3+ distinct sub-observables per row, verifiable from the declaration
table alone. C-23: T-1 ANNEX is a mandatory block; naming a withheld T-1 observation or invoking
T-1 RECALIBRATION is required; compliance checklist row 6 sub-claim 2 independently verifies the
named T-1 rejection. The partial-compliance verdict converts a binary "fired / not fired" into a
diagnostic instrument: if C-22 fails (rows not co-equal), sub-claim 1 names it; if C-23 fails
(T-1 ANNEX missing or T-1 rejection not named), sub-claim 2 names it; if per-scope gates
centralized, sub-claim 3 names it. This is the architecturally strongest variation.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five axes
with equal column depth. The last section verifies all five fired with evidence citations and
partial-compliance sub-claims. Both sections are written by the model into the output artifact --
not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated.
  Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment --
  only that the schema ran. Required: revisit candidate list. Either (a) name at least one
  observation that should be rejected under the filter rules, or (b) provide explicit justification
  that every candidate is genuinely anchored to a named spec location and scoped to at least one
  downstream component."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections)**: "T-1 ANNEX: Zero observations withheld
  under T-1 in this report. T-1 RECALIBRATION REQUIRED: A T-1 rule with no rejection citations
  is unfalsified. Either (a) identify an observation that was considered and withheld because it
  lacked a spec reference or concrete implementation consequence, or (b) state why this topic
  produced no sub-T-1 observations and what that implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise
  comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in
  Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did
  not produce observable output. Reason: [why]. Impact on report validity: [whether omission
  affects findings]."
- **Compliance checklist partial (observational discipline)**: "Observational discipline axis:
  PARTIAL. [State which sub-claim failed: (1) genre not declared / structural labels missing;
  (2) T-1 ANNEX absent or T-1 rejection not named; (3) per-scope gates centralized rather than
  co-located]. Remaining sub-claims: [list which fired with evidence]."

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

Write this section as the first section of your output report. This section is part of your output
artifact -- not the prompt text. Rules for this section:

1. All five rows must be present.
2. The Observable Output column for each row must name at least two distinct, independently-
   checkable observables (e.g., section name + content requirement, not just section name).
3. An evaluator reading only this section must be able to verify axis compliance from the named
   observables without reading execution sections.

Complete this before writing any execution results.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules (Rules 1-4); Filter Log Resolution block declaring Template A (normal: at least one rejection) or Template B (vacuous: zero rejections, recalibration required) | (1) Candidate Observations and Filter Log table: populated with Elevate? and Rejection Reason columns; (2) Filter Log Resolution block: names Template letter and rejection count drawn from actual filter log |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; no section may be blank without its template | (1) Any structured section with no results: named template text appears in place of blank; (2) every template application cites the section name and first clause of the template used |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: candidate pairings (Step 1 table required), pairwise verdicts (Step 2 table required), pattern declaration (Step 3 requires Steps 1 and 2 present) | (1) Step 1 table: all F-ID pairs from different sub-skills with surface similarity stated; (2) Step 2 table: verdict and reason for each pair; (3) Step 3: compounding patterns with P-ID and elevation rationale, or empty-state template citing Step 2 verdicts |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows, equal Observable Output depth) + Structural Compliance Checklist (final section, evidence column cites actual section names and counts, partial verdict supported for observational discipline row) | (1) Structural Axis Declaration: this section, five rows, each with 2+ distinct named observables; (2) Structural Compliance Checklist: every row names actual section + actual evidence; row 6 uses fired / partial / not fired |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration naming structural vocabulary + T-1 threshold rule stated as if-and-only-if before execution + T-1 ANNEX (named T-1 rejection or T-1 RECALIBRATION) + five per-scope gate tables embedded co-located with sub-skill execution (not centralized) | (1) OBSERVATIONAL DISCIPLINE section: genre named, structural label glossary (elevated / withheld-T1 / rejected), T-1 rule stated as if-and-only-if condition; (2) five per-scope gate tables, each co-located in its sub-skill section, T-1 outcome column present; (3) T-1 ANNEX in Filter Log Resolution: names withheld observation by sub-skill and obs number, or invokes T-1 RECALIBRATION |

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration and before the Execution Sequence. This
section is part of the output artifact.

**Genre declaration**: This report is a pre-implementation simulation findings document. Structural
vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior considered for the filter gate
- "Elevated" -- observation passed T-1 AND all four filter rules; appears in Findings Table
- "Withheld under T-1" (withheld-T1) -- observation failed T-1 (no spec location or no concrete
  implementation consequence); named in T-1 ANNEX; does not enter filter log or Findings Table
- "Rejected" (withheld-rule) -- observation passed T-1 but failed one of filter rules 1-4;
  appears in filter log with rejection reason and rule number
- "T-1" -- the elevation threshold defined immediately below

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if and only
if it (a) names a specific spec location and (b) describes a gap or violation that would cause
incorrect implementation behavior if unresolved. An observation failing either condition is
withheld under T-1.

**T-1 ANNEX obligation**: The Filter Log Resolution includes a mandatory T-1 ANNEX block. The
T-1 ANNEX must either (a) name at least one observation that was considered and withheld under T-1,
citing the sub-skill and observation number and the T-1 condition that was not met, or (b) invoke
T-1 RECALIBRATION (apply the T-1 ANNEX RECALIBRATION template). A report in which T-1 rejects
nothing and no recalibration is declared has not demonstrated T-1 judgment.

**Per-scope gates**: Five per-scope gate tables follow, one per sub-skill section. Each records
observations considered for that scope and their T-1 outcome (passed or withheld-T1). Gates are
co-located with execution evidence -- not aggregated into a central table.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. Write the per-scope gate table after each sub-skill before advancing.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | T-1 outcome | If withheld-T1: which condition failed |
|-------|-----------------|------------|---------------------------------------|

T-1 outcomes: passed (enters filter log) | withheld-T1 (enters T-1 ANNEX only)

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

Aggregate T-1-passing observations from all five per-scope gate tables into the global filter log.
Observations withheld-T1 do not appear here.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief reason]).
> Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: A gate
> that rejects nothing provides no evidence of filtering judgment. Required: revisit candidate
> list. Either (a) name at least one observation that should be rejected under the filter rules,
> or (b) justify that every candidate is genuinely anchored to a named spec location and scoped
> to at least one downstream component.

**T-1 ANNEX** (required immediately after Template A or B, in every report):

> T-1 ANNEX: [N] observations withheld under T-1 during execution.
> Withheld:
> - [Sub-skill, Obs #]: withheld because [T-1 condition not met: no named spec location /
>   no concrete implementation consequence / other condition]. Not in filter log.
> [Repeat per withheld-T1 observation, or apply T-1 ANNEX RECALIBRATION template if zero.]

The T-1 ANNEX is required even when all observations pass T-1. Zero withheld-T1 observations
trigger T-1 RECALIBRATION, not silence.

---

**FINDINGS TABLE**

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

For top three ranked findings: state blast radius rationale (name downstream flows, components,
or contracts affected and explain why scope reaches that far).

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills that share
surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply the comparison-step empty-state template.

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

For each compounding finding: "Promoted from [tier] to [tier] because [cross-skill root cause
means that X expands downstream scope from Y to Z]."

If no compounding pairs: apply the cross-skill-patterns empty-state template. Must cite Step 2
pairs and verdicts -- a bare declaration without citations fails C-15.

Steps 1 and 2 are required even when Step 3 concludes no patterns.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in the
STRUCTURAL AXIS DECLARATION, verify whether it fired. Cite the actual report section by name and
actual evidence (counts, template letters, pair counts). Do not write "fired" without a section
name and evidence. Row 6 uses fired / partial / not fired with three independently-verifiable
sub-claims.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observation count; rejections by rule number and reason] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template letter: A or B; rejection count or recalibration justification cited] | fired / not fired |
| Empty-state templates | [list each section where a template fired, or "none"] | [for each: template type + first clause of text applied] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [pair count from Step 1; verdict summary from Step 2: "N pairs, M compounding"] | fired / not fired |
| Structural Axis Declaration (five rows, equal depth) | Structural Axis Declaration | [confirm: "Five rows declared; each names 2+ distinct observables; row 5 (observational discipline) names 3 sub-observables co-equal with rows 1-4"] | fired / not fired |
| Observational discipline axis | [OBSERVATIONAL DISCIPLINE section] + [names of all five per-scope gate sections] + [T-1 ANNEX location] | Sub-claim 1: genre named, structural label glossary present (elevated / withheld-T1 / rejected defined) -- [cite section and first label defined]; Sub-claim 2: T-1 ANNEX present in Filter Log Resolution -- [name the withheld-T1 observation cited, e.g., "flow-lifecycle Obs 3: withheld, no spec location"] or [confirm T-1 RECALIBRATION invoked]; Sub-claim 3: five per-scope gate tables present, each co-located with its sub-skill section (not centralized) -- [cite each section name] | fired / partial / not fired |

**Partial verdict guidance** (row 6): If partial, name the failed sub-claim: "Partial: Sub-claim
[1/2/3] not satisfied because [specific reason]. Sub-claims [x, y] satisfied: [evidence for
each]." A partial result is preferable to a silent failure -- it makes the weakest mechanism
immediately actionable.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline > Execution
(with per-scope gate tables embedded, one per sub-skill) > Candidate Observations and Filter Log >
Filter Log Resolution (with T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings >
Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section (five rows, each with 2+ named observables,
equal depth). Structural Compliance Checklist is the last section (row 6 uses fired / partial /
not fired with three independently-verifiable sub-claims). T-1 ANNEX is required in every report;
it may never be omitted.

The five structural axes -- filtering, empty-state, cross-skill comparison,
declaration-compliance, observational discipline -- must each produce observable output in the
sections named in the declaration table. The compliance checklist is the report's self-attestation
that they did, and row 6's partial verdict is the diagnostic instrument if the observational
discipline axis fires incompletely.
