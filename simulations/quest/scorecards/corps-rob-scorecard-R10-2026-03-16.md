## corps-rob R10 Scorecard (v10 Rubric)

---

### Scoring Key

| Weight | Points |
|--------|--------|
| Essential | 15 pts each (PASS/FAIL) |
| Recommended | 5 pts each |
| Aspirational | 5 pts each |
| Max composite | 225 (5×15 + 3×5 + 27×5) |

---

### V-01 -- Carry-Forward Structural Axis

**Single axis**: RULE CARRY-FORWARD as primary mechanism. VIOLATION-12. Single IB-01. Default order.

#### Essential (75/75)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage Identity | PASS | `## Stage: [stage-name]` in every stage template |
| C-02 | Role-Loaded Perspective | PASS | ROLE: line with Frame/Lens loaded from `.roles/`; fallback by stage name |
| C-03 | ROB Document Format | PASS | Labeled findings, verdict table, TPM Risk Register + Go/No-Go, SPIRE Mission Cascade |
| C-04 | Actionable Findings (2x) | PASS | Minimum 2 findings per stage enforced; Via:+Owner+Resolution columns required |
| C-05 | Go/No-Go in TPM | PASS | Explicit Go/No-Go table with labeled Verdict/Rationale/Risk Refs |

#### Recommended (15/15)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Cross-Stage Coherence | PASS | CARRY FORWARD blocks guarantee ≥5 cross-stage refs in 6-stage run; Escalates:/Inherits: also required |
| C-07 | Structured Risk Register | PASS | Table: ≥3 rows, title/severity/likelihood/mitigation, ≥1 HIGH, ≥2 Status values |
| C-08 | Exec-Office Cascade | PASS | SPIRE Mission Cascade table; named mission required |

#### Aspirational (120/135)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Inter-Stage Blocker Detection | PASS | BLOCKER PROTOCOL required; min 1 per full run; upstream stage + LID + downstream impact |
| C-10 | Cross-Cutting Theme Elevation | PASS | Document-level `## Cross-Cutting Theme:` format; VIOLATION-08 if only within one stage |
| C-11 | Conditional Verdict Itemization | PASS | RULE CONDITIONAL-ITEM: numbered (1)/(2)/(3) items with what/owner/LID |
| C-12 | Finding Severity Discrimination | PASS | "severity must vary" instruction; HIGH and MED in example row |
| C-13 | Risk Register Status Lifecycle | PASS | Status column: OPEN/WATCH/MITIGATED; ≥2 distinct values required |
| C-14 | Pre-Finding Severity Calibration | PASS | Calibration Block: HIGH DRIVER/LOW ANCHOR/DISTRIBUTION FACTOR before findings |
| C-15 | Risk Register Update Protocol | PASS | Update Protocol table: Trigger Events/Owner Role/Revisit Cadence |
| C-16 | Role-Lens Pre-Declaration | PASS | ROLE LENS: field in Calibration Block; topic-specific required |
| C-17 | Pre-Commitment Enforcement Audit | PASS | POST-STAGE AUDIT SUITE with CALIBRATION AUDIT covering Calibration Block compliance |
| C-18 | Universal Per-Stage Triage Note | PASS | Calibration Block with three named fields mandated in every stage template |
| C-19 | Zero-Deviation Explicit Declaration | PASS | "VIOLATIONS: [named or NONE]"; CARRY FORWARD GAPS: [or NONE]; zero-state required |
| C-20 | Enforcement Audit Structured Table | PASS | CALIBRATION AUDIT: Stage/HIGH DRIVER/LOW ANCHOR/DISTRIBUTION FACTOR/Honored/Deviation (6 cols) |
| C-21 | Named Triage Field Vocabulary | PASS | HIGH DRIVER:/LOW ANCHOR:/DISTRIBUTION FACTOR: as labeled fields in every stage |
| C-22 | Post-Stage Role-Concern Gap Scan | PASS | ROLE CONCERN AUDIT section in POST-STAGE AUDIT SUITE |
| C-23 | Post-Stage Triage Note Gap Scan | PASS | TRIAGE NOTE AUDIT section in POST-STAGE AUDIT SUITE |
| C-24 | Multi-Type Post-Stage Audit Suite | PASS | Four distinct sections: CALIBRATION + ROLE CONCERN + TRIAGE NOTE + CARRY FORWARD AUDIT |
| C-25 | Triage Note Field-Level Audit | PASS | TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c) failure conditions |
| C-26 | Named Audit Rule + Anti-Patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 (merged) and ANTI-PATTERN-2 (same dimension ×3) |
| C-27 | Gap-Scan Absence = Format Error | PASS | `[ROLE CONCERN GAPS: absence = FORMAT VIOLATION -- RULE BOOKEND-AUDIT]` in section headers |
| C-28 | Named Field-Level Audit Schema | PASS | TRIAGE NOTE AUDIT SCHEMA: with labeled (a)/(b)/(c) conditions |
| C-29 | Enumerated Condition Zero-State | PASS | AUDIT RESULT: (a) NONE / (b) NONE / (c) NONE in TRIAGE NOTE AUDIT |
| C-30 | Run-Level Preamble Schema | **FAIL** | No RUN-LEVEL RULE GLOSSARY; TRIAGE NOTE AUDIT SCHEMA declared inline in post-stage section |
| C-31 | Rule Citations in Section Headers | PASS | `[RULE AUDIT-SUITE, Section 1]`; `[RULE BOOKEND-AUDIT]` in ROLE CONCERN + TRIAGE NOTE headers |
| C-32 | Carry-Forward Structural Artifact | PASS | Per-stage `### Carry Forward` block in stage template; CARRY: NONE zero-state; VIOLATION-12 |
| C-33 | Synthesis Non-Audit Declaration | PASS | RULE SYNTHESIS declared with "NOT an audit section; does NOT count toward RULE AUDIT-SUITE; VIOLATION-13" |
| C-34 | Conditional Item vs Enum Disambiguation | **FAIL** | RULE CONDITIONAL-ITEM lacks `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]` annotation |
| C-35 | Audit Table Additive-Not-Replacement | **FAIL** | No RULE AUDIT-TABLE declared; no additive constraint |

**V-01 Total: 210/225** | All essentials: PASS | Fails: C-30, C-34, C-35

---

### V-02 -- Named Rule Glossary Preamble

**Single axis**: RUN-LEVEL RULE GLOSSARY before any stage output. All rules front-loaded; post-stage sections cite by name. Single IB-01. Default order.

#### Essential (75/75) -- all PASS (same structural coverage as V-01)

#### Recommended (15/15) -- all PASS

#### Aspirational (120/135)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 through C-29 | PASS | All standard structural elements present; RULE SYNTHESIS in glossary with VIOLATION-13 |
| C-30 | PASS | RUN-LEVEL RULE GLOSSARY declares RULE CONDITION-ENUM before stages; TRIAGE NOTE AUDIT cites `[preamble declaration applies -- RULE CONDITION-ENUM for AUDIT RESULT]` |
| C-31 | PASS | Section headers: `[RULE AUDIT-SUITE Section 1 -- RULE CONDITION-ENUM applies]`; `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` |
| C-32 | **FAIL** | RULE CARRY-FORWARD declared in glossary (VIOLATION-12 listed) but no `### Carry Forward` block in stage template; rule declared, not implemented |
| C-33 | PASS | RULE SYNTHESIS in glossary: "NOT an audit section; does NOT count toward RULE AUDIT-SUITE"; VIOLATION-13 |
| C-34 | **FAIL** | RULE CONDITIONAL-ITEM in glossary lacks disambiguation annotation |
| C-35 | **FAIL** | No RULE AUDIT-TABLE declared |

**V-02 Total: 210/225** | All essentials: PASS | Fails: C-32, C-34, C-35

---

### V-03 -- Synthesis Affirmative Identity

**Single axis**: RULE SYNTHESIS as positive artifact with 5 required subsections. Dual IB-01+IB-02 baselines. Default order.

#### Essential (75/75) -- all PASS

#### Recommended (15/15) -- all PASS

#### Aspirational (115/135)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | BLOCKERS is a required SYNTHESIS subsection; zero-state mandatory; VIOLATION-13 for absent subsection |
| C-10 | PASS | CROSS-CUTTING THEMES SUMMARY is a required SYNTHESIS subsection with document-level elevation |
| C-11 through C-29 | PASS | All standard elements present; RULE AUDIT-SUITE with ANTI-PATTERN-1/2; TRIAGE NOTE AUDIT SCHEMA (a)/(b)/(c) |
| C-30 | **FAIL** | No RUN-LEVEL RULE GLOSSARY preamble; no pre-stage schema declaration |
| C-31 | PASS | Audit section headers cite `[RULE AUDIT-SUITE, Section N]`; `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` |
| C-32 | **FAIL** | No per-stage CARRY FORWARD blocks in stage template; RULE CARRY-FORWARD not declared |
| C-33 | PASS | Strongest C-33 signal: RULE SYNTHESIS AFFIRMATIVE IDENTITY DECLARATION with five required subsections; absence = SYNTHESIS FORMAT ERROR; VIOLATION-13 |
| C-34 | **FAIL** | No disambiguation annotation on RULE CONDITIONAL-ITEM (no glossary entry to annotate) |
| C-35 | **FAIL** | No RULE AUDIT-TABLE declared |

Note: V-03 gains C-33 more richly than any other single-axis variation -- the affirmative identity contract (five required subsections, SYNTHESIS FORMAT ERROR for absent subsection) produces stronger C-09/C-10 enforcement than the negation declaration in V-01/V-02.

**V-03 Total: 205/225** | All essentials: PASS | Fails: C-30, C-32, C-34, C-35

---

### V-04 -- Carry-Forward + Rule Glossary (Combination)

**Axes**: V-01 (carry blocks) + V-02 (rule glossary) + C-34 disambiguation annotation in glossary. Single IB-01. Default order.

#### Essential (75/75) -- all PASS

#### Recommended (15/15) -- all PASS

#### Aspirational (130/135)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 through C-29 | PASS | Full structural coverage from combined V-01+V-02 base |
| C-30 | PASS | RUN-LEVEL RULE GLOSSARY present; `### TRIAGE NOTE AUDIT` cites `[preamble declaration applies]`; RULE CONDITION-ENUM in preamble |
| C-31 | PASS | Verdict header: `[RULE CONDITIONAL-ITEM applies -- governs conditional verdicts; see glossary: distinct from RULE CONDITION-ENUM]`; audit headers cite multiple rules |
| C-32 | PASS | `### Carry Forward [RULE CARRY-FORWARD applies]` in stage template; CARRY: NONE zero-state; VIOLATION-12 in glossary |
| C-33 | PASS | RULE SYNTHESIS in glossary: "NOT an audit section; does NOT count toward RULE AUDIT-SUITE"; VIOLATION-13 |
| C-34 | PASS | RULE CONDITIONAL-ITEM in glossary annotated: `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]`; reciprocal annotation on RULE CONDITION-ENUM; Anti-pattern-2 names the conflation pattern |
| C-35 | **FAIL** | No RULE AUDIT-TABLE declared; no additive-not-replacement constraint |

**V-04 Total: 220/225** | All essentials: PASS | Fails: C-35 only

---

### V-05 -- Full R10 Stack

**Axes**: Dual IB-01+IB-02 + risk-lead order + glossary + carry blocks + RULE SYNTHESIS affirmative + C-34 annotation + RULE AUDIT-TABLE additive constraint. Four C-24 enforcement loops. VIOLATION-01 through VIOLATION-14.

#### Essential (75/75) -- all PASS

#### Recommended (15/15) -- all PASS

#### Aspirational (135/135)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | BLOCKER PROTOCOL + required BLOCKERS subsection in SYNTHESIS; VIOLATION-13 for absent subsection |
| C-10 | PASS | Required CROSS-CUTTING THEMES SUMMARY subsection; VIOLATION-08 if single-stage |
| C-11 | PASS | RULE CONDITIONAL-ITEM in glossary with (1)/(2)/(3) requirement; verdict hint: "Do NOT use (a)/(b)/(c) format" |
| C-12 | PASS | "severity must vary"; HIGH/MED example rows; DISTRIBUTION FACTOR required |
| C-13 | PASS | Risk register Status: OPEN/WATCH/MITIGATED; ≥2 distinct values |
| C-14 | PASS | Calibration Block in every stage with HIGH DRIVER/LOW ANCHOR/DISTRIBUTION FACTOR |
| C-15 | PASS | Risk Register Update Protocol table with Trigger Events/Owner Role/Revisit Cadence |
| C-16 | PASS | ROLE LENS: topic-specific field in every stage Calibration Block |
| C-17 | PASS | POST-STAGE AUDIT SUITE: three audit sections covering distinct pre-commitment dimensions |
| C-18 | PASS | Calibration Block mandated in every stage template; all three fields required |
| C-19 | PASS | VIOLATIONS: NONE / ROLE CONCERN GAPS: NONE / TRIAGE NOTE GAPS: NONE / CARRY FORWARD GAPS: NONE |
| C-20 | PASS | Stage-per-row tables in all three audit sections with ≥4 named columns each |
| C-21 | PASS | HIGH DRIVER:/LOW ANCHOR:/DISTRIBUTION FACTOR: labeled fields in every Calibration Block |
| C-22 | PASS | ROLE CONCERN AUDIT section; `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` |
| C-23 | PASS | TRIAGE NOTE AUDIT section; `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` |
| C-24 | PASS | Four distinct sections: CALIBRATION + ROLE CONCERN + TRIAGE NOTE + CARRY FORWARD AUDIT |
| C-25 | PASS | TRIAGE NOTE AUDIT SCHEMA with (a) absent / (b) missing field / (c) placeholder; per-stage table |
| C-26 | PASS | RULE AUDIT-SUITE in glossary with Anti-pattern-1 (merged) and Anti-pattern-2 (same dimension ×3) |
| C-27 | PASS | `[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]` in both mandatory section headers |
| C-28 | PASS | TRIAGE NOTE AUDIT SCHEMA: labeled (a)/(b)/(c) in post-stage section with preamble reference |
| C-29 | PASS | AUDIT RESULT block: (a) NONE / (b) NONE / (c) NONE preserved beneath table per RULE AUDIT-TABLE |
| C-30 | PASS | Full RUN-LEVEL RULE GLOSSARY; TRIAGE NOTE AUDIT cites `[preamble declaration -- RULE CONDITION-ENUM applies to AUDIT RESULT]` |
| C-31 | PASS | CALIBRATION AUDIT: `[RULE AUDIT-SUITE Section 1 -- RULE CONDITION-ENUM applies]` + `[RULE AUDIT-TABLE applies: table above AUDIT RESULT block; additive -- VIOLATION-14 if table replaces]`; verdict header cites RULE CONDITIONAL-ITEM with disambiguation |
| C-32 | PASS | `### Carry Forward [RULE CARRY-FORWARD applies]` in every stage; CARRY: NONE for first stage (tpm); VIOLATION-12 with consequence paragraph naming C-32 as fourth C-24 loop |
| C-33 | PASS | RULE SYNTHESIS in glossary + SYNTHESIS section header: "NOT an audit section; does NOT count toward RULE AUDIT-SUITE's three required sections; VIOLATION-13 if used as substitute or any subsection absent" |
| C-34 | PASS | RULE CONDITIONAL-ITEM: `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]`; RULE CONDITION-ENUM: `[governs audit schema result blocks -- distinct from RULE CONDITIONAL-ITEM]`; both declared in glossary before first stage |
| C-35 | PASS | RULE AUDIT-TABLE in glossary: "inserted ABOVE the AUDIT RESULT block -- additive, not replacement"; AUDIT RESULT preserved beneath in all three audit sections; VIOLATION-14 with consequence paragraph naming C-35 pattern |

**V-05 Total: 225/225** | All essentials: PASS | Fails: none

---

### Ranking Summary

| Rank | Variation | Score | Delta from Max | Fails |
|------|-----------|-------|----------------|-------|
| 1 | V-05 | **225/225** | 0 | — |
| 2 | V-04 | **220/225** | -5 | C-35 |
| 3 | V-01 | **210/225** | -15 | C-30, C-34, C-35 |
| 3 | V-02 | **210/225** | -15 | C-32, C-34, C-35 |
| 5 | V-03 | **205/225** | -20 | C-30, C-32, C-34, C-35 |

All variations: all-essential PASS. All variations: above golden threshold (80).

---

### Excellence Signals from V-05

**1. Glossary-first rule architecture eliminates inline re-declaration**
All named rules declared in RUN-LEVEL RULE GLOSSARY before any stage runs. Post-stage sections cite by name (`[RULE AUDIT-SUITE applies -- see glossary]`, `[RULE CONDITION-ENUM applies]`). Enables C-30/C-31 as structural consequences rather than per-section effort. Reduces inconsistency risk when rules evolve.

**2. Disambiguation at rule-declaration time (C-34 pattern)**
RULE CONDITIONAL-ITEM annotated `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]` in the glossary. A generator processing the glossary encounters the distinction before writing any verdict block or audit result. V-04 demonstrates this is achievable without the full V-05 stack -- it is a single glossary annotation.

**3. RULE AUDIT-TABLE additive-not-replacement constraint (C-35 pattern)**
Explicitly declares the stage-per-row table as "inserted ABOVE the AUDIT RESULT block -- additive, not replacement." The AUDIT RESULT block with per-condition (a)/(b)/(c) enumeration is preserved beneath. VIOLATION-14 makes a table-induced C-29 void structurally detectable. This protects two criteria (C-29 + C-35) with one named rule.

**4. Four-loop enforcement architecture**
Each structural element (IB-01, IB-02, FINDING LEDGER, CARRY FORWARD) has: a named rule in the glossary, a VIOLATION-NN entry, a consequence paragraph naming the criterion source, and an explicit C-24 enforcement loop declaration. Pattern: `RULE X --> VIOLATION-N --> "names [criterion] as criterion-specific structural element -- creating [Nth] C-24 enforcement loop"`. Every new structural requirement can follow this template.

**5. Carry blocks as structural coherence guarantee**
Per-stage CARRY FORWARD blocks guarantee ≥5 cross-stage references in a 6-stage run as a mechanical consequence of the stage template. C-06 is satisfied by structure, not prose discipline. CARRY: NONE zero-state makes zero-carry stages affirmatively declared rather than silent. Pairs with VIOLATION-12 to make C-32 self-policing.

---

### New Patterns (not established in prior rounds)

- **RULE AUDIT-TABLE additive constraint**: named rule explicitly protecting enumerated zero-states from table-layer replacement; extends the consequence-paragraph pattern to post-stage structural integrity
- **Violation series extended to VIOLATION-14 with criterion-source annotations**: each new VIOLATION-NN includes "names [element] as the criterion-specific structural element (from C-NN)" -- making the violation taxonomy a machine-readable map from violation to rubric criterion

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["RULE AUDIT-TABLE additive-not-replacement constraint protects enumerated zero-states (C-35) by declaring enforcement tables as insertions above AUDIT RESULT blocks, not replacements for them", "Violation taxonomy extended to VIOLATION-14 with consequence paragraphs naming criterion source -- pattern: each structural rule paired with VIOLATION-NN that explicitly identifies the criterion it makes self-policing"]}
```
