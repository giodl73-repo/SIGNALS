Written to `simulations/quest/rubrics/topic-report-rubric-v9-variations-R9-2026-03-15.md`.

---

## Round 9 Variations -- `topic-report`

**Rubric**: v9 (C-01 through C-30, aspirational_pass/22 * 10)
**Base**: R8 neutral base (19/22 under v9 -- fails C-28, C-29, C-30)

### Variation Axes

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| A: dual-identifier violation | `(no stall cost -- G-9 INERTIA / C-21 violation)` | YES | YES | NO | YES | NO |
| B: recovery directive in Branch B header | explicit re-read instruction in Branch B THREE-LAYER | YES | NO | YES | YES | NO |
| C: slot-indexed contract register | `G-9 INERTIA [SLOT 4]`, `G-7a COMPLETENESS [SLOT 3]`, etc. | NO | YES | YES | YES | NO |

### R9 Rationale

R8 single-axis variations (V-01 A, V-02 B, V-03 C) tied at 20/22 because C-28, C-29, C-30 are mutually orthogonal -- no v9 criterion differentiates them. R9 tests the **pairwise combinations** as the live discriminators:

- **V-01 (A+B)**: Closes output-to-invariant recovery (Axis A) + Branch B generation-flow recovery (Axis B). Two failure modes: wrong output vs. branch-entry attention loss.
- **V-02 (A+C)**: Closes output-to-invariant recovery (Axis A) + register-to-slot forward navigation (Axis C). Backward recovery after bad output + forward planning before writing.
- **V-03 (B+C)**: Closes Branch B layer-sequence recovery (Axis B) + register forward navigation (Axis C). Both early-arc; lacks the violation-text dual-identifier -- key asymmetry for surfacing C-31.
- **V-04 (A+B+C)**: Ceiling, re-verifies R8 V-05 score is stable.
- **V-05 (neutral)**: Control baseline at 19/22.

### Predicted scores

| Variation | v9 asp | v9 score | Gap |
|-----------|--------|---------|-----|
| V-01 A+B | 21/22 | 99.5 | -C-30 |
| V-02 A+C | 21/22 | 99.5 | -C-29 |
| V-03 B+C | 21/22 | 99.5 | -C-28 |
| V-04 A+B+C | 22/22 | 100.0 | -- |
| V-05 neutral | 19/22 | 95.5 | -3 |

If predictions hold, all three pairwise combinations tie at 99.5 -- same as R8 V-04 (A+B). The only rubric-level discriminator left is **V-04 vs. V-01/V-02/V-03** (ceiling vs. one-short). Live-run asymmetries between V-01, V-02, and V-03 despite identical scores would surface a candidate C-31. V-03 is the one to watch: it lacks the dual-identifier, so any elevated SLOT 4 inertia error rate points to C-28 as the primary NEXT STEP recovery mechanism.
