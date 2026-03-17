---
skill: quest-rubric
skill_target: corps-leaderboard
rubric_version: 13
date: 2026-03-17
derived_from: corps-leaderboard-rubric-v12-2026-03-17.md
changelog: Added C-34 (Insight Falsifiability Contract), C-35 (Cross-Role Discrepancy Check), C-36 (2D Action Matrix) from R15 excellence signals.
---

# Rubric v13 — corps-leaderboard

Reconstructed from R15 excellence signals (see `corps-leaderboard-scorecard-R15-2026-03-17.md`).

## What changed: v12 -> v13

Three new aspirational criteria extracted from R15 excellence signals. All three appeared exclusively in V-05.

**C-34 -- Insight Falsifiability Contract** (from V-05, Seed X)
C-13 tests structural form (cross-topic conclusion + concrete number + specific name); C-25 tests the novelty gate (Skeptic bar); C-34 tests a third orthogonal dimension: whether the Team Insight carries an explicit two-line falsifiability contract that names specific observable conditions under which it holds and under which it would be invalidated. Vague conditions ("holds if things continue") do not satisfy C-34 -- both lines must name a specific topic path, contributor identity, or numeric metric threshold.

**C-35 -- Cross-Role Discrepancy Check** (from V-05, Seed I)
C-33 tests logical coexistence constraints (flag + achievement impossibility rules); C-35 tests a different orthogonal dimension: whether a dedicated role or phase performs a structured empirical comparison of upstream flag assignments against downstream Health Phase evidence, producing a Discrepancy Table that catches cases where a flag was raised but Health Phase data contradicts it (e.g., `stuck-at-first` flagged but Signal Depth EARNED). Retractions from this table must flow downstream: the action-writing role must exclude both echo-retracted and discrepancy-retracted flags from `resolves:` targeting. A discrepancy check embedded in prose without a structured table output fails. A check within the same role that produced the flags fails -- the adversarial cross-check must be performed by a separate role or phase.

**C-36 -- 2D Action Matrix (Round x Tier)** (from V-05, Seeds K+V combined)
C-08 tests gap prioritization by achievement distance; C-26/C-29 test named-role structure and per-phase checklist gates. C-36 tests a fourth orthogonal dimension: whether the action output section is organized as a two-dimensional matrix where actions are indexed by BOTH temporal round (Round 1: exactly 1 signal closes the gap; Round 2: 2-3 signals; Round 3: 4+ signals or coordination required) AND severity tier (CRITICAL / WARNING / ADVANCING) within each round. An instruction that groups by round only (without tier within each round) fails. An instruction that uses tiered action labels only (without multi-round sequencing) fails. Both dimensions must be simultaneously present for a single action row to satisfy C-36.

---

### Scoring update

| Tier | Before (v12) | After (v13) |
|------|--------|-------|
| Aspirational criteria | 25 | 28 |
| Points per criterion | 0.40 | 0.357 |

Formula: `90 + (aspirational_passed / 28) * 10`

| Aspirational passed | Score |
|---------------------|-------|
| 28/28 | 100.00 |
| 27/28 | 99.64 |
| 26/28 | 99.29 |
| 25/28 | 98.93 |
| 24/28 | 98.57 |
| 22/28 | 97.86 |
| 20/28 | 97.14 |

---

## Essential Criteria (correctness baseline -- 60% of score)

*Five criteria at 12 pts each. All five must pass to reach the golden threshold.*

### C-01 -- Signal Registry Scan

*(criterion text preserved from v12)*

### C-02 -- Per-Topic Achievement Evaluation with Exact Names

*(criterion text preserved from v12)*

### C-03 -- All Three Team Milestones Present with Exact Names

*(criterion text preserved from v12)*

### C-04 -- Contributor Leaderboard Present and Ranked

*(criterion text preserved from v12)*

### C-05 -- Specific Next Actions Naming Namespace and Achievement

*(criterion text preserved from v12)*

---

## Aspirational Criteria (quality ceiling -- 40% of score)

*Twenty-eight criteria at 10/28 pts each (0.357 pts). Pass all five essential first; aspirational
points accumulate on top.*

### C-06 through C-33

*(criterion text preserved from v12 -- see corps-leaderboard-rubric-v12-2026-03-17.md)*

---

### C-34 -- Insight Falsifiability Contract

- **Weight**: aspirational | **Category**: quality
- **Text**: The Team Insight section carries an explicit two-line falsifiability contract
  appended after the insight sentence:
  `[holds if: {specific observable condition naming a topic, contributor, or metric threshold}]`
  `[falsified by: {specific observable condition that would invalidate the insight}]`
  C-13 tests the structural form of the insight (cross-topic conclusion + concrete number +
  specific name); C-25 tests the novelty gate (the insight must pass a Skeptic who has read the
  analysis); C-34 tests a third, orthogonal dimension -- whether the insight is *directly
  falsifiable* by a named future observable state. An insight that carries the correct structural
  form and passes the Skeptic novelty bar, but has no falsifiability contract, satisfies C-13 and
  C-25 but fails C-34. Vague conditions that do not name a specific entity fail -- both the
  `[holds if:]` and `[falsified by:]` lines must anchor to a specific topic path, contributor
  identity, or numeric metric threshold. Generic conditions ("holds if current trends continue",
  "falsified by unexpected changes") fail because they cannot be verified by inspection.
- **Pass condition**: The insight section contains two distinct contract lines immediately after
  the insight sentence, each beginning with `[holds if:]` or `[falsified by:]`. Both lines must
  name a specific observable entity (topic path, contributor, or measurable threshold). A single
  contract line fails. Contract lines embedded in prose rather than as bracketed annotations fail.
  Contract lines that use vague or general conditions rather than named specifics fail.
- **Derived from**: R15 excellence signal -- V-05 only. **Passes**: V-05.

---

### C-35 -- Cross-Role Discrepancy Check

- **Weight**: aspirational | **Category**: robustness
- **Text**: The instruction includes a dedicated cross-role discrepancy validation step -- a
  structured comparison performed by a role or phase that is downstream from the inertia flag
  assignment role, comparing the upstream role's flag assignments against the Health Phase
  evidence to catch empirical inconsistencies (e.g., `stuck-at-first` raised but Signal Depth
  EARNED; `solo-hold` raised but contributor index shows 2 contributors). C-33 tests *logical*
  coexistence constraints (impossibility rules between flag categories and achievement names --
  these are structural rules that can be checked without reference to the data); C-35 tests a
  different orthogonal dimension -- *empirical* consistency of flag assignments against observed
  Health Phase evidence (flags that are structurally permissible but data-incorrect). An echo
  detection scan (C-33) that enforces logical rules without a separate empirical comparison fails
  C-35. A discrepancy check embedded within the same role that produced the flags fails -- the
  adversarial relationship (a downstream role checking an upstream role's claims) is the
  structural class. The discrepancy check must produce a named Discrepancy Table with retraction
  statements, and the action-writing role must carry a pre-write exclusion constraint covering
  both echo-retracted flags (from C-33 logic check) and discrepancy-retracted flags (from C-35
  empirical check).
- **Pass condition**: The instruction defines a downstream role or phase (distinct from the
  inertia phase) that: (1) explicitly compares inertia flag assignments against Health Phase
  evidence rows; (2) produces a named Discrepancy Table with retraction statements for any
  empirical mismatches found; (3) the action-writing role carries a pre-write constraint
  explicitly referencing both echo-retracted flags AND discrepancy-retracted flags as excluded
  from `resolves:` targeting. A check that names logical rules only (not data comparison) fails.
  A check that produces retraction statements but does not flow them into the action-writing
  pre-write constraint fails.
- **Derived from**: R15 excellence signal -- V-05 only. **Passes**: V-05.

---

### C-36 -- 2D Action Matrix (Round x Tier)

- **Weight**: aspirational | **Category**: structure
- **Text**: The action output section is organized as a two-dimensional matrix where each row is
  indexed by BOTH a temporal round dimension (Round 1: exactly 1 signal closes the gap; Round 2:
  2-3 signals; Round 3: 4+ signals or coordination required) AND a severity tier dimension
  (CRITICAL / WARNING / ADVANCING) within each round. C-08 tests gap prioritization by
  achievement distance; C-20 and C-22 test the `prevents:` rule; C-26 and C-29 test named-role
  structure and per-phase gates. C-36 tests a dimension none of those criteria cover: whether the
  action plan simultaneously encodes both *when* (round: how many signals to close the gap) and
  *how urgent* (tier: topic severity) for each recommended action. An action plan organized by
  round only (without tier within each round) satisfies multi-round sequencing but fails C-36. An
  action plan organized by tier only (CRITICAL/WARNING/ADVANCING blocks) satisfies tiered output
  but fails C-36. Only a plan where both dimensions are simultaneously present -- e.g., "Round 1
  | CRITICAL: {action}" and "Round 1 | WARNING: {action}" and "Round 2 | CRITICAL: {action}" --
  satisfies C-36. A narrative that mentions both rounds and tiers in prose without a structured
  matrix fails.
- **Pass condition**: The action section is structured so that each action row simultaneously
  carries a round label (Round 1/2/3 or equivalent) and a severity tier label
  (CRITICAL/WARNING/ADVANCING or equivalent). Both dimensions must be structurally present as
  distinct fields per action row -- a prose narrative or flat list fails even if it mentions both
  concepts. The instruction must specify the definitions for both axes (round = gap distance;
  tier = topic severity from inertia phase). An instruction that defines only one axis fails.
- **Derived from**: R15 excellence signal -- V-05 only (requires both Seed K and Seed V
  simultaneously). **Passes**: V-05.

---

## Scoring Model (v13)

- **Essential** (C-01--C-05): 5 criteria x 12 pts each = **60 pts**
- **Aspirational** (C-06--C-36): 28 criteria x 10/28 pts each (~0.357 pts) = **40 pts**
- **Total max: 100 pts**

Formula: `90 + (aspirational_passed / 28) * 10`
