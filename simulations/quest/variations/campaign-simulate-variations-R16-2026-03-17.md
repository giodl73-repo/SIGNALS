All 5 variations present. File written to `simulations/quest/variations/campaign-simulate-variations-R16-2026-03-17.md` (2272 lines, 199KB).

---

**Summary of R16 variations:**

| Var | Axis | New mechanism | Axes | New towers |
|-----|------|---------------|------|------------|
| V-01 | Output format | Column-scan enumeration table: checklist sub-claim 2 of column-scan verification IS a 3-column scan table (F-ID \| FT Verb \| RQG Verb); verbatim sufficiency declaration references table by name | 22 | C-50 ceiling |
| V-02 | Phrasing register | Tier severity axiom: formal SEVERITY AXIOM block before ECM; T1>T2 derivable from axiom + Status cell tier label alone | 22 | C-51 ceiling |
| V-03 | Output format | Self-match audit table: checklist sub-claim 2 of Verb-source chain IS a 3-column audit table (RQG Row F-ID \| Verb Source F-NN \| Match?); column-equality scan exhausts verification | 22 | C-52 ceiling |
| V-04 | Output format + format | V-01 + V-03 combined; two disjoint table surfaces | 23 | C-50 + C-52 ceilings |
| V-05 | Full integration | V-01 + V-02 + V-03; three disjoint surfaces; surface independence declaration in RQG | 24 | C-50 + C-51 + C-52 ceilings |

**Key ceiling mechanisms:** The three new towers turn C-50/C-51/C-52's existing mechanism proofs into structural artifacts — a scan table's column schema IS the no-narrative-read proof; a formal axiom block IS the severity derivation source; a column-equality table IS the self-match audit. Each ceiling converts an assertion into a falsifiable structural form.
ing) combined (23 axes) | Both mechanisms operate on different checklist sub-claims of different axes; independently additive with no surface overlap |
| V-05 | Full integration | V-01 + V-02 + V-03: all three ceiling mechanisms on R15 V-05 21-axis base → 24 axes | Three mechanisms on disjoint surfaces; Row Count Assertion at 24; all R15 V-05 mechanisms intact |

**New tower openings:**
- C-50 → **column-scan enumeration table ceiling**: the enumeration IS a 3-column scan table with no narrative columns; sufficiency declaration references the table by name; absence of table reference = ceiling fail
- C-51 → **severity-axiom-first ceiling**: SEVERITY AXIOM block precedes ECM; gap ordering derivable from axiom + Status cell tier label alone; no Examining Sub-Skill or finding content consulted
- C-52 → **self-match audit table ceiling**: 3-column audit table makes F-ID equality verifiable by column scan; mismatch detectable without reading Verb Source cell content

---

## V-01 -- Column-Scan Enumeration Table: C-50 Ceiling (output format)

**Variation axis:** Output format -- the compliance checklist sub-claim 2 of the column-scan
verification axis is written as an explicit 3-column scan table rather than prose enumeration.
The table schema is `| F-ID | FT Verb | RQG Verb |`. The table has no narrative columns; this
structural property is itself the proof that no narrative field was read. The verbatim sufficiency
declaration (sub-claim 3 of column-scan verification axis) references the enumeration table by
name: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared
sufficient." A new dedicated SAD axis (axis 21: Column-scan enumeration table axis) carries three
sub-observables for this mechanism. The Row Count Assertion promotes from 21 to 22.

**Hypothesis:** The R15 V-05 column-scan sufficiency declaration works as a proof because it is
self-defeating if false. The C-50 ceiling adds a structural layer: the enumeration format itself
— a 3-column table with no narrative column — is the falsifiable artifact. A prose list could
silently include narrative context; the 3-column table cannot. The ceiling is: the verbatim
declaration references the named table as the proof handle, converting the assertion into a
structural citation. C-51 and C-52 mechanisms are not extended; R15 V-05 SKIPPED-tier (axis 19)
and Verb-source chain (axis 20) remain exactly as specified.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty-two structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 22nd and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all twenty-two axes fired using sub-claim decomposition. All three
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
- **SKIPPED-T1 entity**: "SKIPPED-T1 (commitment-present): Entity [name] (E-[NN]) committed to
  [sub-skill]; execution gap. Stronger gap: promise-breach."
- **SKIPPED-T2 entity**: "SKIPPED-T2 (none-declared): Entity [name] (E-[NN]); no sub-skill
  committed. Weaker gap: planning gap."
- **Column-scan enumeration table (zero findings)**: "COLUMN-SCAN ENUMERATION TABLE: zero
  findings. Table schema: F-ID | FT Verb | RQG Verb. Zero rows. Column-scan declared sufficient
  by empty set: no narrative field read for any F-ID because no F-IDs exist."

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

Write immediately after the Topic Entity Manifest. Twenty-two rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty, manifest commitment, mismatch templates, column-scan empty findings, SKIPPED-T1/T2 templates, column-scan enumeration table empty |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (twenty-two rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
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
| Column-scan verification axis | C-47, C-50 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist sub-claim 2 writes enumeration as structured 3-column scan table (F-ID \| FT Verb \| RQG Verb); verbatim sufficiency declaration references table by name | (1) schema note "COLUMN-SCAN SURFACE (C-47)" present in Verb field definition before any finding is recorded; note names included columns (FT Verb, RQG Verb) and excluded fields (Summary, Impact, Remediation, BR rationale, Conf rationale); (2) checklist sub-claim 2: 3-column scan table (F-ID \| FT Verb \| RQG Verb) with no narrative column; table row count == finding count; any Verb requiring narrative reading flagged inline as scan-insufficient; (3) compliance checklist sub-claim 3 declares verbatim: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient; C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" |
| SKIPPED-tier axis | C-48, C-51 | SKIPPED-T1 (commitment-present) / SKIPPED-T2 (none-declared) labels directly in ECM Status cell; tier derivation rule stated above ECM table | (1) ECM Status cells use SKIPPED-T1 or SKIPPED-T2 labels (not bare "SKIPPED"); tier derivation rule present above ECM table: "T1 if Examining Sub-Skill != none-declared; T2 if == none-declared"; (2) compliance checklist sub-claim 2: every committed entity has Commitment Honored? present; SKIPPED-T1 entities cited with entity ID; (3) compliance checklist sub-claim 3: gap severity order declared -- SKIPPED-T1 (promise-breach, stronger gap) > SKIPPED-T2 (planning gap, weaker gap); cite one T1 and one T2 or confirm only one tier fired |
| Verb-source chain axis | C-49, C-52 | RQG Verb Source format: DETECTION: FT[F-NN].Verb=[Verb] (clean) or CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared (corrected); F-NN in Verb Source must match RQG row's own F-ID | (1) every Verb Source cell uses F-ID back-cite format with F-NN matching row F-ID; (2) compliance checklist sub-claim 2 traces one complete three-point chain (FT[F-NN].Verb -> RQG[F-NN].Verb Source -> Verb Source.FT[F-NN]) -- chain traversable forward and backward; (3) chain break audit: for every CORRECTED entry, F-NN matches row F-ID and [old] matches FT Verb; discrepancy detectable from either endpoint |
| Column-scan enumeration table axis | C-50 ceiling | Compliance checklist sub-claim 2 of column-scan verification axis IS the 3-column scan table (F-ID \| FT Verb \| RQG Verb); table structure is the proof; verbatim sufficiency declaration references table by name | (1) 3-column scan table present in checklist sub-claim 2: schema is F-ID \| FT Verb \| RQG Verb and no other column; table has no narrative column -- structural absence of narrative column is the scan-sufficiency proof; (2) table row count equals finding count -- cite both; any finding where Verb required narrative reading to resolve is flagged inline with F-ID and "scan declared insufficient for this row"; (3) verbatim declaration in sub-claim 3 of column-scan verification axis references this enumeration table by name: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient" -- presence of named table reference is the proof handle; absence of table reference = C-50 ceiling fail |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 22nd and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 22nd and final of the 22 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42: this assertion is C-37's completeness proof) and count invariant (C-44: 22nd and final of 22) -- both verifiable at zero-scan scope from one sentence; (2) enumerated list of all 22 targeted axes by name follows; "Declaration-completeness-proof axis (this Row Count Assertion block)" appears as item 22; (3) row count in SAD == 22 == count of targeted quality criteria; 22 targeted axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Column-scan enumeration table(21), Declaration-completeness-proof(22) |

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

Tier derivation rule (write above table): T1 if Examining Sub-Skill != none-declared;
T2 if Examining Sub-Skill == none-declared.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

Status values: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED-T1 (commitment-present) / SKIPPED-T2 (none-declared)

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
- DETECTION: FT[F-NN].Verb=[Verb] -- Verb unchanged from FT Verb field; F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's F-ID

**Three-path C-28 consistency**: For every REASSESSED finding, the [old]->[new] direction must
be identical in (1) Re-Assessment Gate table Direction column, (2) inline ELEVATED annotation
on Updated Ranked Findings, and (3) Blast Status cell in this table. Discrepancy between any
two paths = declared three-path integrity failure in compliance checklist with F-ID.

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Twenty-two rows. Multi-part: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + rejection count; Sub-claim 2: T-1 ANNEX total + example + source scope; Sub-claim 3: ANNEX declared as summary aggregator only | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs named or empty-state template applied | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twenty-two rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary -- cite two labels; Sub-claim 2: T-1 if-and-only-if stated before any sub-skill; Sub-claim 3: Disposition columns present in all five per-scope tables | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; Sub-claim 3: findings cite Dep rule backlink | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks present; findings assigned by confidence x blast quadrant; Sub-claim 2: every finding in either track carries Confidence label and falsifiable Conf rationale -- cite one Conf rationale verbatim; Sub-claim 3: non-HIGH-blast findings excluded -- cite count excluded | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field in every FT row -- cite count; Type-verb vocabulary enforced at detection; Sub-claim 2: Verb Source column -- cite count of DETECTION vs CORRECTED; CORRECTED entries declared as bind failures; Sub-claim 3: count of CORRECTED == count of F-IDs where FT Verb != RQG Verb -- cite count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: Coverage Gate present; one row per declared DR-NN; Sub-claim 2: {declared DR-NNs} == {gate rows union gap log} -- cite both sets; Sub-claim 3: OPEN PROPAGATION GAP entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record -- Platform 1-3 complete before Domain; Sub-claim 2: P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; Sub-claim 3: Execution Log Layer column; Platform rows match P2; Domain "n/a" | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; Sub-claim 2: union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; Sub-claim 3: this axis verified from SAD row alone, independent of Execution Order Gate section -- cite the SAD row's three sub-observables by name | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns (Verb, Target, Location, Conformance, Blast Status, Verb Source) populated; blank = fail; cite count; Sub-claim 2: Verb matches Type vocabulary every row; Verb Source documents all mismatches; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim to confirm named-observable format | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: ECM has one row per manifest entity -- cite entity count from manifest; confirm matrix count matches; Sub-claim 2: COVERED cites evidence; CLEAN names sub-skill and reason; SKIPPED-T1/T2 declared as execution gap in this row with entity name, ID, and tier; Sub-claim 3: ADDED entities appear with annotation in ECM -- confirm manifest updated before matrix written | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: Re-Assessment Gate table; one row per P-ID; all columns populated; cite P-ID count; Sub-claim 2: every ELEVATED finding carries inline annotation on Updated Ranked Findings row -- cite F-ID and annotation verbatim; if no elevation: cite applied empty-state template; Sub-claim 3: Updated Ranked Findings labeled authoritative; cite one finding that moved tiers or confirm no-elevation template applied | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status populated for every row: ORIGINAL or REASSESSED with direction and P-ID; cite count of ORIGINAL vs REASSESSED; Sub-claim 2: for each REASSESSED finding, direction in Blast Status == direction in Gate table Direction column == direction in Updated Ranked Findings ELEVATED annotation -- cite one REASSESSED F-ID and all three values; any discrepancy = three-path integrity failure declared with F-ID; Sub-claim 3: if no findings elevated: confirm all ORIGINAL; cite no-elevation template as evidence column was populated | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column present; every entity has a value; cite count committed vs none-declared; Sub-claim 2: every committed entity has Commitment Honored? = YES, MISMATCH (with template), or N/A; no blank for committed entities; cite count of each; Sub-claim 3: two-tier SKIPPED: SKIPPED-T1 (promise-breach, stronger gap) vs SKIPPED-T2 (planning gap, weaker gap) -- cite one of each tier or confirm only one tier exists; if zero SKIPPED: cite "zero SKIPPED; two-tier distinction did not fire" | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field present in every FT row -- cite count; no F-ID without Verb; Sub-claim 2: Verb Source count of DETECTION vs CORRECTED; every CORRECTED entry declared as cross-artifact bind failure -- cite F-ID and both values or confirm zero corrections; Sub-claim 3: count of CORRECTED Verb Source entries == count of F-IDs where FT Verb != RQG Verb -- cite count and confirm equality; if zero: confirm all DETECTION | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47, C-50) | Findings Table + Remediation Quality Gate + Structural Compliance Checklist (sub-claim 2) | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present in FT Verb column definition -- cite verbatim; confirm note names included columns (FT Verb, RQG Verb) and excluded fields (Summary, Impact, Remediation, BR rationale, Conf rationale); Sub-claim 2: 3-column scan table (F-ID \| FT Verb \| RQG Verb) written here -- table has no narrative column; any Verb requiring narrative reading flagged inline; table row count == finding count (cite both); Sub-claim 3: column-scan sufficiency declaration verbatim: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient; C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" -- this declaration is the proof; if the declaration cannot be made without qualification, C-47 and C-50 fail | fired / partial [sub-claim] / not fired |
| SKIPPED-tier axis (C-48, C-51) | Entity Coverage Matrix + Structural Compliance Checklist | Sub-claim 1: ECM Status cells use SKIPPED-T1 or SKIPPED-T2 (not bare "SKIPPED"); tier derivation rule present above ECM table -- cite rule verbatim; Sub-claim 2: every committed entity has Commitment Honored? value; SKIPPED-T1 entities cited with entity ID and committed sub-skill; Sub-claim 3: gap severity order declared -- SKIPPED-T1 (promise-breach) > SKIPPED-T2 (planning gap); cite one T1 and one T2 entity label from ECM Status column alone (no Examining Sub-Skill column consulted); if zero SKIPPED: confirm two-tier distinction did not fire | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49, C-52) | Remediation Quality Gate (Verb Source column) + Findings Table | Sub-claim 1: every Verb Source cell uses F-ID back-cite format: DETECTION: FT[F-NN].Verb=[Verb] or CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared; cite count of DETECTION vs CORRECTED; Sub-claim 2: chain trace: cite one complete three-point chain (FT[F-NN].Verb -> RQG[F-NN].Verb -> Verb Source F-NN back-cite) -- chain traversable in both directions; if zero findings: cite empty-state template; Sub-claim 3: self-match audit -- for every CORRECTED entry, confirm F-NN in Verb Source matches RQG row F-ID and [old] matches FT Verb; cite one CORRECTED entry with all three values, or confirm zero CORRECTED entries | fired / partial [sub-claim] / not fired |
| Column-scan enumeration table axis (C-50 ceiling) | Structural Compliance Checklist (sub-claim 2 of column-scan verification axis) | Sub-claim 1: 3-column scan table (F-ID \| FT Verb \| RQG Verb) present in checklist sub-claim 2 of column-scan verification axis; confirm table schema has no narrative column -- structural absence of narrative column is the scan-sufficiency proof; Sub-claim 2: table row count equals finding count -- cite both counts; confirm every row has both Verb values populated without narrative field read; if any row is flagged as scan-insufficient, cite F-ID and declare C-50 ceiling fail for that row; Sub-claim 3: verbatim declaration in sub-claim 3 of column-scan verification axis references this enumeration table by name: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient" -- absence of named table reference in the declaration = C-50 ceiling fail; cite the declaration sentence and confirm table reference present | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 22nd and final of the 22 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference (this assertion is C-37's completeness proof) and count invariant (22nd and final of 22) -- both verifiable at zero-scan scope; Sub-claim 2 (C-40): enumerated list of 22 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Column-scan enumeration table(21), Declaration-completeness-proof(22); "Declaration-completeness-proof axis" appears as item 22; Sub-claim 3 (C-37): row count in SAD == 22 == count of targeted quality criteria; count mismatch in either direction = C-37 fail | fired / partial [sub-claim] / not fired |

---

## V-02 -- Tier Severity Axiom: C-51 Ceiling (phrasing register)

**Variation axis:** Phrasing register -- a formal SEVERITY AXIOM block is written immediately
before the Entity Coverage Matrix table. The axiom states: "SEVERITY AXIOM: T1 severity >
T2 severity. T1 = promise-breach (sub-skill committed in TEM, execution skipped). T2 = planning
gap (no sub-skill committed, no promise made)." The axiom is a named standalone block and is
falsifiable by its own terms. The compliance checklist sub-claim 3 of the SKIPPED-tier axis
derives the severity ordering from the axiom text and the ECM Status cell tier label alone,
without consulting the Examining Sub-Skill column, the SKIPPED reason field, or any finding
content. A new dedicated SAD axis (axis 21: Tier severity axiom axis) carries three
sub-observables. The Row Count Assertion promotes from 21 to 22.

**Hypothesis:** R15 V-05 embedded T1/T2 labels in Status cells and stated a tier derivation rule.
The C-51 ceiling adds a severity layer: the ordering T1 > T2 is formally derivable from an
axiom, not just a label convention. By pre-stating the axiom before the ECM, severity ordering
becomes derivable from axiom text + Status cell tier label alone. The checklist sub-claim closes
the proof by citing only axiom + Status cell. C-50 and C-52 mechanisms are not extended; R15
V-05 column-scan verification (axis 18) and Verb-source chain (axis 20) remain as specified.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty-two structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 22nd and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all twenty-two axes fired using sub-claim decomposition. All three
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
- **SKIPPED-T1 entity**: "SKIPPED-T1 (commitment-present): Entity [name] (E-[NN]) committed to
  [sub-skill]; execution gap. SEVERITY AXIOM: T1 = promise-breach -- stronger gap."
- **SKIPPED-T2 entity**: "SKIPPED-T2 (none-declared): Entity [name] (E-[NN]); no sub-skill
  committed. SEVERITY AXIOM: T2 = planning gap -- weaker gap."
- **Tier severity axiom (no SKIPPED entities)**: "SEVERITY AXIOM fired; zero SKIPPED entities.
  T1-T2 distinction did not activate. Axiom on record: T1 > T2 severity. Axiom application:
  none required this execution."

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

Write immediately after the Topic Entity Manifest. Twenty-two rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty, manifest commitment, mismatch templates, column-scan empty findings, SKIPPED-T1/T2 templates, tier severity axiom no-SKIPPED template |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (twenty-two rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope source records |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks to map |
| Confidence-stratification axis | C-30, C-35 | Confidence-Stratified Action List with two named tracks; Conf rationale required per finding | (1) two named action tracks present; findings assigned by confidence x blast-radius quadrant; (2) every finding in either track carries Confidence label and falsifiable Conf rationale; (3) findings below HIGH-blast threshold excluded -- cite count excluded |
| Type-verb binding axis | C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary declared; Verb field in FT at detection; Verb column in RQG; cross-artifact consistency enforced | (1) Verb field in every FT row; vocabulary enforced at detection; out-of-vocabulary declared as bind failure; (2) Verb Source in RQG: DETECTION or CORRECTED; CORRECTED = declared bind failure; (3) count of CORRECTED == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate accounts for all declared dependency rules: honored or OPEN PROPAGATION GAP | (1) Coverage Gate present; one row per declared DR-NN; (2) {declared DR-NNs} == {gate rows union gap log}; (3) OPEN PROPAGATION GAP entries carry rule ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate signal with per-sub-skill cross-cites; Execution Log Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5; (2) P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; (3) Execution Log Layer column; Platform rows match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; (2) union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; (3) checklist verifies from SAD row alone, independent of Execution Order Gate section |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; all six columns populated; blank = fail; cite count; (2) Verb matches Type vocabulary; Verb Source documents DETECTION or CORRECTED; (3) Conformance is falsifiable: named-observable format required |
| Entity-coverage axis | C-27 | Topic Entity Manifest + Entity Coverage Matrix; COVERED / CLEAN / SKIPPED-T1 / SKIPPED-T2 per entity | (1) ECM: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED-T1/T2 logged as execution gap; (2) SKIPPED declared in checklist with entity name, ID, tier; (3) ADDED entities appended with annotation before matrix written |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + Blast Status column in RQG | (1) Re-Assessment Gate table; one row per P-ID; all columns populated; (2) ELEVATED annotation inline on Updated Ranked Findings; (3) Updated Ranked Findings re-sorted; labeled authoritative |
| Blast-status axis | C-28 extension | Third independent C-28 verification path: Blast Status column in RQG | (1) Blast Status every row: ORIGINAL or REASSESSED with direction and P-ID; (2) REASSESSED direction matches Gate table AND ELEVATED annotation; discrepancy = three-path integrity failure; (3) checklist confirms three-path consistency from Blast Status column alone |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in TEM; Commitment Honored? column in ECM; two-tier SKIPPED distinction | (1) Examining Sub-Skill column present; every entity has a value; cite counts; (2) every committed entity has Commitment Honored? = YES, MISMATCH, or N/A; cite count of each; (3) SKIPPED-T1 (promise-breach) vs SKIPPED-T2 (planning gap) -- cite one of each or confirm only one tier exists |
| Finding-verb axis | C-31 extension | Verb field in FT declared at detection; Verb Source column in RQG | (1) Verb field in every FT row -- cite count; no F-ID without Verb; (2) Verb Source count DETECTION vs CORRECTED; every CORRECTED declared as bind failure; (3) CORRECTED count == FT/RQG mismatch count |
| Column-scan verification axis | C-47, C-50 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist sub-claim 2 enumerates (F-ID, Verb) pairs; verbatim sufficiency declaration | (1) schema note "COLUMN-SCAN SURFACE (C-47)" present in Verb field definition; note names included columns (FT Verb, RQG Verb) and excluded fields; (2) checklist sub-claim 2: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced; if any narrative required, F-ID cited and scan declared insufficient; (3) verbatim declaration: "C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" |
| SKIPPED-tier axis | C-48, C-51 | SKIPPED-T1 / SKIPPED-T2 labels in ECM Status cells; tier derivation rule above ECM; SEVERITY AXIOM block before ECM delivers the gap-ordering proof | (1) ECM Status cells use SKIPPED-T1 or SKIPPED-T2 (not bare "SKIPPED"); tier derivation rule present above ECM table; (2) SEVERITY AXIOM block present before ECM: "T1 > T2 severity: T1 = promise-breach; T2 = planning gap"; axiom is standalone named block; (3) checklist sub-claim 3 derives severity ordering from SEVERITY AXIOM text + Status cell tier label alone -- no Examining Sub-Skill column or finding content consulted; cite axiom clause and one Status cell tier label |
| Verb-source chain axis | C-49, C-52 | RQG Verb Source format: DETECTION: FT[F-NN].Verb=[Verb] or CORRECTED: FT[F-NN].Verb=[old]->[new]; F-NN must match row F-ID | (1) every Verb Source cell uses F-ID back-cite format; F-NN matches row F-ID; (2) checklist sub-claim 2 traces one complete three-point chain; chain traversable in both directions; (3) for every CORRECTED entry, F-NN matches row F-ID and [old] matches FT Verb; break detectable from either endpoint |
| Tier severity axiom axis | C-51 ceiling | SEVERITY AXIOM block written before ECM table; axiom falsifiable by its own terms; checklist sub-claim 3 of SKIPPED-tier axis derives severity ordering from axiom + Status cell tier label alone | (1) SEVERITY AXIOM block present before ECM table -- cite axiom location and first clause verbatim: "T1 severity > T2 severity. T1 = promise-breach (sub-skill committed, execution skipped). T2 = planning gap (no sub-skill committed, no promise made)"; confirm axiom is a standalone named block not embedded in prose; (2) checklist sub-claim 3 of SKIPPED-tier axis cites SEVERITY AXIOM text and at least one T1 entity label and one T2 entity label from ECM Status column (or confirms single tier fired with reason); axiom citation is the derivation proof; (3) severity ordering derivable from SEVERITY AXIOM text + ECM Status tier label alone -- no Examining Sub-Skill column consulted, no SKIPPED reason read, no finding content accessed; checklist declares: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted"; absence of this declaration = C-51 ceiling fail |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 22nd and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 22nd and final of the 22 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42) and count invariant (C-44: 22nd and final of 22) -- both verifiable at zero-scan scope; (2) enumerated list of 22 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Tier severity axiom(21), Declaration-completeness-proof(22); item 22 = "Declaration-completeness-proof axis"; (3) row count in SAD == 22 == count of targeted quality criteria |

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

**SEVERITY AXIOM**

Write immediately before the Entity Coverage Matrix.

> SEVERITY AXIOM: T1 severity > T2 severity.
> T1 = promise-breach (sub-skill committed in TEM, execution skipped).
> T2 = planning gap (no sub-skill committed, no promise made).
> Corollary: SKIPPED-T1 findings require stronger remediation priority than SKIPPED-T2.
> Falsification condition: any SKIPPED-T2 entity prioritized above a SKIPPED-T1 entity
> contradicts this axiom and must be declared in the compliance checklist.

Apply "Tier severity axiom (no SKIPPED entities)" template if zero SKIPPED entities exist.

---

**ENTITY COVERAGE MATRIX**

Write after Execution Log and SEVERITY AXIOM block, before Initial Ranked Findings.

Tier derivation rule (write above table): T1 if Examining Sub-Skill != none-declared;
T2 if Examining Sub-Skill == none-declared.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

Status values: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED-T1 (commitment-present) / SKIPPED-T2 (none-declared)

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

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

Apply Blast Re-Assessment Gate no-patterns template if Step 3 produced zero patterns.
Apply Blast Re-Assessment Gate no-elevation template if patterns exist but no blast increases.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label: "RANKED FINDINGS (post-re-assessment -- authoritative)"

ELEVATED findings carry inline annotation:
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

**Track 1 -- HIGH-confidence / HIGH-blast: Implement Fix Immediately**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

**Track 2 -- LOW-confidence / HIGH-blast: Confirm Spec Interpretation First**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

Apply confidence-stratification empty template if no HIGH-blast findings exist.

---

**REMEDIATION QUALITY GATE**

Every finding from the Findings Table must appear as exactly one row. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary**: GAP -> "add" or "remove"; CONTRADICTION -> "resolve"; ASSUMPTION -> "confirm"

**Conformance column rule**: "Confirm that [named behavior] is observable at [named location]
under [named condition]." Prose without named observable = fail.

**Blast Status column rule**: ORIGINAL / REASSESSED: [old] -> [new] (P-ID: [P-ID])

**Verb Source column rule**:
- DETECTION: FT[F-NN].Verb=[Verb] -- F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's F-ID

**Three-path C-28 consistency**: [old]->[new] direction must match Re-Assessment Gate,
ELEVATED annotation, and Blast Status cell. Discrepancy = declared three-path integrity failure.

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Twenty-two rows. Multi-part: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + rejection count; Sub-claim 2: T-1 ANNEX total + example + source scope; Sub-claim 3: ANNEX declared as summary aggregator only | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs named or empty-state template applied | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twenty-two rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if before any sub-skill; Sub-claim 3: Disposition columns in all five per-scope tables | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: set equality; Sub-claim 3: findings cite Dep rule backlink | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks; assignments correct; Sub-claim 2: Conf rationale per finding -- cite one verbatim; Sub-claim 3: non-HIGH-blast excluded -- cite count | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row; vocabulary enforced; Sub-claim 2: Verb Source DETECTION/CORRECTED count; CORRECTED declared; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: one row per DR-NN; Sub-claim 2: set equality; Sub-claim 3: OPEN PROPAGATION GAP entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Platform before Domain; Sub-claim 2: P1+P2 with DR-NN IDs and Execution Log cross-cites; N1+N2+N3 confirmed; Sub-claim 3: Layer column matches | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; each trace step lists; Sub-claim 2: union equals full map -- cite counts; Sub-claim 3: verified from SAD row alone | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns; cite count; Sub-claim 2: Verb matches vocabulary; Verb Source documents all; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: one row per manifest entity; counts match; Sub-claim 2: COVERED/CLEAN/SKIPPED-T1/T2 declared with tier; Sub-claim 3: ADDED entities annotated | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: one row per P-ID; all columns; Sub-claim 2: ELEVATED annotation -- cite F-ID verbatim or confirm template; Sub-claim 3: labeled authoritative | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status every row; ORIGINAL vs REASSESSED counts; Sub-claim 2: REASSESSED three-path consistency; Sub-claim 3: all ORIGINAL confirmed with template if no elevation | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column; every entity has value; cite counts; Sub-claim 2: Commitment Honored? for all committed; Sub-claim 3: SKIPPED-T1 vs SKIPPED-T2 -- cite one of each or confirm single tier | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row -- cite count; Sub-claim 2: DETECTION vs CORRECTED count; CORRECTED declared as bind failures; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47, C-50) | Findings Table + Remediation Quality Gate | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present -- cite verbatim; included/excluded fields named; Sub-claim 2: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced -- if any narrative required, F-ID cited and scan declared insufficient; Sub-claim 3: verbatim declaration: "C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" | fired / partial [sub-claim] / not fired |
| SKIPPED-tier axis (C-48, C-51) | Entity Coverage Matrix + SEVERITY AXIOM block | Sub-claim 1: ECM Status cells use SKIPPED-T1 or SKIPPED-T2; tier derivation rule present above ECM -- cite rule; Sub-claim 2: SEVERITY AXIOM block present before ECM -- cite axiom first clause verbatim; axiom is standalone named block; Sub-claim 3: gap severity derived from SEVERITY AXIOM + ECM Status tier label only: cite axiom clause and one T1 label and one T2 label from Status column (or confirm single tier); no Examining Sub-Skill column consulted; checklist declares: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted" | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49, C-52) | Remediation Quality Gate (Verb Source column) + Findings Table | Sub-claim 1: every Verb Source cell uses F-ID back-cite format; cite count DETECTION vs CORRECTED; Sub-claim 2: one complete three-point chain traced -- forward and backward; Sub-claim 3: self-match audit -- for every CORRECTED entry, F-NN matches row F-ID and [old] matches FT Verb; cite one or confirm zero | fired / partial [sub-claim] / not fired |
| Tier severity axiom axis (C-51 ceiling) | SEVERITY AXIOM block + Structural Compliance Checklist (sub-claim 3 of SKIPPED-tier axis) | Sub-claim 1: SEVERITY AXIOM block present before ECM table; cite axiom location and first clause verbatim: "T1 severity > T2 severity. T1 = promise-breach (sub-skill committed, execution skipped). T2 = planning gap (no sub-skill committed, no promise made)"; confirm axiom is a standalone named block not embedded in prose; Sub-claim 2: sub-claim 3 of SKIPPED-tier axis cites SEVERITY AXIOM text and at least one T1 entity label and one T2 entity label from ECM Status column -- or confirms single tier fired with reason; axiom citation is the derivation proof; Sub-claim 3: severity ordering derivable from SEVERITY AXIOM text + ECM Status tier label alone -- no Examining Sub-Skill column consulted, no SKIPPED reason read, no finding content accessed; checklist declares: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted"; absence of this declaration = C-51 ceiling fail | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 22nd and final of the 22 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference and count invariant (22nd and final of 22) -- both verifiable at zero-scan scope; Sub-claim 2 (C-40): enumerated list of 22 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Tier severity axiom(21), Declaration-completeness-proof(22); Sub-claim 3 (C-37): row count in SAD == 22 == count of targeted quality criteria | fired / partial [sub-claim] / not fired |

---

## V-03 -- Self-Match Audit Table: C-52 Ceiling (output format)

**Variation axis:** Output format -- the compliance checklist sub-claim 2 of the Verb-source
chain axis is written as an explicit 3-column audit table: `| RQG Row F-ID | Verb Source F-NN | Match? |`
The table makes the F-ID self-match constraint verifiable by column equality scan: a reviewer
scanning columns 1 and 2 sees equality (Match=YES) or mismatch (Match=NO, chain break declared)
without reading Verb Source cell content. A new dedicated SAD axis (axis 21: Self-match audit
table axis) carries three sub-observables. The Row Count Assertion promotes from 21 to 22.

**Hypothesis:** R15 V-05 established the Verb-source chain axis with the F-ID back-cite format
"DETECTION: FT[F-NN].Verb=[Verb]" and required self-match in C-52. The C-52 ceiling adds a
structural layer: the self-match verification is performed as a 3-column audit table in the
compliance checklist, not as prose assertion. The table format makes the self-match an
enumerated proof: a mismatch row is visible by column-equality scan without reading Verb Source
cell narrative. C-50 and C-51 mechanisms are not extended; R15 V-05 column-scan verification
(axis 18) and SKIPPED-tier (axis 19) remain exactly as specified.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty-two structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 22nd and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all twenty-two axes fired using sub-claim decomposition. All three
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
- **SKIPPED-T1 entity**: "SKIPPED-T1 (commitment-present): Entity [name] (E-[NN]) committed to
  [sub-skill]; execution gap. Stronger gap: promise-breach."
- **SKIPPED-T2 entity**: "SKIPPED-T2 (none-declared): Entity [name] (E-[NN]); no sub-skill
  committed. Weaker gap: planning gap."
- **Self-match audit table (zero rows)**: "SELF-MATCH AUDIT TABLE: zero rows. Table schema:
  RQG Row F-ID | Verb Source F-NN | Match?. Zero rows. Self-match vacuously satisfied: no
  F-ID exists to mismatch. C-52 ceiling verified by empty audit table."

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

Write immediately after the Topic Entity Manifest. Twenty-two rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause cited in compliance checklist; (3) sections covered: sub-skill, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty, manifest commitment, mismatch templates, column-scan empty findings, SKIPPED-T1/T2 templates, self-match audit table zero-rows template |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (twenty-two rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope source records |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks to map |
| Confidence-stratification axis | C-30, C-35 | Confidence-Stratified Action List with two named tracks; Conf rationale required per finding | (1) two named action tracks present; findings assigned by confidence x blast-radius quadrant; (2) every finding in either track carries Confidence label and falsifiable Conf rationale; (3) findings below HIGH-blast threshold excluded -- cite count excluded |
| Type-verb binding axis | C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary declared; Verb field in FT at detection; Verb column in RQG; cross-artifact consistency enforced | (1) Verb field in every FT row; vocabulary enforced at detection; out-of-vocabulary declared as bind failure; (2) Verb Source in RQG: DETECTION or CORRECTED; CORRECTED = declared bind failure; (3) count of CORRECTED == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate accounts for all declared dependency rules: honored or OPEN PROPAGATION GAP | (1) Coverage Gate present; one row per declared DR-NN; (2) {declared DR-NNs} == {gate rows union gap log}; (3) OPEN PROPAGATION GAP entries carry rule ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate signal with per-sub-skill cross-cites; Execution Log Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5; (2) P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; (3) Execution Log Layer column; Platform rows match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; (2) union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; (3) checklist verifies from SAD row alone, independent of Execution Order Gate section |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; all six columns populated; blank = fail; cite count; (2) Verb matches Type vocabulary; Verb Source documents DETECTION or CORRECTED; (3) Conformance is falsifiable: named-observable format required |
| Entity-coverage axis | C-27 | Topic Entity Manifest + Entity Coverage Matrix; COVERED / CLEAN / SKIPPED-T1 / SKIPPED-T2 per entity | (1) ECM: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED-T1/T2 logged as execution gap; (2) SKIPPED declared in checklist with entity name, ID, tier; (3) ADDED entities appended with annotation before matrix written |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + Blast Status column in RQG | (1) Re-Assessment Gate table; one row per P-ID; all columns populated; (2) ELEVATED annotation inline on Updated Ranked Findings; (3) Updated Ranked Findings re-sorted; labeled authoritative |
| Blast-status axis | C-28 extension | Third independent C-28 verification path: Blast Status column in RQG | (1) Blast Status every row: ORIGINAL or REASSESSED with direction and P-ID; (2) REASSESSED direction matches Gate table AND ELEVATED annotation; discrepancy = three-path integrity failure; (3) checklist confirms three-path consistency from Blast Status column alone |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in TEM; Commitment Honored? column in ECM; two-tier SKIPPED distinction | (1) Examining Sub-Skill column present; every entity has a value; cite counts; (2) every committed entity has Commitment Honored? = YES, MISMATCH, or N/A; cite count of each; (3) SKIPPED-T1 (promise-breach) vs SKIPPED-T2 (planning gap) -- cite one of each or confirm only one tier exists |
| Finding-verb axis | C-31 extension | Verb field in FT declared at detection; Verb Source column in RQG | (1) Verb field in every FT row -- cite count; no F-ID without Verb; (2) Verb Source count DETECTION vs CORRECTED; every CORRECTED declared as bind failure; (3) CORRECTED count == FT/RQG mismatch count |
| Column-scan verification axis | C-47, C-50 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist sub-claim 2 enumerates (F-ID, Verb) pairs; verbatim sufficiency declaration | (1) schema note "COLUMN-SCAN SURFACE (C-47)" present in Verb field definition; note names included columns (FT Verb, RQG Verb) and excluded fields; (2) checklist sub-claim 2: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced; if any narrative required, F-ID cited and scan declared insufficient; (3) verbatim declaration: "C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" |
| SKIPPED-tier axis | C-48, C-51 | SKIPPED-T1 / SKIPPED-T2 labels in ECM Status cells; tier derivation rule above ECM | (1) ECM Status cells use SKIPPED-T1 or SKIPPED-T2 (not bare "SKIPPED"); tier derivation rule present above ECM table: "T1 if Examining Sub-Skill != none-declared; T2 if == none-declared"; (2) compliance checklist sub-claim 2: every committed entity has Commitment Honored? present; SKIPPED-T1 entities cited with entity ID; (3) compliance checklist sub-claim 3: gap severity order declared -- SKIPPED-T1 (promise-breach, stronger gap) > SKIPPED-T2 (planning gap, weaker gap); cite one T1 and one T2 or confirm only one tier fired |
| Verb-source chain axis | C-49, C-52 | RQG Verb Source format: DETECTION: FT[F-NN].Verb=[Verb] or CORRECTED: FT[F-NN].Verb=[old]->[new]; F-NN must match row F-ID; compliance checklist sub-claim 2 IS the 3-column self-match audit table | (1) every Verb Source cell uses F-ID back-cite format; F-NN matches row F-ID; (2) checklist sub-claim 2: 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here -- table verifiable by column-equality scan; row count equals RQG row count; every row: Match=YES (cite count) or Match=NO with chain break declared; (3) chain break audit from table: scan columns 1 and 2 for equality without reading cell narrative; table declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" |
| Self-match audit table axis | C-52 ceiling | Compliance checklist sub-claim 2 of Verb-source chain axis IS the 3-column audit table; column-equality scan form is itself the proof | (1) 3-column audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) present in checklist sub-claim 2 of Verb-source chain axis; confirm table schema has exactly three columns and no Verb Source narrative column; row count equals RQG row count -- cite both counts; (2) every row has Match=YES or Match=NO; cite count of YES vs NO; any Match=NO row declares chain break with F-ID; if zero NO: confirm all self-matching and cite count; (3) column-equality scan audit: a reviewer scanning columns 1 and 2 for equality exhausts the self-match verification; checklist declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" -- absence of this declaration = C-52 ceiling fail |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 22nd and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 22nd and final of the 22 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42) and count invariant (C-44: 22nd and final of 22) -- both verifiable at zero-scan scope; (2) enumerated list of 22 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Self-match audit table(21), Declaration-completeness-proof(22); item 22 = "Declaration-completeness-proof axis"; (3) row count in SAD == 22 == count of targeted quality criteria |

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

Tier derivation rule (write above table): T1 if Examining Sub-Skill != none-declared;
T2 if Examining Sub-Skill == none-declared.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

Status values: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED-T1 (commitment-present) / SKIPPED-T2 (none-declared)

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

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

Apply Blast Re-Assessment Gate no-patterns template if Step 3 produced zero patterns.
Apply Blast Re-Assessment Gate no-elevation template if patterns exist but no blast increases.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label: "RANKED FINDINGS (post-re-assessment -- authoritative)"

ELEVATED findings carry inline annotation:
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

**Track 1 -- HIGH-confidence / HIGH-blast: Implement Fix Immediately**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

**Track 2 -- LOW-confidence / HIGH-blast: Confirm Spec Interpretation First**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

Apply confidence-stratification empty template if no HIGH-blast findings exist.

---

**REMEDIATION QUALITY GATE**

Every finding from the Findings Table must appear as exactly one row. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary**: GAP -> "add" or "remove"; CONTRADICTION -> "resolve"; ASSUMPTION -> "confirm"

**Conformance column rule**: "Confirm that [named behavior] is observable at [named location]
under [named condition]." Prose without named observable = fail.

**Blast Status column rule**: ORIGINAL / REASSESSED: [old] -> [new] (P-ID: [P-ID])

**Verb Source column rule**:
- DETECTION: FT[F-NN].Verb=[Verb] -- F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's F-ID

**Three-path C-28 consistency**: [old]->[new] direction must match Re-Assessment Gate,
ELEVATED annotation, and Blast Status cell. Discrepancy = declared three-path integrity failure.

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Twenty-two rows. Multi-part: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + rejection count; Sub-claim 2: T-1 ANNEX total + example + source scope; Sub-claim 3: ANNEX declared as summary aggregator only | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs named or empty-state template applied | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twenty-two rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if before any sub-skill; Sub-claim 3: Disposition columns in all five per-scope tables | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: set equality; Sub-claim 3: findings cite Dep rule backlink | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks; assignments correct; Sub-claim 2: Conf rationale per finding -- cite one verbatim; Sub-claim 3: non-HIGH-blast excluded -- cite count | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row; vocabulary enforced; Sub-claim 2: Verb Source DETECTION/CORRECTED count; CORRECTED declared; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: one row per DR-NN; Sub-claim 2: set equality; Sub-claim 3: OPEN PROPAGATION GAP entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Platform before Domain; Sub-claim 2: P1+P2 with DR-NN IDs and Execution Log cross-cites; N1+N2+N3 confirmed; Sub-claim 3: Layer column matches | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; each trace step lists; Sub-claim 2: union equals full map -- cite counts; Sub-claim 3: verified from SAD row alone | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns; cite count; Sub-claim 2: Verb matches vocabulary; Verb Source documents all; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: one row per manifest entity; counts match; Sub-claim 2: COVERED/CLEAN/SKIPPED-T1/T2 declared with tier; Sub-claim 3: ADDED entities annotated | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: one row per P-ID; all columns; Sub-claim 2: ELEVATED annotation -- cite F-ID or confirm template; Sub-claim 3: labeled authoritative | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status every row; ORIGINAL vs REASSESSED counts; Sub-claim 2: REASSESSED three-path consistency; Sub-claim 3: all ORIGINAL confirmed with template if no elevation | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column; every entity has value; cite counts; Sub-claim 2: Commitment Honored? for all committed; Sub-claim 3: SKIPPED-T1 vs SKIPPED-T2 -- cite one of each or confirm single tier | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row -- cite count; Sub-claim 2: DETECTION vs CORRECTED count; CORRECTED declared as bind failures; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47, C-50) | Findings Table + Remediation Quality Gate | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present -- cite verbatim; included/excluded fields named; Sub-claim 2: all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared; no narrative field referenced; if any narrative required, F-ID cited and scan declared insufficient; Sub-claim 3: verbatim declaration: "C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient" | fired / partial [sub-claim] / not fired |
| SKIPPED-tier axis (C-48, C-51) | Entity Coverage Matrix | Sub-claim 1: ECM Status cells use SKIPPED-T1 or SKIPPED-T2; tier derivation rule present above ECM -- cite rule verbatim; Sub-claim 2: every committed entity has Commitment Honored? value; SKIPPED-T1 entities cited with entity ID and committed sub-skill; Sub-claim 3: gap severity order declared -- SKIPPED-T1 (promise-breach) > SKIPPED-T2 (planning gap); cite one T1 and one T2 entity label from ECM Status column alone (no Examining Sub-Skill column consulted); if zero SKIPPED: confirm two-tier distinction did not fire | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49, C-52) | Remediation Quality Gate (Verb Source column) + Structural Compliance Checklist (sub-claim 2) | Sub-claim 1: every Verb Source cell uses F-ID back-cite format; cite count DETECTION vs CORRECTED; Sub-claim 2: 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here; row count equals RQG row count -- cite both; every row: Match=YES or Match=NO with chain break declared; table verifiable by column-equality scan; Sub-claim 3: audit declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row"; one complete three-point chain traced if findings exist | fired / partial [sub-claim] / not fired |
| Self-match audit table axis (C-52 ceiling) | Structural Compliance Checklist (sub-claim 2 of Verb-source chain axis) | Sub-claim 1: 3-column audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) present in checklist sub-claim 2 of Verb-source chain axis; confirm table schema has exactly three columns: RQG Row F-ID, Verb Source F-NN, Match? and no Verb Source narrative column; row count equals RQG row count -- cite both counts; Sub-claim 2: every row has Match=YES or Match=NO; cite count of YES vs NO; any Match=NO row declares chain break with F-ID; if zero NO: confirm all self-matching and cite count; if zero rows: cite self-match audit table zero-rows empty-state template; Sub-claim 3: column-equality audit: scanning columns 1 and 2 exhausts the self-match verification; checklist declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" -- absence of this declaration = C-52 ceiling fail | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 22nd and final of the 22 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference and count invariant (22nd and final of 22) -- both verifiable at zero-scan scope; Sub-claim 2 (C-40): enumerated list of 22 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Self-match audit table(21), Declaration-completeness-proof(22); item 22 = "Declaration-completeness-proof axis"; (3) row count in SAD == 22 == count of targeted quality criteria | fired / partial [sub-claim] / not fired |

---

## V-04 -- C-50 + C-52 Combined: Column-Scan Enumeration Table + Self-Match Audit Table (23 axes)

**Variation axis:** Output format + output format -- V-01 column-scan enumeration table axis
(C-50 ceiling) and V-03 self-match audit table axis (C-52 ceiling) combined on the R15 V-05
21-axis base. The two mechanisms operate on different checklist sub-claims of different axes:
the column-scan enumeration table is sub-claim 2 of the column-scan verification axis (axis 18);
the self-match audit table is sub-claim 2 of the Verb-source chain axis (axis 20). No surface
overlap. Two new dedicated SAD axes (axes 21 and 22). Row Count Assertion promotes to 23.

**Hypothesis:** Column-scan enumeration table and self-match audit table operate on structurally
disjoint checklist surfaces. The column-scan table scans FT/RQG Verb columns; the self-match
table audits RQG Verb Source F-NN equality. A CORRECTED blast status (affecting Blast Status
column) leaves both tables unaffected. Adding them simultaneously to one variation proves
independent additive compliance: neither mechanism degrades the other. C-51 mechanism (Tier
severity axiom) is not included; R15 V-05 SKIPPED-tier axis (axis 19) is unchanged.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty-three structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 23rd and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all twenty-three axes fired using sub-claim decomposition. All three
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
- **SKIPPED-T1 entity**: "SKIPPED-T1 (commitment-present): Entity [name] (E-[NN]) committed to
  [sub-skill]; execution gap. Stronger gap: promise-breach."
- **SKIPPED-T2 entity**: "SKIPPED-T2 (none-declared): Entity [name] (E-[NN]); no sub-skill
  committed. Weaker gap: planning gap."
- **Column-scan enumeration table (zero findings)**: "COLUMN-SCAN ENUMERATION TABLE: zero
  findings. Table schema: F-ID | FT Verb | RQG Verb. Zero rows. Column-scan declared sufficient
  by empty set: no narrative field read for any F-ID because no F-IDs exist."
- **Self-match audit table (zero rows)**: "SELF-MATCH AUDIT TABLE: zero rows. Table schema:
  RQG Row F-ID | Verb Source F-NN | Match?. Zero rows. Self-match vacuously satisfied: no
  F-ID exists to mismatch. C-52 ceiling verified by empty audit table."

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
Declaration.

| Entity ID | Entity Name | Category | Source | Examining Sub-Skill |
|-----------|-------------|----------|--------|---------------------|

Examining Sub-Skill: one of the five sub-skill names, or "none-declared". ADDED entities
discovered during execution: append with "ADDED -- post-execution".

---

**STRUCTURAL AXIS DECLARATION**

Write immediately after the Topic Entity Manifest. Twenty-three rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause cited in compliance checklist; (3) sections covered: all sub-skill sections, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty, manifest commitment, mismatch templates, column-scan empty findings, SKIPPED-T1/T2 templates, column-scan enumeration table empty, self-match audit table zero-rows |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (twenty-three rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope source records |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks to map |
| Confidence-stratification axis | C-30, C-35 | Confidence-Stratified Action List with two named tracks; Conf rationale required per finding | (1) two named action tracks present; findings assigned by confidence x blast-radius quadrant; (2) every finding in either track carries Confidence label and falsifiable Conf rationale; (3) findings below HIGH-blast threshold excluded -- cite count excluded |
| Type-verb binding axis | C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary declared; Verb field in FT at detection; Verb column in RQG; cross-artifact consistency enforced | (1) Verb field in every FT row; vocabulary enforced at detection; out-of-vocabulary declared as bind failure; (2) Verb Source in RQG: DETECTION or CORRECTED; CORRECTED = declared bind failure; (3) count of CORRECTED == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate accounts for all declared dependency rules: honored or OPEN PROPAGATION GAP | (1) Coverage Gate present; one row per declared DR-NN; (2) {declared DR-NNs} == {gate rows union gap log}; (3) OPEN PROPAGATION GAP entries carry rule ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate signal with per-sub-skill cross-cites; Execution Log Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5; (2) P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; (3) Execution Log Layer column; Platform rows match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; (2) union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; (3) checklist verifies from SAD row alone, independent of Execution Order Gate section |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; all six columns populated; blank = fail; cite count; (2) Verb matches Type vocabulary; Verb Source documents DETECTION or CORRECTED; (3) Conformance is falsifiable: named-observable format required |
| Entity-coverage axis | C-27 | Topic Entity Manifest + Entity Coverage Matrix; COVERED / CLEAN / SKIPPED-T1 / SKIPPED-T2 per entity | (1) ECM: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED-T1/T2 logged as execution gap; (2) SKIPPED declared in checklist with entity name, ID, tier; (3) ADDED entities appended with annotation before matrix written |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + Blast Status column in RQG | (1) Re-Assessment Gate table; one row per P-ID; all columns populated; (2) ELEVATED annotation inline on Updated Ranked Findings; (3) Updated Ranked Findings re-sorted; labeled authoritative |
| Blast-status axis | C-28 extension | Third independent C-28 verification path: Blast Status column in RQG | (1) Blast Status every row: ORIGINAL or REASSESSED with direction and P-ID; (2) REASSESSED direction matches Gate table AND ELEVATED annotation; discrepancy = three-path integrity failure; (3) checklist confirms three-path consistency from Blast Status column alone |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in TEM; Commitment Honored? column in ECM; two-tier SKIPPED distinction | (1) Examining Sub-Skill column present; every entity has a value; cite counts; (2) every committed entity has Commitment Honored? = YES, MISMATCH, or N/A; cite count of each; (3) SKIPPED-T1 vs SKIPPED-T2 -- cite one of each or confirm only one tier exists |
| Finding-verb axis | C-31 extension | Verb field in FT declared at detection; Verb Source column in RQG | (1) Verb field in every FT row -- cite count; no F-ID without Verb; (2) Verb Source count DETECTION vs CORRECTED; every CORRECTED declared as bind failure; (3) CORRECTED count == FT/RQG mismatch count |
| Column-scan verification axis | C-47, C-50 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist sub-claim 2 IS the 3-column scan table; verbatim sufficiency declaration references table by name | (1) schema note "COLUMN-SCAN SURFACE (C-47)" present in Verb field definition; note names included columns and excluded fields; (2) checklist sub-claim 2: 3-column scan table (F-ID \| FT Verb \| RQG Verb) with no narrative column; table row count == finding count; any Verb requiring narrative reading flagged inline; (3) verbatim declaration: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient; C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" |
| SKIPPED-tier axis | C-48, C-51 | SKIPPED-T1 / SKIPPED-T2 labels in ECM Status cells; tier derivation rule above ECM | (1) ECM Status cells use SKIPPED-T1 or SKIPPED-T2 (not bare "SKIPPED"); tier derivation rule present above ECM table: "T1 if Examining Sub-Skill != none-declared; T2 if == none-declared"; (2) compliance checklist sub-claim 2: every committed entity has Commitment Honored? present; SKIPPED-T1 entities cited with entity ID; (3) compliance checklist sub-claim 3: gap severity order declared -- SKIPPED-T1 (promise-breach) > SKIPPED-T2 (planning gap); cite one T1 and one T2 or confirm only one tier fired |
| Verb-source chain axis | C-49, C-52 | RQG Verb Source format: DETECTION: FT[F-NN].Verb=[Verb] or CORRECTED: FT[F-NN].Verb=[old]->[new]; F-NN must match row F-ID; compliance checklist sub-claim 2 IS the 3-column self-match audit table | (1) every Verb Source cell uses F-ID back-cite format; F-NN matches row F-ID; (2) checklist sub-claim 2: 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here; table verifiable by column-equality scan; row count equals RQG row count; every row: Match=YES or Match=NO with chain break declared; (3) audit declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" |
| Column-scan enumeration table axis | C-50 ceiling | 3-column scan table (F-ID \| FT Verb \| RQG Verb) in checklist sub-claim 2 of column-scan verification axis; no narrative column; sufficiency declaration references table by name | (1) 3-column scan table present in checklist sub-claim 2: schema is F-ID \| FT Verb \| RQG Verb and no other column; structural absence of narrative column is the scan-sufficiency proof; (2) table row count equals finding count -- cite both; any Verb requiring narrative reading flagged inline with F-ID; (3) verbatim declaration in sub-claim 3 of column-scan verification axis references enumeration table by name: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient" -- absence of named table reference = C-50 ceiling fail |
| Self-match audit table axis | C-52 ceiling | 3-column audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) in checklist sub-claim 2 of Verb-source chain axis; column-equality scan form is the proof | (1) 3-column audit table present in checklist sub-claim 2 of Verb-source chain axis: schema is RQG Row F-ID \| Verb Source F-NN \| Match? and no Verb Source narrative column; row count equals RQG row count -- cite both; (2) every row: Match=YES or Match=NO; cite count of YES vs NO; any Match=NO declares chain break with F-ID; if zero NO: confirm all self-matching; (3) checklist declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" -- absence of this declaration = C-52 ceiling fail |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 23rd and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 23rd and final of the 23 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42) and count invariant (C-44: 23rd and final of 23) -- both verifiable at zero-scan scope; (2) enumerated list of 23 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Column-scan enumeration table(21), Self-match audit table(22), Declaration-completeness-proof(23); item 23 = "Declaration-completeness-proof axis"; (3) row count in SAD == 23 == count of targeted quality criteria |

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

Tier derivation rule (write above table): T1 if Examining Sub-Skill != none-declared;
T2 if Examining Sub-Skill == none-declared.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

Status values: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED-T1 (commitment-present) / SKIPPED-T2 (none-declared)

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

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

Apply Blast Re-Assessment Gate no-patterns template if Step 3 produced zero patterns.
Apply Blast Re-Assessment Gate no-elevation template if patterns exist but no blast increases.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label: "RANKED FINDINGS (post-re-assessment -- authoritative)"

ELEVATED findings carry inline annotation:
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

**Track 1 -- HIGH-confidence / HIGH-blast: Implement Fix Immediately**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

**Track 2 -- LOW-confidence / HIGH-blast: Confirm Spec Interpretation First**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

Apply confidence-stratification empty template if no HIGH-blast findings exist.

---

**REMEDIATION QUALITY GATE**

Every finding from the Findings Table must appear as exactly one row. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary**: GAP -> "add" or "remove"; CONTRADICTION -> "resolve"; ASSUMPTION -> "confirm"

**Conformance column rule**: "Confirm that [named behavior] is observable at [named location]
under [named condition]." Prose without named observable = fail.

**Blast Status column rule**: ORIGINAL / REASSESSED: [old] -> [new] (P-ID: [P-ID])

**Verb Source column rule**:
- DETECTION: FT[F-NN].Verb=[Verb] -- F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's F-ID

**Three-path C-28 consistency**: [old]->[new] direction must match Re-Assessment Gate,
ELEVATED annotation, and Blast Status cell. Discrepancy = declared three-path integrity failure.

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Twenty-three rows. Multi-part: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + rejection count; Sub-claim 2: T-1 ANNEX total + example + source scope; Sub-claim 3: ANNEX declared as summary aggregator only | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs named or empty-state template applied | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twenty-three rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if before any sub-skill; Sub-claim 3: Disposition columns in all five per-scope tables | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: set equality; Sub-claim 3: findings cite Dep rule backlink | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks; assignments correct; Sub-claim 2: Conf rationale per finding -- cite one verbatim; Sub-claim 3: non-HIGH-blast excluded -- cite count | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row; vocabulary enforced; Sub-claim 2: DETECTION/CORRECTED count; CORRECTED declared; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: one row per DR-NN; Sub-claim 2: set equality; Sub-claim 3: OPEN PROPAGATION GAP entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Platform before Domain; Sub-claim 2: P1+P2 with DR-NN IDs and Execution Log cross-cites; N1+N2+N3 confirmed; Sub-claim 3: Layer column matches | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; each trace step lists; Sub-claim 2: union equals full map -- cite counts; Sub-claim 3: verified from SAD row alone | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns; cite count; Sub-claim 2: Verb matches vocabulary; Verb Source documents all; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: one row per manifest entity; counts match; Sub-claim 2: COVERED/CLEAN/SKIPPED-T1/T2 declared with tier; Sub-claim 3: ADDED entities annotated | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: one row per P-ID; all columns; Sub-claim 2: ELEVATED annotation -- cite F-ID or confirm template; Sub-claim 3: labeled authoritative | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status every row; ORIGINAL vs REASSESSED counts; Sub-claim 2: REASSESSED three-path consistency; Sub-claim 3: all ORIGINAL confirmed with template if no elevation | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column; every entity has value; Sub-claim 2: Commitment Honored? for all committed; Sub-claim 3: SKIPPED-T1 vs SKIPPED-T2 -- cite one of each or confirm single tier | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row -- cite count; Sub-claim 2: DETECTION vs CORRECTED count; CORRECTED declared as bind failures; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47, C-50) | Findings Table + Structural Compliance Checklist (sub-claim 2) | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present -- cite verbatim; included/excluded fields named; Sub-claim 2: 3-column scan table (F-ID \| FT Verb \| RQG Verb) written here -- no narrative column; table row count == finding count; any Verb requiring narrative reading flagged inline; Sub-claim 3: verbatim declaration: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient; C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" | fired / partial [sub-claim] / not fired |
| SKIPPED-tier axis (C-48, C-51) | Entity Coverage Matrix | Sub-claim 1: ECM Status cells use SKIPPED-T1 or SKIPPED-T2; tier derivation rule present above ECM -- cite rule; Sub-claim 2: every committed entity has Commitment Honored? value; SKIPPED-T1 entities cited with entity ID; Sub-claim 3: gap severity order declared -- SKIPPED-T1 (promise-breach) > SKIPPED-T2 (planning gap); cite one T1 and one T2 entity label from ECM Status column alone (no Examining Sub-Skill consulted); if zero SKIPPED: confirm two-tier distinction did not fire | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49, C-52) | Remediation Quality Gate (Verb Source column) + Structural Compliance Checklist (sub-claim 2) | Sub-claim 1: every Verb Source cell uses F-ID back-cite format; cite count DETECTION vs CORRECTED; Sub-claim 2: 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here; table verifiable by column-equality scan; row count equals RQG row count; every row: Match=YES or Match=NO with chain break declared; Sub-claim 3: audit declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" | fired / partial [sub-claim] / not fired |
| Column-scan enumeration table axis (C-50 ceiling) | Structural Compliance Checklist (sub-claim 2 of column-scan verification axis) | Sub-claim 1: 3-column scan table present in checklist sub-claim 2 of column-scan verification axis; schema: F-ID \| FT Verb \| RQG Verb and no other column; row count equals finding count -- cite both; Sub-claim 2: every row has both Verb values without narrative field read; any flagged row declares C-50 ceiling fail for that row; Sub-claim 3: verbatim declaration in sub-claim 3 references enumeration table by name: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient" -- absence of named table reference = C-50 ceiling fail | fired / partial [sub-claim] / not fired |
| Self-match audit table axis (C-52 ceiling) | Structural Compliance Checklist (sub-claim 2 of Verb-source chain axis) | Sub-claim 1: 3-column audit table present in checklist sub-claim 2 of Verb-source chain axis; schema: RQG Row F-ID \| Verb Source F-NN \| Match? and no Verb Source narrative column; row count equals RQG row count -- cite both; Sub-claim 2: every row: Match=YES or Match=NO; cite YES vs NO counts; any NO declares chain break with F-ID; Sub-claim 3: checklist declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" -- absence of this declaration = C-52 ceiling fail | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 23rd and final of the 23 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference and count invariant (23rd and final of 23); Sub-claim 2 (C-40): enumerated list of 23 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Column-scan enumeration table(21), Self-match audit table(22), Declaration-completeness-proof(23); Sub-claim 3 (C-37): row count in SAD == 23 | fired / partial [sub-claim] / not fired |

---

## V-05 -- Full Integration: C-50 + C-51 + C-52 Ceilings (24 axes)

**Variation axis:** Full integration -- V-01 column-scan enumeration table axis (C-50 ceiling)
+ V-02 tier severity axiom axis (C-51 ceiling) + V-03 self-match audit table axis (C-52 ceiling)
on R15 V-05 21-axis base. Three mechanisms added simultaneously, each on a disjoint surface:
the 3-column scan table is in checklist sub-claim 2 of axis 18; the SEVERITY AXIOM block is
before the ECM table; the 3-column self-match audit table is in checklist sub-claim 2 of axis
20. No mechanism interferes with any other. Three new dedicated SAD axes (21, 22, 23). Row
Count Assertion promotes to 24.

**Hypothesis:** The three ceiling mechanisms operate on three non-overlapping surfaces: the FT
schema note and its checklist enumeration format (C-50); the pre-ECM formal axiom block and its
checklist derivation (C-51); the RQG Verb Source cell format and its checklist audit table
(C-52). A REASSESSED blast status (affecting Blast Status column) leaves all three surfaces
unchanged. A CORRECTED Verb Source entry (C-52) leaves the FT Verb scan table (C-50) and the
SEVERITY AXIOM block (C-51) unchanged. All three ceiling proofs remain independently falsifiable
in the same execution. The Row Count Assertion at 24 preserves the "Nth and final of N"
structural property without brittle count-specific encoding.

---

Simulate the technical behavior of: {{topic}}

This report enforces twenty-four structural axes simultaneously. The first section is the Topic
Entity Manifest (with Examining Sub-Skill column), declaring the entity coverage commitment
before any structural axis is declared. The second section is the Structural Axis Declaration,
which is itself the 24th and final declared axis. The last section is the Structural Compliance
Checklist, which verifies all twenty-four axes fired using sub-claim decomposition. All three
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
- **SKIPPED-T1 entity**: "SKIPPED-T1 (commitment-present): Entity [name] (E-[NN]) committed to
  [sub-skill]; execution gap. SEVERITY AXIOM: T1 = promise-breach -- stronger gap."
- **SKIPPED-T2 entity**: "SKIPPED-T2 (none-declared): Entity [name] (E-[NN]); no sub-skill
  committed. SEVERITY AXIOM: T2 = planning gap -- weaker gap."
- **Column-scan enumeration table (zero findings)**: "COLUMN-SCAN ENUMERATION TABLE: zero
  findings. Table schema: F-ID | FT Verb | RQG Verb. Zero rows. Column-scan declared sufficient
  by empty set: no narrative field read for any F-ID because no F-IDs exist."
- **Tier severity axiom (no SKIPPED entities)**: "SEVERITY AXIOM fired; zero SKIPPED entities.
  T1-T2 distinction did not activate. Axiom on record: T1 > T2 severity. Axiom application:
  none required this execution."
- **Self-match audit table (zero rows)**: "SELF-MATCH AUDIT TABLE: zero rows. Table schema:
  RQG Row F-ID | Verb Source F-NN | Match?. Zero rows. Self-match vacuously satisfied: no
  F-ID exists to mismatch. C-52 ceiling verified by empty audit table."

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
Declaration.

| Entity ID | Entity Name | Category | Source | Examining Sub-Skill |
|-----------|-------------|----------|--------|---------------------|

Examining Sub-Skill: one of the five sub-skill names, or "none-declared". ADDED entities
discovered during execution: append with "ADDED -- post-execution".

---

**STRUCTURAL AXIS DECLARATION**

Write immediately after the Topic Entity Manifest. Twenty-four rows required, three
independently-verifiable sub-observables each.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution (Template A / Template B) | (1) Candidate Observations: Elevate? and Rejection Reason columns; (2) Filter Log Resolution: template letter and count; (3) filter rules 1-4 declared before any row evaluated |
| Empty-state axis | C-11, C-34 | Per-section named templates; silent sections prohibited | (1) Named template in any empty section; (2) type and first clause cited in compliance checklist; (3) sections covered: all sub-skill sections, ranked tiers, comparison steps, both Blast Gate states, confidence tracks empty, Disposition zero-withheld-T1, Execution Log zero-contribution, Remediation Quality Gate empty, manifest commitment, mismatch templates, column-scan empty findings, SKIPPED-T1/T2 templates, column-scan enumeration table empty, tier severity axiom no-SKIPPED, self-match audit table zero-rows |
| Cross-skill comparison axis | C-15 | Three-step protocol with stable P-IDs (Step 3) | (1) Step 1: F-ID A, F-ID B, surface similarity; (2) Step 2: verdict, reason; (3) Step 3: P-IDs named or empty-state template applied |
| Declaration-compliance axis | C-17, C-18 | SAD (twenty-four rows) + Compliance Checklist (sub-claim architecture) | (1) SAD before execution evidence; (2) Checklist final with sub-claim decomposition; binary verdict = structural violation; (3) evidence cites actual section names and counts |
| Observational discipline axis | C-19, C-20, C-21 | Genre declaration + T-1 rule (if-and-only-if) + five per-scope gate tables + T-1 ANNEX | (1) four-term glossary; T-1 if-and-only-if stated before any sub-skill; (2) five per-scope gate tables with Disposition column; (3) T-1 ANNEX: summary aggregator role stated; cites per-scope source records |
| DR-NN citation chain axis | C-32 | Three-point chain: dependency map declaration, Coverage Gate row, finding Dep rule cite field | (1) Cross-Skill Dependency Map: DR-NN ID + source sub-skill + constraint; (2) Coverage Gate cites DR-NNs; {map IDs} == {gate rows union gap log}; (3) finding Dep rule cite backlinks to map |
| Confidence-stratification axis | C-30, C-35 | Confidence-Stratified Action List with two named tracks; Conf rationale required per finding | (1) two named action tracks present; findings assigned by confidence x blast-radius quadrant; (2) every finding in either track carries Confidence label and falsifiable Conf rationale; (3) findings below HIGH-blast threshold excluded -- cite count excluded |
| Type-verb binding axis | C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary declared; Verb field in FT at detection; Verb column in RQG; cross-artifact consistency enforced | (1) Verb field in every FT row; vocabulary enforced at detection; out-of-vocabulary declared as bind failure; (2) Verb Source in RQG: DETECTION or CORRECTED; CORRECTED = declared bind failure; (3) count of CORRECTED == count of F-IDs where FT Verb != RQG Verb |
| Propagation coverage axis | C-29 | Coverage Gate accounts for all declared dependency rules: honored or OPEN PROPAGATION GAP | (1) Coverage Gate present; one row per declared DR-NN; (2) {declared DR-NNs} == {gate rows union gap log}; (3) OPEN PROPAGATION GAP entries carry rule ID and reason |
| Execution-order axis | C-36, C-38, C-39, C-41 | Layer Completion Record; P1/P2 gate signal with per-sub-skill cross-cites; Execution Log Layer column | (1) Layer Completion Record: Platform 1-3 complete before Domain 4-5; (2) P1 names three Platform sub-skills; P2 per-sub-skill entries cite DR-NN IDs AND Execution Log row by name; N1+N2+N3=N_total confirmed; (3) Execution Log Layer column; Platform rows match P2; Domain "n/a" |
| Execution-log attribution axis | C-43, C-45 | Dedicated SAD row; DR-NN Contributed column in Execution Log; union-of-rows equality check | (1) DR-NN Contributed column present; each trace step lists DR-NNs or zero-template; (2) union of Contributed entries rows 1-3 equals full dependency map -- cite both counts; (3) checklist verifies from SAD row alone, independent of Execution Order Gate section |
| Remediation-quality axis | C-26 | REMEDIATION QUALITY GATE: Verb / Target / Location / Conformance / Blast Status / Verb Source per F-ID | (1) one row per F-ID; all six columns populated; blank = fail; cite count; (2) Verb matches Type vocabulary; Verb Source documents DETECTION or CORRECTED; (3) Conformance is falsifiable: named-observable format required |
| Entity-coverage axis | C-27 | Topic Entity Manifest + Entity Coverage Matrix; COVERED / CLEAN / SKIPPED-T1 / SKIPPED-T2 per entity | (1) ECM: one row per manifest entity; COVERED cites F-ID or Obs #; CLEAN names sub-skill and reason; SKIPPED-T1/T2 logged as execution gap; (2) SKIPPED declared in checklist with entity name, ID, tier; (3) ADDED entities appended with annotation before matrix written |
| Blast-reassessment axis | C-28 | BLAST RADIUS RE-ASSESSMENT GATE + ELEVATED inline annotations + Blast Status column in RQG | (1) Re-Assessment Gate table; one row per P-ID; all columns populated; (2) ELEVATED annotation inline on Updated Ranked Findings; (3) Updated Ranked Findings re-sorted; labeled authoritative |
| Blast-status axis | C-28 extension | Third independent C-28 verification path: Blast Status column in RQG | (1) Blast Status every row: ORIGINAL or REASSESSED with direction and P-ID; (2) REASSESSED direction matches Gate table AND ELEVATED annotation; discrepancy = three-path integrity failure; (3) checklist confirms three-path consistency from Blast Status column alone |
| Manifest-commitment axis | C-27 extension | Examining Sub-Skill column in TEM; Commitment Honored? column in ECM; two-tier SKIPPED distinction | (1) Examining Sub-Skill column present; every entity has a value; cite counts; (2) every committed entity has Commitment Honored? = YES, MISMATCH, or N/A; cite count of each; (3) SKIPPED-T1 vs SKIPPED-T2 -- cite one of each or confirm only one tier exists |
| Finding-verb axis | C-31 extension | Verb field in FT declared at detection; Verb Source column in RQG | (1) Verb field in every FT row -- cite count; no F-ID without Verb; (2) Verb Source count DETECTION vs CORRECTED; every CORRECTED declared as bind failure; (3) CORRECTED count == FT/RQG mismatch count |
| Column-scan verification axis | C-47, C-50 | FT Verb column carries "COLUMN-SCAN SURFACE (C-47)" schema note; compliance checklist sub-claim 2 IS the 3-column scan table; verbatim sufficiency declaration references table by name | (1) schema note "COLUMN-SCAN SURFACE (C-47)" present in Verb field definition; note names included columns and excluded fields; (2) checklist sub-claim 2: 3-column scan table (F-ID \| FT Verb \| RQG Verb) with no narrative column; table row count == finding count; any Verb requiring narrative reading flagged inline; (3) verbatim declaration: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient; C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" |
| SKIPPED-tier axis | C-48, C-51 | SKIPPED-T1 / SKIPPED-T2 labels in ECM Status cells; tier derivation rule above ECM; SEVERITY AXIOM block before ECM delivers the gap-ordering proof | (1) ECM Status cells use SKIPPED-T1 or SKIPPED-T2 (not bare "SKIPPED"); tier derivation rule present above ECM table; (2) SEVERITY AXIOM block present before ECM: "T1 > T2 severity: T1 = promise-breach; T2 = planning gap"; axiom is standalone named block; (3) checklist sub-claim 3 derives severity ordering from SEVERITY AXIOM text + Status cell tier label alone -- no Examining Sub-Skill column or finding content consulted; cite axiom clause and one Status cell tier label |
| Verb-source chain axis | C-49, C-52 | RQG Verb Source format: DETECTION: FT[F-NN].Verb=[Verb] or CORRECTED: FT[F-NN].Verb=[old]->[new]; F-NN must match row F-ID; compliance checklist sub-claim 2 IS the 3-column self-match audit table | (1) every Verb Source cell uses F-ID back-cite format; F-NN matches row F-ID; (2) checklist sub-claim 2: 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here; table verifiable by column-equality scan; row count equals RQG row count; every row: Match=YES or Match=NO with chain break declared; (3) audit declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" |
| Column-scan enumeration table axis | C-50 ceiling | 3-column scan table (F-ID \| FT Verb \| RQG Verb) in checklist sub-claim 2 of column-scan verification axis; no narrative column; sufficiency declaration references table by name | (1) 3-column scan table present in checklist sub-claim 2: schema is F-ID \| FT Verb \| RQG Verb and no other column; structural absence of narrative column is the scan-sufficiency proof; (2) table row count equals finding count -- cite both; any Verb requiring narrative reading flagged inline; (3) verbatim declaration in sub-claim 3 references enumeration table by name: "3-column scan table at sub-claim 2 is the enumeration proof" -- absence of named table reference = C-50 ceiling fail |
| Tier severity axiom axis | C-51 ceiling | SEVERITY AXIOM block written before ECM table; axiom falsifiable by its own terms; checklist sub-claim 3 of SKIPPED-tier axis derives severity ordering from axiom + Status cell tier label alone | (1) SEVERITY AXIOM block present before ECM -- cite axiom location and first clause verbatim: "T1 severity > T2 severity. T1 = promise-breach (sub-skill committed, execution skipped). T2 = planning gap (no sub-skill committed, no promise made)"; confirm standalone named block not embedded in prose; (2) checklist sub-claim 3 of SKIPPED-tier axis cites SEVERITY AXIOM text and at least one T1 label and one T2 label from ECM Status column (or confirms single tier fired); axiom citation is the derivation proof; (3) severity ordering derivable from SEVERITY AXIOM text + ECM Status tier label alone; checklist declares: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted"; absence of this declaration = C-51 ceiling fail |
| Self-match audit table axis | C-52 ceiling | 3-column audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) in checklist sub-claim 2 of Verb-source chain axis; column-equality scan form is the proof | (1) 3-column audit table present in checklist sub-claim 2 of Verb-source chain axis: schema is RQG Row F-ID \| Verb Source F-NN \| Match? and no Verb Source narrative column; row count equals RQG row count -- cite both; (2) every row: Match=YES or Match=NO; cite YES vs NO counts; any NO declares chain break with F-ID; (3) checklist declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" -- absence of this declaration = C-52 ceiling fail |
| Declaration-completeness-proof axis | C-37, C-40, C-42, C-44 | Row Count Assertion as the 24th and final targeted axis; opening sentence embeds count invariant and self-reference simultaneously | This Row Count Assertion, itself the 24th and final of the 24 targeted axes declared below, is C-37's completeness proof: (1) opening sentence simultaneously declares self-reference (C-42) and count invariant (C-44: 24th and final of 24) -- both verifiable at zero-scan scope; (2) enumerated list of 24 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Column-scan enumeration table(21), Tier severity axiom(22), Self-match audit table(23), Declaration-completeness-proof(24); item 24 = "Declaration-completeness-proof axis"; (3) row count in SAD == 24 == count of targeted quality criteria |

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

**SEVERITY AXIOM**

Write immediately before the Entity Coverage Matrix.

> SEVERITY AXIOM: T1 severity > T2 severity.
> T1 = promise-breach (sub-skill committed in TEM, execution skipped).
> T2 = planning gap (no sub-skill committed, no promise made).
> Corollary: SKIPPED-T1 findings require stronger remediation priority than SKIPPED-T2.
> Falsification condition: any SKIPPED-T2 entity prioritized above a SKIPPED-T1 entity
> contradicts this axiom and must be declared in the compliance checklist.

Apply "Tier severity axiom (no SKIPPED entities)" template if zero SKIPPED entities exist.

---

**ENTITY COVERAGE MATRIX**

Write after Execution Log and SEVERITY AXIOM block, before Initial Ranked Findings.

Tier derivation rule (write above table): T1 if Examining Sub-Skill != none-declared;
T2 if Examining Sub-Skill == none-declared.

| Entity ID | Entity Name | Status | Sub-Skill(s) | Evidence (F-ID / Obs # / clean reason) | Commitment Honored? |
|-----------|-------------|--------|--------------|----------------------------------------|---------------------|

Status values: COVERED (cite F-ID or Obs #) / CLEAN (name sub-skill and reason) /
SKIPPED-T1 (commitment-present) / SKIPPED-T2 (none-declared)

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

| P-ID | Participant F-IDs | Individual Blast Radii | Compound Blast | F-IDs Elevated | Direction |
|------|-------------------|----------------------|----------------|----------------|-----------|

Apply Blast Re-Assessment Gate no-patterns template if Step 3 produced zero patterns.
Apply Blast Re-Assessment Gate no-elevation template if patterns exist but no blast increases.

---

**UPDATED RANKED FINDINGS** (post-re-assessment -- authoritative)

Label: "RANKED FINDINGS (post-re-assessment -- authoritative)"

ELEVATED findings carry inline annotation:
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

**Track 1 -- HIGH-confidence / HIGH-blast: Implement Fix Immediately**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

**Track 2 -- LOW-confidence / HIGH-blast: Confirm Spec Interpretation First**

| F-ID | Confidence | Conf Rationale | Action |
|------|-----------|----------------|--------|

Apply confidence-stratification empty template if no HIGH-blast findings exist.

---

**REMEDIATION QUALITY GATE**

Every finding from the Findings Table must appear as exactly one row. Blank cell = fail.

| F-ID | Verb | Target | Location | Conformance | Blast Status | Verb Source |
|------|------|--------|----------|-------------|--------------|-------------|

**Verb vocabulary**: GAP -> "add" or "remove"; CONTRADICTION -> "resolve"; ASSUMPTION -> "confirm"

**Conformance column rule**: "Confirm that [named behavior] is observable at [named location]
under [named condition]." Prose without named observable = fail.

**Blast Status column rule**: ORIGINAL / REASSESSED: [old] -> [new] (P-ID: [P-ID])

**Verb Source column rule**:
- DETECTION: FT[F-NN].Verb=[Verb] -- F-NN must match this row's F-ID
- CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared -- F-NN must match this row's F-ID

**Three-path C-28 consistency**: [old]->[new] direction must match Re-Assessment Gate,
ELEVATED annotation, and Blast Status cell. Discrepancy = declared three-path integrity failure.

**Surface independence declaration**: A REASSESSED Blast Status does not alter Verb, Verb Source,
SEVERITY AXIOM, or the column-scan enumeration table. A CORRECTED Verb Source does not alter
the SEVERITY AXIOM or Blast Status. All three ceiling proofs remain independently falsifiable
in the same execution.

If no findings: apply Remediation Quality Gate empty template.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write as the final section. Twenty-four rows. Multi-part: `fired / partial [sub-claim] / not fired`.
Binary PASS or FAIL = structural violation.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log | Candidate Observations and Filter Log | [total observations; rule-by-rule counts] | fired / not fired |
| Filter Log Resolution + T-1 ANNEX | Filter Log Resolution | Sub-claim 1: template letter + rejection count; Sub-claim 2: T-1 ANNEX total + example + source scope; Sub-claim 3: ANNEX declared as summary aggregator only | fired / partial [sub-claim] / not fired |
| Empty-state templates (C-11, C-34) | [sections fired] | [template name and first clause each] | fired / not fired |
| Cross-skill comparison | Cross-Skill Comparison Protocol | Sub-claim 1: Step 1 ([N] pairs); Sub-claim 2: Step 2 ([N] verdicts); Sub-claim 3: Step 3 P-IDs named or empty-state template applied | fired / partial [sub-claim] / not fired |
| Structural Axis Declaration | Structural Axis Declaration | Sub-claim 1: twenty-four rows; Sub-claim 2: three sub-observables each; Sub-claim 3: before any execution evidence | fired / partial [sub-claim] / not fired |
| Observational discipline axis | [per-scope sections] + T-1 ANNEX | Sub-claim 1: four-term glossary; Sub-claim 2: T-1 if-and-only-if before any sub-skill; Sub-claim 3: Disposition columns in all five per-scope tables | fired / partial [sub-claim] / not fired |
| DR-NN citation chain (C-32) | Dependency Map + Coverage Gate + Findings Table | Sub-claim 1: DR-NN IDs in map -- cite count; Sub-claim 2: set equality; Sub-claim 3: findings cite Dep rule backlink | fired / partial [sub-claim] / not fired |
| Confidence-stratification axis (C-30, C-35) | Confidence-Stratified Action List | Sub-claim 1: two named tracks; assignments correct; Sub-claim 2: Conf rationale per finding -- cite one verbatim; Sub-claim 3: non-HIGH-blast excluded -- cite count | fired / partial [sub-claim] / not fired |
| Type-verb binding axis (C-31) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row; vocabulary enforced; Sub-claim 2: DETECTION/CORRECTED count; CORRECTED declared; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Propagation coverage axis (C-29) | Coverage Gate | Sub-claim 1: one row per DR-NN; Sub-claim 2: set equality; Sub-claim 3: OPEN PROPAGATION GAP entries carry rule ID and reason | fired / partial [sub-claim] / not fired |
| Execution-order axis (C-36, C-38, C-39, C-41) | EXECUTION ORDER GATE + Execution Log | Sub-claim 1: Layer Completion Record; Platform before Domain; Sub-claim 2: P1+P2 with DR-NN IDs and Execution Log cross-cites; N1+N2+N3 confirmed; Sub-claim 3: Layer column matches | fired / partial [sub-claim] / not fired |
| Execution-log attribution axis (C-43, C-45) | Execution Log | Sub-claim 1: DR-NN Contributed column; each trace step lists; Sub-claim 2: union equals full map -- cite counts; Sub-claim 3: verified from SAD row alone | fired / partial [sub-claim] / not fired |
| Remediation-quality axis (C-26) | Remediation Quality Gate | Sub-claim 1: one row per F-ID; all six columns; cite count; Sub-claim 2: Verb matches vocabulary; Verb Source documents all; Sub-claim 3: Conformance is falsifiable -- cite one cell verbatim | fired / partial [sub-claim] / not fired |
| Entity-coverage axis (C-27) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: one row per manifest entity; counts match; Sub-claim 2: COVERED/CLEAN/SKIPPED-T1/T2 declared with tier; Sub-claim 3: ADDED entities annotated | fired / partial [sub-claim] / not fired |
| Blast-reassessment axis (C-28) | Blast Radius Re-Assessment Gate + Updated Ranked Findings | Sub-claim 1: one row per P-ID; all columns; Sub-claim 2: ELEVATED annotation -- cite F-ID or confirm template; Sub-claim 3: labeled authoritative | fired / partial [sub-claim] / not fired |
| Blast-status axis (C-28 extension) | Remediation Quality Gate (Blast Status column) | Sub-claim 1: Blast Status every row; ORIGINAL vs REASSESSED counts; Sub-claim 2: REASSESSED three-path consistency; Sub-claim 3: all ORIGINAL confirmed with template if no elevation | fired / partial [sub-claim] / not fired |
| Manifest-commitment axis (C-27 extension) | Topic Entity Manifest + Entity Coverage Matrix | Sub-claim 1: Examining Sub-Skill column; every entity has value; Sub-claim 2: Commitment Honored? for all committed; Sub-claim 3: SKIPPED-T1 vs SKIPPED-T2 -- cite one of each or confirm single tier | fired / partial [sub-claim] / not fired |
| Finding-verb axis (C-31 extension) | Findings Table + Remediation Quality Gate | Sub-claim 1: Verb field every FT row -- cite count; Sub-claim 2: DETECTION vs CORRECTED count; CORRECTED declared as bind failures; Sub-claim 3: CORRECTED count == mismatch count | fired / partial [sub-claim] / not fired |
| Column-scan verification axis (C-47, C-50) | Findings Table + Structural Compliance Checklist (sub-claim 2) | Sub-claim 1: schema note "COLUMN-SCAN SURFACE (C-47)" present -- cite verbatim; included/excluded fields named; Sub-claim 2: 3-column scan table (F-ID \| FT Verb \| RQG Verb) written here -- no narrative column; table row count == finding count; any Verb requiring narrative reading flagged inline; Sub-claim 3: verbatim declaration: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient; C-47 and C-50 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID" | fired / partial [sub-claim] / not fired |
| SKIPPED-tier axis (C-48, C-51) | Entity Coverage Matrix + SEVERITY AXIOM block | Sub-claim 1: ECM Status cells use SKIPPED-T1 or SKIPPED-T2; tier derivation rule present above ECM -- cite rule; Sub-claim 2: SEVERITY AXIOM block present before ECM -- cite axiom first clause verbatim; axiom is standalone named block; Sub-claim 3: gap severity derived from SEVERITY AXIOM + ECM Status tier label only: cite axiom clause and one T1 label and one T2 label from Status column (or confirm single tier); no Examining Sub-Skill column consulted; checklist declares: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted" | fired / partial [sub-claim] / not fired |
| Verb-source chain axis (C-49, C-52) | Remediation Quality Gate (Verb Source column) + Structural Compliance Checklist (sub-claim 2) | Sub-claim 1: every Verb Source cell uses F-ID back-cite format; cite count DETECTION vs CORRECTED; Sub-claim 2: 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here; table verifiable by column-equality scan; row count equals RQG row count; every row: Match=YES or Match=NO with chain break declared; Sub-claim 3: audit declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" | fired / partial [sub-claim] / not fired |
| Column-scan enumeration table axis (C-50 ceiling) | Structural Compliance Checklist (sub-claim 2 of column-scan verification axis) | Sub-claim 1: 3-column scan table present in checklist sub-claim 2 of column-scan verification axis; schema: F-ID \| FT Verb \| RQG Verb and no other column; row count equals finding count -- cite both; Sub-claim 2: every row has both Verb values without narrative field read; any flagged row declares C-50 ceiling fail for that row; Sub-claim 3: verbatim declaration in sub-claim 3 references enumeration table by name: "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient" -- absence of named table reference = C-50 ceiling fail | fired / partial [sub-claim] / not fired |
| Tier severity axiom axis (C-51 ceiling) | SEVERITY AXIOM block + Structural Compliance Checklist (sub-claim 3 of SKIPPED-tier axis) | Sub-claim 1: SEVERITY AXIOM block present before ECM table; cite axiom location and first clause verbatim: "T1 severity > T2 severity. T1 = promise-breach (sub-skill committed, execution skipped). T2 = planning gap (no sub-skill committed, no promise made)"; confirm standalone named block not embedded in prose; Sub-claim 2: sub-claim 3 of SKIPPED-tier axis cites SEVERITY AXIOM text and at least one T1 label and one T2 label from ECM Status column -- or confirms single tier fired; axiom citation is the derivation proof; Sub-claim 3: severity ordering derivable from SEVERITY AXIOM text + ECM Status tier label alone -- no Examining Sub-Skill column consulted; checklist declares: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted"; absence of this declaration = C-51 ceiling fail | fired / partial [sub-claim] / not fired |
| Self-match audit table axis (C-52 ceiling) | Structural Compliance Checklist (sub-claim 2 of Verb-source chain axis) | Sub-claim 1: 3-column audit table present in checklist sub-claim 2 of Verb-source chain axis: schema is RQG Row F-ID \| Verb Source F-NN \| Match? and no Verb Source narrative column; row count equals RQG row count -- cite both; Sub-claim 2: every row: Match=YES or Match=NO; cite YES vs NO counts; any NO declares chain break with F-ID; if zero NO: confirm all self-matching; Sub-claim 3: checklist declares: "self-match verified by column-equality scan; Verb Source cell content not read for any row" -- absence of this declaration = C-52 ceiling fail | fired / partial [sub-claim] / not fired |
| Declaration-completeness-proof axis (C-37, C-40, C-42, C-44) | SAD + this Row Count Assertion block | This Row Count Assertion, itself the 24th and final of the 24 targeted axes declared below, is C-37's completeness proof: Sub-claim 1 (C-44): opening sentence declares self-reference and count invariant (24th and final of 24) -- both verifiable at zero-scan scope; Sub-claim 2 (C-40): enumerated list of 24 axes: Filtering(1), Empty-state(2), Cross-skill comparison(3), Declaration-compliance(4), Observational discipline(5), DR-NN citation chain(6), Confidence-stratification(7), Type-verb binding(8), Propagation coverage(9), Execution-order(10), Execution-log attribution(11), Remediation-quality(12), Entity-coverage(13), Blast-reassessment(14), Blast-status(15), Manifest-commitment(16), Finding-verb(17), Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Column-scan enumeration table(21), Tier severity axiom(22), Self-match audit table(23), Declaration-completeness-proof(24); item 24 = "Declaration-completeness-proof axis"; (3) row count in SAD == 24 == count of targeted quality criteria | fired / partial [sub-claim] / not fired |

---
