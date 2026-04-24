---
skill: campaign-simulate
round: 13
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v12-2026-03-17.md
---

# campaign-simulate -- Round 13 Variations

**Context**: R12 V-05 achieved all three criterion towers (C-33->C-44, C-36->C-45, C-39->C-46)
simultaneously and was first to achieve C-44/C-45/C-46. C-26/C-27/C-28 failed for all five R12
variations -- they are the confirmed next unlock targets. C-26 requires a Remediation Quality Gate
with Verb/Target/Location/Conformance per finding. C-27 requires an Entity Coverage Matrix with
COVERED/CLEAN/SKIPPED per entity. C-28 requires ELEVATED annotations from cross-skill synthesis
propagating back into the ranked findings table with re-ordering.

**R13 target**: Unlock C-26, C-27, and C-28 individually (V-01/V-02/V-03), then in pairs (V-04),
then in full integration on the R12 V-05 twelve-axis base extended to fifteen axes (V-05).

**Under rubric v12**: aspirational pool 38 criteria (C-26 through C-46), capped at 10 pts.
Max score 100.

**Round 13 axes chosen:**
- Single-axis: V-01 (output format -- Remediation Quality Gate structured table with
  Verb/Target/Location/Conformance per F-ID), V-02 (correctness -- Topic Entity Manifest before
  execution + Entity Coverage Matrix with COVERED/CLEAN/SKIPPED after all five sub-skills),
  V-03 (phrasing register -- Blast Radius Re-Assessment Gate propagating P-ID synthesis results
  back into Ranked Findings as ELEVATED annotations with re-ordering)
- Combined: V-04 (output format + phrasing register -- Remediation Quality Gate table + ELEVATED
  re-assessment; gate rows retroactively flagged for re-assessed findings via Blast Status column)
- Full integration: V-05 (all three extensions on R12 V-05 twelve-axis base; SAD promoted to
  fifteen rows; Row Count Assertion counts to fifteen; three new sections; Compliance Checklist
  gains three new rows; all R12 V-05 mechanisms preserved)

---

## V-01 -- Remediation Quality Gate Structured Table (C-26)

**Variation axis:** Output format -- the report includes a REMEDIATION QUALITY GATE section that
decomposes each finding's remediation into a Verb / Target / Location / Conformance table. Every
F-ID must appear as a row. Blank cells in any column fail C-26 regardless of how detailed the
narrative Remediation field is. The Verb column is constrained by finding Type (GAP -> add/remove;
CONTRADICTION -> resolve; ASSUMPTION -> confirm). The Conformance column must contain a falsifiable
verification instruction naming the specific observable and location -- not a prose summary.

**Hypothesis:** C-26 passes when the structured table is present with all four columns populated
per finding. The column decomposition converts an opaque remediation narrative into a machine-
auditable claim. Verb constraint also enables Type-verb binding verification at the gate level.
Scoring will reveal whether the Conformance column's falsifiability requirement is recognized as
distinct from the Verb/Target/Location triple alone. C-27 and C-28 not targeted.

---

Simulate the technical behavior of: {{topic}}

This report enforces eight structural axes simultaneously. The first section declares all eight
axes. The last section verifies all eight fired using sub-claim decomposition for multi-part axes.
Both sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION
  REQUIRED: revisit candidate list. Either (a) name at least one observation that should be
  rejected, or (b) justify every candidate is anchored to a named spec location."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N] observations.
  Zero withheld-T1. T-1 SCOPE RECALIBRATION: Either name one observation that failed T-1, or
  confirm scope is clean."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1 rows. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Cross-skill comparison
  cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list and
  verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules declared. DEPENDENCY SCOPE RECALIBRATION: Either identify a cross-skill
  constraint or confirm clean execution."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer complete. C-36 FAIL. Retroactive re-examination required."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] rules declared (DR-01 through
  DR-[N]). All accounted for. No OPEN PROPAGATION GAPS."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED."
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings to decompose.
  Gate schema: F-ID | Verb | Target | Location | Conformance. Gate executed with empty finding
  set."

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
Dep rule cite:  [DR-NN if instantiates a dependency rule; "none" otherwise]
Remediation:    [narrative: specific action at named target]
```

The Verb/Target/Location/Conformance decomposition is written in the REMEDIATION QUALITY GATE
section, not inline per finding. The Remediation field contains the narrative; the Gate section
contains the structured columns.

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. All eight rows must have equal
depth: three independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count; (3) filter rules 1-4 listed before any row evaluated |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any section with no results; (2) type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, Remediation Quality Gate, Disposition zero-withheld-T1, Execution Log zero-contribution |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration (Step 3) | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | SAD (eight rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before any execution evidence; (2) Checklist as final section with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables; (3) T-1 ANNEX: summary aggregator role stated; names withheld-T1 example; cites per-scope source |
| DR-NN citation chain axis | C-32 | Three-point chain: map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks |
| Execution-order axis | C-36, C-38, C-39, C-41, C-43 | Layer Completion Record with Status column; P1/P2 gate signal (P2 cross-cites Execution Log DR-NN Contributed by row); Execution Log with Layer AND DR-NN Contributed columns | (1) Layer Completion Record: Status -- Platform 1-3 complete before Domain 4-5; (2) P1/P2 gate: P1 names three Platform sub-skills; P2 entries cite DR-NN IDs AND Execution Log row by name; N1 + N2 + N3 = N_total confirmed; (3) Execution Log: Layer AND DR-NN Contributed columns; Platform match P2; Domain "n/a" |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE section: per-finding table with Verb / Target / Location / Conformance; Verb constrained by Type; Conformance must be falsifiable | (1) one row per F-ID; all four columns populated -- blank cell = C-26 fail; (2) Verb matches Type vocabulary: GAP->add/remove, CONTRADICTION->resolve, ASSUMPTION->confirm; out-of-vocabulary Verb declared as Type-verb bind failure in compliance checklist; (3) Conformance column contains falsifiable verification instruction naming the specific observable and named location -- prose summary without named observable = fail |

---

**EXECUTION ORDER GATE**

Write immediately after the Structural Axis Declaration and before OBSERVATIONAL DISCIPLINE.

**C-36 constraint**: Platform Layer sub-skills must ALL complete before any Domain Layer sub-skill
begins.

**Layer Completion Record** (Status column; DR-NN attribution is in the standard Execution Log):

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
> P2 DEPENDENCY MAP COMPLETE: Per-sub-skill attribution:
>   - trace-state contributed: [DR-NN IDs, N1 rules]
>     cross-verify: Execution Log, trace-state row, DR-NN Contributed column
>   - trace-contract contributed: [DR-NN IDs, N2 rules]
>     cross-verify: Execution Log, trace-contract row, DR-NN Contributed column
>   - trace-permissions contributed: [DR-NN IDs, N3 rules]
>     cross-verify: Execution Log, trace-permissions row, DR-NN Contributed column
>   - Total: N1 + N2 + N3 = [N_total] rules. DR-01 through DR-[N] declared.
> Domain Layer may begin.

---

**OBSERVATIONAL DISCIPLINE**

**Genre declaration**: Pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed filter rule 1-4

**T-1 threshold rule** (before any sub-skill fires): An observation is elevated if and only if it
names a specific spec location AND describes a gap or violation that would cause incorrect
implementation behavior.

**Per-scope Disposition rule**: Zero withheld-T1 triggers RECALIBRATION.

**T-1 ANNEX role (summary aggregator only)**: Aggregates withheld-T1. Not primary evidence.
Cites per-scope records by scope name.

---

**EXECUTION SEQUENCE**

Trace-first order. After each Platform sub-skill: update Cross-Skill Dependency Map AND populate
Execution Log DR-NN Contributed column.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with cross-cites) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

---

**CROSS-SKILL DEPENDENCY MAP**

Populate during Platform Layer execution. Domain sub-skills do not add rows.

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

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

Populate DR-NN Contributed per sub-skill. Platform rows match P2 gate signal. Domain "n/a."

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

**Step 3**: Name compounding patterns with stable P-IDs or apply empty-state template.

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

Apply empty-state template for zero rules or zero gaps.

---

**REMEDIATION QUALITY GATE**

Write this section after Coverage Gate and before the Structural Compliance Checklist. Decompose
every finding from the Findings Table into structured columns. Every F-ID must appear exactly once.
A blank cell in any column is a C-26 fail.

| F-ID | Verb | Target | Location | Conformance |
|------|------|--------|----------|-------------|

**Verb vocabulary** (constrained by finding Type):
- GAP -> "add" or "remove"
- CONTRADICTION -> "resolve"
- ASSUMPTION -> "confirm"

**Conformance column rule**: State the specific observable behavior a reviewer can check to confirm
the fix is complete. Format: "Confirm that [named behavior] is observable at [named location] under
[named condition]." Restating the Summary or writing "fix the spec" fails -- the cell must name a
falsifiable observation point.

**Type-verb bind check**: Any out-of-vocabulary Verb must be declared as a Type-verb bind failure
in the compliance checklist evidence field, citing the F-ID and the out-of-vocabulary Verb.

If no findings exist: apply the Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this as the final section. Multi-part rows: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations, rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary aggregator | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11) | [sections fired] | [template type and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: eight rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary -- cite two labels; Sub-claim 2: T-1 if-and-only-if before sub-skill; Sub-claim 3: Disposition columns all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs -- cite count; Sub-claim 2: Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings cite Dep rule | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41, C-43) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record -- Platform 1-3 before Domain; Sub-claim 2: P1/P2 gate -- P1 names three sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row; N1 + N2 + N3 confirmed; Sub-claim 3: Execution Log Layer AND DR-NN Contributed columns; Platform match P2; Domain "n/a" | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID -- no F-ID absent; all four columns (Verb, Target, Location, Conformance) populated; blank cell = C-26 fail; cite count; Sub-claim 2: Verb column matches Type vocabulary every row -- cite any out-of-vocabulary Verb as Type-verb bind failure with F-ID; Sub-claim 3: Conformance column is falsifiable -- cite one Conformance cell verbatim to confirm named-observable format ("Confirm that [behavior] at [location] under [condition]") | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table > Execution
Log (with DR-NN Contributed column) > Ranked Findings > Cross-Skill Comparison Protocol >
Coverage Gate > Remediation Quality Gate > Structural Compliance Checklist.

---

## V-02 -- Entity Coverage Matrix: COVERED / CLEAN / SKIPPED (C-27)

**Variation axis:** Correctness -- the report declares a TOPIC ENTITY MANIFEST before execution
(listing every entity relevant to the simulation target), then produces an ENTITY COVERAGE MATRIX
after all five sub-skills complete. Every manifest entity receives exactly one of three statuses:
COVERED (appeared in at least one finding or elevated observation, evidence cited), CLEAN (examined,
no gap found, examining sub-skill and reason stated), or SKIPPED (not examined -- treated as an
execution gap with the same disqualifying weight as a missing sub-skill sentinel row under C-16,
declared in compliance checklist).

**Hypothesis:** C-27 passes when every manifest entity has a named status in the Entity Coverage
Matrix, the matrix is generated after all sub-skills run, and SKIPPED entities produce a compliance
checklist gap declaration. The matrix converts entity coverage from an implicit claim into a set-
membership check: {manifest entities} must equal {matrix rows}. Entities absent from the matrix
fail C-27 even if candidate observations about them exist. C-26 and C-28 not targeted.

---

Simulate the technical behavior of: {{topic}}

This report enforces eight structural axes simultaneously. The first section (Topic Entity Manifest)
declares entities before execution. The second section (Structural Axis Declaration) declares all
eight axes. The last section verifies all eight fired using sub-claim decomposition. Both the
declaration and checklist sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected.
  RECALIBRATION REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N] observations.
  Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Comparison cannot
  proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list]."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules. DEPENDENCY SCOPE RECALIBRATION."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: Domain Layer sub-skill
  [name] began before Platform Layer complete. C-36 FAIL."
- **Entity Coverage Matrix empty manifest**: "TOPIC ENTITY MANIFEST: No entities declared.
  MANIFEST RECALIBRATION REQUIRED: Declare at least one entity before execution begins."
- **Entity SKIPPED gap**: "ENTITY COVERAGE GAP: Entity [name] (E-[NN]) status=SKIPPED.
  Reason: [why not examined]. Execution gap logged in compliance checklist."

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

**TOPIC ENTITY MANIFEST**

Write this section as the first section of your output report, before the Structural Axis
Declaration. List every entity relevant to {{topic}} that the simulation must examine. An entity
is any named system component, actor, boundary, state machine, contract, or permission set that
the spec defines or the topic implies. The manifest is written before any sub-skill executes.
Entities discovered during execution are appended with an ADDED annotation.

| Entity ID | Entity Name | Category | Source (spec section or derived) |
|-----------|-------------|----------|----------------------------------|

Entity categories: state-machine / contract-boundary / permission-set / lifecycle-phase /
actor / integration-point

If the manifest is empty after inspection: apply the Entity Coverage Matrix empty manifest
template.

---

**STRUCTURAL AXIS DECLARATION**

Write this section immediately after the Topic Entity Manifest.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations table: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections: sub-skill, ranked tiers, comparison steps, Disposition zero, Execution Log zero-contribution, Entity SKIPPED gap |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings, verdicts, pattern declaration | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: patterns or empty-state template |
| Declaration-compliance axis | C-17, C-18 | SAD (eight rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist final with sub-claim decomposition; (3) evidence cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Three-point chain: map, Coverage Gate, finding Dep rule cite | (1) DR-NN IDs in map; (2) Coverage Gate cites DR-NNs; (3) finding Dep rule cite backlinks |
| Execution-order axis | C-36, C-38, C-39, C-41, C-43 | Layer Completion Record; P1/P2 gate with cross-cites; Execution Log Layer AND DR-NN Contributed | (1) Layer Completion Record Status -- Platform 1-3 before Domain; (2) P1/P2 gate with attribution; (3) Execution Log Layer AND DR-NN Contributed |
| Entity-coverage axis | C-27 | Topic Entity Manifest (before execution) + Entity Coverage Matrix (after all five sub-skills) with COVERED / CLEAN / SKIPPED per entity | (1) Entity Coverage Matrix: one row per manifest entity -- no entity absent; COVERED cites F-ID or Obs #; CLEAN names examining sub-skill and clean reason; SKIPPED logged as execution gap; (2) SKIPPED entities declared in compliance checklist evidence field with entity name, ID, and reason; (3) entities discovered during execution appended to manifest with ADDED annotation before matrix is written |

---

**EXECUTION ORDER GATE**

Write immediately after the Structural Axis Declaration.

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | |

Gate signal after position 3:

> EXECUTION ORDER GATE:
> P1: trace-state (1): complete. trace-contract (2): complete. trace-permissions (3): complete.
> P2: trace-state: [DR-NNs, N1] -- cross-verify: Execution Log, trace-state row, DR-NN Contributed.
>     trace-contract: [DR-NNs, N2] -- cross-verify: Execution Log, trace-contract row, DR-NN Contributed.
>     trace-permissions: [DR-NNs, N3] -- cross-verify: Execution Log, trace-permissions row, DR-NN Contributed.
>     Total: N1 + N2 + N3 = [N_total]. DR-01 through DR-[N] declared.
> Domain Layer may begin.

---

**OBSERVATIONAL DISCIPLINE**

**Genre**: Pre-implementation simulation findings document.
**Vocabulary**: "Candidate observation", "elevated", "withheld-T1", "withheld-rule".
**T-1**: Elevated if and only if it names a specific spec location AND describes a gap causing
incorrect implementation behavior.
**Per-scope Disposition rule**: Zero withheld-T1 triggers RECALIBRATION.
**T-1 ANNEX**: Summary aggregator only. Cites per-scope records by scope name.

---

**EXECUTION SEQUENCE**

Trace-first: 1. trace-state, 2. trace-contract, 3. trace-permissions, [GATE], 4. flow-lifecycle,
5. flow-conversation. During each sub-skill, note which manifest entities are examined.

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

After completing all five sub-skills: write the Entity Coverage Matrix before the Ranked Findings.

---

**CROSS-SKILL DEPENDENCY MAP**

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
> - Total withheld-T1: [N] (sources: [list])
> - Example: [Sub-skill, Obs #] withheld -- record in [section]
> - Zero-withheld scopes: [list or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

---

**ENTITY COVERAGE MATRIX**

Write after the Execution Log and before Ranked Findings. Every manifest entity (including ADDED
entries) must appear. Status rules:
- **COVERED**: appeared in at least one elevated finding or elevated observation -- cite F-ID or Obs #
- **CLEAN**: examined during execution, no gap found -- name examining sub-skill(s) and explain why no gap was detected
- **SKIPPED**: not examined -- execution gap; apply Entity SKIPPED gap template inline

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) |
|-----------|-------------|--------|--------------|----------------------------------------|

---

**RANKED FINDINGS**

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

[Apply ranked-tier empty-state template for any empty tier]

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |
**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |
**Step 3**: Compounding patterns named or empty-state template.

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations | [observations, rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + count; Sub-claim 2: ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11) | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: eight rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows with DR-NN IDs + source; Sub-claim 2: Coverage Gate cites DR-NNs; Sub-claim 3: findings cite Dep rule | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41, C-43) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record -- Platform before Domain; Sub-claim 2: P1/P2 per-sub-skill attribution with Execution Log cross-cites; Sub-claim 3: Execution Log Layer AND DR-NN Contributed | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Entity Coverage Matrix has one row per manifest entity -- cite entity count from manifest and confirm matrix row count matches; Sub-claim 2: COVERED entities cite evidence; CLEAN entities name examining sub-skill and reason; SKIPPED entities have execution gap declaration in this checklist row with entity name and ID; Sub-claim 3: entities discovered during execution appear in matrix with ADDED annotation -- confirm manifest updated before matrix | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration > EXECUTION ORDER
GATE > Observational Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map >
Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table >
Execution Log > Entity Coverage Matrix > Ranked Findings > Cross-Skill Comparison Protocol >
Coverage Gate > Structural Compliance Checklist.

---

## V-03 -- Blast Radius Re-Assessment Gate: ELEVATED Annotations (C-28)

**Variation axis:** Phrasing register -- after the Cross-Skill Comparison Protocol produces
compounding patterns (Step 3, P-IDs), a BLAST RADIUS RE-ASSESSMENT GATE fires before report
finalization. The gate re-evaluates the blast radius of every finding that participates in a
compounding pattern. Findings whose blast radius increases receive an ELEVATED annotation inline
in the Ranked Findings table, citing the P-ID. The Ranked Findings table is re-sorted by
re-assessed blast radii.

**Hypothesis:** C-28 passes when at least one finding carries an ELEVATED annotation with P-ID
citation in the Ranked Findings table and the ordering reflects re-assessed blast radii. A
synthesis section that records P-IDs without updating the Ranked Findings table = C-24 pass,
C-28 fail. The ELEVATED annotation must appear on the finding's row in the Ranked Findings table --
not in a separate section. C-26 and C-27 not targeted.

---

Simulate the technical behavior of: {{topic}}

This report enforces eight structural axes simultaneously. The first section declares all eight
axes. The last section verifies all eight fired using sub-claim decomposition. Both sections are
written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected.
  RECALIBRATION REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N] observations.
  Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns. Step 2 pairs: [list]. Each distinct
  root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed (Execution Log,
  [sub-skill]): Zero rules. DEPENDENCY SCOPE RECALIBRATION."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: [name] began before
  Platform complete. C-36 FAIL."
- **Blast Re-Assessment Gate no elevation**: "BLAST RADIUS RE-ASSESSMENT GATE: [N] compounding
  patterns declared (P-01 through P-[N]). Re-assessment complete. Zero findings elevated.
  No blast radius changes from synthesis. Ranked Findings order unchanged."
- **Blast Re-Assessment Gate no patterns**: "BLAST RADIUS RE-ASSESSMENT GATE: Zero compounding
  patterns declared (Step 3 empty). Re-assessment cannot proceed. Ranked Findings unchanged."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE FIELD]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Dep rule cite:  [DR-NN or "none"]
Remediation:    [REQUIRED: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason; (2) Filter Log Resolution: template letter + count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11 | Per-section empty-state templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in checklist; (3) sections: sub-skill, ranked tiers, comparison steps, both Blast Re-Assessment Gate states, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs in Step 3 | (1) Step 1: pairs; (2) Step 2: verdicts; (3) Step 3: P-IDs named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | SAD (eight rows) + Compliance Checklist | (1) SAD before execution; (2) Checklist final with sub-claims; (3) evidence cites actual sections |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Map, Coverage Gate, finding Dep rule cite | (1) DR-NN IDs in map; (2) Coverage Gate cites; (3) findings backlink |
| Execution-order axis | C-36, C-38, C-39, C-41, C-43 | Layer Completion Record; P1/P2 gate; Execution Log Layer AND DR-NN Contributed | (1) Layer Completion Record Status -- Platform before Domain; (2) P1/P2 with per-sub-skill cross-cites; (3) Execution Log Layer AND DR-NN Contributed |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE fires after Cross-Skill Comparison Step 3; P-IDs drive re-assessment; ELEVATED annotations inline on Ranked Findings rows; table re-sorted | (1) Re-Assessment Gate table: P-ID, participant F-IDs, individual blast radii, compound blast, ELEVATED flag; (2) ELEVATED annotation inline on each affected Ranked Findings row in form "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]" -- verifiable by row inspection; (3) Ranked Findings table re-sorted by re-assessed blast radius -- if any elevation: cite one finding that moved tiers; if none: cite applied empty-state template |

---

**EXECUTION ORDER GATE**

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending] | |
| Domain | flow-conversation | 5 | [pending] | |

Gate signal after position 3:

> EXECUTION ORDER GATE:
> P1: trace-state (1): complete. trace-contract (2): complete. trace-permissions (3): complete.
> P2: trace-state: [DR-NNs, N1] -- cross-verify: Execution Log, trace-state row, DR-NN Contributed.
>     trace-contract: [DR-NNs, N2] -- cross-verify: Execution Log, trace-contract row, DR-NN Contributed.
>     trace-permissions: [DR-NNs, N3] -- cross-verify: Execution Log, trace-permissions row, DR-NN Contributed.
>     Total: N1 + N2 + N3 = [N_total]. DR-01 through DR-[N] declared.
> Domain Layer may begin.

---

**OBSERVATIONAL DISCIPLINE**

**Genre**: Pre-implementation simulation findings document.
**Vocabulary**: "Candidate observation", "elevated", "withheld-T1", "withheld-rule".
**T-1**: Elevated if and only if it names a specific spec location AND describes a gap causing
incorrect implementation behavior.
**T-1 ANNEX**: Summary aggregator only.

---

**EXECUTION SEQUENCE** (trace-first: 1-3 Platform, [GATE], 4-5 Domain)

**Per-scope gate table** (one per sub-skill):
| Obs # | What was noticed | Disposition | T-1 reason | Filter rule |
|-------|-----------------|------------|-----------|-------------|

---

**CROSS-SKILL DEPENDENCY MAP** / **CANDIDATE OBSERVATIONS AND FILTER LOG** /
**FILTER LOG RESOLUTION + T-1 ANNEX** / **FINDINGS TABLE** / **EXECUTION LOG** -- same schemas
as V-01.

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

Label this section "RANKED FINDINGS (pre-re-assessment)".

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |

**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |

**Step 3 -- Pattern declaration**: Assign stable P-IDs. For each pattern:
- P-ID: [P-01, ...]
- Participant findings: [F-IDs]
- Compounding mechanism: [how findings compound]
- Blast radius implication: [does the compound exceed any participant's individual blast?]

Apply empty-state template if no patterns.

---

**BLAST RADIUS RE-ASSESSMENT GATE**

Write immediately after the Cross-Skill Comparison Protocol.

This gate takes the P-IDs from Step 3 and re-evaluates the blast radius of every participant
finding. A finding's blast radius is elevated if the compounding pattern implies a broader failure
scope than its individual blast radius.

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

**Re-assessment rule**: If Compound Blast > any Participant's Individual Blast, set ELEVATED=YES.
Write the ELEVATED annotation inline on that finding's Updated Ranked Findings row. Re-sort
the Updated Ranked Findings table.

Apply the Blast Re-Assessment Gate no patterns template if Step 3 produced zero patterns.
Apply the Blast Re-Assessment Gate no elevation template if patterns exist but no blast increases.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label this section "RANKED FINDINGS (post-re-assessment -- authoritative)".

Re-sorted by re-assessed blast radius. Elevated findings carry inline annotation appended to the
Summary field:

```
Summary: [original summary] [ELEVATED: [old] -> [new] (P-ID: [P-ID])]
```

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations | [observations, counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template + count; Sub-claim 2: ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11) | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 with P-IDs | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: eight rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings | Sub-claim 1: DR-NN IDs + source; Sub-claim 2: Coverage Gate cites; Sub-claim 3: findings cite | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41, C-43) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Sub-claim 2: P1/P2 per-sub-skill with cross-cites; Sub-claim 3: Execution Log Layer AND DR-NN Contributed | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Re-Assessment Gate table present; one row per P-ID; all columns populated; cite P-ID count; Sub-claim 2: every finding flagged ELEVATED in gate table carries inline annotation on Updated Ranked Findings row -- cite F-ID and annotation text verbatim; if no elevation: cite applied empty-state template; Sub-claim 3: Updated Ranked Findings is re-sorted by re-assessed blast radius and labeled as authoritative -- cite one finding that moved tiers as evidence, or cite no-elevation template if none | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table > Execution
Log > Initial Ranked Findings (pre-re-assessment) > Cross-Skill Comparison Protocol > Blast
Radius Re-Assessment Gate > Updated Ranked Findings (post-re-assessment, authoritative) >
Coverage Gate > Structural Compliance Checklist.

Note: Ranked Findings appears twice -- before and after the Re-Assessment Gate. The post-
re-assessment version is authoritative.

---

## V-04 -- Remediation Quality Gate + ELEVATED Re-Assessment (C-26 + C-28)

**Variation axes:** Output format + phrasing register combined -- V-01's Remediation Quality Gate
table merged with V-03's ELEVATED annotation mechanism. The Remediation Quality Gate table adds
a fifth column: Blast Status. After the Blast Radius Re-Assessment Gate fires and elevates
findings, the Blast Status column is updated for those findings: "REASSESSED: [old] -> [new]
(P-ID: [P-ID])". All non-elevated findings carry "ORIGINAL". This creates a closed loop: a
reviewer can confirm synthesis propagation by scanning the Blast Status column without re-reading
the Re-Assessment Gate section. C-27 (Entity Coverage Matrix) not targeted.

**Hypothesis:** C-26 and C-28 can be jointly satisfied. The Remediation Quality Gate table and
the ELEVATED annotation mechanism are independently verifiable; combining them adds a fifth column
to the gate table without altering C-26's core pass condition (four columns, no blanks). The
REASSESSED Blast Status flag converts the Remediation Quality Gate into a third verification path
for synthesis propagation, alongside the Re-Assessment Gate table (first path) and the inline
ELEVATED annotation on the Ranked Findings row (second path).

---

Simulate the technical behavior of: {{topic}}

This report enforces nine structural axes simultaneously. The first section declares all nine.
The last section verifies all nine using sub-claim decomposition. Both sections are written into
the output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps detected."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected.
  RECALIBRATION REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N] observations.
  Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns. Step 2 pairs: [list]. Distinct root
  causes."
- **Execution log zero candidates**: "Zero candidates. Reason: [explanation]."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed ([sub-skill]):
  Zero rules. DEPENDENCY SCOPE RECALIBRATION."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: [name] before Platform
  complete. C-36 FAIL."
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Schema: F-ID |
  Verb | Target | Location | Conformance | Blast Status."
- **Blast Re-Assessment Gate no elevation**: "BLAST RADIUS RE-ASSESSMENT GATE: [N] patterns
  declared. Zero elevated. Ranked Findings unchanged. All Blast Status = ORIGINAL."
- **Blast Re-Assessment Gate no patterns**: "BLAST RADIUS RE-ASSESSMENT GATE: Zero patterns.
  Re-assessment skipped. All Blast Status = ORIGINAL."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Spec location:  [REQUIRED]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Dep rule cite:  [DR-NN or "none"]
Remediation:    [narrative: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log; Filter Log Resolution | (1) Candidate Observations: Elevate? + Rejection Reason; (2) Resolution: letter + count; (3) rules 1-4 before any row |
| Empty-state axis | C-11 | Per-section templates; silence prohibited | (1) Named template in empty sections; (2) type + first clause in checklist; (3) sections: sub-skill, tiers, comparison, both Blast Gate states, Remediation Quality Gate, Disposition zero |
| Cross-skill comparison axis | C-15 | Three-step protocol; stable P-IDs | (1) Step 1: pairs; (2) Step 2: verdicts; (3) Step 3: P-IDs or empty-state |
| Declaration-compliance axis | C-17, C-18 | SAD (nine rows) + Compliance Checklist | (1) SAD before execution; (2) Checklist final with sub-claims; (3) evidence cites sections |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 + five per-scope + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope tables; (3) T-1 ANNEX as aggregator |
| DR-NN citation chain axis | C-32 | Map, Coverage Gate, Dep rule cite | (1) DR-NN IDs in map; (2) Coverage Gate cites; (3) findings backlink |
| Execution-order axis | C-36, C-38, C-39, C-41, C-43 | Layer Completion Record; P1/P2; Execution Log Layer + DR-NN Contributed | (1) Layer Completion Status; (2) P1/P2 with cross-cites; (3) Execution Log Layer + DR-NN Contributed |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE with Verb / Target / Location / Conformance / Blast Status; Verb constrained by Type | (1) one row per F-ID; all five columns populated; blank = C-26 fail; (2) Verb matches Type vocabulary; out-of-vocabulary = Type-verb bind failure in checklist; (3) Conformance is falsifiable -- names specific observable + location; Blast Status: ORIGINAL or REASSESSED:[old]->[new](P-ID) |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE after Step 3; ELEVATED annotations inline on Updated Ranked Findings; Remediation Quality Gate Blast Status updated | (1) Re-Assessment Gate table: P-ID, participants, individual blasts, compound blast, ELEVATED flag; (2) ELEVATED annotation inline on Updated Ranked Findings row -- form "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]"; (3) Remediation Quality Gate Blast Status = REASSESSED for every elevated finding -- verifiable by column scan independent of Re-Assessment Gate and Ranked Findings sections |

---

**EXECUTION ORDER GATE**

**Layer Completion Record**:

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending] | |
| Domain | flow-conversation | 5 | [pending] | |

Gate signal after position 3:

> EXECUTION ORDER GATE:
> P1: trace-state (1): complete. trace-contract (2): complete. trace-permissions (3): complete.
> P2: trace-state: [DR-NNs, N1] -- cross-verify: Execution Log, trace-state, DR-NN Contributed.
>     trace-contract: [DR-NNs, N2] -- cross-verify: Execution Log, trace-contract, DR-NN Contributed.
>     trace-permissions: [DR-NNs, N3] -- cross-verify: Execution Log, trace-permissions, DR-NN Contributed.
>     Total: N1 + N2 + N3 = [N_total]. DR-01 through DR-[N] declared.
> Domain Layer may begin.

---

**OBSERVATIONAL DISCIPLINE**

**Genre**: Pre-implementation simulation findings document.
**Vocabulary**: "Candidate observation", "elevated", "withheld-T1", "withheld-rule".
**T-1**: Elevated if and only if it names a specific spec location AND describes a gap causing
incorrect implementation behavior.
**T-1 ANNEX**: Summary aggregator only.

---

**EXECUTION SEQUENCE** (trace-first: 1-3 Platform, [GATE], 4-5 Domain)

**Per-scope gate table**: | Obs # | What was noticed | Disposition | T-1 reason | Filter rule |

---

**CROSS-SKILL DEPENDENCY MAP** / **CANDIDATE OBSERVATIONS AND FILTER LOG** /
**FILTER LOG RESOLUTION + T-1 ANNEX** / **FINDINGS TABLE** / **EXECUTION LOG** -- same schemas
as V-01.

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

Label "RANKED FINDINGS (pre-re-assessment)". Apply empty-state templates for empty tiers.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |
**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |
**Step 3**: P-IDs with participant F-IDs, mechanism, blast implication. Empty-state if none.

---

**BLAST RADIUS RE-ASSESSMENT GATE**

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

For each ELEVATED finding:
1. Append ELEVATED annotation inline on Updated Ranked Findings row.
2. Set Blast Status to "REASSESSED: [old] -> [new] (P-ID: [P-ID])" in Remediation Quality Gate.

Apply empty-state template for zero patterns or zero elevations.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label "RANKED FINDINGS (post-re-assessment -- authoritative)". Re-sorted. ELEVATED annotations
appended inline to Summary field of affected rows.

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**REMEDIATION QUALITY GATE**

Write after Coverage Gate. One row per F-ID. No finding absent. Five columns required.

| F-ID | Verb | Target | Location | Conformance | Blast Status |
|------|------|--------|----------|-------------|--------------|

**Verb vocabulary**: GAP -> add/remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm.

**Blast Status column**: ORIGINAL for findings not elevated. REASSESSED: [old] -> [new]
(P-ID: [P-ID]) for findings elevated by the Re-Assessment Gate.

**Conformance rule**: Falsifiable -- "Confirm that [named behavior] is observable at [named
location] under [named condition]."

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations | [observations, counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template + count; Sub-claim 2: ANNEX + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11) | [sections] | [type + first clause] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: nine rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings | Sub-claim 1: DR-NN IDs + source; Sub-claim 2: Coverage Gate cites; Sub-claim 3: findings cite | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41, C-43) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Sub-claim 2: P1/P2 cross-cites; Sub-claim 3: Execution Log Layer + DR-NN Contributed | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all five columns (Verb, Target, Location, Conformance, Blast Status) populated; blank = fail; Sub-claim 2: Verb matches Type vocabulary; cite mismatches as Type-verb bind failures; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim; Blast Status = ORIGINAL or REASSESSED with P-ID for every elevated finding | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings + Remediation Quality Gate | Sub-claim 1: Re-Assessment Gate table present; one row per P-ID; all columns populated; Sub-claim 2: every ELEVATED finding carries inline annotation on Updated Ranked Findings row -- cite F-ID + text; Updated Ranked Findings re-sorted (cite moved finding, or no-elevation template); Sub-claim 3: Remediation Quality Gate Blast Status column = REASSESSED for every elevated finding -- confirm by column scan; bidirectional: Re-Assessment Gate flag -> Updated Ranked Findings annotation -> Remediation Quality Gate Blast Status | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table > Execution
Log > Initial Ranked Findings (pre-re-assessment) > Cross-Skill Comparison Protocol > Blast
Radius Re-Assessment Gate > Updated Ranked Findings (post-re-assessment, authoritative) >
Coverage Gate > Remediation Quality Gate > Structural Compliance Checklist.

---

## V-05 -- Full Integration: 15-Axis SAD with C-26, C-27, C-28 on R12 V-05 Base

**Variation axes:** Role sequence + output format + phrasing register combined -- builds on R12
V-05 twelve-axis base and promotes C-26, C-27, C-28 to first-class SAD axes: (13) remediation-
quality axis (C-26), (14) entity-coverage axis (C-27), (15) blast-reassessment axis (C-28). SAD
promoted from twelve to fifteen rows. Row Count Assertion counts to fifteen. Three new sections
added. Compliance Checklist gains three rows. All R12 V-05 mechanisms (C-29 through C-46) are
preserved; the three new axes are additive.

**Hypothesis:** All criteria through C-28 (plus C-44/C-45/C-46 from R12 V-05) pass
simultaneously. The Remediation Quality Gate Blast Status column creates a third verification path
for C-28 propagation (alongside the Re-Assessment Gate table and the inline ELEVATED annotation),
enabling a reviewer to confirm synthesis propagated by scanning the Blast Status column alone
without reading either the Re-Assessment Gate section or the Updated Ranked Findings section.
The fifteen-axis Row Count Assertion simultaneously satisfies C-37 (count), C-40 (self-reference),
C-42 (opening sentence), and C-44 (count inline in opening sentence) at the new scope of fifteen.

---

Simulate the technical behavior of: {{topic}}

This report enforces fifteen structural axes simultaneously. The first section (Topic Entity
Manifest) declares entities. The second section (Structural Axis Declaration) declares all fifteen
axes with a self-referential Row Count Assertion immediately following. The last section verifies
all fifteen fired using sub-claim decomposition. All sections are written by the model into the
output artifact.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list].
  No gaps or violations detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION
  REQUIRED: revisit candidate list. Either (a) name at least one observation that should be
  rejected, or (b) justify every candidate is anchored to a named spec location."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N] observations.
  Zero withheld-T1. T-1 SCOPE RECALIBRATION: name one observation that failed T-1, or confirm
  scope is clean."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Comparison cannot
  proceed."
- **Cross-skill patterns empty**: "No compounding patterns. Step 2 pairs: [list and verdicts].
  Each distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but no observable output. Reason: [why].
  Impact: [effect]."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: [name] began before
  Platform complete. C-36 FAIL. Retroactive re-examination required."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed ([sub-skill]):
  Zero rules. DEPENDENCY SCOPE RECALIBRATION: Either identify a constraint or confirm clean
  execution."
- **Propagation Coverage Gate no gaps**: "Coverage Gate: [N] rules declared (DR-01 through
  DR-[N]). All accounted for. No OPEN PROPAGATION GAPS."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED."
- **Confidence stratification track empty**: "Action track [HIGH/LOW-confidence HIGH-blast]:
  No findings. Schema: F-ID | Summary | Blast Radius | Confidence | Conf rationale."
- **Row Count Assertion mismatch**: "Row Count Assertion MISMATCH: Opening sentence states
  count [stated]. Table contains [actual] rows. Targeted axis count is [expected]. Three-way
  match required. Missing axis: [name]. C-37 FAIL."
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Schema: F-ID |
  Verb | Target | Location | Conformance | Blast Status."
- **Entity Coverage Matrix empty manifest**: "TOPIC ENTITY MANIFEST: No entities declared.
  MANIFEST RECALIBRATION REQUIRED."
- **Entity SKIPPED gap**: "ENTITY COVERAGE GAP: Entity [name] (E-[NN]) status=SKIPPED.
  Reason: [why not examined]. Execution gap logged."
- **Blast Re-Assessment Gate no elevation**: "BLAST RADIUS RE-ASSESSMENT GATE: [N] patterns
  declared. Zero findings elevated. Ranked Findings unchanged. All Blast Status = ORIGINAL."
- **Blast Re-Assessment Gate no patterns**: "BLAST RADIUS RE-ASSESSMENT GATE: Zero patterns.
  Re-assessment skipped. All Blast Status = ORIGINAL."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Spec location:  [REQUIRED]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Confidence:     [HIGH / LOW -- required for cross-skill and system-wide]
Conf rationale: [REQUIRED if Confidence present: falsifiable basis]
Dep rule cite:  [DR-NN or "none"]
Remediation:    [narrative: specific action at named target]
Verb:           [constrained by Type: GAP -> add/remove; CONTRADICTION -> resolve;
                 ASSUMPTION -> confirm]
```

---

**TOPIC ENTITY MANIFEST**

Write as the first section of your output report.

| Entity ID | Entity Name | Category | Source |
|-----------|-------------|----------|--------|

Entity categories: state-machine / contract-boundary / permission-set / lifecycle-phase /
actor / integration-point

Entities discovered during execution: append with ADDED annotation.
If empty: apply Entity Coverage Matrix empty manifest template.

---

**STRUCTURAL AXIS DECLARATION**

Write immediately after the Topic Entity Manifest. All fifteen rows must have equal depth:
three independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? + Rejection Reason; (2) Filter Log Resolution: template letter + count; (3) rules 1-4 before any row |
| Empty-state axis | C-11, C-34 | Per-section templates; named templates for zero-content structured sections | (1) Named template in any empty section; (2) type + first clause in checklist; (3) sections: sub-skill, tiers, comparison, action tracks, Coverage Gate, Disposition zero, Execution Log zero-contribution, Entity Coverage Matrix, Remediation Quality Gate, both Blast Gate states |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs in Step 3 | (1) Step 1: F-ID A, F-ID B, Surface similarity; (2) Step 2: Verdict, Reason; (3) Step 3: P-IDs named or empty-state template |
| Declaration-compliance axis | C-17, C-18 | SAD (fifteen rows, three observables each) + Compliance Checklist | (1) SAD before any execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 (if-and-only-if) + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if before any sub-skill; (2) five per-scope tables; (3) T-1 ANNEX: summary aggregator; names withheld-T1 example by scope |
| DR-NN citation chain axis | C-32 | Three-point chain: map, Coverage Gate, Dep rule cite; P2 cross-cites Execution Log row | (1) Cross-Skill Dependency Map: DR-NN ID + source + constraint; {map IDs} declared; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks; P2 entries cite Execution Log row by name |
| Confidence stratification axis | C-30, C-35 | Action list: two named tracks by confidence x blast; Conf rationale per finding | (1) Track 1: HIGH-confidence / HIGH-blast; (2) Track 2: LOW-confidence / HIGH-blast; (3) each finding carries Conf rationale with falsifiable basis |
| Type-verb binding axis | C-31 | Type declared at detection; Verb constrained; Verb in Findings Table AND Remediation Quality Gate | (1) every finding carries Type before Verb written; (2) Verb matches Type vocabulary; (3) out-of-vocabulary Verb declared as Type-verb bind failure; dual-column check: Findings Table + Remediation Quality Gate |
| Propagation coverage axis | C-29 | Coverage Gate: every DR-NN honored or logged as OPEN PROPAGATION GAP | (1) Coverage Gate: DR-ID, Status, Finding IDs, Gap Reason; (2) all DR-NNs accounted for; (3) gap log entries carry DR-NN ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate (P2 labeled, per-sub-skill attribution, cross-cites Execution Log); Execution Log Layer column | (1) Layer Completion Record Status -- Platform 1-3 before Domain 4-5; (2) P1/P2: P1 names three sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row; N1 + N2 + N3 = N_total; (3) Execution Log Layer column: Platform 1-3, Domain 4-5 |
| Execution-log attribution axis | C-43 | Standard five-row Execution Log DR-NN Contributed column as dedicated fourth structural path | (1) DR-NN Contributed in standard Execution Log (not only Layer Completion Record); Platform rows 1-3 list DR-NN IDs or zero-template; Domain rows carry "n/a"; (2) union of rows 1-3 = full dependency map; (3) Compliance Checklist: confirms column present; union equals map; Domain rows "n/a" |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: per-finding table with Verb / Target / Location / Conformance / Blast Status; Verb constrained by Type | (1) one row per F-ID; all five columns populated; blank = fail; (2) Verb matches Type vocabulary; mismatch = Type-verb bind failure in checklist; (3) Conformance is falsifiable; Blast Status = ORIGINAL or REASSESSED:[old]->[new](P-ID) for every elevated finding |
| Entity-coverage axis | C-27 | Topic Entity Manifest (before execution) + Entity Coverage Matrix (after all five sub-skills) with COVERED / CLEAN / SKIPPED per entity | (1) Entity Coverage Matrix: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names examining sub-skill + reason; SKIPPED logged as execution gap; (2) SKIPPED entities declared in checklist with entity name, ID, reason; (3) ADDED entities (discovered during execution) in manifest before matrix |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE after Step 3; ELEVATED inline on Updated Ranked Findings; Remediation Quality Gate Blast Status updated | (1) Re-Assessment Gate table: P-ID, participants, blasts, ELEVATED flag; (2) ELEVATED annotation inline on Updated Ranked Findings row -- form "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]"; (3) Remediation Quality Gate Blast Status = REASSESSED for elevated findings -- verifiable by column scan without reading Re-Assessment Gate section |
| Declaration-completeness-proof axis | C-37, C-40, C-42 | Row Count Assertion block below this table: first sentence embeds count 15 inline; enumerates all fifteen axes ending with this axis | (1) Row Count Assertion first sentence: "This Row Count Assertion, itself the 15th and final of the 15 targeted axes declared below, is C-37's completeness proof" -- count 15 readable without reading list; (2) enumerated list names all fifteen with this axis as final; (3) Compliance Checklist: sub-claim 1 cites first sentence verbatim + three-way match; sub-claim 2 confirms final list item; sub-claim 3 confirms 15 == 15 |

**Row Count Assertion** (write immediately after the table above):

> This Row Count Assertion, itself the 15th and final of the 15 targeted axes declared below,
> is C-37's completeness proof. (The count "15" is embedded in this opening sentence: the
> C-37 count invariant -- N rows == N targeted axes -- is verifiable from this sentence alone
> without reading the enumerated list or the table row count.)
> Targeted quality axes in this simulation:
> (1) Filtering axis, (2) Empty-state axis, (3) Cross-skill comparison axis,
> (4) Declaration-compliance axis, (5) Observational discipline axis,
> (6) DR-NN citation chain axis, (7) Confidence stratification axis,
> (8) Type-verb binding axis, (9) Propagation coverage axis,
> (10) Execution-order axis, (11) Execution-log attribution axis,
> (12) Remediation-quality axis, (13) Entity-coverage axis,
> (14) Blast-reassessment axis,
> (15) Declaration-completeness-proof axis (this Row Count Assertion block).
> Three-way count match: opening sentence count [15] == table rows [15] == enumerated items [15].
> Declaration is contract-complete. Self-reference confirmed: this block appears as item (15),
> the final item, in the list it is proving complete.

If count mismatch: apply Row Count Assertion mismatch template.

---

**EXECUTION ORDER GATE**

Write immediately after the Structural Axis Declaration.

**Layer Completion Record** (Status column; DR-NN attribution is in the standard Execution Log):

| Layer | Sub-Skill | Position | Status | Completion Marker |
|-------|-----------|----------|--------|-------------------|
| Platform | trace-state | 1 | [pending / in-progress / complete] | |
| Platform | trace-contract | 2 | [pending / in-progress / complete] | |
| Platform | trace-permissions | 3 | [pending / in-progress / complete] | |
| Domain | flow-lifecycle | 4 | [pending -- must not start until Platform complete] | |
| Domain | flow-conversation | 5 | [pending -- must not start until Platform complete] | |

Gate signal after position 3:

> EXECUTION ORDER GATE:
> P1 EXECUTION ORDER COMPLETE: Platform Layer fully executed in positions 1-3.
>   - trace-state (position 1): complete
>   - trace-contract (position 2): complete
>   - trace-permissions (position 3): complete
> P2 DEPENDENCY MAP COMPLETE: Per-sub-skill attribution (cross-verify via Execution Log):
>   - trace-state contributed: [DR-NN IDs, N1 rules]
>     cross-verify: Execution Log, trace-state row, DR-NN Contributed column
>   - trace-contract contributed: [DR-NN IDs, N2 rules]
>     cross-verify: Execution Log, trace-contract row, DR-NN Contributed column
>   - trace-permissions contributed: [DR-NN IDs, N3 rules]
>     cross-verify: Execution Log, trace-permissions row, DR-NN Contributed column
>   - Total: N1 + N2 + N3 = [N_total] rules. DR-01 through DR-[N] declared.
>   - Three-way convergence: Cross-Skill Dependency Map, P2, and Execution Log DR-NN
>     Contributed column (rows 1-3) must all agree. Discrepancy = integrity failure.
> Domain Layer may begin.

---

**OBSERVATIONAL DISCIPLINE**

Write immediately after the EXECUTION ORDER GATE.

**Genre declaration**: Pre-implementation simulation findings document.
Structural vocabulary (minimum four terms):
- "Candidate observation" -- spec behavior submitted for T-1 evaluation
- "elevated" -- passed T-1 AND all four filter rules; enters Findings Table
- "withheld-T1" -- failed T-1; primary record in per-scope Disposition column
- "withheld-rule" -- passed T-1 but failed filter rule 1-4

**T-1 threshold rule** (stated before any sub-skill fires): An observation is elevated if and
only if it names a specific spec location AND describes a gap or violation that would cause
incorrect implementation behavior.

**Per-scope Disposition rule**: Zero withheld-T1 triggers RECALIBRATION.

**T-1 ANNEX role (summary aggregator only)**: Aggregates withheld-T1. Cites per-scope records
by scope name.

---

**EXECUTION SEQUENCE**

Trace-first order. After each Platform sub-skill: update Layer Completion Record Status, add
dependency rules to Cross-Skill Dependency Map, populate Execution Log DR-NN Contributed column,
and note which manifest entities were examined.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual at each interface
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with cross-cites) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|----------------------------|---------------------------------|

---

**CROSS-SKILL DEPENDENCY MAP**

Populate during Platform Layer execution. Domain sub-skills do not add rows.

| DR-ID | Source Sub-Skill | Constraint | Domain Scope Constrained |
|-------|-----------------|------------|--------------------------|

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

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Confidence | Conf Rationale | Dep Rule Cite | Remediation | Verb |
|------|-----------|------|--------------|---------|--------|-------------|------------|----------------|---------------|-------------|------|

---

**EXECUTION LOG**

Populate DR-NN Contributed per sub-skill. Platform rows match P2 gate signal. Domain "n/a."
Union of rows 1-3 = full declared dependency map.

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NN IDs, or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

---

**ENTITY COVERAGE MATRIX**

Write after Execution Log, after all five sub-skills complete.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence |
|-----------|-------------|--------|--------------|----------|

Status: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill + reason) /
SKIPPED (execution gap -- apply Entity SKIPPED gap template).

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

Label "RANKED FINDINGS (pre-re-assessment)".

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**: | Pair # | F-ID A | F-ID B | Surface similarity |

**Step 2 -- Pairwise comparison**: | Pair # | F-ID A | F-ID B | Verdict | Reason |

**Step 3 -- Pattern declaration**: Stable P-IDs. For each: participant F-IDs, mechanism, blast
implication. Empty-state template if no patterns.

---

**BLAST RADIUS RE-ASSESSMENT GATE**

Write immediately after the Cross-Skill Comparison Protocol.

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

For each ELEVATED finding:
1. Append ELEVATED annotation to Updated Ranked Findings row.
2. Set Blast Status to "REASSESSED: [old] -> [new] (P-ID: [P-ID])" in Remediation Quality Gate.

Apply empty-state template for zero patterns or zero elevations.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label "RANKED FINDINGS (post-re-assessment -- authoritative)". Re-sorted. ELEVATED annotations
appended inline to Summary field of affected rows in form:
`[ELEVATED: [old] -> [new] (P-ID: [P-ID])]`

---

**COVERAGE GATE**

All declared DR-NN rules must appear in a finding (honored) or gap log (OPEN PROPAGATION GAP).

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**CONFIDENCE-STRATIFIED ACTION LIST**

**Track 1 -- HIGH-confidence / HIGH-blast** (implement immediately):

| F-ID | Summary | Blast Radius | Confidence | Conf Rationale |
|------|---------|-------------|------------|----------------|

[Apply track empty template if no findings]

**Track 2 -- LOW-confidence / HIGH-blast** (confirm spec interpretation first):

| F-ID | Summary | Blast Radius | Confidence | Conf Rationale |
|------|---------|-------------|------------|----------------|

[Apply track empty template if no findings]

---

**REMEDIATION QUALITY GATE**

Write after Confidence-Stratified Action List. One row per F-ID. No finding absent.

| F-ID | Verb | Target | Location | Conformance | Blast Status |
|------|------|--------|----------|-------------|--------------|

**Verb vocabulary**: GAP -> add/remove; CONTRADICTION -> resolve; ASSUMPTION -> confirm.

**Blast Status**: ORIGINAL for unchanged findings. REASSESSED: [old] -> [new] (P-ID: [P-ID])
for findings elevated by the Re-Assessment Gate.

**Conformance rule**: Falsifiable -- "Confirm that [named behavior] is observable at [named
location] under [named condition]."

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as final section. Multi-part rows: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations, rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary aggregator | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11 + C-34) | [sections fired] | [type + first clause each; include all entity/remediation/blast templates] | fired / not fired |
| Cross-skill comparison (Steps 1, 2, 3) | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 with P-IDs or empty-state | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: fifteen rows present; Sub-claim 2: each row has three sub-observables; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [five per-scope] + T-1 ANNEX | Sub-claim 1: four-term glossary -- cite two labels; Sub-claim 2: T-1 if-and-only-if before sub-skill; Sub-claim 3: Disposition all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs + source -- cite count; Sub-claim 2: Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings with dependency rules cite DR-NN; P2 bidirectional cross-cites verified | fired / partial [sub-claim] / not fired |
| Confidence stratification (C-30, C-35) | Confidence-Stratified Action List + Findings Table | Sub-claim 1: two named tracks present; Sub-claim 2: every HIGH-blast finding assigned; Sub-claim 3: every track finding carries Conf rationale with falsifiable basis | fired / partial [sub-claim] / not fired |
| Type-verb binding (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: every finding carries Type; Sub-claim 2: Verb matches Type vocabulary -- cite any mismatch; Sub-claim 3: no out-of-vocabulary Verb; dual-column confirmation: Findings Table Verb AND Remediation Quality Gate Verb agree | fired / partial [sub-claim] / not fired |
| Propagation coverage (C-29) | Coverage Gate | Sub-claim 1: Coverage Gate present with all DR-NNs; Sub-claim 2: every DR-NN accounted for; Sub-claim 3: gap log entries carry DR-NN ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36 + C-38 + C-39 + C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record Status -- Platform 1-3 before Domain; Sub-claim 2: P1/P2 gate -- P1 names three sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row; N1 + N2 + N3 = N_total; Sub-claim 3: Execution Log Layer column; Platform 1-3, Domain 4-5 | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43) | Execution Log | Sub-claim 1: DR-NN Contributed column in standard five-row Execution Log; Platform rows 1-3 list DR-NN IDs or zero-template; Domain 4-5 carry "n/a"; Sub-claim 2: union of rows 1-3 = full dependency map -- cite union set and confirm match; Sub-claim 3: three-way convergence: Execution Log DR-NN column, P2 gate signal, and Dependency Map all agree | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all five columns (Verb, Target, Location, Conformance, Blast Status) populated -- blank = fail; cite count; Sub-claim 2: Verb matches Type vocabulary every row; mismatches declared as Type-verb bind failures with F-ID; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim; Blast Status = ORIGINAL or REASSESSED with P-ID for every elevated finding | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Entity Coverage Matrix has one row per manifest entity -- cite entity count + confirm matrix row count matches; Sub-claim 2: COVERED cites evidence; CLEAN names sub-skill + reason; SKIPPED has execution gap declaration in this checklist row with entity name and ID; Sub-claim 3: ADDED entities in matrix with annotation -- confirm manifest updated before matrix | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings + Remediation Quality Gate | Sub-claim 1: Re-Assessment Gate table present; one row per P-ID; all columns populated; cite P-ID count; Sub-claim 2: every ELEVATED finding carries inline annotation on Updated Ranked Findings row -- cite F-ID + annotation verbatim; Updated Ranked Findings re-sorted (cite moved finding, or no-elevation template); Sub-claim 3: Remediation Quality Gate Blast Status = REASSESSED for every elevated finding -- confirm by column scan; bidirectional coverage: Re-Assessment Gate flag -> Updated Ranked Findings annotation -> Remediation Quality Gate Blast Status | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof (C-37 + C-40 + C-42 + C-44) | Row Count Assertion block | Sub-claim 1: first sentence embeds count 15 inline -- "the 15th and final of 15 targeted axes" -- cite verbatim; three-way match: opening [15] == table rows [15] == enumerated items [15]; Sub-claim 2: enumerated list ends with "Declaration-completeness-proof axis (this Row Count Assertion block)" as final item -- confirm by name; Sub-claim 3: 15 == 15; self-reference verified from first sentence alone | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration (including Row
Count Assertion block) > EXECUTION ORDER GATE > Observational Discipline > Execution Sequence
(trace-first: 1-3 Platform, gate signal P1+P2, 4-5 Domain) > Cross-Skill Dependency Map >
Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table >
Execution Log (with DR-NN Contributed column) > Entity Coverage Matrix > Initial Ranked Findings
(pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment Gate > Updated
Ranked Findings (post-re-assessment, authoritative) > Coverage Gate > Confidence-Stratified
Action List > Remediation Quality Gate > Structural Compliance Checklist.

If all sections are empty: sub-skill no-findings templates for all five scopes; Entity Coverage
Matrix with CLEAN or SKIPPED for all manifest entities; findings table empty; all four ranked-tier
templates; comparison no-pairs template; Blast Re-Assessment Gate no-patterns template; both
confidence track empty templates; Coverage Gate empty-state; Remediation Quality Gate empty;
Structural Compliance Checklist must fire for all fifteen mechanisms.
