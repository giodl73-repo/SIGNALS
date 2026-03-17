---
skill: campaign-simulate
round: 7
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v7-2026-03-16.md
---

# campaign-simulate -- Round 7 Variations

**Context**: R6 V-04 and V-05 both scored 100/100 under v6 rubric. V-05 was architecturally
superior because its compliance checklist decomposed the observational discipline axis into
`fired/partial/not-fired` sub-claim verdicts (C-24 signal), and V-03's per-scope Disposition
column made T-1 evidence verifiable at the execution scope rather than in a post-hoc ANNEX
(C-25 signal). These patterns were codified as C-24 (sub-claim architecture in compliance
checklist for multi-part axes) and C-25 (T-1 evidence co-located at execution scope, not only
in a post-execution block) in rubric v7.

**Under v7**: raw max 114, divisor 1.14. R6 V-05 without C-24/C-25 = 110/114 = 96.5
normalized. To reach 100: must pass both C-24 and C-25.

**Round 7 axes chosen:**
- Single-axis: V-01 (C-24 — sub-claim architecture in compliance checklist rows),
  V-02 (C-25 — per-scope Disposition column as primary T-1 evidence),
  V-03 (C-25 alternative — structural Disposition column embedded in per-scope gate table
  with explicit withheld-T1 / elevated / withheld-rule labeling)
- Combined: V-04 (C-24 + C-25 on R6 V-05 base), V-05 (full integration: sub-claim
  compliance architecture + per-scope Disposition + T-1 ANNEX as summary-only)

---

## V-01 -- Sub-Claim Architecture in Compliance Checklist (C-24)

**Variation axis:** Output format -- the compliance checklist row for any multi-part structural
axis must break its verdict into independently-verifiable sub-claim statuses. The observational
discipline row (the canonical multi-part axis) declares three sub-claims -- `fired/partial/
not-fired` per sub-claim -- and a partial overall verdict must name the specific failing
sub-claim. Other multi-part axes (cross-skill comparison with Steps 1+2+3; declaration-
compliance with declaration+checklist) also receive sub-claim decomposition.

**Hypothesis:** C-24 passes by construction. Every compliance checklist row that covers a
multi-part commitment declares named sub-claims with independent verdicts. A partial verdict
identifies the failing sub-claim by name rather than emitting a binary PASS. C-25 is not
directly targeted -- the T-1 ANNEX structure from R6 V-05 is preserved, so T-1 evidence may
still live primarily in a post-execution block.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes. The last section verifies all five fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact -- not the prompt text
you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any
section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped to
  at least one downstream component."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections)**: "T-1 ANNEX: Zero observations withheld
  under T-1 in this report. T-1 RECALIBRATION REQUIRED: A T-1 rule with no rejection
  citations is unfalsified. Either (a) identify an observation that was considered and
  withheld because it lacked a spec reference or concrete consequence, or (b) state why this
  topic produced no sub-T-1 observations and what that implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts from the Step 2 table]. Each describes a distinct root
  cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation of why
  this area produced no observable candidates]."
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

Write this section as the first section of your output report. An evaluator reading only this
section must be able to predict which structural sections appear in the report and verify each
axis independently by checking its named sub-observables. All five rows must have equal depth
in the Observable Output column: each names at least two distinct, independently-checkable
observables. Complete this before writing any execution results.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution block (Template A: normal / Template B: vacuous, recalibration required) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited |
| Empty-state axis | C-11 | Per-section empty-state templates defined for all section types; silent empty sections not permitted | (1) Any structured section with no results: named template text in place of blank; (2) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: candidate pairings (Step 1), pairwise verdicts (Step 2), pattern declaration (Step 3 -- requires Steps 1+2) | (1) Step 1 table: F-ID pairs and surface similarity; (2) Step 2 table: pairwise verdicts; (3) Step 3 declaration: compounding patterns named or Step 2 pairs and verdicts cited |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (before findings, five rows equal depth) + Structural Compliance Checklist (after findings, sub-claim decomposition for multi-part mechanisms) | (1) Structural Axis Declaration: this section, five rows, equal Observable Output depth; (2) Structural Compliance Checklist: final section, multi-part rows decomposed to named sub-claims |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 threshold rule stated before execution + T-1 ANNEX (named T-1 rejection or T-1 RECALIBRATION) + five per-scope gate tables co-located with execution evidence | (1) OBSERVATIONAL DISCIPLINE section: genre named with structural label glossary, T-1 rule stated as if-and-only-if; (2) five per-scope gate tables: one per sub-skill, co-located, T-1 outcome per observation; (3) T-1 ANNEX in Filter Log Resolution: names withheld observation or invokes T-1 RECALIBRATION |

Mechanisms declared above that do not produce observable output receive "not fired" in the
compliance checklist. Do not declare mechanisms you do not use.

---

**OBSERVATIONAL DISCIPLINE**

Write this section immediately after the Structural Axis Declaration and before the Execution
Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior considered for elevation
- "Elevated" -- observation passed T-1 AND all four filter rules; appears in Findings Table
- "Withheld under T-1" -- observation failed T-1 (no spec location or no concrete
  consequence); noted in T-1 ANNEX; does not enter filter log
- "Rejected" -- observation passed T-1 but failed a filter rule (1-4); appears in filter log
  with rejection reason
- "T-1" -- the elevation threshold defined below

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. T-1 is not satisfied by a vague concern, a style
preference, or an observation without a named spec section.

**T-1 ANNEX obligation**: The Filter Log Resolution block includes a mandatory T-1 ANNEX.
The T-1 ANNEX names at least one observation withheld under T-1 ("Obs [X] from [sub-skill]:
withheld because [T-1 condition not met]") or invokes T-1 RECALIBRATION. The T-1 ANNEX
closes the falsifiability gap: a T-1 rule with no rejection citations is a rule that has not
been tested.

**Per-scope gates**: Five per-scope gate tables follow, one per sub-skill, embedded
co-located with execution evidence. Each records observations considered for that scope and
their T-1 outcome. Per-scope gates are not centralized -- each fires within its sub-skill
section.

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
>   no concrete implementation consequence / other].
> [Repeat for each withheld-T1 observation, or apply T-1 ANNEX RECALIBRATION template if
> zero.]

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

Complete all three steps. Step 3 requires Steps 1 and 2 to be present.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills that
share surface similarity.

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

If no compounding pairs: apply the cross-skill-patterns empty-state template. The template
requires citing every pair from Step 2 and their verdicts.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in
the STRUCTURAL AXIS DECLARATION, confirm whether it fired.

**Sub-claim architecture rule**: For any row that covers a multi-part mechanism (a mechanism
that committed to two or more independently-verifiable observables in the declaration table),
the Status column must decompose the verdict into named sub-claim statuses using the scheme:
`fired / partial / not-fired` per sub-claim. A partial overall verdict names the specific
failing sub-claim. A binary "PASS" for a multi-part row is not permitted.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "6 observations across 5 sub-skills; 2 rejected at Rule 1; 1 rejected at Rule 3"] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template letter cited; rejection count; T-1 ANNEX: name the T-1 rejection cited or RECALIBRATION invoked] | fired / not fired |
| Empty-state templates | [list each section where a template fired] | [for each: template type and first clause] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding or empty-state with cited pairs) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present; Sub-claim 2: equal Observable Output depth (at least two named observables per row); Sub-claim 3: appears before any execution section | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [list: OBSERVATIONAL DISCIPLINE section + per-scope gate section names + T-1 ANNEX location] | Sub-claim 1: genre named with structural label glossary; Sub-claim 2: T-1 rule stated as if-and-only-if before execution; Sub-claim 3: five per-scope gate tables co-located with execution; partial verdict names failing sub-claim | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," name the specific failing sub-claim. If "not fired,"
apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution (with per-scope gate tables) > Candidate Observations and Filter Log > Filter Log
Resolution (with T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings > Cross-Skill
Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section. Structural Compliance Checklist is the last
section. The T-1 ANNEX is required in every report. The Structural Compliance Checklist uses
sub-claim decomposition for all multi-part rows -- binary verdicts for multi-part axes are
not permitted.

---

## V-02 -- Per-Scope Disposition Column as Primary T-1 Evidence (C-25)

**Variation axis:** Output format -- T-1 evidence must be embedded at each per-scope gate
table as a Disposition column (`elevated / withheld-T1 / withheld-rule`), so the filter
decision is verifiable at the point of execution. The T-1 ANNEX in Filter Log Resolution
is permitted and encouraged as a summary aggregator, but it may not substitute for per-scope
records. A per-scope gate table with no Disposition column fails C-25 even if a T-1 ANNEX
exists. The compliance checklist verifies per-scope embedding explicitly.

**Hypothesis:** C-25 passes by construction. Each per-scope gate table has a Disposition
column populated per observation. The T-1 ANNEX summarizes what the per-scope tables already
contain -- it does not introduce new evidence. An evaluator can verify T-1 application at
each scope without cross-referencing any post-execution block. C-24 is not targeted here --
the compliance checklist uses the R6 V-05 row format without sub-claim decomposition.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes. The last section verifies all five fired. Both sections are written by the model into
the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored to a named spec location and scoped to
  at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. SCOPE RECALIBRATION REQUIRED: Either name one observation
  that was considered and failed T-1 for this scope, or confirm this scope is unusually clean
  and state why no observation failed the elevation threshold."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections)**: "T-1 ANNEX: No withheld-T1 rows
  appear across all five per-scope gate tables. T-1 RECALIBRATION REQUIRED: Either identify
  an observation withheld under T-1, or confirm per-scope clean and state what that implies
  about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output. Reason: [why]. Impact on report validity: [whether
  omission affects findings]."

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

Write as the first section of your output report. All five rows must have equal depth in the
Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A or B) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution block: template letter and rejection count |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types | (1) Named template text in all structured sections with no results; (2) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol (Steps 1, 2, 3) | (1) Step 1 table: F-ID pairs and surface similarity; (2) Step 2 table: pairwise verdicts; (3) Step 3 declaration: patterns named or Step 2 pairs cited |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, five rows equal depth) + Structural Compliance Checklist (last section, evidence column cites section names and counts) | (1) Structural Axis Declaration: this section; (2) Structural Compliance Checklist: final section with populated evidence column |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 threshold rule stated before execution + per-scope Disposition column (elevated / withheld-T1 / withheld-rule) embedded in each sub-skill gate table + T-1 ANNEX (summary aggregator, not primary evidence) | (1) OBSERVATIONAL DISCIPLINE section: genre named, T-1 rule stated; (2) five per-scope gate tables with Disposition column: primary T-1 evidence co-located at execution scope; (3) T-1 ANNEX in Filter Log Resolution: summarizes per-scope Disposition totals, does not introduce new evidence |

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior evaluated for elevation
- "elevated" -- Disposition value: observation passed T-1 AND all four filter rules
- "withheld-T1" -- Disposition value: observation failed T-1 (no spec location or no
  concrete implementation consequence); does not enter global filter log
- "withheld-rule" -- Disposition value: observation passed T-1 but failed a filter rule
  (1-4); enters filter log with rejection reason
- "T-1" -- the if-and-only-if elevation criterion defined below

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1.

**Per-scope Disposition rule**: Each per-scope gate table includes a Disposition column
(`elevated / withheld-T1 / withheld-rule`) populated for every observation. The Disposition
column is the primary record of T-1 application -- it is verifiable at the execution scope
without cross-referencing any post-execution block. If zero withheld-T1 rows appear in a
scope, that scope triggers T-1 SCOPE RECALIBRATION (see template above).

**T-1 ANNEX role**: The T-1 ANNEX in Filter Log Resolution aggregates Disposition totals
from all five per-scope gate tables. It is a summary, not a primary evidence source. It does
not introduce T-1 rejections that are absent from per-scope records.

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

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table.

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

Declare the gate state.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason]).
> Gate operating normally.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after Template A or B -- aggregates per-scope Disposition
data, does not introduce new evidence):

> T-1 ANNEX (summary): Across all five per-scope gate tables:
> - withheld-T1 total: [N] (see per-scope Disposition columns for source records)
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

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

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: [compounding patterns, or empty-state template citing
Step 2 verdicts]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Cite actual section names and evidence from the report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [counts and rule numbers] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | [Template letter + count; T-1 ANNEX: total withheld-T1 count, scopes with zero withheld-T1 named] | fired / not fired |
| Empty-state templates | [list sections where templates fired] | [template type and first clause] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [pair count + verdict summary] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [five rows, equal depth confirmed] | fired / not fired |
| Observational discipline axis | [list all five per-scope gate section names] + T-1 ANNEX | Sub-claim 1: genre declared (vocabulary listed); Sub-claim 2: T-1 rule stated as if-and-only-if before execution; Sub-claim 3: per-scope Disposition columns present for all five sub-skills with at least one withheld-T1 row per scope (or RECALIBRATION invoked); T-1 ANNEX is a summary of per-scope data, not new evidence | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution (with per-scope gate tables with Disposition column) > Candidate Observations and
Filter Log > Filter Log Resolution (with T-1 ANNEX summary) > Findings Table > Execution Log >
Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance
Checklist.

The per-scope Disposition column is the primary record of T-1 application. The T-1 ANNEX
summarizes it. An evaluator must be able to verify every T-1 decision from the per-scope
gate tables without reading the T-1 ANNEX.

---

## V-03 -- Disposition Column as Structural Template in Per-Scope Gate (C-25 Alternative)

**Variation axis:** Lifecycle emphasis -- the per-scope gate table schema is promoted from
a format suggestion to a structural template with named column constraints. The Disposition
column (`elevated / withheld-T1 / withheld-rule`) is declared in the STRUCTURAL AXIS
DECLARATION as a named observable, not merely described in the OBSERVATIONAL DISCIPLINE
section. The gate table schema appears verbatim in the prompt, making the column non-optional.
A missing Disposition column is a structural axis violation, not a formatting preference.

**Hypothesis:** C-25 passes by construction because the Disposition column is a declared
structural commitment, not an instruction-level request. The compliance checklist row for the
observational discipline axis verifies all five per-scope Disposition columns by name. C-24
is not targeted -- compliance checklist rows use the R6 format without sub-claim decomposition.
Risk: naming the Disposition column in the structural axis declaration adds a row-level
constraint that may conflict with models that reformulate gate table columns.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes including their specific table schemas. The last section verifies all five fired by
checking named columns, not just section presence. Both sections are written by the model
into the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: revisit candidate list; either name one
  observation that should be rejected, or justify that every candidate is genuinely anchored."
- **Disposition column withheld-T1 zero**: "Disposition audit for [sub-skill]: [N]
  observations. Zero withheld-T1 rows. T-1 RECALIBRATION: Either name one withheld-T1
  observation for this scope or confirm scope is clean and state why T-1 did not fire."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but did not fire. Reason: [why].
  Impact: [whether omission affects findings]."

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

Write as the first section of your output report. The Observable Output column names specific
table schemas and column names, not just section names. An evaluator verifying this table
against the report body checks column presence, not section presence.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A or B) | (1) Filter Log table: columns Sub-Skill, Obs #, What was noticed, Spec Location, Blast Radius, Elevate?, Rejection Reason; (2) Filter Log Resolution block: template letter and rejection count |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types | (1) Named template text in any structured section with no results; (2) template type cited in compliance checklist for each fired section |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol (Steps 1, 2, 3) | (1) Step 1 table present with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table present with Verdict and Reason columns; (3) Step 3 declaration citing compounding patterns or Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section) + Structural Compliance Checklist (last section) | (1) Structural Axis Declaration: this section, five rows; (2) Structural Compliance Checklist: final section, evidence column populated |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (named vocabulary) + T-1 rule (if-and-only-if) + five per-scope gate tables each with schema: Obs #, What was noticed, Disposition, T-1 reason (if withheld-T1), Filter rule (if withheld-rule) | (1) OBSERVATIONAL DISCIPLINE section: genre declared with vocabulary glossary; T-1 rule stated; (2) five per-scope gate tables -- one per sub-skill, co-located, schema above enforced; Disposition column values: elevated / withheld-T1 / withheld-rule; (3) compliance checklist names each per-scope gate section by sub-skill |

The per-scope gate table schema above is structural. A per-scope gate table that omits the
Disposition column fails the observational discipline axis regardless of section presence.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout:
- "elevated" -- observation passed T-1 AND all four filter rules (Disposition value)
- "withheld-T1" -- observation failed T-1; excluded from global filter log (Disposition
  value)
- "withheld-rule" -- observation passed T-1; failed a filter rule; enters filter log with
  rule citation (Disposition value)

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. T-1 not satisfied by vague concerns, style
preferences, or observations without spec anchoring.

**Per-scope Disposition schema** (enforced for all five sub-skills):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

This schema is declared as a structural commitment. Every per-scope gate table must use this
exact column set. Disposition is not a computed summary column -- it is the per-observation
filter record, populated at execution time, co-located with the sub-skill that produced it.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table using the
schema above.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

Each per-scope gate table is co-located within its sub-skill section, not centralized. If
zero withheld-T1 rows appear for a scope: apply the Disposition column withheld-T1 zero
template immediately below the gate table.

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

**Template A:** Filter gate applied. [N] evaluated. [M] rejected (Rule [N]: [reason]).
**Template B:** Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION REQUIRED.

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

**Step 3 -- Patterns declaration**: [compounding patterns, or empty-state template citing
Step 2 verdicts]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Verify by column name and section name, not section presence
alone.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [counts and rule numbers] | fired / not fired |
| Filter Log Resolution | [section name] | [Template letter + count] | fired / not fired |
| Empty-state templates | [sections where templates fired] | [template type cited] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [pair count + verdict summary] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [five rows confirmed; schemas in row 5 match execution] | fired / not fired |
| Observational discipline axis (per-scope Disposition) | [name each of the five per-scope gate section names explicitly] | Sub-claim 1: genre declared with vocabulary glossary; Sub-claim 2: T-1 rule stated before execution; Sub-claim 3: five per-scope Disposition columns present (Obs #, What was noticed, Disposition, T-1 reason, Filter rule) -- for each, cite sub-skill name and whether at least one withheld-T1 row appeared or RECALIBRATION was invoked | fired / partial [name the sub-skill missing Disposition column] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution (with per-scope gate tables using declared schema) > Candidate Observations and
Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings >
Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

The Disposition column schema is structural. Any per-scope gate table missing the Disposition
column fails the observational discipline axis. The compliance checklist names each of the
five per-scope gate sections explicitly.

---

## V-04 -- Combined: C-24 + C-25 on R6 V-05 Base

**Variation axes combined:**
1. Sub-claim architecture in compliance checklist (V-01 axis) -- C-24: every multi-part
   mechanism row in the compliance checklist declares named sub-claim statuses (`fired /
   partial / not-fired`); a partial verdict names the failing sub-claim
2. Per-scope Disposition column as primary T-1 evidence (V-02 axis) -- C-25: each per-scope
   gate table has a Disposition column (`elevated / withheld-T1 / withheld-rule`) as the
   primary T-1 record; T-1 ANNEX in Filter Log Resolution is a summary aggregator only
3. All prior R6 V-05 mechanisms: filtering, empty-state, cross-skill comparison,
   declaration-compliance, observational discipline (C-19/C-20/C-21), co-equal axis row
   depth (C-22), T-1 rejection obligation (C-23)

**Hypothesis:** C-24 and C-25 both pass by construction. C-24: compliance checklist rows for
multi-part axes (observational discipline, cross-skill comparison, declaration-compliance)
declare three independently-verifiable sub-claims each; a partial verdict names the failing
sub-claim by name rather than emitting a binary PASS. C-25: the per-scope Disposition column
is the primary T-1 record at execution scope; the T-1 ANNEX summarizes what the per-scope
tables already contain and does not introduce new evidence. All prior C-01--C-23 mechanisms
are unchanged. Risk: four structural layers (co-equal axis row depth + T-1 ANNEX + per-scope
Disposition + sub-claim compliance checklist) add overhead. The compliance checklist with
sub-claim architecture will be the longest section; the model must populate it without
abbreviating sub-claim details.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes with equal structural depth and three independently-verifiable sub-observables per axis.
The last section verifies all five fired using sub-claim decomposition for multi-part rows.
Both sections are written by the model into the output artifact -- not the prompt text you
are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment -- only that the schema ran. Required: revisit candidate list. Either
  (a) name at least one observation that should be rejected under the filter rules, or (b)
  justify that every candidate is genuinely anchored."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. SCOPE RECALIBRATION REQUIRED: Either name one observation
  that failed T-1 for this scope, or confirm scope is clean and state why T-1 did not fire."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections)**: "T-1 ANNEX: No withheld-T1 rows across
  all five per-scope gate tables. T-1 RECALIBRATION REQUIRED: Either identify a withheld-T1
  observation, or confirm per-scope clean and state what that implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output. Reason: [why]. Impact on report validity: [whether
  omission affects findings]."

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
section must be able to (a) predict which structural sections appear in the report, (b)
verify each axis independently by checking named sub-observables, and (c) know the exact
schema of each gate table before reading any execution section. All five rows must have equal
depth: three independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous, recalibration required) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named, rejection count cited; (3) Filter rules 1-4 listed in filter log section |
| Empty-state axis | C-11 | Per-section empty-state templates defined for all section types; silent empty sections not permitted | (1) Named template text in all structured sections with no results; (2) template type cited in compliance checklist; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table: F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table: Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (before findings, five rows equal depth, three observables per row) + Structural Compliance Checklist (after findings, sub-claim decomposition for multi-part rows) | (1) Structural Axis Declaration: this section, five rows, three observables each; (2) Structural Compliance Checklist: final section, multi-part rows use sub-claim architecture; (3) compliance checklist evidence column cites section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 threshold rule (if-and-only-if, before execution) + per-scope Disposition column (elevated / withheld-T1 / withheld-rule) as primary T-1 record + T-1 ANNEX as summary aggregator | (1) OBSERVATIONAL DISCIPLINE section: genre named with glossary, T-1 rule stated as if-and-only-if; (2) five per-scope gate tables with Disposition column: primary T-1 evidence at execution scope -- schema: Obs #, What was noticed, Disposition, T-1 reason, Filter rule; (3) T-1 ANNEX in Filter Log Resolution: summarizes per-scope Disposition totals; names at least one withheld-T1 observation by scope and reason (or invokes T-1 RECALIBRATION) |

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary used throughout:
- "Candidate observation" -- an observed spec behavior evaluated for elevation
- "elevated" -- Disposition: passed T-1 AND all four filter rules; appears in Findings Table
- "withheld-T1" -- Disposition: failed T-1 (no spec location or no concrete consequence);
  primary record in per-scope Disposition column; also aggregated in T-1 ANNEX
- "withheld-rule" -- Disposition: passed T-1 but failed a filter rule (1-4); enters filter
  log with rule citation
- "T-1" -- the if-and-only-if elevation criterion defined below

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would
cause incorrect implementation behavior. Observations failing either condition receive
Disposition: withheld-T1.

**Per-scope Disposition rule**: Each per-scope gate table includes a Disposition column as
the primary record of T-1 application. The Disposition column is populated at execution
time, co-located with the sub-skill that produced the observation. It is verifiable without
reading any post-execution block. If zero withheld-T1 rows appear in a scope, that scope
triggers T-1 SCOPE RECALIBRATION.

**T-1 ANNEX role**: The T-1 ANNEX in Filter Log Resolution aggregates Disposition: withheld-
T1 totals from all five per-scope gate tables. It is a summary, not a primary evidence
source. It must cite at least one named withheld-T1 observation by scope and reason (or
invoke T-1 RECALIBRATION) to satisfy C-23.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each sub-skill, write its per-scope gate table.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

**Per-scope gate table schema** (write one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero withheld-T1
template immediately below the gate table.

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

Declare the gate state.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason]).
> Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after Template A or B -- aggregates per-scope data):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records):
> - withheld-T1 total across all scopes: [N]
> - Named example: [Sub-skill, Obs #] withheld because [T-1 condition not met: no named
>   spec location / no concrete implementation consequence / other]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

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

Complete all three steps. Step 3 requires Steps 1 and 2 to be present.

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: [compounding patterns, or empty-state template citing
Step 2 verdicts]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section of your output report. For each mechanism, verify it fired.

**Sub-claim architecture rule**: For any row covering a multi-part mechanism (two or more
independently-verifiable observables declared in the declaration table), the Status column
must declare sub-claim-level statuses using `fired / partial / not-fired` per sub-claim.
A partial verdict names the failing sub-claim. Binary PASS for a multi-part row is not
permitted.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "7 observations across 5 sub-skills; 2 rejected at Rule 1; 1 rejected at Rule 4"] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: Template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present with withheld-T1 total and named example (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX cites per-scope source records, not new evidence | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (compounding pattern named or empty-state with Step 2 pairs cited) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present; Sub-claim 2: equal Observable Output depth (three named observables per row); Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary (list two structural labels cited); Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills with Disposition values cited (elevated / withheld-T1 / withheld-rule); at least one withheld-T1 row per scope (or RECALIBRATION invoked per scope); T-1 ANNEX summarizes per-scope data as aggregator; partial verdict names which sub-skill's Disposition column is absent or unpopulated | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline. If "not fired,"
apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline >
Execution (per-scope gate tables with Disposition column, co-located per sub-skill) >
Candidate Observations and Filter Log > Filter Log Resolution (Template A or B, then T-1
ANNEX) > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol
(Steps 1, 2, 3) > Structural Compliance Checklist.

The per-scope Disposition column is the primary T-1 record. The T-1 ANNEX summarizes it.
The Structural Compliance Checklist uses sub-claim decomposition for all multi-part rows;
binary verdicts for multi-part axes are not permitted.

---

## V-05 -- Full Integration: Sub-Claim Compliance + Per-Scope Disposition + T-1 ANNEX as Summary

**Variation axes combined:**
1. Sub-claim architecture in compliance checklist (C-24): multi-part rows declare named
   sub-claim statuses; partial verdict names the failing sub-claim; schema enforced by an
   explicit rule at the top of the checklist section
2. Per-scope Disposition column as primary T-1 evidence (C-25): Disposition column is a
   declared structural commitment (named in the axis table); T-1 ANNEX is explicitly marked
   as a summary aggregator -- it must cite per-scope source records; a T-1 ANNEX that
   introduces evidence absent from per-scope tables is a structural violation
3. All prior mechanisms: filtering, empty-state, cross-skill comparison, declaration-
   compliance (C-17/C-18), co-equal axis row depth (C-22), T-1 rejection obligation in T-1
   ANNEX (C-23)

**Hypothesis:** C-24 and C-25 both pass by construction. C-24: the compliance checklist
opens with an explicit sub-claim architecture rule; every multi-part row decomposes into
named sub-claims; a partial verdict identifies the failing sub-claim inline rather than
emitting a binary PASS. C-25: the Disposition column is named in the STRUCTURAL AXIS
DECLARATION as a declared observable -- its absence is a structural axis violation, not a
formatting miss; the T-1 ANNEX is explicitly characterized as a summary aggregator and must
cite per-scope source records. All C-01--C-23 mechanisms are present. Risk: this is the
most structurally demanding variation; the model must maintain Disposition column fidelity
across five sub-skill sections while producing a sub-claim-decomposed compliance checklist.
The structural axis declaration preempts abbreviation by naming the column schema as an
observable before any execution occurs.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five
axes with equal structural depth. Each axis names three independently-verifiable observables
including specific schema constraints. The last section verifies all five fired using
sub-claim decomposition -- binary verdicts for multi-part mechanisms are a structural
violation. Both sections are written by the model into the output artifact -- not the
prompt text you are reading.

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
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural, its absence fails this axis; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing the per-scope record by scope name (or invokes T-1 RECALIBRATION with reference to which scopes had zero withheld-T1) |

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
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: five rows present; Sub-claim 2: each row has three independently-verifiable observables in the Observable Output column; Sub-claim 3: section appears before any execution evidence -- confirmed by section ordering | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires -- cite OBSERVATIONAL DISCIPLINE section; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- for each scope, cite sub-skill name and whether Disposition column is populated with at least one withheld-T1 row (or T-1 SCOPE RECALIBRATION invoked); T-1 ANNEX confirmed as summary aggregator citing per-scope source records; partial verdict names the sub-skill whose Disposition column is absent or the T-1 ANNEX that introduced evidence without per-scope counterpart | fired / partial [name failing sub-claim] / not fired |

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
1. Per-scope Disposition column is present for all five sub-skills (C-25)
2. T-1 ANNEX summarizes per-scope Disposition data; it does not introduce new evidence (C-25)
3. Compliance checklist uses sub-claim decomposition for all multi-part rows; binary verdicts
   are a structural violation (C-24)
4. A partial compliance verdict names the specific failing sub-claim inline (C-24)
5. Five structural axis rows with equal depth appear before any execution evidence (C-22)
6. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)
