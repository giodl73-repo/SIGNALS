---
skill: campaign-simulate
round: 10
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v9-2026-03-17.md
---

# campaign-simulate -- Round 10 Variations

**Context**: R9 V-05 satisfies C-32 (three-point DR-NN chain), C-33 (self-extending
nine-row declaration), C-34 (full empty-state coverage for four section types), C-35
(typed Conf rationale), and also satisfies C-36 and C-37 as implicit consequences of its
structure. Rubric v9 formalizes C-36 and C-37 as explicit aspirational criteria. R10
target: isolate C-36 and C-37 as standalone structural mechanisms (V-01, V-02, V-03),
merge them (V-04), then build the full eleven-axis integration on the R9 V-05 base (V-05).

**Under rubric v9**: aspirational pool is 29 criteria capped at 10 pts. Max score 100.
R9 V-05 without explicit C-36/C-37 mechanisms passes those criteria by implication but
does not expose them as verifiable structural commitments with their own checklist rows.
R10 V-05 targets all six R7-R9 criteria simultaneously with eleven independently-verifiable
structural axis rows, each with a corresponding compliance checklist row.

**Round 10 axes chosen:**
- Single-axis: V-01 (C-36 -- Execution Order Gate as structural enforcement; role sequence
  axis), V-02 (C-37 -- Row Count Assertion as completeness proof; output format axis),
  V-03 (C-36 via layer-narrative phrasing register -- prose enforcement vs structural gate;
  phrasing register axis)
- Combined: V-04 (C-36 + C-37 -- gate table + count assertion merged on 7-row declaration;
  role sequence + output format)
- Full integration: V-05 (all six: C-32 + C-33 + C-34 + C-35 + C-36 + C-37 on R9 V-05
  base; eleven-row declaration with Row Count Assertion and Execution Order Gate)

---

## V-01 -- Execution Order Gate (C-36)

**Variation axis:** Role sequence -- a dedicated EXECUTION ORDER GATE section appears
before OBSERVATIONAL DISCIPLINE. It declares Platform Layer = {trace-state, trace-contract,
trace-permissions} and Domain Layer = {flow-lifecycle, flow-conversation}, states the C-36
constraint, and requires the model to fill a Layer Completion Record as execution proceeds.
The gate signal is written between step 3 and step 4. The Execution Log gains a Layer column
as an independent second verifier. The Structural Compliance Checklist gains a dedicated
execution-order-gate row. C-29, C-31, C-33, C-34, C-35 are not targeted.

**Hypothesis:** C-36 passes by construction. The EXECUTION ORDER GATE is the primary
enforcement record: all three Platform rows must show "complete" before any Domain row
advances from "pending." The Execution Log Layer column is a second verifier a reviewer
can read in isolation. The checklist row provides a third verification path via sub-claims.

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
- **Execution Order Gate -- domain started before platform complete**: "EXECUTION ORDER GATE
  VIOLATION: Domain Layer sub-skill [name] began before Platform Layer completion was
  recorded. C-36 FAIL: trace-state, trace-contract, and trace-permissions must all appear in
  the Layer Completion Record as complete before any domain sub-skill begins. Retroactive
  re-examination of [domain sub-skill] findings required: dependency rules may have been
  undeclared when those findings were evaluated."

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
of each gate table before reading any execution. All six rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing per-scope record by scope name |
| Execution-order axis | C-36 | EXECUTION ORDER GATE (before Observational Discipline): Layer Completion Record with status column for each sub-skill; gate signal written between step 3 and step 4; Execution Log Layer column as second verifier | (1) EXECUTION ORDER GATE section present before any execution: Platform Layer table {trace-state, trace-contract, trace-permissions} and Domain Layer table {flow-lifecycle, flow-conversation} with Status column; (2) Layer Completion Record: gate signal written after step 3 confirming all Platform rows "complete" before Domain rows advance from "pending" -- gate signal cites all three platform sub-skills by name; (3) Execution Log Layer column present for all five sub-skills: Platform rows in positions 1-3, Domain rows in positions 4-5 -- ordering verifiable independently of gate signal |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration and before
OBSERVATIONAL DISCIPLINE. Declare the layer model and record completion status as
execution proceeds.

**C-36 constraint**: Platform Layer sub-skills (trace-state, trace-contract,
trace-permissions) must ALL be recorded as "complete" in the Layer Completion Record before
any Domain Layer sub-skill (flow-lifecycle, flow-conversation) advances beyond "pending."

**Why this ordering matters**: Dependency rules describing how findings in one sub-skill
scope constrain findings in another are defined during Platform Layer execution. A domain
finding evaluated before the relevant dependency rule has been declared is evaluated against
an incomplete rule set -- producing a false CLEAN result or an unindexed finding.
Platform-first ordering eliminates this evaluation race condition.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion marker |
|-------|-----------|----------|--------|------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | [state when complete, e.g., "gate table written, N observations"] |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until all Platform rows = complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until all Platform rows = complete] | |

After completing execution position 3 (trace-permissions) and before beginning execution
position 4 (flow-lifecycle), write this gate signal in the output:

> EXECUTION ORDER GATE: Platform Layer complete. trace-state: complete. trace-contract:
> complete. trace-permissions: complete. Domain Layer may begin. Cross-skill dependency
> context is now fully populated for domain finding evaluation.

If any platform sub-skill was not complete before a domain sub-skill began: apply the
Execution Order Gate -- domain started before platform complete empty-state template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE, before the Execution Sequence.

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

Run sub-skills in Platform Layer first, then Domain Layer (C-36 constraint). After each
sub-skill, write its per-scope gate table and update the Layer Completion Record.

1. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants [PLATFORM LAYER]
2. trace-contract    -- expected vs actual output comparison at contract boundaries
                        [PLATFORM LAYER]
3. trace-permissions -- RBAC path trace with privilege escalation detection [PLATFORM LAYER]
                        [Write EXECUTION ORDER GATE signal here before step 4]
4. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
                        [DOMAIN LAYER -- begins only after gate signal]
5. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
                        [DOMAIN LAYER]

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

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

The Layer column is a second verifier for the execution-order axis. Platform rows must
appear in positions 1-3; Domain rows in positions 4-5.

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs |
|-----------|-------|--------|------------|---------|-------------|
| trace-state | Platform | executed / no findings | | | |
| trace-contract | Platform | executed / no findings | | | |
| trace-permissions | Platform | executed / no findings | | | |
| flow-lifecycle | Domain | executed / no findings | | | |
| flow-conversation | Domain | executed / no findings | | | |

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

If no compounding pairs: apply cross-skill-patterns empty-state template.

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
| Execution-order gate (C-36) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: EXECUTION ORDER GATE section present before OBSERVATIONAL DISCIPLINE -- cite section position in report (after Structural Axis Declaration, before Observational Discipline); Sub-claim 2: gate signal present between step 3 and step 4 citing all three platform sub-skills as complete -- quote signal text or cite section name where it appears; Sub-claim 3: Execution Log Layer column shows trace-state, trace-contract, trace-permissions in positions 1-3 (Layer = Platform) and flow-lifecycle, flow-conversation in positions 4-5 (Layer = Domain) -- confirm ordering is independently verifiable from this column alone | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE >
Observational Discipline > Execution Sequence (five sub-skills in platform-first order:
trace-state [1], trace-contract [2], trace-permissions [3], gate signal, flow-lifecycle [4],
flow-conversation [5]; each with co-located per-scope gate table using Disposition schema) >
Candidate Observations and Filter Log > Filter Log Resolution (Template A or B, then T-1
ANNEX as summary aggregator) > Findings Table > Execution Log > Ranked Findings >
Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. EXECUTION ORDER GATE records all three Platform Layer sub-skills as "complete" before
   any Domain Layer sub-skill begins; gate signal written between step 3 and step 4 (C-36)
2. Execution Log Layer column confirms platform-before-domain ordering independently of
   gate signal -- second verifier for C-36 (C-36)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope Disposition data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
6. A partial compliance verdict names the specific failing sub-claim inline (C-24)
7. Six structural axis rows with equal depth appear before any execution evidence (C-22)
8. T-1 ANNEX names at least one withheld-T1 observation by scope and reason (C-23)

---

## V-02 -- Declaration Row Count Assertion (C-37)

**Variation axis:** Output format -- the Structural Axis Declaration gains a Row Count
Assertion block immediately below the table. The block states the row count, enumerates all
targeted quality axes by name, and declares the 1:1 invariant: row count == targeted axis
count. A new "declaration-completeness-proof axis" row in the declaration commits to this
mechanism. The Structural Compliance Checklist gains a dedicated C-37 row verifying the
count, the axis list, and the 1:1 mapping. Execution order is standard (flow-first) -- C-36
is not targeted.

**Hypothesis:** C-37 passes by construction. The Row Count Assertion is written by the
model into the output and contains a verifiable claim: the declared row count matches the
list of targeted axes. A reviewer counts rows in the table, counts entries in the axis list,
and verifies they match. Any discrepancy in either direction is a C-37 fail. C-33
self-extension is not targeted -- the declaration has exactly six rows because six axes are
targeted.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six
axes with a Row Count Assertion proving that every targeted axis has exactly one row. The
last section verifies all six fired using sub-claim decomposition for multi-part axes. Both
sections are written by the model into the output artifact.

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
- **Row Count Assertion mismatch**: "Declaration Row Count Assertion: [N] rows counted.
  Targeted axis count: [M]. N != M: declaration is not contract-complete. Missing row for
  targeted axis: [name]. OR: Row present for untargeted axis: [name]. C-37 FAIL."

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
of each gate table before reading any execution. All six rows must have equal depth: three
independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason (if withheld-T1), Filter rule (if withheld-rule) -- Disposition column is structural; (3) T-1 ANNEX in Filter Log Resolution: characterizes itself as summary aggregator; names at least one withheld-T1 observation by scope and reason, citing per-scope record by scope name |
| Declaration-completeness-proof axis | C-37 | Row Count Assertion block immediately below declaration table: row count stated, targeted axis list enumerated, 1:1 invariant declared; Compliance Checklist C-37 row verifies count, list, and mapping | (1) Row Count Assertion block present immediately below this table: "This declaration contains [6] rows. Targeted quality axes: [list all six by name]. Row count [6] == targeted axis count [6]: declaration is contract-complete."; (2) targeted axis list names exactly the six axes in this table -- no axis absent, no axis extra; (3) Compliance Checklist C-37 row: sub-claim 1 verifies row count is [6], sub-claim 2 verifies axis list has [6] entries with names matching table rows, sub-claim 3 confirms 1:1 mapping holds -- no targeted axis without a row, no row without a targeted axis |

**Row Count Assertion** (write this block immediately after the table above):

> This declaration contains [6] rows. Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) Declaration-completeness-proof axis.
> Row count [6] == targeted axis count [6]: declaration is contract-complete.
> Every targeted axis has exactly one row; no row represents an untargeted axis.

If the count does not match: apply the Row Count Assertion mismatch empty-state template
and identify which targeted axis lacks a row or which row has no corresponding targeted axis.

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
declared schema.

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
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief
> reason for each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED:
> [apply template text; justify that every candidate is anchored].

**T-1 ANNEX** (required immediately after):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total across all scopes: [N] (source: per-scope Disposition columns in
>   [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [T-1 condition not met] --
>   per-scope record in [sub-skill section name]
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

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

[Apply ranked-tier empty-state template for any empty tier]

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Name compounding patterns or apply cross-skill-patterns
empty-state template citing every pair from Step 2.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section. Cite actual section names and evidence.

**Sub-claim architecture rule**: Multi-part rows must use `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited (or RECALIBRATION invoked); Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs listed); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [name each of the five per-scope gate sections by sub-skill] + T-1 ANNEX in Filter Log Resolution | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each scope by sub-skill name | fired / partial [name failing sub-claim] / not fired |
| Declaration completeness proof (C-37) | Structural Axis Declaration (Row Count Assertion block) | Sub-claim 1: Row Count Assertion block present immediately after declaration table -- cite its first sentence; row count stated as [6]; Sub-claim 2: targeted axis list in assertion names all six axes exactly as they appear in the table -- list the six names cited and confirm each matches a table row; Sub-claim 3: 1:1 invariant holds -- row count [6] equals targeted axis count [6]; no targeted axis absent from table, no table row without a corresponding targeted axis -- confirm by name | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (including Row Count Assertion block
immediately below the table) > Observational Discipline > Execution Sequence (five
sub-skills, each with co-located per-scope gate table using Disposition schema) > Candidate
Observations and Filter Log > Filter Log Resolution (Template A or B, then T-1 ANNEX as
summary aggregator) > Findings Table > Execution Log > Ranked Findings > Cross-Skill
Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Row Count Assertion block present immediately after declaration table; row count equals
   targeted axis count; 1:1 mapping holds (C-37)
2. Any mismatch in row count vs targeted axis count triggers Row Count Assertion mismatch
   template and names the discrepancy (C-37)
3. Per-scope Disposition column present for all five sub-skills (C-25)
4. T-1 ANNEX summarizes per-scope Disposition data; introduces no new evidence (C-25)
5. Compliance checklist uses sub-claim decomposition for all multi-part rows (C-24)
6. Six structural axis rows with equal depth appear before any execution evidence (C-22)

---

## V-03 -- Layer-Narrative Phrasing Register (C-36 via Prose Discipline)

**Variation axis:** Phrasing register -- the C-36 constraint is expressed as a prose
annotation within OBSERVATIONAL DISCIPLINE rather than as a separate structural gate table.
A "Layer Sequence Rule" paragraph declares Platform Layer and Domain Layer, states the
ordering constraint, and explains why it matters. No EXECUTION ORDER GATE section. The
execution-order axis row in the declaration names OBSERVATIONAL DISCIPLINE as the mechanism
carrier. The Compliance Checklist verifies C-36 compliance through Execution Log ordering
and the Layer Sequence Rule paragraph, not through a gate signal.

**Hypothesis:** Phrasing register weakens verifiability relative to V-01. The prose-based
mechanism passes C-36 if the execution sequence matches the declared order -- but a reviewer
verifying compliance must infer completion from narrative rather than read a completion
status column. The checklist sub-claim structure exposes this weakness: sub-claim 2 can only
cite "narrative states platform complete" rather than "gate signal with named completion
entries." This variation tests whether prose enforcement satisfies the letter of C-36 while
reducing the structural depth required for independent verification.

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

Write this section as the first section of your output report. All six rows must have equal
depth: three independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + Layer Sequence Rule paragraph (in this section) + five per-scope gate tables with STRUCTURAL Disposition column + T-1 ANNEX (summary aggregator only) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; Layer Sequence Rule paragraph names Platform Layer {trace-state, trace-contract, trace-permissions} and Domain Layer {flow-lifecycle, flow-conversation} and states the ordering constraint; (2) five per-scope gate tables with Disposition column as structural field; (3) T-1 ANNEX: characterizes itself as summary aggregator; names at least one withheld-T1 by scope and reason, citing per-scope record by scope name |
| Execution-order axis (prose) | C-36 | Layer Sequence Rule paragraph in Observational Discipline (prose declaration, not gate table); Execution Log Layer column as structural verifier -- Platform Layer sub-skills appear in positions 1-3, Domain Layer in positions 4-5 | (1) Layer Sequence Rule paragraph present in OBSERVATIONAL DISCIPLINE before any sub-skill fires: names Platform Layer = {trace-state, trace-contract, trace-permissions}, Domain Layer = {flow-lifecycle, flow-conversation}, and states ordering constraint; (2) Execution Sequence section runs trace-state [1], trace-contract [2], trace-permissions [3], flow-lifecycle [4], flow-conversation [5] -- order matches the declared layer sequence; (3) Execution Log Layer column: Platform rows 1-3, Domain rows 4-5 -- reviewer can verify no domain sub-skill executed before a platform sub-skill from the log alone |

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

**Layer Sequence Rule** (stated before any sub-skill fires): This simulation observes a
two-layer discipline. The Platform Layer -- trace-state, trace-contract, and
trace-permissions -- runs first because it defines the structural vocabulary (contracts,
state invariants, permission boundaries) that domain findings will reference. The Domain
Layer -- flow-lifecycle and flow-conversation -- runs only after all three Platform Layer
sub-skills have completed. Reversing this order risks evaluating a domain finding against an
incomplete structural picture: a dependency or contract not yet surfaced by the platform
trace cannot be cited by a domain finding discovered before that trace runs.

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

Run each sub-skill in layer order (Platform Layer first, then Domain Layer). After each
sub-skill, write its per-scope gate table using the declared schema.

1. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants [PLATFORM LAYER]
2. trace-contract    -- expected vs actual output comparison at contract boundaries
                        [PLATFORM LAYER]
3. trace-permissions -- RBAC path trace with privilege escalation detection [PLATFORM LAYER]
4. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
                        [DOMAIN LAYER -- Platform Layer complete at this point]
5. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
                        [DOMAIN LAYER]

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1 rows appear for this scope: apply Per-scope Disposition zero
withheld-T1 template immediately below the gate table before advancing.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

Filter rules: (1) no specific spec location; (2) no blast radius; (3) style preference;
(4) duplicates a higher-blast finding.

---

**FILTER LOG RESOLUTION**

Template A or Template B. T-1 ANNEX immediately after.

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

The order of rows in this log is the structural verifier for the layer sequence.
Platform Layer sub-skills must appear in rows 1-3; Domain Layer sub-skills in rows 4-5.

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs |
|-----------|-------|--------|------------|---------|-------------|
| trace-state | Platform | executed / no findings | | | |
| trace-contract | Platform | executed / no findings | | | |
| trace-permissions | Platform | executed / no findings | | | |
| flow-lifecycle | Domain | executed / no findings | | | |
| flow-conversation | Domain | executed / no findings | | | |

---

**RANKED FINDINGS** / **CROSS-SKILL COMPARISON PROTOCOL** (Steps 1, 2, 3)

[Standard sections -- apply empty-state templates as applicable]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section. Cite actual section names and evidence.

**Sub-claim architecture rule**: Multi-part rows must use `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX present -- withheld-T1 total cited, named example with scope + reason, per-scope source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence introduced | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [list each section where a template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present; Sub-claim 2: Step 2 table present; Sub-claim 3: Step 3 declaration present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [name failing sub-claim] / not fired |
| Observational discipline + layer sequence (C-36) | OBSERVATIONAL DISCIPLINE + Execution Log | Sub-claim 1: genre declared with vocabulary glossary + Layer Sequence Rule paragraph present -- cite the sentence that names both Platform Layer and Domain Layer; Sub-claim 2: Layer Sequence Rule states the ordering constraint before any sub-skill fires -- cite the sentence that says Domain Layer begins only after Platform Layer completes; Sub-claim 3: Execution Log Layer column shows Platform rows in positions 1-3 and Domain rows in positions 4-5 -- cite each sub-skill name with its row position and Layer value, confirming layer sequence matches the declared rule | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline (includes
Layer Sequence Rule paragraph) > Execution Sequence (trace-state [1], trace-contract [2],
trace-permissions [3], flow-lifecycle [4], flow-conversation [5]; each with per-scope gate
table) > Candidate Observations and Filter Log > Filter Log Resolution (Template A or B +
T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison
Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural commitments:
1. Layer Sequence Rule paragraph present in OBSERVATIONAL DISCIPLINE before any sub-skill
   fires; names both layers and states ordering constraint (C-36)
2. Execution sequence runs trace-state, trace-contract, trace-permissions before
   flow-lifecycle and flow-conversation (C-36)
3. Execution Log Layer column presents Platform rows in positions 1-3 and Domain rows in
   positions 4-5 as a structural verifier readable independently (C-36)
4. Per-scope Disposition column present for all five sub-skills (C-25)
5. T-1 ANNEX as summary aggregator only (C-25)
6. Sub-claim decomposition in compliance checklist for all multi-part rows (C-24)
7. Six structural axis rows with equal depth before any execution evidence (C-22)

---

## V-04 -- Execution Order Gate + Row Count Assertion (C-36 + C-37)

**Variation axis:** Role sequence + output format -- both single-axis mechanisms merged on a
7-row declaration. The declaration gains a declaration-completeness-proof axis row and a Row
Count Assertion block below the table. The EXECUTION ORDER GATE section is present before
OBSERVATIONAL DISCIPLINE with its Layer Completion Record and gate signal requirement. The
Structural Compliance Checklist gains two new rows: one for C-36 and one for C-37.

**Hypothesis:** C-36 and C-37 both pass by construction. The EXECUTION ORDER GATE provides
the structural record for C-36: gate signal names all three platform sub-skills as complete
before domain begins. The Row Count Assertion provides the structural record for C-37: seven
rows for seven targeted axes. A reviewer can verify C-36 from the gate signal and Execution
Log independently. A reviewer can verify C-37 by counting rows and axis list entries and
confirming equality.

---

Simulate the technical behavior of: {{topic}}

This report enforces seven structural axes simultaneously. The first section declares all
seven axes with a Row Count Assertion proving completeness. The last section verifies all
seven fired using sub-claim decomposition for multi-part axes. Both sections are written
by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: revisit candidate list. Either (a) name
  at least one observation that should be rejected, or (b) justify that every candidate is
  genuinely anchored to a named spec location and scoped to at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  was considered and failed T-1 for this scope, or confirm scope is clean and state why T-1
  did not fire here."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation, or confirm all scopes are clean."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output. Reason: [why]. Impact: [whether affects findings]."
- **Execution Order Gate -- domain started before platform complete**: "EXECUTION ORDER GATE
  VIOLATION: Domain Layer sub-skill [name] began before Platform Layer completion was
  recorded. C-36 FAIL: All three platform sub-skills must be recorded complete before any
  domain sub-skill begins."
- **Row Count Assertion mismatch**: "Declaration Row Count Assertion: [N] rows counted.
  Targeted axis count: [M]. N != M: declaration is not contract-complete. [Identify
  discrepancy]. C-37 FAIL."

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

Write this section as the first section of your output report. All seven rows must have
equal depth: three independently-verifiable sub-observables in the Observable Output column.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A: normal / Template B: vacuous) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns populated; (2) Filter Log Resolution block: template letter named and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any structured section with no results; (2) template type and first clause cited in compliance checklist for each fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log entries, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | (1) Step 1 table with F-ID A, F-ID B, Surface similarity columns; (2) Step 2 table with Verdict and Reason columns; (3) Step 3 declaration: compounding patterns named, or empty-state template citing every Step 2 pair and verdict |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, seven rows, three observables each) + Structural Compliance Checklist (last section, sub-claim architecture for multi-part rows) | (1) Structural Axis Declaration: this section, before any execution; (2) Structural Compliance Checklist: final section, all multi-part rows use sub-claim decomposition with fired/partial/not-fired per sub-claim; binary verdict for multi-part row is a structural violation; (3) evidence column in checklist cites actual section names and counts, not template text |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration (vocabulary glossary) + T-1 rule (if-and-only-if, before execution) + five per-scope gate tables with STRUCTURAL Disposition column (primary T-1 record) + T-1 ANNEX (summary aggregator only -- must cite per-scope records) | (1) OBSERVATIONAL DISCIPLINE section: genre named with vocabulary glossary (at least four terms); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables -- schema: Obs #, What was noticed, Disposition, T-1 reason, Filter rule -- Disposition column is structural; (3) T-1 ANNEX: characterizes itself as summary aggregator; names at least one withheld-T1 by scope and reason, citing per-scope record by scope name |
| Execution-order axis | C-36 | EXECUTION ORDER GATE (before Observational Discipline): Layer Completion Record with status column; gate signal written after step 3; Execution Log Layer column as second verifier | (1) EXECUTION ORDER GATE section present: Layer Completion Record with Platform {trace-state, trace-contract, trace-permissions} and Domain {flow-lifecycle, flow-conversation} rows with Status column; (2) gate signal written after step 3 before step 4 naming all three platform sub-skills as complete; (3) Execution Log Layer column: Platform rows 1-3, Domain rows 4-5 -- ordering verifiable independently of gate signal |
| Declaration-completeness-proof axis | C-37 | Row Count Assertion block immediately below this table: row count [7] stated, seven targeted axes listed, 1:1 invariant declared; Compliance Checklist C-37 row verifies count, list, and mapping | (1) Row Count Assertion block present immediately below this table: row count stated as [7]; lists all seven targeted axes; declares 7 == 7; (2) targeted axis list names exactly the seven axes in this table -- no axis absent, no axis extra; (3) Compliance Checklist C-37 row verifies count via sub-claims: sub-claim 1 confirms row count, sub-claim 2 confirms axis list completeness, sub-claim 3 confirms 1:1 mapping holds |

**Row Count Assertion** (write this block immediately after the table above):

> This declaration contains [7] rows. Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) Execution-order axis, (7) Declaration-completeness-proof axis.
> Row count [7] == targeted axis count [7]: declaration is contract-complete.
> Every targeted axis has exactly one row; no row represents an untargeted axis.

If the count does not match: apply Row Count Assertion mismatch template.

---

**EXECUTION ORDER GATE**

Write immediately after the Structural Axis Declaration and before OBSERVATIONAL DISCIPLINE.

**C-36 constraint**: Platform Layer (trace-state, trace-contract, trace-permissions) must
ALL be recorded as "complete" before any Domain Layer sub-skill advances beyond "pending."

| Layer | Sub-Skill | Position | Status | Completion marker |
|-------|-----------|----------|--------|------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- holds until all Platform rows = complete] | |
| Domain | flow-conversation | 5 | [pending -- holds until all Platform rows = complete] | |

After completing position 3, before beginning position 4, write:

> EXECUTION ORDER GATE: Platform Layer complete. trace-state: complete. trace-contract:
> complete. trace-permissions: complete. Domain Layer may begin.

If any platform sub-skill was not complete before a domain sub-skill began: apply the
Execution Order Gate -- domain started before platform complete empty-state template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition: passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- Disposition: failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- Disposition: passed T-1 but failed a filter rule

**T-1 threshold rule** (before any sub-skill fires): Elevated if and only if names a
specific spec location AND describes a gap or violation causing incorrect implementation.

**Per-scope Disposition rule**: Each gate table has Disposition column as primary T-1 record.
If zero withheld-T1 for a scope: apply T-1 SCOPE RECALIBRATION immediately.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by scope name. No new
evidence.

---

**EXECUTION SEQUENCE**

1. trace-state       [PLATFORM LAYER]
2. trace-contract    [PLATFORM LAYER]
3. trace-permissions [PLATFORM LAYER]
   [Write EXECUTION ORDER GATE signal here before step 4]
4. flow-lifecycle    [DOMAIN LAYER -- begins only after gate signal]
5. flow-conversation [DOMAIN LAYER]

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

If zero withheld-T1: apply Per-scope Disposition zero withheld-T1 template immediately.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

Filter rules: (1) no specific spec location; (2) no blast radius; (3) style preference;
(4) duplicates a higher-blast finding.

---

**FILTER LOG RESOLUTION**

Template A or Template B. T-1 ANNEX immediately after.

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs |
|-----------|-------|--------|------------|---------|-------------|
| trace-state | Platform | executed / no findings | | | |
| trace-contract | Platform | executed / no findings | | | |
| trace-permissions | Platform | executed / no findings | | | |
| flow-lifecycle | Domain | executed / no findings | | | |
| flow-conversation | Domain | executed / no findings | | | |

---

**RANKED FINDINGS** / **CROSS-SKILL COMPARISON PROTOCOL** (Steps 1, 2, 3)

[Standard sections -- apply empty-state templates as applicable]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

**Sub-claim architecture rule**: Multi-part rows must use `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section] | [total obs, rejection counts by rule] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX -- total, example, per-scope source; Sub-claim 3: T-1 ANNEX as summary | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates | [sections that fired] | [template type and first clause] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section] | Sub-claim 1: Step 1 present; Sub-claim 2: Step 2 present; Sub-claim 3: Step 3 present | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: seven rows present; Sub-claim 2: each row has three sub-observables; Sub-claim 3: section before any execution | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope sections] + T-1 ANNEX | Sub-claim 1: genre + vocabulary glossary; Sub-claim 2: T-1 if-and-only-if stated; Sub-claim 3: Disposition column in all five per-scope gates | fired / partial [name failing sub-claim] / not fired |
| Execution-order gate (C-36) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: EXECUTION ORDER GATE section present before OBSERVATIONAL DISCIPLINE -- cite section position; Sub-claim 2: gate signal present after step 3 naming all three platform sub-skills as complete -- quote gate signal; Sub-claim 3: Execution Log Layer column shows Platform rows 1-3 and Domain rows 4-5 -- cite each sub-skill name, position, and Layer value | fired / partial [name failing sub-claim] / not fired |
| Declaration completeness proof (C-37) | Structural Axis Declaration (Row Count Assertion) | Sub-claim 1: Row Count Assertion block present below declaration table -- row count stated as [7]; Sub-claim 2: targeted axis list names all seven axes exactly as they appear in the table -- list all seven and confirm each matches a table row; Sub-claim 3: 1:1 invariant holds -- row count [7] equals targeted axis count [7]; no targeted axis absent, no row without a targeted axis | fired / partial [name failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (with Row Count Assertion block) >
EXECUTION ORDER GATE > Observational Discipline > Execution Sequence (trace-state [1],
trace-contract [2], trace-permissions [3], gate signal, flow-lifecycle [4], flow-conversation
[5]; each with per-scope gate table) > Candidate Observations and Filter Log > Filter Log
Resolution (Template A or B + T-1 ANNEX) > Findings Table > Execution Log > Ranked
Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural commitments:
1. Row Count Assertion: 7 rows, 7 targeted axes, 7 == 7 declared (C-37)
2. EXECUTION ORDER GATE: Platform Layer complete before Domain Layer begins; gate signal
   written after step 3; Execution Log Layer column as second verifier (C-36)
3. Per-scope Disposition column in all five gate tables (C-25)
4. T-1 ANNEX as summary aggregator only (C-25)
5. Sub-claim decomposition in checklist for all multi-part rows (C-24)
6. Seven structural axis rows with equal depth before any execution evidence (C-22)

---

## V-05 -- Full Integration: All Six R7-R9 Criteria (C-32 + C-33 + C-34 + C-35 + C-36 + C-37)

**Variation axis:** Role sequence + full integration -- R9 V-05 base (nine axes, carrying
C-32, C-33, C-34, C-35, and all essential criteria) extended with two new structural axes:
execution-order (C-36) and declaration-completeness-proof (C-37). Execution order is
trace-first as in R9 V-05, but now enforced by a dedicated EXECUTION ORDER GATE section
with a Layer Completion Record. The declaration gains a Row Count Assertion block asserting
eleven rows for eleven targeted axes. The Compliance Checklist gains two new rows.

**What this variation adds vs R9 V-05:**
- C-36: EXECUTION ORDER GATE section (new) with Layer Completion Record, gate signal between
  step 3 and step 4, and Execution Log Layer column -- making trace-first ordering an
  independently verifiable structural commitment with its own checklist row
- C-37: Row Count Assertion block (new) immediately below the declaration table -- stating
  row count [11], listing all eleven targeted axes by name, declaring the 1:1 invariant;
  Compliance Checklist C-37 row verifies count, list, and mapping
- Declaration: eleven rows (nine from R9 V-05 plus execution-order and declaration-
  completeness-proof)

**Hypothesis:** All six R7-R9 aspirational criteria pass. C-32: three-point DR-NN chain
verified by checklist sub-claims. C-33: eleven axis rows -- base five plus six quality-axis
additions. C-34: four structured section types guarded by named empty-state templates. C-35:
typed Conf rationale for all Tier 1 and Tier 2 findings. C-36: EXECUTION ORDER GATE signal
names all three platform sub-skills complete; Execution Log Layer column provides independent
second verification. C-37: Row Count Assertion asserts 11 == 11 with named axis list;
checklist verifies 1:1 mapping via sub-claims.

---

Simulate the technical behavior of: {{topic}}

This report enforces eleven structural axes simultaneously. The first section declares all
eleven axes with a Row Count Assertion proving completeness. The last section verifies all
eleven fired using sub-claim decomposition for multi-part axes. Both sections are written
by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave
any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: revisit candidate list. Either (a) name
  at least one observation that should be rejected, or (b) justify that every candidate is
  genuinely anchored to a named spec location and scoped to at least one downstream component."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  was considered and failed T-1, or confirm scope clean and state why T-1 did not fire."
- **T-1 ANNEX RECALIBRATION (zero T-1 rejections across all scopes)**: "T-1 ANNEX: Zero
  withheld-T1 rows across all five per-scope Disposition logs. T-1 RECALIBRATION REQUIRED:
  Either identify a withheld-T1 observation in any scope, or confirm all scopes clean."
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
- **Execution Order Gate -- domain started before platform complete**: "EXECUTION ORDER GATE
  VIOLATION: Domain Layer sub-skill [name] began before Platform Layer completion was
  recorded. C-36 FAIL: Retroactive re-examination of [domain sub-skill] findings required --
  dependency rules DR-01 through DR-[N] may have been undeclared when those findings were
  evaluated."
- **Row Count Assertion mismatch**: "Declaration Row Count Assertion: [N] rows counted.
  Targeted axis count: [M]. N != M: declaration is not contract-complete. [Identify
  discrepancy]. C-37 FAIL."

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
                    Tier 3 and Tier 4 findings are exempt.]
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

Write this section as the first section of your output report. Eleven rows -- one per
targeted quality axis. All eleven rows must have equal depth: three independently-verifiable
sub-observables in the Observable Output column.

C-33 self-extension rule: the base five axes are supplemented by one row per quality axis
targeted by this simulation. This simulation targets C-29/C-32 (propagation + DR-NN),
C-30/C-35 (confidence + rationale), C-31 (type-verb), C-34 (full empty-state), C-36
(execution-order), and C-37 (declaration-completeness-proof). Each produces one additional
axis row beyond the base five. A fixed-depth template without these six rows satisfies C-22
but fails C-33.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations and Filter Log table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter named with rejection count; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state base axis | C-11 | Per-section templates for sub-skill, ranked-tier, comparison, execution log, and Disposition sections | (1) Template text in any empty section; (2) template type and first clause in compliance checklist per fired section; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, execution log, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings, verdicts, patterns | (1) Step 1 table with F-ID A, F-ID B, Surface similarity; (2) Step 2 table with Verdict and Reason; (3) Step 3: pattern or empty-state template citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, eleven rows) + Compliance Checklist (last section, sub-claim architecture) | (1) This declaration: eleven rows before any execution; (2) Compliance Checklist: last section, sub-claim decomposition for all multi-part rows; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator) | (1) OBSERVATIONAL DISCIPLINE: genre with vocabulary glossary (four terms), T-1 rule as if-and-only-if; (2) five per-scope gates with Disposition column (structural); (3) T-1 ANNEX: summary aggregator, names at least one withheld-T1 by scope and reason |
| DR-NN citation chain axis | C-29, C-32 | Cross-Skill Dependency Map (DR-NN at declaration) + Coverage Gate (DR-NN in Rule ID column) + Finding Dep rule cite (DR-NN closes three-point chain) | (1) Dependency map: each rule assigned DR-NN at declaration; range DR-01 through DR-[N] stated; (2) Coverage Gate: each row's Rule ID (DR-NN) column cites exactly the DR-NN from the map; (3) each finding with Dep rule cite populated names a DR-NN matching both map and gate -- three-point chain verifiable by set membership |
| Confidence stratification + rationale axis | C-30, C-35 | Confidence field (HIGH/LOW) + typed Conf rationale ("HIGH -- [artifact]" or "LOW -- [question]") + Confidence-Stratified Action List (Track 1 / Track 2) | (1) Confidence and typed Conf rationale populated for all Tier 1 and Tier 2 findings; (2) Track 1 and Track 2 present with named labels; each empty track shows action-track-empty template; (3) every Tier 1/Tier 2 Conf rationale follows typed format -- reviewer can verify by locating artifact (HIGH) or checking question answerability (LOW) |
| Type-verb binding axis | C-31 | Classification field (GAP/CONTRADICTION/ASSUMPTION) + Remediation verb constrained by Classification + Remediation Quality Gate table | (1) Classification field populated for all findings: GAP / CONTRADICTION / ASSUMPTION; (2) Remediation verb in vocabulary for each type: GAP -> add/remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm; (3) Remediation Quality Gate table: Verb / Target / Location / Conformance columns with all rows populated |
| Full empty-state coverage axis | C-34 | Empty-state templates for all four structured output sections: action tracks, Coverage Gate, T-1 ANNEX, Entity Coverage Matrix | (1) Action tracks: Track 1 and Track 2 each either contain findings or display action-track-empty template -- no silent absence; (2) Coverage Gate: section present with content rows, or Coverage Gate no-rules template, or Coverage Gate all-covered template; (3) T-1 ANNEX and Entity Coverage Matrix: each present with content or named empty-state template; no section simply absent |
| Execution-order axis | C-36 | EXECUTION ORDER GATE (after Cross-Skill Dependency Map, before Observational Discipline): Layer Completion Record; gate signal written after step 3 stating DR-NN map is fully declared; Execution Log Layer column as second verifier | (1) EXECUTION ORDER GATE section present: Layer Completion Record with Status column; Platform {trace-state, trace-contract, trace-permissions} listed before Domain {flow-lifecycle, flow-conversation}; (2) gate signal written after step 3 before step 4 naming all three platform sub-skills complete and confirming DR-01 through DR-[N] are fully declared before domain finding evaluation begins; (3) Execution Log Layer column: Platform rows in positions 1-3, Domain rows in positions 4-5 -- ordering verifiable independently of gate signal |
| Declaration-completeness-proof axis | C-37 | Row Count Assertion block immediately below this table: row count [11] stated, all eleven targeted axes listed, 1:1 invariant declared | (1) Row Count Assertion block present immediately below this table: row count stated as [11]; targeted axis list names all eleven axes; declares 11 == 11; (2) targeted axis list contains exactly eleven names matching the eleven table rows -- no targeted axis absent, no row without a named targeted axis; (3) Compliance Checklist C-37 row verifies via sub-claims: sub-claim 1 confirms row count [11], sub-claim 2 confirms axis list has [11] entries matching table rows, sub-claim 3 confirms 1:1 mapping holds |

**Row Count Assertion** (write this block immediately after the table above):

> This declaration contains [11] rows. Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state base axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) DR-NN citation chain axis, (7) Confidence stratification + rationale axis,
> (8) Type-verb binding axis, (9) Full empty-state coverage axis,
> (10) Execution-order axis, (11) Declaration-completeness-proof axis.
> Row count [11] == targeted axis count [11]: declaration is contract-complete.
> Every targeted axis has exactly one row; no row represents an untargeted axis.

If the count does not match: apply Row Count Assertion mismatch template.

---

**CROSS-SKILL DEPENDENCY MAP**

Write immediately after the Structural Axis Declaration and before EXECUTION ORDER GATE.
Assign DR-NN at declaration. Rules declared here are the dependency context pre-loaded
before flow sub-skills execute -- the EXECUTION ORDER GATE signal confirms this map is
complete before domain finding evaluation begins.

| DR-NN | Rule | Feeds from scope | Feeds into scope | Why the dependency exists |
|-------|------|-----------------|-----------------|--------------------------|

If fewer than two rules can be declared: apply Coverage Gate no rules template.

---

**EXECUTION ORDER GATE**

Write immediately after the Cross-Skill Dependency Map and before OBSERVATIONAL DISCIPLINE.

**C-36 constraint**: Platform Layer (trace-state, trace-contract, trace-permissions) must
complete before Domain Layer (flow-lifecycle, flow-conversation) begins. The DR-NN
dependency rules declared in the Cross-Skill Dependency Map are the pre-loaded context --
a flow finding evaluated before trace completes is evaluated against an incomplete rule set.

| Layer | Sub-Skill | Position | Status | Completion marker |
|-------|-----------|----------|--------|------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- holds until all Platform = complete] | |
| Domain | flow-conversation | 5 | [pending -- holds until all Platform = complete] | |

After completing position 3, before beginning position 4, write:

> EXECUTION ORDER GATE: Platform Layer complete. trace-state: complete. trace-contract:
> complete. trace-permissions: complete. Dependency rules DR-01 through DR-[N] are fully
> declared. Domain Layer may begin. All flow findings will be evaluated against the
> complete dependency rule set.

If any domain sub-skill began before a platform sub-skill completed: apply Execution Order
Gate -- domain started before platform complete empty-state template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- Disposition: passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- Disposition: failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- Disposition: passed T-1 but failed a filter rule

**T-1 threshold rule** (before any sub-skill fires): Elevated if and only if names a
specific spec location AND describes a gap or violation causing incorrect implementation.

**Per-scope Disposition rule**: Each gate table has Disposition column as primary T-1 record.
If zero withheld-T1 for a scope: apply T-1 SCOPE RECALIBRATION immediately.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by scope name. No new
evidence.

---

**EXECUTION SEQUENCE**

Run in this order (trace before flow -- C-36 platform-first constraint). After each
sub-skill, write its per-scope gate table. Update the Layer Completion Record after each
sub-skill completes. Where a finding instantiates a dependency rule, populate Dep rule cite
with the originating DR-NN.

1. trace-state       -- state transition hand-compilation [PLATFORM LAYER]
2. trace-contract    -- expected vs actual comparison at contract boundaries [PLATFORM LAYER]
3. trace-permissions -- RBAC trace with privilege escalation detection [PLATFORM LAYER]
                        [Write EXECUTION ORDER GATE signal here before step 4]
4. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
                        [DOMAIN LAYER -- begins only after gate signal]
5. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
                        [DOMAIN LAYER]

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|-------------------------------|

Disposition values: `elevated` | `withheld-T1` | `withheld-rule`

If zero withheld-T1: apply Per-scope Disposition zero withheld-T1 template immediately.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

Filter rules: (1) no specific spec location; (2) no blast radius; (3) style preference;
(4) duplicates a higher-blast finding.

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
> - withheld-T1 total across all scopes: [N] (source: [list scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [reason] -- per-scope record
>   in [sub-skill section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

---

**TOPIC ENTITY MANIFEST**

List all entities in scope before synthesis. Each appears in Entity Coverage Matrix with
COVERED / CLEAN / SKIPPED status.

| Entity # | Entity Name | Type (contract / state-machine / permission-boundary / lifecycle-phase) |
|----------|-------------|-------------------------------------------------------------------------|

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Classification | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Confidence | Conf Rationale | Remediation Verb | Target | Location | Conformance |
|------|-----------|---------------|------|--------------|---------|--------|-------------|--------------|-----------|----------------|-----------------|--------|----------|-------------|

---

**EXECUTION LOG**

The Layer column is a second verifier for C-36. Platform rows must appear in positions 1-3;
Domain rows in positions 4-5.

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs |
|-----------|-------|--------|------------|---------|-------------|
| trace-state | Platform | executed / no findings | | | |
| trace-contract | Platform | executed / no findings | | | |
| trace-permissions | Platform | executed / no findings | | | |
| flow-lifecycle | Domain | executed / no findings | | | |
| flow-conversation | Domain | executed / no findings | | | |

---

**ENTITY COVERAGE MATRIX**

| Entity # | Entity Name | Status | Sub-Skills that touched this entity | Notes |
|----------|-------------|--------|-------------------------------------|-------|

Status values: `COVERED` / `CLEAN` / `SKIPPED`

If all entities COVERED or CLEAN with zero SKIPPED: apply Entity Coverage Matrix all-clean
template immediately below the table.

---

**RANKED FINDINGS**

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

---

**CONFIDENCE-STRATIFIED ACTION LIST**

**Track 1 -- Implement Now (HIGH-confidence / HIGH-blast)**

| F-ID | Blast Tier | Conf Rationale (format: HIGH -- [spec artifact]) | Action |
|------|------------|--------------------------------------------------|--------|

If no qualifying findings: apply action-track-empty template.

**Track 2 -- Confirm Spec First (LOW-confidence / HIGH-blast)**

| F-ID | Blast Tier | Conf Rationale (format: LOW -- [interpretive question]) | Action after confirmation |
|------|------------|--------------------------------------------------------|--------------------------|

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

One row per finding. Verb constrained by Classification.

| F-ID | Classification | Verb | Target | Location | Conformance |
|------|---------------|------|--------|----------|-------------|

Verb vocabulary: GAP -> add / remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm.
Out-of-vocabulary Verb = C-31 fail.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Name compounding patterns or apply cross-skill-patterns
empty-state template citing Step 2 pairs and verdicts.

---

**PROPAGATION COVERAGE GATE**

| Rule ID (DR-NN) | Rule (abbreviated) | Coverage Status | Evidence |
|----------------|--------------------|----------------|----------|

Coverage Status: `Covered by [F-ID]` (Dep rule cite in finding must match this DR-NN) or
`OPEN PROPAGATION GAP [DR-NN]` (no finding covers this rule; state why).

Every declared rule must appear. Apply Coverage Gate no rules or Coverage Gate all-covered
template as applicable.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Cite actual section names and evidence from this report.

**Sub-claim architecture rule**: Multi-part rows must use `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL for any multi-part row is a structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [total obs, rejection counts by rule] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter cited (A or B) with rejection count; Sub-claim 2: T-1 ANNEX -- withheld-T1 total, named example with scope + reason, per-scope source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary -- no new evidence | fired / partial [name failing sub-claim] / not fired |
| Empty-state templates (base) | [sections that fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present (pattern or empty-state citing Step 2) | fired / partial [name failing sub-claim] / not fired |
| Structural Axis Declaration (eleven rows) | Structural Axis Declaration | Sub-claim 1: eleven rows present -- name all eleven axis labels; Sub-claim 2: each row has three independently-verifiable sub-observables -- confirm for each; Sub-claim 3: section appears before any execution evidence; Row Count Assertion block present immediately below table | fired / partial [name failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate section names] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural terms named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each by sub-skill name | fired / partial [name failing sub-claim] / not fired |
| DR-NN citation chain (C-32) | Cross-Skill Dependency Map + Propagation Coverage Gate + Findings Table | Sub-claim 1: every map rule has DR-NN at declaration -- cite count and range (DR-01 through DR-[N]); Sub-claim 2: every Coverage Gate row cites DR-NN in Rule ID (DR-NN) column matching the map -- cite row count and each DR-NN; Sub-claim 3: every finding with Dep rule cite populated has DR-NN matching both map row and Coverage Gate row -- cite each F-ID, DR-NN, and confirm three-point match | fired / partial [name failing sub-claim] / not fired |
| Confidence stratification (C-30) | CONFIDENCE-STRATIFIED ACTION LIST + Findings Table | Sub-claim 1: Track 1 present with label "Implement Now (HIGH-confidence / HIGH-blast)"; Sub-claim 2: Track 2 present with label "Confirm Spec First (LOW-confidence / HIGH-blast)"; Sub-claim 3: every HIGH-blast finding in exactly one track -- no finding in both or neither | fired / partial [name failing sub-claim] / not fired |
| Conf rationale typed format (C-35) | Findings Table | Sub-claim 1: every Tier 1 and Tier 2 finding has Conf rationale populated -- cite F-IDs; Sub-claim 2: every HIGH Conf rationale names a locatable spec artifact in format "HIGH -- [artifact name]" -- cite the artifact for each; Sub-claim 3: every LOW Conf rationale states a concrete YES/NO answerable question in format "LOW -- [question]" -- verify question answerability for each | fired / partial [name failing sub-claim] / not fired |
| Type-verb binding (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: all findings have Classification populated -- cite count per type (GAP/CONTRADICTION/ASSUMPTION); Sub-claim 2: all Remediation verbs in-vocabulary for Classification -- cite each F-ID, Classification, Verb, verdict (in-vocab / out-of-vocab); Sub-claim 3: Remediation Quality Gate present with all four columns populated | fired / partial [name failing sub-claim] / not fired |
| Full empty-state coverage (C-34) | CONFIDENCE-STRATIFIED ACTION LIST + Propagation Coverage Gate + T-1 ANNEX + Entity Coverage Matrix | Sub-claim 1: action tracks -- Track 1 and Track 2 each contain findings or display action-track-empty template; cite which tracks fired template; Sub-claim 2: Coverage Gate present with content rows, Coverage Gate no-rules, or Coverage Gate all-covered template; cite which applies; Sub-claim 3: T-1 ANNEX and Entity Coverage Matrix each present with content or named empty-state template; cite which template fired for each if any | fired / partial [name failing sub-claim] / not fired |
| Execution-order gate (C-36) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: EXECUTION ORDER GATE section present after Cross-Skill Dependency Map and before OBSERVATIONAL DISCIPLINE -- cite its position; Sub-claim 2: gate signal present after step 3 before step 4 naming all three platform sub-skills (trace-state, trace-contract, trace-permissions) as complete and confirming DR-01 through DR-[N] fully declared -- quote gate signal or cite section name; Sub-claim 3: Execution Log Layer column shows trace-state, trace-contract, trace-permissions in positions 1-3 (Layer = Platform) and flow-lifecycle, flow-conversation in positions 4-5 (Layer = Domain) -- confirm ordering verifiable from this column independently of the gate signal | fired / partial [name failing sub-claim] / not fired |
| Declaration completeness proof (C-37) | Structural Axis Declaration (Row Count Assertion block) | Sub-claim 1: Row Count Assertion block present immediately after declaration table -- cite first sentence; row count stated as [11]; Sub-claim 2: targeted axis list names all eleven axes exactly as they appear in the table -- list all eleven names and confirm each matches a table row label; Sub-claim 3: 1:1 invariant holds -- row count [11] equals targeted axis count [11]; every targeted axis has a row; no row represents an untargeted axis -- confirm by naming any potential discrepancy and resolving it | fired / partial [name failing sub-claim] / not fired |

If a mechanism is marked "partial," the failing sub-claim is named inline in the Status
column. If "not fired," apply the compliance-checklist-not-fired template.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (with Row Count Assertion block) >
Cross-Skill Dependency Map > EXECUTION ORDER GATE > Observational Discipline > Execution
Sequence (trace-state [1], trace-contract [2], trace-permissions [3], gate signal,
flow-lifecycle [4], flow-conversation [5]; each with per-scope gate table) > Topic Entity
Manifest > Candidate Observations and Filter Log > Filter Log Resolution (Template A or B +
T-1 ANNEX) > Findings Table > Execution Log > Entity Coverage Matrix > Ranked Findings
(Tiers 1-2) > Confidence-Stratified Action List (Track 1 and Track 2) > Ranked Findings
(Tiers 3-4) > Remediation Quality Gate > Cross-Skill Comparison Protocol (Steps 1, 2, 3) >
Propagation Coverage Gate > Structural Compliance Checklist.

Structural commitments that must hold in every report:
1. Row Count Assertion block asserts 11 rows for 11 targeted axes; 11 == 11; 1:1 mapping
   verified in checklist sub-claims (C-37)
2. EXECUTION ORDER GATE records Platform Layer complete before Domain Layer begins; gate
   signal names all three platform sub-skills and confirms DR-NN map fully declared;
   Execution Log Layer column provides independent second verification (C-36)
3. DR-NN appears in exactly three places per rule: map declaration, Coverage Gate row,
   finding Dep rule cite -- three-point chain verified in checklist (C-32)
4. Eleven axis rows in declaration, each extended from base five by six quality-axis
   additions, each with three sub-observables (C-33)
5. Four section types guarded by named empty-state templates: action tracks, Coverage Gate,
   T-1 ANNEX, Entity Coverage Matrix -- no silent absence (C-34)
6. Typed Conf rationale for all Tier 1 and Tier 2 findings (C-35)
7. Every HIGH-blast finding in exactly one of Track 1 or Track 2 (C-30)
8. Every finding has Classification; Remediation verb in-vocabulary for that type (C-31)
9. Per-scope Disposition column in all five sub-skill gate tables (C-25)
10. T-1 ANNEX as summary aggregator only (C-25)
11. Sub-claim decomposition in compliance checklist for all multi-part rows (C-24)
