Written to `simulations/quest/rubrics/trace-component-rubric-v2-2026-03-14.md`. Here's the complete updated rubric:

---

# Rubric: trace-component (v2)

**12 criteria across 3 tiers:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 Fix Recommendations, C-10 Render Quantification, **C-11 Inline Phase-Close Gates**, **C-12 Mandatory Comparison Column** | 10 |

---

### C-11 · Inline Phase-Close Gates *(new)*
- **Category**: behavior
- **Text**: The template prints the failure condition for each sequential phase at the phase boundary itself — not in external rubric instructions. The model encounters its own gate at the moment it would otherwise fail. The gate names the exact vague phrase that does not close the phase.
- **Pass condition**: At least two phase boundaries carry an inline close condition naming the exact failure mode. A general preamble instruction does not satisfy this — the gate must appear at the boundary.

### C-12 · Mandatory Comparison Column *(new)*
- **Category**: behavior
- **Text**: At least one table column structurally cannot be satisfied with N/A or silence — it requires per-row comparative analysis. The column instruction explicitly disallows N/A. The only valid escape is a substantive claim that itself constitutes analysis.
- **Pass condition**: At least one column prohibits N/A by instruction, has per-row entries, and demonstrates the escape pattern with a substantive claim. A FINDINGS section that consolidates once for the whole output does not satisfy this — forcing must be per-row.

---

**Two changes from v1:**

1. **C-10 tightened** — count and verdict must be co-located per component (same row or sentence). V-01's split layout revealed the original wording allowed separation that dilutes the criterion.

2. **Aspirational scoring** — pool stays at 10 pts, now split 4 ways at 2.5 pts each. Pass threshold (80) and essential gate unchanged. New ceiling: 100.
**Text**: The output traces the path of the action through the component hierarchy — from
  the event-receiving leaf up through handlers, context providers, or HOCs to the root of
  the affected subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with
  a clear parent->child or handler->provider direction. A flat list of components with no
  structural relationship does not pass.

### C-03 · State Update Map
- **Category**: correctness
- **Weight**: essential
- **Text**: The output identifies every state mutation triggered by the action: local
  component state (`useState`, `this.setState`), context state, and store state (Redux,
  Zustand, Pinia, etc.). For each mutation: the state key, old value shape, new value
  shape, and the component or store that owns it.
- **Pass condition**: At least one concrete state mutation is named with its owner. "State
  updates" as a section header with no specifics does not pass.

### C-04 · Re-render Inventory
- **Category**: correctness
- **Weight**: essential
- **Text**: The output lists which components re-render as a result of the state changes,
  explaining why each one re-renders (owns the state, subscribes to context, receives new
  props, etc.).
- **Pass condition**: At least one component is listed with its re-render cause. "Several
  components re-render" does not pass.

### C-05 · Final UI State
- **Category**: correctness
- **Weight**: essential
- **Text**: The output describes the observable UI state after all synchronous effects and
  at least one async settle point (e.g., after a loading state resolves). This is the
  "what the user sees" close to the trace.
- **Pass condition**: A concrete final state is described — visible elements, disabled
  states, error messages, or confirmed no-change. "UI updates accordingly" does not pass.

---

## Recommended Criteria (weight: 30 points total)

Output is meaningfully better with these. Missing one is acceptable; missing both is a gap.

### C-06 · Side Effect Coverage
- **Category**: coverage
- **Weight**: recommended
- **Text**: The output captures side effects triggered by the action beyond synchronous
  state updates: API calls (endpoint + method), timers set or cleared, subscriptions
  started or torn down, localStorage writes, or navigation events.
- **Pass condition**: At least one side effect is identified with its mechanism (e.g.,
  `useEffect` dependency, `thunk`, `saga`). If the trace genuinely has no side effects,
  the output explicitly states "no side effects detected" — silence does not pass.

### C-07 · Issue Detection
- **Category**: depth
- **Weight**: recommended
- **Text**: The output identifies at least one concrete problem in the traced path from
  the canonical issue types: unnecessary re-renders, missing loading states, error state
  gaps, or accessibility failures (missing ARIA, keyboard trap, focus loss after action).
- **Pass condition**: At least one issue is named with the component or state path where
  it occurs. "May have performance issues" does not pass; "ButtonGroup re-renders on every
  keystroke because it receives the full form state object" passes.

### C-08 · Framework Vocabulary
- **Category**: behavior
- **Weight**: recommended
- **Text**: The output uses terminology appropriate to the detected or stated frontend
  framework (e.g., React: hooks, reconciler, fiber; Vue: reactivity system, watcher,
  computed; Angular: zone.js, change detection strategy, signals).
- **Pass condition**: At least two framework-specific terms appear correctly applied in
  context. A fully framework-agnostic trace on framework-specific code does not pass.

---

## Aspirational Criteria (weight: 10 points total, 2.5 pts each)

These raise the bar once essential and recommended are stable.

### C-09 · Fix Recommendations
- **Category**: depth
- **Weight**: aspirational
- **Text**: For each identified issue (from C-07), the output provides a concrete, minimal
  fix — a specific hook, memoization boundary, ARIA attribute, or state restructure — not
  a general best-practice lecture.
- **Pass condition**: At least one issue has a fix that names a specific API or pattern
  (e.g., "wrap ButtonGroup in `React.memo` and pass only `formValid` instead of the full
  state object").

### C-10 · Render Quantification
- **Category**: depth
- **Weight**: aspirational
- **Text**: The output provides a render count or relative render frequency for the
  identified re-renders — either an exact count per action or a "renders N times per
  keystroke" characterization — and flags any component that renders more than once per
  user action without justification.
- **Pass condition**: At least one component has a numeric or rate-based render annotation
  AND a verdict (justified or unnecessary) co-located in the same table row or sentence.
  A count column and a verdict column that appear in separate sections of the output do
  not jointly satisfy this criterion — both must be co-located per component.

### C-11 · Inline Phase-Close Gates
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The template prints the failure condition for each sequential phase at the
  phase boundary itself — not only in external rubric instructions. The model encounters
  the pass/fail gate in its own output context at the moment it would otherwise fail. The
  gate names the exact vague phrase that does not close the phase (e.g., "'State updates'
  with no specifics does not close this phase").
- **Pass condition**: At least two phase boundaries in the trace output carry an inline
  close condition that names the exact failure mode. A general section instruction at the
  top of the output does not satisfy this criterion — the gate must appear at the
  boundary, not in a preamble.

### C-12 · Mandatory Comparison Column
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The output includes at least one table column that structurally cannot be
  satisfied with N/A or silence — a column that requires per-row comparative or
  evaluative analysis (e.g., "What this approach misses vs. DevTools," "unnecessary or
  justified," "what ad-hoc inspection would not show"). The column header or its inline
  instruction explicitly disallows N/A. The only valid escape from a column cell is a
  substantive claim that itself constitutes analysis (e.g., "Nothing — this row is fully
  observable in DevTools via the Network tab. Note: this is the exception, not the rule").
- **Pass condition**: At least one table column prohibits N/A by instruction, has per-row
  entries, and at least one row demonstrates the escape pattern with a substantive claim
  rather than a blank or generic phrase. A FINDINGS section that consolidates issues once
  for the whole output does not satisfy this criterion — the forcing must be per-row.

---

## Criterion Summary Table

| ID   | Text (short)                | Weight       | Category    | Pts |
|------|-----------------------------|--------------|-------------|-----|
| C-01 | Event Anchor                | essential    | correctness | 12  |
| C-02 | Component Tree Traversal    | essential    | correctness | 12  |
| C-03 | State Update Map            | essential    | correctness | 12  |
| C-04 | Re-render Inventory         | essential    | correctness | 12  |
| C-05 | Final UI State              | essential    | correctness | 12  |
| C-06 | Side Effect Coverage        | recommended  | coverage    | 10  |
| C-07 | Issue Detection             | recommended  | depth       | 10  |
| C-08 | Framework Vocabulary        | recommended  | behavior    | 10  |
| C-09 | Fix Recommendations         | aspirational | depth       | 2.5 |
| C-10 | Render Quantification       | aspirational | depth       | 2.5 |
| C-11 | Inline Phase-Close Gates    | aspirational | behavior    | 2.5 |
| C-12 | Mandatory Comparison Column | aspirational | behavior    | 2.5 |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Pass condition**: all 5 essential criteria pass AND composite >= 80.

---

## Scoring Examples

**Minimum passing output** (all essential, no recommended):
- C-01 through C-05 pass, C-06/07/08 fail, C-09 through C-12 fail
- composite = (5/5 * 60) + (0/3 * 30) + (0/4 * 10) = 60
- Result: FAIL (composite < 80, even though all essential pass)

**Solid output** (all essential + two recommended):
- C-01 through C-05 pass, C-06 + C-07 pass, C-08 fail, C-09 through C-12 fail
- composite = (5/5 * 60) + (2/3 * 30) + (0/4 * 10) = 60 + 20 = 80
- Result: PASS (all essential pass AND composite >= 80)

**Strong output** (all essential + all recommended + two aspirational):
- C-01 through C-08 pass, C-11 + C-12 pass, C-09 + C-10 fail
- composite = (5/5 * 60) + (3/3 * 30) + (2/4 * 10) = 60 + 30 + 5 = 95
- Result: PASS (golden)

**Perfect output** (all 12 criteria):
- C-01 through C-12 all pass
- composite = (5/5 * 60) + (3/3 * 30) + (4/4 * 10) = 60 + 30 + 10 = 100
- Result: PASS (ceiling)

---

## v2 Changelog

**Source**: Round 1 scorecard excellence signals (trace-component-scorecard-R1-2026-03-14.md)

**C-10 tightened**: Pass condition now requires count and verdict co-located per component
in the same row or sentence. V-01's split layout (count column + separate verdict
subsection) revealed the gap — the original wording allowed spatial separation that
dilutes the criterion.

**C-11 added** (Inline Phase-Close Gates): Extracted from V-04's pattern. Printing the
failure condition at the phase boundary puts the gate in the model's output context at
the moment of potential failure. External rubric instructions are not in that context.
Generalizable to any skill with sequential phases.

**C-12 added** (Mandatory Comparison Column): Extracted from V-05's "What ad-hoc misses"
column pattern. A column that cannot say N/A forces per-row analysis; a section can be
cleared once but a column must be cleared per row. The escape pattern — a substantive
claim that itself constitutes analysis — is the mechanism that prevents the criterion
from becoming unsatisfiable.

**Aspirational pool**: Stays at 10 pts total, now divided across 4 criteria at 2.5 pts
each. The pass threshold (80) and essential gate are unchanged.
