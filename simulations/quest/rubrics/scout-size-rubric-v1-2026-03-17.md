---
skill: quest-rubric
skill_target: scout-size
date: 2026-03-17
version: 1
---

# Scoring Rubric — scout-size

## Purpose

Evaluates output quality for the `scout-size` skill, which produces a feature sizing
signal covering surface area, implementation complexity, team-size signal, timeline
signal, confidence level, and an inertia check against the current workaround cost.

---

## Essential Criteria (60 points total — all must pass)

### C-01 — Complexity tier is present and uses the canonical scale
- **Weight**: essential
- **Category**: correctness
- **Description**: Output contains an explicit implementation complexity rating using
  exactly one of: LOW, MEDIUM, HIGH, XL. No narrative substitutes ("moderate", "non-trivial")
  in place of the tier label.
- **Pass condition**: One of {LOW, MEDIUM, HIGH, XL} appears as a labeled rating for
  implementation complexity.

### C-02 — Timeline signal is a sprint range, not a point estimate
- **Weight**: essential
- **Category**: correctness
- **Description**: Timeline is expressed as a range (e.g., "2-3 sprints", "4-6 sprints").
  A single number without range (e.g., "3 sprints") fails. Calendar dates fail.
- **Pass condition**: Output contains a sprint range with both lower and upper bound
  for the timeline signal.

### C-03 — Surface area is quantified by integration points
- **Weight**: essential
- **Category**: correctness
- **Description**: Surface area section identifies discrete integration points (APIs,
  hooks, namespaces, data stores, UI surfaces, external systems). Must be a count or
  enumerated list — not a vague qualifier like "moderate surface area".
- **Pass condition**: Output names or counts at least 2 distinct integration points,
  or explicitly states 0-1 with reasoning.

### C-04 — Inertia check is present and names the workaround cost
- **Weight**: essential
- **Category**: coverage
- **Description**: Output includes an explicit inertia check that names what teams
  currently do without this feature (the workaround) and characterizes its cost
  (time, error rate, manual effort, missing capability). Absence of this section
  is a hard fail — it is the signal's differentiator from a raw estimate.
- **Pass condition**: A clearly labeled inertia check section or paragraph identifies
  the current workaround and states at least one cost dimension.

### C-05 — Confidence level is stated with basis
- **Weight**: essential
- **Category**: depth
- **Description**: Output states a confidence level (percentage, tier, or LOW/MED/HIGH
  label) AND gives the primary reason for that level (e.g., "HIGH confidence — surface
  area well-understood from existing flow skill", "LOW confidence — cross-service
  dependencies uncharted"). Confidence without basis is not actionable.
- **Pass condition**: Confidence level is present AND at least one sentence explains
  why that level was assigned.

---

## Recommended Criteria (30 points total)

### C-06 — Team-size signal names required specializations
- **Weight**: recommended
- **Category**: depth
- **Description**: Team-size signal goes beyond headcount to name the types of
  specialists required (e.g., "1 backend + 1 infra", not just "2 engineers"). This
  lets program-plan route work correctly.
- **Pass condition**: Team-size signal identifies at least one role or specialization,
  not just a number.

### C-07 — Complexity rating is justified with at least one driver
- **Weight**: recommended
- **Category**: depth
- **Description**: The complexity tier (C-01) is accompanied by the primary driver
  that determined the rating — e.g., "HIGH because of distributed transaction boundary",
  "LOW because isolated namespace with no shared state". Bare tier labels are less
  useful downstream.
- **Pass condition**: At least one sentence following or inline with the complexity
  tier names what pushed it to that level.

### C-08 — AMEND instructions modify the stated output, not the process
- **Weight**: recommended
- **Category**: behavior
- **Description**: When an AMEND directive is present (adjust confidence thresholds
  or focus on a complexity dimension), the output reflects the amendment in its
  content — e.g., a revised confidence level, or expanded analysis of the named
  dimension. The skill should not just acknowledge the amendment; it should
  change the artifact.
- **Pass condition**: If AMEND is invoked, at least one substantive change in the
  output (different tier, revised confidence, expanded section) can be traced to
  the amendment. If no AMEND is present, criterion is scored as pass by default.

---

## Aspirational Criteria (10 points total)

### C-09 — Sizing signal explicitly scopes what is NOT included
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output states at least one thing the sizing does NOT cover
  (out-of-scope sub-systems, deferred complexity, assumptions made). This prevents
  silent misreads when program-plan consumes the signal.
- **Pass condition**: At least one explicit exclusion, assumption, or out-of-scope
  boundary is named.

### C-10 — Inertia check includes a break-even signal
- **Weight**: aspirational
- **Category**: depth
- **Description**: Beyond naming the workaround cost, the output estimates when
  building the feature pays off relative to continued workaround cost — even as
  a rough qualitative signal ("break-even at ~4 uses/week", "never breaks even
  if adoption stays below 3 teams"). This is the highest-value form of the
  inertia check for investment decisions.
- **Pass condition**: Output contains a break-even estimate or explicitly states
  that break-even cannot be assessed and why.

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Publish-ready sizing signal |
| Silver | >= 60, all essential pass | Useful but missing depth |
| Bronze | >= 40, <=2 essential fail | Partial signal, needs revision |
| Fail | Any essential fail | Output not usable downstream |

---

## Evaluation Notes

- C-04 (inertia check) is the highest-signal differentiator — a sizing output without
  it is indistinguishable from a naive estimate.
- C-02 (sprint range) guards against false precision; point estimates imply certainty
  that sizing signals never have.
- C-08 only activates on AMEND invocations; default-pass otherwise to avoid penalizing
  non-amend runs.
- Surface area (C-03) and team-size (C-06) together feed `program-plan` routing — weak
  values here are the most common downstream failure mode.
