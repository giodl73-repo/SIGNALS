Written to `simulations/quest/rubrics/quest-score-rubric-v9-variations-R9-2026-03-15.md`.

---

## R9 Design Notes

**New criteria targeted:** C-24 (C-22 diagnostic three-scale enumeration) and C-25 (standalone three-scale enumeration principle in design notes). N_aspirational: 16 → 18. Criterion roster: 23 → 25 rows.

**Evidence ladders:**
- C-24: V-03/V-05 = FAIL, V-02 = PARTIAL, V-01/V-04 = PASS
- C-25: V-05 = FAIL, V-04 = PARTIAL, V-01/V-02/V-03 = PASS

---

## Variation Map

| Variation | Axis | C-24 | C-25 | Type |
|-----------|------|------|------|------|
| V-01 | R9 full-stack baseline | PASS | PASS | Baseline |
| V-02 | C-24 PARTIAL ablation | PARTIAL | PASS | Single-axis |
| V-03 | C-24 FAIL ablation | FAIL | PASS | Single-axis |
| V-04 | C-25 PARTIAL ablation | PASS | PARTIAL | Single-axis |
| V-05 | C-24 FAIL + C-25 FAIL floor | FAIL | FAIL | Combination |

---

## Structural Diff from R8 V-01 (all variations)

Every R9 variation carries these universal updates from the R8 baseline:
- **N_aspirational**: 16 → 18 in formula and score distribution note
- **Roster row count**: 23 → 25 (C-24 and C-25 rows added)
- **C-01 diagnostic**: "exactly 25 rows" (was 23)
- **C-03 diagnostic**: "N_aspirational=18" (was 16)
- **C-12 diagnostic**: "N_aspirational=18 (v9 values)" (was 16)
- **C-14 diagnostic**: "C-01 through C-25" (was C-23)
- **C-17 diagnostic**: 25-row check and N_aspirational=18 check updated
- **Phase 2**: "25-row scoring table" / "C-08--C-25" in composite block
- **Score distribution**: "10/18 = 0.556 pt" (was 0.625)

## Per-Variation Structural Signature (axis-controlled properties only)

**V-01 only:** SETUP Step 1.2 is a named "Three-Scale Enumeration Principle" standalone block. C-22 roster row enumerates all three verdict cases (FAIL/PARTIAL/PASS) with structural contrasting examples.

**V-02:** C-25 standalone principle block intact. C-22 roster row enumerates only two cases (FAIL + PARTIAL; PASS omitted).

**V-03:** C-25 standalone principle block intact. C-22 roster row describes only the FAIL case; PARTIAL/PASS absent.

**V-04:** No standalone principle block in SETUP. The three-scale enumeration rule is mentioned only inside the C-24 roster row's diagnostic question text. C-22 roster row enumerates all three cases (full C-24 pass maintained).

**V-05:** No standalone principle block. C-22 roster row is a binary probe: "Does the rule name both required location and SETUP exclusion?" — no verdict-case enumeration.
