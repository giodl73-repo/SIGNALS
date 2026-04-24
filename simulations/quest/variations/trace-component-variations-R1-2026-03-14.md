Written to `simulations/quest/variations/trace-component-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — trace-component

**5 variations, 3 single-axis + 2 combined:**

| V | Axis | Core mechanism | Key rubric bet |
|---|------|----------------|----------------|
| **V-01** | Role sequence: framework-declaration-first | FRAMEWORK GATE fires before event chain; vocabulary set declared with 3–5 framework-specific terms | C-08 guaranteed before C-01 even begins |
| **V-02** | Output format: pre-printed 7-column event table | Columns map to C-01/event through C-06/UI change; blank cell = visible gap | Structural guarantee for C-02 through C-05 — columns cannot be skipped |
| **V-03** | Phrasing register: imperative | "Name the event. Walk the tree. State the mutation." — 7-step checklist, no formal section headers | Tests whether direct commands drive all 5 essential criteria without scaffolding |
| **V-04** | Lifecycle emphasis: gated phases | 5 discrete phases (ANCHOR / TREE / STATE / RENDERS / FINAL) each with an explicit close condition printed in the template | Prevents collapse failure — C-02 tree must close before C-03 state opens |
| **V-05** | Inertia framing + pre-printed event table | Table carries a pre-printed "What ad-hoc misses" column; standalone INERTIA section establishes the DevTools baseline | C-07 issue detection structurally unavoidable — column cannot say "N/A" |

**Inertia translation:** The status-quo competitor is ad-hoc DevTools inspection — observing rendered output without tracing the subscriber map, component tree path, or async chain. This reliably misses unnecessary re-renders (requires Profiler), missing loading states (async sequence not traced), and accessibility failures (not in Elements panel). V-05 forces the trace to name per-row what DevTools cannot show — structurally identical to scout-feasibility's "Do-nothing cost" column.

**Predicted ceiling:** V-02 and V-04 for essential criterion coverage (table/gates enforce all five). V-05 for C-07 depth if the inertia column surface drives issue identification. V-01 for C-08 framework vocabulary by construction. V-03 is the minimum-structure floor test.
hases cannot be omitted). V-05 is the richer candidate if inertia framing improves C-07 depth. V-01 is the strongest for C-08 framework vocabulary by construction. V-03 is the minimum-structure floor test.

---

## V-01: Framework-Declaration-First Role Sequence

**Axis:** Role sequence — FRAMEWORK GATE executes before the event chain begins; the auto-selected
role declares the detected framework, its vocabulary, and the state management pattern in use; all
downstream event chain entries use that vocabulary
**Hypothesis:** Forcing framework identification into a pre-execution gate guarantees C-08 (framework
vocabulary) is established before C-01 (event anchor) is written, so all five essential trace steps
use correct framework-specific terminology from the start rather than drifting between generic and
framework-specific language mid-trace. The gate also prevents the failure mode where the model
traces a React component tree using Vue vocabulary (or vice versa) because the framework was never
explicitly declared.

```
You are running /trace:component. Fill in this structured template.
Complete the FRAMEWORK GATE before writing any part of the event chain.
Do not begin EVENT CHAIN until all framework fields are filled.

---

## FRAMEWORK GATE

Detect or accept the frontend framework from context. Declare it here before tracing anything.

Framework detected: [React / Vue / Angular / Svelte / Other: ___]
Framework version (if determinable): [e.g., React 18.2, Vue 3.4 — or "not specified"]
State management: [useState/useReducer / Redux / Zustand / Pinia / NgRx / Vuex / none / other: ___]
Rendering model: [Virtual DOM + reconciler / Signals-based / Zone.js change detection / Svelte
  compiler / other: ___]
Role selected: [Frontend domain expert — name the role variant that matches the framework.
  Examples: "React/Redux performance engineer", "Vue 3 Composition API specialist",
  "Angular OnPush change detection expert"]

Framework vocabulary in use (list 3–5 terms that will appear in the trace below):
- [Term 1]: [What it means in this framework — one clause]
- [Term 2]: [What it means in this framework — one clause]
- [Term 3]: [What it means in this framework — one clause]
[Add terms 4–5 if the framework warrants them]

[FRAMEWORK GATE: Do not begin EVENT CHAIN until every field above is filled in.]

---

## SETUP

Surface: [The UI component or page being traced — name it specifically]
User action: [The exact user action — click, keypress, navigation, drag. Name the UI element.]
Expected outcome: [What the user expects to see after the action completes]

---

## EVENT CHAIN

[Use the framework vocabulary declared in the FRAMEWORK GATE throughout this section.
Trace each event in sequence. Number them. Do not skip events — if an event has no handler,
state that explicitly: "No handler registered on [component] for this event."]

Event 1 — [Event type and origin]:
  Trigger: [What fired this event and from which component]
  Component receiving: [Named component — use the exact component name from the codebase or surface]
  Handler: [The handler function or lifecycle hook that processes it. If none: "No handler registered."]

Event 2 — [Event type and origin]:
  Trigger: [What fired this event and where it propagates to]
  Component receiving: [Named component]
  Handler: [Handler function or hook]

[Continue for all events in the action chain. Include async events as separate entries
with their trigger mechanism: "fires after useEffect dependency change", "dispatched by thunk",
"emitted by Pinia action", etc.]

---

## COMPONENT TREE PATH

[Trace the path from event-receiving leaf to the root of the affected subtree.
Each hop must name the component and the relationship.]

[LeafComponent] (receives event)
  → [ParentComponent] (handler propagates via [prop / context / store subscription])
  → [ProviderComponent] (provides [context name or store slice])
  → [RootComponent or affected subtree root]

[If the path branches — e.g., context update affects multiple subtrees — trace each branch separately.]

---

## STATE MUTATION MAP

[List every state mutation triggered by the action.
For each mutation: owner, key, old shape, new shape. Be specific.
"State updates" with no detail does not satisfy this section.]

Mutation 1:
  Owner: [Component name or store name — exact]
  State key: [The specific key or slice — e.g., `isLoading`, `cart.items`, `user.profile`]
  Old shape: [Value or shape before the action — e.g., `false`, `[]`, `{id: null}`]
  New shape: [Value or shape after the action — e.g., `true`, `[{id: 1}]`, `{id: "abc"}`]
  Mechanism: [How the mutation is triggered — e.g., `useState setter`, `dispatch(addItem())`,
    `store.$patch`, `this.setState`]

[Repeat for each mutation. Minimum one concrete mutation required.
If no state mutation occurs, write: "No state mutation — this action is [read-only / presentational /
side-effect-only]. Justification: [why]." Do not leave this section empty.]

---

## RE-RENDER INVENTORY

[List every component that re-renders as a result of the state mutations above.
For each: name the component and explain why it re-renders.]

| Component | Re-render cause | Render count per action |
|-----------|----------------|------------------------|
| [ComponentName] | [owns state / subscribes to context / receives new props / selector matches] | [1 / N / "once per keystroke"] |
| [ComponentName] | [reason] | [count or rate] |
[Add rows for all re-rendering components. Minimum one row required.]

Unnecessary re-renders:
[List any component that re-renders but did not need to, and why.
If none: "No unnecessary re-renders detected — [reason: memoized / no prop changes / etc.]"]

---

## SIDE EFFECTS

[Capture every side effect beyond synchronous state mutations.]

| Effect | Mechanism | Trigger condition |
|--------|-----------|------------------|
| [API call: METHOD /endpoint] | [useEffect / thunk / saga / action creator] | [dependency that triggered it] |
| [Timer set/cleared] | [setTimeout / setInterval / useEffect cleanup] | [condition] |
| [Navigation] | [router.push / Link / history.replace] | [condition] |
| [localStorage / sessionStorage write] | [direct write / middleware] | [key and value shape] |
[Add rows for all side effects. If none exist, write a single row: "No side effects" | "N/A" | "Confirmed: action is synchronous with no subscriptions or API calls."]

---

## FINAL UI STATE

[Describe what the user sees after all synchronous effects complete.
Then describe the state after the first async settle point (e.g., after a loading state resolves,
after an API response returns). Two states required if any async effect exists.]

Synchronous final state:
[Visible elements, disabled states, loading indicators, error messages — be specific.
"UI updates accordingly" does not satisfy this section.]

Post-async final state (if applicable):
[What the user sees after the async operation settles — success state, error state, or both.
If the action is fully synchronous, write: "No async settle point — action is synchronous."]

---

## FINDINGS

[Identify issues in the traced path. Use the canonical issue types:
- Unnecessary re-renders (components in the Re-render Inventory that did not need to)
- Missing loading states (async effects without a pending/loading UI state)
- Error state gaps (API calls or async effects with no error handler or error UI)
- Accessibility failures (missing ARIA, focus loss after action, keyboard trap)

For each issue: name the component or state path, state the problem, classify the severity
(P1 critical / P2 degraded / P3 cosmetic).]

[If no issues were found: "No issues detected in this trace. Justification: [specific reason —
e.g., all re-renders are justified by prop changes, all async effects have error boundaries,
no accessibility failures visible in the tree]."]

---

## AMENDMENTS

[If any findings above warrant a fix, provide one concrete, minimal fix per finding.
Name the specific API, hook, memoization boundary, or ARIA attribute. Do not give general advice.]

[Or: "No amendments required — no issues found."]

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
components_traced, mutations_count, rerender_count, issues_count.
```

---

## V-02: Pre-Printed Event Table

**Axis:** Output format — a fixed 7-column event table replaces the prose event chain; each row is
one event in the action sequence; column headers map directly to C-01 through C-06; supplementary
sections handle C-07 (issues) and C-08 (framework vocabulary) after the table
**Hypothesis:** A pre-printed table whose column headers correspond to the six essential+recommended
trace steps physically cannot omit any step for any event: a blank cell is a visible, detectable
gap. The table format also forces the trace to progress event-by-event rather than jumping to
conclusions, which is the failure mode where state mutations are summarized at the top without
tracing the component tree path that produced them.

```
You are running /trace:component. Fill in the pre-printed template below.
All column headers are fixed. Fill in every cell for every event row.
Do not add, rename, reorder, or remove any column. Do not leave any cell blank.

---

## SETUP

Surface: [UI component or page — name it specifically]
User action: [Exact action — click, change, drag — name the UI element]
Expected outcome: [What the user expects to see]

---

## FRAMEWORK

Framework: [React / Vue / Angular / Svelte / Other: ___]
State management: [useState / Redux / Zustand / Pinia / NgRx / other: ___]

---

## EVENT TRACE TABLE

Column instructions:
- **Event** (C-01): Number and name the event (e.g., "1 — onClick on SubmitButton"). The first row
  must be the triggering user action. Subsequent rows are propagated or derived events.
- **Component path** (C-02): Name the component(s) involved in this event hop — show direction
  with →. At least two named components must appear across the full table. A row may name one
  component if this event stays local; the parent→child relationship must appear somewhere.
- **State mutation** (C-03): Name the state key, its owner, and the old→new value shape for any
  mutation this event causes. If no mutation occurs at this event: "None — [reason]."
- **Re-renders** (C-04): Name each component that re-renders because of this event and why.
  If no re-render: "None — [reason]." "Several components" without names does not pass.
- **Side effects** (C-05): Name any API call, timer, subscription, navigation, or storage write
  triggered at this event. Include the mechanism (useEffect / thunk / saga / etc.).
  If none: "None — confirmed."
- **UI change** (C-06): Describe the observable UI change after this event settles.
  If no visible change: "No UI change — [reason]."

| Event | Component path | State mutation | Re-renders | Side effects | UI change |
|-------|---------------|----------------|------------|--------------|-----------|
| 1 — [event name] | [ComponentA → ComponentB] | [key: old → new, owner: X] | [ComponentName (reason)] | [API: METHOD /path via useEffect] | [What user sees] |
| 2 — [event name] | [path] | [mutation or "None — reason"] | [renders or "None — reason"] | [effect or "None — confirmed"] | [UI or "No change — reason"] |
[Add one row per event in the action chain. Minimum three rows for a non-trivial action.
Async events (API response, timer callback) are separate rows — do not collapse with sync events.]

---

## POST-ASYNC STATE

[Required if any row in the Side effects column is not "None — confirmed."
Describe the final UI state after the async operation settles — both success and error paths.]

Success path: [What the user sees when the async effect completes successfully]
Error path: [What the user sees if the async effect fails — or: "No error state defined.
  This is a missing loading/error state issue — see FINDINGS."]

If the action is fully synchronous: write "No async effect — action is synchronous."

---

## ISSUES

[Identify problems in the trace. Use the canonical types:]
- **Unnecessary re-renders**: Component re-rendered but received no meaningful change
- **Missing loading state**: Async effect (Side effects column) has no loading UI row
- **Error state gap**: Async effect has no error path in POST-ASYNC STATE
- **Accessibility failure**: Missing ARIA attribute, focus loss, keyboard trap

For each issue: name the component or column cell where it appears, classify severity
(P1 / P2 / P3), and provide a minimal fix (specific hook, attribute, or pattern).

[If none: "No issues detected. Justification: [all async effects have loading rows in the table,
all re-renders are justified in column 4, no accessibility failures in component path]."]

---

## FRAMEWORK VOCABULARY NOTE

[Verify that the EVENT TRACE TABLE used at least two framework-specific terms correctly.
List them here with their row location.]

- [Term 1] used in row [N], column [column name]: [correct usage confirmed / usage note]
- [Term 2] used in row [N], column [column name]: [correct usage confirmed / usage note]

[If fewer than two framework-specific terms appear in the table, add them here with an explanation
of where they apply in the traced path.]

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, events_traced,
mutations_count, issues_count.
```

---

## V-03: Imperative Register

**Axis:** Phrasing register — short imperative sentences replace formal section headers and
descriptive instructions; each trace obligation is a direct command; no pre-printed table structure;
seven-step checklist framing where each step is a discrete action, not a criterion to satisfy
**Hypothesis:** Direct imperative phrasing ("Name the event. Walk the tree. State the mutation.")
reduces hedge language and prevents the vague-but-technically-present outputs that formal
descriptive instructions sometimes invite (e.g., "State updates occur in response to the action").
The checklist framing makes each of the five essential criteria feel like an action to complete
rather than a box to check. Tests whether register alone drives C-01 through C-05 without
structural scaffolding, and whether conversational phrasing reduces "State updates" filler responses.

```
You are running /trace:component.

Trace the user action through the component tree step by step.
Work through each step in order. Do not skip. Do not summarize ahead — complete each step before
moving to the next.

---

**Before you trace anything, declare two things:**

1. Framework: [Name the framework. React / Vue / Angular / Svelte / other. If you cannot determine
   it from context, state what you are inferring from and why.]

2. State management: [Name the state management approach in use. useState / Redux / Zustand /
   Pinia / NgRx / none / other.]

---

**Step 1. Name the event.**

State the exact event that the user action fires. Name the component that receives it.
Use the component's actual name — not "the button" or "the form." Give the event type
(onClick, onChange, onDragEnd, onSubmit, etc.) and which component is the immediate receiver.

Write: "[EventType] fires on [ComponentName]."

---

**Step 2. Walk the component tree.**

Trace the path from the event-receiving component up through its parent chain to the root of the
affected subtree. Name every hop. Show the direction.

Write each hop as: "[ChildComponent] → [ParentComponent] via [prop callback / context / store]."

Stop when you reach a component that is not affected by this event chain.
Show at least two named hops. A flat list of component names with no relationships does not satisfy
this step.

---

**Step 3. State the mutations.**

For every state change this event triggers, write:
"[ComponentName or StoreName] mutates [stateKey]: [oldShape] → [newShape]."

If the mutation is synchronous: mark it SYNC.
If the mutation happens after an async settle: mark it ASYNC and name the async mechanism
(useEffect, dispatch, thunk, saga, watcher, etc.).

If no mutation occurs: write "No mutation — this event does not produce a state change.
Reason: [why — e.g., read-only operation, animation only, navigation without state update]."
Do not leave this step blank.

---

**Step 4. List the re-renders.**

For each component that re-renders because of the mutations in Step 3, write:
"[ComponentName] re-renders because [it owns the state / it subscribes to this context /
it received new props from / its selector matches the changed slice]."

Include the render count if it re-renders more than once per action:
"[ComponentName] re-renders [N times per action] because [reason]."

If no component re-renders: write "No re-renders — [reason: all subscribers are memoized /
mutation is local with no subscribers / etc.]."

Do not write "several components re-render" without naming them.

---

**Step 5. Capture the side effects.**

For each side effect this action triggers beyond synchronous state mutations, write:
"[Side effect type]: [specific detail] via [mechanism]."

Examples of what to name:
- API call: "POST /api/cart/items via useEffect on [dependency]"
- Timer: "setTimeout(callback, 3000) set in [ComponentName]"
- Navigation: "router.push('/checkout') after [condition]"
- Storage: "localStorage.setItem('cart', serialized) in [middleware/action]"

If no side effects: write "No side effects — confirmed: this action is synchronous with no
subscriptions, API calls, or storage writes."

---

**Step 6. Describe what the user sees.**

State the final UI after all synchronous effects complete. Be specific.
Name elements that are now visible, hidden, disabled, or updated.

Then, if any side effect in Step 5 is async, describe what the user sees after it settles:
- Success: [what appears]
- Error: [what appears — or "no error state defined"]

Do not write "UI updates accordingly." Name what updates, to what value, and for whom.

---

**Step 7. Find the problems.**

Look at the complete trace above. Check for:
- Any component in Step 4 that re-rendered but received no meaningful change
- Any async effect in Step 5 that has no loading state between start and settle
- Any async effect in Step 5 that has no error state in Step 6
- Any component in Steps 2 or 6 with missing ARIA, keyboard support, or focus management

For each problem: name the component or state path, state the issue, state the severity
(P1 / P2 / P3), and give the minimal fix (name a specific hook, attribute, or boundary).

If you find nothing: write "No issues detected" followed by a specific reason — name why
each check came back clean, not just "the implementation looks correct."

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, issues_count.
```

---

## V-04: Gated Phases with Explicit Phase Close

**Axis:** Lifecycle emphasis — each of the five essential trace steps is a discrete, named phase
with an explicit phase-close condition; no phase can begin until the prior phase is declared
complete; phase boundaries are printed in the template as hard stops; the overall lifecycle
mirrors the Findings → Amend → Re-trace loop from the spec
**Hypothesis:** Explicit phase gates prevent the most common trace failure mode: collapsing all
five essential criteria into a single prose narrative where state mutations appear before the
component tree path is established, re-renders are inferred instead of inventoried, and the
final UI state is assumed rather than described. Each gate forces the model to close one trace
step before opening the next, ensuring that C-02 (tree), C-03 (state), and C-04 (re-renders)
are sequential and each complete before the next begins — which is the correct logical dependency
order for a trace.

```
You are running /trace:component. Complete each phase in order.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase has a close condition — the phase is not complete until that condition is met.

---

## PHASE 0: SURFACE AND FRAMEWORK

Identify the surface and detect the framework.

Surface: [UI component or page — name it specifically]
User action: [Exact user action — name the UI element and event type]
Expected outcome: [What the user expects to happen]
Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Role: [Auto-selected frontend expert — match to framework]

[PHASE 0 CLOSE: All fields above are filled in. Framework and state management are named.
Role is declared. Mark complete: PHASE 0 COMPLETE before continuing.]

---

## PHASE 1: EVENT ANCHOR

Identify the triggering event and its immediate receiver.

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Component name — the exact UI element that fires the event]
Event payload: [What data is carried in the event — e.g., value, id, coordinates.
  If no payload: "No payload — void event."]
Handler: [The function or lifecycle method that receives this event.
  If no handler registered: "No handler on [ComponentName] — event bubbles to [parent]."]

[PHASE 1 CLOSE: Event type, firing component, and handler are named.
Handler is a specific function name or lifecycle hook — not "the event handler."
Mark complete: PHASE 1 COMPLETE before continuing.]

---

## PHASE 2: COMPONENT TREE PATH

Trace the path from the event-receiving component to the root of the affected subtree.
Name every hop. Each hop must show the relationship (prop callback, context, store).

[EventReceivingComponent] (PHASE 1 component — receives event)
  ↓ [prop callback / context subscription / store dispatch]
[IntermediateComponent] (what it does with the event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

[If multiple subtrees are affected — context update propagates to two branches — trace each branch:]

Branch A:
  [ComponentA] → [ParentA] → [ContextConsumer A]

Branch B:
  [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 CLOSE: At least two named components appear with a directional relationship.
A flat list of component names without structure does not close this phase.
Mark complete: PHASE 2 COMPLETE before continuing.]

---

## PHASE 3: STATE MUTATION MAP

List every state mutation triggered by the event traced in PHASE 1–2.
Do not analyze re-renders yet — only state what changes.

Mutation [N]:
  Owner: [Component name or store name — exact match to PHASE 2 tree]
  Key: [State key or slice — e.g., `isLoading`, `cart.items[0]`, `user.authToken`]
  Old: [Value or shape before the action]
  New: [Value or shape after the action]
  Mechanism: [useState setter / dispatch / store.$patch / computed setter / etc.]
  Timing: [SYNC — completes in the same tick] or [ASYNC — after: useEffect / thunk / API response]

[If no state mutation occurs: "No state mutation — this action is read-only / presentational.
Justification: [specific reason]." This is a valid finding, not a gap. But it must be explicit.]

[PHASE 3 CLOSE: At least one mutation is named with owner, key, old value, new value, and mechanism.
"State updates" with no specifics does not close this phase.
Mark complete: PHASE 3 COMPLETE before continuing.]

---

## PHASE 4: RE-RENDER INVENTORY

Using the mutations from PHASE 3, list every component that re-renders and why.

| Component | Why it re-renders | Renders per action | Verdict |
|-----------|-------------------|-------------------|---------|
| [Name] | [owns state X / subscribes to context Y / receives prop Z from parent] | [1] | [justified / unnecessary] |
| [Name] | [reason] | [count] | [justified / unnecessary] |

Unnecessary re-renders: [For each row marked "unnecessary" above, state the fix.
  Example: "Wrap [Component] in React.memo and pass only [specific prop] instead of the full
  [object] — this prevents re-render when sibling state changes."
  If none: "No unnecessary re-renders — all components in the table have justified causes."]

[PHASE 4 CLOSE: At least one component is listed with its re-render cause and a justified/unnecessary
verdict. "Several components re-render" does not close this phase.
Mark complete: PHASE 4 COMPLETE before continuing.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI

**Side effects:**

[List every effect beyond synchronous state mutations. For each:]
Effect: [API call / timer / navigation / storage write / subscription]
Detail: [endpoint + method / timer delay / route / storage key]
Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

[If no side effects: "No side effects — confirmed synchronous: no API calls, timers, subscriptions,
or navigation triggered by this action."]

**Final UI state:**

Synchronous: [Describe what the user sees after all SYNC mutations (PHASE 3) and re-renders
  (PHASE 4) complete. Name elements: visible, hidden, disabled, in error state.]

Post-async: [Describe the UI after the async effect in Side effects above settles.
  Success: [what the user sees]
  Error: [what the user sees — or "No error state defined. This is a missing error state — see
  FINDINGS."]
  If synchronous only: "No async settle point."]

[PHASE 5 CLOSE: A concrete final state is described for the sync path. If any side effect exists,
a post-async state is described for both success and error paths.
"UI updates accordingly" does not close this phase.
Mark complete: PHASE 5 COMPLETE before continuing.]

---

## FINDINGS

[Review the closed phases above. Check for:]
- PHASE 4 unnecessary re-renders (already flagged there — summarize as findings here)
- PHASE 5 async effects without a loading state row between start and settle
- PHASE 5 post-async error paths marked "No error state defined"
- PHASE 2 components with missing ARIA, lost focus, or keyboard trap after the action completes

For each finding:
  Severity: P1 (critical path) / P2 (degraded experience) / P3 (cosmetic / accessibility debt)
  Location: [Phase + component or state key]
  Problem: [Specific statement — "ButtonGroup re-renders on every keystroke because it receives
    the full formState object" not "may have performance issues"]
  Fix: [One concrete, minimal fix — specific hook, attribute, or boundary. Not general advice.]

[If no findings: "No issues across all five phases. Justification: [phase-by-phase summary of
why each check came back clean]."]

---

## AMEND

[If any P1 or P2 finding above warrants a re-trace, describe what changes and re-run from the
affected phase. Reference the finding by number or severity.]

[If no amendment needed: "No re-trace required."]

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, phases_completed,
mutations_count, rerender_count, issues_count.
```

---

## V-05: Inertia Framing + Pre-Printed Event Table

**Axis (combined):** Inertia framing + output format — pre-printed 7-column event table carries a
"What ad-hoc inspection misses" column that forces comparison between the structured trace and
the status-quo alternative (opening Chrome DevTools, observing output, guessing the render path);
a standalone INERTIA section establishes the baseline before the table
**Hypothesis:** The status-quo competitor to `/trace:component` is ad-hoc DevTools inspection:
a developer observes the rendered output, maybe opens React DevTools, and infers the render
path from what they see rather than tracing what actually happened. That approach reliably misses
unnecessary re-renders (no component-level subscriber map in DevTools without profiler setup),
missing loading states (async chain not traced as a sequence), and accessibility failures
(not visible in the Elements panel without axe/Lighthouse). Forcing the trace to name "what
ad-hoc inspection misses" per row structurally guarantees C-07 (issue detection) surfaces even
when the developer would not naturally identify issues — the column demands a gap statement for
every event row.

```
You are running /trace:component. Fill in the pre-printed template below.
All column headers are fixed. Fill every cell. Do not leave any cell blank.
The "What ad-hoc misses" column is mandatory — it cannot be "N/A."

---

## SETUP

Surface: [UI component or page]
User action: [Exact action — name the UI element and event type]
Expected outcome: [What the user expects]
Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]

---

## INERTIA: STATUS QUO

Before tracing, state what a developer would learn by using ad-hoc DevTools inspection
instead of this structured trace — and what they would miss.

What ad-hoc DevTools shows:
- [Element rendered / not rendered in DOM]
- [Network tab: API call fired or not]
- [Console: errors logged or not]

What ad-hoc DevTools does NOT show without additional setup:
- [Component-level re-render cause — requires React Profiler / Vue DevTools component tab]
- [Full component tree path from event to state owner — requires stepping through source]
- [Unnecessary re-renders across sibling subtrees — invisible in DOM inspection]
- [Any other gap specific to this surface and framework]

Baseline cost of skipping this trace: [Describe the most likely mistake a developer makes
  without this trace — e.g., "Ships with ButtonGroup re-rendering on every keystroke; not caught
  until a performance regression surfaces in production." Be specific to this action and surface.]

---

## EVENT TRACE TABLE

Column instructions:
- **Event** (C-01): Number and name each event. The first row is the triggering user action.
- **Component path** (C-02): Name components with direction (→). At least two named components
  must appear across the full table.
- **State mutation** (C-03): Name key, owner, old→new shape. "None — [reason]" if no mutation.
- **Re-renders** (C-04): Name each re-rendering component and why. "None — [reason]" if none.
- **Side effects** (C-05): API call, timer, navigation, or storage write with mechanism.
  "None — confirmed" if none.
- **UI change** (C-06): Observable UI change after this event settles.
- **What ad-hoc misses** (C-07-inertia): What would a developer using only browser DevTools
  (without profiler, without source-stepping) fail to observe or conclude from this row?
  Cannot be "N/A." If everything in this row is visible in DevTools, write exactly:
  "Nothing — this row is fully observable in DevTools via [element/network/console tab]. Note:
  this is the exception, not the rule."

| Event | Component path | State mutation | Re-renders | Side effects | UI change | What ad-hoc misses |
|-------|---------------|----------------|------------|--------------|-----------|-------------------|
| 1 — [name] | [A → B] | [key: old → new] | [C (reason)] | [POST /path via useEffect] | [visible change] | [what DevTools cannot show here] |
| 2 — [name] | [path] | [mutation or None] | [renders or None] | [effect or None] | [change] | [what is invisible to ad-hoc] |
[Add one row per event. Minimum three rows. Async events are separate rows.]

---

## POST-ASYNC STATE

[Required if any Side effects cell is not "None — confirmed."]

Success path: [What the user sees when the async effect completes successfully]
Error path: [What the user sees if it fails — or "No error state defined. See FINDINGS."]

What ad-hoc DevTools would show for success: [observable in network tab / DOM]
What ad-hoc DevTools would NOT show for success: [e.g., which component triggered the re-render
  that updated the success state, whether a sibling unnecessarily re-rendered on success]

---

## FINDINGS

[Consolidate issues from the "What ad-hoc misses" column and POST-ASYNC STATE above.
Each finding should reference the row or section where it was flagged in the table.]

For each issue:
  Source: [Row N, column "What ad-hoc misses" / POST-ASYNC STATE error path]
  Type: [Unnecessary re-render / Missing loading state / Error state gap / Accessibility failure]
  Severity: P1 / P2 / P3
  Problem: [Specific — name the component and the exact issue]
  Fix: [Minimal, concrete — name a specific hook, attribute, or boundary]
  Do-nothing cost: [What happens in production if this is not fixed — tie back to INERTIA section]

[If no issues: "No issues detected. Reference: all 'What ad-hoc misses' cells are 'Nothing' —
this is an unusually clean trace. Verify with the INERTIA baseline that no issues were assumed
away rather than confirmed clean."]

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, events_traced,
issues_count, inertia_baseline.
```
