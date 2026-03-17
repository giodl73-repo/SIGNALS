# trace-component Variations R5 — V-01 through V-05

---

## V-01 · Single-axis: Role Sequence
**Axis**: Framework detection runs before expert persona is assumed — model names its own role after reading context.
**Hypothesis**: Forcing explicit framework identification before assigning the reviewer persona increases correct use of framework-specific vocabulary (C-08) and reduces generic "state updates" language in C-03.

---

```
You are about to trace a user action through a frontend component system.

**Step 0 — Framework Declaration (required before all else)**

Read the code or description provided. State:
- Framework: [React / Vue / Angular / Svelte / other — name it]
- State management layer: [useState / Redux / Pinia / NgRx / Zustand / stores / signals — name it]
- Your role: You are a [framework]-specialized frontend engineer. All vocabulary,
  patterns, and APIs you name must be idiomatic to that framework.

Do not proceed until you have completed Step 0.

---

**Your task**: Trace the following user action through the full component lifecycle.

[INSERT: action description, component code, or feature spec]

---

**Trace Output — required sections in order:**

### 1. Event Anchor
Name: the exact event type (click / submit / input / keydown / etc.), the exact component
that fired it (use its actual component name from the code), the event payload or input
value, and the handler function or lifecycle hook that received it.

Failure mode to avoid: "The button fires a click event" with no handler named is
incomplete. "The input field" with no component name is incomplete.

### 2. Component Tree Traversal
Trace the call path from the event-receiving component upward through handlers, providers,
HOCs, or composables to the root of the affected subtree. Show each hop as:

  ComponentA (event source)
    → ComponentB (passes via prop / calls handler)
      → ComponentC (owns state / provides context)

At minimum two named components must appear with explicit directional relationship.

### 3. State Update Map
For every state mutation triggered: name the state owner (component, store, context),
the state key or slice, the value shape before, and the value shape after.

Format each mutation as:
  Owner: [component or store name]
  Key: [state key / slice]
  Before: [value or shape]
  After: [value or shape]

"State updates" without specifics does not satisfy this section.

### 4. Re-render Inventory
List every component that re-renders. For each, state why it re-renders:
  - owns the mutated state
  - subscribes to the updated context
  - receives new props from a re-rendering parent
  - selector matches updated slice

"Several components re-render" without naming them does not satisfy this section.

### 5. Side Effects
List every side effect the action triggers: API calls (name the endpoint or function),
timers, subscriptions, router navigation, analytics events.

If none: write exactly — "No side effects — confirmed synchronous: no API calls, timers,
subscriptions, or navigation triggered by this action."

Silence does not satisfy this section.

### 6. Final UI State
Describe what the user sees after all synchronous effects complete and after the first
async settle point (e.g., after a loading state resolves or an error appears). Name
visible elements, disabled states, error messages, or confirmed no-change.

"UI updates accordingly" does not satisfy this section.

### 7. FINDINGS
Produce a table. If no issues found, the table must still appear with zero rows and
a note explaining why.

| # | Component / State Path | Issue Type | Severity | Evidence |
|---|------------------------|------------|----------|----------|

Issue types: UnnecessaryReRender · MissingLoadingState · ErrorStateGap ·
AccessibilityFailure · PropDrilling · StaleClosureRisk · MemoryLeak

Severity: Critical · High · Medium · Low

An advisory narrative in place of this table does not satisfy this section.

### 8. Fix Recommendations (if FINDINGS has rows)
For each finding: name the specific API, pattern, or framework primitive that fixes it.
Example: "Wrap with React.memo — prevents re-render when props are shallowly equal."
```

---

## V-02 · Single-axis: Output Format
**Axis**: Tables dominate every section — even traversal and state maps are tabular.
**Hypothesis**: A fully tabular format eliminates narrative escape paths that allow vague language (C-03, C-04, C-05) — every cell is a discrete claim that can be audited against pass/fail criteria.

---

```
You are a frontend domain expert. Detect the framework from the provided code or context
and apply its idiomatic vocabulary throughout.

Trace the following user action end-to-end.

[INSERT: action description, component code, or feature spec]

Produce your trace as a sequence of tables. Prose between tables is allowed only for
explanations that cannot be expressed in a row. Do not use prose as a substitute for
a table.

---

**TABLE 1 — Event Anchor**

| Field | Value |
|-------|-------|
| Event Type | [click / submit / input / keydown / etc.] |
| Firing Component | [exact component name] |
| Input Payload | [value, key, or "void"] |
| Handler / Hook | [exact function name] |

All four cells must be filled. "N/A" is not permitted here.

---

**TABLE 2 — Component Tree Traversal**

| Hop | Component | Role in Path |
|-----|-----------|--------------|
| 1 | [event source component] | fires event |
| 2 | [next component] | [passes prop / calls handler / provides context] |
| … | … | … |

Continue until you reach the component that owns the affected state or context root.
Minimum two hops. "Component tree updates" is not a row.

---

**TABLE 3 — State Update Map**

| Owner | State Key / Slice | Before (shape or value) | After (shape or value) |
|-------|-------------------|-------------------------|------------------------|
| [component or store] | [key] | [shape] | [shape] |

One row per mutation. "State changes" is not a row. Empty table requires a note:
"No state mutations — confirmed: [reason]."

---

**TABLE 4 — Re-render Inventory**

| Component | Re-render Cause | Necessary? |
|-----------|-----------------|------------|
| [component] | [owns state / context subscriber / new props / selector match] | Yes / No |

"Several components" is not a row. Every re-render must be named. Mark unnecessary
re-renders No — these become FINDINGS candidates.

---

**TABLE 5 — Side Effects**

| Effect Type | Target | Trigger Point | Async? |
|-------------|--------|---------------|--------|
| [API call / timer / subscription / navigation / analytics] | [endpoint or function] | [component or hook] | Yes / No |

If no side effects: one row — "None · Confirmed synchronous: no API calls, timers,
subscriptions, or navigation."

---

**TABLE 6 — UI State Progression**

| Phase | What the User Sees |
|-------|--------------------|
| Before action | [visible elements, enabled/disabled states] |
| During (loading) | [loading indicator, disabled submit, skeleton — or "no async, skip"] |
| After success | [confirmed visible outcome] |
| After error | [error message, recovery affordance — or "no error path, confirmed"] |

"UI updates accordingly" is not a cell value.

---

**TABLE 7 — FINDINGS**

| # | Component / State Path | Issue Type | Severity | Evidence |
|---|------------------------|------------|----------|----------|

Issue types: UnnecessaryReRender · MissingLoadingState · ErrorStateGap ·
AccessibilityFailure · PropDrilling · StaleClosureRisk · MemoryLeak

Severity: Critical · High · Medium · Low

Zero rows requires a note: "No issues detected — [brief rationale]."

---

**TABLE 8 — Fix Recommendations**

| Finding # | Fix | API / Pattern |
|-----------|-----|---------------|
| [#] | [what to change] | [specific API: React.memo, useCallback, aria-live, etc.] |

Omit this table only if TABLE 7 has zero rows.
```

---

## V-03 · Single-axis: Lifecycle Emphasis
**Axis**: Each lifecycle phase gets an explicit named section with mandatory boundary conditions — the model cannot skip a phase or collapse two phases into one.
**Hypothesis**: Explicit phase enforcement with boundary declarations prevents the most common failure modes: collapsing traversal+state into one vague paragraph, or omitting the loading state phase.

---

```
You are a frontend domain expert. From the provided code or context, identify the
framework and state layer before beginning the trace.

Framework detected: [fill this in]
State layer detected: [fill this in]

Trace the following user action through six lifecycle phases. Each phase is mandatory.
You may not skip a phase or merge two phases. If a phase has nothing to report, you
must write the explicit null declaration for that phase.

[INSERT: action description, component code, or feature spec]

---

## PHASE 1 · TRIGGER
*Boundary: begins at user gesture, ends at handler invocation*

What the user did. The exact event type emitted. The exact component that emitted it
(use the component name from the code — not "the button", not "the form"). The exact
handler function or lifecycle hook that received the event. The event payload or input
value if relevant.

Required: event type + component name + handler name. All three. Missing any one of
these fails this phase.

---

## PHASE 2 · TRAVERSE
*Boundary: begins at handler invocation, ends at first state write*

The call path from the event handler through the component tree: which components
are traversed, in what order, and what each one does (pass the event up, invoke a
context method, dispatch to a store, call a composable, etc.).

Required: at least two named components shown in structural order (parent→child or
handler→provider direction). A flat list with no direction fails this phase.

---

## PHASE 3 · MUTATE
*Boundary: begins at first state write, ends when all synchronous state changes settle*

Every state change that occurs: name the owner (component, context, store), the key
or slice, the before-shape, and the after-shape. If multiple stores or contexts are
touched, list each one separately.

Null declaration (use only if truly no state changes):
"No state mutations — confirmed: this action triggers only [effect type] with no
local or global state writes."

Required: at least one concrete mutation with owner + key + before/after.
"State is updated" without specifics fails this phase.

---

## PHASE 4 · RENDER
*Boundary: begins after state settles, ends after all synchronous re-renders complete*

Every component that re-renders: name it, explain why it re-renders (owns the state,
subscribes to context, receives new props, matches selector), and note whether the
re-render is necessary or can be prevented.

Null declaration (only if no re-renders occur):
"No re-renders — confirmed: state write did not trigger any subscribed component."

Required: at least one named component with its re-render cause.
"Components re-render as expected" fails this phase.

---

## PHASE 5 · SETTLE
*Boundary: begins at first async suspension point, ends at final UI state observable to user*

What happens asynchronously: the API call or async operation triggered, its endpoint
or function name, the loading state the user sees while waiting, the success state
the user sees after resolution, and the error state the user sees on failure.

Null declaration (use only if no async behavior):
"No async settle phase — confirmed synchronous: no API calls, timers, subscriptions,
or navigation triggered. Final UI state is the same as end of PHASE 4."

Required: if async exists, name the operation + describe all three user-visible states
(loading / success / error). "Success and error states are handled" fails this phase.

---

## PHASE 6 · DIAGNOSE
*Boundary: begins after full trace is complete; this phase does not modify the trace*

Produce a FINDINGS table reviewing the complete trace for issues. Evaluate every
re-render in PHASE 4 for necessity. Check PHASE 5 for missing loading/error coverage.
Check PHASE 2 for accessibility gaps on the triggering component.

| # | Component / State Path | Issue Type | Severity | Evidence |
|---|------------------------|------------|----------|----------|

Issue types: UnnecessaryReRender · MissingLoadingState · ErrorStateGap ·
AccessibilityFailure · PropDrilling · StaleClosureRisk · MemoryLeak

Zero rows requires: "No issues detected — [one sentence rationale referencing
specific phase evidence]."

For each row with Severity Critical or High, add a fix recommendation naming the
specific API or pattern: React.memo, useCallback, useMemo, aria-live, ErrorBoundary,
Vue's shallowRef, Angular's OnPush, etc.
```

---

## V-04 · Single-axis: Phrasing Register
**Axis**: Conversational, direct "you" address with imperative instructions — no role-playing framing, no "your task is."
**Hypothesis**: Removing role scaffolding and meta-commentary framing reduces the model's tendency to describe what it is about to do instead of doing it, increasing trace density and reducing escape phrases like "UI updates accordingly."

---

```
Trace this user action through the component system. Detect the framework from context.
Do the work — don't narrate the approach.

[INSERT: action description, component code, or feature spec]

---

**Event anchor first.**

Name the event type. Name the exact component that fired it — use its actual name from
the code. Name the handler function. Name the payload or input value if there is one.

Don't write "The button fires a click event." Write "SubmitButton fires onClick →
handleFormSubmit(event) with payload {email: value}."

---

**Walk the tree.**

Start at the event source. Move up through handlers, providers, HOCs, composables.
Name every component you pass through and what it does at each hop. Keep going until
you reach the component that owns the state being changed.

Show direction. Don't list components — connect them:
  SubmitButton → FormContainer → AuthProvider

---

**Map every state change.**

For each state mutation: who owns it, what key or slice changed, what it was before,
what it is now.

Be specific. Don't write "loading state is set to true." Write:
  AuthProvider.state.loading: false → true
  userStore.currentUser: null → {id, email}

If nothing changes: say so explicitly and say why.

---

**Name every re-render.**

For each component that re-renders: name it, say why (owns the state / context
subscriber / new props / selector). Say whether it needed to re-render.

Don't write "several components re-render." Write:
  LoginForm re-renders — owns AuthProvider context (loading changed)
  NavBar re-renders — subscribes to userStore.currentUser
  Sidebar re-renders — receives user prop from NavBar [unnecessary]

---

**Cover side effects.**

Every API call, timer, subscription, and navigation event triggered. Name the function
or endpoint. Note whether it's async.

If there are none: "No side effects — confirmed synchronous: no API calls, timers,
subscriptions, or navigation."

---

**Close with what the user sees.**

Loading state: what's on screen while waiting.
Success state: what the user sees after it resolves.
Error state: what the user sees if it fails.

Don't write "the UI reflects the state changes." Write what is literally visible —
which elements appear, which disappear, which become enabled or disabled, what text
changes.

---

**FINDINGS table.**

| # | Component / State Path | Issue Type | Severity | Evidence |
|---|------------------------|------------|----------|----------|

Issue types: UnnecessaryReRender · MissingLoadingState · ErrorStateGap ·
AccessibilityFailure · PropDrilling · StaleClosureRisk · MemoryLeak

Severity: Critical · High · Medium · Low

Zero rows is fine — but write zero rows in the table, not "no issues found" in prose.

For any Critical or High finding: name the fix. Name the specific API.
"Use memoization" doesn't count. "Wrap LoginForm in React.memo — prevents re-render
when AuthProvider.user reference is stable" counts.
```

---

## V-05 · Combined: Role Sequence + Tables + Lifecycle Phases
**Axes**: Framework detection before role assumption (V-01) + table-dominant format (V-02) + explicit lifecycle phase headers (V-03).
**Hypothesis**: Combining framework-first role assignment with tabular output and mandatory phase boundaries produces the highest simultaneous pass rate on C-01 through C-07 by preventing three independent failure modes at once: vocabulary mismatch (C-08), narrative escape paths (C-03/C-04/C-05), and phase elision (C-06).

---

```
**Step 0 — Identify before tracing (required)**

Read the provided code or context. Fill in:

| Field | Value |
|-------|-------|
| Framework | [React / Vue / Angular / Svelte / other] |
| State layer | [useState / Redux / Pinia / NgRx / Zustand / signals / etc.] |
| Reviewer role | [e.g., "React + Redux senior frontend engineer"] |

Do not proceed to Phase 1 until Step 0 is complete.

---

Trace the following user action. Output each phase as a table. Narrative between
tables is allowed only to explain structural relationships that cannot fit in a cell.

[INSERT: action description, component code, or feature spec]

---

## Phase 1 · TRIGGER

| Field | Value |
|-------|-------|
| Event Type | [exact event name — click, submit, input, keydown, etc.] |
| Firing Component | [exact component name from code] |
| Input Payload | [value, object shape, or "void"] |
| Handler / Hook | [exact function name] |

All four cells required. "N/A" not permitted in this table.

---

## Phase 2 · TRAVERSE

| Hop | Component | Action at This Hop |
|-----|-----------|-------------------|
| 1 | [event source] | fires event, calls [handler] |
| 2 | [next component] | [dispatches / passes prop / invokes context method] |
| … | … | … |

Continue to the component that owns or writes to the state being changed.
Minimum two hops. Direction must be explicit (source → owner).

---

## Phase 3 · MUTATE

| Owner | Key / Slice | Before | After |
|-------|-------------|--------|-------|
| [component or store name] | [key] | [value or shape] | [value or shape] |

One row per mutation. If no mutations occur, one row: "None · [reason — e.g., action
triggers navigation only, no state written]."

---

## Phase 4 · RENDER

| Component | Re-render Cause | Necessary? |
|-----------|-----------------|------------|
| [component name] | [owns state / context subscriber / new props / selector] | Yes / No |

Every No row is a FINDINGS candidate in Phase 6.
If no re-renders: one row — "None · [reason]."

---

## Phase 5 · SETTLE

*Use this table only if the action triggers async behavior.*

| State | User-Visible Outcome |
|-------|----------------------|
| Loading | [what appears on screen — spinner, disabled button, skeleton, etc.] |
| Success | [what the user sees after resolution] |
| Error | [error message, recovery affordance, retry option] |

If no async behavior:
> "No async settle phase — confirmed synchronous: no API calls, timers, subscriptions,
> or navigation triggered by this action."

Do not write this declaration as a table row. Write it as a blockquote beneath the
table header, then omit the table body.

---

## Phase 6 · DIAGNOSE

Review Phase 4 No rows, Phase 5 gaps, and Phase 1 for accessibility on the triggering
element.

| # | Component / State Path | Issue Type | Severity | Evidence |
|---|------------------------|------------|----------|----------|

Issue types: UnnecessaryReRender · MissingLoadingState · ErrorStateGap ·
AccessibilityFailure · PropDrilling · StaleClosureRisk · MemoryLeak

Severity: Critical · High · Medium · Low

Zero rows: write the empty table + one sentence: "No issues detected — [rationale
citing at least one phase observation, e.g., 'all Phase 4 re-renders are necessary
because each component directly owns the mutated slice']."

---

## Phase 7 · FIX

*Omit if Phase 6 has zero rows.*

| Finding # | Component | Fix | Specific API / Pattern |
|-----------|-----------|-----|------------------------|
| [#] | [component] | [what changes] | [e.g., React.memo, Vue shallowRef, NgRx memoized selector, aria-live="polite"] |

"Use memoization" is not a Specific API. "Wrap [ComponentName] in React.memo to
prevent re-render when [prop] reference is stable" is.
```

---

## Summary Table

| Variation | Primary Axis | Key Hypothesis | Rubric Criteria Targeted |
|-----------|--------------|----------------|--------------------------|
| V-01 | Role Sequence | Framework ID before role → better C-08 + C-03 vocabulary | C-01, C-03, C-08 |
| V-02 | Output Format | All-table format eliminates narrative escapes | C-03, C-04, C-05, C-07 |
| V-03 | Lifecycle Emphasis | Explicit phase boundaries prevent phase elision | C-02, C-05, C-06 |
| V-04 | Phrasing Register | Imperative "you" voice reduces meta-narration | C-01, C-04, C-05 |
| V-05 | Combined (V-01+V-02+V-03) | All three failure modes addressed simultaneously | C-01 through C-08 |
