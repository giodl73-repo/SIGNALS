Three new patterns at 115 vs 110:
1. **INERTIA CHECK fires at classification time** (not preamble) — refines C-11
2. **Re-sweep trigger when SINGLE=0** — refines C-13
3. **FINAL COUNT table is DA-update-aware** — refines C-12

These become C-14, C-15, C-16. Total climbs 115→130. Here is the complete v3:

```markdown
---
skill: validate-consistency
rubric_version: v3
date: 2026-03-20
total_points: 130
changes_from_v2: Added C-14, C-15, C-16 from R2 excellence signals; aspirational weight raised
  from 25 to 40; scoring thresholds updated proportionally.
---

# validate-consistency — Rubric v3

**5 essential** criteria cover the non-negotiables: registry populated, 3A check executed,
inconsistency register with severity, P1 correctly identified (not downgraded), and frontmatter
fields match actuals.

**3 recommended** push for all four check types (3A-3D), ordered/actionable amendments, and
algebraic reasoning on any 3B failure.

**8 aspirational** reward showing explicit substitution steps in 3C, registering single-location
quantities as unverifiable, structural anti-downgrade enforcement, frontmatter counts bound to a
named phase event, a completeness gate between Phase 2 and Phase 3, an inline
classification-time INERTIA CHECK, a re-sweep trigger when SINGLE=0, and a DA-update-aware
FINAL COUNT table.

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

## Aspirational Criteria (weight: 40 pts total — 5 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Boundary / limit checks (3C) include explicit evaluation steps | depth | For every 3C row, the output shows the substitution made so a reader can independently verify the verdict |
| C-10 | Single-location quantities are registered and noted as unverifiable | coverage | Phase 2 registry includes single-location quantities annotated as "single-location — cannot cross-check" |
| C-11 | P1 severity is structurally enforced, not just stated | correctness | The output contains a mechanism beyond a rule — a named adversarial role, challenge-and-rebuttal block, or inertia warning — that forces any P1 downgrade to be documented and rebutted, not silently absorbed |
| C-12 | Frontmatter counts are bound to a named phase event, not carried forward | format | An explicit count step derives p1_count, p2_count, and quantities_checked from a specific named phase completion; estimates or early-filled values left stale are a fail |
| C-13 | A completeness gate is present between Phase 2 and Phase 3 | coverage | Before Phase 3 begins, the output includes an explicit gate confirming Phase 2 is complete — listing total quantities, MULTI count, and SINGLE count |
| C-14 | INERTIA CHECK fires at classification time, not in a preamble | correctness | At the moment of severity assignment in Phase 4, the output triggers an inline INERTIA CHECK that names at least four drift patterns and requires a paper citation before any P1 downgrade; a pattern applied without paper support is explicitly disqualified at the point of application, not in a standing rule elsewhere |
| C-15 | SINGLE=0 triggers a re-sweep before Phase 3 proceeds | coverage | The Phase 2 completeness gate checks whether SINGLE=0; if the paper contains any numerical values and SINGLE=0, a re-sweep is explicitly mandated before Phase 3 begins |
| C-16 | FINAL COUNT table is re-derived after Phase 4 DA review | format | A three-row FINAL COUNT table binds p1_count, p2_count, and quantities_checked each to a named source phase; the table is updated after Phase 4B (Devil's Advocate review) so any severity changes from DA challenges are reflected before frontmatter is written |

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 130 | All criteria pass |
| 104-129 | Golden — all essential pass, strong recommended/aspirational coverage |
| 78-103 | Passing — all essential pass, weak recommended coverage |
| < 78 | Failing — one or more essential criteria miss |

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
- **C-14 miss**: INERTIA CHECK appears in a preamble or instructions block but does not fire inline at the moment of classification; a model can read the rule and still assign severity without executing the check.
- **C-15 miss**: Gate lists SINGLE count but takes no action when SINGLE=0; a paper with many numerical values in a single section passes Phase 2 with zero single-location entries and proceeds unchallenged.
- **C-16 miss**: FINAL COUNT table is written after Phase 3, then Phase 4 DA review changes a P2 to P1, but the table and frontmatter are not updated; stale counts are carried into the artifact.
```

---

**What changed in v3:**

| New criterion | Source evidence | What it rewards |
|---|---|---|
| C-14 | V-02/V-04 inline INERTIA CHECK at severity assignment | Check fires at classification time with paper-citation requirement; standing rule in preamble does not qualify |
| C-15 | V-01/V-04 re-sweep trigger when SINGLE=0 | Gate actively blocks Phase 3 if SINGLE count is implausibly zero given numerical content in paper |
| C-16 | V-05 post-DA FINAL COUNT table | Three-row table with source-phase column is re-derived after DA review; prevents stale frontmatter when Phase 4B changes severity |

Total points: 115 → 130. Thresholds updated (80% golden = 104, 60% passing = 78).
