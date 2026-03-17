Rubric written to `simulations/quest/rubrics/trace-component-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 Event Anchor, C-02 Component Tree Traversal, C-03 State Update Map, C-04 Re-render Inventory, C-05 Final UI State | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 Fix Recommendations, C-10 Render Quantification | 10 |

**Key design decisions:**

- 5 essential criteria because all 5 trace steps in the skill description are independently meaningful — a trace with a state map but no re-render inventory is broken for its stated purpose
- The minimum passing score requires at least 2/3 recommended (composite = 80 exactly), so "all essential + nothing else" deliberately fails at 60 — the output has to be useful, not just structurally complete
- C-07 (Issue Detection) is recommended not essential because a clean trace with no issues is valid output; the skill says "identify" problems, not "always find" them
- Pass conditions are written as falsifiable tests, not descriptions — the rubric can be scored without ambiguity


### C-02 · Component Tree Traversal
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces the path of the action through the component hierarchy — from
  the event-receiving leaf up through handlers, context providers, or HOCs to the root of
  the affected subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with
  a clear parent→child or handler→provider direction. A flat list of components with no
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

## Aspirational Criteria (weight: 10 points total)

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
  and a verdict (justified or unnecessary).

---

## Criterion Summary Table

| ID   | Text (short)             | Weight       | Category    |
|------|--------------------------|--------------|-------------|
| C-01 | Event Anchor             | essential    | correctness |
| C-02 | Component Tree Traversal | essential    | correctness |
| C-03 | State Update Map         | essential    | correctness |
| C-04 | Re-render Inventory      | essential    | correctness |
| C-05 | Final UI State           | essential    | correctness |
| C-06 | Side Effect Coverage     | recommended  | coverage    |
| C-07 | Issue Detection          | recommended  | depth       |
| C-08 | Framework Vocabulary     | recommended  | behavior    |
| C-09 | Fix Recommendations      | aspirational | depth       |
| C-10 | Render Quantification    | aspirational | depth       |

---

## Scoring Examples

**Minimum passing output** (all essential, no recommended):
- C-01 through C-05 pass, C-06/07/08 fail, C-09/10 fail
- composite = (5/5 * 60) + (0/3 * 30) + (0/2 * 10) = 60
- Result: FAIL (composite < 80, even though all essential pass)

**Solid output** (all essential + two recommended):
- C-01 through C-05 pass, C-06 + C-07 pass, C-08 fail, C-09/10 fail
- composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10) = 60 + 20 = 80
- Result: PASS (all essential pass AND composite >= 80)

**Strong output** (all essential + all recommended + one aspirational):
- C-01 through C-08 pass, C-09 passes, C-10 fails
- composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10) = 60 + 30 + 5 = 95
- Result: PASS (golden)
