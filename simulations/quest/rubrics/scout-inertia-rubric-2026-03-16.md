```markdown
---
skill: quest-rubric
skill_target: scout-inertia
date: 2026-03-16
version: 1
---

# Scoring Rubric — scout-inertia

> Inertia is the primary competitor for every feature. This rubric enforces the central contract of
> scout-inertia: the output must answer "why does inertia lose?" If it cannot, the analysis fails
> regardless of quality elsewhere.

## Composite Score Formula

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 2 * 10)
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

*Output is better with these. Two or three passing raises quality significantly.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-06 | **Stop signal surfaced when "why inertia loses" is unanswerable** | behavior | recommended |
| C-07 | **Team segmentation: high vs. low inertia profiles** | depth | recommended |
| C-08 | **All three switching cost dimensions addressed separately** | coverage | recommended |

### C-06 — Stop signal surfaced when "why inertia loses" is unanswerable

**Pass condition**: If the skill cannot produce at least two passing conditions for C-04, the output
explicitly surfaces a stop recommendation ("Recommend halting design until inertia loss conditions
are identified"). The skill description says "if you cannot answer that, stop" — this criterion
checks that the stop signal is visible in the artifact, not silently absent.

### C-07 — Team segmentation: high vs. low inertia profiles

**Pass condition**: Output identifies at least two distinct team or user types with meaningfully
different inertia levels (e.g., "small teams with a single data owner: low switching cost, moderate
inertia; enterprise teams with embedded Excel skills and audit trails: high switching cost, extreme
inertia"). Segmentation must be tied to switching cost differences, not just attitudes.

### C-08 — All three switching cost dimensions addressed separately

**Pass condition**: Time cost, training cost, and disruption cost appear as distinct labeled
sections or rows — not merged into a single paragraph. Each must carry at least one quantified
estimate (satisfying C-02 at minimum for two; this criterion requires all three). Separation matters
because the three dimensions have different mitigations.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-09 | **Tipping point identified: measurable threshold where inertia reliably loses** | depth | aspirational |
| C-10 | **Steel-man of inertia: strongest case for staying, then rebutted** | depth | aspirational |

### C-09 — Tipping point identified

**Pass condition**: Output names a specific, measurable threshold — a team size, data volume,
frequency of workaround failure, or org event — at which inertia reliably breaks. The threshold
must be stated as a number or event ("teams with > 3 contributors sharing the same spreadsheet
hit merge conflicts within 2 weeks, which is the tipping point"), not an impression. This turns
inertia analysis into a targeting instrument.

### C-10 — Steel-man of inertia: strongest case for staying, then rebutted

**Pass condition**: Output presents the single strongest argument for why a team should rationally
stay with the workaround (not a strawman), then provides a direct rebuttal grounded in the failure
modes from C-05. The steel-man must acknowledge real switching costs, not dismiss them. This
demonstrates that the analysis has genuinely pressure-tested the feature decision rather than
assumed adoption.
```

The rubric writes to: `simulations/quest/rubrics/scout-inertia-rubric-v1-2026-03-16.md`

Key design decisions:

- **C-03 threat score is always HIGH** — the skill spec is explicit that HIGH is the default and cannot be silently omitted or downgraded without named evidence. This is a correctness gate, not a depth check.
- **C-04 is the load-bearing criterion** — the skill description says "if you cannot answer that, stop." C-04 enforces the answer exists; C-06 enforces the stop signal when it doesn't.
- **C-02 + C-08 split** — C-02 is the AMEND requirement (quantified, any two dimensions); C-08 raises the bar to all three dimensions separated. This lets a passing output be promoted to recommended quality by improving one criterion.
- **C-10 steel-man** is aspirational because most runs will skip it, but it's the difference between a defensive analysis and a genuinely pressure-tested one.
