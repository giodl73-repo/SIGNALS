Written to `simulations/quest/rubrics/trace-component-rubric-v9-2026-03-14.md`.

---

# Rubric: trace-component (v9)

**32 criteria across 3 tiers — 3 new aspirational criteria added from R8 excellence signals:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-32 | 48 |

**Ceiling: 138 pts** (up from 132; 3 new criteria x 2 pts each)

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. Failing any one essential criterion fails the entire output regardless of composite score.

### C-01 . Event Anchor
- **Category**: correctness
- **Weight**: essential
- **Text**: The output names the exact event that triggered the trace: the event type (click, submit, input, etc.), the specific UI component that fired it (not a generic description like "the button"), the event payload or input value if relevant, and the handler function or lifecycle hook that received it.
- **Pass condition**: The event type, the exact component name, and the handler function are all named. "The button fires a click event" without naming the handler does not pass. "The input" without naming the component does not pass.

### C-02 . Component Tree Traversal
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces the path of the action through the component hierarchy -- from the event-receiving leaf up through handlers, context providers, or HOCs to the root of the affected subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with a clear parent->child or handler->provider direction. A flat list of components with no structural relationship does not pass.

### C-03 . State Update Map
- **Category**: correctness
- **Weight**: essential
- **Text**: The output identifies every state mutation triggered by the action: local component state (useState, this.setState), context state, and store state (Redux, Zustand, Pinia, etc.). For each mutation: the state key, old value shape, new value shape, and the component or store that owns it.
- **Pass condition**: At least one concrete state mutation is named with its owner. "State updates" as a section header with no specifics does not pass. "State changes in response to the action" does not pass. "The store is modified" without naming the key or slice does not pass.

### C-04 . Re-render Inventory
- **Category**: correctness
- **Weight**: essential
- **Text**: The output lists which components re-render as a result of the state changes, explaining why each one re-renders (owns the state, subscribes to context, receives new props, etc.).
- **Pass condition**: At least one component is listed with its re-render cause. "Several components re-render" without naming them does not pass. "Components re-render as expected" without naming them does not pass.

### C-05 . Final UI State
- **Category**: correctness
- **Weight**: essential
- **Text**: The output describes the observable UI state after all synchronous effects and at least one async settle point (e.g., after a loading state resolves). This is the "what the user sees" close to the trace.
- **Pass condition**: A concrete final state is described -- visible elements, disabled states, error messages, or confirmed no-change. "UI updates accordingly" does not pass. "The UI reflects the state changes" does not pass. "Success and error states are handled" without describing what the user sees does not pass.

---

## Recommended Criteria (weight: 30 points total)

Output is meaningfully better with these. Missing one is acceptable; missing all three is a gap.

### C-06 . Side Effect Coverage
- **Category**: coverage
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one side effect identified with its mechanism. If none, explicitly state "No side effects -- confirmed synchronous: no API calls, timers, subscriptions, or navigation triggered by this action." Silence does not pass.

### C-07 . Issue Detection
- **Category**: depth
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one issue named with its component or state path, presented in a structured FINDINGS table with N/A-prohibited columns. An advisory narrative section with a single-block escape path does not pass. "May have performance issues" does not pass.

### C-08 . Framework Vocabulary
- **Category**: behavior
- **Weight**: recommended (10 pts)
- **Pass condition**: At least two framework-specific terms correctly applied in context.

---

## Aspirational Criteria (weight: 48 points total, 2 pts each)

### C-09 . Fix Recommendations
- **Category**: depth
- **Pass condition**: At least one issue has a fix naming a specific API or pattern.

### C-10 . Render Quantification
- **Category**: depth
- **Pass condition**: *(text carried from v6)*

### C-11 through C-19
*(text carried from v6)*

### C-20 . Framework Declaration Gate
- **Category**: behavior
- **Pass condition**: The output includes an explicit framework and state management declaration before any phase analysis begins -- naming the framework (React, Vue, Angular, etc.) and the state management layer (Redux, Pinia, Zustand, NgRx, etc.) as a required output header. A pickup instruction without a required output declaration does not pass. Framework inferred silently from context does not pass.

### C-21 . Failure Mode Displacement
- **Category**: behavior
- **Pass condition**: The output produces explicit displacement text that names the blocked phrase and the required replacement -- e.g., "NOT 'state updates' -- Owner: CartStore, Key: items, Old: [], New: [{id: 1}]". Instruction-level blocking without displacement confirmation text in the output does not pass.

### C-22 . Re-render Necessity Annotation
- **Category**: depth
- **Pass condition**: Every component in the re-render inventory carries an explicit necessity annotation: necessary (reason: owns state / receives new props / subscribes to changed context) or unnecessary (reason: memoization missing / selector too broad / etc.). A re-render list with causes but no necessity verdict per component does not pass.

### C-23 . Four-Phase UI Progression
- **Category**: correctness
- **Pass condition**: The final UI state section covers all four phases in order: (1) before the action -- the baseline state the user started from, (2) immediately after the action fires -- optimistic or synchronous update, (3) after async resolution -- success state, (4) after async rejection -- error state. A three-phase section that collapses success and error or omits the pre-action baseline does not pass.

### C-24 . Zero-Mutation Declaration *(new -- R6 excellence signal)*
- **Category**: correctness
- **Pass condition**: When the traced action produces no state mutations, the output includes an explicit zero-mutation declaration -- naming the reason (read-only operation, display-only component, event consumed without store dispatch, etc.) and confirming that no local, context, or store state was modified. A missing state section does not pass. Silence does not pass. This criterion applies only to traces where no mutations occur; it is N/A otherwise.

### C-25 . Issue Category Completeness *(new -- R6 excellence signal)*
- **Category**: coverage
- **Pass condition**: The findings section explicitly addresses at least three of the following issue categories: render performance / unnecessary re-renders / accessibility / async error handling / memory leaks. Each category must appear either with a concrete finding or with an explicit "none detected -- [brief reason]" confirmation. A findings section that lists only discovered issues without clearing unchecked categories does not pass.

### C-26 . Unnecessary Re-render Promotion *(new -- R6 excellence signal)*
- **Category**: depth
- **Pass condition**: Every re-render annotated as unnecessary in the re-render inventory (C-22) appears in the findings section, referenced by component name, with a named fix -- a specific API or pattern (e.g., React.memo, createSelector, computed with stable deps). If the re-render inventory contains no unnecessary re-renders, the findings section includes an explicit statement to that effect. A findings section that omits the cross-link from inventory to fix does not pass.

### C-27 . Mutation Count Pre-Declaration *(new -- R7 excellence signal)*
- **Category**: correctness
- **Pass condition**: Before the state mutation table or section, the output declares the total count of state mutations produced by the action -- e.g., "Mutation count: N=3" or "State mutations: 0." For N=0 this declaration serves as the structural gate leading into C-24. For N>0 the declared count must match the number of mutations enumerated; a count that does not match the table row count does not pass. Omitting the pre-declaration and proceeding directly to the table does not pass.

### C-28 . Per-Hop Direction Annotation *(new -- R7 excellence signal)*
- **Category**: correctness
- **Pass condition**: Each hop in the component tree traversal carries an explicit direction annotation indicating the flow of the event or data at that hop -- upward propagation, downward prop-passing, event delegation, or context injection. C-02 requires that traversal direction be shown; this criterion requires the annotation to appear per hop, not once as a summary statement. A traversal that names components and shows overall direction but does not annotate each hop individually does not pass.

### C-29 . Re-render Inventory Completeness by Traversal *(new -- R7 excellence signal)*
- **Category**: correctness
- **Pass condition**: Every component named in the component tree traversal (C-02) must appear in the re-render inventory (C-04) with a verdict -- either a re-render verdict (re-renders -- reason: owns state / receives new props / etc.) or a non-render verdict (does not re-render -- reason: no state owned, no props changed, not subscribed to changed context, etc.). C-04 requires "at least one component with its re-render cause"; this criterion requires traversal-complete accounting so no traversal component is silently dropped. A re-render inventory that names fewer components than the traversal without explicit non-render verdicts for the missing ones does not pass.

---

### C-30 . Mutation Count Dual-Track (Direct + Inherited) *(new -- R8 excellence signal)*
- **Category**: correctness
- **Pass condition**: The mutation pre-declaration (C-27) distinguishes direct mutations -- state writes the action produces immediately -- from inherited mutations -- state writes triggered transitively through subscriptions, effects, computed properties, or watchers. Format: "Mutations: N=X direct, M=Y inherited" (or equivalent labeling) embedded in the existing mutation table header or pre-declaration line. A single-value count that conflates direct and inherited mutations does not pass. A separate sub-table introduced solely to separate the two counts does not pass -- the dual count must be absorbed into the existing mutation table structure without structural proliferation.

### C-31 . Schema-Field Coverage of Aspirational Criteria *(new -- R8 excellence signal)*
- **Category**: behavior
- **Pass condition**: Every structural element required by C-20 through C-29 is surfaced in the output as a schema-enforced field -- a named table column, a required row with fixed column headers, or a required cell that cannot be left blank -- rather than as a prose statement or advisory instruction alone. For each criterion in C-20 through C-29, there must be a corresponding field in the output's table structure that makes omission structurally visible. An output where all of C-20 through C-29 is satisfied through prose sections without table-column enforcement does not pass. An output where at least 7 of the 10 criteria map to specific schema fields passes; fewer than 5 does not pass.

### C-32 . Blank-Blocked Field Primacy *(new -- R8 excellence signal)*
- **Category**: behavior
- **Pass condition**: The output's primary enforcement mechanism for the five essential criteria (C-01 through C-05) is schema-field prevention -- table columns or required rows that cannot be left blank -- rather than prose narration, advisory instructions, or post-hoc auditor verification. Each of C-01 through C-05 must be satisfiable by reading a specific table cell or required row in the output, not only by reading the prose. An output that satisfies C-01 through C-05 entirely through narrative paragraphs without any corresponding schema field does not pass. An output where at least three of the five essential criteria are backed by blank-blocked schema fields passes; fewer than three does not pass.

---

**Three new criteria -- rationale:**

| Criterion | Source pattern | What v8 covered | What v9 adds |
|-----------|---------------|-----------------|--------------|
| C-30 | R8: V-05 N+M dual mutation count is a stronger C-27 implementation than V-01 single N, but separate TABLE 3b costs 2 aspirational pts | C-27 requires a pre-declaration count N | Requires the count to distinguish direct (N) from inherited (M) mutations, embedded in the existing table without adding a separate sub-table |
| C-31 | R8: Excellence-signal-to-criteria-to-field pipeline closes automatically -- V-01 schema satisfied new criteria at zero revision cost because its schema fields were already the source of the signals | C-20 through C-29 each specify a required output element | Requires those elements to be schema-enforced fields (table columns/rows) not prose-only, so future criteria promotions are automatically satisfied |
| C-32 | R8: Prevention beats detection beats instruction -- blank-blocked schema fields (38/42) > blocking exit conditions (35/42) > auditor verification (34/42) > prose instruction (19/42), ~3-4 pt gap per tier | No criterion rewarded the enforcement mechanism itself | Requires the five essential criteria to be backed by blank-blocked schema fields not prose narration alone, explicitly rewarding prevention-first structure |

---

The three R8 patterns promote cleanly:

- **C-30** captures the V-05 N+M insight: split direct from inherited in the mutation pre-declaration but absorb it into the existing table header, no sub-table. The constraint "no separate TABLE 3b" prevents the proliferation penalty that cost V-05 two points.

- **C-31** closes the pipeline loop: because V-01's schema was the source of both R7's excellence signals and R8's new criteria, any variation whose schema fields already satisfy C-20–C-29 will satisfy C-31 at zero revision cost. The pipeline self-reinforces.

- **C-32** makes the enforcement hierarchy a first-class criterion: blank-blocked fields for essentials is now a graded requirement, not just an observed correlation. A variation that scores high on C-31 (schema fields for aspirational) but narrates the essentials in prose is now explicitly penalized.
