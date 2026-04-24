Done. Here's the complete updated rubric:

---

```markdown
---
skill: validate-consistency
rubric_version: v2
date: 2026-03-20
total_points: 115
changes_from_v1: Added C-11, C-12, C-13 from R1 excellence signals; aspirational weight raised
  from 10 to 25; scoring thresholds updated proportionally.
---

# validate-consistency — Rubric v2

**5 essential** criteria cover the non-negotiables: registry populated, 3A check executed,
inconsistency register with severity, P1 correctly identified (not downgraded), and frontmatter
fields match actuals.

**3 recommended** push for all four check types (3A-3D), ordered/actionable amendments, and
algebraic reasoning on any 3B failure.

**5 aspirational** reward showing explicit substitution steps in 3C, registering single-location
quantities as unverifiable, structural anti-downgrade enforcement, frontmatter counts bound to a
named phase event, and a completeness gate between Phase 2 and Phase 3.

---

## Essential Criteria (weight: 60 pts total — 12 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | Phase 2 registry is populated and multi-location quantities are flagged | coverage | A registry table exists listing every quantity found in the artifact; each entry records how many locations it appears in, and any quantity found in more than one location is explicitly flagged for cross-checking |
| C-02 | Value consistency check (3A) is executed | correctness | Phase 3A table is present; every quantity flagged in Phase 2 as multi-location appears as a row with Location A / Value A / Location B / Value B and a Consistent? verdict |
| C-03 | Inconsistency register is present with severity labels | correctness | Phase 4 table exists with I-ID, type, description, and P1/P2/P3 severity for every FAIL verdict found in Phase 3; if no inconsistencies are found the table is present but explicitly states "none found" |
| C-04 | P1 issues are correctly identified and marked as reject conditions | correctness | Any value conflict where the same quantity takes different numerical values in different locations, or two equations that provably disagree, is labeled P1; no P1-class conflict is downgraded to P2 or P3 |
| C-05 | Artifact frontmatter contains all required fields | format | Frontmatter block includes skill, topic, date, p1_count, p2_count, and quantities_checked with non-empty values; p1_count and p2_count match the actual count of P1/P2 entries in the inconsistency register |

---

## Recommended Criteria (weight: 30 pts total — 10 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | All four check types (3A-3D) are executed | coverage | Sections 3A, 3B, 3C, and 3D are all present; each has either a populated table or an explicit "none applicable" statement |
| C-07 | Phase 5 amendments are ordered by severity and are actionable | depth | Phase 5 lists at least one fix per severity level, ordered P1 -> P2 -> P3; each fix names the specific location and correct value |
| C-08 | Equation consistency (3B) shows algebraic reasoning for any FAIL | depth | For any 3B FAIL row, the "what diverges" column contains a concrete algebraic or symbolic step |

---

## Aspirational Criteria (weight: 25 pts total — 5 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Boundary / limit checks (3C) include explicit evaluation steps | depth | For every 3C row, the output shows the substitution made so a reader can independently verify the verdict |
| C-10 | Single-location quantities are registered and noted as unverifiable | coverage | Phase 2 registry includes single-location quantities annotated as "single-location — cannot cross-check" |
| C-11 | P1 severity is structurally enforced, not just stated | correctness | The output contains a mechanism beyond a rule — a named adversarial role, challenge-and-rebuttal block, or inertia warning — that forces any P1 downgrade to be documented and rebutted, not silently absorbed |
| C-12 | Frontmatter counts are bound to a named phase event, not carried forward | format | An explicit count step derives p1_count, p2_count, and quantities_checked from a specific named phase completion; estimates or early-filled values left stale are a fail |
| C-13 | A completeness gate is present between Phase 2 and Phase 3 | coverage | Before Phase 3 begins, the output includes an explicit gate confirming Phase 2 is complete — listing total quantities, MULTI count, and SINGLE count |

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 115 | All criteria pass |
| 92-114 | Golden — all essential pass, strong recommended/aspirational coverage |
| 69-91 | Passing — all essential pass, weak recommended coverage |
| < 69 | Failing — one or more essential criteria miss |

---

## Common Failure Modes

- **C-01 miss**: Registry exists but multi-location quantities are not flagged, so Phase 3 cross-checks are incomplete.
- **C-04 miss**: A clear numerical conflict is labeled P2 instead of P1, understating rejection risk.
- **C-05 miss**: Frontmatter p1_count is 0 but the register shows P1 entries — field is stale.
- **C-06 miss**: Section 3D (sign/direction) is omitted when the paper uses directional language.
- **C-08 miss**: 3B FAIL row says "equations differ" without showing the algebraic step.
- **C-11 miss**: Skill output states "P1 — no exceptions" as a rule but provides no structural mechanism; a model run can still quietly relabel.
- **C-12 miss**: quantities_checked is filled early and never updated after Phase 4 DA review changes the P1/P2 count.
- **C-13 miss**: Phase 3 begins immediately with no summary gate; a partial Phase 2 sweep silently omits quantities found later.
```

---

**What changed in v2:**

| New criterion | Source evidence | What it rewards |
|---|---|---|
| C-11 | V-01 Skeptic mandate; V-05 DA + inertia warning | Structural mechanism that forces P1 challenges to be documented, not just a rule that says "don't downgrade" |
| C-12 | V-01 "count after Phase 4"; V-02 Phase 2E binding; V-03 dedicated count step; V-05 post-DA counts | Counts explicitly derived from a named phase event, preventing stale carry-forward |
| C-13 | V-02 Phase 2E completeness gate | Explicit gate before Phase 3 — Phase 3 cannot silently run on a partial Phase 2 |

Total points: 100 → 115. Scoring thresholds updated proportionally (80% golden = 92, 60% passing = 69).
l quietly relabel without triggering any documented challenge.
- **C-12 miss**: quantities_checked is filled early and never updated after Phase 4 DA review changes the P1/P2 count; stale numbers pass C-05 if not carefully audited.
- **C-13 miss**: Phase 3 begins immediately after the last quantity is found with no summary gate; a partial Phase 2 sweep produces a Phase 3 that silently omits quantities discovered later.
