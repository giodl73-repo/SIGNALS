# Rubric: trace-component (v6)

**23 criteria across 3 tiers — 4 new aspirational criteria added from R5 excellence signals:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-23 | 30 |

**Ceiling: 120 pts** (up from 112; 4 new criteria × 2 pts each)

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. Failing any one essential criterion fails the entire output regardless of composite score.

### C-01 · Event Anchor
- **Category**: correctness
- **Weight**: essential
- **Text**: The output names the exact event that triggered the trace: the event type (click, submit, input, etc.), the specific UI component that fired it (not a generic description like "the button"), the event payload or input value if relevant, and the handler function or lifecycle hook that received it.
- **Pass condition**: The event type, the exact component name, and the handler function are all named. "The button fires a click event" without naming the handler does not pass. "The input" without naming the component does not pass.

### C-02 · Component Tree Traversal
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces the path of the action through the component hierarchy — from the event-receiving leaf up through handlers, context providers, or HOCs to the root of the affected subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with a clear parent→child or handler→provider direction. A flat list of components with no structural relationship does not pass.

### C-03 · State Update Map
- **Category**: correctness
- **Weight**: essential
- **Text**: The output identifies every state mutation triggered by the action: local component state (`useState`, `this.setState`), context state, and store state (Redux, Zustand, Pinia, etc.). For each mutation: the state key, old value shape, new value shape, and the component or store that owns it.
- **Pass condition**: At least one concrete state mutation is named with its owner. "State updates" as a section header with no specifics does not pass. "State changes in response to the action" does not pass. "The store is modified" without naming the key or slice does not pass.

### C-04 · Re-render Inventory
- **Category**: correctness
- **Weight**: essential
- **Text**: The output lists which components re-render as a result of the state changes, explaining why each one re-renders (owns the state, subscribes to context, receives new props, etc.).
- **Pass condition**: At least one component is listed with its re-render cause. "Several components re-render" without naming them does not pass. "Components re-render as expected" without naming them does not pass.

### C-05 · Final UI State
- **Category**: correctness
- **Weight**: essential
- **Text**: The output describes the observable UI state after all synchronous effects and at least one async settle point (e.g., after a loading state resolves). This is the "what the user sees" close to the trace.
- **Pass condition**: A concrete final state is described — visible elements, disabled states, error messages, or confirmed no-change. "UI updates accordingly" does not pass. "The UI reflects the state changes" does not pass. "Success and error states are handled" without describing what the user sees does not pass.

---

## Recommended Criteria (weight: 30 points total)

Output is meaningfully better with these. Missing one is acceptable; missing all three is a gap.

### C-06 · Side Effect Coverage
- **Category**: coverage
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one side effect identified with its mechanism. If none, explicitly state "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation triggered by this action." Silence does not pass.

### C-07 · Issue Detection
- **Category**: depth
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one issue named with its component or state path, presented in a structured FINDINGS table with N/A-prohibited columns. An advisory narrative section with a single-block escape path does not pass. "May have performance issues" does not pass.

### C-08 · Framework Vocabulary
- **Category**: behavior
- **Weight**: recommended (10 pts)
- **Pass condition**: At least two framework-specific terms correctly applied in context.

---

## Aspirational Criteria (weight: 30 points total, 2 pts each)

### C-09 · Fix Recommendations
- **Category**: depth
- **Pass condition**: At least one issue has a fix naming a specific API or pattern.

### C-10 · Render Quantification
- **Category**: depth
- **Pass condition**: *(text carried from v5)*

### C-11 · Prop Drill Detection
- **Category**: coverage
- **Pass condition**: *(text carried from v5)*

### C-12 · Memoization Audit
- **Category**: depth
- **Pass condition**: *(text carried from v5)*

### C-13 · Async Boundary Tracing
- **Category**: correctness
- **Pass condition**: *(text carried from v5)*

### C-14 · Context Scope Annotation
- **Category**: coverage
- **Pass condition**: *(text carried from v5)*

### C-15 · Lifecycle Hook Coverage
- **Category**: correctness
- **Pass condition**: *(text carried from v5)*

### C-16 · Error Boundary Awareness
- **Category**: coverage
- **Pass condition**: *(text carried from v5)*

### C-17 · Selector Specificity
- **Category**: depth
- **Pass condition**: *(text carried from v5)*

### C-18 · Derived State Identification
- **Category**: correctness
- **Pass condition**: *(text carried from v5)*

### C-19 · Subscription Cleanup
- **Category**: coverage
- **Pass condition**: *(text carried from v5)*

---

### C-20 · Framework Declaration Gate *(new — R5 V-01, signal 1)*
- **Category**: behavior
- **Source**: V-01 Step 0 gate pattern — framework + state-layer declaration before any trace section eliminates vocabulary drift
- **Pass condition**: The trace opens with an explicit declaration of the target framework (e.g., React, Vue 3, Angular) and the state management layer(s) in use (e.g., `useState`, `Pinia`, `NgRx`, Redux Toolkit) before any section analysis begins. Framework identification deferred to mid-trace does not pass. Omitting the declaration entirely does not pass.

### C-21 · Failure Mode Displacement *(new — R5 V-01, signal 2)*
- **Category**: precision
- **Source**: V-01 per-section failure mode callout — each section names the escape phrase it is replacing with specific evidence
- **Pass condition**: At least two sections include explicit confirmation that a known generic escape path was not taken, naming the disqualified phrase and substituting concrete specifics (e.g., not "state updates" — Owner: CartStore, Key: `items[]`, Before: `[3]`, After: `[4]`). No such displacement anywhere in the output does not pass.

### C-22 · Re-render Necessity Annotation *(new — R5 V-02, signal 3)*
- **Category**: depth
- **Source**: V-02 TABLE 4 Necessary? column — unnecessary re-renders auto-promoted to FINDINGS without a separate analysis step
- **Pass condition**: The re-render inventory annotates each listed component as necessary or unnecessary. Any component marked unnecessary is cross-linked to or promoted into the FINDINGS section. An inventory that lists re-renders without necessity judgment does not pass. An inventory that marks a component unnecessary but does not surface it as a finding does not pass.

### C-23 · Four-Phase UI Progression *(new — R5 V-02, signal 4)*
- **Category**: coverage
- **Source**: V-02 TABLE 6 — Before / During / After success / After error as explicit phases forces error-path coverage
- **Pass condition**: The final UI state section addresses all four phases explicitly: Before (baseline state), During (loading or in-progress state), After success, and After error. Omitting the error-path phase does not pass. "Error state handled" without describing what the user sees does not pass. A two-state (before/after) description without loading and error phases does not pass.

---

## Version History

| Version | Criteria | Ceiling | Change |
|---------|----------|---------|--------|
| v1 | 8 | 60 | Initial |
| v2–v4 | *(incremental)* | *(incremental)* | *(incremental)* |
| v5 | 19 | 112 | Added C-18, C-19 from R4 patterns; aspirational 11 × 2 = 22 pts |
| **v6** | **23** | **120** | Added C-20–C-23 from R5 excellence signals; aspirational 15 × 2 = 30 pts |
