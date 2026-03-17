Written to `simulations/quest/variations/campaign-simulate-variations-R14-2026-03-17.md`.

---

## campaign-simulate — Round 14 Variations

**Context**: R13 V-05 scored 100/100 under rubric v12 — all 21 aspirational criteria passing. R14 explores three new criterion towers surfaced by R13 V-05's excellence signals.

**Round 14 axes chosen:**

| Variation | Axis | New mechanism | Hypothesis |
|-----------|------|---------------|-----------|
| V-01 | Output format | Blast Status column in Remediation Quality Gate | Third independent C-28 verification path scannable without reading Re-Assessment Gate or Updated Ranked Findings |
| V-02 | Role sequence | Verb field in Findings Table at detection time | Cross-artifact C-31 verification: Type-verb binding falsifiable from either the Findings Table or the Remediation Quality Gate independently |
| V-03 | Phrasing register | Examining Sub-Skill column in Topic Entity Manifest | Pre-execution coverage commitment converts passive manifest into falsifiable contract; two-tier SKIPPED signal (commitment-present vs none-declared) |
| V-04 | Output format + role sequence | V-01 + V-02; adds Verb Source column to six-column RQG | Silent Verb mismatches become declared cross-artifact bind failures; Blast Status and Verb Source independently falsifiable in the same row |
| V-05 | Full integration | All three on R13 V-05 15-axis base → 18 axes | Row Count Assertion: "itself the 18th and final of the 18 targeted axes declared below" — C-44 preserved at 18-axis scope; all 21 rubric v12 criteria intact |

**Three new towers opened by R14** (targets for rubric v13):
- **C-28 extension**: Blast Status column as third independent path (C-28 floor → third-path ceiling)
- **C-31 extension**: Findings Table Verb field for cross-artifact binding (C-31 floor → cross-artifact ceiling)
- **C-27 extension**: Examining Sub-Skill commitment with two-tier SKIPPED (C-27 floor → pre-execution-contract ceiling)
nce -- Blast Status column + Findings Table Verb
  field; post-elevation Verb binding persists: REASSESSED Blast Status does not alter Verb,
  cross-artifact C-31 check survives elevation)
- Full integration: V-05 (all three extensions on R13 V-05 fifteen-axis base extended to
  eighteen axes; Row Count Assertion counts to eighteen; C-44 preserved at eighteen-axis scope;
  all R13 V-05 mechanisms intact)

---

## V-01 -- Blast Status Column: Third C-28 Verification Path (output format)

**Variation axis:** Output format -- the Remediation Quality Gate table gains a fifth column:
Blast Status. For every finding, Blast Status is either "ORIGINAL" (blast radius unchanged by
synthesis) or "REASSESSED: [old] -> [new] (P-ID: [P-ID])" (blast radius elevated by a
compounding pattern). A reviewer confirming C-28 compliance can scan the Blast Status column
alone without reading the Blast Radius Re-Assessment Gate section or the Updated Ranked Findings
table. The three verification paths are structurally independent: Re-Assessment Gate table (path
1), inline ELEVATED annotation on Updated Ranked Findings rows (path 2), Blast Status column in
Remediation Quality Gate (path 3).

**Hypothesis:** When C-26 and C-28 are co-targeted, the Remediation Quality Gate row is
mandatory for every finding, making it a natural third verification surface for synthesis
propagation. A reviewer who has confirmed C-26 compliance (Verb/Target/Location/Conformance
populated) can simultaneously confirm C-28 propagation without re-reading the Re-Assessment Gate
section. A mismatch between the Blast Status column and the inline ELEVATED annotation on the
Updated Ranked Findings row is structurally detectable from either artifact. C-27 not
independently extended.

---

Simulate the technical behavior of: {{topic}}

This report enforces twelve structural axes simultaneously. The first section declares all twelve
axes with three independently-verifiable sub-observables each. The last section verifies all
twelve fired using sub-claim decomposition. Both sections are written into the output artifact.

---

**EMPTY-STATE TEMPLATES**

Do not omit any section. Apply the named template when a section has no content.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION
  REQUIRED: either name one rejected observation or justify every candidate is spec-anchored."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N] observations.
  Zero withheld-T1. T-1 SCOPE RECALIBRATION: confirm at least one observation failed T-1 or
  confirm scope is clean."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Cross-skill comparison
  cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list and
  verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates. Reason: [explanation]."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed ([sub-skill]): Zero
  rules declared. DEPENDENCY SCOPE RECALIBRATION: identify a cross-skill constraint or confirm
  clean execution."
- **Execution Order Gate violation**: "EXECUTION ORDER GATE VIOLATION: [name] began before
  Platform Layer complete. C-36 FAIL. Retroactive re-examination required."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED."
- **Blast Re-Assessment Gate no patterns**: "BLAST RADIUS RE-ASSESSMENT GATE: Zero compounding
  patterns (Step 3 empty). Re-assessment cannot proceed. Ranked Findings unchanged."
- **Blast Re-Assessment Gate no elevation**: "BLAST RADIUS RE-ASSESSMENT GATE: [N] patterns
  declared (P-01 through P-[N]). Re-assessment complete. Zero findings elevated. Blast Status
  column: all rows ORIGINAL."
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance | Blast Status. Executed with empty finding set."

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

Verb/Target/Location/Conformance/Blast Status decomposition is in the REMEDIATION QUALITY GATE
section, not inline. The Remediation field carries the narrative.

---

**STRUCTURAL AXIS DECLARATION**

Write as the first section of the output report. All twelve rows require three independently-
verifiable sub-observables.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and rejection count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named empty-state templates; silent sections prohibited | (1) Named template in any section with no results; (2) template type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty |
| Cross-skill comparison axis | C-15 | Three-step protocol: pairings (Step 1), verdicts (Step 2), pattern declaration with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (twelve rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before any execution evidence; (2) Checklist as final section with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope source |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks to map |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record with Status column; P1/P2 gate signal (P2 cross-cites Execution Log DR-NN Contributed by row); Execution Log with Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5 begin; (2) P1 names all three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1 + N2 + N3 = N_total confirmed; (3) Execution Log: Layer column; Platform match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row (not embedded in execution-order axis); DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present in Execution Log; each trace sub-skill step lists contributed DR-NN IDs or zero-contribution template; (2) union of all DR-NN Contributed entries across Execution Log rows 1-3 equals full set of declared DR-NNs in dependency map; (3) compliance checklist verifies this axis from SAD alone, independent of Execution Order Gate section |
| Remediation-quality axis | C-26, C-31 | REMEDIATION QUALITY GATE section with five columns: Verb / Target / Location / Conformance / Blast Status; Verb constrained by Type; Conformance falsifiable; Blast Status is ORIGINAL or REASSESSED | (1) one row per F-ID; all five columns populated -- blank cell = fail; (2) Verb matches Type vocabulary: GAP->add/remove, CONTRADICTION->resolve, ASSUMPTION->confirm; out-of-vocabulary Verb declared as bind failure in compliance checklist with F-ID; (3) Conformance is falsifiable: "Confirm that [named behavior] at [named location] under [named condition]" -- prose summary without named observable = fail |
| Entity-coverage axis | C-27 | Topic Entity Manifest (before execution) + Entity Coverage Matrix (after all sub-skills) with COVERED / CLEAN / SKIPPED per entity | (1) Entity Coverage Matrix: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names examining sub-skill and reason; SKIPPED logged as execution gap in compliance checklist; (2) SKIPPED entities declared in compliance checklist with entity name, ID, and reason; (3) entities discovered during execution appended to manifest with ADDED annotation before matrix |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE fires after Cross-Skill Comparison Step 3; P-IDs drive re-assessment; ELEVATED inline annotation on Updated Ranked Findings; Blast Status column in Remediation Quality Gate | (1) Re-Assessment Gate table: P-ID, participant F-IDs, individual blast radii, compound blast, ELEVATED flag; (2) ELEVATED annotation inline: "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]" on Updated Ranked Findings row; (3) Blast Status column in Remediation Quality Gate: "ORIGINAL" for unchanged findings, "REASSESSED: [old] -> [new] (P-ID: [P-ID])" for elevated findings -- third verification path scannable without reading Re-Assessment Gate section or Updated Ranked Findings |
| Blast-status axis | C-28 extension | Blast Status column as structurally independent third verification path: (a) Blast Status value derivable from Re-Assessment Gate table alone; (b) Blast Status value must equal the ELEVATED annotation direction on the Updated Ranked Findings row for the same F-ID; (c) compliance checklist verifies all three paths are consistent | (1) Blast Status column populated for every finding: ORIGINAL or REASSESSED with direction and P-ID; (2) for every finding flagged ELEVATED in Re-Assessment Gate table, Blast Status column value matches the direction declared in the inline annotation: [old] -> [new] must be identical in both; (3) compliance checklist sub-claim 3 confirms three-path consistency: Gate table ELEVATED flag, Updated Ranked Findings annotation, and Blast Status column -- any mismatch declared as three-path integrity failure with F-ID cited |

---

**TOPIC ENTITY MANIFEST**

Write before the Structural Axis Declaration as the first section of the output report. List every
entity relevant to {{topic}} the simulation must examine.

| Entity ID | Entity Name | Category | Source (spec section or derived) |
|-----------|-------------|----------|----------------------------------|

Entity categories: state-machine / contract-boundary / permission-set / lifecycle-phase /
actor / integration-point

Entities discovered during execution: append with ADDED annotation.

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

**T-1 threshold rule** (before any sub-skill fires): An observation is elevated if and only if
it names a specific spec location AND describes a gap or violation that would cause incorrect
implementation behavior.

**Per-scope Disposition rule**: Zero withheld-T1 triggers RECALIBRATION.

**T-1 ANNEX role**: Summary aggregator only. Not new evidence. Cites per-scope records by scope
name.

---

**EXECUTION SEQUENCE**

Trace-first order. After each Platform sub-skill: update Cross-Skill Dependency Map AND populate
Execution Log DR-NN Contributed column.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with per-sub-skill cross-cites) here]
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
> - Zero-withheld scopes: [list or "none"]

---

**FINDINGS TABLE**

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG**

Populate DR-NN Contributed per sub-skill. Platform rows match P2 gate signal. Domain "n/a."

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | executed / no findings | | | | [DR-NNs or zero-template] |
| trace-contract | Platform | executed / no findings | | | | [DR-NNs or zero-template] |
| trace-permissions | Platform | executed / no findings | | | | [DR-NNs or zero-template] |
| flow-lifecycle | Domain | executed / no findings | | | | n/a |
| flow-conversation | Domain | executed / no findings | | | | n/a |

---

**ENTITY COVERAGE MATRIX**

Write after the Execution Log and before Initial Ranked Findings.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) |
|-----------|-------------|--------|--------------|----------------------------------------|

Status rules: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED (execution gap -- apply Entity SKIPPED gap template; declare in compliance checklist)

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

Label: "RANKED FINDINGS (pre-re-assessment)"

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

[Apply ranked-tier empty-state template for any empty tier]

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1**: | Pair # | F-ID A | F-ID B | Surface similarity |

**Step 2**: | Pair # | F-ID A | F-ID B | Verdict | Reason |

**Step 3 -- Pattern declaration**: Assign stable P-IDs. For each pattern:
- P-ID: [P-01, ...]
- Participant findings: [F-IDs]
- Compounding mechanism: [how findings compound]
- Blast radius implication: [does compound exceed individual blast?]

Apply empty-state template if no patterns.

---

**BLAST RADIUS RE-ASSESSMENT GATE**

Write immediately after the Cross-Skill Comparison Protocol.

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

Re-assessment rule: if Compound Blast > any Participant's Individual Blast, set ELEVATED=YES.
Write ELEVATED annotation inline on Updated Ranked Findings row. Re-sort the table.

Apply Blast Re-Assessment Gate no-patterns template if Step 3 produced zero patterns.
Apply Blast Re-Assessment Gate no-elevation template if patterns exist but no blast increases.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label: "RANKED FINDINGS (post-re-assessment -- authoritative)"

ELEVATED findings carry inline annotation appended to Summary:
```
Summary: [original summary] [ELEVATED: [old] -> [new] (P-ID: [P-ID])]
```

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

Apply empty-state template for zero rules or zero gaps.

---

**REMEDIATION QUALITY GATE**

Write after Coverage Gate, before Structural Compliance Checklist.

Every finding from the Findings Table must appear as exactly one row. A blank cell in any
column is a C-26 fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status |
|------|------|--------|----------|-------------|--------------|

**Verb vocabulary** (constrained by finding Type):
- GAP -> "add" or "remove"
- CONTRADICTION -> "resolve"
- ASSUMPTION -> "confirm"

**Conformance column rule**: "Confirm that [named behavior] is observable at [named location]
under [named condition]." Prose summary without named observable = fail.

**Blast Status column rule**:
- ORIGINAL -- blast radius unchanged by synthesis; no compounding pattern touches this finding
- REASSESSED: [old] -> [new] (P-ID: [P-ID]) -- blast radius elevated; must match the ELEVATED
  annotation direction on this finding's Updated Ranked Findings row exactly

**Three-path consistency**: For every finding with Blast Status = REASSESSED, the declared
direction ([old] -> [new]) must be identical in (1) the Re-Assessment Gate table's Direction
column, (2) the inline ELEVATED annotation on the Updated Ranked Findings row, and (3) the
Blast Status cell in this table. A discrepancy between any two paths is declared as a three-path
integrity failure in the compliance checklist, citing the F-ID and the conflicting values.

If no findings: apply the Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Multi-part rows: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations, rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary aggregator | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template type and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs or empty-state | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twelve rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary -- cite two labels; Sub-claim 2: T-1 if-and-only-if before any sub-skill; Sub-claim 3: Disposition columns all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: map rows carry DR-NN IDs -- cite count; Sub-claim 2: Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings cite Dep rule | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record -- Platform 1-3 before Domain; Sub-claim 2: P1/P2 gate -- P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1 + N2 + N3 confirmed; Sub-claim 3: Execution Log Layer column; Platform match P2; Domain "n/a" | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; Sub-claim 2: union of Contributed entries rows 1-3 equals full dependency map DR-NN set -- cite both counts; Sub-claim 3: this sub-claim verifies the attribution axis from the SAD row alone, independent of the Execution Order Gate section -- cite the SAD row's three sub-observables by name | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26, C-31) | Remediation Quality Gate | Sub-claim 1: one row per F-ID -- no F-ID absent; all five columns (Verb, Target, Location, Conformance, Blast Status) populated; blank cell = fail; cite count; Sub-claim 2: Verb column matches Type vocabulary every row -- cite any out-of-vocabulary Verb as Type-verb bind failure with F-ID; Sub-claim 3: Conformance column is falsifiable -- cite one Conformance cell verbatim to confirm named-observable format | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Entity Coverage Matrix has one row per manifest entity -- cite entity count from manifest and confirm matrix count matches; Sub-claim 2: COVERED cites evidence; CLEAN names sub-skill and reason; SKIPPED entities declared as execution gaps in this checklist row with entity name and ID; Sub-claim 3: entities discovered during execution appear with ADDED annotation -- confirm manifest updated before matrix | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Re-Assessment Gate table present; one row per P-ID; all columns populated; cite P-ID count; Sub-claim 2: every finding flagged ELEVATED in gate table carries inline annotation on Updated Ranked Findings row -- cite F-ID and annotation verbatim; if no elevation: cite applied empty-state template; Sub-claim 3: Updated Ranked Findings labeled authoritative; cite one finding that moved tiers or cite no-elevation template | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status populated for every finding row -- ORIGINAL or REASSESSED with direction and P-ID; cite count of ORIGINAL vs REASSESSED; Sub-claim 2: for each REASSESSED finding, the [old]->[new] direction in Blast Status matches the direction in both the Re-Assessment Gate table Direction column and the Updated Ranked Findings inline ELEVATED annotation -- cite one REASSESSED F-ID and all three values; Sub-claim 3: if no findings were elevated, confirm Blast Status column shows all ORIGINAL and cite the applied no-elevation empty-state template as evidence that the column was still populated | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration > EXECUTION
ORDER GATE > Observational Discipline > Execution Sequence (trace-first) > Cross-Skill
Dependency Map > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX)
> Findings Table > Execution Log > Entity Coverage Matrix > Initial Ranked Findings
(pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment Gate >
Updated Ranked Findings (post-re-assessment, authoritative) > Coverage Gate > Remediation
Quality Gate > Structural Compliance Checklist.

---

## V-02 -- Findings Table Verb Field: Cross-Artifact C-31 Verification (role sequence)

**Variation axis:** Role sequence -- each finding carries a Verb field declared at detection
time (inline in the Findings Table row), before the Remediation Quality Gate is written. The
Verb is constrained by Type at detection: GAP -> "add" or "remove"; CONTRADICTION -> "resolve";
ASSUMPTION -> "confirm". The Remediation Quality Gate still carries its own Verb column. The
compliance checklist verifies that the Findings Table Verb field matches the Remediation Quality
Gate Verb column for every F-ID -- cross-artifact consistency. A Type-verb mismatch is
detectable from either artifact independently.

**Hypothesis:** Declaring the Verb at detection (Findings Table) rather than only at remediation
planning (Remediation Quality Gate) creates a temporal checkpoint: the Type-verb binding is
established during execution, before synthesis. A mismatch between the declared Type and the
detection-time Verb is immediately visible in the Findings Table, independent of whether the
Remediation Quality Gate has been written. The cross-artifact consistency check makes C-31
independently falsifiable from two artifacts: a reviewer who has read only the Findings Table
can verify Type-verb binding without reading the Remediation Quality Gate. C-27 and Blast Status
column not independently extended; Blast Re-Assessment Gate fires but produces no Blast Status
column extension.

---

Simulate the technical behavior of: {{topic}}

This report enforces twelve structural axes simultaneously. The first section declares all twelve
axes. The last section verifies all twelve using sub-claim decomposition.

---

**EMPTY-STATE TEMPLATES**

Use the same templates as V-01 except:
- Remediation Quality Gate empty: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance. Executed with empty finding set."
  (No Blast Status column in this variation.)

All other V-01 empty-state templates apply unchanged.

---

**FINDING SCHEMA**

All fields required. Note: Verb is a new required field at detection time.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Verb:           [add / remove / resolve / confirm -- constrained by Type: GAP->add or remove;
                 CONTRADICTION->resolve; ASSUMPTION->confirm; out-of-vocabulary = bind failure]
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE FIELD: what breaks if unresolved]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Dep rule cite:  [DR-NN if instantiates a dependency rule; "none" otherwise]
Remediation:    [narrative: specific action at named target]
```

**Verb at detection rule**: The Verb field is set when the finding is first recorded. It must
satisfy the Type-verb vocabulary at that moment. An out-of-vocabulary Verb is declared as a
Type-verb bind failure immediately in the per-scope Disposition section where the finding was
elevated -- not deferred to the compliance checklist.

---

**STRUCTURAL AXIS DECLARATION**

All twelve rows, three sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, Disposition zero, Execution Log zero-contribution, Remediation Quality Gate empty |
| Cross-skill comparison axis | C-15 | Three-step protocol with P-IDs | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs or empty-state |
| Declaration-compliance axis | C-17, C-18 | SAD (twelve rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution; (2) Checklist final with sub-claims; (3) evidence cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 rule + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Three-point chain: map, Coverage Gate, finding Dep rule cite | (1) DR-NN IDs in map; (2) Coverage Gate cites DR-NNs; (3) findings backlink |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate with cross-cites; Execution Log Layer column | (1) Layer Completion Record Status: Platform 1-3 before Domain; (2) P1/P2 gate with per-sub-skill attribution and Execution Log cross-cites; (3) Execution Log Layer column; Platform match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column; union-of-rows equality | (1) DR-NN Contributed column in Execution Log; (2) union of rows 1-3 equals full dependency map; (3) compliance checklist verifies from SAD row alone |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance per F-ID; Verb constrained by Type; Conformance falsifiable | (1) one row per F-ID; all four columns populated; (2) Verb matches Type vocabulary; bind failures declared in checklist; (3) Conformance is falsifiable with named observable and location |
| Entity-coverage axis | C-27 | Topic Entity Manifest + Entity Coverage Matrix; COVERED / CLEAN / SKIPPED | (1) Entity Coverage Matrix: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED logged as execution gap; (2) SKIPPED declared in checklist; (3) ADDED entities appended before matrix |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + re-sorted Updated Ranked Findings | (1) Re-Assessment Gate table per P-ID; (2) ELEVATED annotation inline on Updated Ranked Findings; (3) Updated Ranked Findings re-sorted and labeled authoritative |
| Finding-verb axis | C-31 extension | Verb field in Findings Table declared at detection time (before Remediation Quality Gate); cross-artifact consistency: Findings Table Verb must match Remediation Quality Gate Verb column for every F-ID | (1) Verb field present in every finding row in the Findings Table -- no F-ID without Verb; (2) for every F-ID, Findings Table Verb == Remediation Quality Gate Verb column value; a mismatch is declared as a cross-artifact bind failure in the compliance checklist with both values cited; (3) out-of-vocabulary Verb in Findings Table declared as bind failure in the per-scope Disposition section at detection time -- not deferred |

---

**TOPIC ENTITY MANIFEST**

Write as the first section, before the Structural Axis Declaration.

| Entity ID | Entity Name | Category | Source |
|-----------|-------------|----------|--------|

---

**EXECUTION ORDER GATE**, **OBSERVATIONAL DISCIPLINE**, **EXECUTION SEQUENCE**

Same as V-01.

---

**CROSS-SKILL DEPENDENCY MAP** / **CANDIDATE OBSERVATIONS AND FILTER LOG** /
**FILTER LOG RESOLUTION + T-1 ANNEX**

Same schemas as V-01.

---

**FINDINGS TABLE**

Note: Verb column added. Must match Remediation Quality Gate Verb for same F-ID.

| F-ID | Sub-Skill | Type | Verb | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG** / **ENTITY COVERAGE MATRIX** / **INITIAL RANKED FINDINGS** /
**CROSS-SKILL COMPARISON PROTOCOL** / **BLAST RADIUS RE-ASSESSMENT GATE** /
**UPDATED RANKED FINDINGS** / **COVERAGE GATE**

Same as V-01 except: BLAST RADIUS RE-ASSESSMENT GATE does not produce a Blast Status column
in the Remediation Quality Gate (that column is V-01 only).

---

**REMEDIATION QUALITY GATE**

Four columns (no Blast Status column in this variation).

| F-ID | Verb | Target | Location | Conformance |
|------|------|--------|----------|-------------|

**Verb cross-artifact check**: For every F-ID, the Verb in this column must match the Verb
field in the Findings Table row for the same F-ID. A mismatch is declared as a cross-artifact
bind failure in the compliance checklist.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations | [counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template + count; Sub-claim 2: ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 P-IDs or empty-state | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: twelve rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map; Sub-claim 2: Coverage Gate cites; Sub-claim 3: findings cite | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Sub-claim 2: P1/P2 with per-sub-skill Execution Log cross-cites; Sub-claim 3: Execution Log Layer column | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; Sub-claim 2: union equals full map; Sub-claim 3: verifiable from SAD row alone | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; four columns; no blanks; Sub-claim 2: Verb matches Type vocabulary; Sub-claim 3: Conformance is falsifiable | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: one row per manifest entity -- counts match; Sub-claim 2: COVERED cites evidence; CLEAN names sub-skill; SKIPPED declared as gap here; Sub-claim 3: ADDED entities appear with annotation | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Re-Assessment Gate table; Sub-claim 2: ELEVATED inline annotations; Sub-claim 3: Updated Ranked Findings labeled authoritative | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field present in every Findings Table row -- cite count; no F-ID without Verb; Sub-claim 2: cross-artifact consistency -- for every F-ID, Findings Table Verb == Remediation Quality Gate Verb; cite one F-ID and both values as evidence; declare any mismatch as cross-artifact bind failure with F-ID and conflicting values; Sub-claim 3: out-of-vocabulary Verb in Findings Table declared at detection in per-scope Disposition section -- cite one example or confirm none occurred | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration > EXECUTION
ORDER GATE > Observational Discipline > Execution Sequence (trace-first) > Cross-Skill
Dependency Map > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX)
> Findings Table (with Verb column) > Execution Log > Entity Coverage Matrix > Initial Ranked
Findings (pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment
Gate > Updated Ranked Findings (post-re-assessment, authoritative) > Coverage Gate > Remediation
Quality Gate > Structural Compliance Checklist.

---

## V-03 -- Examining Sub-Skill Commitment in Manifest: Pre-Execution Coverage Contract (phrasing register)

**Variation axis:** Phrasing register -- the Topic Entity Manifest carries a fifth column:
Examining Sub-Skill. Before execution begins, each entity is assigned the sub-skill that will
examine it. This converts the manifest from a passive inventory into a pre-execution coverage
commitment. The compliance checklist verifies: (1) every entity with an Examining Sub-Skill
designation has a COVERED or CLEAN status in the Entity Coverage Matrix; (2) SKIPPED entities
whose Examining Sub-Skill was declared produce a stronger compliance gap signal than SKIPPED
entities with "none-declared"; (3) entities discovered during execution carry "ADDED -- post-
execution" in the Examining Sub-Skill column.

**Hypothesis:** A manifest that commits to which sub-skill examines each entity before execution
creates a falsifiable pre-execution contract. The Entity Coverage Matrix row for each entity
must be consistent with its manifest commitment: an entity whose commitment named trace-state
but ended as SKIPPED must declare both the commitment and the failure in the compliance
checklist. This is structurally stronger than C-27's current model (manifest exists; matrix
exists) because it makes the examining sub-skill choice an auditable decision, not an
undocumented implementation detail. C-26 and C-28 are in the base but not independently
extended.

---

Simulate the technical behavior of: {{topic}}

This report enforces twelve structural axes simultaneously. The first section declares all twelve
axes. The last section verifies all twelve using sub-claim decomposition.

---

**EMPTY-STATE TEMPLATES**

Same as V-01 except:
- **Manifest no examining commitment**: "TOPIC ENTITY MANIFEST: Entity [name] (E-[NN]) has no
  Examining Sub-Skill committed. Coverage outcome is CLEAN or SKIPPED only -- cannot be COVERED
  without prior commitment unless ADDED annotation present."
- **Commitment-outcome mismatch**: "COMMITMENT OUTCOME MISMATCH: Entity [name] (E-[NN])
  committed to [sub-skill] but status = SKIPPED. Examining sub-skill did not execute this entity.
  Compliance gap declared below."

All V-01 templates apply otherwise.

---

**FINDING SCHEMA**

Same as V-01 (no Verb field; Verb is in Remediation Quality Gate only).

---

**STRUCTURAL AXIS DECLARATION**

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log; Filter Log Resolution | (1) Candidate Observations: Elevate? + Rejection Reason; (2) Filter Log Resolution: template + count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11, C-34 | Named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in checklist; (3) sections: sub-skill, ranked tiers, comparison, both Blast Gate states, Disposition zero, Execution Log zero-contribution, manifest no-commitment, commitment-mismatch |
| Cross-skill comparison axis | C-15 | Three-step protocol with P-IDs | (1) Step 1: pairs; (2) Step 2: verdicts; (3) Step 3: P-IDs or empty-state |
| Declaration-compliance axis | C-17, C-18 | SAD (twelve rows) + Compliance Checklist | (1) SAD before execution; (2) Checklist final with sub-claims; (3) evidence cites actual sections |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if; (2) five per-scope tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Map, Coverage Gate, finding Dep rule cite | (1) DR-NN IDs in map; (2) Coverage Gate cites; (3) findings backlink |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate; Execution Log Layer column | (1) Layer Completion Record Status; (2) P1/P2 gate with per-sub-skill cross-cites; (3) Execution Log Layer column |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column; union equality | (1) DR-NN Contributed column; (2) union equals full map; (3) verifiable from SAD row alone |
| Remediation-quality axis | C-26, C-31 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status per F-ID | (1) one row per F-ID; five columns; no blanks; (2) Verb matches Type; bind failures declared; (3) Conformance is falsifiable |
| Blast-reassessment axis | C-28 | Re-Assessment Gate + ELEVATED inline + re-sorted Updated Ranked Findings | (1) Re-Assessment Gate table; (2) ELEVATED inline annotation; (3) Updated Ranked Findings labeled authoritative |
| Entity-coverage axis | C-27 | Topic Entity Manifest + Entity Coverage Matrix | (1) one row per manifest entity in matrix; (2) status per entity; SKIPPED declared as gap; (3) ADDED entities appended before matrix |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in Topic Entity Manifest; commitment-to-outcome verification in Compliance Checklist; two-tier SKIPPED signal (committed vs not-committed) | (1) Examining Sub-Skill column present in manifest; every entity has a value (sub-skill name or "none-declared"); entities with "none-declared" cannot become COVERED through normal execution -- only through ADDED annotation; (2) for every entity with a declared Examining Sub-Skill, the Entity Coverage Matrix row's status is COVERED, CLEAN, or SKIPPED with a commitment-mismatch declaration naming both the committed sub-skill and the SKIPPED outcome; (3) compliance checklist distinguishes two-tier SKIPPED: (a) commitment-present-SKIPPED: stronger gap, examining sub-skill failed to execute; (b) none-declared-SKIPPED: weaker gap, entity was never committed; cite one example of each tier present or confirm only one tier exists |

---

**TOPIC ENTITY MANIFEST**

Write as the first section, before the Structural Axis Declaration.

| Entity ID | Entity Name | Category | Source | Examining Sub-Skill |
|-----------|-------------|----------|--------|---------------------|

**Examining Sub-Skill values**: one of the five sub-skill names, or "none-declared" if the entity
cannot be pre-assigned. "none-declared" entities may not become COVERED in the normal execution
path (only through an ADDED annotation or opportunistic detection).

**ADDED entities**: discovered during execution. Append with "ADDED -- post-execution" in the
Examining Sub-Skill column.

If no examining commitments can be made: apply the Manifest no-examining-commitment template
for each unassigned entity.

---

**EXECUTION ORDER GATE**, **OBSERVATIONAL DISCIPLINE**, **EXECUTION SEQUENCE**

Same as V-01.

---

**CROSS-SKILL DEPENDENCY MAP** / **CANDIDATE OBSERVATIONS AND FILTER LOG** /
**FILTER LOG RESOLUTION + T-1 ANNEX** / **FINDINGS TABLE** / **EXECUTION LOG**

Same schemas as V-01 (Findings Table has no Verb column in this variation).

---

**ENTITY COVERAGE MATRIX**

Write after the Execution Log, before Initial Ranked Findings. For each entity with a declared
Examining Sub-Skill, note whether the commitment was honored:

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence | Commitment Honored? |
|-----------|-------------|--------|--------------|----------|---------------------|

**Commitment Honored?** values:
- YES -- entity has a declared Examining Sub-Skill and status is COVERED or CLEAN
- MISMATCH -- entity has a declared Examining Sub-Skill but status is SKIPPED; apply
  Commitment-outcome mismatch template inline
- N/A -- entity had "none-declared" in manifest

---

**INITIAL RANKED FINDINGS** / **CROSS-SKILL COMPARISON PROTOCOL** / **BLAST RADIUS
RE-ASSESSMENT GATE** / **UPDATED RANKED FINDINGS** / **COVERAGE GATE** / **REMEDIATION
QUALITY GATE**

Same as V-01 (Remediation Quality Gate includes Blast Status column as in V-01 base).

---

**STRUCTURAL COMPLIANCE CHECKLIST**

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations | [counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template + count; Sub-claim 2: ANNEX; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates | [sections] | [type and first clause] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: twelve rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings | Sub-claim 1: DR-NNs in map; Sub-claim 2: Coverage Gate; Sub-claim 3: findings | fired / partial [sub-claim] / not fired |
| Execution-order axis | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Sub-claim 2: P1/P2; Sub-claim 3: Execution Log Layer | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis | Execution Log | Sub-claim 1: DR-NN Contributed; Sub-claim 2: union equals map; Sub-claim 3: SAD-row-only verifiable | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26, C-31) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; five columns; Sub-claim 2: Verb matches Type; Sub-claim 3: Conformance falsifiable | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Gate table; Sub-claim 2: ELEVATED annotations; Sub-claim 3: authoritative label | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: one row per manifest entity; Sub-claim 2: status per entity; SKIPPED declared; Sub-claim 3: ADDED appear with annotation | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column present; every entity has a value (sub-skill or none-declared); cite count of each; Sub-claim 2: every entity with a declared sub-skill has Commitment Honored? = YES, MISMATCH, or N/A -- no entity with a declared sub-skill has a blank Commitment Honored? field; cite the count of each value; Sub-claim 3: two-tier SKIPPED distinction -- cite one commitment-present-SKIPPED and one none-declared-SKIPPED entity if both exist; if only one tier: confirm which tier is present and cite entity name; if zero SKIPPED: cite "zero SKIPPED entities; two-tier distinction did not fire" | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest (with Examining Sub-Skill column) > Structural
Axis Declaration > EXECUTION ORDER GATE > Observational Discipline > Execution Sequence
(trace-first) > Cross-Skill Dependency Map > Candidate Observations and Filter Log > Filter Log
Resolution (with T-1 ANNEX) > Findings Table > Execution Log > Entity Coverage Matrix (with
Commitment Honored? column) > Initial Ranked Findings (pre-re-assessment) > Cross-Skill
Comparison Protocol > Blast Radius Re-Assessment Gate > Updated Ranked Findings
(post-re-assessment, authoritative) > Coverage Gate > Remediation Quality Gate > Structural
Compliance Checklist.

---

## V-04 -- Blast Status Column + Findings Table Verb Field (output format + role sequence)

**Variation axes:** Output format + role sequence combined -- V-01's Blast Status column merged
with V-02's Findings Table Verb field. The Remediation Quality Gate carries six columns:
Verb / Target / Location / Conformance / Blast Status / Verb Source. The Verb Source column
declares whether the Verb value was carried forward unchanged from the Findings Table Verb field
("DETECTION: [Verb]") or was corrected at remediation planning ("CORRECTED: [Findings Table
Verb] -> [RQG Verb]; bind failure declared"). The six-column gate makes both the Blast Status
propagation and the cross-artifact Verb consistency auditable from the gate table alone.

**Hypothesis:** Combining Blast Status (third C-28 path) with the Findings Table Verb field
(cross-artifact C-31 check) does not degrade either mechanism. The Verb Source column adds a
fourth dimension: it surfaces detection-time Verb corrections at the remediation planning stage,
converting silent mismatches into declared bind failures. A reviewer scanning the Verb Source
column can identify all cross-artifact Verb mismatches without comparing the Findings Table and
the Remediation Quality Gate row-by-row. C-27 commitment model not targeted.

---

Simulate the technical behavior of: {{topic}}

This report enforces thirteen structural axes simultaneously. The first section declares all
thirteen. The last section verifies all thirteen using sub-claim decomposition.

---

**EMPTY-STATE TEMPLATES**

Use V-01 templates plus:
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source. Executed with
  empty finding set."

---

**FINDING SCHEMA**

Same as V-02 (includes Verb field at detection time).

---

**STRUCTURAL AXIS DECLARATION**

Thirteen rows: axes 1-11 identical to V-01. Axis 12 = finding-verb axis (V-02 definition).
Axis 13 = blast-status axis (V-01 definition) with one additional observable:

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| [axes 1-11 same as V-01] | | | |
| Finding-verb axis | C-31 extension | Verb in Findings Table at detection; cross-artifact consistency with RQG Verb; Verb Source column in RQG surfaces corrections | (1) Verb field in every Findings Table row; (2) Verb Source column in RQG: DETECTION:[Verb] if unchanged, CORRECTED:[old]->[new] if mismatch; any CORRECTED entry is declared as cross-artifact bind failure in compliance checklist; (3) for every F-ID, Findings Table Verb and RQG Verb column are consistent -- CORRECTED entries document the discrepancy rather than silently overwriting |
| Blast-status axis | C-28 extension | Blast Status in RQG (sixth column) as third independent C-28 path; three-path consistency check with Gate table and Updated Ranked Findings | (1) Blast Status populated for every row: ORIGINAL or REASSESSED:[old]->[new](P-ID); (2) REASSESSED direction matches Gate table Direction AND Updated Ranked Findings ELEVATED annotation for same F-ID; (3) compliance checklist sub-claim 3: three-path consistency confirmed or any mismatch declared with F-ID and conflicting values |

---

**TOPIC ENTITY MANIFEST**, **EXECUTION ORDER GATE**, **OBSERVATIONAL DISCIPLINE**,
**EXECUTION SEQUENCE**, **CROSS-SKILL DEPENDENCY MAP**, **CANDIDATE OBSERVATIONS AND FILTER
LOG**, **FILTER LOG RESOLUTION + T-1 ANNEX**

Same as V-01.

---

**FINDINGS TABLE**

Includes Verb column (from V-02).

| F-ID | Sub-Skill | Type | Verb | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG** / **ENTITY COVERAGE MATRIX** / **INITIAL RANKED FINDINGS** /
**CROSS-SKILL COMPARISON PROTOCOL** / **BLAST RADIUS RE-ASSESSMENT GATE** /
**UPDATED RANKED FINDINGS** / **COVERAGE GATE**

Same as V-01.

---

**REMEDIATION QUALITY GATE**

Six columns. Every F-ID must appear. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb Source column rule**:
- "DETECTION: [Verb]" -- Verb is unchanged from the Findings Table Verb field
- "CORRECTED: [FT Verb] -> [RQG Verb]; bind failure declared in compliance checklist" -- the
  Verb was changed at remediation planning; the correction is a bind failure, not a silent fix

**Three-path C-28 consistency** (same as V-01): REASSESSED Blast Status direction must match
Gate table and Updated Ranked Findings annotation for same F-ID.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Thirteen rows. Axes 1-10 same as V-01. Axis 11 (blast-status) same as V-01. Plus:

| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field present in every Findings Table row -- cite count; Sub-claim 2: Verb Source column: cite count of DETECTION vs CORRECTED; every CORRECTED entry declared as cross-artifact bind failure -- cite F-ID and both values or confirm zero corrections; Sub-claim 3: no silent Verb mismatches -- every difference between Findings Table Verb and RQG Verb appears as a CORRECTED Verb Source entry; confirm by stating the count of CORRECTED entries matches the count of F-IDs where FT Verb != RQG Verb | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration > EXECUTION
ORDER GATE > Observational Discipline > Execution Sequence (trace-first) > Cross-Skill
Dependency Map > Candidate Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX)
> Findings Table (with Verb column) > Execution Log > Entity Coverage Matrix > Initial Ranked
Findings (pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment
Gate > Updated Ranked Findings (post-re-assessment, authoritative) > Coverage Gate > Remediation
Quality Gate (six columns) > Structural Compliance Checklist.

---

## V-05 -- Full Integration: All Three Extensions on R13 V-05 Fifteen-Axis Base (eighteen axes)

**Variation axes:** Full integration -- V-01's Blast Status column, V-02's Findings Table Verb
field, and V-03's Examining Sub-Skill manifest commitment applied simultaneously on the R13 V-05
fifteen-axis base. The SAD is promoted to eighteen rows. The Row Count Assertion opening
sentence reads: "This Row Count Assertion, itself the 18th and final of the 18 targeted axes
declared below, is C-37's completeness proof." C-44 is preserved at eighteen-axis scope. All
R13 V-05 mechanisms (confidence stratification, type-verb binding, propagation coverage,
declaration-completeness-proof, Blast Status column, cross-artifact Verb, commitment model)
are present and cross-verified.

**Hypothesis:** The three new mechanisms are independently additive and do not degrade each
other. The Blast Status column interacts with the Findings Table Verb field through the
Remediation Quality Gate: REASSESSED findings still have their Verb bound by Type; the Blast
Status column and the Verb Source column are independently falsifiable in the same row. The
manifest commitment interacts with the Entity Coverage Matrix, whose COVERED entries must be
consistent with the committed Examining Sub-Skill. All three new mechanisms open new criterion
towers: Blast Status is the third-path ceiling of C-28; Findings Table Verb is the
cross-artifact ceiling of C-31; Manifest Commitment is the pre-execution-contract ceiling of
C-27. Scoring under rubric v12 (max 100) will confirm all 21 established aspirational criteria
remain intact.

---

Simulate the technical behavior of: {{topic}}

This report enforces eighteen structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 18th and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all eighteen axes fired using sub-claim decomposition. All three
sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

All templates from V-01 plus:
- **Manifest no examining commitment**: "TOPIC ENTITY MANIFEST: Entity [name] (E-[NN]) has no
  Examining Sub-Skill committed. Status may be CLEAN or SKIPPED only."
- **Commitment-outcome mismatch**: "COMMITMENT OUTCOME MISMATCH: Entity [name] (E-[NN])
  committed to [sub-skill]; status = SKIPPED. Compliance gap declared."
- **Finding-verb mismatch**: "FINDING-VERB MISMATCH: F-[NN] Findings Table Verb = [value];
  Remediation Quality Gate Verb = [value]. Cross-artifact bind failure declared in compliance
  checklist."
- **Confidence-stratification action tracks empty**: "CONFIDENCE-STRATIFIED ACTION LIST:
  No HIGH-blast findings to stratify. Action track schema: Track | F-ID | Confidence | Conf
  Rationale | Action."

---

**FINDING SCHEMA**

All fields required. Verb field declared at detection time.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Verb:           [add / remove / resolve / confirm -- constrained by Type]
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only]
Impact:         [STANDALONE FIELD]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Confidence:     [HIGH / LOW -- required for cross-skill or system-wide only]
Conf rationale: [REQUIRED when Confidence present: basis for HIGH or LOW judgment]
Dep rule cite:  [DR-NN or "none"]
Remediation:    [narrative: specific action at named target]
```

---

**TOPIC ENTITY MANIFEST**

Write as the absolute first section of the output report -- before the Structural Axis
Declaration. This commits the entity coverage contract before any structural declaration.

| Entity ID | Entity Name | Category | Source | Examining Sub-Skill |
|-----------|-------------|----------|--------|---------------------|

Examining Sub-Skill: one of the five sub-skill names, or "none-declared". ADDED entities
discovered during execution: append with "ADDED -- post-execution".

---

**STRUCTURAL AXIS DECLARATION**

Write immediately after the Topic Entity Manifest. Eighteen rows required, three independently-
verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 before any row |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero, Execution Log zero-contribution, all four Remediation Quality Gate empty states, manifest commitment, mismatch templates |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs or empty-state |
| Declaration-compliance axis | C-17, C-18 | SAD (eighteen rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 (if-and-only-if) + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope sources |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map, Coverage Gate, finding Dep rule cite | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks |
| Confidence-stratification axis | C-30, C-35 | Confidence-Stratified Action List with two named tracks (HIGH-confidence/HIGH-blast and LOW-confidence/HIGH-blast); Conf rationale required per finding in list | (1) two named action tracks present; findings assigned by confidence x blast-radius quadrant; (2) every finding in either track carries both Confidence label and Conf rationale; Conf rationale is falsifiable -- cites spec section or observable evidence; (3) findings below HIGH-blast threshold not in list -- confirm they are excluded with count |
| Type-verb binding axis | C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary declared; Verb field in Findings Table at detection time; Verb column in Remediation Quality Gate; cross-artifact consistency enforced | (1) Verb field present in every Findings Table row; Type-verb vocabulary enforced at detection: GAP->add/remove, CONTRADICTION->resolve, ASSUMPTION->confirm; out-of-vocabulary Verb declared as bind failure in per-scope Disposition section at detection time; (2) Verb Source column in Remediation Quality Gate: DETECTION:[Verb] if unchanged, CORRECTED:[old]->[new] if mismatch -- every CORRECTED entry is a declared cross-artifact bind failure; (3) compliance checklist verifies cross-artifact consistency from Verb Source column alone: count of CORRECTED entries == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate accounts for all declared dependency rules: honored (finding recorded, rule cited) or OPEN PROPAGATION GAP (rule ID + reason) | (1) Coverage Gate present with one row per declared DR-NN; (2) every DR-NN from dependency map appears in Coverage Gate rows or OPEN PROPAGATION GAP log -- {declared DR-NNs} == {gate rows union gap log}; (3) OPEN PROPAGATION GAP entries carry rule ID and reason for non-execution |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record (Status column); P1/P2 gate signal with per-sub-skill cross-cites; Execution Log Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5; (2) P1 names all three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1 + N2 + N3 = N_total confirmed; (3) Execution Log Layer column; Platform rows match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row (not embedded in execution-order axis); DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present; each trace step lists contributed DR-NNs or zero-contribution template; (2) union of Contributed entries rows 1-3 equals full dependency map DR-NN set -- cite both counts; (3) compliance checklist verifies this axis from the SAD row alone, independent of the Execution Order Gate section |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; all six columns populated -- blank cell = fail; (2) Verb matches Type vocabulary; Verb Source column documents DETECTION or CORRECTED; (3) Conformance is falsifiable: "Confirm that [named behavior] at [named location] under [named condition]" |
| Entity-coverage axis | C-27 | Topic Entity Manifest (first section, before SAD) + Entity Coverage Matrix (after all sub-skills); COVERED / CLEAN / SKIPPED per entity | (1) Entity Coverage Matrix: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED logged as execution gap in compliance checklist; (2) SKIPPED declared in compliance checklist with entity name, ID, reason; (3) ADDED entities appended with annotation before matrix written |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + Blast Status column in Remediation Quality Gate | (1) Re-Assessment Gate table: one row per P-ID; all columns populated; (2) ELEVATED annotation inline on Updated Ranked Findings: "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]"; (3) Updated Ranked Findings re-sorted by re-assessed blast radius; labeled authoritative; cite one finding that moved tiers or cite no-elevation template |
| Blast-status axis | C-28 extension | Third independent C-28 verification path: Blast Status column in Remediation Quality Gate scannable without reading Re-Assessment Gate section or Updated Ranked Findings | (1) Blast Status populated for every row: ORIGINAL or REASSESSED:[old]->[new](P-ID); (2) REASSESSED direction matches Gate table Direction column AND Updated Ranked Findings ELEVATED annotation -- all three paths consistent; any discrepancy declared as three-path integrity failure with F-ID and conflicting values; (3) compliance checklist confirms three-path consistency from Blast Status column alone: cite one REASSESSED F-ID and all three values, or confirm all ORIGINAL and cite the no-elevation template |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in Topic Entity Manifest; Commitment Honored? column in Entity Coverage Matrix; two-tier SKIPPED distinction in compliance checklist | (1) Examining Sub-Skill column present; every entity has a value (sub-skill name or none-declared); cite count of committed vs none-declared; (2) every entity with a declared sub-skill has Commitment Honored? = YES, MISMATCH (with mismatch template), or N/A; no entity with a declared sub-skill has a blank Commitment Honored? field; (3) two-tier SKIPPED distinction: commitment-present-SKIPPED (stronger gap) vs none-declared-SKIPPED (weaker gap) -- cite one example of each tier or confirm only one tier exists |
| Finding-verb axis | C-31 extension | Verb field in Findings Table declared at detection; Verb Source column in Remediation Quality Gate; cross-artifact consistency verifiable from either artifact independently | (1) Verb field in every Findings Table row; count cited; (2) Verb Source column: count of DETECTION vs CORRECTED; every CORRECTED entry declared as cross-artifact bind failure; (3) no silent mismatches: count of CORRECTED Verb Source entries equals count of F-IDs where Findings Table Verb != RQG Verb -- cite the count and confirm equality |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 18th and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 18th and final of the 18 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42: this assertion is C-37's completeness proof) and count invariant (C-44: 18th and final of 18); both properties verifiable at zero-scan scope from one sentence without further reading; (2) enumerated list of all 18 targeted axes by name follows the opening sentence; "Declaration-completeness-proof axis (this Row Count Assertion block)" appears as item 18 in that list (C-40); (3) row count in SAD == 18 == count of targeted quality criteria for this simulation run; count mismatch in either direction = C-37 fail |

---

**EXECUTION ORDER GATE**

Same as V-01.

---

**OBSERVATIONAL DISCIPLINE**

Same as V-01.

---

**EXECUTION SEQUENCE**

Trace-first order. During each sub-skill: update Cross-Skill Dependency Map, populate Execution
Log DR-NN Contributed, note which manifest entities are examined, and declare Verb for any
elevated finding at detection time.

1. trace-state
2. trace-contract
3. trace-permissions
   [Write EXECUTION ORDER GATE signal (P1 + P2 with cross-cites) here]
4. flow-lifecycle
5. flow-conversation

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason | Filter rule |
|-------|-----------------|------------|-----------|-------------|

---

**CROSS-SKILL DEPENDENCY MAP**

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

**Template A / Template B** (same as V-01).

**T-1 ANNEX** (same as V-01).

---

**FINDINGS TABLE**

Verb column present. Declared at detection, before Remediation Quality Gate.

| F-ID | Sub-Skill | Type | Verb | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|------|--------------|---------|--------|-------------|---------------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Layer | Status | Candidates | Rejected | Finding IDs | DR-NN Contributed |
|-----------|-------|--------|------------|---------|-------------|-------------------|
| trace-state | Platform | | | | | [DR-NNs or zero-template] |
| trace-contract | Platform | | | | | [DR-NNs or zero-template] |
| trace-permissions | Platform | | | | | [DR-NNs or zero-template] |
| flow-lifecycle | Domain | | | | | n/a |
| flow-conversation | Domain | | | | | n/a |

---

**ENTITY COVERAGE MATRIX**

Write after Execution Log, before Initial Ranked Findings.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence | Commitment Honored? |
|-----------|-------------|--------|--------------|----------|---------------------|

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

Label: "RANKED FINDINGS (pre-re-assessment)"
Tiers 1-4. Empty-state template per empty tier.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Step 1 / Step 2 / Step 3 (same as V-01).

---

**BLAST RADIUS RE-ASSESSMENT GATE**

Same as V-01.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

ELEVATED findings carry: `[ELEVATED: [old] -> [new] (P-ID: [P-ID])]` inline.

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Write after Coverage Gate, before Remediation Quality Gate.

**Track 1 -- HIGH-confidence / HIGH-blast: Implement Fix Immediately**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

**Track 2 -- LOW-confidence / HIGH-blast: Confirm Spec Interpretation First**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

Apply confidence-stratification empty template if no HIGH-blast findings exist.

---

**REMEDIATION QUALITY GATE**

Six columns. Every finding must appear. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary** (GAP->add/remove; CONTRADICTION->resolve; ASSUMPTION->confirm).
**Conformance**: "Confirm that [behavior] at [location] under [condition]."
**Blast Status**: ORIGINAL or REASSESSED:[old]->[new](P-ID).
**Verb Source**: DETECTION:[Verb] or CORRECTED:[FT Verb]->[RQG Verb]; bind failure declared.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Eighteen rows. Multi-part: `fired / partial [sub-claim] / not fired`.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations | [counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template + count; Sub-claim 2: ANNEX total + example + source; Sub-claim 3: ANNEX is summary | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template type and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 P-IDs or empty-state | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: eighteen rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five scopes | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: Coverage Gate cites DR-NNs; {map} == {gate union gap log}; Sub-claim 3: findings cite Dep rule | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks present; findings assigned by confidence x blast; Sub-claim 2: every finding in either track carries Confidence label and non-empty Conf rationale -- cite one Conf rationale verbatim; Sub-claim 3: non-HIGH-blast findings excluded -- cite count excluded | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field in every Findings Table row -- cite count; Type-verb vocabulary enforced at detection; Sub-claim 2: Verb Source column -- cite count of DETECTION vs CORRECTED; CORRECTED entries declared as cross-artifact bind failures; Sub-claim 3: count of CORRECTED Verb Source entries == count of F-IDs where FT Verb != RQG Verb -- cite count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: Coverage Gate present; Sub-claim 2: {declared DR-NNs} == {gate rows union gap log}; Sub-claim 3: OPEN PROPAGATION GAPentries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record -- Platform 1-3 before Domain; Sub-claim 2: P1/P2 gate -- P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1 + N2 + N3 confirmed; Sub-claim 3: Execution Log Layer column; Platform match P2; Domain "n/a" | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; each trace step lists DR-NNs or zero-template; Sub-claim 2: union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; Sub-claim 3: this axis verified from SAD row alone, independent of Execution Order Gate section -- cite SAD row's three sub-observables by name | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns (Verb, Target, Location, Conformance, Blast Status, Verb Source) populated; blank cell = fail; cite count; Sub-claim 2: Verb column matches Type vocabulary; Verb Source documents all mismatches; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Entity Coverage Matrix has one row per manifest entity -- cite entity count from manifest; confirm matrix count matches; Sub-claim 2: COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED declared as execution gap in this checklist row with entity name, ID, reason; Sub-claim 3: entities discovered during execution appear in matrix with ADDED annotation -- confirm manifest updated before matrix | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Re-Assessment Gate table; one row per P-ID; all columns populated; cite P-ID count; Sub-claim 2: every ELEVATED finding carries inline annotation on Updated Ranked Findings row -- cite F-ID and annotation verbatim; if no elevation: cite applied empty-state template; Sub-claim 3: Updated Ranked Findings labeled authoritative; cite one finding that moved tiers or confirm no-elevation template applied | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status populated for every row: ORIGINAL or REASSESSED with direction and P-ID; cite count of ORIGINAL vs REASSESSED; Sub-claim 2: for each REASSESSED finding, direction in Blast Status == direction in Gate table Direction column == direction in Updated Ranked Findings ELEVATED annotation -- cite one REASSESSED F-ID and all three values; any discrepancy = three-path integrity failure declared with F-ID and conflicting values; Sub-claim 3: if no findings elevated: all rows ORIGINAL; cite no-elevation empty-state template as evidence column was populated | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column present; every entity has a value; cite count of committed vs none-declared; Sub-claim 2: every committed entity has Commitment Honored? = YES, MISMATCH (with template), or N/A; no blank Commitment Honored? for committed entities; cite count of each value; Sub-claim 3: two-tier SKIPPED distinction declared -- cite one commitment-present-SKIPPED and one none-declared-SKIPPED entity if both exist; if only one tier: state which tier and cite entity name; if zero SKIPPED: cite "zero SKIPPED; two-tier distinction did not fire" | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field present in every Findings Table row -- cite count; Sub-claim 2: Verb Source count of DETECTION vs CORRECTED; every CORRECTED entry declared as cross-artifact bind failure with both values; Sub-claim 3: count of CORRECTED == count of F-IDs where FT Verb != RQG Verb -- cite the count and confirm equality; if zero: confirm all DETECTION and cite count | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | Structural Axis Declaration + this Row Count Assertion block | This Row Count Assertion, itself the 18th and final of the 18 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence simultaneously declares self-reference ("this Row Count Assertion is C-37's completeness proof") and count invariant ("18th and final of 18") -- both C-37 and C-42 verifiable from the opening sentence at zero-scan scope; Sub-claim 2 (C-40): enumerated list of all 18 targeted axes by name follows; "Declaration-completeness-proof axis" appears as item 18 in that list -- C-37 axis self-cites within the proof; Sub-claim 3 (C-37): row count in SAD == 18 == count of targeted quality criteria; counted targeted axes: Filtering (1), Empty-state (2), Cross-skill comparison (3), Declaration-compliance (4), Observational discipline (5), DR-NN citation chain (6), Confidence-stratification (7), Type-verb binding (8), Propagation coverage (9), Execution-order (10), Execution-log attribution (11), Remediation-quality (12), Entity-coverage (13), Blast-reassessment (14), Blast-status (15), Manifest-commitment (16), Finding-verb (17), Declaration-completeness-proof (18) | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest (with Examining Sub-Skill column) > Structural
Axis Declaration (eighteen rows) > EXECUTION ORDER GATE > Observational Discipline > Execution
Sequence (trace-first) > Cross-Skill Dependency Map > Candidate Observations and Filter Log >
Filter Log Resolution (with T-1 ANNEX) > Findings Table (with Verb column) > Execution Log >
Entity Coverage Matrix (with Commitment Honored? column) > Initial Ranked Findings
(pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment Gate >
Updated Ranked Findings (post-re-assessment, authoritative) > Coverage Gate >
Confidence-Stratified Action List > Remediation Quality Gate (six columns) > Structural
Compliance Checklist (eighteen rows).
