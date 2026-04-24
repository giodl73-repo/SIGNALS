Written to `simulations/quest/rubrics/scout-size-rubric-v2-2026-03-17.md`.

---

**Three new aspirational criteria added (C-11 through C-13):**

**C-11 — Specialization ownership** (refinement of C-06)
Sourced from V-02 and V-03, the two highest-scoring variations. Both required each named role to state what it *owns during the build*. Without this, the role list is decorative — program-plan still needs a follow-up to assign work.

**C-12 — Named unknowns in confidence** (refinement of C-05)
Sourced from V-02 Step 6 and V-03 RISK. Both required the confidence section to name the *specific unknowns that would move the rating* — not just a basis. A confidence statement without actionable unknowns can't be closed.

**C-13 — Cross-signal synthesis**
Sourced from V-03's deduction: "verbose juxtaposition over true synthesis." An output that merely restates each field in sequence hasn't reasoned; it's populated a form. Pass requires at least one sentence that cross-references two dimensions to produce a directional recommendation.

**Scoring model update:** aspirational denominator bumped from 2 to 5 — max composite still 100.
s") fails. Calendar dates fail.
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

### C-11 — Each named specialization states its implementation ownership
- **Weight**: aspirational
- **Category**: depth
- **Description**: Team-size signal goes beyond naming roles (C-06) to state what
  each specialization owns during implementation — e.g., "1 backend (owns event
  schema + storage layer) + 1 infra (owns deployment pipeline)". Without ownership
  scope, the role list is decorative and program-plan still needs a follow-up
  conversation to assign work. Sourced from V-02 Step 6 and V-03 INERTIA ANALYST,
  the two highest-scoring variations, both of which required "what they own during
  the build."
- **Pass condition**: At least one named specialization includes a description of
  its implementation scope or ownership area.

### C-12 — Confidence section names specific unknowns that would change the rating
- **Weight**: aspirational
- **Category**: depth
- **Description**: A confidence basis (C-05) is actionable only when the output also
  names the specific unknowns that, if resolved, would raise or lower the rating —
  e.g., "LOW confidence; HIGH once cross-service contracts are published." A basis
  without named unknowns leaves the reader unable to close the gap. Sourced from
  V-02 Step 6 ("name the specific unknowns driving it down") and V-03 RISK ("Name
  any unknowns that would move confidence down"), both present in the two
  highest-scoring variations.
- **Pass condition**: At least one concrete unknown is named that would move the
  confidence level if resolved, or output explicitly states no remaining unknowns.

### C-13 — Closing synthesis integrates signals, not just restates them
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output contains a concluding statement that draws a decision-
  relevant conclusion by cross-referencing two or more signal dimensions — e.g.,
  "HIGH complexity + LOW confidence in dependency map argues for deferral until
  contracts are published" or "LOW surface area + HIGH inertia cost argues for
  fast-track even at MEDIUM complexity." A closing that merely restates each field
  in sequence is juxtaposition, not synthesis. Sourced from V-03 deduction:
  "verbose juxtaposition over true synthesis" was the primary structural gap in
  the role-sequence variation.
- **Pass condition**: At least one sentence cross-references two or more signal
  dimensions (complexity, timeline, confidence, inertia) to produce a directional
  recommendation or decision-relevant observation.

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
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
- C-11 and C-12 are upward refinements of C-06 and C-05 respectively: an output can
  pass the essential/recommended bar and still fail these if ownership scope and named
  unknowns are absent.
- C-13 is the hardest aspirational to pass mechanically; it requires the model to
  reason across dimensions rather than populate fields in sequence.

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (specialization ownership), C-12 (named unknowns in confidence), C-13 (cross-signal synthesis); aspirational denominator updated 2 -> 5 |
