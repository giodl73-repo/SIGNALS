# Quest Score — topic-retro / Round 7

**Rubric version**: v5 (116 pts total)
**Scoring date**: 2026-03-17
**Variations scored**: V-01 through V-05

---

## Scoring Framework

| Tier | Criteria | Pts each | Subtotal |
|------|----------|----------|----------|
| Essential | C-01 to C-05 | 12 | 60 |
| Recommended | C-06 to C-08 | 10 | 30 |
| Aspirational (baseline) | C-09, C-11–C-14, C-17–C-19 | 2 | 16 |
| Aspirational (targeted) | C-10, C-15, C-16, C-20, C-21 | 2 | 10 |
| **Total available** | | | **116** |

PARTIAL = 1 pt (half). FAIL = 0 pt.

---

## V-01 — Single Axis: C-20 (Gap assumption column)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 Signal Accuracy section | PASS | Structure unaffected by assumption column addition |
| C-02 Verdict per signal | PASS | Verdict labels not disrupted |
| C-03 Gaps section actionable | PASS | Gaps section maintained; assumption column augments it |
| C-04 Echo present | PASS | Not disrupted |
| C-05 Topic/commitment context | PASS | Not disrupted |
| C-06 Signal coverage summary | PASS | Inherits from template |
| C-07 Improvement tied to gaps | PASS | Recommendation mechanism intact |
| C-08 Accuracy rate stated | PASS | Numerical summary present |
| C-10 AMEND per-table | PARTIAL | Not targeted; template partial compliance only |
| C-15 (prior round criterion) | PARTIAL | Not addressed |
| C-16 9-row namespace table | PARTIAL | Not targeted; row order unspecified |
| C-20 gap-inertia-assumption-named | **PASS** | Explicit Phase 7 assumption column; SEAL checks "We assumed X" vs "Would have surfaced Y" — two structurally distinct statements |
| C-21 phase-seal-explicit | FAIL | Not targeted |

**Score: 60 + 30 + 16 + 1 + 1 + 1 + 2 + 0 = 111 / 116**

---

## V-02 — Single Axis: C-10 (AMEND per-table)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 to C-05 | PASS × 5 | Essential structure unaffected |
| C-06 to C-08 | PASS × 3 | Recommended structure unaffected |
| C-10 AMEND per-table | **PASS** | `{{#if amend}}` scope marker above every table; OOS secondary table in Phase 2 — clean scoping |
| C-15 | PARTIAL | Not addressed |
| C-16 | PARTIAL | Row order unspecified |
| C-20 gap-inertia-assumption-named | FAIL | No assumption column; gap table unchanged |
| C-21 phase-seal-explicit | FAIL | Not targeted |

**Score: 60 + 30 + 16 + 2 + 1 + 1 + 0 + 0 = 110 / 116**

---

## V-03 — Single Axis: C-16 (9-row namespace table)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 to C-05 | PASS × 5 | Essential structure unaffected |
| C-06 to C-08 | PASS × 3 | Recommended structure unaffected |
| C-10 | PARTIAL | AMEND markers not targeted |
| C-15 | PARTIAL | Not addressed |
| C-16 9-row namespace table | **PASS** | Fixed scout→topic row order; COVERED/EMPTY vocabulary only; TOTAL row present — unambiguous format |
| C-20 gap-inertia-assumption-named | FAIL | No assumption column |
| C-21 phase-seal-explicit | FAIL | Not targeted |

**Score: 60 + 30 + 16 + 1 + 1 + 2 + 0 + 0 = 110 / 116**

---

## V-04 — Combined: C-20 + C-10

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 to C-05 | PASS × 5 | Essential structure intact across combined axes |
| C-06 to C-08 | PASS × 3 | Full recommended compliance |
| C-10 AMEND per-table | **PASS** | Per-table markers present |
| C-15 | PARTIAL | Not explicitly targeted |
| C-16 | PARTIAL | Namespace row order not locked |
| C-20 gap-inertia-assumption-named | **PASS** | Assumption column present; belief vs outcome distinction maintained alongside AMEND markers |
| C-21 phase-seal-explicit | PARTIAL | Combined design suggests some seal-like gating but format strings per field not confirmed explicit |

**Score: 60 + 30 + 16 + 2 + 1 + 1 + 2 + 1 = 113 / 116**

---

## V-05 — Full Integration: C-20 + C-10 + C-15 + C-16 + C-21

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 to C-05 | PASS × 5 | All essential maintained |
| C-06 to C-08 | PASS × 3 | All recommended maintained |
| C-10 AMEND per-table | **PASS** | Scope markers active; OOS secondary table in Phase 2 |
| C-15 | **PASS** | Explicitly targeted in combined set |
| C-16 9-row namespace table | **PASS** | Fixed row order; COVERED/EMPTY; TOTAL row |
| C-20 gap-inertia-assumption-named | **PASS** | Assumption column; SEAL distinguishes inertia belief from missed discovery |
| C-21 phase-seal-explicit | **PASS** | Per-phase seals with exact format strings per field — not just field names, but precise format anchors per required value |

**Score: 60 + 30 + 16 + 2 + 2 + 2 + 2 + 2 = 116 / 116**

---

## Rankings

| Rank | Variation | Score | % |
|------|-----------|-------|---|
| 1 | V-05 | 116 | 100% |
| 2 | V-04 | 113 | 97% |
| 3 | V-01 | 111 | 96% |
| 4 | V-02 | 110 | 95% |
| 4 | V-03 | 110 | 95% |

---

## Excellence Signals from V-05

**Pattern 1 — phase-seal-format-string-per-field**
V-05's C-21 implementation goes beyond naming required fields — it supplies exact format strings per field in the SEAL. C-21 as written only requires field names and explicit confirmation. V-05 shows that format-string anchoring prevents the "named but loosely implemented" failure mode where a compliant label appears but the value structure is wrong. This is a structural guarantee C-21 does not yet demand.

**Pattern 2 — composite-axis-zero-regression**
V-04 tested C-20+C-10 and confirmed zero interference between the assumption column and AMEND markers. V-05 extends to five axes without regression on any passing criterion. The zero-interference property across combined axes is a design quality not currently captured as a scored criterion — it is tested implicitly when each targeted criterion is scored, but not verified explicitly as a property of the full composite.

---

## All-Essential Pass Check

Every variation (V-01 through V-05) passes all five essential criteria. The assumption column (C-20), AMEND markers (C-10), namespace table ordering (C-16), phase seals (C-21), and C-15 are all non-essential axes — they do not affect the fundamental retrospective structure required by C-01 through C-05.

**All essential pass: TRUE**

---

```json
{"top_score": 116, "all_essential_pass": true, "new_patterns": ["phase-seal-format-string-per-field", "composite-axis-zero-regression"]}
```
