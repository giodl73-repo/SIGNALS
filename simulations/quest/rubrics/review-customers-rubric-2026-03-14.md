Rubric written to `simulations/quest/rubrics/review-customers-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential | 5 | All 12 personas scored (C-01), weighted aggregate (C-02), adoption blockers (C-03), positioning leaks (C-04), tier labels (C-05) |
| Recommended | 3 | Delight signals (C-06), amend order blockers-before-leaks (C-07), per-persona rationale (C-08) |
| Aspirational | 2 | Cross-persona pattern synthesis (C-09), amend-to-score projection (C-10) |

Key design decisions:
- **C-05 (tier assignment) is essential** — without it the 3x/2x/1x weighting is unauditable
- **C-03 and C-04 both require explicit "none" statements** — silence is a fail, not a pass
- **C-10 auto-passes when no blockers/leaks exist** — the skill shouldn't be penalized for a clean run
ith explicit scores for usefulness, clarity, and would-adopt on a 1-5 scale.
- **Pass condition**: Output contains all 12 persona identifiers (C-01 through C-12) with three
  numeric scores each. Missing persona or missing any of the three score dimensions = FAIL.

### C-02 -- Weighted Aggregate Score Computed

- **Weight**: essential
- **Category**: correctness
- **Text**: A weighted aggregate score is computed using the correct multipliers: primary audience
  3x, secondary audience 2x, non-target 1x. The final score is presented as a single number or
  range on a normalized scale.
- **Pass condition**: Output explicitly states the weighting scheme applied (3x/2x/1x) and
  presents a computed aggregate. An unweighted average or missing aggregate = FAIL.

### C-03 -- Adoption Blockers Identified

- **Weight**: essential
- **Category**: correctness
- **Text**: Any primary-audience persona with would-adopt < 3 is flagged as an adoption blocker.
  Blockers are named by persona ID and the low score is cited.
- **Pass condition**: If any primary persona scores would-adopt < 3, they appear in a dedicated
  blockers section. If no primary persona scores < 3, output explicitly states "no adoption
  blockers." Silently omitting the blocker check = FAIL.

### C-04 -- Positioning Leaks Identified

- **Weight**: essential
- **Category**: coverage
- **Text**: Any non-target persona who expresses confusion about whether the feature is meant for
  them (high usefulness or would-adopt despite being non-target, or explicit confusion in
  rationale) is flagged as a positioning leak.
- **Pass condition**: Output includes a positioning leaks section. If leaks exist they are named.
  If none exist, output explicitly states "no positioning leaks." Missing the section entirely
  = FAIL.

### C-05 -- Persona Tier Assignment Stated

- **Weight**: essential
- **Category**: format
- **Text**: Each persona is explicitly assigned a tier (primary, secondary, or non-target) before
  or alongside their scores, making the weighting auditable.
- **Pass condition**: Every persona entry includes a tier label. Tier labels absent from 3 or more
  personas = FAIL.

---

## Recommended Criteria

Output is materially better when these pass.

### C-06 -- Delight Signals Identified

- **Weight**: recommended
- **Category**: coverage
- **Text**: Any persona awarding a score of 5 on any dimension is flagged as a delight signal.
  Delight signals are grouped separately from blockers/leaks and interpreted for positioning or
  marketing value.
- **Pass condition**: Output includes a delight signals section (or explicitly states "no delight
  signals"). Delight signals present but not surfaced = FAIL on this criterion.

### C-07 -- Amendment Guidance Prioritizes Blockers Then Leaks

- **Weight**: recommended
- **Category**: behavior
- **Text**: The amend section sequences recommended actions: (1) resolve adoption blockers,
  (2) close positioning leaks, (3) amplify delight signals. This ordering is explicit or implied
  by section structure.
- **Pass condition**: Amend guidance exists and addresses blockers before leaks (or states there
  are none). Amend section absent, or leaks addressed before blockers = FAIL on this criterion.

### C-08 -- Per-Persona Rationale Provided

- **Weight**: recommended
- **Category**: depth
- **Text**: Each persona entry includes a brief rationale (1-3 sentences) explaining why they
  scored as they did, grounded in the persona's role, goals, or known pain points.
- **Pass condition**: At least 10 of 12 personas have non-trivial rationale (not just restating
  the score). Fewer than 10 with rationale = FAIL on this criterion.

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable.

### C-09 -- Cross-Persona Pattern Synthesis

- **Weight**: aspirational
- **Category**: depth
- **Text**: The output identifies a cross-cutting pattern across persona scores -- e.g., a role
  cluster that consistently scores low on clarity, or a segment where usefulness/would-adopt
  diverge -- and names the implication for feature design or messaging.
- **Pass condition**: Output includes at least one named cross-persona pattern with an explicit
  implication stated. Generic observations ("scores vary") do not count.

### C-10 -- Amend-to-Score Projection

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The amend section projects how resolving each blocker or leak would move the weighted
  aggregate score. Even a directional estimate ("resolving C-03 blocker likely lifts aggregate
  by ~0.3") qualifies.
- **Pass condition**: At least one blocker or leak has an associated score-impact estimate. If no
  blockers or leaks exist, this criterion is waived (auto-pass).

---

## Persona Stock Reference

| ID   | Name            | Role       |
|------|-----------------|------------|
| C-01 | Maria Chen      | Maker      |
| C-02 | James Okafor    | Builder    |
| C-03 | Priya Nair      | Strategist |
| C-04 | Tom Bergstrom   | Operator   |
| C-05 | Aisha Mensah    | Researcher |
| C-06 | Carlos Reyes    | Designer   |
| C-07 | Lin Wei         | Analyst    |
| C-08 | Sophie Dubois   | Manager    |
| C-09 | Raj Patel       | Advocate   |
| C-10 | Yuki Tanaka     | Evaluator  |
| C-11 | Elena Vasquez   | Buyer      |
| C-12 | Frank Hoffmann  | Regulator  |

Tier assignment (primary/secondary/non-target) is feature-specific and must be declared in the
skill run, not assumed from the stock list.

---

## Scoring Summary

| ID   | Criterion                          | Weight       | Category    |
|------|------------------------------------|--------------|-------------|
| C-01 | All 12 personas present and scored | essential    | correctness |
| C-02 | Weighted aggregate score computed  | essential    | correctness |
| C-03 | Adoption blockers identified       | essential    | correctness |
| C-04 | Positioning leaks identified       | essential    | coverage    |
| C-05 | Persona tier assignment stated     | essential    | format      |
| C-06 | Delight signals identified         | recommended  | coverage    |
| C-07 | Amendment guidance order correct   | recommended  | behavior    |
| C-08 | Per-persona rationale provided     | recommended  | depth       |
| C-09 | Cross-persona pattern synthesis    | aspirational | depth       |
| C-10 | Amend-to-score projection          | aspirational | behavior    |
