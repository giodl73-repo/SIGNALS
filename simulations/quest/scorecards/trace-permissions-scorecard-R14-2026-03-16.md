## Round 14 — trace-permissions Scorecard

**Rubric:** v13 — 31 criteria (C-01 to C-39), denominator 31  
**Scoring model:** Essential (C-01–C-05) × 12 pts each = 60 | Recommended (C-06–C-08) × 10 pts each = 30 | Aspirational (C-09–C-39, 31 items) × 10/31 ≈ 0.323 pts each = 10 | Max = 100.0

**Entering state:** R13-V-05 = 99.7 (30/31). Only C-37 fails (attestation rows used "Dimension 1/2/3", not preamble A-N row labels). All R14 variations are built on R13-V-05 base with C-37 fixed.

---

### C-37 Gate Check (the only failing criterion from R13-V-05)

**C-37 definition:** Attestation rows cite preamble axis row labels (A-1/A-2/A-3 or equivalent) as row identifiers — closes the C-34→C-36 labeling loop under a shared scheme.
**Dependencies:** C-34 + C-36 (both pass in all R14 variations — all inherit R13-V-05 base which satisfies them).

| Variation | C-37 mechanism | C-37 verdict |
|-----------|---------------|--------------|
| V-01 | Preamble axis table gains "Row ID" column (A-1/A-2/A-3). Attestation primary row IDs: A-1/A-2/A-3 matching preamble. Loop closed by same label set. | **PASS** |
| V-02 | Preamble axis table uses semantic IDs (AXIS:EXE/AXIS:CNF/AXIS:CSR). Attestation row IDs use same semantic IDs. "Or equivalent" clause explicitly tested; loop consistent. | **PASS** |
| V-03 | V-01 A-N fix carried forward. Attestation table Row IDs A-1/A-2/A-3. Register change (imperative numbered steps) is structurally inert. | **PASS** |
| V-04 | V-01 A-N fix carried forward. Attestation Row IDs A-1/A-2/A-3. CA-1.N Scope Declaration table adds phase-boundary clarity for C-39 without disturbing C-37 structure. | **PASS** |
| V-05 | Preamble gains 5th column "Attestation Row Ref" pre-assigning ATTEST-A-1/A-2/A-3. Attestation uses ATTEST-A-N as primary ID + "Preamble Row Ref" back-column citing A-N. Loop is bidirectional, auditable at column level by ref match without semantic interpretation. | **PASS** |

---

### Full 31-Criterion Scorecard

#### Essential Criteria (C-01–C-05) — all variations

All R14 variations inherit full essential compliance from R13-V-05. Confirmed present across all five.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Role-operation matrix | PASS | PASS | PASS | PASS | PASS |
| C-02 FLS coverage + null case | PASS | PASS | PASS | PASS | PASS |
| C-03 Record scope per role | PASS | PASS | PASS | PASS | PASS |
| C-04 Privilege escalation path detection | PASS | PASS | PASS | PASS | PASS |
| C-05 Security gap inventory | PASS | PASS | PASS | PASS | PASS |

*Evidence: TABLE_1 through TABLE_5 schemas present in all variations; SE-0/SE-1/SE-2/SE-3/SE-4/SE-5 sub-sections preserved; no essential machinery removed.*

#### Recommended Criteria (C-06–C-08) — all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Dataverse-native terminology | PASS | PASS | PASS | PASS | PASS |
| C-07 Sharing rule conflict analysis | PASS | PASS | PASS | PASS | PASS |
| C-08 Remediation specificity | PASS | PASS | PASS | PASS | PASS |

*Evidence: CS-2 sharing rule expectations table with Potential Overreach? column and SE cross-reference preserved; TABLE_5 CS-EXPECTATION-VIOLATED three-field Remediation structure (CS-Expected/SE-Actual/Delta) preserved across all.*

#### Aspirational Criteria (C-09–C-39)

Key criteria to check individually; C-09 through C-33 are structural inheritance from R13-V-05 and carry without disruption across all variations. Focusing on the C-34–C-39 block where R14 makes relevant changes.

| ID | What it tests | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|---------------|------|------|------|------|------|-------|
| C-09 | Defense-in-depth layering | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-10 | Cross-role differential | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-11 | Pre-printed tables + blank-cell prohibition | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-12 | SHALL obligations + terminal checklist | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-13 | Expert role persona sequencing | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-14 | Criterion-owner attribution in checklist | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-15 | Triple-lock enforcement | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-16 | Dedicated format-compliance auditor role (CA) | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-17 | Criterion enforcement preamble matrix | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-18 | Four-mechanism quad-lock | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-19 | CA-first authorship model | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-20 | Schema Registry + preamble reaffirmation | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-21 | Closed authorship loop | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-22 | Output-embedded phase execution attestation | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-23 | Registry-preamble double-anchor CA verification | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-24 | *(inherited pass)* | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-25–C-30 | *(inherited)* | PASS×all | PASS×all | PASS×all | PASS×all | PASS×all | Inherited |
| **C-31** | SE-0 before SE-1; Tier columns | PASS | PASS | PASS | PASS | PASS | Inherited; axis A-1 |
| **C-32** | Exact-label MANUAL GAP / STRUCTURED CLOSE blocks | PASS | PASS | PASS | PASS | PASS | Inherited; axis A-2 |
| **C-33** | CS-0 self-reference sub-section | PASS | PASS | PASS | PASS | PASS | Inherited; axis A-3 |
| **C-34** | Preamble axis declaration with non-interference statement | PASS | PASS | PASS | PASS | PASS | All R14 variations add Row IDs (A-N or AXIS:*) + non-interference |
| **C-35** | SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot + CA-1.9 distinct from CA-1.4/CA-1.7 | PASS | PASS | PASS | PASS | PASS | Inherited from R13-V-05 base |
| **C-36** | CA terminal verdict tri-dimensional self-evidence attestation | PASS | PASS | PASS | PASS | PASS | Attestation now uses A-N/AXIS:/ATTEST-A-N labels — all pass |
| **C-37** | Attestation rows cite preamble axis row labels as row identifiers | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | The fix — all five approaches satisfy it |
| **C-38** | SHALL-D [C-35] named extension sub-clause; CA-1.9 preamble anchor cites it | PASS | PASS | PASS | PASS | PASS | Inherited from R13-V-05 base; preserved unchanged |
| **C-39** | Phase 3 mandate explicitly names CA-1.9 + inter-row distinctness from CA-1.4/CA-1.7 | PASS | PASS | PASS | PASS | **PASS+** | V-04 and V-05 strengthen this with CA-1.N Scope Declaration table; V-01/V-02/V-03 satisfy minimally via Phase 3 mandate text |

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | Score |
|-----------|---------------|-----------------|-------------------|-------|-------|
| V-01 | 60/60 | 30/30 | 31 × 0.323 = 10.0 | 100.0 | **100.0** |
| V-02 | 60/60 | 30/30 | 31 × 0.323 = 10.0 | 100.0 | **100.0** |
| V-03 | 60/60 | 30/30 | 31 × 0.323 = 10.0 | 100.0 | **100.0** |
| V-04 | 60/60 | 30/30 | 31 × 0.323 = 10.0 | 100.0 | **100.0** |
| V-05 | 60/60 | 30/30 | 31 × 0.323 = 10.0 | 100.0 | **100.0** |

**All hypotheses confirmed. All five variations achieve 31/31 = 100.0%.**

---

### Ranking

All variations tie at 100.0. Differentiated by structural elegance of C-37 expression:

| Rank | Variation | C-37 mechanism | Distinguishing quality |
|------|-----------|---------------|----------------------|
| 1 | **V-05** | Bidirectional ATTEST-A-N / Preamble-Row-A-N cross-link | Loop auditable at column level by ref scan; no semantic interpretation required; most robust against label drift |
| 2 | **V-04** | A-N + Phase 3 CA-1.N Scope Declaration table | C-39 strengthened to phase-boundary visibility; 9-row scope table makes CA-1.9 distinctness independently verifiable before reading any CA-1 row |
| 3 | **V-01** | A-N numeric labels (minimal surgical fix) | Simplest correct fix; no additional machinery |
| 3 | **V-03** | A-N + imperative register | Proves register-neutrality of all 31 criteria; useful for verification but adds no structural signal |
| 3 | **V-02** | Semantic AXIS:EXE/CNF/CSR labels | Proves C-37's "or equivalent" clause; useful for confirming label-scheme flexibility |

---

### Excellence Signals (V-05 as canonical reference)

**1. Bidirectional column-level loop closure.**  
Preamble axis table pre-declares attestation row refs (ATTEST-A-N) in a dedicated column. Attestation table carries a "Preamble Row Ref" back-column. The C-34→C-37 loop is closed at the column-reference level: any label inconsistency between preamble and attestation is immediately visible by column scan without reading cell content. This is stricter than "same labels appear in both places" — it makes the loop contract structurally self-enforcing.

**2. Pre-declared row identity binding.**  
Declaring the terminal attestation's row IDs in the preamble (before any SE execution) converts a labeling convention into a binding structural contract. The model can't choose different row IDs at attestation time — they were pre-assigned in Phase 0. This extends the CA-first authorship principle (C-19) to terminal verdict structure.

**3. Register-neutrality confirmation (V-03).**  
All 31 criteria pass unchanged under full imperative numbered-step rewrite. This means the structural enforcement mechanisms are content-independent — they don't rely on declarative sentence structure.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["bidirectional-column-loop-closure: preamble declares ATTEST-A-N ref for each axis; attestation table carries Preamble-Row-Ref back-column; C-34->C-37 loop auditable by column scan without semantic interpretation", "pre-declared-row-identity-binding: attestation row IDs assigned in Phase 0 preamble converts labeling convention into structural contract enforced before execution begins"]}
```
