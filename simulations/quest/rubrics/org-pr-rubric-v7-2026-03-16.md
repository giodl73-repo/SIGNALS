Looking at the R6 excellence signals carefully:

- **Signal 1** (C-23 complexity-independent) and **Signal 2** (C-25 labeling-independent) confirm existing criteria — no new criterion.
- **Signal 3** (embedded resolution is minimal 100/100 path) → new criterion about explicit governance scope declaration (the explicit phrase that makes embedding's axis count visible).
- **Signal 4** (3-axis table is sufficient, 8-axis over-engineered) → new criterion about priority axis non-redundancy.

Two new criteria: **C-26** and **C-27**. Retroactive R6 scores under v7: V-05 remains 100.00 (C-26 PASS + C-27 N/A); V-04 drops to 99.41 (C-26 FAIL, C-27 PASS).

---

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 7
supersedes: org-pr-rubric-v6-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v6 -> v7)

Two new aspirational criteria extracted from R6 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=15 to N=17.

**C-26** (governance scope declaration): V-05 opens with "This prompt operates under two
governance axes." V-01 through V-04 all omit this declaration. Without an explicit axis
count, reviewers must infer governance scope from structure — a gap that allows axis count
to be disputed when resolution conflicts arise, and that permits incremental axis addition
by reviewers who consider their domain a separate governance dimension. V-05's declaration
anchors the resolution mechanism's authority to a specific, non-negotiable count. The
signal: an explicit axis count forecloses scope expansion in the same way that
judgment-elimination (C-23) forecloses soft overrides — by naming the boundary rather
than implying it. PASS requires an explicit statement of the number of governance axes the
prompt operates under (e.g., "two governance axes," "N governance axes," or an unambiguous
named equivalent). FAIL if axis count is implicit or derivable only from table structure
without a direct declaration. N/A if only one axis is present — no declaration is needed
for single-axis prompts (counts as PASS).

**C-27** (priority axis non-redundancy): V-04 confirms that a 3-row priority table
(authority chain + inertia + conflict resolution) is sufficient for 100/100; designs with
8+ axes from earlier rounds were over-engineered. An axis is necessary if it governs a
conflict type unreachable by the resolution logic of other listed axes. An axis is
redundant if its resolution outcome is always identical to, or derivable from, the
authority chain or inertia rules alone. The signal: redundant axes do not increase
resolution determinism but increase cognitive overhead and expand the surface for reviewer
misapplication. Each additional axis is a new site where a reviewer can argue their domain
deserves special treatment; non-redundant table design closes this surface. PASS if every
axis in the priority table is structurally distinct and non-derivable from others. FAIL if
any axis is a subdivision, restatement, or logical consequence of an existing axis. N/A if
no priority table is present (counts as PASS).

---

## Scoring Formula

Composite = Essential (max 60) + Recommended (max 30) + Aspirational (max 10).

Aspirational = (PASS_equiv / N_aspirational) × 10, rounded to 2 decimal places.

PASS_equiv weights: N/A → 1.0, PASS → 1.0, PARTIAL → 0.5, FAIL → 0.

---

## Scorecard — org-pr Round 5 (evaluated against v6 rubric)

**Rubric**: v6 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 15

See org-pr-rubric-v6-2026-03-16.md for the full R5 criterion grid and composite scores.
Preserved without re-evaluation; R5 scores are not retroactively updated under v7.

---

## Scorecard — org-pr Round 6 (evaluated against v7 rubric)

**Rubric**: v7 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 17

### Essential (all variations, all PASS — 60 pts)

All 5 essential criteria pass across all 5 variations.

### Recommended

| Variation | C-09 gap | Total |
|-----------|----------|-------|
| V-01 | FAIL (no phase gate — single-axis isolation) | **24** |
| V-02–V-05 | all PASS | **30** |

### Aspirational — criterion grid

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | P | P | P | P | P |
| C-12 Named invalid forms | F | F | F | P | P |
| C-13 Inertia / if-stays | F | F | F | P | P |
| C-14 Escape closure | PT | PT | PT | P | P |
| C-15 Projection convergence | P | P | P | P | P |
| C-16 Pre-commit self-check | P | P | P | P | P |
| C-17 Authority sequence | P | P | P | P | P |
| C-18 Axis conflict rule | N/A | N/A | N/A | P | N/A |
| C-19 Verdict hardening pair | PT | PT | PT | P | P |
| C-20 Priority table | N/A | N/A | N/A | P | N/A |
| C-21 Auth-inertia reconciliation | N/A | N/A | N/A | P | P |
| C-22 Conflict resolution column | P | P | P | P | P |
| C-23 Judgment-elimination | P | F | P | P | P |
| C-24 Correction-paired catalog | N/A | N/A | N/A | P | P |
| C-25 Coupling label | F | P | P | P | P |
| **C-26** Governance scope decl. | **N/A** | **F** | **F** | **F** | **P** |
| **C-27** Priority axis non-redundancy | **N/A** | **N/A** | **N/A** | **P** | **N/A** |

**C-26 N/A rule applied to V-01**: Single-axis isolation means no multi-axis declaration
is possible or required. N/A → PASS.

**C-26 FAIL for V-02 / V-03**: Both are multi-axis designs (authority chain + inertia).
Neither declares axis count explicitly. Axis count is inferable from the conflict
resolution column's governance reference but is not stated as a bounded integer.

**C-26 FAIL for V-04**: The 3-row priority table structurally implies N=3 but no sentence
of the form "This prompt operates under N governance axes" or equivalent is present. FAIL.

**C-26 PASS for V-05**: "This prompt operates under two governance axes." Explicit integer
declaration. PASS.

**C-27 N/A for V-01 / V-02 / V-03 / V-05**: None of these variations contains a standalone
priority table (C-20 N/A for V-01/V-02/V-03; V-05 embeds resolution inside the Authority
Chain section rather than as a table row). N/A → PASS.

**C-27 PASS for V-04**: The 3-row table (authority chain, inertia, conflict resolution)
is evaluated for redundancy. Authority chain governs positional precedence. Inertia governs
trajectory-weight precedence. Conflict resolution governs which axis prevails when both
fire simultaneously. Each row governs a distinct conflict type unreachable by the other two.
No axis is derivable from another. PASS.

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 24 | 7.65 | **91.65** |
| V-02 | 60 | 30 | 7.06 | **97.06** |
| V-03 | 60 | 30 | 7.65 | **97.65** |
| V-04 | 60 | 30 | 9.41 | **99.41** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

**Score movements from v6 to v7:**
- V-01: 91.33 → 91.65 (+0.32): C-26 N/A and C-27 N/A both count as PASS, raising
  PASS_equiv without adding FAILs. Single-axis designs improve under v7.
- V-02: 97.33 → 97.06 (−0.27): C-26 FAIL adds a zero-weight entry to the denominator.
  C-27 N/A recovers one unit but not enough to offset denominator growth with one FAIL.
- V-03: 98.00 → 97.65 (−0.35): Same mechanism as V-02. C-26 FAIL, C-27 N/A.
- V-04: 100.00 → 99.41 (−0.59): C-26 FAIL is the sole gap. C-27 PASS is captured.
  Highest-scoring design without embedded resolution.
- V-05: 100.00 → 100.00 (0): C-26 PASS and C-27 N/A both resolve to full weight.
  First and only 100/100 design under v7.

### Excellence Signals

1. **C-26 PASS requires embedded resolution as a structural precondition** — The only R6
   design achieving C-26 PASS (V-05) is the one with resolution embedded inside the
   Authority Chain section, keeping the axis count at two. A design declaring N=3 (V-04)
   cannot satisfy C-26 without also eliminating the standalone resolution axis. C-26 and
   embedded resolution are architecturally coupled: embedding is what makes the low-count
   declaration structurally accurate, and the declaration is what makes the axis boundary
   visible to reviewers.

2. **C-27 activates only for 3-axis designs — sub-threshold designs reach it via N/A** —
   V-04 is the only R6 variation where C-27 is an active requirement. The N/A path
   (available to all non-table designs) means C-27 is not a structural burden for minimal
   designs. Its primary function is as a quality gate on explicitly-tabled multi-axis
   prompts.

3. **V-04 falls from 100.00 to 99.41 — C-26 is the sole remaining gap** — V-04 satisfies
   all structural requirements (C-12, C-13, C-14, C-18, C-19, C-20, C-21, C-24, C-25,
   C-27) but omits the governance scope declaration. The fix is a single sentence added to
   the Authority Chain section preamble: "This prompt operates under three governance axes."

4. **V-05 remains the minimum complete form across all 7 rubric versions** — The
   embedded-resolution path (introduced in R6 V-05) satisfies C-26 PASS and C-27 N/A
   simultaneously, achieving 100/100 at N=2 axes. No design from R1 through R5 reached
   this form; no design from R6 V-01 through V-04 reached it. V-05 is the first prompt
   in the series to achieve 100/100 under both the rubric version it was scored under (v6)
   and the subsequent version (v7).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-26 (governance scope declaration) and embedded resolution are architecturally coupled: embedding keeps axis count at N=2, making the explicit low-count declaration structurally accurate; a 3-axis design cannot achieve C-26 PASS without eliminating the standalone resolution axis", "C-27 (priority axis non-redundancy) activates only for designs with explicit priority tables (C-20 PASS path); all sub-threshold and embedded-resolution designs reach C-27 via N/A — the criterion functions as a quality gate on multi-axis table designs, not a universal requirement", "V-04 drops from 100.00 to 99.41 under v7 due solely to C-26 FAIL; the fix is a single declaration sentence — the 3-axis table structure itself is correct and non-redundant (C-27 PASS)", "Single-axis designs (V-01) improve under v7 because C-26 N/A and C-27 N/A both count as full PASS weight, raising PASS_equiv without adding active failures to the denominator"]}
```
```
