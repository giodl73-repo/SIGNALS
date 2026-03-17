Reading the scorecard findings to extract the new patterns before writing.

The two new patterns from R3 are:

1. **Gate family completeness requires FINDINGS coverage** — phase gates intercept escape strings during trace phases, but the closing FINDINGS/consolidation section is an unguarded gap where "no impact" and "low risk" survive without a dedicated FINDINGS gate.

2. **Triple structural lock** — mandatory column + column-header instruction + per-row exact-phrase gate are three independent mechanisms; each catches what the others miss. Having only one or two leaves enforcement gaps.

These become **C-16** and **C-17**. Here is the complete v4 rubric:

---

# Rubric: trace-component (v4)

**17 criteria across 3 tiers:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-17 | 18 |

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

## Aspirational Criteria (weight: 18 points total, 2 pts each)

### C-09 · Fix Recommendations
- **Category**: depth
- **Pass condition**: At least one issue has a fix naming a specific API or pattern.

### C-10 · Render Quantification
- **Category**: depth
- **Pass condition**: At least one component has a numeric render annotation AND verdict co-located in the same table row or sentence. Separation into two columns or two sections does not satisfy.

### C-11 · Inline Phase-Close Gates
- **Category**: structure
- **Pass condition**: At least three trace phases each end with an explicit gate statement naming exact phrases that do not close the phase.

### C-12 · Mandatory Comparison Column
- **Category**: structure
- **Pass condition**: At least one table includes a "What this adds vs. ad-hoc" or equivalent comparison column that is populated for every row.

### C-13 · Exact-Phrase Gate Family
- **Category**: structure
- **Pass condition**: The phase gate set intercepts at least three distinct escape strings across multiple phases (not just one phase). Generic intercepts like "no impact", "minor issue", and "low risk" each appear as named non-closers in at least one gate.

### C-14 · Column-Header Escape Instruction
- **Category**: structure
- **Pass condition**: At least one mandatory column embeds its fill constraint in the column header itself (e.g., "Verdict [justified/unnecessary/0×]"), providing enforcement at cell-write time independent of surrounding prose instructions.

### C-15 · Do-Nothing Cost
- **Category**: depth
- **Pass condition**: At least one finding quantifies the cost or risk of leaving the issue unaddressed, not merely describing the issue itself.

### C-16 · FINDINGS Section Gate
- **Category**: structure
- **Pass condition**: The closing FINDINGS or consolidation section has its own explicit gate intercepting at least two phrases that summarize-away rather than enumerate issues — specifically strings such as "no impact", "minor issue", "low risk", or "no concerns found". Phase-only gates do not satisfy this criterion; the FINDINGS section itself must carry the gate so that escape strings that survive trace phases are intercepted at consolidation.

### C-17 · Triple Structural Lock
- **Category**: structure
- **Pass condition**: At least one mandatory column is enforced by all three independent mechanisms simultaneously: (1) the column is present in the template and marked mandatory, (2) the column header embeds the constraint instruction (satisfying C-14), and (3) a per-row exact-phrase gate names the specific strings a model produces when it clears the first two mechanisms without substantive content. Having only one or two of the three mechanisms does not pass — the lock is only complete when all three are co-present.

---

## Scoring Summary

| Tier | Max Points |
|------|-----------|
| Essential (C-01–C-05) | 60 |
| Recommended (C-06–C-08) | 30 |
| Aspirational (C-09–C-17) | 18 |
| **Total** | **108** |

Failing any essential criterion → output fails regardless of composite score.
