Reading the R6 scorecard for new excellence patterns not yet captured as criteria.

Three new patterns emerge, all of which scored PARTIAL or FAIL across every variation in R6 — indicating they represent aspirations the current criteria don't yet enforce:

1. **Zero-mutation declaration** — V-01's TABLE 3 zero-mutation row format (Key="none" row with explanation; silence blocked) was the only variation to address the no-mutation case structurally. No criterion covers this gap.

2. **Issue category completeness** — V-03's Phase 6 four-category clearing checklist (performance, unnecessary re-renders, accessibility, async error handling) was the strongest pattern. C-07 covers format; nothing covers category coverage.

3. **Unnecessary re-render promotion** — C-22 scored PARTIAL for all five variations. The gap was always the cross-link: re-renders flagged as unnecessary in the inventory never explicitly appeared in findings with a fix. C-22 covers the annotation; promotion to findings is uncovered.

---

```markdown
# Rubric: trace-component (v7)

**26 criteria across 3 tiers — 3 new aspirational criteria added from R6 excellence signals:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-26 | 36 |

**Ceiling: 126 pts** (up from 120; 3 new criteria × 2 pts each)

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. Failing any one essential criterion fails the entire output regardless of
composite score.

### C-01 · Event Anchor
- **Category**: correctness
- **Weight**: essential
- **Text**: The output names the exact event that triggered the trace: the event type (click,
  submit, input, etc.), the specific UI component that fired it (not a generic description like
  "the button"), the event payload or input value if relevant, and the handler function or
  lifecycle hook that received it.
- **Pass condition**: The event type, the exact component name, and the handler function are all
  named. "The button fires a click event" without naming the handler does not pass. "The input"
  without naming the component does not pass.

### C-02 · Component Tree Traversal
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces the path of the action through the component hierarchy — from the
  event-receiving leaf up through handlers, context providers, or HOCs to the root of the affected
  subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with a clear
  parent→child or handler→provider direction. A flat list of components with no structural
  relationship does not pass.

### C-03 · State Update Map
- **Category**: correctness
- **Weight**: essential
- **Text**: The output identifies every state mutation triggered by the action: local component
  state (`useState`, `this.setState`), context state, and store state (Redux, Zustand, Pinia,
  etc.). For each mutation: the state key, old value shape, new value shape, and the component or
  store that owns it.
- **Pass condition**: At least one concrete state mutation is named with its owner. "State updates"
  as a section header with no specifics does not pass. "State changes in response to the action"
  does not pass. "The store is modified" without naming the key or slice does not pass.

### C-04 · Re-render Inventory
- **Category**: correctness
- **Weight**: essential
- **Text**: The output lists which components re-render as a result of the state changes, explaining
  why each one re-renders (owns the state, subscribes to context, receives new props, etc.).
- **Pass condition**: At least one component is listed with its re-render cause. "Several components
  re-render" without naming them does not pass. "Components re-render as expected" without naming
  them does not pass.

### C-05 · Final UI State
- **Category**: correctness
- **Weight**: essential
- **Text**: The output describes the observable UI state after all synchronous effects and at least
  one async settle point (e.g., after a loading state resolves). This is the "what the user sees"
  close to the trace.
- **Pass condition**: A concrete final state is described — visible elements, disabled states, error
  messages, or confirmed no-change. "UI updates accordingly" does not pass. "The UI reflects the
  state changes" does not pass. "Success and error states are handled" without describing what the
  user sees does not pass.

---

## Recommended Criteria (weight: 30 points total)

Output is meaningfully better with these. Missing one is acceptable; missing all three is a gap.

### C-06 · Side Effect Coverage
- **Category**: coverage
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one side effect identified with its mechanism. If none, explicitly
  state "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or
  navigation triggered by this action." Silence does not pass.

### C-07 · Issue Detection
- **Category**: depth
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one issue named with its component or state path, presented in a
  structured FINDINGS table with N/A-prohibited columns. An advisory narrative section with a
  single-block escape path does not pass. "May have performance issues" does not pass.

### C-08 · Framework Vocabulary
- **Category**: behavior
- **Weight**: recommended (10 pts)
- **Pass condition**: At least two framework-specific terms correctly applied in context.

---

## Aspirational Criteria (weight: 36 points total, 2 pts each)

### C-09 · Fix Recommendations
- **Category**: depth
- **Pass condition**: At least one issue has a fix naming a specific API or pattern.

### C-10 · Render Quantification
- **Category**: depth
- **Pass condition**: *(text carried from v6)*

### C-11 through C-19
*(text carried from v6)*

### C-20 · Framework Declaration Gate
- **Category**: behavior
- **Pass condition**: The output includes an explicit framework and state management declaration
  before any phase analysis begins — naming the framework (React, Vue, Angular, etc.) and the
  state management layer (Redux, Pinia, Zustand, NgRx, etc.) as a required output header. A
  pickup instruction without a required output declaration does not pass. Framework inferred
  silently from context does not pass.

### C-21 · Failure Mode Displacement
- **Category**: behavior
- **Pass condition**: The output produces explicit displacement text that names the blocked phrase
  and the required replacement — e.g., "NOT 'state updates' — Owner: CartStore, Key:
  items, Old: [], New: [{id: 1}]". Instruction-level blocking without displacement confirmation
  text in the output does not pass.

### C-22 · Re-render Necessity Annotation
- **Category**: depth
- **Pass condition**: Every component in the re-render inventory carries an explicit necessity
  annotation: necessary (reason: owns state / receives new props / subscribes to changed context)
  or unnecessary (reason: memoization missing / selector too broad / etc.). A re-render list with
  causes but no necessity verdict per component does not pass.

### C-23 · Four-Phase UI Progression
- **Category**: correctness
- **Pass condition**: The final UI state section covers all four phases in order: (1) before the
  action — the baseline state the user started from, (2) immediately after the action fires —
  optimistic or synchronous update, (3) after async resolution — success state, (4) after async
  rejection — error state. A three-phase section that collapses success and error or omits the
  pre-action baseline does not pass.

---

### C-24 · Zero-Mutation Declaration  *(new — R6 excellence signal)*
- **Category**: correctness
- **Pass condition**: When the traced action produces no state mutations, the output includes an
  explicit zero-mutation declaration — naming the reason (read-only operation, display-only
  component, event consumed without store dispatch, etc.) and confirming that no local, context,
  or store state was modified. A missing state section does not pass. Silence does not pass. This
  criterion applies only to traces where no mutations occur; it is N/A otherwise.

### C-25 · Issue Category Completeness  *(new — R6 excellence signal)*
- **Category**: coverage
- **Pass condition**: The findings section explicitly addresses at least three of the following
  issue categories: render performance / unnecessary re-renders / accessibility / async error
  handling / memory leaks. Each category must appear either with a concrete finding or with an
  explicit "none detected — [brief reason]" confirmation. A findings section that lists only
  discovered issues without clearing unchecked categories does not pass.

### C-26 · Unnecessary Re-render Promotion  *(new — R6 excellence signal)*
- **Category**: depth
- **Pass condition**: Every re-render annotated as unnecessary in the re-render inventory (C-22)
  appears in the findings section, referenced by component name, with a named fix — a specific
  API or pattern (e.g., `React.memo`, `createSelector`, `computed` with stable deps). If the
  re-render inventory contains no unnecessary re-renders, the findings section includes an
  explicit statement to that effect. A findings section that omits the cross-link from inventory
  to fix does not pass.
```
