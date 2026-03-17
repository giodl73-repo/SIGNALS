Written to `simulations/quest/variations/campaign-simulate-variations-R15-2026-03-17.md`.

---

## campaign-simulate — Round 15 Variations

**Context**: R14 V-05 as 18-axis base. R15 targets C-47, C-48, C-49 (rubric v13).

**Axes chosen:**

| Variation | Axis | New mechanism | Hypothesis |
|-----------|------|---------------|------------|
| V-01 | Output format | Column-scan verification note on FT Verb column (C-47) | Making "column-scan sufficient" an explicit declared assertion creates a new falsifiable property: a finding whose Verb requires narrative reading fails C-47 even if it passes C-31 |
| V-02 | Output format | SKIPPED-T1 / SKIPPED-T2 tier labels in ECM Status cells (C-48) | Embedding tier labels in the Status cell makes the two-tier distinction scannable from the ECM Status column without cross-referencing the Examining Sub-Skill column |
| V-03 | Role sequence | Verb Source carries F-ID back-cite to originating FT row (C-49) | F-ID in Verb Source creates bidirectional chain: discrepancy detectable by tracing forward from FT or backward from VerbSource.back-cite |
| V-04 | Output format + role sequence | V-01 + V-03: C-47 + C-49 combined (20 axes) | Column-scan note and F-ID back-cite operate on disjoint surfaces; independently additive |
| V-05 | Full integration | All three on 18-axis base → 21 axes | Three mechanisms on disjoint surfaces; Row Count Assertion at 21; all R14 V-05 mechanisms intact |

**New tower openings:**
- C-47 → **column-scan sufficiency ceiling**: checklist enumerates (F-ID, Verb) pairs from both columns with no narrative read; sufficiency is a declared, falsifiable assertion
- C-48 → **Status-scannable tier ceiling**: tier label in Status cell; derivable from Status column alone without Examining Sub-Skill cross-reference
- C-49 → **full bidirectional-chain ceiling**: Verb Source carries F-ID back-cite; chain traversable forward (FT→RQG→VerbSource) and backward (VerbSource.F-NN→FT); break detectable from either endpoint
otes from 18 to 21; all 18 R14 V-05 mechanisms remain intact |

**Three new towers opened by R15** (targets for rubric v14):
- **C-47 → column-scan sufficiency ceiling**: compliance checklist sub-claim explicitly enumerates (F-ID, Verb) column pairs without reading narrative; sufficiency is a declared, falsifiable assertion
- **C-48 → Status-scannable tier ceiling**: tier labels in ECM Status cell; tier derivation rule explicit; tier distinction requires no column cross-reference
- **C-49 → full bidirectional-chain ceiling**: Verb Source cell carries F-ID back-cite; chain traversable in both directions; break detectable from either endpoint

---

## V-01 -- Column-Scan Verification: FT Verb as C-47 Surface (output format)

**Variation axis:** Output format -- the Findings Table Verb field carries an explicit
"COLUMN-SCAN SURFACE (C-47)" annotation in the schema. This annotation declares which columns
are scanned (FT Verb, RQG Verb), which fields are excluded from the scan (Summary, Impact,
Remediation, BR rationale, Conf rationale), and that C-47 compliance is verifiable by
column scan alone. The finding-verb axis (axis 17) continues to enforce cross-artifact
consistency via the Verb Source mechanism; the column-scan verification axis (axis 18) adds
the structural proof that no narrative field is required. The Row Count Assertion promotes
from 18 to 19.

**Hypothesis:** Separating the consistency check (finding-verb axis, cross-artifact Verb ==
Verb) from the scanability proof (column-scan verification axis, no narrative reading) creates
a strictly stronger invariant. The compliance checklist sub-claim for the column-scan axis
enumerates all (F-ID, Verb) pairs from FT and RQG explicitly, then declares the scan
sufficient. C-48 and C-49 are not extended; the R14 V-05 manifest-commitment (axis 16) and
Verb Source format (axis 17) remain exactly as specified.

---

Simulate the technical behavior of: {{topic}}

This report enforces nineteen structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 19th and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all nineteen axes fired using sub-claim decomposition. All three
sections are written by the model into the output artifact.

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
- **Comparison step with no pairs**: "No findings from multiple sub-skills. Cross-skill
  comparison cannot proceed."
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
  F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source. Executed with
  empty finding set."
- **Manifest no examining commitment**: "TOPIC ENTITY MANIFEST: Entity [name] (E-[NN]) has no
  Examining Sub-Skill committed. Status may be CLEAN or SKIPPED only."
- **Commitment-outcome mismatch**: "COMMITMENT OUTCOME MISMATCH: Entity [name] (E-[NN])
  committed to [sub-skill]; status = SKIPPED. Compliance gap declared."
- **Finding-verb mismatch**: "FINDING-VERB MISMATCH: F-[NN] Findings Table Verb = [value];
  Remediation Quality Gate Verb = [value]. Cross-artifact bind failure declared."
- **Confidence-stratification action tracks empty**: "CONFIDENCE-STRATIFIED ACTION LIST: No
  HIGH-blast findings to stratify. Action track schema: Track | F-ID | Confidence | Conf
  Rationale | Action."
- **Column-scan surface note (empty findings)**: "COLUMN-SCAN SURFACE VERIFICATION: No findings
  elevated. FT Verb column: empty. RQG Verb column: empty. Column scan complete: zero pairs.
  C-47 verified by column scan; no narrative field read."

---

**FINDING SCHEMA**

All fields required. Verb field declared at detection time and labeled as column-scan surface.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Verb:           [add / remove / resolve / confirm -- constrained by Type: GAP->add or remove;
                 CONTRADICTION->resolve; ASSUMPTION->confirm; out-of-vocabulary = bind failure
                 declared in per-scope Disposition at detection time]
                 COLUMN-SCAN SURFACE (C-47): this Verb field contributes to the FT Verb column.
                 C-47 compliance is verified by scanning FT Verb column vs RQG Verb column
                 row-by-row. No narrative field is read during a C-47 scan. Excluded: Summary,
                 Impact, Remediation, BR rationale, Conf rationale.
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only -- EXCLUDED from C-47 column scan]
Impact:         [STANDALONE FIELD -- EXCLUDED from C-47 column scan]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide -- EXCLUDED from C-47 column scan]
Confidence:     [HIGH / LOW -- required for cross-skill or system-wide]
Conf rationale: [REQUIRED when Confidence present -- EXCLUDED from C-47 column scan]
Dep rule cite:  [DR-NN or "none"]
Remediation:    [narrative: specific action at named target -- EXCLUDED from C-47 column scan]
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

Write immediately after the Topic Entity Manifest. Nineteen rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty, manifest commitment, mismatch templates, column-scan empty findings |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (nineteen rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope source records |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks to map |
| Confidence-stratification axis | C-30, C-35 | Confidence-Stratified Action List with two named tracks; Conf rationale required per finding | (1) two named action tracks present; findings assigned by confidence x blast-radius quadrant; (2) every finding in either track carries Confidence label and falsifiable Conf rationale citing spec section or observable evidence; (3) findings below HIGH-blast threshold excluded -- cite count excluded |
| Type-verb binding axis | C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary declared; Verb field in FT at detection; Verb column in RQG; cross-artifact consistency enforced | (1) Verb field in every FT row; Type-verb vocabulary enforced at detection: GAP->add/remove, CONTRADICTION->resolve, ASSUMPTION->confirm; out-of-vocabulary Verb declared as bind failure in per-scope Disposition at detection time; (2) Verb Source column in RQG: DETECTION:[Verb] if unchanged, CORRECTED:[old]->[new] if mismatch; CORRECTED entry = declared cross-artifact bind failure; (3) compliance checklist verifies cross-artifact consistency from Verb Source column: count of CORRECTED entries == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate accounts for all declared dependency rules: honored (finding recorded, rule cited) or OPEN PROPAGATION GAP (rule ID + reason) | (1) Coverage Gate present with one row per declared DR-NN; (2) {declared DR-NNs} == {gate rows union gap log}; (3) OPEN PROPAGATION GAP entries carry rule ID and reason for non-execution |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record (Status column); P1/P2 gate signal with per-sub-skill cross-cites; Execution Log Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5 begin; (2) P1 names all three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; (3) Execution Log Layer column; Platform rows match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row (not embedded in execution-order axis); DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present; each trace step lists contributed DR-NNs or zero-contribution template; (2) union of Contributed entries rows 1-3 equals full dependency map DR-NN set -- cite both counts; (3) compliance checklist verifies this axis from the SAD row alone, independent of the Execution Order Gate section |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; all six columns populated -- blank cell = fail; cite count; (2) Verb matches Type vocabulary; Verb Source documents DETECTION or CORRECTED; (3) Conformance is falsifiable: "Confirm that [named behavior] at [named location] under [named condition]" -- prose summary without named observable = fail |
| Entity-coverage axis | C-27 | Topic Entity Manifest (first section, before SAD) + Entity Coverage Matrix (after all sub-skills); COVERED / CLEAN / SKIPPED per entity | (1) ECM: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED logged as execution gap; (2) SKIPPED declared in compliance checklist with entity name, ID, reason; (3) ADDED entities appended with annotation before matrix written |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + Blast Status column in RQG | (1) Re-Assessment Gate table: one row per P-ID; all columns populated; (2) ELEVATED annotation inline on Updated Ranked Findings: "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]"; (3) Updated Ranked Findings re-sorted by re-assessed blast radius; labeled authoritative |
| Blast-status axis | C-28 extension | Third independent C-28 verification path: Blast Status column in RQG scannable without reading Re-Assessment Gate or Updated Ranked Findings | (1) Blast Status populated for every row: ORIGINAL or REASSESSED:[old]->[new](P-ID); (2) REASSESSED direction matches Gate table Direction column AND Updated Ranked Findings ELEVATED annotation -- three-path consistent; discrepancy = declared three-path integrity failure with F-ID and conflicting values; (3) compliance checklist confirms three-path consistency from Blast Status column alone: cite one REASSESSED F-ID and all three values, or confirm all ORIGINAL and cite no-elevation template |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in TEM; Commitment Honored? column in ECM; two-tier SKIPPED distinction in compliance checklist | (1) Examining Sub-Skill column present; every entity has a value (sub-skill name or none-declared); cite count committed vs none-declared; (2) every entity with a declared sub-skill has Commitment Honored? = YES, MISMATCH (with mismatch template inline), or N/A; no blank Commitment Honored? for committed entities; cite count of each; (3) two-tier SKIPPED in checklist: commitment-present-SKIPPED (stronger gap) vs none-declared-SKIPPED (weaker gap) -- cite one of each or confirm only one tier exists |
| Finding-verb axis | C-31 extension | Verb field in FT declared at detection; Verb Source column in RQG; cross-artifact consistency verifiable from either artifact independently | (1) Verb field in every FT row -- cite count; no F-ID without Verb; (2) Verb Source: count of DETECTION vs CORRECTED; every CORRECTED entry declared as cross-artifact bind failure with both values; (3) count of CORRECTED Verb Source entries == count of F-IDs where FT Verb != RQG Verb -- cite count and confirm equality; if zero: confirm all DETECTION and cite count |
| Column-scan verification axis | C-47 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist enumerates all (F-ID, Verb) pairs from FT and RQG without reading any narrative field; scan declared sufficient | (1) schema note "COLUMN-SCAN SURFACE (C-47)" present in Verb field definition before any finding is recorded; note names included columns (FT Verb, RQG Verb) and excluded fields (Summary, Impact, Remediation, BR rationale, Conf rationale); (2) compliance checklist sub-claim 2: all FT (F-ID, Verb) pairs listed explicitly; all RQG (F-ID, Verb) pairs listed explicitly; set equality declared; no narrative field referenced in the enumeration; if any narrative field was required to resolve a Verb value, the F-ID is cited and the scan is declared insufficient; (3) compliance checklist sub-claim 3 declares verbatim: "column-scan declared sufficient; C-47 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" -- this declaration is the proof; if the declaration cannot be made without qualification, C-47 fails |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 19th and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 19th and final of the 19 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42: this assertion is C-37's completeness proof) and count invariant (C-44: 19th and final of 19) -- both verifiable at zero-scan scope from one sentence; (2) enumerated list of all 19 targeted axes by name follows; "Declaration-completeness-proof axis (this Row Count Assertion block)" appears as item 19; (3) row count in SAD == 19 == count of targeted quality criteria; 19 targeted axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), Declaration-completeness-proof(19) |

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

**T-1 ANNEX role**: Summary aggregator only. Not new evidence. Cites per-scope records.

---

**EXECUTION SEQUENCE**

Trace-first order. During each sub-skill: update Cross-Skill Dependency Map, populate
Execution Log DR-NN Contributed, note which manifest entities are examined, and declare
Verb for any elevated finding at detection time.

1. trace-state       -- state transitions: preconditions, postconditions, invariants
2. trace-contract    -- contract boundary: expected vs actual
3. trace-permissions -- RBAC trace: privilege escalation detection
   [Write EXECUTION ORDER GATE signal (P1 + P2 with per-sub-skill cross-cites) here]
4. flow-lifecycle    -- lifecycle trace: phase contracts and exception flows
5. flow-conversation -- conversation simulation: dead-end and loop detection

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|-----------------------------|---------------------------------|

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

Verb column present. Declared at detection time, labeled as COLUMN-SCAN SURFACE (C-47).

| F-ID | Sub-Skill | Type | Verb | Spec Location | Summary | Impact | Blast Radius | Dep Rule Cite | Remediation |
|------|-----------|------|------|--------------|---------|--------|-------------|---------------|-------------|

Column note (write once, above the table): "Verb column -- COLUMN-SCAN SURFACE (C-47): scan
this column against RQG Verb column to verify C-47; no narrative field read required."

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

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

Status values: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED (execution gap -- declare in compliance checklist)

Commitment Honored? values: YES / MISMATCH (apply mismatch template inline) / N/A

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

Label: "RANKED FINDINGS (pre-re-assessment)"

**Tier 1 -- System-Wide** / **Tier 2 -- Cross-Skill** / **Tier 3 -- Component-Wide** /
**Tier 4 -- Isolated**

Apply ranked-tier empty-state template for any empty tier.

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

Write after Confidence-Stratified Action List, before Structural Compliance Checklist.

Every finding from the Findings Table must appear as exactly one row. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary** (constrained by finding Type):
- GAP -> "add" or "remove"
- CONTRADICTION -> "resolve"
- ASSUMPTION -> "confirm"

**Conformance column rule**: "Confirm that [named behavior] is observable at [named location]
under [named condition]." Prose without named observable = fail.

**Blast Status column rule**:
- ORIGINAL -- blast radius unchanged by synthesis
- REASSESSED: [old] -> [new] (P-ID: [P-ID]) -- must match ELEVATED annotation direction

**Verb Source column rule**:
- DETECTION: [Verb] -- Verb unchanged from FT Verb field
- CORRECTED: [FT Verb] -> [RQG Verb]; bind failure declared in compliance checklist

**Three-path C-28 consistency**: For every REASSESSED finding, the [old]->[new] direction must
be identical in (1) Re-Assessment Gate table Direction column, (2) inline ELEVATED annotation
on Updated Ranked Findings, and (3) Blast Status cell in this table. Discrepancy between any
two paths = declared three-path integrity failure in compliance checklist with F-ID.

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Nineteen rows. Multi-part: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + rejection count; Sub-claim 2: T-1 ANNEX total + example + source scope; Sub-claim 3: ANNEX declared as summary aggregator only | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs named or empty-state template applied | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: nineteen rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary -- cite two labels; Sub-claim 2: T-1 if-and-only-if stated before any sub-skill; Sub-claim 3: Disposition columns present in all five per-scope tables | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings cite Dep rule backlink | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks present; findings assigned by confidence x blast quadrant; Sub-claim 2: every finding in either track carries Confidence label and falsifiable Conf rationale -- cite one Conf rationale verbatim; Sub-claim 3: non-HIGH-blast findings excluded -- cite count excluded | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field in every FT row -- cite count; Type-verb vocabulary enforced at detection; Sub-claim 2: Verb Source column -- cite count of DETECTION vs CORRECTED; CORRECTED entries declared as bind failures; Sub-claim 3: count of CORRECTED == count of F-IDs where FT Verb != RQG Verb -- cite count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: Coverage Gate present; one row per declared DR-NN; Sub-claim 2: {declared DR-NNs} == {gate rows union gap log} -- cite both sets; Sub-claim 3: OPEN PROPAGATION GAP entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record -- Platform 1-3 complete before Domain; Sub-claim 2: P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; Sub-claim 3: Execution Log Layer column; Platform rows match P2; Domain "n/a" | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; Sub-claim 2: union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; Sub-claim 3: this axis verified from SAD row alone, independent of Execution Order Gate section -- cite the SAD row's three sub-observables by name | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns (Verb, Target, Location, Conformance, Blast Status, Verb Source) populated; blank = fail; cite count; Sub-claim 2: Verb matches Type vocabulary every row; Verb Source documents all mismatches; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim to confirm named-observable format | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: ECM has one row per manifest entity -- cite entity count from manifest; confirm matrix count matches; Sub-claim 2: COVERED cites evidence; CLEAN names sub-skill and reason; SKIPPED declared as execution gap in this row with entity name and ID; Sub-claim 3: ADDED entities appear with annotation in ECM -- confirm manifest updated before matrix written | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Re-Assessment Gate table; one row per P-ID; all columns populated; cite P-ID count; Sub-claim 2: every ELEVATED finding carries inline annotation on Updated Ranked Findings row -- cite F-ID and annotation verbatim; if no elevation: cite applied empty-state template; Sub-claim 3: Updated Ranked Findings labeled authoritative; cite one finding that moved tiers or confirm no-elevation template applied | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status populated for every row: ORIGINAL or REASSESSED with direction and P-ID; cite count of ORIGINAL vs REASSESSED; Sub-claim 2: for each REASSESSED finding, direction in Blast Status == direction in Gate table Direction column == direction in Updated Ranked Findings ELEVATED annotation -- cite one REASSESSED F-ID and all three values; any discrepancy = three-path integrity failure declared with F-ID; Sub-claim 3: if no findings elevated: confirm all ORIGINAL; cite no-elevation template as evidence column was populated | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column present; every entity has a value; cite count committed vs none-declared; Sub-claim 2: every committed entity has Commitment Honored? = YES, MISMATCH (with template), or N/A; no blank for committed entities; cite count of each; Sub-claim 3: two-tier SKIPPED: commitment-present-SKIPPED (stronger gap) vs none-declared-SKIPPED (weaker gap) -- cite one of each tier or confirm only one tier exists; if zero SKIPPED: cite "zero SKIPPED; two-tier distinction did not fire" | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field present in every FT row -- cite count; no F-ID without Verb; Sub-claim 2: Verb Source count of DETECTION vs CORRECTED; every CORRECTED entry declared as cross-artifact bind failure -- cite F-ID and both values or confirm zero corrections; Sub-claim 3: count of CORRECTED Verb Source entries == count of F-IDs where FT Verb != RQG Verb -- cite count and confirm equality; if zero: confirm all DETECTION | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47) | Findings Table + Remediation Quality Gate | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present in FT Verb column definition -- cite verbatim; confirm note names included columns (FT Verb, RQG Verb) and excluded fields (Summary, Impact, Remediation, BR rationale, Conf rationale); Sub-claim 2: column-scan enumeration performed here: list all FT (F-ID, Verb) pairs; list all RQG (F-ID, Verb) pairs; declare set equality; confirm no narrative field referenced in this enumeration -- if any narrative field was required, cite the F-ID and declare scan insufficient; Sub-claim 3: column-scan sufficiency declaration: "C-47 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" -- this verbatim declaration is the proof; if the declaration cannot be made without qualification, C-47 fails | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 19th and final of the 19 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference (this assertion is C-37's completeness proof) and count invariant (19th and final of 19) -- both verifiable at zero-scan scope; Sub-claim 2 (C-40): enumerated list of 19 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), Declaration-completeness-proof(19); "Declaration-completeness-proof axis" appears as item 19; Sub-claim 3 (C-37): row count in SAD == 19 == count of targeted quality criteria; count mismatch in either direction = C-37 fail | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest (with Examining Sub-Skill column) >
Structural Axis Declaration (nineteen rows) > EXECUTION ORDER GATE > Observational Discipline
> Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate Observations and
Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table (with Verb column,
COLUMN-SCAN SURFACE note) > Execution Log > Entity Coverage Matrix (with Commitment Honored?
column) > Initial Ranked Findings (pre-re-assessment) > Cross-Skill Comparison Protocol >
Blast Radius Re-Assessment Gate > Updated Ranked Findings (post-re-assessment, authoritative)
> Coverage Gate > Confidence-Stratified Action List > Remediation Quality Gate (six columns)
> Structural Compliance Checklist (nineteen rows).

---

## V-02 -- SKIPPED Tier Labels: Two-Tier Gap Signal in ECM Status Cells (output format)

**Variation axis:** Output format -- ECM Status cells for SKIPPED entities carry explicit tier
labels directly in the Status value: "SKIPPED-T1 (commitment-present)" for entities whose
Examining Sub-Skill was declared but not honored, and "SKIPPED-T2 (none-declared)" for
entities whose Examining Sub-Skill was "none-declared". The tier label makes the two-tier
distinction scannable from the ECM Status column alone, without cross-referencing the
Examining Sub-Skill column. The manifest-commitment axis (axis 16) continues to enforce the
commitment-contract mechanism; the SKIPPED-tier axis (axis 18) adds the structural proof that
tier derivation is column-local. The Row Count Assertion promotes from 18 to 19.

**Hypothesis:** Embedding the tier label in the Status cell rather than in a compliance
checklist narrative converts the two-tier distinction into a column-scannable signal: a
reviewer confirms C-48 compliance by scanning the Status column for SKIPPED entries and
reading the tier label in the cell, without looking up the entity's Examining Sub-Skill
commitment. A SKIPPED entry with no tier label fails C-48 even if the checklist declares the
tier correctly. C-47 and C-49 are not independently extended; V-01's column-scan note and
V-01's Verb Source format remain as in R14 V-05.

---

Simulate the technical behavior of: {{topic}}

This report enforces nineteen structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 19th and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all nineteen axes fired using sub-claim decomposition. All three
sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

All templates from V-01 plus:
- **SKIPPED-T1 entity**: "ENTITY COVERAGE: Entity [name] (E-[NN]) status = SKIPPED-T1
  (commitment-present). Examining Sub-Skill [sub-skill] was committed but did not execute this
  entity. Promise-breach gap declared in compliance checklist."
- **SKIPPED-T2 entity**: "ENTITY COVERAGE: Entity [name] (E-[NN]) status = SKIPPED-T2
  (none-declared). No pre-execution commitment was made for this entity. Planning gap declared
  in compliance checklist."

Replace V-01's Remediation Quality Gate empty template:
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source. Executed with
  empty finding set." (unchanged from V-01)

---

**FINDING SCHEMA**

Same as V-01.

---

**STRUCTURAL AXIS DECLARATION**

Nineteen rows. Axes 1-17 same as V-01. Axis 18 = SKIPPED-tier axis (new). Axis 19 =
Declaration-completeness-proof (updated count).

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| [Axes 1-17 identical to V-01] | | | |
| SKIPPED-tier axis | C-48 | ECM Status cell carries explicit tier label for every SKIPPED entry: SKIPPED-T1 (commitment-present) or SKIPPED-T2 (none-declared); tier derivation rule explicit; tier distinction scannable from Status column without cross-referencing Examining Sub-Skill column | (1) ECM Status values for SKIPPED entities are exactly "SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)"; a bare "SKIPPED" without tier label = C-48 fail; tier derivation rule stated above ECM table: T1 if Examining Sub-Skill != "none-declared"; T2 if Examining Sub-Skill == "none-declared"; (2) tier distinction is column-local: a reviewer scanning only the Status column can identify all SKIPPED entries and their tier without reading the Examining Sub-Skill column -- confirm by stating the count of T1 and T2 entries derivable from Status column alone; (3) compliance checklist SKIPPED-tier sub-claim 3 declares gap severity order: T1 (promise-breach gap, stronger) ranks above T2 (planning gap, weaker); cite one T1 entity and one T2 entity if both exist, or confirm which tier is present; if zero SKIPPED: cite "zero SKIPPED; tier labels did not fire" |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 19th and final targeted axis | This Row Count Assertion, itself the 19th and final of the 19 targeted axes declared below, is C-37's completeness proof: (1) opening sentence declares self-reference and count invariant (19th and final of 19) -- both verifiable at zero-scan scope; (2) enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), SKIPPED-tier(18), Declaration-completeness-proof(19); item 19 is this block; (3) row count in SAD == 19 |

---

**TOPIC ENTITY MANIFEST**, **EXECUTION ORDER GATE**, **OBSERVATIONAL DISCIPLINE**,
**EXECUTION SEQUENCE**, **CROSS-SKILL DEPENDENCY MAP**, **CANDIDATE OBSERVATIONS AND FILTER
LOG**, **FILTER LOG RESOLUTION + T-1 ANNEX**, **FINDINGS TABLE**, **EXECUTION LOG**

Same as V-01.

---

**ENTITY COVERAGE MATRIX**

Write after Execution Log, before Initial Ranked Findings.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

**Status values**:
- COVERED -- cite F-ID or Obs #
- CLEAN -- name examining sub-skill and reason
- SKIPPED-T1 (commitment-present) -- entity had a declared Examining Sub-Skill that was not
  honored; apply SKIPPED-T1 template inline; declare in compliance checklist
- SKIPPED-T2 (none-declared) -- entity had "none-declared" Examining Sub-Skill; apply
  SKIPPED-T2 template inline; declare in compliance checklist

**Tier derivation rule** (write above the matrix):
> T1 if Examining Sub-Skill column != "none-declared" and entity is SKIPPED.
> T2 if Examining Sub-Skill column == "none-declared" and entity is SKIPPED.
> Tier derivable from Status column alone without reading Examining Sub-Skill column.

**Commitment Honored?**: YES / MISMATCH (with mismatch template) / N/A

---

**INITIAL RANKED FINDINGS** through **COVERAGE GATE** / **CONFIDENCE-STRATIFIED ACTION LIST**
/ **REMEDIATION QUALITY GATE**

Same as V-01.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Nineteen rows. Axes 1-17 same as V-01. Row 18 = SKIPPED-tier axis. Row 19 = updated
Declaration-completeness-proof.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| [Rows 1-17 same as V-01 compliance checklist rows] | | | |
| SKIPPED-tier axis (C-48) | Entity Coverage Matrix | Sub-claim 1: all SKIPPED Status cells carry tier labels -- every SKIPPED entry is either "SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)"; a bare "SKIPPED" = C-48 fail; cite count of T1 vs T2; Sub-claim 2: tier derivation rule stated above ECM table -- T1 if Examining Sub-Skill != "none-declared"; T2 if == "none-declared"; confirm tier derivable from Status column without reading Examining Sub-Skill column: "scanning the Status column, I can identify [N] SKIPPED-T1 and [N] SKIPPED-T2 entities without cross-referencing the Examining Sub-Skill column"; Sub-claim 3: gap severity declared: T1 (promise-breach gap -- examining sub-skill committed but did not execute) ranks above T2 (planning gap -- no commitment made); cite one T1 entity by name or confirm zero T1; cite one T2 entity by name or confirm zero T2; if zero SKIPPED: "zero SKIPPED; SKIPPED-tier labels did not fire" | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 19th and final of the 19 targeted axes declared below, is C-37's completeness proof: Sub-claim 1: opening sentence declares self-reference and count invariant (19th and final of 19) -- zero-scan verifiable; Sub-claim 2: enumerated list of 19 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), SKIPPED-tier(18), Declaration-completeness-proof(19); Sub-claim 3: row count in SAD == 19 | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest (with Examining Sub-Skill column) >
Structural Axis Declaration (nineteen rows) > EXECUTION ORDER GATE > Observational Discipline
> Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate Observations and
Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table (with Verb column) >
Execution Log > Entity Coverage Matrix (with SKIPPED-T1/SKIPPED-T2 tier labels and
Commitment Honored? column) > Initial Ranked Findings (pre-re-assessment) > Cross-Skill
Comparison Protocol > Blast Radius Re-Assessment Gate > Updated Ranked Findings
(post-re-assessment, authoritative) > Coverage Gate > Confidence-Stratified Action List >
Remediation Quality Gate (six columns) > Structural Compliance Checklist (nineteen rows).

---

## V-03 -- Verb Source F-ID Back-Cite: Three-Point Bidirectional Chain (role sequence)

**Variation axis:** Role sequence -- the RQG Verb Source column format changes to carry an
explicit F-ID back-citation to the originating Findings Table row. Format:
"DETECTION: FT[F-NN].Verb=[Verb]" (Verb unchanged) or
"CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared" (Verb changed at remediation
planning). The F-NN in the Verb Source cell must match the F-ID of the RQG row in which it
appears. This creates the three-point bidirectional chain: FT[F-NN].Verb (at detection) -->
RQG[F-NN].Verb (at remediation planning) --> VerbSource.back-cites(FT[F-NN]). A discrepancy
is structurally detectable from either endpoint: forward from FT, or backward from the
VerbSource back-cite. The Row Count Assertion promotes from 18 to 19.

**Hypothesis:** The existing Verb Source format ("DETECTION: [Verb]") establishes a
unidirectional link from RQG to a type-verb vocabulary check. Adding the F-ID back-cite creates
a bidirectional link: the VerbSource cell names its originating FT row, so a reviewer at the
RQG can trace backward to the exact FT row and verify the Verb was correctly carried forward.
A chain break (wrong F-NN, or F-NN not found in FT) is detectable from the VerbSource cell
alone. C-47 and C-48 are not independently extended.

---

Simulate the technical behavior of: {{topic}}

This report enforces nineteen structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 19th and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all nineteen axes fired using sub-claim decomposition. All three
sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

All templates from V-01, with one replacement:
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source. Verb Source
  format: DETECTION: FT[F-NN].Verb=[Verb]. Executed with empty finding set."

---

**FINDING SCHEMA**

Same as V-01 (Verb field has COLUMN-SCAN SURFACE note; this note is carried forward unchanged).

---

**STRUCTURAL AXIS DECLARATION**

Nineteen rows. Axes 1-17 same as V-01. Axis 18 = Verb-source chain axis (new). Axis 19 =
Declaration-completeness-proof (updated count).

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| [Axes 1-17 identical to V-01] | | | |
| Verb-source chain axis | C-49 | RQG Verb Source column carries explicit F-ID back-cite to originating FT row; three-point bidirectional chain: FT[F-NN].Verb at detection --> RQG[F-NN].Verb at remediation --> VerbSource.back-cites(FT[F-NN]); chain break detectable from either endpoint | (1) Verb Source column format: every cell is exactly "DETECTION: FT[F-NN].Verb=[Verb]" or "CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared"; the F-NN in the Verb Source cell must match the F-ID of the RQG row in which it appears; a Verb Source cell without an F-ID back-cite = C-49 fail; (2) three-point chain verifiable in both directions: (a) forward: from FT row F-NN, read Verb; locate RQG row F-NN, confirm Verb; read VerbSource, confirm back-cite names F-NN; (b) backward: from VerbSource cell, read F-NN; locate FT row F-NN, read Verb; confirm chain is intact; compliance checklist sub-claim 2 traces one complete chain (forward or backward) citing all three points by section and value; (3) chain break declared: if the F-NN in a Verb Source cell does not match the RQG row's F-ID, or if the Verb cited in VerbSource does not match the FT row's Verb, declare a chain break in the compliance checklist with the F-ID, the expected value, and the actual value |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 19th and final targeted axis | This Row Count Assertion, itself the 19th and final of the 19 targeted axes declared below, is C-37's completeness proof: (1) opening sentence declares self-reference and count invariant (19th and final of 19); (2) enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Verb-source chain(18), Declaration-completeness-proof(19); item 19 is this block; (3) row count in SAD == 19 |

---

**TOPIC ENTITY MANIFEST** through **EXECUTION LOG** / **ENTITY COVERAGE MATRIX** through
**COVERAGE GATE** / **CONFIDENCE-STRATIFIED ACTION LIST**

Same as V-01.

---

**REMEDIATION QUALITY GATE**

Six columns. Verb Source column format updated for F-ID back-cite.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary**, **Conformance rule**, **Blast Status rule**: same as V-01.

**Verb Source column rule** (updated for C-49):
- DETECTION: FT[F-NN].Verb=[Verb] -- Verb unchanged from FT row F-NN; F-NN must match this
  RQG row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared in compliance checklist --
  Verb changed at remediation planning; F-NN must match this RQG row's F-ID; the chain
  break between FT Verb [old] and RQG Verb [new] is the declared bind failure

**Three-point chain rule**: For every row, the F-NN cited in the Verb Source cell must equal
the F-ID of that row. A mismatch between the Verb Source F-NN and the row F-ID is a chain
break, declared in the compliance checklist with both values.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Nineteen rows. Rows 1-17 same as V-01. Row 18 = Verb-source chain. Row 19 = updated
Declaration-completeness-proof.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| [Rows 1-17 same as V-01 compliance checklist] | | | |
| Verb-source chain axis (C-49) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb Source format confirmed: every cell is "DETECTION: FT[F-NN].Verb=[Verb]" or "CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared"; cite one Verb Source cell verbatim; confirm F-NN in cell matches row F-ID; Sub-claim 2: three-point chain traced for one F-ID: cite FT row F-ID and Verb; cite RQG row F-ID and Verb; cite Verb Source cell and confirm F-NN back-cite matches; declare chain intact or cite chain break with F-ID, expected value, and actual value; Sub-claim 3: chain break audit: for every CORRECTED Verb Source entry, confirm the F-NN cited matches the RQG row F-ID and that the [old] value matches the FT row Verb; cite count of CORRECTED entries and confirm zero chain breaks, or declare each break | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 19th and final of the 19 targeted axes declared below, is C-37's completeness proof: Sub-claim 1: opening sentence declares self-reference and count invariant (19th and final of 19); Sub-claim 2: enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Verb-source chain(18), Declaration-completeness-proof(19); Sub-claim 3: row count in SAD == 19 | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration (nineteen
rows) > EXECUTION ORDER GATE > Observational Discipline > Execution Sequence (trace-first) >
Cross-Skill Dependency Map > Candidate Observations and Filter Log > Filter Log Resolution
(with T-1 ANNEX) > Findings Table (with Verb column) > Execution Log > Entity Coverage Matrix
(with Commitment Honored? column) > Initial Ranked Findings (pre-re-assessment) > Cross-Skill
Comparison Protocol > Blast Radius Re-Assessment Gate > Updated Ranked Findings
(post-re-assessment, authoritative) > Coverage Gate > Confidence-Stratified Action List >
Remediation Quality Gate (six columns, Verb Source with F-ID back-cite) > Structural
Compliance Checklist (nineteen rows).

---

## V-04 -- Column-Scan + Verb Source Chain: C-47 + C-49 Combined (output format + role sequence)

**Variation axes:** Output format + role sequence combined -- V-01's column-scan verification
note on the FT Verb column merged with V-03's F-ID back-cite in the RQG Verb Source column.
The full type-verb-source chain is: FT[F-NN].Verb (column-scan surface, C-47) --> RQG[F-NN].Verb
(remediation planning) --> VerbSource.DETECTION:FT[F-NN].Verb=[Verb] (C-49 back-cite). A
reviewer can verify the chain by scanning from either endpoint without reading narrative fields.
C-48 (SKIPPED tier labels) is not independently extended. Row Count Assertion promotes to 20.

**Hypothesis:** The two mechanisms operate on disjoint surfaces: the column-scan note is in the
FT schema (read during detection-time recording) while the F-ID back-cite is in the RQG Verb
Source cell (written at remediation planning). Combining them does not create interaction
effects: REASSESSED blast-radius elevations do not alter Verb values, so the C-28 three-path
consistency check and the C-49 chain remain independently falsifiable in the same RQG row. The
compliance checklist carries separate sub-claims for each mechanism and a combined chain trace.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column). The second section is the Structural Axis
Declaration, which is itself the 20th and final declared axis. The last section is the
Structural Compliance Checklist, which verifies all twenty axes fired using sub-claim
decomposition.

---

**EMPTY-STATE TEMPLATES**

All templates from V-01, with one replacement:
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source. Verb Source
  format: DETECTION: FT[F-NN].Verb=[Verb]. Executed with empty finding set."
- **Column-scan surface note (empty findings)**: same as V-01.

---

**FINDING SCHEMA**

Same as V-01 (includes COLUMN-SCAN SURFACE (C-47) annotation on Verb field).

---

**STRUCTURAL AXIS DECLARATION**

Twenty rows. Axes 1-17 identical to V-01. Axis 18 = Column-scan verification (V-01 definition).
Axis 19 = Verb-source chain (V-03 definition). Axis 20 = Declaration-completeness-proof.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| [Axes 1-17 identical to V-01] | | | |
| Column-scan verification axis | C-47 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist enumerates all (F-ID, Verb) pairs from FT and RQG without reading any narrative field; scan declared sufficient | (1) schema note present: "COLUMN-SCAN SURFACE (C-47)"; names included columns (FT Verb, RQG Verb) and excluded fields (Summary, Impact, Remediation, BR rationale, Conf rationale); (2) compliance checklist sub-claim 2: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced; (3) compliance checklist sub-claim 3: "C-47 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" |
| Verb-source chain axis | C-49 | RQG Verb Source carries F-ID back-cite: "DETECTION: FT[F-NN].Verb=[Verb]" or "CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared"; three-point bidirectional chain; chain break detectable from either endpoint | (1) every Verb Source cell uses F-ID back-cite format; F-NN in cell matches row F-ID; cell without back-cite = C-49 fail; (2) three-point chain traced in compliance checklist sub-claim 2: FT[F-NN].Verb --> RQG[F-NN].Verb --> VerbSource.FT[F-NN] back-cite -- cite all three points; (3) chain break audit: for every CORRECTED entry, F-NN in cell matches row F-ID and [old] matches FT Verb; declare any break |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 20th and final targeted axis | This Row Count Assertion, itself the 20th and final of the 20 targeted axes declared below, is C-37's completeness proof: (1) opening sentence declares self-reference and count invariant (20th and final of 20); (2) enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), Verb-source chain(19), Declaration-completeness-proof(20); (3) row count in SAD == 20 |

---

**TOPIC ENTITY MANIFEST**, **EXECUTION ORDER GATE**, **OBSERVATIONAL DISCIPLINE**,
**EXECUTION SEQUENCE**, **CROSS-SKILL DEPENDENCY MAP**, **CANDIDATE OBSERVATIONS AND FILTER
LOG**, **FILTER LOG RESOLUTION + T-1 ANNEX**, **FINDINGS TABLE**, **EXECUTION LOG**,
**ENTITY COVERAGE MATRIX**, **INITIAL RANKED FINDINGS**, **CROSS-SKILL COMPARISON PROTOCOL**,
**BLAST RADIUS RE-ASSESSMENT GATE**, **UPDATED RANKED FINDINGS**, **COVERAGE GATE**,
**CONFIDENCE-STRATIFIED ACTION LIST**

Same as V-01.

---

**REMEDIATION QUALITY GATE**

Six columns. Verb Source column uses F-ID back-cite format (from V-03).

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary**, **Conformance rule**, **Blast Status rule**: same as V-01.

**Verb Source column rule** (V-03 format with F-ID back-cite):
- DETECTION: FT[F-NN].Verb=[Verb] -- F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's
  F-ID; chain break between FT Verb and RQG Verb is the declared bind failure

**REASSESSED and Verb independence**: A finding whose Blast Status is REASSESSED retains its
original Type-verb binding; the Blast Status column and the Verb Source column are
independently falsifiable in the same row. A REASSESSED Blast Status does not alter Verb.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Twenty rows. Rows 1-17 same as V-01. Row 18 = Column-scan verification. Row 19 = Verb-source
chain. Row 20 = Declaration-completeness-proof.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| [Rows 1-17 same as V-01 compliance checklist] | | | |
| Column-scan verification axis (C-47) | Findings Table + Remediation Quality Gate | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present; cite verbatim; names included and excluded fields; Sub-claim 2: column-scan enumeration: list all FT (F-ID, Verb) pairs; list all RQG (F-ID, Verb) pairs; declare set equality; no narrative field referenced; Sub-claim 3: "C-47 verified without reading Summary, Impact, Remediation, or any other narrative field; column-scan declared sufficient" | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49) | Remediation Quality Gate | Sub-claim 1: every Verb Source cell uses F-ID back-cite format; cite one cell verbatim; confirm F-NN in cell matches row F-ID; Sub-claim 2: three-point chain traced: cite FT[F-NN].Verb, RQG[F-NN].Verb, and VerbSource.FT[F-NN] back-cite; all three points cited by section and value; declare chain intact; Sub-claim 3: CORRECTED entries audited: for each CORRECTED cell, F-NN matches row F-ID and [old] matches FT Verb; cite count of CORRECTED or confirm zero; declare zero chain breaks or cite each break | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 20th and final of the 20 targeted axes declared below, is C-37's completeness proof: Sub-claim 1: opening sentence declares self-reference and count invariant (20th and final of 20); Sub-claim 2: enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), Verb-source chain(19), Declaration-completeness-proof(20); Sub-claim 3: row count in SAD == 20 | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Structural Axis Declaration (twenty rows)
> EXECUTION ORDER GATE > Observational Discipline > Execution Sequence (trace-first) >
Cross-Skill Dependency Map > Candidate Observations and Filter Log > Filter Log Resolution
(with T-1 ANNEX) > Findings Table (with Verb column, COLUMN-SCAN SURFACE note) > Execution
Log > Entity Coverage Matrix (with Commitment Honored? column) > Initial Ranked Findings
(pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment Gate >
Updated Ranked Findings (post-re-assessment, authoritative) > Coverage Gate >
Confidence-Stratified Action List > Remediation Quality Gate (six columns, Verb Source with
F-ID back-cite) > Structural Compliance Checklist (twenty rows).

---

## V-05 -- Full Integration: C-47 + C-48 + C-49 on 18-Axis Base (twenty-one axes)

**Variation axes:** Full integration -- V-01's column-scan verification note (C-47), V-02's
SKIPPED-T1/SKIPPED-T2 tier labels (C-48), and V-03's Verb Source F-ID back-cite (C-49)
applied simultaneously on the R14 V-05 eighteen-axis base. The SAD promotes to twenty-one
rows. The Row Count Assertion opening sentence reads: "This Row Count Assertion, itself the
21st and final of the 21 targeted axes declared below, is C-37's completeness proof." C-44
is preserved at twenty-one-axis scope. All R14 V-05 mechanisms remain intact and cross-verified.

**Hypothesis:** The three R15 mechanisms operate on disjoint structural surfaces: C-47 adds a
schema note to the FT Verb field; C-48 changes the ECM Status cell values for SKIPPED entries;
C-49 changes the Verb Source cell format in the RQG. No surface overlap exists: C-47 does not
affect the RQG; C-48 does not affect the FT Verb or RQG; C-49 does not affect the ECM.
Combining all three creates three new independently-falsifiable compliance sub-claims without
degrading any of the eighteen existing axis mechanisms. The compliance checklist at twenty-one
rows preserves all prior sub-claims with the count updated throughout.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty-one structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 21st and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all twenty-one axes fired using sub-claim decomposition. All three
sections are written by the model into the output artifact.

---

**EMPTY-STATE TEMPLATES**

All templates from V-04 plus V-02's tier templates:
- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No
  gaps detected because [reason]."
- **Filter gate Template B**: "Filter gate applied. [N] evaluated. Zero rejected. RECALIBRATION
  REQUIRED."
- **Per-scope Disposition zero withheld-T1**: "Disposition log for [sub-skill]: [N]
  observations. Zero withheld-T1. T-1 SCOPE RECALIBRATION."
- **T-1 ANNEX RECALIBRATION**: "T-1 ANNEX: Zero withheld-T1. T-1 RECALIBRATION REQUIRED."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills."
- **Cross-skill patterns empty**: "No compounding patterns detected. Step 2 pairs: [list]. Each
  describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates. Reason: [explanation]."
- **Execution Log DR-NN zero-contribution (Platform)**: "DR-NN Contributed ([sub-skill]): Zero
  rules declared. DEPENDENCY SCOPE RECALIBRATION."
- **Propagation Coverage Gate no rules**: "Coverage Gate: zero rules. DEPENDENCY MAP
  RECALIBRATION REQUIRED."
- **Blast Re-Assessment Gate no patterns**: "BLAST RADIUS RE-ASSESSMENT GATE: Zero compounding
  patterns. Re-assessment cannot proceed. Ranked Findings unchanged."
- **Blast Re-Assessment Gate no elevation**: "BLAST RADIUS RE-ASSESSMENT GATE: [N] patterns
  declared. Zero findings elevated. Blast Status column: all rows ORIGINAL."
- **Remediation Quality Gate empty**: "REMEDIATION QUALITY GATE: No findings. Gate schema:
  F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source. Verb Source
  format: DETECTION: FT[F-NN].Verb=[Verb]. Executed with empty finding set."
- **Manifest no examining commitment**: "TOPIC ENTITY MANIFEST: Entity [name] (E-[NN]) has no
  Examining Sub-Skill committed."
- **Commitment-outcome mismatch**: "COMMITMENT OUTCOME MISMATCH: Entity [name] (E-[NN])
  committed to [sub-skill]; status = SKIPPED. Compliance gap declared."
- **Finding-verb mismatch**: "FINDING-VERB MISMATCH: F-[NN] FT Verb = [value]; RQG Verb =
  [value]. Cross-artifact bind failure declared."
- **Confidence-stratification action tracks empty**: "CONFIDENCE-STRATIFIED ACTION LIST: No
  HIGH-blast findings to stratify."
- **Column-scan surface note (empty findings)**: "COLUMN-SCAN SURFACE VERIFICATION: No
  findings. FT Verb column: empty. RQG Verb column: empty. Column scan complete: zero pairs.
  C-47 verified; no narrative field read."
- **SKIPPED-T1 entity**: "ENTITY COVERAGE: Entity [name] (E-[NN]) status = SKIPPED-T1
  (commitment-present). Examining Sub-Skill [sub-skill] was committed but did not execute.
  Promise-breach gap declared."
- **SKIPPED-T2 entity**: "ENTITY COVERAGE: Entity [name] (E-[NN]) status = SKIPPED-T2
  (none-declared). No pre-execution commitment. Planning gap declared."

---

**FINDING SCHEMA**

All fields required. Verb field declared at detection time and labeled as column-scan surface.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract /
                 trace-permissions]
Type:           [GAP / CONTRADICTION / ASSUMPTION]
Verb:           [add / remove / resolve / confirm -- constrained by Type]
                 COLUMN-SCAN SURFACE (C-47): scan FT Verb column vs RQG Verb column for C-47.
                 Excluded from scan: Summary, Impact, Remediation, BR rationale, Conf rationale.
Spec location:  [REQUIRED]
Summary:        [one sentence -- EXCLUDED from C-47 scan]
Impact:         [STANDALONE FIELD -- EXCLUDED from C-47 scan]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide -- EXCLUDED from C-47 scan]
Confidence:     [HIGH / LOW -- required for cross-skill or system-wide]
Conf rationale: [REQUIRED when Confidence present -- EXCLUDED from C-47 scan]
Dep rule cite:  [DR-NN or "none"]
Remediation:    [narrative -- EXCLUDED from C-47 scan]
```

---

**TOPIC ENTITY MANIFEST**

Write as the absolute first section, before the Structural Axis Declaration.

| Entity ID | Entity Name | Category | Source | Examining Sub-Skill |
|-----------|-------------|----------|--------|---------------------|

Examining Sub-Skill: one of the five sub-skill names, or "none-declared". ADDED entities:
append with "ADDED -- post-execution".

---

**STRUCTURAL AXIS DECLARATION**

Write immediately after the Topic Entity Manifest. Twenty-one rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero, Execution Log zero-contribution, RQG empty, manifest commitment, mismatch templates, column-scan empty, SKIPPED-T1/T2 templates |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs | (1) Step 1: pairs; (2) Step 2: verdicts; (3) Step 3: P-IDs or empty-state |
| Declaration-compliance axis | C-17, C-18 | SAD (twenty-one rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claims; binary verdict = structural violation; (3) evidence cites actual section names |
| Observational discipline axis | C-19, C-20, C-21 | Genre + T-1 if-and-only-if + five per-scope tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if before any sub-skill; (2) five per-scope tables; (3) T-1 ANNEX as summary aggregator |
| DR-NN citation chain axis | C-32 | Three-point chain: map, Coverage Gate, Dep rule cite | (1) DR-NN IDs in map; (2) Coverage Gate cites; {map} == {gate union gap log}; (3) findings backlink |
| Confidence-stratification axis | C-30, C-35 | Two named action tracks; Conf rationale required | (1) two tracks; (2) every listed finding has Confidence + falsifiable Conf rationale; (3) non-HIGH-blast excluded with count |
| Type-verb binding axis | C-31 | Verb field in FT at detection; Verb column in RQG; Verb Source documents DETECTION/CORRECTED | (1) Verb in every FT row; vocabulary enforced at detection; out-of-vocabulary = bind failure in per-scope Disposition; (2) Verb Source: CORRECTED = declared bind failure; (3) count of CORRECTED == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate: all declared DR-NNs honored or OPEN PROPAGATION GAP | (1) one row per DR-NN; (2) {declared DR-NNs} == {gate rows union gap log}; (3) OPEN entries carry rule ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate; Execution Log Layer column | (1) Platform 1-3 before Domain; (2) P1/P2 with per-sub-skill DR-NN and Execution Log cross-cites; N1+N2+N3 confirmed; (3) Execution Log Layer column; Platform match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column; union equality | (1) DR-NN Contributed column; each trace step lists DR-NNs or zero-template; (2) union rows 1-3 equals full map; (3) verifiable from SAD row alone |
| Remediation-quality axis | C-26 | RQG: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; six columns; blank = fail; (2) Verb matches Type; Verb Source documents DETECTION or CORRECTED; (3) Conformance is falsifiable |
| Entity-coverage axis | C-27 | TEM + ECM; COVERED / CLEAN / SKIPPED-T1 / SKIPPED-T2 per entity | (1) ECM: one row per manifest entity; COVERED cites evidence; CLEAN names sub-skill; SKIPPED-T1/T2 logged as execution gap; (2) SKIPPED declared in checklist with entity name, ID, reason, tier; (3) ADDED entities appended with annotation before matrix |
| Blast-reassessment axis | C-28 | Re-Assessment Gate + ELEVATED inline + Blast Status column | (1) Re-Assessment Gate table; one row per P-ID; (2) ELEVATED inline on Updated Ranked Findings; (3) Updated Ranked Findings re-sorted; labeled authoritative |
| Blast-status axis | C-28 extension | Blast Status column in RQG: third independent C-28 path | (1) Blast Status: ORIGINAL or REASSESSED:[old]->[new](P-ID) for every row; (2) REASSESSED direction matches Gate table and Updated Ranked Findings annotation -- three-path consistent; discrepancy = declared failure; (3) checklist confirms three-path from Blast Status column alone |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in TEM; Commitment Honored? in ECM; two-tier SKIPPED in checklist | (1) Examining Sub-Skill present; every entity has a value; cite count; (2) every committed entity: Commitment Honored? = YES, MISMATCH, or N/A; no blank; (3) two-tier SKIPPED in checklist: T1 stronger, T2 weaker |
| Finding-verb axis | C-31 extension | Verb field in FT at detection; Verb Source in RQG; cross-artifact consistency from either artifact | (1) Verb in every FT row; (2) Verb Source: count DETECTION vs CORRECTED; CORRECTED = declared bind failure; (3) count CORRECTED == count F-IDs where FT Verb != RQG Verb |
| Column-scan verification axis | C-47 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist enumerates (F-ID, Verb) pairs from FT and RQG without narrative reading; scan declared sufficient | (1) schema note present: names included columns (FT Verb, RQG Verb) and excluded fields (Summary, Impact, Remediation, BR rationale, Conf rationale); (2) checklist sub-claim 2: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced; (3) checklist sub-claim 3: "C-47 verified without reading Summary, Impact, Remediation, or any other narrative field; column-scan declared sufficient" |
| SKIPPED-tier axis | C-48 | ECM Status cell carries SKIPPED-T1 (commitment-present) or SKIPPED-T2 (none-declared) for every SKIPPED entity; tier derivation rule explicit; tier distinction scannable from Status column | (1) every SKIPPED Status cell: "SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)"; bare "SKIPPED" = C-48 fail; tier derivation rule above ECM: T1 if Examining Sub-Skill != "none-declared"; T2 if == "none-declared"; (2) tier distinction column-local: reviewerscanning Status column can identify T1 vs T2 without reading Examining Sub-Skill column -- declare count of T1 and T2 from Status column scan; (3) gap severity declared: T1 (promise-breach gap) > T2 (planning gap) |
| Verb-source chain axis | C-49 | RQG Verb Source carries F-ID back-cite: "DETECTION: FT[F-NN].Verb=[Verb]" or "CORRECTED: FT[F-NN].Verb=[old]->[new]"; three-point bidirectional chain; break detectable from either endpoint | (1) every Verb Source cell uses F-ID back-cite format; F-NN must match row F-ID; cell without back-cite = C-49 fail; (2) three-point chain traceable both directions: forward FT[F-NN].Verb --> RQG[F-NN].Verb --> VerbSource.FT[F-NN]; backward VerbSource.F-NN --> FT row Verb; compliance checklist traces one chain citing all three points; (3) chain break audit: every CORRECTED entry's F-NN matches row F-ID and [old] matches FT Verb |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 21st and final targeted axis | This Row Count Assertion, itself the 21st and final of the 21 targeted axes declared below, is C-37's completeness proof: (1) opening sentence declares self-reference (C-42) and count invariant (C-44: 21st and final of 21) -- zero-scan verifiable; (2) enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Declaration-completeness-proof(21); item 21 is this block; (3) row count in SAD == 21 |

---

**EXECUTION ORDER GATE**

Same as V-01.

---

**OBSERVATIONAL DISCIPLINE**

Same as V-01.

---

**EXECUTION SEQUENCE**

Trace-first order. During each sub-skill: update Cross-Skill Dependency Map, populate
Execution Log DR-NN Contributed, note which manifest entities are examined, and declare Verb
for any elevated finding at detection time (labeled as COLUMN-SCAN SURFACE contribution).

1. trace-state
2. trace-contract
3. trace-permissions
   [Write EXECUTION ORDER GATE signal (P1 + P2 with per-sub-skill cross-cites) here]
4. flow-lifecycle
5. flow-conversation

**Per-scope gate table** (one per sub-skill):

| Obs # | What was noticed | Disposition | T-1 reason (if withheld-T1) | Filter rule (if withheld-rule) |
|-------|-----------------|------------|-----------------------------|---------------------------------|

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

**FILTER LOG RESOLUTION + T-1 ANNEX**

Same as V-01.

---

**FINDINGS TABLE**

Verb column present. COLUMN-SCAN SURFACE (C-47) note written above table.

Column note: "Verb column -- COLUMN-SCAN SURFACE (C-47): scan this column against RQG Verb
column to verify C-47; no narrative field read required."

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

**Tier derivation rule** (write above table):
> T1 if Examining Sub-Skill column != "none-declared" and entity is SKIPPED.
> T2 if Examining Sub-Skill column == "none-declared" and entity is SKIPPED.
> Tier derivable from Status column alone.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence | Commitment Honored? |
|-----------|-------------|--------|--------------|----------|---------------------|

**Status values**:
- COVERED -- cite F-ID or Obs #
- CLEAN -- name examining sub-skill and reason
- SKIPPED-T1 (commitment-present) -- apply SKIPPED-T1 template; declare in compliance checklist
- SKIPPED-T2 (none-declared) -- apply SKIPPED-T2 template; declare in compliance checklist

**Commitment Honored?**: YES / MISMATCH (with mismatch template inline) / N/A

---

**INITIAL RANKED FINDINGS** (pre-re-assessment)

Label: "RANKED FINDINGS (pre-re-assessment)"

Tiers 1-4. Apply ranked-tier empty-state template for any empty tier.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Step 1 / Step 2 / Step 3 (same as V-01).

---

**BLAST RADIUS RE-ASSESSMENT GATE**

Same as V-01.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

ELEVATED findings carry: `[ELEVATED: [old] -> [new] (P-ID: [P-ID])]` inline on Summary.

---

**COVERAGE GATE**

| DR-ID | Status | Finding ID(s) | Gap Reason (if OPEN) |
|-------|--------|---------------|----------------------|

---

**CONFIDENCE-STRATIFIED ACTION LIST**

Same as V-01.

---

**REMEDIATION QUALITY GATE**

Six columns. Verb Source uses F-ID back-cite format.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary** (GAP->add/remove; CONTRADICTION->resolve; ASSUMPTION->confirm).

**Conformance**: "Confirm that [named behavior] at [named location] under [named condition]."

**Blast Status**: ORIGINAL or REASSESSED:[old]->[new](P-ID). REASSESSED does not alter Verb.

**Verb Source** (C-49 format):
- DETECTION: FT[F-NN].Verb=[Verb] -- F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's F-ID

**Three-path C-28 consistency**: For every REASSESSED finding, [old]->[new] direction identical
in (1) Re-Assessment Gate table Direction column, (2) Updated Ranked Findings ELEVATED
annotation, and (3) Blast Status cell. Discrepancy = three-path integrity failure declared.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Twenty-one rows. `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + count; Sub-claim 2: T-1 ANNEX total + example + source; Sub-claim 3: ANNEX is summary aggregator | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1; Sub-claim 2: Step 2; Sub-claim 3: Step 3 P-IDs or empty-state | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | SAD | Sub-claim 1: twenty-one rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before execution | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if; Sub-claim 3: Disposition all five | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings | Sub-claim 1: DR-NN IDs in map; Sub-claim 2: Coverage Gate; {map} == {gate union gap log}; Sub-claim 3: findings cite Dep rule | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks; Sub-claim 2: Confidence + Conf rationale per finding; cite one verbatim; Sub-claim 3: non-HIGH-blast excluded with count | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb in every FT row; vocabulary enforced at detection; Sub-claim 2: Verb Source DETECTION vs CORRECTED count; CORRECTED = declared bind failure; Sub-claim 3: count CORRECTED == count F-IDs where FT Verb != RQG Verb | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: Gate present; one row per DR-NN; Sub-claim 2: {declared DR-NNs} == {gate union gap log}; Sub-claim 3: OPEN entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Platform 1-3 before Domain; Sub-claim 2: P1/P2 with DR-NN and Execution Log cross-cites; N1+N2+N3 confirmed; Sub-claim 3: Execution Log Layer column | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; each trace step lists DR-NNs; Sub-claim 2: union rows 1-3 equals full map -- cite counts; Sub-claim 3: verifiable from SAD row alone -- cite three sub-observables by name | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; six columns; blank = fail; cite count; Sub-claim 2: Verb matches Type; Verb Source documents mismatches; Sub-claim 3: Conformance falsifiable -- cite one cell verbatim | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | TEM + ECM | Sub-claim 1: ECM has one row per manifest entity -- cite counts; Sub-claim 2: COVERED cites evidence; CLEAN names sub-skill; SKIPPED-T1/T2 declared as execution gap with entity name, ID, reason, tier; Sub-claim 3: ADDED entities appear with annotation | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Gate table; one row per P-ID; Sub-claim 2: ELEVATED annotations; cite one F-ID verbatim; Sub-claim 3: Updated Ranked Findings labeled authoritative | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status populated every row: ORIGINAL or REASSESSED; cite counts; Sub-claim 2: REASSESSED direction matches Gate table + Updated Ranked Findings -- cite one F-ID and all three values; Sub-claim 3: if no elevation, all ORIGINAL; cite no-elevation template | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | TEM + ECM | Sub-claim 1: Examining Sub-Skill column present; every entity has a value; cite counts; Sub-claim 2: committed entities: Commitment Honored? = YES/MISMATCH/N/A; no blanks; Sub-claim 3: two-tier SKIPPED in checklist -- T1 stronger, T2 weaker; cite one of each or confirm only one tier; zero SKIPPED: "two-tier did not fire" | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb in every FT row -- cite count; Sub-claim 2: Verb Source DETECTION vs CORRECTED; CORRECTED = bind failure declared; Sub-claim 3: count CORRECTED == count F-IDs where FT Verb != RQG Verb | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47) | Findings Table + Remediation Quality Gate | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present -- cite verbatim; names included columns and excluded fields; Sub-claim 2: column-scan enumeration: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced -- if any narrative field was required, cite F-ID and declare scan insufficient; Sub-claim 3: "C-47 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" | fired / partial [sub-claim] / not fired |
| SKIPPED-tier axis (C-48) | Entity Coverage Matrix | Sub-claim 1: all SKIPPED Status cells carry tier labels -- every SKIPPED entry is "SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)"; bare "SKIPPED" = C-48 fail; cite count T1 vs T2; Sub-claim 2: tier derivation rule stated above ECM; tier derivable from Status column without reading Examining Sub-Skill column -- declare count of T1 and T2 from Status column scan only; Sub-claim 3: gap severity: T1 (promise-breach gap) > T2 (planning gap); cite one T1 entity and one T2 entity if both exist; if only one tier: name it and cite entity; if zero SKIPPED: "SKIPPED-tier labels did not fire" | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49) | Remediation Quality Gate | Sub-claim 1: every Verb Source cell uses F-ID back-cite format -- cite one verbatim; F-NN in cell matches row F-ID; cell without back-cite = C-49 fail; Sub-claim 2: three-point chain traced: FT[F-NN].Verb --> RQG[F-NN].Verb --> VerbSource.FT[F-NN]; cite all three points by section and value; declare chain intact; Sub-claim 3: chain break audit: every CORRECTED entry's F-NN matches row F-ID and [old] matches FT Verb; cite count of CORRECTED or confirm zero; declare zero chain breaks or cite each break with F-ID, expected, actual | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 21st and final of the 21 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference and count invariant (21st and final of 21) -- zero-scan verifiable; Sub-claim 2 (C-40): enumerated list: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Declaration-completeness-proof(21); item 21 is this block; Sub-claim 3 (C-37): row count in SAD == 21 == count of targeted quality criteria; count mismatch in either direction = C-37 fail | fired / partial [sub-claim] / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest (with Examining Sub-Skill column) >
Structural Axis Declaration (twenty-one rows) > EXECUTION ORDER GATE > Observational
Discipline > Execution Sequence (trace-first) > Cross-Skill Dependency Map > Candidate
Observations and Filter Log > Filter Log Resolution (with T-1 ANNEX) > Findings Table (with
Verb column, COLUMN-SCAN SURFACE note) > Execution Log > Entity Coverage Matrix (with
SKIPPED-T1/SKIPPED-T2 tier labels and Commitment Honored? column) > Initial Ranked Findings
(pre-re-assessment) > Cross-Skill Comparison Protocol > Blast Radius Re-Assessment Gate >
Updated Ranked Findings (post-re-assessment, authoritative) > Coverage Gate >
Confidence-Stratified Action List > Remediation Quality Gate (six columns, Verb Source with
F-ID back-cite) > Structural Compliance Checklist (twenty-one rows).
