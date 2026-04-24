Rubric written to `simulations/quest/rubrics/validate-consistency-rubric-2026-03-20.md`.

**5 essential** criteria cover the non-negotiables: registry populated, 3A check executed, inconsistency register with severity, P1 correctly identified (not downgraded), and frontmatter fields match actuals.

**3 recommended** push for all four check types (3A-3D), ordered/actionable amendments, and algebraic reasoning on any 3B failure.

**2 aspirational** reward showing explicit substitution steps in 3C and registering single-location quantities as "unverifiable" rather than silently skipping them.

The "Common Failure Modes" section documents the most likely ways a skill run misses a criterion — useful for diagnosing output quality during quest loops.
 flagged for cross-checking |
| C-02 | Value consistency check (3A) is executed | correctness | Phase 3A table is present; every quantity flagged in Phase 2 as multi-location appears as a row with Location A / Value A / Location B / Value B and a Consistent? verdict |
| C-03 | Inconsistency register is present with severity labels | correctness | Phase 4 table exists with I-ID, type, description, and P1/P2/P3 severity for every FAIL verdict found in Phase 3; if no inconsistencies are found the table is present but explicitly states "none found" |
| C-04 | P1 issues are correctly identified and marked as reject conditions | correctness | Any value conflict where the same quantity takes different numerical values in different locations, or two equations that provably disagree, is labeled P1; no P1-class conflict is downgraded to P2 or P3 |
| C-05 | Artifact frontmatter contains all required fields | format | Frontmatter block includes skill, topic, date, p1_count, p2_count, and quantities_checked with non-empty values; p1_count and p2_count match the actual count of P1/P2 entries in the inconsistency register |

---

## Recommended Criteria (weight: 30 pts total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | All four check types (3A–3D) are executed | coverage | Sections 3A, 3B, 3C, and 3D are all present in the output; each has either a populated table or an explicit "none applicable" statement — a missing section is a fail even if no issues exist |
| C-07 | Phase 5 amendments are ordered by severity and are actionable | depth | Phase 5 lists at least one fix per severity level present in the register, ordered P1 → P2 → P3; each fix names the specific location to change and the correct value or form to use, not just a general instruction |
| C-08 | Equation consistency (3B) shows algebraic reasoning for any FAIL | depth | For any row in the 3B table marked FAIL, the "what diverges" column contains a concrete algebraic or symbolic step showing why the two forms disagree — not just "they differ" |

---

## Aspirational Criteria (weight: 10 pts total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Boundary / limit checks (3C) include explicit evaluation steps | depth | For every row in the 3C table, the output shows the substitution made (e.g., "setting dR/dt=0 in Eq. 7 gives...") so a reader can independently verify the verdict without re-deriving it |
| C-10 | Single-location quantities are registered and noted as unverifiable | coverage | The Phase 2 registry includes quantities that appear only once; these are annotated as "single-location — cannot cross-check" rather than silently omitted, giving a complete picture of what was and was not verified |

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 100 | All criteria pass |
| 80–99 | Golden — all essential pass, strong recommended/aspirational coverage |
| 60–79 | Passing — all essential pass, weak recommended coverage |
| < 60 | Failing — one or more essential criteria miss |

## Common Failure Modes

- **C-01 miss**: Registry exists but multi-location quantities are not flagged, so Phase 3 cross-checks are incomplete.
- **C-04 miss**: A clear numerical conflict (e.g., MAPE 7.4% in one table vs 11.3% in the abstract) is labeled P2 instead of P1, understating rejection risk.
- **C-05 miss**: Frontmatter p1_count is 0 but the register shows P1 entries — field is stale or not updated after Phase 4.
- **C-06 miss**: Section 3D (sign/direction) is omitted entirely when the paper uses directional language ("positive feedback", "inverse relationship") that could be inconsistent.
- **C-08 miss**: 3B FAIL row says "equations differ" without showing the algebraic step — a reviewer cannot verify the finding.
