Written to `simulations/quest/rubrics/org-pr-rubric-v2-2026-03-16.md`. Here is the complete updated rubric:

---

```
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 2
supersedes: org-pr-rubric-v1-2026-03-16.md
```

# Scoring Rubric -- org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis, and a go/no-go recommendation.

---

## Changelog (v1 -> v2)

Added three aspirational criteria extracted from R1 excellence signals:

- **C-11** (formula lock): V-01 C-07 PASS -- formula was not just stated but explicitly locked: "This formula is not editable at this step." Aspirational because it requires the skill to actively block rationalization of the verdict formula, not merely apply it.

- **C-12** (locator anti-pattern): V-02 C-08 PASS (strongest locator enforcement of all visible variations) -- "General concern is not a location." Teaching by negative example is a stronger guard than a percentage floor alone.

- **C-13** (inertia framing): V-04 C-10 estimated PASS -- "what breaks if this stays in" lifecycle framing naturally surfaces cross-cutting concerns the author would not self-identify. Inertia framing is the structural mechanism that makes C-10 reliably pass.

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total) — unchanged

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Multi-role coverage | coverage | 2+ labeled sections from defined role set, each with a finding |
| C-02 | P1/P2/P3 on every finding | correctness | Zero untagged findings |
| C-03 | File-based role selection rationale | correctness | Each role's inclusion tied to specific changed files |
| C-04 | Explicit go/no-go recommendation | correctness | Labeled verdict block, derivable from findings |
| C-05 | Per-role structure | format | Each section opens with role-name heading; sections can't bleed |

## Recommended Criteria (weight: 30 pts total) — unchanged

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Consensus analysis | depth | Convergence + conflicts both addressed |
| C-07 | P1 blocks go | correctness | Any open P1 = No-Go, no exceptions |
| C-08 | Actionable findings | depth | 80%+ of findings include a specific locator |

## Aspirational Criteria (weight: 10 pts total) — N=2 -> N=5

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Author-blind perspective | depth | 1+ finding per section challenges an embedded assumption |
| C-10 | Non-obvious issue surfaced | coverage | 1+ cross-cutting / out-of-diff finding present |
| C-11 | **Formula lock** | correctness | Explicit "this formula is not editable" or equivalent; applying it without locking it satisfies C-07 not C-11 |
| C-12 | **Locator anti-pattern named** | depth | Names what does NOT count as a locator (e.g., "General concern is not a location") |
| C-13 | **Inertia framing** | depth | 1+ finding answers "what breaks if this stays in" with a downstream effect or failure mode |

---

## Scoring Worksheet

```
Essential (N=5):    C-01[_] C-02[_] C-03[_] C-04[_] C-05[_]
  essential_pts  = essential_pass / 5 * 60 = __

Recommended (N=3):  C-06[_] C-07[_] C-08[_]
  recommended_pts = recommended_pass / 3 * 30 = __

Aspirational (N=5): C-09[_] C-10[_] C-11[_] C-12[_] C-13[_]
  aspirational_pts = aspirational_pass / 5 * 10 = __

Composite = __ + __ + __ = __

Golden = all essential pass AND composite >= 80? [YES / NO]
```

---

**Three extraction decisions:**

| New criterion | Source in scorecard | Why aspirational not recommended |
|---|---|---|
| C-11 formula lock | V-01 C-07 PASS: "not editable at this step" | C-07 already tests application; lock is an additive excellence signal, not load-bearing |
| C-12 locator anti-pattern | V-02 C-08 PASS (only variation to hit full PASS): named disallowed form | C-08's 80% floor covers correctness; explicit anti-pattern is a teaching mechanism, not a minimum bar |
| C-13 inertia framing | V-04 C-10 estimated PASS: "what breaks if this stays in" | C-10 tests that non-obvious issues appear; inertia framing is the mechanism that reliably produces them |
that triggered the concern, not generic observations. | depth | At least 80% of findings include a specific locator: file name, line range, component name, or named code pattern. Findings that say only "there may be a security risk" without a locator do not satisfy this criterion. |

---

## Aspirational Criteria (weight: 10 pts total)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Author-blind perspective** -- findings read as if reviewers had no access to the author's intent; no charitable interpretation of ambiguous patterns. | depth | At least one finding per active reviewer section challenges an assumption embedded in the diff rather than its stated behavior. Findings that only confirm what the diff intended to do do not satisfy this criterion for that section. |
| C-10 | **Non-obvious issue surfaced** -- the output includes at least one finding the author is unlikely to have self-identified: a cross-cutting concern, a latent interaction, or an omission not visible from the changed files alone. | coverage | Output contains at least one finding labeled or classified as a cross-cutting concern, an omission, or an out-of-diff interaction risk. The finding must be traceable to a role perspective not replicated by the author's own discipline. |
| C-11 | **Formula lock** -- the P1 = No-Go verdict formula is explicitly stated as non-overridable, not merely applied. | correctness | Output or skill prompt contains an explicit signal that the verdict formula cannot be rationalized away (e.g., "this formula is not editable", "no exceptions", or equivalent language). Applying the formula correctly without locking it satisfies C-07 but not C-11. |
| C-12 | **Locator anti-pattern named** -- the output or skill prompt explicitly defines what does NOT count as a locator, teaching by negative example. | depth | At least one of: (a) a statement like "General concern is not a location", (b) a named list of disallowed locator forms (e.g., "not: the codebase, this area, the feature"), or (c) an inline rejection of a vague finding with a redirect to a specific locator. |
| C-13 | **Inertia framing** -- at least one finding includes the cost of non-fix: what breaks, degrades, or compounds downstream if this issue is not resolved before merge. | depth | At least one finding answers "what breaks if this stays in" -- referencing a downstream effect, a latent failure mode, or a maintenance burden that will grow. Forward-looking projection required; backward description of the bug alone does not pass. |

---

## Criterion Reference Table

| ID | Text (short) | Weight | Category |
|----|-------------|--------|----------|
| C-01 | Multi-role coverage (2+ roles produce findings) | essential | coverage |
| C-02 | P1/P2/P3 on every finding | essential | correctness |
| C-03 | File-based role selection rationale | essential | correctness |
| C-04 | Explicit go/no-go recommendation | essential | correctness |
| C-05 | Per-role labeled structure | essential | format |
| C-06 | Consensus analysis (convergence + conflicts) | recommended | depth |
| C-07 | P1 blocks go (formula consistency) | recommended | correctness |
| C-08 | Actionable findings with locators (80% floor) | recommended | depth |
| C-09 | Author-blind challenge perspective | aspirational | depth |
| C-10 | Non-obvious cross-cutting issue surfaced | aspirational | coverage |
| C-11 | Formula lock (non-overridable signal) | aspirational | correctness |
| C-12 | Locator anti-pattern named | aspirational | depth |
| C-13 | Inertia framing (cost of non-fix) | aspirational | depth |

---

## Scoring Worksheet

```
Essential (N=5):   C-01[_] C-02[_] C-03[_] C-04[_] C-05[_]
  essential_pass = __ / 5
  essential_pts  = essential_pass / 5 * 60 = __

Recommended (N=3): C-06[_] C-07[_] C-08[_]
  recommended_pass = __ / 3
  recommended_pts  = recommended_pass / 3 * 30 = __

Aspirational (N=5): C-09[_] C-10[_] C-11[_] C-12[_] C-13[_]
  aspirational_pass = __ / 5
  aspirational_pts  = aspirational_pass / 5 * 10 = __

Composite = essential_pts + recommended_pts + aspirational_pts = __

Golden = all essential pass AND composite >= 80? [YES / NO]
```
