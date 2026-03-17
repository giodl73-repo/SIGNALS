---
skill: campaign-simulate
round: 11
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v10-2026-03-17.md
---

# campaign-simulate -- Round 11 Variations

**Context**: R10 V-05 satisfies C-38 (three-path gate: Layer Completion Record status column +
explicit gate signal + Execution Log Layer column), C-39 (dual-property gate signal certifying
execution order AND DR-NN map completeness), and C-40 (self-referential Row Count Assertion
naming the C-37 axis in its own enumerated list). All three R10 aspirational criteria are
established in the pool (32 total). R11 target: push each ceiling one step further. V-01 extends
C-38 by adding a DR-NN Contributed column to the Layer Completion Record -- dependency map
attribution becomes traceable to individual sub-skills without reading the dependency map section.
V-02 extends C-39 by decomposing the gate signal into named P1/P2 properties with per-sub-skill
DR attribution, closing a scope-attribution gap that C-39's range assertion cannot detect. V-03
extends C-40 by placing the self-reference as the opening sentence of the Row Count Assertion
block, making the self-referential property verifiable by reading only the first sentence. V-04
combines V-01 and V-02 with mutual cross-reference: gate signal P2 cites the Layer Completion
Record column by name. V-05 integrates all three extensions on the R10 V-05 eleven-axis base.

**Under rubric v10**: aspirational pool 32 criteria, capped at 10 pts. Max score 100.
R10 V-05 estimated ~97. R11 V-05 targets the same criteria with enriched mechanisms for the
C-38/C-39/C-40 axes; scoring round will reveal whether any new patterns warrant C-41+.

**Round 11 axes chosen:**
- Single-axis: V-01 (output format -- DR-NN Contributed column extends C-38 machine-readability
  to per-sub-skill dependency attribution), V-02 (phrasing register -- P1/P2 named-property
  decomposition extends C-39 dual certification to per-sub-skill scope attribution),
  V-03 (phrasing register -- Row Count Assertion self-reference as opening sentence extends
  C-40 to opening-sentence verifiability)
- Combined: V-04 (output format + phrasing register -- DR-NN column + P1/P2 gate signal;
  gate signal P2 cites "Layer Completion Record column DR-NN Contributed" by name)
- Full integration: V-05 (all three extensions on R10 V-05 eleven-axis base; SAD preserved
  at eleven rows; execution-order axis, DR-NN chain axis, and completeness-proof axis
  descriptions enriched with the new patterns)

---

## V-01 -- DR-NN Contributed Column in Layer Completion Record (C-38 Extension)

**Variation axis:** Output format -- the Layer Completion Record gains a "DR-NN Contributed"
column. Each Platform sub-skill row populates this column with the DR-NN identifiers of every
dependency rule declared during its execution. Domain sub-skill rows carry "n/a." This creates
a fourth structural verification path for C-38: a reviewer can confirm dependency map completeness
from the Layer Completion Record alone by scanning the column -- no cross-reference to the
dependency map section required. The three original C-38 paths (Layer Completion Record status
column, explicit gate signal, Execution Log Layer column) are preserved unchanged; the DR-NN
column is additive. C-32 is not co-targeted: dependency rules are declared in the column but
not tracked through the full three-point citation chain. C-37 and C-40 are not targeted: no
Row Count Assertion.

**Hypothesis:** C-38 passes via the original three paths. The DR-NN Contributed column adds a
fourth path producing a new verifiability property: per-sub-skill dependency rule attribution
without reading the dependency map. Scoring will reveal whether this fourth path is recognized
as a distinct mechanism or absorbed into C-38's existing verifiability ceiling.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six
axes. The last section verifies all six fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

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
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows across all five per-scope
  Disposition logs. T-1 RECALIBRATION REQUIRED: Either identify a withheld-T1 observation in
  any scope, or confirm all scopes are clean and state what this implies about spec completeness."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but
  did not produce observable output in this report. Reason: [why]. Impact: [whether omission
  affects any findings]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer completion was recorded. C-36 FAIL: trace-state,
  trace-contract, and trace-permissions must all appear as complete before any domain sub-skill
  begins. Retroactive re-examination of [domain sub-skill] findings required."
- **DR-NN Contributed zero from Platform sub-skill**: "DR-NN Contributed ([sub-skill]): Zero
  rules declared. DEPENDENCY SCOPE RECALIBRATION: [sub-skill] must declare at least one
  cross-skill dependency rule during Platform Layer execution. Either (a) identify a constraint
  from this sub-skill's findings that restricts domain-layer evaluation and name the domain scope
  it constrains, or (b) confirm this sub-skill produced no findings and explain why no dependency
  rules are derivable from a clean execution."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only -- FAILURE: merging Impact into Summary]
Impact:         [STANDALONE FIELD: what breaks if unresolved]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Remediation:    [REQUIRED HERE: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only
this section must be able to (a) predict every structural section in the report, (b) verify
each axis independently, and (c) identify the exact schema of each gate table. All six rows
must have equal depth: three independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any section with no results; (2) template type and first clause cited in compliance checklist; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, Disposition zero-withheld-T1 |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1 table: F-ID A, F-ID B, Surface similarity; (2) Step 2 table: Verdict and Reason; (3) Step 3: compounding patterns named or empty-state template citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (sub-claim architecture) | (1) Structural Axis Declaration before any execution; (2) Compliance Checklist as final section with sub-claim decomposition; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator) | (1) genre named with vocabulary glossary (four terms minimum); T-1 rule stated as if-and-only-if; (2) five per-scope gate tables: Obs #, What was noticed, Disposition, T-1 reason, Filter rule; (3) T-1 ANNEX: characterizes itself as summary aggregator, names withheld-T1 example by scope, cites per-scope source |
| Execution-order axis | C-36, C-38 | EXECUTION ORDER GATE before Observational Discipline: Layer Completion Record with Status AND DR-NN Contributed columns; gate signal citing column total; Execution Log Layer column | (1) Layer Completion Record: Status and DR-NN Contributed columns populated; all three Platform rows show "complete" with DR-NN IDs or zero-template before Domain rows advance; (2) gate signal after position 3: names all three Platform sub-skills as complete AND cites DR-NN Contributed column total; (3) Execution Log Layer column: Platform rows in positions 1-3, Domain rows in positions 4-5 |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration and before
OBSERVATIONAL DISCIPLINE.

**C-36 constraint**: Platform Layer sub-skills (trace-state, trace-contract, trace-permissions)
must ALL be recorded as "complete" before any Domain Layer sub-skill advances beyond "pending."

**DR-NN Contributed column**: As each Platform sub-skill executes, populate its DR-NN
Contributed cell with the IDs of every dependency rule it declared. Domain rows carry "n/a."
A reviewer summing this column obtains the full dependency rule count without reading the
dependency map section. If a Platform sub-skill contributes zero rules, apply the
DR-NN Contributed zero template before writing the gate signal.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | DR-NN Contributed | Completion Marker |
|-------|-----------|----------|--------|--------------------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | [DR-NN IDs, or "pending", or apply zero-template] | [e.g., "gate table written, N obs"] |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | [DR-NN IDs, or "pending", or apply zero-template] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | [DR-NN IDs, or "pending", or apply zero-template] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until all Platform rows = complete] | n/a | |
| Domain | flow-conversation | 5 | [pending -- must not start until all Platform rows = complete] | n/a | |

After completing position 3 and before beginning position 4, write this gate signal:

> EXECUTION ORDER GATE: Platform Layer complete.
> trace-state: complete. trace-contract: complete. trace-permissions: complete.
> Dependency rules -- see Layer Completion Record column DR-NN Contributed:
> Platform total [N] rules. Domain Layer may begin.
> Cross-skill dependency context is fully populated for domain finding evaluation.

If any Platform sub-skill was not complete before a domain sub-skill began: apply the
Execution Order Gate violation template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE, before the Execution Sequence.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed filter rule 1-4; enters filter log with rule citation

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would cause
incorrect implementation behavior.

**Per-scope Disposition rule**: Each per-scope gate table includes a Disposition column as the
primary record of T-1 application. If zero withheld-T1 rows appear: apply T-1 SCOPE
RECALIBRATION immediately below that gate table.

**T-1 ANNEX role (summary aggregator only)**: Aggregates withheld-T1 records from all five
per-scope tables. Not a primary evidence source. Must cite per-scope records by scope name.

---

**EXECUTION SEQUENCE**

Run sub-skills in trace-first order. Platform Layer (positions 1-3) completes before Domain
Layer (positions 4-5). Update the Layer Completion Record DR-NN Contributed column after each
Platform sub-skill.

1. trace-state       -- state transition hand-compilation with preconditions, postconditions,
                        invariants
2. trace-contract    -- expected vs actual output comparison at contract boundaries
3. trace-permissions -- RBAC path trace with privilege escalation detection
   [Write EXECUTION ORDER GATE signal here -- all Platform rows must show "complete"]
4. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
5. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

If zero withheld-T1 rows: apply Per-scope Disposition zero withheld-T1 template before advancing.

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
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [N]: [reason]). Gate
> operating normally.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED:
> [apply template text].

**T-1 ANNEX** (required immediately after):

> T-1 ANNEX (summary of per-scope Disposition: withheld-T1 records -- not new evidence):
> - withheld-T1 total: [N] (source: per-scope Disposition columns in [scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [reason] -- per-scope record in
>   [section name]
> - Scopes with zero withheld-T1: [list, or "none"]
> [If zero total: apply T-1 ANNEX RECALIBRATION template]

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
empty-state template citing every Step 2 pair and verdict.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section. Cite actual section names and evidence.

**Sub-claim architecture rule**: Multi-part rows must use `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section name] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section name] | Sub-claim 1: template letter (A or B) cited with rejection count; Sub-claim 2: T-1 ANNEX present -- total cited, named example with scope + reason, per-scope source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary | fired / partial [failing sub-claim] / not fired |
| Empty-state templates | [list sections where template fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | [section name] | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present | fired / partial [failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate sections by sub-skill name] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each scope by sub-skill name | fired / partial [failing sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 extension) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record present with Status AND DR-NN Contributed columns -- all three Platform rows show "complete" with DR-NN IDs or zero-template before Domain rows advance; Sub-claim 2: gate signal written after position 3, names all three Platform sub-skills AND cites DR-NN Contributed column total by name; Sub-claim 3: Execution Log Layer column present for all five sub-skills in correct order (Platform 1-3, Domain 4-5) -- verify by column scan | fired / partial [failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first: positions 1-3 Platform, gate signal, positions
4-5 Domain) > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) >
Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol > Structural
Compliance Checklist.

---

## V-02 -- P1/P2 Gate Signal Decomposition with Per-Sub-Skill DR Attribution (C-39 Extension)

**Variation axis:** Phrasing register -- the gate signal is restructured into two explicitly
named properties, P1 and P2, each independently verifiable. P1 certifies execution order: lists
all three Platform sub-skills by name with their completion status. P2 certifies dependency map
completeness with per-sub-skill attribution: names each Platform sub-skill alongside the DR-NN
IDs it contributed, with a running total confirmed by addition (N1 + N2 + N3 = N_total). This
closes a scope-attribution gap C-39 cannot detect: a sub-skill that declares DR-NN rules from
the wrong scope (e.g., trace-state declaring permission rules belonging to trace-permissions)
would appear complete in a range assertion ("DR-01 through DR-06 declared") but its attribution
mismatch would be visible in P2's per-sub-skill listing. C-38 is preserved via the standard
three-path structure. C-32 is co-targeted (DR-NN chain throughout). C-37 and C-40 not targeted.

**Hypothesis:** C-39 passes via the P1/P2 gate signal (both properties certified). The per-
sub-skill attribution in P2 additionally produces a scope-attribution property that C-39 does
not require but may merit its own criterion. Scoring will reveal whether the attribution
breakdown is absorbed into C-39 or recognized as a distinct mechanism.

---

Simulate the technical behavior of: {{topic}}

This report enforces seven structural axes simultaneously. The first section declares all seven
axes. The last section verifies all seven fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: revisit candidate list. Either (a) name
  at least one observation that should be rejected, or (b) justify every candidate is genuinely
  anchored to a named spec location."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  failed T-1, or confirm scope is clean and state why T-1 did not fire."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows across all five scopes.
  T-1 RECALIBRATION REQUIRED: Either identify a withheld-T1 observation, or confirm all scopes
  are clean."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but produced no observable output.
  Reason: [why]. Impact: [whether omission affects findings]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer completion was recorded. C-36 FAIL. Retroactive
  re-examination required."
- **Propagation Coverage Gate no gaps**: "Propagation Coverage Gate: [N] dependency rules
  declared (DR-01 through DR-[N]). All [N] rules accounted for. DR-NN to F-NN map: [list].
  No OPEN PROPAGATION GAPSs."
- **Propagation Coverage Gate no rules**: "Dependency map produced zero dependency rules.
  DEPENDENCY MAP RECALIBRATION REQUIRED."

---

**FINDING SCHEMA**

All fields required.

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
Dep rule cite:  [DR-NN if this finding instantiates a dependency rule; "none" otherwise]
Remediation:    [REQUIRED HERE: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count; (3) filter rules 1-4 listed before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template text in any empty section; (2) template type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1 table: F-ID A, F-ID B, Surface similarity; (2) Step 2 table: Verdict, Reason; (3) Step 3: patterns named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, seven rows) + Structural Compliance Checklist (sub-claim architecture) | (1) SAD before any execution; (2) Checklist as final section with sub-claim decomposition; (3) evidence column cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables + T-1 ANNEX | (1) genre named with four-term glossary; T-1 if-and-only-if rule stated; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated, example cited |
| DR-NN citation chain axis | C-32 | Every dependency rule carries DR-NN ID at three points: (1) map declaration, (2) Coverage Gate row, (3) finding Dep rule cite field | (1) Cross-Skill Dependency Map: each rule row has DR-NN ID, source sub-skill, constraint text; (2) Coverage Gate row for each DR-NN citing its ID; (3) every finding that instantiates a rule has DR-NN in Dep rule cite -- verify: {map DR-NNs} == {gate rows union gap log entries} |
| Execution-order axis | C-36, C-38, C-39 | EXECUTION ORDER GATE: Layer Completion Record with Status column; P1/P2 gate signal; Execution Log Layer column | (1) Layer Completion Record: Status column -- all three Platform rows "complete" before Domain rows advance; (2) gate signal after position 3: P1 names all three Platform sub-skills as complete; P2 names per-sub-skill DR-NN attribution with addition confirmation (N1 + N2 + N3 = N_total); (3) Execution Log Layer column: Platform 1-3, Domain 4-5 |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration.

**C-36 constraint**: Platform Layer sub-skills must ALL complete before any Domain Layer
sub-skill begins.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|--------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | [state when complete] |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until all Platform rows = complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until all Platform rows = complete] | |

After completing position 3 and before beginning position 4, write this gate signal:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE: All DR-NN rules declared, per-sub-skill:
>   - trace-state contributed: [list DR-NN IDs, N1 rules]
>   - trace-contract contributed: [list DR-NN IDs, N2 rules]
>   - trace-permissions contributed: [list DR-NN IDs, N3 rules]
>   Total: DR-01 through DR-[N], [N_total] rules. N1 + N2 + N3 = [N_total] confirmed.
> Domain Layer may begin. Cross-skill dependency context is fully populated.

If a Platform sub-skill contributed zero rules: note "0 rules" in P2 for that sub-skill and
provide the dependency scope recalibration rationale inline.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed filter rule 1-4

**T-1 threshold rule**: An observation is elevated if and only if it names a specific spec
location AND describes a gap or violation causing incorrect implementation behavior.

**Per-scope Disposition rule**: Disposition column is the primary T-1 record at each scope.
Zero withheld-T1 rows triggers T-1 SCOPE RECALIBRATION immediately below that table.

**T-1 ANNEX role**: Summary aggregator only. Must cite per-scope source records by scope name.

---

**EXECUTION SEQUENCE**

Run sub-skills in trace-first order. After each Platform sub-skill, update the Layer Completion
Record and register dependency rules in the Cross-Skill Dependency Map.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual at each interface
3. trace-permissions -- RBAC path trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (co-located with each sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

---

**CROSS-SKILL DEPENDENCY MAP**

Populate this section during Platform Layer execution (positions 1-3). Each Platform sub-skill
adds rows for every cross-skill constraint its findings declare. Domain sub-skills do not add
rows.

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

**DR-NN assignment rule**: Assign DR-NN IDs sequentially (DR-01, DR-02, ...) in the order
rules are declared during execution. Do not reassign IDs once assigned.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules**: (1) No spec location nameable; (2) No blast radius estimable;
(3) Style preference; (4) Duplicate of higher-blast finding.

---

**FILTER LOG RESOLUTION**

**Template A:** > Filter gate applied. [N] evaluated. [M] rejected. Gate operating normally.

**Template B:** > Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX**:

> T-1 ANNEX (summary aggregator -- not new evidence):
> - Total withheld-T1: [N] (source scopes: [list])
> - Example: [Sub-skill, Obs #] withheld because [reason] -- per-scope record in [section]
> - Zero-withheld scopes: [list or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|---------------|-------------|

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

**RANKED FINDINGS**

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

[Apply ranked-tier empty-state template for any empty tier]

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |

**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |

**Step 3**: Name compounding patterns or apply empty-state template.

---

**COVERAGE GATE**

Verify all declared DR-NN rules are accounted for. Apply Propagation Coverage Gate empty-state
template if zero gaps or zero rules.

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section] | [observations, rejection counts per rule] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter with count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary only | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections fired] | [type and first clause each] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 present | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: seven rows present; Sub-claim 2: three observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: glossary with two cited labels; Sub-claim 2: T-1 if-and-only-if before execution; Sub-claim 3: per-scope Disposition columns for all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain axis (C-32) | Cross-Skill Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: each map row has DR-NN ID -- cite count; Sub-claim 2: each Coverage Gate row cites DR-NN -- cite {map IDs} == {gate rows union gap log}; Sub-claim 3: each finding that instantiates a rule has DR-NN in Dep rule cite column -- cite any finding with DR-NN backlink | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 extension) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record present -- all three Platform rows "complete" before Domain rows advance (Status column); Sub-claim 2: gate signal uses P1/P2 format -- P1 names three Platform sub-skills; P2 names per-sub-skill DR attribution with N1 + N2 + N3 = N_total addition confirmation; Sub-claim 3: Execution Log Layer column present; Platform 1-3, Domain 4-5 by column scan | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table >
Execution Log > Ranked Findings > Cross-Skill Comparison Protocol > Coverage Gate > Structural
Compliance Checklist.

---

## V-03 -- Self-Reference as Opening Sentence in Row Count Assertion (C-40 Extension)

**Variation axis:** Phrasing register -- the Row Count Assertion block opens with an explicit
self-reference sentence before the axis enumeration. The opening sentence states: "This Row Count
Assertion is itself C-37's completeness proof and appears as the final axis in the enumerated
list below." The enumeration then follows, ending with "Declaration-completeness-proof axis (this
block)." This makes the self-referential property verifiable by reading only the first sentence,
without scanning the entire list to find the C-37 axis. C-40 requires (1) the Row Count Assertion
to enumerate axes by name and (2) the C-37 axis to appear in that list -- V-03's innovation is
making property (2) explicit in the opening rather than discoverable only through list inspection.
C-36, C-38, C-39, C-32 not targeted: no EXECUTION ORDER GATE section, no DR-NN chain.

**Hypothesis:** C-40 passes by construction via the opening sentence. The self-reference is
verifiable by reading the first sentence alone, not by scanning the list. Scoring will reveal
whether "verifiable from the opening sentence" is recognized as a distinct property above C-40's
"verifiable by name inspection."

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six
axes with a Row Count Assertion immediately following. The last section verifies all six fired.

---

**EMPTY-STATE TEMPLATES**

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected.
  RECALIBRATION REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows. RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Comparison cannot
  proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list]."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but produced no observable output.
  Reason: [why]. Impact: [effect on findings]."
- **Row Count Assertion mismatch**: "Row Count Assertion MISMATCH: Table contains [actual] rows.
  Targeted axis count is [expected]. Missing axis: [name]. Row Count Assertion FAIL: C-37 cannot
  pass until every targeted axis has exactly one row in this declaration."

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
Remediation:    [REQUIRED HERE: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only this
section must be able to predict every structural section in the report, verify each axis
independently, and identify the schema of each gate table before reading any execution.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count; (3) filter rules 1-4 listed before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template text in any empty section; (2) template type and first clause in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1 table: F-ID A, F-ID B, Surface similarity; (2) Step 2 table: Verdict, Reason; (3) Step 3: patterns named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows) + Structural Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist as final section with sub-claim decomposition; (3) evidence column cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables + T-1 ANNEX | (1) genre named with four-term glossary; T-1 if-and-only-if; (2) five per-scope Disposition tables; (3) T-1 ANNEX as summary aggregator |
| Declaration-completeness-proof axis | C-37, C-40 | Row Count Assertion block immediately below this table: opens with explicit self-reference sentence naming this axis as the final enumerated item; enumerates all six axes by name ending with this axis | (1) Row Count Assertion first sentence states: "This Row Count Assertion is itself C-37's completeness proof and appears as the final axis listed below"; (2) enumerated list names all six axes ending with "Declaration-completeness-proof axis (this block)"; (3) Compliance Checklist C-37/C-40 row: sub-claim 1 verifies first sentence present and names this axis; sub-claim 2 verifies axis list ends with this axis by name; sub-claim 3 confirms 1:1 count |

**Row Count Assertion** (write this block immediately after the table above):

> This Row Count Assertion is itself C-37's completeness proof and appears as the final axis
> listed below. (C-40 self-reference: the proof names itself as one of the items it is proving
> complete.)
> This declaration contains [6] rows. Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) Declaration-completeness-proof axis (this Row Count Assertion block).
> Row count [6] == targeted axis count [6]: declaration is contract-complete.
> Self-reference confirmed by first sentence: the Declaration-completeness-proof axis names
> itself as item (6) in the list it is proving complete.

If the count does not match: apply the Row Count Assertion mismatch empty-state template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed filter rule 1-4

**T-1 threshold rule**: Elevated if and only if it names a specific spec location AND describes
a gap or violation causing incorrect implementation behavior.

**Per-scope Disposition rule**: Disposition column is the primary T-1 record. Zero withheld-T1
triggers RECALIBRATION immediately below.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by name.

---

**EXECUTION SEQUENCE**

Run sub-skills in trace-first order (Platform positions 1-3 before Domain positions 4-5).
No formal EXECUTION ORDER GATE section in this variation.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary comparison
3. trace-permissions -- RBAC path trace
4. flow-lifecycle    -- lifecycle trace with exception flows
5. flow-conversation -- conversation simulation with dead-end detection

**Per-scope gate table** (co-located with each sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules**: (1) No spec location; (2) No blast radius; (3) Style preference;
(4) Duplicate.

---

**FILTER LOG RESOLUTION**

**Template A:** > Filter gate applied. [N] evaluated. [M] rejected. Gate operating normally.
**Template B:** > Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX**:
> T-1 ANNEX (summary aggregator):
> - Total withheld-T1: [N] (sources: [scope names])
> - Example: [Sub-skill, Obs #] withheld because [reason] -- record in [section]
> - Zero-withheld scopes: [list or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

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

**RANKED FINDINGS**

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

[Apply ranked-tier empty-state template for any empty tier]

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |

**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |

**Step 3**: Name compounding patterns or apply empty-state template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section] | [observations, rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter with count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: six rows present; Sub-claim 2: three observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: glossary with two cited labels; Sub-claim 2: T-1 if-and-only-if before execution; Sub-claim 3: Disposition columns for all five scopes | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof (C-37 + C-40 extension) | Row Count Assertion block | Sub-claim 1: first sentence explicitly names "Declaration-completeness-proof axis" and states it appears in the list below -- cite first sentence verbatim; Sub-claim 2: axis list ends with "Declaration-completeness-proof axis (this block)" by name -- confirm by name inspection of final list item; Sub-claim 3: row count [6] equals targeted axis count [6]; 1:1 confirmed | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (including Row Count Assertion block
immediately below the table) > Observational Discipline > Execution Sequence (five sub-skills,
trace-first) > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) >
Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol > Structural
Compliance Checklist.

---

## V-04 -- DR-NN Column + P1/P2 Gate Signal with Mutual Cross-Reference (C-38 + C-39 Extension)

**Variation axis:** Output format + phrasing register combined -- V-01's DR-NN Contributed
column in the Layer Completion Record is merged with V-02's P1/P2 gate signal format. The
mutual cross-reference is the new mechanism: gate signal P2 explicitly cites "see Layer
Completion Record column DR-NN Contributed" for its completeness evidence, instead of
restating the DR-NN range. A reviewer can verify P2 either from the gate signal directly
(the per-sub-skill attribution) or by scanning the Layer Completion Record column (the
independent column total). The two mechanisms are mutually reinforcing: the column enables
independent verification of P2; P2 provides the per-sub-skill attribution the column
summarizes. Both C-32 and C-36 are co-targeted; C-39 activates and is satisfied by P2's
dual-property certification; C-37 and C-40 not targeted.

**Hypothesis:** C-38 passes via the original three paths plus the DR-NN column (fourth path).
C-39 passes via the P1/P2 dual-property gate signal. The mutual cross-reference (P2 citing the
column) creates an additional verification property: the two mechanisms can be triangulated
against each other. Scoring will reveal whether this triangulation is recognized as distinct
from having either mechanism alone.

---

Simulate the technical behavior of: {{topic}}

This report enforces seven structural axes simultaneously. The first section declares all seven.
The last section verifies all seven using sub-claim decomposition for multi-part axes.

---

**EMPTY-STATE TEMPLATES**

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected.
  RECALIBRATION REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows. RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns. Step 2 pairs: [list]."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but no observable output. Reason:
  [why]. Impact: [effect]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer complete. C-36 FAIL. Retroactive re-examination required."
- **DR-NN Contributed zero from Platform sub-skill**: "DR-NN Contributed ([sub-skill]): Zero
  rules. DEPENDENCY SCOPE RECALIBRATION: Either identify a cross-skill constraint, or confirm
  clean execution with explanation."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] rules declared, all accounted for.
  DR-NN to F-NN map: [list]. No OPEN PROPAGATION GAPSs."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules declared.
  DEPENDENCY MAP RECALIBRATION REQUIRED."

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
Dep rule cite:  [DR-NN if instantiates a dependency rule; "none" otherwise]
Remediation:    [REQUIRED HERE: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections: sub-skill, ranked tiers, comparison steps, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings, verdicts, pattern declaration | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns or empty-state template |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (seven rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist final with sub-claim decomposition; (3) evidence column cites actual names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope Disposition tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Three-point chain: map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint text; (2) Coverage Gate rows cite DR-NN IDs; (3) finding Dep rule cite fields backlink to map; {map IDs} == {gate rows union gap log} |
| Execution-order axis | C-36, C-38, C-39 | Layer Completion Record with Status AND DR-NN Contributed columns; P1/P2 gate signal with P2 citing column by name; Execution Log Layer column | (1) Layer Completion Record: Status and DR-NN Contributed columns; Platform 1-3 complete before Domain 4-5 advance; (2) P1/P2 gate signal: P1 names three Platform sub-skills; P2 gives per-sub-skill attribution AND cites "Layer Completion Record column DR-NN Contributed" as the verification source; N1 + N2 + N3 = N_total confirmed; (3) Execution Log Layer column: Platform 1-3, Domain 4-5 by column scan |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration.

**Layer Completion Record** (updated after each Platform sub-skill executes):

| Layer | Sub-Skill | Position | Status | DR-NN Contributed | Completion Marker |
|-------|-----------|----------|--------|--------------------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | [DR-NN IDs or "pending" or zero-template] | [state when complete] |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | [DR-NN IDs or "pending" or zero-template] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | [DR-NN IDs or "pending" or zero-template] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | n/a | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | n/a | |

After completing position 3 and before position 4, write this gate signal:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE (see Layer Completion Record column DR-NN Contributed):
>   - trace-state contributed: [DR-NN IDs, N1 rules] -- confirmed in Layer Completion Record row 1
>   - trace-contract contributed: [DR-NN IDs, N2 rules] -- confirmed in Layer Completion Record row 2
>   - trace-permissions contributed: [DR-NN IDs, N3 rules] -- confirmed in Layer Completion Record row 3
>   - Column total: N1 + N2 + N3 = [N_total] rules. DR-01 through DR-[N] declared.
>   - Verification: sum DR-NN Contributed column (rows 1-3) to confirm independently.
> Domain Layer may begin.

If any Platform sub-skill was not complete before a domain sub-skill began: apply the
Execution Order Gate violation template.

---

**OBSERVATIONAL DISCIPLINE**

**Genre declaration**: Pre-implementation simulation findings document.
Vocabulary (minimum four terms):
- "Candidate observation" -- spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND filter rules
- "withheld-T1" -- failed T-1; primary per-scope record
- "withheld-rule" -- passed T-1, failed filter rule

**T-1 threshold rule**: Elevated if and only if it names a specific spec location AND describes
a gap causing incorrect implementation behavior.

**Per-scope Disposition rule**: Disposition column is primary T-1 record. Zero withheld-T1
triggers RECALIBRATION.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by name.

---

**EXECUTION SEQUENCE**

Trace-first order. Update Layer Completion Record and Cross-Skill Dependency Map after each
Platform sub-skill.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation: dead-end and loop detection

**Per-scope gate table**:

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

---

**CROSS-SKILL DEPENDENCY MAP**

Populate during Platform Layer execution.

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules**: (1) No spec location; (2) No blast radius; (3) Style; (4) Duplicate.

---

**FILTER LOG RESOLUTION**

**Template A:** > Filter gate applied. [N] evaluated. [M] rejected. Gate operating normally.
**Template B:** > Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX**:
> T-1 ANNEX (summary aggregator -- not new evidence):
> - Total withheld-T1: [N] (sources: [list scopes])
> - Example: [Sub-skill, Obs #] withheld because [reason] -- record in [section]
> - Zero-withheld scopes: [list or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|---------------|-------------|

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

**RANKED FINDINGS**

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

[Apply ranked-tier empty-state template for any empty tier]

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |

**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |

**Step 3**: Name compounding patterns or apply empty-state template.

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section] | [observations, counts per rule] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: seven rows; Sub-claim 2: three observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: glossary two labels cited; Sub-claim 2: T-1 if-and-only-if before execution; Sub-claim 3: Disposition columns all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows have DR-NN IDs with source sub-skill; Sub-claim 2: Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings with dependency rules have DR-NN in Dep rule cite | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 + mutual cross-reference) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record present with Status AND DR-NN Contributed columns; Platform 1-3 complete before Domain advance; Sub-claim 2: P1/P2 gate signal: P1 names three Platform sub-skills; P2 cites "Layer Completion Record column DR-NN Contributed" by name AND gives per-sub-skill attribution with N1 + N2 + N3 = N_total; Sub-claim 3: Execution Log Layer column; Platform 1-3, Domain 4-5; reviewer can verify from column without reading gate signal | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table >
Execution Log > Ranked Findings > Cross-Skill Comparison Protocol > Coverage Gate > Structural
Compliance Checklist.

---

## V-05 -- Full Integration: All Three Extensions on R10 V-05 Eleven-Axis Base

**Variation axis:** Role sequence + output format + phrasing register combined -- builds on
the R10 V-05 eleven-axis base (C-32 + C-33 + C-34 + C-35 + C-36 + C-37) and integrates all
three R11 extensions: (1) DR-NN Contributed column in the Layer Completion Record from V-01;
(2) P1/P2 gate signal with per-sub-skill attribution and mutual cross-reference from V-04;
(3) self-reference as opening sentence in the Row Count Assertion from V-03. The SAD is
preserved at eleven rows; the execution-order axis row description is enriched to mention the
DR-NN column and P1/P2 format; the DR-NN citation chain axis row description is enriched to
mention per-sub-skill attribution; the declaration-completeness-proof axis row description is
enriched with the opening-sentence self-reference pattern. No new rows are added: the three
extensions are mechanism enrichments within existing axes.

**Hypothesis:** All criteria through C-40 pass. The three enriched mechanisms produce new
observable properties (fourth C-38 path via DR-NN column; scope-attribution traceability via
P1/P2 per-sub-skill breakdown; opening-sentence verifiability of C-40 self-reference) that
scoring will assess. If any new property is recognized as a distinct mechanism in the scoring
round, the pattern becomes a candidate for C-41+.

---

Simulate the technical behavior of: {{topic}}

This report enforces eleven structural axes simultaneously. The first section declares all
eleven axes with a self-referential Row Count Assertion immediately following. The last section
verifies all eleven fired using sub-claim decomposition for multi-part axes. Both sections are
written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected.
  RECALIBRATION REQUIRED: revisit candidate list. Either (a) name at least one observation that
  should be rejected, or (b) justify every candidate is genuinely anchored to a spec location."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: name one observation that failed
  T-1, or confirm scope is clean."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows. T-1 RECALIBRATION REQUIRED:
  identify a withheld-T1 observation or confirm all scopes clean."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Comparison cannot
  proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list and
  verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but produced no observable output.
  Reason: [why]. Impact: [effect on findings]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer complete. C-36 FAIL. Retroactive re-examination required."
- **DR-NN Contributed zero from Platform sub-skill**: "DR-NN Contributed ([sub-skill]): Zero
  rules. DEPENDENCY SCOPE RECALIBRATION: Either identify a cross-skill constraint or confirm
  clean execution with explanation."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] dependency rules declared
  (DR-01 through DR-[N]). All accounted for. DR-NN to F-NN map: [list]. No OPEN PROPAGATION
  GAPSs."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED."
- **Confidence stratification track empty**: "Action track [HIGH/LOW-confidence HIGH-blast]:
  No findings assigned. Schema: F-ID | Summary | Blast Radius | Confidence | Conf rationale."
- **Row Count Assertion mismatch**: "Row Count Assertion MISMATCH: Table contains [actual] rows.
  Targeted axis count is [expected]. Missing axis: [name]. C-37 FAIL."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE FIELD: what breaks if unresolved]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Confidence:     [HIGH / LOW -- required for cross-skill and system-wide findings]
Conf rationale: [REQUIRED if Confidence present: basis for HIGH or LOW judgment]
Dep rule cite:  [DR-NN if instantiates a dependency rule; "none" otherwise]
Remediation:    [Verb constrained by Type: GAP -> "add"/"remove"; CONTRADICTION -> "resolve";
                 ASSUMPTION -> "confirm"; REQUIRED: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. An evaluator reading only this
section must be able to (a) predict every structural section, (b) verify each axis independently
from its named sub-observables, and (c) identify each gate table schema before reading any
execution. All eleven rows must have equal depth: three independently-verifiable sub-observables.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count; (3) filter rules 1-4 listed before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section empty-state templates for all section types; named templates for zero-content structured sections; silent sections prohibited | (1) Named template text in any section with no results; (2) template type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, action tracks, Coverage Gate, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns named or empty-state template citing all Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (eleven rows, three observables each) + Compliance Checklist (sub-claim architecture for multi-part rows) | (1) SAD before any execution evidence; (2) Checklist as final section with sub-claim decomposition; binary verdict = structural violation; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator only) | (1) genre named with four-term glossary; T-1 if-and-only-if rule stated before any sub-skill; (2) five per-scope gate tables: Obs #, What was noticed, Disposition, T-1 reason, Filter rule; Disposition column is primary T-1 record; (3) T-1 ANNEX: characterizes itself as summary aggregator; names withheld-T1 example by scope, cites per-scope source |
| DR-NN citation chain axis | C-32 | Three-point chain: (1) map declaration, (2) Coverage Gate row, (3) finding Dep rule cite field; per-sub-skill attribution in P2 of gate signal | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint text; {map IDs} set declared; (2) Coverage Gate: every DR-NN cited; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite fields backlink map IDs; per-sub-skill attribution confirmed in gate signal P2 (N1 + N2 + N3 = N_total) |
| Confidence stratification axis | C-30, C-35 | Action list split into two named tracks by confidence x blast quadrant; Conf rationale field per finding | (1) Track 1: HIGH-confidence / HIGH-blast -- implement immediately; (2) Track 2: LOW-confidence / HIGH-blast -- confirm spec interpretation first; (3) each Track 1 / Track 2 finding has Conf rationale sub-field: "HIGH/LOW -- [falsifiable basis]" not "HIGH/LOW" alone |
| Type-verb binding axis | C-31 | Finding type declared at detection (GAP / CONTRADICTION / ASSUMPTION); remediation Verb constrained: GAP -> add/remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm | (1) every finding carries Type declaration before remediation Verb is written; (2) remediation Verb vocabulary matches Type in every row: GAP rows use add/remove; CONTRADICTION rows use resolve; ASSUMPTION rows use confirm; (3) any out-of-vocabulary Verb causes row-level Type mis-bind declaration in compliance checklist |
| Propagation coverage axis | C-29 | Coverage Gate: every DR-NN either honored in a finding or logged as OPEN PROPAGATION GAP | (1) Coverage Gate table: DR-ID, Status (honored/OPEN), Finding ID(s), Gap Reason; (2) all declared DR-NNs appear in either honored finding or gap log; none silently dropped; (3) gap log entries carry DR-NN ID and reason |
| Execution-order axis | C-36, C-38, C-39 | EXECUTION ORDER GATE: Layer Completion Record with Status AND DR-NN Contributed columns; P1/P2 gate signal (P2 cites column by name + per-sub-skill attribution); Execution Log Layer column | (1) Layer Completion Record: Status and DR-NN Contributed columns populated; Platform 1-3 complete before Domain 4-5 advance; (2) P1/P2 gate signal: P1 names all three Platform sub-skills; P2 cites "Layer Completion Record column DR-NN Contributed" AND per-sub-skill attribution (N1 + N2 + N3 = N_total); (3) Execution Log Layer column: Platform 1-3, Domain 4-5; verify by column scan independent of gate signal |
| Declaration-completeness-proof axis | C-37, C-40 | Row Count Assertion block immediately below this table: opens with explicit self-reference sentence naming this axis; enumerates all eleven axes by name ending with this axis | (1) Row Count Assertion first sentence: "This Row Count Assertion is itself C-37's completeness proof and appears as the final axis listed below" -- verifiable from first sentence alone; (2) enumerated list names all eleven axes with Declaration-completeness-proof axis as final item; (3) Compliance Checklist row: sub-claim 1 cites first sentence verbatim; sub-claim 2 confirms final list item matches axis name; sub-claim 3 confirms count 11 == 11 |

**Row Count Assertion** (write this block immediately after the table above):

> This Row Count Assertion is itself C-37's completeness proof and appears as the final axis
> listed below. (C-40 self-reference: the proof names itself as one of the items it is proving
> complete. This property is verifiable from this opening sentence alone.)
> This declaration contains [11] rows. Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) DR-NN citation chain axis, (7) Confidence stratification axis,
> (8) Type-verb binding axis, (9) Propagation coverage axis,
> (10) Execution-order axis,
> (11) Declaration-completeness-proof axis (this Row Count Assertion block).
> Row count [11] == targeted axis count [11]: declaration is contract-complete.
> Self-reference confirmed: the Declaration-completeness-proof axis appears as item (11) --
> the final item -- in the list it is proving complete. Verifiable by reading the final list
> entry and comparing to this axis row by name.

If count does not match: apply the Row Count Assertion mismatch template and identify which
targeted axis lacks a row or which row has no corresponding targeted axis.

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration.

**C-36 constraint**: All three Platform Layer sub-skills must complete before any Domain Layer
sub-skill begins.

**DR-NN Contributed column**: Populate as each Platform sub-skill executes. A reviewer summing
this column obtains the full dependency rule count without reading the Cross-Skill Dependency
Map section (fourth C-38 verification path). If a Platform sub-skill contributes zero rules,
apply the DR-NN Contributed zero template before writing the gate signal.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | DR-NN Contributed | Completion Marker |
|-------|-----------|----------|--------|--------------------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | [DR-NN IDs or "pending" or zero-template] | [e.g., "gate table written, N obs"] |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | [DR-NN IDs or "pending" or zero-template] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | [DR-NN IDs or "pending" or zero-template] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | n/a | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | n/a | |

After completing position 3 and before position 4, write this gate signal:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE (see Layer Completion Record column DR-NN Contributed):
>   - trace-state contributed: [DR-NN IDs, N1 rules] -- see Layer Completion Record row 1
>   - trace-contract contributed: [DR-NN IDs, N2 rules] -- see Layer Completion Record row 2
>   - trace-permissions contributed: [DR-NN IDs, N3 rules] -- see Layer Completion Record row 3
>   - Column total: N1 + N2 + N3 = [N_total]. DR-01 through DR-[N] fully declared.
>   - Verification: sum DR-NN Contributed column (rows 1-3) independently.
> Domain Layer may begin.

If any Platform sub-skill not complete before a domain sub-skill begins: apply the Execution
Order Gate violation template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE.

**Genre declaration**: This report is a pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- observed spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed filter rule 1-4

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if
and only if it names a specific spec location AND describes a gap or violation that would cause
incorrect implementation behavior.

**Per-scope Disposition rule**: Each per-scope gate table includes a Disposition column as the
primary T-1 record. Zero withheld-T1 triggers RECALIBRATION immediately below.

**T-1 ANNEX role (summary aggregator only)**: Aggregates withheld-T1 from all five per-scope
tables. Not primary evidence. Must cite per-scope records by scope name.

---

**EXECUTION SEQUENCE**

Run sub-skills in trace-first order. After each Platform sub-skill: update the Layer Completion
Record DR-NN Contributed column, write per-scope gate table, add dependency rules to the
Cross-Skill Dependency Map.

1. trace-state       -- state transition hand-compilation: preconditions, postconditions,
                        invariants
2. trace-contract    -- contract boundary: expected vs actual output at each interface
3. trace-permissions -- RBAC path trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation: dead-end and loop detection

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

If zero withheld-T1: apply T-1 SCOPE RECALIBRATION before advancing.

---

**CROSS-SKILL DEPENDENCY MAP**

Populate during Platform Layer execution (positions 1-3).

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

Assign DR-NN IDs sequentially in declaration order. Once assigned, IDs are stable.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules**: (1) No spec location; (2) No blast radius; (3) Style preference;
(4) Duplicate of higher-blast finding.

---

**FILTER LOG RESOLUTION**

**Template A:** > Filter gate applied. [N] evaluated. [M] rejected (Rule [N]: [reason]).
> Gate operating normally.

**Template B:** > Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX**:

> T-1 ANNEX (summary aggregator -- not new evidence):
> - Total withheld-T1: [N] (source scopes: [list by sub-skill name])
> - Example: [Sub-skill, Obs #] withheld because [reason] -- per-scope record in [section]
> - Zero-withheld scopes: [list, or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Confidence | Conf Rationale | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|------------|----------------|---------------|-------------|

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

**Step 3 -- Patterns declaration**: Name compounding patterns or apply empty-state template
citing every Step 2 pair.

---

**COVERAGE GATE**

All declared DR-NN rules must appear either in a finding (honored) or in a gap log entry
(OPEN PROPAGATION GAP). Apply empty-state templates for zero rules or zero gaps.

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Assign each HIGH-blast finding to one of two named tracks based on confidence:

**Track 1 -- HIGH-confidence / HIGH-blast** (implement immediately):

| F-ID | Summary | Blast Radius | Confidence | Conf Rationale |
|------|---------|-------------|------------|----------------|

[Apply confidence stratification track empty template if no findings assigned]

**Track 2 -- LOW-confidence / HIGH-blast** (confirm spec interpretation first, then implement):

| F-ID | Summary | Blast Radius | Confidence | Conf Rationale |
|------|---------|-------------|------------|----------------|

[Apply confidence stratification track empty template if no findings assigned]

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section. Cite actual section names and evidence.

**Sub-claim architecture rule**: Multi-part rows must use `fired / partial / not-fired` per
named sub-claim. Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations, rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter (A or B) cited with rejection count; Sub-claim 2: T-1 ANNEX present -- total cited, named example with scope + reason, source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary aggregator | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11 + C-34) | [list every section where a template fired] | [template type and first clause for each fired section, including action track templates if invoked] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: eleven rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate sections by sub-skill name] + T-1 ANNEX | Sub-claim 1: genre declared with glossary -- cite two structural labels; Sub-claim 2: T-1 if-and-only-if rule stated before any sub-skill; Sub-claim 3: per-scope Disposition columns all five scopes -- cite each by sub-skill name | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Cross-Skill Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs with source sub-skill -- cite count; Sub-claim 2: Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; Sub-claim 3: finding Dep rule cite fields backlink to map DR-NNs | fired / partial [sub-claim] / not fired |
| Confidence stratification (C-30, C-35) | Confidence-Stratified Action List + Findings Table | Sub-claim 1: two named tracks present (HIGH-confidence and LOW-confidence); Sub-claim 2: every HIGH-blast finding assigned to a track; Sub-claim 3: every Track 1 and Track 2 finding carries Conf rationale sub-field with falsifiable basis | fired / partial [sub-claim] / not fired |
| Type-verb binding (C-31) | Findings Table | Sub-claim 1: every finding carries Type declaration (GAP / CONTRADICTION / ASSUMPTION); Sub-claim 2: remediation Verb matches Type vocabulary in every row -- cite any row where Verb was verified; Sub-claim 3: no out-of-vocabulary Verb present | fired / partial [sub-claim] / not fired |
| Propagation coverage (C-29) | Coverage Gate | Sub-claim 1: Coverage Gate table present with all DR-NNs from map; Sub-claim 2: every DR-NN accounted for (honored or OPEN GAP); Sub-claim 3: gap log entries carry DR-NN ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 + C-38 extension + mutual cross-reference) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record with Status AND DR-NN Contributed columns -- Platform 1-3 complete with DR-NN IDs or zero-template before Domain advance; Sub-claim 2: P1/P2 gate signal -- P1 names three Platform sub-skills; P2 cites "Layer Completion Record column DR-NN Contributed" by name AND per-sub-skill attribution with N1 + N2 + N3 = N_total; Sub-claim 3: Execution Log Layer column; Platform 1-3, Domain 4-5 by column scan | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof (C-37 + C-40 + opening-sentence extension) | Row Count Assertion block | Sub-claim 1: first sentence of Row Count Assertion states self-reference explicitly and names "Declaration-completeness-proof axis" -- cite first sentence verbatim; Sub-claim 2: enumerated list ends with "Declaration-completeness-proof axis (this Row Count Assertion block)" as final named item -- confirm by inspecting final list item; Sub-claim 3: row count [11] equals targeted axis count [11]; 1:1 confirmed by name; no targeted axis absent, no extra row | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (including Row Count Assertion block
immediately below the table) > EXECUTION ORDER GATE > Observational Discipline > Execution
Sequence (eleven-axis trace-first: positions 1-3 Platform, gate signal P1+P2, positions 4-5
Domain) > Cross-Skill Dependency Map > Candidate Observations and Filter Log > Filter Log
Resolution (with T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings > Cross-Skill
Comparison Protocol > Coverage Gate > Confidence-Stratified Action List > Structural
Compliance Checklist.

If all sections are empty: apply sub-skill no findings templates for all five scopes; apply
findings table empty template; apply ranked-tier empty-state templates for all four tiers;
apply comparison step with no pairs template; apply both confidence stratification track
empty templates; apply all Coverage Gate and Propagation Coverage Gate empty-state templates;
Structural Compliance Checklist must still fire for all eleven mechanisms.
