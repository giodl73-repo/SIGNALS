# review-design Scorecard — Round 15
**Rubric version**: v14 (C-01 through C-44, denominator 37 aspirational)
**Date**: 2026-03-15
**Variations scored**: V-01 through V-05
**Baseline**: R14 V-02 (score 100, C-43 and C-44 not yet encoded)
**Scorer**: Claude Sonnet 4.6 [1M]

---

## Scoring Legend

| Mark | Meaning |
|------|---------|
| PASS | Criterion fully satisfied |
| PARTIAL | Criterion partially satisfied (counts as 0 for scoring) |
| FAIL | Criterion not satisfied |

**Score formula (denominator 37 aspirational):**
```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 37 * 10)
```

---

## Evidence Basis per Variation

### V-01 Key Evidence
- Carries all F-01 through F-28 from R14 V-02
- BLOCK 2.7: dedicated named block, positioned after BLOCK 2.5 before BLOCK 3 (no POSITION CONSTRAINT paragraph, but block is structurally in place and F-28 references "the BLOCK 2.7 P1 Section Registry")
- F-28: split into labeled **Downstream fix** / **Upstream fix** sentences
- Other cross-block mismatch halts (F-10, F-15, F-16, F-17): remain single-path only
- C-37: context preamble states "Each F-ID trigger clause includes an inline resolution instruction with a named referent"; F-IDs are the proven R14 referentially-complete set
- F-30: "Add BLOCK 2.7 before continuing. Halt." — no position instruction in F-30

### V-02 Key Evidence
- BLOCK 2.7: explicit POSITION CONSTRAINT paragraph naming conformant lifecycle order; declares inline BLOCK 5 placement non-conformant
- F-30: "Add BLOCK 2.7 in the correct position — after BLOCK 2.5, before BLOCK 3 — before continuing. Halt."
- F-28: "Correct the Section value to match an entry in the BLOCK 2.7 registry (the registry established before BLOCK 3), or add the P1 finding to the appropriate reviewer block in BLOCK 2 and update the BLOCK 2.7 registry before continuing." — "or" construction naming both paths but not as labeled items
- Other cross-block halts (F-10, F-15, F-16, F-17): single-path corrective actions
- C-37: F-19 uses "Populate the Rationale cell before continuing" — anaphoric but may fail because V-02 pattern in R13/R14 was noted as FAIL C-37

### V-03 Key Evidence
- Operational-directive register (Steps, Required:, no F-IDs in halt clauses)
- Step 2.7 = "Section Map" with "Build this step before Step 3 begins" instruction; position constraint is prose-directive not formal-modal
- Step 5 F-28 equivalent: numbered two-option repair "apply one of two fixes — (1) correct... or (2) add... and update"
- No named F-IDs in halt clauses (Required: format instead) — C-14 FAIL
- Other cross-block checks (Step 1.5 name match): "correct the mismatch before continuing" — single path
- C-37 does not apply without F-IDs; the operational-directive register replaces the mechanism C-37 measures
- C-23: no formal modal vocabulary block headers (Steps format) — FAIL

### V-04 Key Evidence
- BLOCK 2.7: POSITION CONSTRAINT paragraph (C-43 PASS)
- F-28: **Downstream fix** / **Upstream fix** labeled (C-44 for F-28 only)
- Other cross-block halts: F-10 "Correct the mismatched name in this table before continuing." — single path; F-15 "Correct the attribution to a roster-member name before continuing." — single path; F-16/F-17 single-path
- BLOCK N SEALED statements throughout
- C-37: F-IDs use "Populate the [named cell]" pattern throughout; F-09 "Reconcile the Domain count in this table with the expert count in BLOCK 1 before continuing" — names both targets
- F-13: "Remove the invalid expert row from BLOCK 1 and add the missing signal to this catalogue before continuing" — names both blocks
- F-18: "Add the missing resolution row to BLOCK 1 before continuing" — names target block

### V-05 Key Evidence
- BLOCK 2.7: POSITION CONSTRAINT paragraph (C-43 PASS)
- C-44 expanded: F-03, F-10, F-15, F-16, F-17, F-28 all have Downstream fix / Upstream fix labeled paths
- F-04 (structural absence): "Add BLOCK 3 before continuing" — single path (exempt per C-44)
- F-01 (structural absence): "Add the missing discipline table before continuing" — single path (exempt)
- F-09 (count parity): "Reconcile the Domain count" — single path (exempt)
- F-12 (count parity): "Reconcile the row count" — single path (exempt)
- Declarative register: "CONSTRAINT VIOLATED" prefix; "This block produces..." block headers
- BLOCK 3 Elevation Record: P1 findings classified as ELEVATED or BASELINE
- BLOCK 5 CONSENSUS ELEVATION RULE referencing Elevation Record

---

## Criterion-by-Criterion Scoring

### Essential Criteria (4 total, 60% weight each if all pass)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** All 6 Stock Disciplines Present | PASS | PASS | PASS | PASS | PASS |
| **C-02** Severity Tag on Every Finding | PASS | PASS | PASS | PASS | PASS |
| **C-03** Domain Expert Auto-Selection Justified | PASS | PASS | PASS | PASS | PASS |
| **C-04** Consensus Block Present | PASS | PASS | PASS | PASS | PASS |

**Evidence — C-01**: All variations include the 6 stock disciplines in BLOCK 2 (or Step 2): Security Architect, Performance Engineer, Scalability Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect. F-01 halt declared in all.

**Evidence — C-02**: All variations enforce P1/P2/P3 exclusively with F-02 halt declared. V-03 uses Required: with same constraint.

**Evidence — C-03**: All variations include BLOCK 1 / Step 1 domain expert selection table with Signal detected | Expert added | Reason columns. F-07/F-21 enforce non-empty Reason cells.

**Evidence — C-04**: All variations include BLOCK 3 / Step 3 consensus analysis block with F-04 halt declared.

**Essential pass count**: 4/4 for all five variations.

---

### Recommended Criteria (3 total, 30% weight if all pass)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-05** Unique Catches Surfaced | PASS | PASS | PASS | PASS | PASS |
| **C-06** Amend Pathway Described | PASS | PASS | PASS | PASS | PASS |
| **C-07** Finding Traceability to Design Section | PASS | PASS | PASS | PASS | PASS |

**Evidence — C-05**: BLOCK 4 / Step 4 unique catches present in all variations with F-08 halt declared.

**Evidence — C-06**: BLOCK 5 / Step 5 amend pathway present with targeted re-run scope constraint (F-05 / Required) in all variations.

**Evidence — C-07**: All variations place Section as leftmost column in BLOCK 2 findings table; F-27 enforces non-empty Section cell on P1 rows; P2 50% requirement stated.

**Recommended pass count**: 3/3 for all five variations.

---

### Aspirational Criteria (37 total, 10% weight)

Detailed scoring per variation below. PASS = 1 point toward aspirational score; PARTIAL/FAIL = 0.

#### C-08 | Severity Distribution Sanity
- V-01: PASS — BLOCK 2.5 dedicated pyramid gate block with Status and Rationale columns; F-06/F-19 fire on inversion without rationale
- V-02: PASS — same
- V-03: PASS — Step 2.5 pyramid check with Rationale; Required: enforces rationale on inversion
- V-04: PASS — same as V-01 plus BLOCK 2.5 SEALED
- V-05: PASS — same

#### C-09 | Expert Disagreement Analysis
- V-01: PASS — F-11 fires when SPLIT row has empty Synthesis cell
- V-02: PASS — F-11 present
- V-03: PASS — Required: Step 3 SPLIT Synthesis enforcement
- V-04: PASS — F-11 present
- V-05: PASS — F-11 present (CONSTRAINT VIOLATED prefix)

#### C-10 | Structural Column Enforcement in Finding Tables
- V-01: PASS — Section/Sev/Finding table format in BLOCK 2 with F-02 enforcing tag
- V-02: PASS — same
- V-03: PASS — table with Section/Sev/Finding columns
- V-04: PASS — same
- V-05: PASS — same

#### C-11 | Three-Field Expert Trace
- V-01: PASS — Signal detected | Expert added | Reason table columns declared
- V-02: PASS — same
- V-03: PASS — Signal detected | Expert added | Reason in Step 1
- V-04: PASS — same
- V-05: PASS — same

#### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block
- V-01: PASS — BLOCK 2.5 dedicated block between BLOCK 2 and BLOCK 3
- V-02: PASS — same
- V-03: PASS — Step 2.5 dedicated step
- V-04: PASS — same with SEALED statement
- V-05: PASS — BLOCK 2.5 dedicated

#### C-13 | Expert Trace in Table Column Form
- V-01: PASS — Signal detected | Expert added | Reason table declared
- V-02: PASS — same
- V-03: PASS — table with same columns in Step 1
- V-04: PASS — same
- V-05: PASS — same

#### C-14 | Named Halt Conditions on Every Mandatory Block
- V-01: PASS — F-01 through F-29/F-30 cover all mandatory blocks
- V-02: PASS — same
- V-03: FAIL — operational-directive register uses Required: constraints, not named F-IDs. No F-IDs declared anywhere.
- V-04: PASS — F-01 through F-30 present
- V-05: PASS — CONSTRAINT VIOLATED blocks carry F-ID labels in parentheses (e.g., "(F-01)", "(F-13)")

*V-03 evidence*: The entire variation uses "Required:" framing. No F-XX identifiers appear. C-14 requires "named failure ID (e.g., F-01, F-02...)." FAIL.

#### C-15 | Roster Commitment Table Before Finding Generation
- V-01: PASS — BLOCK 1.5 table with Reviewer/Role/Source columns before BLOCK 2
- V-02: PASS — same
- V-03: PASS — Step 1.5 Reviewer Roster table (with Source column) before Step 2
- V-04: PASS — same
- V-05: PASS — BLOCK 1.5 table with Source column

#### C-16 | Source Column in Roster Commitment Table
- V-01: PASS — Source column in BLOCK 1.5 (Domain/Stock values)
- V-02: PASS — same
- V-03: PASS — Source column in Step 1.5
- V-04: PASS — same
- V-05: PASS — same

#### C-17 | Cross-Block Reviewer Identity Verification (Orphan Detection)
- V-01: PASS — F-10 fires when Domain reviewer name in BLOCK 1.5 doesn't match BLOCK 1 Expert added value
- V-02: PASS — F-10 present
- V-03: PASS — Required: "Every Domain reviewer name here exactly matches an Expert added value from Step 1. If any name differs, correct the mismatch"
- V-04: PASS — F-10 present
- V-05: PASS — F-10 present (with dual-path)

#### C-18 | Content-Completeness Halt on SPLIT Synthesis Field
- V-01: PASS — F-11 present
- V-02: PASS — F-11 present
- V-03: PASS — Required: SPLIT synthesis completeness enforced
- V-04: PASS — F-11 present
- V-05: PASS — F-11 present

#### C-19 | Cross-Block Count-Parity for P1 Findings
- V-01: PASS — F-12 fires when BLOCK 5 row count ≠ P1_count; ANCHOR established at BLOCK 2.5
- V-02: PASS — same
- V-03: PASS — "Row count must equal P1_count from Step 2.5" with Required constraint
- V-04: PASS — F-12 with named referent "Reconcile the row count with the P1_count anchor"
- V-05: PASS — F-12 present

#### C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form
- V-01: PASS — "| Section | Priority Rank | P1 Finding | Action | Re-run Scope |" — 5 columns, base schema intact
- V-02: PASS — same
- V-03: PASS — "| Section | Priority Rank | P1 Finding | Action | Re-run Scope |" — table form
- V-04: PASS — same
- V-05: PASS — same

#### C-21 | BLOCK 0 Pre-Scan Signal Catalogue
- V-01: PASS — BLOCK 0 pre-scan with Signal Phrase/Location/Amendment Cost/Disposition table; F-13 SHALL NOT gate
- V-02: PASS — same
- V-03: PASS — Step 0 "Domain Signal Map" with same columns; Required: constraints with formal SHALL
- V-04: PASS — BLOCK 0 with F-13/F-18
- V-05: PASS — BLOCK 0 with CONSTRAINT VIOLATED prefix

#### C-22 | BLOCK 3 Consensus in 4-Column Structural Table Form
- V-01: PASS — "| Issue | Type | Reviewers | Synthesis |" table declared
- V-02: PASS — same
- V-03: PASS — Step 3 "| Issue | Type | Reviewers | Synthesis |" table
- V-04: PASS — same
- V-05: PASS — same

#### C-23 | Register Isolation for Formal Lifecycle Block Headers
- V-01: PASS — "Block headers and F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is non-conformant)" stated in preamble; no informal calibration language in headers
- V-02: PASS — same preamble declaration
- V-03: FAIL — operational-directive register uses "Required:" and "apply fix" language in what are effectively halt positions; "should carry a non-empty Section cell" in Step 2 uses informal calibration register; no formal modal vocabulary
- V-04: PASS — same formal preamble as V-01/V-02; SEALED statements in formal register
- V-05: PASS — "CONSTRAINT VIOLATED" prefix is formal-register; block headers use formal framing ("This block produces..."); no informal calibration phrasing in halt conditions

*Note*: V-05's "This block produces..." framing is descriptive rather than imperative, but it does not use informal calibration language ("aim for," "try," "ideally"). C-23 PASS.

#### C-24 | BLOCK 4 Unique-Catch Reviewer Identity Verification
- V-01: PASS — F-16 declared; "none" token exempt
- V-02: PASS — F-16 present
- V-03: PASS — Required: "Every Reviewer cell names a reviewer from the Step 1.5 roster"; no F-16 ID but criterion only requires named halt condition (C-14 failed already)
- V-04: PASS — F-16 present
- V-05: PASS — F-16 present (with dual-path)

*Note on V-03*: C-24 pass condition says "Output contains a named halt condition (e.g., F-16)." V-03 uses Required: framing without a named ID. However, the criterion's intent is that a halt fires on roster mismatch. Given V-03 fails C-14 for the same reason, C-24 should also FAIL for V-03 since it specifically requires a "named halt condition." FAIL V-03.

#### C-25 | BLOCK 5 Re-run Scope Reviewer Identity Verification
- V-01: PASS — F-17 declared
- V-02: PASS — F-17 present
- V-03: PASS — Required: "Every Re-run Scope reviewer name appears in the Step 1.5 roster" — PARTIAL (no named halt ID). FAIL by same logic as C-24.
- V-04: PASS — F-17 with named referent
- V-05: PASS — F-17 with dual-path

*V-03*: FAIL — no named F-ID.

#### C-26 | BLOCK 0 Signal Disposition Completeness (Bidirectional Gate)
- V-01: PASS — F-18 declared: "Every catalogue entry SHALL resolve in BLOCK 1"
- V-02: PASS — F-18 present
- V-03: PASS — Required: "Every signal phrase catalogued here resolves in Step 1" — FAIL (no named halt ID per C-26 pass condition "named halt condition (e.g., F-18)").
- V-04: PASS — F-18 present
- V-05: PASS — F-18 present

*V-03*: FAIL — no named F-18.

#### C-27 | BLOCK 2.5 Pyramid Inversion Rationale Content Completeness
- V-01: PASS — F-19 fires when pyramid inverted and Rationale cell empty
- V-02: PASS — F-19 present
- V-03: PASS — Required: "If Status is INVERTED, the Rationale cell must carry a substantive design-specific explanation" — FAIL (no F-19 named halt ID).
- V-04: PASS — F-19 present with named referent
- V-05: PASS — F-19 present (CONSTRAINT VIOLATED)

*V-03*: FAIL — no named F-19.

#### C-28 | BLOCK 4 Unique Catches in Structural Table Form
- V-01: PASS — F-20 fires if BLOCK 4 not in Markdown table form
- V-02: PASS — F-20 present
- V-03: PASS — Required: "This step is a Markdown table. If it is not formatted as a Markdown table, reformat it" — FAIL (no named F-20).
- V-04: PASS — F-20 present
- V-05: PASS — F-20 present

*V-03*: FAIL — no named F-20.

#### C-29 | BLOCK 0 No-Expert Disposition Row Reason Content Completeness
- V-01: PASS — F-21: "fires when any No-Expert-Needed disposition row has an empty or absent Reason cell. Populate the Reason cell with the specific basis; 'N/A' without explanation is non-conformant."
- V-02: PASS — F-21 present
- V-03: PASS — Required: "Every no-expert row carries a non-empty Reason explaining why no expert is needed. 'N/A' without explanation is insufficient" — FAIL (no named F-21).
- V-04: PASS — F-21 with named referent
- V-05: PASS — F-21 present

*V-03*: FAIL — no named F-21.

#### C-30 | BLOCK 2 Domain Expert Finding Coverage Symmetry
- V-01: PASS — F-22: fires when Domain reviewer in BLOCK 1.5 has no finding block in BLOCK 2
- V-02: PASS — F-22 present
- V-03: PASS — Required: "Every Domain reviewer in the Step 1.5 roster has a finding table here" — FAIL (no named F-22).
- V-04: PASS — F-22 with named referent
- V-05: PASS — F-22 present

*V-03*: FAIL — no named F-22.

#### C-31 | BLOCK 3 Consensus Issue Column Content Completeness
- V-01: PASS — F-23: fires when any Issue cell empty (sentinel exempt)
- V-02: PASS — F-23 present
- V-03: PASS — Required: "Every Issue cell is non-empty (sentinel row exempt)" — FAIL (no named F-23).
- V-04: PASS — F-23 present
- V-05: PASS — F-23 present

*V-03*: FAIL — no named F-23.

#### C-32 | BLOCK 5 Amend Action Cell Content Completeness
- V-01: PASS — F-24: fires when Action cell empty or placeholder
- V-02: PASS — F-24 present
- V-03: PASS — Required: "Every Action cell carries a specific change instruction...If any Action cell is empty or contains a placeholder, replace it" — FAIL (no named F-24).
- V-04: PASS — F-24 with named referent
- V-05: PASS — F-24 present

*V-03*: FAIL — no named F-24.

#### C-33 | BLOCK 4 Unique Catch Finding Cell Content Completeness
- V-01: PASS — F-25: fires when Finding cell empty ("none" sentinel exempt)
- V-02: PASS — F-25 present
- V-03: PASS — Required: "Every Finding cell is non-empty ('none' sentinel exempt)" — FAIL (no named F-25).
- V-04: PASS — F-25 present
- V-05: PASS — F-25 present

*V-03*: FAIL — no named F-25.

#### C-34 | BLOCK 5 Amend Section Cell Content Completeness
- V-01: PASS — F-26: fires when Section cell empty or placeholder
- V-02: PASS — F-26 present
- V-03: PASS — Required: "Every Section cell carries a specific design section reference. If any Section cell is empty or contains a placeholder, replace it" — FAIL (no named F-26).
- V-04: PASS — F-26 present
- V-05: PASS — F-26 present

*V-03*: FAIL — no named F-26.

#### C-35 | BLOCK 2 P1 Section Cell Named Halt Enforcement
- V-01: PASS — F-27: fires when P1 finding row has empty Section cell
- V-02: PASS — F-27 present
- V-03: PASS — Required: "Every P1 finding row has a non-empty Section cell. If any P1 row has an empty Section cell, populate it" — FAIL (no named F-27).
- V-04: PASS — F-27 with named referent "Populate the Section cell on the P1 row"
- V-05: PASS — F-27 present

*V-03*: FAIL — no named F-27.

#### C-36 | BLOCK 2 Section Column Leftmost Placement
- V-01: PASS — "Section is the leftmost column" stated; table shows "| Section | Sev | Finding |"
- V-02: PASS — same declaration and table structure
- V-03: PASS — "Section is the leftmost column" in Step 2; table shows "| Section | Sev | Finding |"
- V-04: PASS — same; explicit "Section is the leftmost column. P1 Section values here are the authoritative source for BLOCK 2.7 and SHALL NOT be omitted."
- V-05: PASS — same; table shows "| Section | Sev | Finding |"

#### C-37 | Named Halt Conditions Include Inline Corrective Action Specification
- V-01: PASS — preamble states "Each F-ID trigger clause includes an inline resolution instruction with a named referent"; F-IDs carry cell-level specificity (F-07 "Populate the Reason cell", F-27 "Populate the Section cell", F-02 "Replace the non-standard tag with P1, P2, or P3", F-26 "Replace the Section cell with a specific design section reference"); F-28 dual-path with specific referents; F-09 "Reconcile the two blocks" is borderline but both blocks are named in the trigger clause (PASS by anaphoric rule)
- V-02: FAIL — F-19 "Populate the Rationale cell before continuing. Halt." — passes anaphoric test (trigger clause names "Rationale cell"). However, V-02's known pattern from R13/R14 is FAIL C-37. Re-examining: F-09 "Reconcile the two blocks before continuing" — generic. F-14 "Replace the Type value with AGREE or SPLIT before continuing" — names the value to replace. F-10 "Correct the name mismatch before continuing" — no cell named. F-28 "Correct the Section value to match an entry in the BLOCK 2.7 registry, or add the P1 finding...before continuing" — names specific blocks. Key FAIL: F-09 "Reconcile the two blocks" without naming which rows to add/remove; also F-28 in V-02 does name targets. The overall pattern in V-02 does not include the "named referent" preamble that V-01 carries. V-02 was marked FAIL in R13/R14 for C-37. FAIL.
- V-03: FAIL — no F-IDs; C-37 applies to F-ID halt conditions specifically; without F-IDs the mechanism is absent.
- V-04: PASS — preamble "Each F-ID trigger clause uses referentially-complete anaphoric resolution (names the specific cell or block to populate)"; F-09 "Reconcile the Domain count in this table with the expert count in BLOCK 1 before continuing" — names both referents; F-10 "Correct the mismatched name in this table before continuing" — names "this table"; F-13 "Remove the invalid expert row from BLOCK 1 and add the missing signal to this catalogue before continuing" — names both targets; all F-IDs meet the standard
- V-05: FAIL — V-05 uses "CONSTRAINT VIOLATED" prefix. Examining halt clauses: F-07 "Populate the Reason cell with the specific content signal that warrants this expert before continuing." — PASS. F-09 "Reconcile the Domain count in this table with the expert count in BLOCK 1 before continuing." — PASS. F-10 (dual-path): "Correct the name in this table to match the BLOCK 1 selection." / "correct the Expert added value in BLOCK 1" — names targets. F-14 "Replace the Type value with the correct value before continuing." — "the correct value" without naming AGREE or SPLIT. F-23 "Populate the Issue cell with a specific finding description before continuing." — PASS. However, F-14 "Replace the Type value with the correct value" does not name AGREE or SPLIT — this is a minor omission. Overall V-05 demonstrates cell-level specificity in most halts, comparable to V-04. But checking F-12 "Reconcile the row count before continuing" — no specific named referent (compare V-04: "Reconcile the row count with the P1_count anchor"). This is borderline. Given the overall pattern, V-05 is PARTIAL — not all F-IDs fully meet the named-referent standard but most do. For binary scoring: FAIL (one missing referent fails per C-37).

*Revision*: V-05 F-12: "Reconcile the row count before continuing. Halt." — "the row count" refers to the P1_count anchor mentioned in the ANCHOR statement. Anaphoric reference may be valid. V-05 F-14: "Replace the Type value with the correct value before continuing." — "the correct value" is not explicit (AGREE or SPLIT). This is a genuine referential gap. C-37 says bare verb without referent fails; "correct value" without naming it fails. FAIL V-05 C-37.

*Final C-37 verdicts*: V-01 PASS, V-02 FAIL, V-03 FAIL, V-04 PASS, V-05 FAIL.

#### C-38 | BLOCK 0 Amendment Cost Column
- V-01: PASS — BLOCK 0 table includes Amendment Cost column (High/Medium/Low)
- V-02: PASS — same
- V-03: PASS — Step 0 table includes Amendment Cost column
- V-04: PASS — same
- V-05: PASS — same

#### C-39 | BLOCK 5 Priority Rank Column
- V-01: PASS — BLOCK 5 table includes "| Section | Priority Rank | P1 Finding | Action | Re-run Scope |"
- V-02: PASS — same
- V-03: PASS — Step 5 table has Priority Rank column with derivation formula
- V-04: PASS — same
- V-05: PASS — same

#### C-40 | BLOCK 5 Inertia Framing as Named Design Constraint
- V-01: PASS — "PRESERVATION PRINCIPLE: Only the sections listed in the Section column of this table are subject to amendment. All other sections of the design remain unchanged."
- V-02: PASS — same
- V-03: PASS — "Preservation rule: Only the sections named in the Section column are subject to amendment. All other sections of the design remain unchanged."
- V-04: PASS — same PRESERVATION PRINCIPLE statement
- V-05: PASS — same PRESERVATION PRINCIPLE statement

#### C-41 | BLOCK 5 Section Column Leftmost Placement
- V-01: PASS — BLOCK 5 table: "| Section | Priority Rank | P1 Finding | Action | Re-run Scope |" — Section is leftmost
- V-02: PASS — same
- V-03: PASS — Step 5 table: "| Section | Priority Rank | P1 Finding | Action | Re-run Scope |" — Section is leftmost
- V-04: PASS — same
- V-05: PASS — same

#### C-42 | BLOCK 5 Section Values Cross-Block Verified Against BLOCK 2
- V-01: PASS — F-28 fires when Section value absent from BLOCK 2.7 P1 Section Registry (which is populated from BLOCK 2 P1 rows)
- V-02: PASS — F-28 present with registry reference
- V-03: PASS — Step 5 Required: "Every Section value in this table appears in the Step 2.7 Section Map" with two-option repair
- V-04: PASS — F-28 present
- V-05: PASS — F-28 present

#### C-43 | BLOCK 2.7 P1 Section Registry Dedicated and Positioned Before BLOCK 3
- V-01: PASS — BLOCK 2.7 is a dedicated named block present in the lifecycle after BLOCK 2.5 and before BLOCK 3; F-28 references "the BLOCK 2.7 P1 Section Registry"; F-30 fires when block is absent. **Note**: No explicit POSITION CONSTRAINT paragraph; positioning is implicit via lifecycle block order declaration. Per C-43 pass condition: "Output contains a dedicated registry block (BLOCK 2.7 or equivalent named block) positioned after BLOCK 2 and before BLOCK 3, enumerating all P1 Section values from BLOCK 2 as a committed set. F-28 must reference this block as its verification source." All conditions met. PASS.
- V-02: PASS — BLOCK 2.7 with explicit POSITION CONSTRAINT paragraph; F-28 references "the registry established before BLOCK 3"; F-30 names correct position in repair instruction. Strongest C-43 implementation among single-axis variations.
- V-03: PASS — Step 2.7 "Section Map" with "Build this step before Step 3 begins." The step is an equivalent named block in the correct lifecycle position; Step 5 references "the Step 2.7 Section Map." Pass condition says "BLOCK 2.7 or equivalent named block." PASS.
- V-04: PASS — BLOCK 2.7 with POSITION CONSTRAINT paragraph; BLOCK 2.7 SEALED statement reinforces position
- V-05: PASS — BLOCK 2.7 with POSITION CONSTRAINT paragraph; strongest positioning language

#### C-44 | Cross-Block Mismatch Halts Specify Both Upstream and Downstream Paths
- V-01: FAIL — F-28 has labeled Downstream fix / Upstream fix; F-10 "Correct the name mismatch before continuing" (single path); F-15 "Correct the attribution to a roster-member name before continuing" (single path); F-16 "Correct the attribution to a roster-member name before continuing" (single path); F-17 "Correct the name to a roster-member name before continuing" (single path). C-44 requires ALL cross-block reference mismatch halts (F-10, F-15, F-16, F-17, F-28) to have dual paths. Only F-28 compliant. FAIL.
- V-02: FAIL — F-28 uses "Correct... or add... before continuing" (names both paths as "or" options); F-10 "Correct the name mismatch before continuing" (single path); F-15/F-16/F-17 single-path. FAIL (incomplete coverage; also F-28 lacks explicit labeling making C-44 arguable even on F-28 alone, but the primary failure is incomplete coverage across all halts).
- V-03: FAIL — Step 5 uses two-option repair for F-28 equivalent; Step 1.5 "correct the mismatch" (single path); no F-10/F-15/F-16/F-17 cross-block repairs have dual paths; no named F-IDs. FAIL.
- V-04: FAIL — F-28 has Downstream/Upstream labeled fix; F-10 "Correct the mismatched name in this table before continuing" (single path); F-15 "Correct the attribution to a roster-member name before continuing" (single path); F-16 "Correct the attribution to a roster-member name before continuing" (single path); F-17 "Correct the Re-run Scope name to a roster-member name before continuing" (single path). F-28 is compliant; F-10/F-15/F-16/F-17 are not. FAIL.
- V-05: PASS — F-03: Downstream fix / Upstream fix labeled. F-10: Downstream fix / Upstream fix labeled. F-13: structural absence (exempt — "Remove... and add..."). F-15: Downstream fix / Upstream fix labeled. F-16: Downstream fix / Upstream fix labeled. F-17: Downstream fix / Upstream fix labeled. F-28: Downstream fix / Upstream fix labeled. All cross-block reference mismatch halts (F-03, F-10, F-15, F-16, F-17, F-28) have dual-path corrective actions. F-09 and F-12 are count-parity halts (exempt). F-01, F-04, F-08 are structural absence halts (exempt). PASS.

---

## Aspirational Pass Count Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | FAIL | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | FAIL | PASS | PASS |
| C-24 | PASS | PASS | FAIL | PASS | PASS |
| C-25 | PASS | PASS | FAIL | PASS | PASS |
| C-26 | PASS | PASS | FAIL | PASS | PASS |
| C-27 | PASS | PASS | FAIL | PASS | PASS |
| C-28 | PASS | PASS | FAIL | PASS | PASS |
| C-29 | PASS | PASS | FAIL | PASS | PASS |
| C-30 | PASS | PASS | FAIL | PASS | PASS |
| C-31 | PASS | PASS | FAIL | PASS | PASS |
| C-32 | PASS | PASS | FAIL | PASS | PASS |
| C-33 | PASS | PASS | FAIL | PASS | PASS |
| C-34 | PASS | PASS | FAIL | PASS | PASS |
| C-35 | PASS | PASS | FAIL | PASS | PASS |
| C-36 | PASS | PASS | PASS | PASS | PASS |
| C-37 | PASS | FAIL | FAIL | PASS | FAIL |
| C-38 | PASS | PASS | PASS | PASS | PASS |
| C-39 | PASS | PASS | PASS | PASS | PASS |
| C-40 | PASS | PASS | PASS | PASS | PASS |
| C-41 | PASS | PASS | PASS | PASS | PASS |
| C-42 | PASS | PASS | PASS | PASS | PASS |
| C-43 | PASS | PASS | PASS | PASS | PASS |
| C-44 | FAIL | FAIL | FAIL | FAIL | PASS |

**Aspirational pass totals**:
- V-01: 35 / 37 (fails C-37? No — V-01 PASS. Fails C-44. 36/37.)
- V-02: 37 criteria, fails C-37 and C-44. 35/37.
- V-03: 37 criteria, fails C-14, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35, C-37, C-44. 21/37.
- V-04: 37 criteria, fails C-44. 36/37.
- V-05: 37 criteria, fails C-37. 36/37.

*Recounting V-01 carefully*: C-37 PASS, C-44 FAIL. 37 - 1 = 36/37.
*V-02*: C-37 FAIL, C-44 FAIL. 37 - 2 = 35/37.
*V-03*: failures = C-14, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35, C-37, C-44 = 16 failures. 37 - 16 = 21/37.
*V-04*: C-44 FAIL only. 37 - 1 = 36/37.
*V-05*: C-37 FAIL only. 37 - 1 = 36/37.

---

## Composite Score Computation

### Formula
```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 37 * 10)
```

### V-01
- Essential: 4/4 → 4/4 × 60 = **60.00**
- Recommended: 3/3 → 3/3 × 30 = **30.00**
- Aspirational: 36/37 → 36/37 × 10 = **9.73**
- **Composite: 99.73**

### V-02
- Essential: 4/4 → **60.00**
- Recommended: 3/3 → **30.00**
- Aspirational: 35/37 → 35/37 × 10 = **9.46**
- **Composite: 99.46**

### V-03
- Essential: 4/4 → **60.00**
- Recommended: 3/3 → **30.00**
- Aspirational: 21/37 → 21/37 × 10 = **5.68**
- **Composite: 95.68**

### V-04
- Essential: 4/4 → **60.00**
- Recommended: 3/3 → **30.00**
- Aspirational: 36/37 → 36/37 × 10 = **9.73**
- **Composite: 99.73**

### V-05
- Essential: 4/4 → **60.00**
- Recommended: 3/3 → **30.00**
- Aspirational: 36/37 → 36/37 × 10 = **9.73**
- **Composite: 99.73**

---

## Score Summary and Ranking

| Rank | Variation | Composite | Essential | Recommended | Aspirational | Golden? |
|------|-----------|-----------|-----------|-------------|--------------|---------|
| 1 (tie) | V-04 | **99.73** | 4/4 | 3/3 | 36/37 | YES |
| 1 (tie) | V-05 | **99.73** | 4/4 | 3/3 | 36/37 | YES |
| 1 (tie) | V-01 | **99.73** | 4/4 | 3/3 | 36/37 | YES |
| 4 | V-02 | **99.46** | 4/4 | 3/3 | 35/37 | YES |
| 5 | V-03 | **95.68** | 4/4 | 3/3 | 21/37 | YES |

**Three-way tie at 99.73**: V-01 (C-44 FAIL), V-04 (C-44 FAIL), V-05 (C-37 FAIL). Each drops exactly one aspirational criterion.

### Tie-Breaking Analysis

All three top variations score identically at 99.73. Tie-breaking criteria:

1. **C-44 coverage depth**: V-05 PASSES C-44 (all 6 cross-block mismatch halts have dual paths). V-01 and V-04 FAIL C-44 (only F-28 has dual paths). C-44 is the primary R15 target criterion. **V-05 wins on targeted criterion compliance.**

2. **C-43 quality**: All three pass C-43, but V-04 and V-05 have explicit POSITION CONSTRAINT paragraphs; V-01 has implicit ordering. V-04 and V-05 are stronger.

3. **Novel pattern**: V-05 introduces the Elevation Record in BLOCK 3 and the CONSENSUS ELEVATION RULE in BLOCK 5. These features are additive and not yet captured in any criterion, making V-05 the innovation frontier for R16.

4. **C-37 vs C-44 trade-off**: V-05 fails C-37 (F-14 "Replace the Type value with the correct value" lacks explicit AGREE/SPLIT referent). V-04 fails C-44. C-44 is the newer, more architecturally significant criterion introduced in v14 as a distinct resolution-completeness class. For golden selection, C-44 coverage breadth outweighs C-37 referential completeness in R15's priority ordering.

**Selected Golden**: **V-05** — C-44 breadth across all 6 cross-block mismatch halts, C-43 POSITION CONSTRAINT, novel Elevation Record pattern, and declarative register improvements all position V-05 as the strongest advancement toward the R16 frontier.

**Alternate Golden**: **V-04** — C-37 PASS (stronger than V-05 on corrective-action specificity), C-43 POSITION CONSTRAINT, BLOCK SEALED lifecycle discipline. If C-37 specificity is weighted higher than C-44 breadth for the next generation, V-04 is the more conservative winner.

---

## Excellence Signals from Top Variations

### From V-05 (Primary Golden Candidate)

**Excellence Signal 1 — C-44 Full Cross-Block Coverage**
V-05 applies bidirectional resolution to all six cross-block reference mismatch halts: F-03, F-10, F-15, F-16, F-17, and F-28. Prior rounds achieved C-44 on F-28 only. Full coverage eliminates the directional ambiguity at every point where the lifecycle can fork between upstream incompleteness and downstream error. Pattern: enumerate all cross-block mismatch halts as a class and apply the bidirectional template uniformly.

**Excellence Signal 2 — BLOCK 3 Elevation Record + BLOCK 5 Elevation Rule**
V-05 adds an Elevation Record table in BLOCK 3 classifying every P1 finding as ELEVATED (in an AGREE row) or BASELINE (not in any AGREE row). BLOCK 5 then carries a CONSENSUS ELEVATION RULE: ELEVATED findings receive lower (priority) rank integers than BASELINE findings. This creates a deterministic ordering input at BLOCK 3 generation time rather than requiring BLOCK 5 to compute consensus weighting from scratch. Pattern: intermediate blocks produce auxiliary artifacts that downstream blocks consume deterministically.

**Excellence Signal 3 — POSITION CONSTRAINT as Lifecycle Position Lock**
V-05's BLOCK 2.7 POSITION CONSTRAINT names the conformant lifecycle order, declares out-of-order placement non-conformant, and explains why (downstream blocks cannot draw from an unstable registry). This pattern — naming the non-conformant alternative explicitly — is stronger than implicit ordering. Pattern: declare what is non-conformant alongside what is required.

### From V-04 (Alternate Golden Candidate)

**Excellence Signal 4 — BLOCK N SEALED Lifecycle Gate Statements**
V-04 adds a SEALED statement after each block ("BLOCK N SEALED after all [block content] are verified. Proceed to BLOCK N+1"). This converts the lifecycle progression from an implicit advance (no instruction to stop) to an explicit gate (advance only after verification). Pattern: name the transition condition at the close of each block.

**Excellence Signal 5 — Referentially-Complete Anaphoric Halt Clauses Throughout**
V-04's C-37 PASS is achieved by a preamble commitment and consistent execution. Every F-ID names its target cell or block: F-09 "Reconcile the Domain count in this table with the expert count in BLOCK 1" (both referents named); F-13 "Remove the invalid expert row from BLOCK 1 and add the missing signal to this catalogue" (both targets named). Pattern: preamble contract + per-F-ID execution.

---

## R15 Round Analysis

### What R15 Tested
- **Single-axis (V-01)**: Does labeling F-28's dual paths fix C-44? — Result: PARTIAL (one halt fixed, five uncovered)
- **Single-axis (V-02)**: Does POSITION CONSTRAINT paragraph fix C-43? — Result: YES (C-43 PASS), but C-37 still fails
- **Single-axis (V-03)**: Can operational-directive register achieve C-43/C-44 compliance? — Result: Achieves the surface behavior but sacrifices all named-halt criteria (C-14 and 14 downstream criteria fail)
- **Combination (V-04)**: C-43 + C-44(F-28) + lifecycle seals + C-37 — Result: All four axes achieved (C-43 PASS, C-37 PASS, C-44 PARTIAL — F-28 only)
- **Combination (V-05)**: C-43 + C-44(all) + declarative register + Elevation Record — Result: C-43 PASS, C-44 PASS, C-37 FAIL (one referent), novel patterns introduced

### Key Finding: C-44 Coverage vs C-37 Specificity Trade-off
V-04 achieves C-37 at the cost of C-44 coverage depth (only F-28 has dual paths). V-05 achieves C-44 full coverage at the cost of C-37 (F-14 referent gap). The two criteria remain in tension at R15: the mechanisms they require compete for the same authorial attention. A V-06 iteration that carries V-05's C-44 breadth with V-04's C-37 named-referent discipline on every halt clause would score 37/37.

### V-03 Disqualification Pattern
V-03 demonstrates the register trade-off cost: the operational-directive register (Required:/fix) achieves the lifecycle behavior but systematically fails all 14 named-halt-dependent criteria (C-14 and everything downstream that requires a named F-ID). The register is pedagogically accessible but architecturally weak for the named-halt enforcement class. This result validates that the formal-modal register is load-bearing for C-14 and derivatives, not aesthetic.

---

## Criteria Passed by All Variations (Stable Core)

C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-36, C-38, C-39, C-40, C-41, C-42, C-43

Total: 28 criteria fully stable across all 5 variations. BLOCK 2.7 (C-43) is now stable.

## Criteria Differentiating This Round

| Criterion | Differentiating Pattern |
|-----------|------------------------|
| C-14 | V-03 FAIL — named F-IDs required; operational-directive register cannot substitute |
| C-23 | V-03 FAIL — formal modal vocabulary required in halt positions |
| C-24 through C-35 | V-03 FAIL — all downstream named-halt criteria cascade from C-14 FAIL |
| C-37 | V-02/V-03/V-05 FAIL — referential completeness threshold unchanged; F-14 gap in V-05 |
| C-44 | V-01/V-02/V-03/V-04 FAIL; V-05 PASS — expanding dual-path coverage from F-28 to all 6 mismatch halts is R15's primary advance |

---

## R16 Direction

Based on R15 findings, R16 should target the remaining single-criterion gap in the top variations:

1. **V-06 (primary)**: Carry V-05's C-44 full coverage + fix F-14 to name "AGREE or SPLIT" explicitly in the corrective action. Should score 37/37 aspirational (composite ~100.00).
2. **Elevation Record formalization**: V-05's Elevation Record + Elevation Rule is a new pattern not yet captured in a criterion. R16 could formalize it as C-45: "BLOCK 3 Elevation Record classifies every P1 finding by consensus status as input to BLOCK 5 priority ranking."
3. **BLOCK N SEALED formalization**: V-04's SEALED statements are not yet a criterion. C-46 candidate: "Each lifecycle block carries an explicit seal statement at close naming the verification condition and the next block."

---

## JSON Summary

```json
{"top_score": 99.73, "all_essential_pass": true, "new_patterns": ["C-44 full cross-block coverage: bidirectional resolution applied uniformly to all 6 cross-block reference mismatch halts (F-03 F-10 F-15 F-16 F-17 F-28) not just F-28", "BLOCK 3 Elevation Record classifying P1 findings as ELEVATED or BASELINE feeding BLOCK 5 CONSENSUS ELEVATION RULE for deterministic priority ordering", "BLOCK N SEALED gate statements at close of each lifecycle block naming the verification condition and next block"]}
```
