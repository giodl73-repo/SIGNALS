```markdown
---
skill: quest-rubric
skill_target: scout-inertia
date: 2026-03-16
version: 3
---

# Scoring Rubric — scout-inertia

> Inertia is the primary competitor for every feature. This rubric enforces the central contract of
> scout-inertia: the output must answer "why does inertia lose?" If it cannot, the analysis fails
> regardless of quality elsewhere.

## Composite Score Formula

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Essential Criteria

*Must all pass. Without these the output is not useful.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Workaround mapped in detail** | correctness | essential |
| C-02 | **Switching cost quantified across dimensions** | depth | essential |
| C-03 | **Inertia threat score is HIGH** | correctness | essential |
| C-04 | **"Why inertia loses" answered with specifics** | correctness | essential |
| C-05 | **Workaround failure modes identified** | coverage | essential |

### C-01 — Workaround mapped in detail

**Pass condition**: Output names the specific workaround (tool, file type, manual step, or process)
and describes at minimum: (a) what data or action it handles, (b) who performs it, and (c) how
often. "Teams use spreadsheets" fails. "PMs export to CSV weekly, pivot in Excel, email to leads
before Monday standup" passes.

### C-02 — Switching cost quantified across dimensions

**Pass condition**: At least two of the three dimensions — time cost, training cost, disruption
cost — carry a number or explicit estimate (ranges acceptable: "2-4 hours per user", "1 sprint of
workflow disruption"). Purely qualitative labels ("high", "low") do not pass. The AMEND requirement
is that costs are quantified; this criterion enforces it.

### C-03 — Inertia threat score is HIGH

**Pass condition**: Output explicitly states the inertia threat score as HIGH. The default is always
HIGH — the output must not silently omit the score, and must not downgrade it without documented
evidence of an unusual mitigating factor with a named rationale. "Inertia is LOW because the feature
is compelling" fails; compelling features do not reduce inertia, they only affect adoption after
switching costs are paid.

### C-04 — "Why inertia loses" answered with specifics

**Pass condition**: Output provides at least two specific, distinct, and testable conditions under
which teams abandon the workaround in favor of the feature. Conditions must be falsifiable ("teams
switch when workaround fails to handle files > 10MB" passes; "teams switch when they see the value"
fails). This is the central question of the skill — if it is absent, the output is not useful.

### C-05 — Workaround failure modes identified

**Pass condition**: Output identifies at least two specific scenarios where the current workaround
breaks, produces errors, causes re-work, or cannot scale. These are the observable cracks in the
inertia armor. Generic pain points ("manual is slow") do not pass; concrete failure modes ("CSV
export silently truncates rows over 65,536 — no error message") pass.

---

## Recommended Criteria

*Strong outputs satisfy all three. Missing one is a quality signal, not a blocker.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| R-01 | **Trigger scoped to team type** | precision | recommended |
| R-02 | **Role-level precision** | precision | recommended |
| R-03 | **At least one cost cited** | depth | recommended |

### R-01 — Trigger scoped to team type

**Pass condition**: Defeat conditions (from C-04) name a specific team type or segment rather than
applying uniformly to all users. "Engineering teams switch when..." or "PMs in regulated industries
switch when..." passes. "Users switch when..." fails. Different team types face different inertia
profiles; a trigger that ignores team type is underspecified.

### R-02 — Role-level precision

**Pass condition**: Every actor named in the analysis (workaround performer, decision-maker,
affected party) is identified at role level, not department or group level. "The PM" or "a data
analyst" passes. "The team", "users", or "marketing" fails. Role-level precision is required because
switching cost and trigger conditions vary by role — a department label cannot carry that weight.

### R-03 — At least one cost cited

**Pass condition**: At least one quantified cost from C-02 is tied to a specific actor or role
named elsewhere in the analysis. A floating number with no actor is weaker than a number anchored
to a person who pays it. "2 hours per PM per week" with PMs named as the workaround performer
passes. "2 hours" with no role anchor is a partial pass.

---

## Aspirational Criteria

*Outputs that satisfy these are structurally self-enforcing — the analyst cannot produce a weak
output without the structure itself flagging the gap.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| A-01 | **Per-section revision gate** | enforcement | aspirational |
| A-02 | **Column-level structural constraint** | enforcement | aspirational |
| A-03 | **Composite gate with back-pointers** | enforcement | aspirational |
| A-04 | **Role precision as continuation gate** | enforcement | aspirational |

### A-01 — Per-section revision gate

**Pass condition**: Each section of the output contains an explicit self-score with a defined pass
condition. An analyst who completes a section must actively mark it pass or fail before moving on.
Sections without self-scores allow the analyst to move forward on weak entries; sections with
self-scores create a local revision loop at the point where correction cost is lowest.

### A-02 — Column-level structural constraint

**Pass condition**: Every column or field in the output carries an explicit semantic contract
(e.g., "this cell must contain a role name, not a department"). Column headers that are labels only
("Who") do not pass; column headers with embedded type constraints ("Who [role, not department]")
pass. The constraint must be visible to the analyst at the moment of entry, not only at review.

### A-03 — Composite gate with back-pointers

**Pass condition**: The output includes a final gate section that aggregates all per-criterion
pass/fail results and, for each failure, names the specific section number to return to for
correction. An advisory self-score does not pass. The gate must function as a completion blocker:
an analyst cannot declare the artifact done while any criterion cell contains a failure without
being directed to the exact section that requires revision. A gate section that lists criteria
without section back-pointers is advisory, not structural.

*Source*: V-01 excellence signal — Section 6 as a cross-criterion completion gate rather than a
summary score.

### A-04 — Role precision as continuation gate

**Pass condition**: Role precision is enforced as a pre-condition for entering subsequent sections,
not as a scoring note at the end. The check must appear early in the output — at or before the
point where roles are first declared — with an explicit instruction to correct before continuing.
Acceptable form: *"If the 'who performs it' entry contains 'teams', 'users', 'people', or a
department name, replace it before continuing to the next section."* A role precision check that
appears only in a final review section or in the rubric rather than in the output template does not
pass; by that point the analyst has already built subsequent sections on an underspecified actor.

*Source*: V-01 excellence signal — role check in Section 1 as a pre-condition for Section 2 entry,
enforced at the moment of lowest correction cost.

---

## Scoring Reference

| Variation | Essential | Recommended | Aspirational | Score | Golden? |
|-----------|-----------|-------------|--------------|-------|---------|
| Perfect | 5/5 → 60 | 3/3 → 30 | 4/4 → 10 | **100** | YES |
| Min golden | 5/5 → 60 | 1/3 → 10 | 2/4 → 5 | **75** | NO — fails >= 80 |
| Min golden | 5/5 → 60 | 2/3 → 20 | 0/4 → 0 | **80** | YES |
```

---

Two changes from v2:

1. **Formula**: `aspirational_pass / 2 * 10` → `aspirational_pass / 4 * 10` (denominator tracks actual count)
2. **Added A-03 and A-04** from V-01 excellence signals — both enforce correction at the point of lowest cost: A-03 via a cross-criterion completion gate with back-pointers, A-04 via a role check that blocks section entry rather than appearing post-hoc in review.
