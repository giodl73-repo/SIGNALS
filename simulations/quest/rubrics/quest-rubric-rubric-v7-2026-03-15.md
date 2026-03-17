Written to `simulations/quest/golden/quest-rubric-variate-v7-R07-2026-03-16.md`.

---

## quest-rubric Rubric v7

**Date:** 2026-03-16  
**Version:** 7 (C-01 through C-22; essential C-01–C-05, recommended C-06–C-08, aspirational C-09–C-22)  
**Formula:** `composite = (E/5 × 60) + (R/3 × 30) + (A/14 × 10)`  
**Denominator change:** /12 → /14

---

### What changed from v6 → v7

**C-21 — Phase-completion status token at every role boundary** (E-1, R6)

Designated explicitly in the R6 roadmap: "Absorb AUTHOR: OPEN / BLOCKED declarative format as E-1 for Round 7 rubric update (C-21)." V-03 and V-05 demonstrate the full pattern: every role transition requires the model to emit a named machine-readable status token (SPEC ANALYST: OPEN/CLOSED, AUTHOR: OPEN/BLOCKED/CLOSED, AUDITOR: OPEN/CLOSED).

Distinct from C-20: C-20 tests whether the Author Entry Gate uses imperative language naming specific artifacts. C-21 tests whether machine-readable tokens appear at **all** role boundaries — SA close, Author open, Author close, Auditor open — so the protocol is auditable by string scan without content analysis. V-01 fails C-21 (has AUTHOR ACCESS: GRANTED/DENIED at entry only; no SA close or Author close tokens). V-03 and V-05 pass.

**C-22 — FINAL RUBRIC reproduction carries explicit citation-retention guard** (E-2, R6)

From V-02's three-enforcement-checkpoint pattern and V-04/V-05 combination evidence. The FINAL RUBRIC reproduction section must include an explicit "retain CM-NN citation — do not simplify during reproduction" instruction (or equivalent).

Distinct from C-19: C-19 tests the output (does the CM-NN identifier appear in the canonical row?). C-22 tests the reproduction guard (does the FINAL RUBRIC section explicitly block stripping?). V-01 fails C-22 — its FINAL RUBRIC section has no retention instruction, only the A2d per-criterion rule. V-02 and V-04/V-05 pass.

---

### Essential Criteria

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-01 | **Skill identity declared** | Rubric names the target skill in the header |
| C-02 | **Criteria are testable** | Every criterion evaluable pass/fail/partial without subjective interpretation |
| C-03 | **Pass condition enforced** | Each criterion uses pass language ("must", "required"); advisory language fails |
| C-04 | **Scoring formula explicit** | Formula states the exact computation including denominator |
| C-05 | **Tier structure present** | Essential / Recommended / Aspirational tiers present |

### Recommended Criteria

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-06 | **Failure modes cataloged** | Known failure modes of target skill listed |
| C-07 | **Specificity test included** | At least one criterion tests output is specific to input, with concrete definition of "specific" for this skill |
| C-08 | **Version and date stamped** | Version number and date present |

### Aspirational Criteria (C-09 through C-22)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-09 | **Coverage of all output sections** | At least one criterion per named output section |
| C-10 | **Partial credit in formula** | Formula distinguishes PARTIAL from PASS; no binary collapse |
| C-11 | **External enforcement gate** | Named review role, rejection step, or prohibition checklist — not advisory language |
| C-12 | **Failure modes before criteria** | Failure mode catalog appears before the criteria it informs |
| C-13 | **Foil pair present** | At least one criterion has concrete PASS example and concrete FAIL example |
| C-14 | **Closed category enumeration** | At least one dimension uses a closed named-category enumeration; "e.g." fails |
| C-15 | **Specificity prohibitions converted** | Every specificity element is a testable output property; mechanism present |
| C-16 | **Fields have structural home** | All required fields declared in an explicit output schema block |
| C-17 | **SCHEMA BLOCK positionally first** | Output schema declaration is the first section, before failure modes and criteria |
| C-18 | **CONVERSION-MAP boolean gate** | Specificity conversion uses boolean classification table with DO-NOT-PROCEED completion gate |
| C-19 | **Identifier citation in canonical row** | CM-NN identifier appears in the CRITERION table row's Pass Condition field for each specificity criterion |
| C-20 | **Author Entry Gate structural block** | Gate uses imperative blocking phrasing AND names specific artifact identifiers (not phase labels) |
| **C-21** | **Phase-completion status token at every boundary** | Machine-readable status tokens present at all four role boundaries: SA close, Author open, Author close, Auditor open; checklists do not pass |
| **C-22** | **FINAL RUBRIC citation-retention guard** | FINAL RUBRIC section contains explicit instruction to retain CM-NN identifiers verbatim during reproduction; A2d-only or STRUCTURAL VERIFICATION-only fails |

---

### New failure modes

**FM-07 — Checklist-advisory phase boundaries**: Transitions governed by checkboxes rather than status tokens. A false CLEAR is not detectable by string scan. Caught by C-21.

**FM-08 — Citation stripping at reproduction**: CM-NN identifiers present during drafting but stripped in the FINAL RUBRIC reproduction step. A2d instructions protect the authoring phase only; the reproduction step needs its own guard. Caught by C-22.

---

### Baseline: R6 V-05 under v7 → 99.29 / Golden

C-10 remains the only failing criterion (universal gap). Both C-21 and C-22 are satisfied by R6 V-05's full PHASE STATUS protocol and FINAL RUBRIC retention instruction respectively.
