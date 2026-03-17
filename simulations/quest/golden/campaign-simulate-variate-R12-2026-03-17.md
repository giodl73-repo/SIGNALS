---
skill: campaign-simulate
round: 12
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v11-2026-03-17.md
---

# campaign-simulate -- Round 12 Variations

**Context**: R11 extracted three new criteria: C-41 (gate signal P1/P2 decomposition with
per-sub-skill DR-NN attribution), C-42 (Row Count Assertion self-reference as opening sentence),
and C-43 (Execution Log DR-NN Contributed column as fourth structural path). R11 V-01 achieved
C-43 by adding a DR-NN Contributed column to the **Layer Completion Record** (Platform-only rows).
R11 V-02 achieved C-41 via P1/P2 gate signal. R11 V-03 achieved C-42 via opening-sentence
self-reference. R11 V-05 integrated all three extensions on an 11-axis base but was not formally
scored; its mechanisms were the source for extracting the three new criteria.

**R12 target**: Push each ceiling one step further and confirm all three stack cleanly.

The C-43 rubric text specifies the DR-NN Contributed column in the **Execution Log** (all five
sub-skills), not only in the Layer Completion Record (Platform-only). R11 V-01 achieved C-43 via
the Layer Completion Record; R12 V-01 targets a more faithful pass by placing the column in the
standard five-row Execution Log, with Domain rows carrying explicit "n/a" entries. V-02 extends
C-41 by adding bidirectional cross-cites: P2 per-sub-skill entries cite the Execution Log row for
independent verification, creating a closed loop between the gate signal and the Execution Log.
V-03 extends C-42 by embedding the count inline in the opening sentence ("the 6th and final of
6"), making the C-37 count invariant verifiable from the opening sentence alone without reading
the enumerated list. V-04 combines V-01 and V-02 (Execution Log DR-NN column + P2 cross-cites).
V-05 integrates all three extensions on a 12-axis base, adding a dedicated
"Execution-log attribution axis" row for C-43.

**Under rubric v11**: aspirational pool 35 criteria (C-26 through C-43), capped at 10 pts.
Max score 100.

**Round 12 axes chosen:**
- Single-axis: V-01 (output format -- Execution Log gains DR-NN Contributed column as the
  primary C-43 mechanism, distinct from the Layer Completion Record; Domain rows carry explicit
  "n/a"), V-02 (phrasing register -- P2 per-sub-skill entries cross-cite the Execution Log DR-NN
  Contributed column by row, making P2 bidirectionally verifiable), V-03 (phrasing register --
  Row Count Assertion opening sentence embeds the count inline, making the C-37 count invariant
  verifiable without reading the list or table row count)
- Combined: V-04 (output format + phrasing register -- Execution Log DR-NN column + P2
  cross-cites; gate signal P2 cites "Execution Log, [sub-skill] row, DR-NN Contributed" by name)
- Full integration: V-05 (all three extensions on the R11 V-05 eleven-axis base, promoted to
  twelve axes; new "Execution-log attribution axis" as 12th SAD row declaring C-43 mechanism;
  P2 bidirectional cross-cites; inline-count opening sentence counting to 12)

---

## V-01 -- Execution Log DR-NN Contributed Column (C-43 via Standard Execution Log)

**Variation axis:** Output format -- the standard five-row Execution Log gains a DR-NN
Contributed column. Unlike the Layer Completion Record (which tracks Platform sub-skills only),
the standard Execution Log covers all five sub-skills: Platform rows list the DR-NN IDs
contributed during that sub-skill's execution; Domain rows carry "n/a" with an explicit schema
entry. A reviewer scanning the DR-NN Contributed column of the standard Execution Log can
reconstruct the full dependency map without cross-referencing the Layer Completion Record or
the Cross-Skill Dependency Map section. C-38 is preserved via its three original paths (Layer
Completion Record Status column, gate signal, Execution Log Layer column); the DR-NN Contributed
column is a fourth path added to the standard Execution Log itself, not a column in the Layer
Completion Record. C-32 not co-targeted. C-37 and C-40 not targeted.

**Hypothesis:** C-43 passes more faithfully when the DR-NN Contributed column appears in the
standard Execution Log (all five sub-skills, Domain rows carry "n/a") versus the Layer Completion
Record (Platform-only rows). The standard Execution Log is the natural host: it already carries
the Layer column (C-38's third path); DR-NN Contributed becomes its companion. Domain rows
carrying "n/a" fulfill C-43's zero-contribution template requirement for non-declaring sub-skills.
Scoring will reveal whether the Execution Log placement is recognized as a distinct canonical
mechanism vs. the Layer Completion Record placement used in R11 V-01.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six axes.
The last section verifies all six fired using sub-claim decomposition for multi-part axes. Both
sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations
  evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate
  filtering judgment. Required: revisit candidate list. Either (a) name at least one observation
  that should be rejected under the filter rules, or (b) justify that every candidate is
  genuinely anchored to a named spec location."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that
  failed T-1, or confirm scope is clean and state why T-1 did not fire."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows across all five per-scope
  Disposition logs. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no
  problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for
  pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared
  in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but produced no observable output.
  Reason: [why]. Impact: [effect on findings]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer completion was recorded. C-36 FAIL. Retroactive
  re-examination required."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules declared. DEPENDENCY SCOPE RECALIBRATION: Either identify a
  cross-skill constraint this sub-skill's findings imply, or confirm clean execution and explain
  why no dependency rules are derivable."

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

Write this section as the first section of your output report. An evaluator reading only this
section must be able to (a) predict every structural section in the report, (b) verify each
axis independently, and (c) identify the exact schema of each gate table. All six rows must
have equal depth: three independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count cited; (3) filter rules 1-4 listed before any row is evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections prohibited | (1) Named template text in any section with no results; (2) template type and first clause cited in compliance checklist; (3) sections covered: sub-skill sections, ranked tiers, comparison steps, Disposition zero-withheld-T1, Execution Log Platform zero-contribution |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1 table: F-ID A, F-ID B, Surface similarity; (2) Step 2 table: Verdict and Reason; (3) Step 3: compounding patterns named or empty-state template citing Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (first section, six rows, three observables each) + Structural Compliance Checklist (sub-claim architecture) | (1) Structural Axis Declaration before any execution; (2) Compliance Checklist as final section with sub-claim decomposition; binary verdict = structural violation; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator only) | (1) genre named with four-term glossary; T-1 if-and-only-if rule stated before any sub-skill; (2) five per-scope gate tables: Obs #, What was noticed, Disposition, T-1 reason, Filter rule; (3) T-1 ANNEX: summary aggregator role stated, named withheld-T1 example by scope, per-scope source cited |
| Execution-order and attribution axis | C-36, C-38, C-43 | EXECUTION ORDER GATE: Layer Completion Record with Status column; gate signal citing Execution Log DR-NN Contributed column; Execution Log with Layer column AND DR-NN Contributed column | (1) Layer Completion Record: Status column -- all three Platform rows "complete" before Domain rows advance; (2) gate signal after position 3: names trace-state, trace-contract, trace-permissions as complete AND cites "Execution Log DR-NN Contributed column, rows 1-3" by name as the per-sub-skill attribution source; (3) Execution Log: Layer column (Platform 1-3, Domain 4-5) AND DR-NN Contributed column (Platform rows list contributed DR-NN IDs or zero-template; Domain rows carry "n/a"); union of all Platform DR-NN Contributed entries = full dependency map |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration and before
OBSERVATIONAL DISCIPLINE.

**C-36 constraint**: Platform Layer sub-skills (trace-state, trace-contract, trace-permissions)
must ALL be recorded as "complete" before any Domain Layer sub-skill advances beyond "pending."

**Layer Completion Record** (Status column only -- DR-NN attribution is in the Execution Log):

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | [e.g., "gate table written, N obs"] |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until all Platform rows = complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until all Platform rows = complete] | |

After completing position 3 and before beginning position 4, write this gate signal:

> EXECUTION ORDER GATE: Platform Layer complete.
> trace-state: complete. trace-contract: complete. trace-permissions: complete.
> Dependency rules declared during Platform Layer execution -- see Execution Log, DR-NN
> Contributed column, rows 1-3 for per-sub-skill attribution. Sum rows 1-3 to verify
> total independently. Domain Layer may begin.

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
Layer (positions 4-5). After each Platform sub-skill: update Layer Completion Record Status
column and populate Execution Log DR-NN Contributed entry for that sub-skill row.

1. trace-state       -- state transition hand-compilation: preconditions, postconditions,
                        invariants
2. trace-contract    -- contract boundary: expected vs actual output at each interface
3. trace-permissions -- RBAC path trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

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
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [N]: [reason]).
> Gate operating normally.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX** (required immediately after):

> T-1 ANNEX (summary aggregator -- not new evidence):
> - withheld-T1 total: [N] (source: per-scope Disposition columns in [scope names])
> - Named example: [Sub-skill, Obs #] withheld-T1 because [reason] -- per-scope record in
>   [section name]
> - Scopes with zero withheld-T1: [list, or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

Populate DR-NN Contributed column for each sub-skill row after that sub-skill executes.
Platform rows: list DR-NN IDs contributed, or apply zero-template if no rules declared.
Domain rows: "n/a" (Domain sub-skills do not declare dependency rules).

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NN IDs contributed, or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NN IDs contributed, or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NN IDs contributed, or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

**Union verification**: The union of all DR-NN IDs in Platform rows (rows 1-3) of the
DR-NN Contributed column must equal the complete set of declared dependency rules.
If these sets do not match, cite the discrepancy in the Structural Compliance Checklist.

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
| Filter Log | Candidate Observations and Filter Log | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter (A or B) cited with rejection count; Sub-claim 2: T-1 ANNEX present -- total cited, named example with scope + reason, per-scope source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary aggregator | fired / partial [failing sub-claim] / not fired |
| Empty-state templates | [list every section where template fired] | [template type and first clause for each fired section] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 table present ([N] pairs); Sub-claim 2: Step 2 table present ([N] verdicts); Sub-claim 3: Step 3 declaration present | fired / partial [failing sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: six rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [failing sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate sections by sub-skill name] + T-1 ANNEX | Sub-claim 1: genre declared with vocabulary glossary -- cite two structural labels named; Sub-claim 2: T-1 rule stated as if-and-only-if before any sub-skill fires; Sub-claim 3: per-scope Disposition columns present for all five sub-skills -- cite each scope by sub-skill name | fired / partial [failing sub-claim] / not fired |
| Execution-order and attribution axis (C-36 + C-38 + C-43 via Execution Log) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record Status column shows all three Platform rows "complete" before Domain rows advance; Sub-claim 2: gate signal names all three Platform sub-skills as complete AND cites "Execution Log, DR-NN Contributed column, rows 1-3" by name as attribution source; Sub-claim 3: Execution Log has both Layer column (Platform 1-3, Domain 4-5) AND DR-NN Contributed column (Platform rows list DR-NN IDs or zero-template; Domain rows carry "n/a"); union of rows 1-3 DR-NN Contributed entries = full dependency map -- verify by column scan, no dependency map cross-reference required | fired / partial [failing sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first: positions 1-3 Platform, gate signal, positions
4-5 Domain) > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) >
Findings Table > Execution Log (with DR-NN Contributed column) > Ranked Findings > Cross-Skill
Comparison Protocol > Structural Compliance Checklist.

---

## V-02 -- P2 Sub-Entries Cross-Cite Execution Log Row (C-41 Bidirectional Extension)

**Variation axis:** Phrasing register -- each P2 sub-entry in the gate signal explicitly cross-
cites the corresponding Execution Log row by sub-skill name. P2 currently asserts per-sub-skill
DR-NN attribution as a self-contained statement. The cross-cite turns each assertion into a
pointer: "trace-state contributed DR-01, DR-02 (2 rules) -- cross-verify: Execution Log,
trace-state row, DR-NN Contributed column." A reviewer can verify P2 in two independent ways:
(1) read P2 directly, (2) scan the Execution Log DR-NN Contributed column for the named row.
These paths converge on the same attribution data. The Execution Log must carry a DR-NN
Contributed column for the cross-cite to reference (C-43 is co-activated). C-38, C-39, C-41,
C-32 are co-targeted. C-37, C-40, C-42 not targeted.

**Hypothesis:** C-41 passes via P1/P2 decomposition with per-sub-skill attribution. The
cross-cite in each P2 sub-entry creates a bidirectional verification property: P2 attribution is
falsifiable either by reading P2 or by scanning the Execution Log independently. A mismatch
between P2 and the Execution Log column would be detectable by the cross-cite format. Scoring
will reveal whether bidirectional verifiability is recognized as a distinct mechanism above
C-41's unidirectional attribution ceiling.

---

Simulate the technical behavior of: {{topic}}

This report enforces seven structural axes simultaneously. The first section declares all seven
axes. The last section verifies all seven fired using sub-claim decomposition for multi-part
axes. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] observations evaluated. Zero rejected.
  RECALIBRATION REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Comparison cannot
  proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list and
  verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but no observable output. Reason:
  [why]. Impact: [effect on findings]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer complete. C-36 FAIL. Retroactive re-examination required."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules. DEPENDENCY SCOPE RECALIBRATION: Either identify a cross-skill
  constraint or confirm clean execution with explanation."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] dependency rules declared
  (DR-01 through DR-[N]). All accounted for. DR-NN to F-NN map: [list]. No OPEN PROPAGATION
  GAPS."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules declared.
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
Remediation:    [REQUIRED: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 listed before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, Disposition zero, Execution Log zero-contribution |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (seven rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist final with sub-claim decomposition; (3) evidence column cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if before any sub-skill; (2) five per-scope Disposition tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Three-point chain: map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite fields backlink to map |
| Execution-order axis | C-36, C-38, C-39, C-41, C-43 | Layer Completion Record with Status column; P1/P2 gate signal (P2 sub-entries cross-cite Execution Log DR-NN Contributed column by row); Execution Log with Layer AND DR-NN Contributed columns | (1) Layer Completion Record: Status column -- Platform 1-3 complete before Domain 4-5 advance; (2) P1/P2 gate signal: P1 names trace-state, trace-contract, trace-permissions; P2 per-sub-skill entries cite DR-NN IDs AND cite "Execution Log, [sub-skill] row, DR-NN Contributed" by name; N1 + N2 + N3 = N_total addition confirmed; (3) Execution Log: Layer column (Platform 1-3, Domain 4-5) AND DR-NN Contributed column (Platform rows must match P2 data; Domain "n/a") -- bidirectional match verifiable by column scan without reading P2 |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration.

**C-36 constraint**: All three Platform Layer sub-skills must complete before any Domain Layer
sub-skill begins.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | |

After completing position 3 and before position 4, write this gate signal:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE: All DR-NN rules declared, per-sub-skill attribution:
>   - trace-state contributed: [list DR-NN IDs, N1 rules]
>     cross-verify: Execution Log, trace-state row, DR-NN Contributed column
>   - trace-contract contributed: [list DR-NN IDs, N2 rules]
>     cross-verify: Execution Log, trace-contract row, DR-NN Contributed column
>   - trace-permissions contributed: [list DR-NN IDs, N3 rules]
>     cross-verify: Execution Log, trace-permissions row, DR-NN Contributed column
>   - Total: N1 + N2 + N3 = [N_total] rules. DR-01 through DR-[N] declared.
>   - Bidirectional verification: P2 sub-entries and Execution Log DR-NN Contributed
>     column rows 1-3 must match; a discrepancy between P2 and the column is a
>     dependency map integrity failure.
> Domain Layer may begin.

If a Platform sub-skill contributed zero rules: note "0 rules" in P2 for that sub-skill,
apply the Execution Log zero-contribution template for that row, and provide the scope
recalibration rationale inline.

If any Platform sub-skill was not complete before a domain sub-skill began: apply the
Execution Order Gate violation template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE.

**Genre declaration**: Pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules
- "withheld-T1" -- failed T-1; primary per-scope record
- "withheld-rule" -- passed T-1, failed filter rule 1-4

**T-1 threshold rule**: An observation is elevated if and only if it names a specific
spec location AND describes a gap causing incorrect implementation behavior.

**Per-scope Disposition rule**: Disposition column is primary T-1 record. Zero withheld-T1
triggers RECALIBRATION immediately below.

**T-1 ANNEX role**: Summary aggregator only. Must cite per-scope source records by scope name.

---

**EXECUTION SEQUENCE**

Trace-first order. After each Platform sub-skill: update Cross-Skill Dependency Map and
populate Execution Log DR-NN Contributed column for that sub-skill row.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with cross-cites) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (one per sub-skill, co-located with execution results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

---

**CROSS-SKILL DEPENDENCY MAP**

Populate during Platform Layer execution (positions 1-3).

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

Assign DR-NN IDs sequentially in declaration order. IDs are stable once assigned.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules**: (1) No spec location; (2) No blast radius; (3) Style preference;
(4) Duplicate of higher-blast finding.

---

**FILTER LOG RESOLUTION**

**Template A:** > Filter gate applied. [N] evaluated. [M] rejected. Gate operating normally.

**Template B:** > Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION REQUIRED.

**T-1 ANNEX**:

> T-1 ANNEX (summary aggregator -- not new evidence):
> - Total withheld-T1: [N] (source scopes: [list by sub-skill name])
> - Example: [Sub-skill, Obs #] withheld because [reason] -- per-scope record in [section]
> - Zero-withheld scopes: [list, or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG**

Populate DR-NN Contributed column for each sub-skill row. Platform rows must match the
per-sub-skill attribution stated in P2 of the gate signal. Domain rows carry "n/a."

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

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

Verify all declared DR-NN rules are accounted for. Apply empty-state template if zero
gaps or zero rules.

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section] | [total observations, rule-by-rule rejection counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections fired] | [type and first clause each] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: seven rows; Sub-claim 2: three observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: glossary two labels cited; Sub-claim 2: T-1 if-and-only-if before execution; Sub-claim 3: Disposition columns all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs with source sub-skill -- cite count; Sub-claim 2: Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings with dependency rules cite DR-NN in Dep rule cite | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 + C-41 bidirectional cross-cite + C-43) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record Status column -- Platform 1-3 complete before Domain advance; Sub-claim 2: P1/P2 gate signal -- P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND cite "Execution Log, [sub-skill] row, DR-NN Contributed" by name for each sub-skill; N1 + N2 + N3 = N_total addition confirmed; Sub-claim 3: Execution Log has Layer column (Platform 1-3, Domain 4-5) AND DR-NN Contributed column; Platform rows match P2 per-sub-skill data; Domain rows carry "n/a"; bidirectional match: scan Execution Log column and compare to P2 sub-entries row-for-row | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table >
Execution Log (with DR-NN Contributed column) > Ranked Findings > Cross-Skill Comparison
Protocol > Coverage Gate > Structural Compliance Checklist.

---

## V-03 -- Inline Count in Row Count Assertion Opening Sentence (C-42 Extension)

**Variation axis:** Phrasing register -- the Row Count Assertion opening sentence embeds the
count N inline: "This Row Count Assertion, itself the Nth and final of the N targeted axes
declared below, is C-37's completeness proof." C-42 requires the self-reference to appear in
the opening sentence (the C-37 axis identifiable without scanning the list). This variation
goes one step further: embedding the count in the opening sentence makes the C-37 count
invariant (N rows == N targeted axes) verifiable from the opening sentence alone, without
reading the enumerated list, the table row count, or any other section. C-36 not targeted
(trace-first order enforced but no formal EXECUTION ORDER GATE section). C-37 and C-40
targeted. C-42 targeted (opening-sentence self-reference). Inline count is the new mechanism.

**Hypothesis:** C-42 passes via the opening-sentence self-reference (the C-37 axis is named
and self-referential from the first sentence). The inline count in the opening sentence produces
a new property above C-42: the C-37 count invariant is verifiable from the first sentence alone,
without reading the enumerated list at all. A reviewer seeing "the 6th and final of 6 targeted
axes" in the opening sentence has confirmed both the self-reference (C-42) and the count
invariant (C-37) without reading further. Scoring will reveal whether "count embedded in
opening sentence" is recognized as a distinct mechanism above C-42's "self-reference in opening
sentence" ceiling.

---

Simulate the technical behavior of: {{topic}}

This report enforces six structural axes simultaneously. The first section declares all six axes
with a self-referential Row Count Assertion immediately following. The last section verifies all
six fired. Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

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
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list]."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but produced no observable output.
  Reason: [why]. Impact: [effect on findings]."
- **Row Count Assertion mismatch**: "Row Count Assertion MISMATCH: Opening sentence states
  count [stated]. Table contains [actual] rows. Targeted axis count is [expected].
  Three-way match required: opening sentence count == table row count == enumerated list count.
  Missing axis: [name]. C-37 FAIL."

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

Write this section as the first section of your output report. An evaluator reading only this
section must be able to predict every structural section, verify each axis independently, and
identify each gate table schema before reading any execution evidence.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 listed before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (six rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist final with sub-claim decomposition; (3) evidence column cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if before any sub-skill; (2) five per-scope Disposition tables; (3) T-1 ANNEX as summary aggregator |
| Declaration-completeness-proof axis | C-37, C-40, C-42 | Row Count Assertion block immediately below this table: first sentence embeds count N inline ("the Nth and final of N targeted axes"); enumerates all six axes ending with this axis | (1) Row Count Assertion first sentence: "This Row Count Assertion, itself the [N]th and final of the [N] targeted axes declared below, is C-37's completeness proof" -- count N readable from first sentence alone without reading list or table; (2) enumerated list names all six axes with this axis as final item; (3) Compliance Checklist: sub-claim 1 cites first sentence verbatim and confirms count N is embedded inline; sub-claim 2 confirms three-way match: opening sentence count [N] == table row count [N] == enumerated list item count [N] |

**Row Count Assertion** (write this block immediately after the table above):

> This Row Count Assertion, itself the 6th and final of the 6 targeted axes declared below,
> is C-37's completeness proof. (The count "6" is embedded in this opening sentence: the
> C-37 count invariant -- N rows == N targeted axes -- is verifiable from this sentence alone
> without reading the enumerated list or the table row count.)
> Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) Declaration-completeness-proof axis (this Row Count Assertion block).
> Three-way count match: opening sentence count [6] == table rows [6] == enumerated items [6].
> Declaration is contract-complete. Self-reference confirmed: this block appears as item (6),
> the final item, in the list it is proving complete.

If the count in the opening sentence does not match the table row count or the enumerated list
item count: apply the Row Count Assertion mismatch template.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the Structural Axis Declaration.

**Genre declaration**: Pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules
- "withheld-T1" -- failed T-1; primary per-scope record
- "withheld-rule" -- passed T-1, failed filter rule 1-4

**T-1 threshold rule**: Elevated if and only if it names a specific spec location AND describes
a gap causing incorrect implementation behavior.

**Per-scope Disposition rule**: Disposition column is primary T-1 record. Zero withheld-T1
triggers RECALIBRATION.

**T-1 ANNEX role**: Summary aggregator only. Cites per-scope records by name.

---

**EXECUTION SEQUENCE**

Run sub-skills in trace-first order (Platform 1-3 before Domain 4-5). No formal EXECUTION
ORDER GATE section in this variation.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary comparison
3. trace-permissions -- RBAC path trace
4. flow-lifecycle    -- lifecycle trace with exception flows
5. flow-conversation -- conversation simulation with dead-end detection

**Per-scope gate table** (one per sub-skill, co-located with results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

If zero withheld-T1: apply T-1 SCOPE RECALIBRATION before advancing.

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
> T-1 ANNEX (summary aggregator -- not new evidence):
> - Total: [N] (sources: [scope names])
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
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: six rows; Sub-claim 2: three observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: glossary two labels cited; Sub-claim 2: T-1 if-and-only-if before execution; Sub-claim 3: Disposition columns all five scopes | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof (C-37 + C-40 + C-42 + inline-count extension) | Row Count Assertion block | Sub-claim 1: first sentence of Row Count Assertion contains count N embedded inline in the form "the [N]th and final of [N] targeted axes" -- cite first sentence verbatim and confirm count N matches table row count AND enumerated list count (three-way match required); Sub-claim 2: enumerated list ends with "Declaration-completeness-proof axis (this Row Count Assertion block)" as the final named item -- confirm by inspecting the final list item; Sub-claim 3: three-way count match confirmed: opening sentence count [N] == table rows [N] == enumerated items [N]; any mismatch is a Row Count Assertion MISMATCH fail | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (including Row Count Assertion block
immediately below the table) > Observational Discipline > Execution Sequence (trace-first:
positions 1-3 Platform, positions 4-5 Domain) > Candidate Observations and Filter Log >
Filter Log Resolution (with T-1 ANNEX) > Findings Table > Execution Log > Ranked Findings >
Cross-Skill Comparison Protocol > Structural Compliance Checklist.

---

## V-04 -- Execution Log DR-NN Column + P2 Bidirectional Cross-Cite (C-43 + C-41 Combined)

**Variation axis:** Output format + phrasing register combined -- V-01's Execution Log DR-NN
Contributed column merged with V-02's P2 bidirectional cross-cite format. The Execution Log
carries a DR-NN Contributed column (all five rows; Platform rows list IDs; Domain rows "n/a").
P2's per-sub-skill entries cite both the DR-NN IDs and the Execution Log row by name. A reviewer
can verify the dependency map in three independent ways: (1) read the Cross-Skill Dependency Map,
(2) read P2 in the gate signal, (3) scan the Execution Log DR-NN Contributed column. All three
converge. A mismatch among them signals a dependency map integrity failure. C-38 and C-32 and
C-36 and C-39 and C-41 are co-targeted; C-43 is co-activated. C-37, C-40, C-42 not targeted.

**Hypothesis:** C-41 passes via P1/P2 decomposition with per-sub-skill attribution. C-43 passes
via the Execution Log DR-NN Contributed column. The mutual cross-reference between P2 and the
Execution Log creates a triangulated verification property: three independent paths (dependency
map, P2 gate signal, Execution Log column) must agree. A discrepancy between P2 and the
Execution Log column is now structurally detectable. Scoring will reveal whether this
three-way triangulation is recognized as a distinct mechanism above the bidirectionality
introduced by V-02 alone.

---

Simulate the technical behavior of: {{topic}}

This report enforces seven structural axes simultaneously. The first section declares all seven.
The last section verifies all seven using sub-claim decomposition for multi-part axes. Both
sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

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
- **Cross-skill patterns empty**: "No compounding patterns. Step 2 pairs: [list and verdicts]."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but no observable output. Reason:
  [why]. Impact: [effect]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer complete. C-36 FAIL. Retroactive re-examination required."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules. DEPENDENCY SCOPE RECALIBRATION."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] dependency rules declared
  (DR-01 through DR-[N]). All accounted for. No OPEN PROPAGATION GAPS."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules declared.
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
Dep rule cite:  [DR-NN if instantiates a dependency rule; "none" otherwise]
Remediation:    [REQUIRED: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections: sub-skill, ranked tiers, comparison steps, Disposition zero, Execution Log zero-contribution |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings, verdicts, pattern declaration | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns or empty-state template |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (seven rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist final with sub-claim decomposition; (3) evidence cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope Disposition tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Three-point chain: map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite fields backlink to map |
| Execution-order axis | C-36, C-38, C-39, C-41, C-43 | Layer Completion Record with Status column; P1/P2 gate signal (P2 sub-entries cite DR-NN IDs AND cross-cite Execution Log row by sub-skill name); Execution Log with Layer AND DR-NN Contributed columns | (1) Layer Completion Record: Status column -- Platform 1-3 complete before Domain 4-5 advance; (2) P1/P2 gate signal: P1 names three Platform sub-skills; P2 per-sub-skill entries state DR-NN IDs AND cite "Execution Log, [sub-skill] row, DR-NN Contributed"; N1 + N2 + N3 = N_total; (3) Execution Log: Layer column AND DR-NN Contributed column; Platform rows match P2 data; Domain "n/a"; three-way convergence: Dependency Map == P2 == Execution Log DR-NN column |

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration.

**C-36 constraint**: All three Platform Layer sub-skills must complete before any Domain Layer
sub-skill begins.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | |

After completing position 3 and before beginning position 4, write this gate signal:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE: Per-sub-skill attribution (cross-verify via Execution Log):
>   - trace-state contributed: [list DR-NN IDs, N1 rules]
>     cross-verify: Execution Log, trace-state row, DR-NN Contributed column
>   - trace-contract contributed: [list DR-NN IDs, N2 rules]
>     cross-verify: Execution Log, trace-contract row, DR-NN Contributed column
>   - trace-permissions contributed: [list DR-NN IDs, N3 rules]
>     cross-verify: Execution Log, trace-permissions row, DR-NN Contributed column
>   - Total: N1 + N2 + N3 = [N_total] rules. DR-01 through DR-[N] declared.
>   - Three-way verification: Cross-Skill Dependency Map, P2 sub-entries, and Execution Log
>     DR-NN Contributed column (rows 1-3) must all agree. A discrepancy among the three
>     sources is a dependency map integrity failure.
> Domain Layer may begin.

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

Trace-first order. After each Platform sub-skill: update Cross-Skill Dependency Map AND
populate Execution Log DR-NN Contributed column for that row.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with cross-cites) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (co-located with each sub-skill):

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
> - Total: [N] (sources: [list by sub-skill name])
> - Example: [Sub-skill, Obs #] withheld because [reason] -- record in [section]
> - Zero-withheld scopes: [list or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG**

Populate DR-NN Contributed after each sub-skill executes. Platform rows must match the
attribution stated in P2 of the gate signal. Domain rows carry "n/a."

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

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

Apply empty-state template for zero rules or zero gaps.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | [section] | [total observations, rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | [section] | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections fired] | [type and first clause] | fired / not fired |
| Cross-skill comparison | [section] | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: seven rows; Sub-claim 2: three observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: glossary two labels; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition columns all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs with source; Sub-claim 2: Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings with dependency rules have DR-NN in Dep rule cite | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 + C-41 + C-43 three-way triangulation) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record Status column -- Platform 1-3 complete before Domain advance; Sub-claim 2: P1/P2 gate signal -- P1 names three Platform sub-skills; P2 sub-entries cite DR-NN IDs AND cite "Execution Log, [sub-skill] row, DR-NN Contributed" by name for each; N1 + N2 + N3 = N_total; Sub-claim 3: Execution Log has Layer column AND DR-NN Contributed column; Platform rows match P2 data; Domain rows "n/a"; three-way convergence verified: scan Dependency Map, P2, and Execution Log column -- all three must agree on attributed IDs and sub-skill scope | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table >
Execution Log (with DR-NN Contributed column) > Ranked Findings > Cross-Skill Comparison
Protocol > Coverage Gate > Structural Compliance Checklist.

---

## V-05 -- Full Integration: 12-Axis SAD with Dedicated Execution-Log Attribution Axis

**Variation axis:** Role sequence + output format + phrasing register combined -- builds on the
R11 V-05 eleven-axis base and promotes C-43 from a mechanism enrichment of the execution-order
axis to a dedicated twelfth axis: "Execution-log attribution axis." The new axis makes the
standard Execution Log's DR-NN Contributed column a first-class SAD declaration with its own
three independently-verifiable sub-observables, separate from the execution-order axis that
carries C-36/C-38/C-39/C-41. The three R12 extensions are integrated: (1) Execution Log DR-NN
Contributed column in the standard five-row table (V-01 mechanism); (2) P2 sub-entries cross-
cite the Execution Log row by name for bidirectional verification (V-02 mechanism); (3) Row
Count Assertion opening sentence embeds the count inline -- "the 12th and final of 12 targeted
axes" (V-03 mechanism). The SAD is promoted from eleven to twelve rows; the Row Count Assertion
counts to twelve; the Compliance Checklist gains a new row for the execution-log attribution
axis.

**Hypothesis:** All criteria through C-43 pass simultaneously. The dedicated execution-log
attribution axis converts C-43 from an additive column (mechanism enrichment within C-38's
axis) into a first-class axis with its own SAD declaration and Compliance Checklist row. This
creates a new verifiability property: a reviewer can confirm C-43 from the SAD alone without
reading the Execution Order Gate section. Scoring will reveal whether promoting C-43 to a
dedicated SAD axis is recognized as a distinct mechanism above V-05/R11's axis-enrichment
approach.

---

Simulate the technical behavior of: {{topic}}

This report enforces twelve structural axes simultaneously. The first section declares all
twelve axes with a self-referential Row Count Assertion immediately following. The last section
verifies all twelve fired using sub-claim decomposition for multi-part axes. Both sections are
written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

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
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules. DEPENDENCY SCOPE RECALIBRATION: Either identify a cross-skill
  constraint or confirm clean execution with explanation."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] dependency rules declared
  (DR-01 through DR-[N]). All accounted for. DR-NN to F-NN map: [list]. No OPEN PROPAGATION
  GAPS."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED."
- **Confidence stratification track empty**: "Action track [HIGH/LOW-confidence HIGH-blast]:
  No findings assigned. Schema: F-ID | Summary | Blast Radius | Confidence | Conf rationale."
- **Row Count Assertion mismatch**: "Row Count Assertion MISMATCH: Opening sentence states
  count [stated]. Table contains [actual] rows. Targeted axis count is [expected]. Three-way
  match required: opening sentence count == table row count == enumerated list count.
  Missing axis: [name]. C-37 FAIL."

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
execution evidence. All twelve rows must have equal depth: three independently-verifiable
sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count; (3) filter rules 1-4 listed before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section empty-state templates for all section types; named templates for zero-content structured sections; silent sections prohibited | (1) Named template in any section with no results; (2) type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, action tracks, Coverage Gate, Disposition zero, Execution Log zero-contribution |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns named or empty-state template citing all Step 2 pairs |
| Declaration-compliance axis | C-17, C-18 | Structural Axis Declaration (twelve rows, three observables each) + Compliance Checklist (sub-claim architecture for multi-part rows) | (1) SAD before any execution evidence; (2) Checklist as final section with sub-claim decomposition; binary verdict = structural violation; (3) evidence column cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables with Disposition column + T-1 ANNEX (summary aggregator only) | (1) genre named with four-term glossary; T-1 if-and-only-if rule stated before any sub-skill; (2) five per-scope gate tables: Obs #, What was noticed, Disposition, T-1 reason, Filter rule; (3) T-1 ANNEX: summary aggregator role stated; names withheld-T1 example by scope; cites per-scope source |
| DR-NN citation chain axis | C-32 | Three-point chain: (1) map declaration, (2) Coverage Gate row, (3) finding Dep rule cite field; P2 per-sub-skill attribution cross-cites Execution Log row for bidirectional verification | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint text; {map IDs} set declared; (2) Coverage Gate: every DR-NN cited; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite fields backlink map IDs; P2 per-sub-skill entries cite "Execution Log, [sub-skill] row, DR-NN Contributed" by name |
| Confidence stratification axis | C-30, C-35 | Action list split into two named tracks by confidence x blast quadrant; Conf rationale field per finding | (1) Track 1: HIGH-confidence / HIGH-blast -- implement immediately; (2) Track 2: LOW-confidence / HIGH-blast -- confirm spec interpretation first; (3) each Track 1 / Track 2 finding has Conf rationale sub-field: "HIGH/LOW -- [falsifiable basis]" |
| Type-verb binding axis | C-31 | Finding type declared at detection (GAP / CONTRADICTION / ASSUMPTION); Verb constrained: GAP -> add/remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm | (1) every finding carries Type before Verb is written; (2) Verb matches Type vocabulary in every row; (3) any out-of-vocabulary Verb = row-level Type mis-bind declaration in compliance checklist |
| Propagation coverage axis | C-29 | Coverage Gate: every DR-NN either honored in a finding or logged as OPEN PROPAGATION GAP | (1) Coverage Gate: DR-ID, Status (honored/OPEN), Finding ID(s), Gap Reason; (2) all declared DR-NNs appear in honored finding or gap log; none silently dropped; (3) gap log entries carry DR-NN ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | EXECUTION ORDER GATE: Layer Completion Record with Status column; P1/P2 gate signal (P2 labeled; per-sub-skill attribution with addition confirmation; P2 entries cross-cite Execution Log DR-NN Contributed column); Execution Log Layer column | (1) Layer Completion Record: Status column -- Platform 1-3 complete before Domain 4-5 advance; (2) P1/P2 gate signal: P1 names trace-state, trace-contract, trace-permissions; P2 per-sub-skill entries cite DR-NN IDs AND cite "Execution Log, [sub-skill] row, DR-NN Contributed" by name; N1 + N2 + N3 = N_total confirmed; (3) Execution Log Layer column: Platform 1-3, Domain 4-5; verify by column scan independent of gate signal |
| Execution-log attribution axis | C-43 | Standard five-row Execution Log carries DR-NN Contributed column as a dedicated fourth structural verification path; Platform rows list contributed DR-NN IDs; Domain rows carry "n/a"; union of Platform rows = full dependency map | (1) Execution Log DR-NN Contributed column present in the standard five-row table (not only in Layer Completion Record); Platform rows 1-3 list DR-NN IDs or zero-contribution template; Domain rows 4-5 carry "n/a"; (2) union of DR-NN Contributed entries across rows 1-3 equals the full set of declared DR-NNs -- verifiable by column scan without reading the Cross-Skill Dependency Map section; (3) Compliance Checklist execution-log-attribution row: sub-claim 1 confirms DR-NN Contributed column present in standard Execution Log; sub-claim 2 confirms union of rows 1-3 = dependency map; sub-claim 3 confirms Domain rows carry "n/a" |
| Declaration-completeness-proof axis | C-37, C-40, C-42 | Row Count Assertion block immediately below this table: first sentence embeds count 12 inline ("the 12th and final of 12 targeted axes"); enumerates all twelve axes ending with this axis | (1) Row Count Assertion first sentence: "This Row Count Assertion, itself the 12th and final of the 12 targeted axes declared below, is C-37's completeness proof" -- count 12 readable from first sentence alone; (2) enumerated list names all twelve axes with this axis as the final item; (3) Compliance Checklist: sub-claim 1 cites first sentence verbatim and confirms inline count 12 matches table row count AND enumerated list count (three-way match); sub-claim 2 confirms final list item is "Declaration-completeness-proof axis (this Row Count Assertion block)"; sub-claim 3 confirms 12 == 12 |

**Row Count Assertion** (write this block immediately after the table above):

> This Row Count Assertion, itself the 12th and final of the 12 targeted axes declared below,
> is C-37's completeness proof. (The count "12" is embedded in this opening sentence: the
> C-37 count invariant -- N rows == N targeted axes -- is verifiable from this sentence alone
> without reading the enumerated list or the table row count.)
> Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) DR-NN citation chain axis, (7) Confidence stratification axis,
> (8) Type-verb binding axis, (9) Propagation coverage axis,
> (10) Execution-order axis, (11) Execution-log attribution axis,
> (12) Declaration-completeness-proof axis (this Row Count Assertion block).
> Three-way count match: opening sentence count [12] == table rows [12] == enumerated items [12].
> Declaration is contract-complete. Self-reference confirmed: this block appears as item (12),
> the final item, in the list it is proving complete.

If count in opening sentence does not match table row count or enumerated list count: apply
the Row Count Assertion mismatch template and identify which targeted axis lacks a row or
which row has no corresponding targeted axis.

---

**EXECUTION ORDER GATE**

Write this section immediately after the Structural Axis Declaration.

**C-36 constraint**: All three Platform Layer sub-skills must complete before any Domain Layer
sub-skill begins.

**Layer Completion Record** (Status column -- DR-NN attribution is in the standard Execution
Log, not duplicated here):

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | |

After completing position 3 and before beginning position 4, write this gate signal:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE: Per-sub-skill attribution (cross-verify via Execution Log):
>   - trace-state contributed: [list DR-NN IDs, N1 rules]
>     cross-verify: Execution Log, trace-state row, DR-NN Contributed column
>   - trace-contract contributed: [list DR-NN IDs, N2 rules]
>     cross-verify: Execution Log, trace-contract row, DR-NN Contributed column
>   - trace-permissions contributed: [list DR-NN IDs, N3 rules]
>     cross-verify: Execution Log, trace-permissions row, DR-NN Contributed column
>   - Total: N1 + N2 + N3 = [N_total] rules. DR-01 through DR-[N] declared.
>   - Three-way convergence: Cross-Skill Dependency Map, P2, and Execution Log DR-NN
>     Contributed column (rows 1-3) must all agree. Discrepancy = integrity failure.
> Domain Layer may begin.

If any Platform sub-skill was not complete before a domain sub-skill began: apply the
Execution Order Gate violation template.

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

**Per-scope Disposition rule**: Disposition column is primary T-1 record. Zero withheld-T1
triggers RECALIBRATION immediately below.

**T-1 ANNEX role (summary aggregator only)**: Aggregates withheld-T1 from all five per-scope
tables. Not primary evidence. Must cite per-scope records by scope name.

---

**EXECUTION SEQUENCE**

Trace-first order. After each Platform sub-skill: update the Layer Completion Record Status
column, add dependency rules to the Cross-Skill Dependency Map, and populate the Execution
Log DR-NN Contributed column for that sub-skill row.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual output at each interface
3. trace-permissions -- RBAC path trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with cross-cites) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (one per sub-skill, co-located with results):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

If zero withheld-T1: apply T-1 SCOPE RECALIBRATION before advancing.

---

**CROSS-SKILL DEPENDENCY MAP**

Populate during Platform Layer execution (positions 1-3). Domain sub-skills do not add rows.

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

Assign DR-NN IDs sequentially in declaration order. IDs are stable once assigned.

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

Populate DR-NN Contributed column for each sub-skill after it executes. Platform rows must
match the per-sub-skill attribution stated in P2 of the gate signal. Domain rows carry "n/a."
Union of rows 1-3 DR-NN Contributed entries = full declared dependency map.

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

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
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter (A or B) cited with count; Sub-claim 2: T-1 ANNEX total + example + source cited; Sub-claim 3: T-1 ANNEX characterizes itself as summary aggregator | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11 + C-34) | [every section where template fired] | [template type and first clause for each, including action track and Coverage Gate templates] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twelve rows present; Sub-claim 2: each row has three independently-verifiable observables; Sub-claim 3: section appears before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [five per-scope gate sections] + T-1 ANNEX | Sub-claim 1: genre declared with glossary -- cite two structural labels; Sub-claim 2: T-1 if-and-only-if before any sub-skill; Sub-claim 3: per-scope Disposition columns all five scopes -- cite each by sub-skill name | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Cross-Skill Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs with source sub-skill -- cite count; Sub-claim 2: Coverage Gate rows cite DR-NN IDs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings with dependency rules have DR-NN in Dep rule cite; P2 bidirectional cross-cites verified | fired / partial [sub-claim] / not fired |
| Confidence stratification (C-30, C-35) | Confidence-Stratified Action List + Findings Table | Sub-claim 1: two named tracks present; Sub-claim 2: every HIGH-blast finding assigned to a track; Sub-claim 3: every Track 1 / Track 2 finding carries Conf rationale with falsifiable basis | fired / partial [sub-claim] / not fired |
| Type-verb binding (C-31) | Findings Table | Sub-claim 1: every finding carries Type (GAP / CONTRADICTION / ASSUMPTION); Sub-claim 2: Verb matches Type vocabulary in every row; Sub-claim 3: no out-of-vocabulary Verb present | fired / partial [sub-claim] / not fired |
| Propagation coverage (C-29) | Coverage Gate | Sub-claim 1: Coverage Gate table present with all DR-NNs from map; Sub-claim 2: every DR-NN accounted for (honored or OPEN GAP); Sub-claim 3: gap log entries carry DR-NN ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 + C-41 bidirectional cross-cite) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record Status column -- Platform 1-3 complete before Domain advance; Sub-claim 2: P1/P2 gate signal -- P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND cite "Execution Log, [sub-skill] row, DR-NN Contributed" by name; N1 + N2 + N3 = N_total confirmed; Sub-claim 3: Execution Log Layer column present; Platform 1-3, Domain 4-5 verified by column scan | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43 dedicated axis) | Execution Log | Sub-claim 1: Execution Log DR-NN Contributed column present in the standard five-row table (not only in Layer Completion Record) -- cite "Execution Log" section by name; Platform rows 1-3 list DR-NN IDs or zero-contribution template; Domain rows 4-5 carry "n/a"; Sub-claim 2: union of DR-NN Contributed entries across rows 1-3 equals the full set of declared DR-NNs in the Cross-Skill Dependency Map -- cite the union set and the map set and confirm they match; Sub-claim 3: three-way convergence confirmed: Execution Log DR-NN Contributed column, P2 gate signal per-sub-skill entries, and Cross-Skill Dependency Map all agree on attributed IDs and sub-skill scope | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof (C-37 + C-40 + C-42 + inline-count extension) | Row Count Assertion block | Sub-claim 1: first sentence embeds count 12 inline -- "the 12th and final of 12 targeted axes" -- cite verbatim and confirm three-way match: opening sentence count [12] == table rows [12] == enumerated list items [12]; Sub-claim 2: enumerated list ends with "Declaration-completeness-proof axis (this Row Count Assertion block)" as the final item -- confirm by name; Sub-claim 3: 12 == 12 confirmed; self-reference verified from first sentence alone | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration (including Row Count Assertion block
immediately below the table) > EXECUTION ORDER GATE > Observational Discipline > Execution
Sequence (twelve-axis trace-first: positions 1-3 Platform, gate signal P1+P2 with cross-cites,
positions 4-5 Domain) > Cross-Skill Dependency Map > Candidate Observations and Filter Log >
Filter Log Resolution (with T-1 ANNEX) > Findings Table > Execution Log (with DR-NN Contributed
column) > Ranked Findings > Cross-Skill Comparison Protocol > Coverage Gate >
Confidence-Stratified Action List > Structural Compliance Checklist.

If all sections are empty: apply sub-skill no findings templates for all five scopes; apply
findings table empty template; apply ranked-tier empty-state templates for all four tiers;
apply comparison step with no pairs template; apply both confidence stratification track empty
templates; apply Coverage Gate empty-state template; Structural Compliance Checklist must still
fire for all twelve mechanisms.
