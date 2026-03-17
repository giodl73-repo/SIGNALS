Looking at the 4 excellence signals from V-02, I'll group them into 2 aspirational criteria (self-correction mechanism, structural constraint enforcement) and write the complete v2 rubric.

```markdown
---
skill: quest-rubric
skill_target: scout-inertia
date: 2026-03-16
version: 2
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
| R-01 | **Adoption trigger is scoped to a team type** | specificity | recommended |
| R-02 | **Workaround owner is named by role** | precision | recommended |
| R-03 | **At least one switching cost has a cited basis** | credibility | recommended |

### R-01 — Adoption trigger is scoped to a team type

**Pass condition**: At least one condition in C-04 names a specific team type, role, or context
("data-heavy teams", "PMs managing more than one product line") rather than stating a universal
trigger. Universal triggers ("all teams switch when...") obscure the segmentation that matters for
rollout planning.

### R-02 — Workaround owner is named by role

**Pass condition**: The actor identified in C-01 is a role, not a department or vague population.
"PMs" passes. "Teams" fails. "The person who runs the export" fails. The distinction matters because
role-specific friction drives targeted onboarding.

### R-03 — At least one switching cost has a cited basis

**Pass condition**: At least one quantified cost in C-02 includes an explicit basis for the
estimate — an analogy, a comparable migration, a stated assumption, or a source. "2-4 hours per
user (based on similar CSV-to-tool migrations in Q3 onboarding)" passes. An unsourced number is
better than a qualitative label but weaker than a grounded estimate.

---

## Aspirational Criteria

*Rare in practice. Either one passing indicates a high-quality, self-verifying output.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| A-01 | **Self-correction mechanism present** | robustness | aspirational |
| A-02 | **Structural constraints enforce specificity** | robustness | aspirational |

### A-01 — Self-correction mechanism present

**Pass condition**: Output includes both (a) a per-section self-assessment keyed to each essential
criterion (PASS/FAIL with explicit pass condition stated or referenced) AND (b) a composite gate
that explicitly instructs revision before finalization if any essential criterion is FAIL. Either
element alone does not pass — the self-score without the revision gate is a post-hoc label, not a
production control.

**Why this matters**: A self-scoring mechanism with a revision gate catches misses before the output
is delivered, reducing the rate of partial outputs that satisfy intent but miss the letter of a
criterion. Observed in V-02 (Round 1): Section 6 composite table plus per-section PASS/FAIL
checkboxes reduced estimated recommended-tier misses compared to V-01.

### A-02 — Structural constraints enforce specificity

**Pass condition**: At least two fields or column headers in the output use constraint language that
makes a vague entry structurally inconsistent — not just instructionally discouraged. Examples that
pass: a column labeled "Observable trigger" (prevents "teams switch when they see value"), a Unit
column with example values ("hours or days/user") that makes a unitless number visibly incomplete,
a column labeled "User-visible symptom" (prevents "manual is slow"). A prose instruction saying
"be specific" does not pass this criterion; the constraint must be in the structure itself.

**Why this matters**: Instructions tell the author what to do; structure makes the wrong thing
harder to do than the right thing. A column header is active every time a row is filled in.
Observed in V-02 (Round 1): the "Observable trigger" and Unit columns prevented the two most
common failure modes (unfalsifiable conditions, unitless costs) without requiring the author to
re-read the instructions.

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial rubric — 5 essential criteria |
| v2 | 2026-03-16 | Added R-01..R-03 recommended criteria; added A-01 (self-correction mechanism) and A-02 (structural constraints) from Round 1 excellence signals |
```

---

Two notes on the decisions made:

**Signals 1 + 3 merged into A-01.** Inline self-scoring and the revision gate are inseparable — a self-score without a gate is just a label; a gate without per-section scores is unactionable. They form one mechanism.

**Signals 2 + 4 merged into A-02.** Column-header constraints and unit-column forcing are both instances of the same pattern: structure that makes the wrong entry visibly inconsistent. Splitting them would produce two criteria that score identically in practice.

I also inferred R-01..R-03 from context (the original rubric was truncated before the recommended body). If the actual R-01..R-03 differ, swap them in — the aspirational section stands regardless.
