# trace-component -- R1 Variations (v1 rubric)

**Round**: 1
**Rubric ceiling**: 100 pts (C-01 through C-09)
**Rubric file**: `simulations/quest/rubrics/trace-component-rubric-2026-03-15.md`

**Variation axes chosen (3 single-axis, then 2 combined):**
1. Role sequence -- framework-detect before trace anchors expert vocabulary to component names and state primitives
2. Output format -- structured tables force enumeration completeness for event chain and re-render list
3. Lifecycle emphasis -- hard phase gates prevent state delta from bleeding into event chain; per-criterion coverage improves
4. Role sequence + Phrasing register -- expert identity + conversational walkthrough register elicits more specific naming
5. Output format + Lifecycle emphasis + Inertia framing -- tables + phase gates + naive-DOM baseline surfaces unnecessary re-renders for C-06

**Variation map:**

| Variation | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | Hypothesis |
|-----------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Role sequence | + | + | + | + | ~ | ~ | ~ | ~ | ~ | Named expert role before trace forces framework-idiomatic component names and state vocabulary |
| V-02 | Output format | + | + | ~ | + | ~ | ~ | ~ | ~ | ~ | Tabular rows prevent omission of individual handlers (C-01) and re-render reasons (C-04) |
| V-03 | Lifecycle emphasis | + | + | + | + | + | ~ | + | ~ | ~ | Phase gates make C-01/C-03 non-overlapping; explicit completion criteria per phase |
| V-04 | Role seq + Register | + | + | + | ~ | ~ | + | ~ | ~ | + | Conversational expert voice surfaces accessibility and framework-portable observations naturally |
| V-05 | Format + Lifecycle + Inertia | + | + | + | + | + | + | + | + | ~ | Naive-DOM baseline column in re-render table makes unnecessary re-renders explicit for C-06 |

Legend: + = axis targets this criterion, ~ = neutral

---

## V-01 -- Role Sequence

**Axis**: Role sequence
**Hypothesis**: Activating a named framework-specific expert role before the trace begins forces use of that framework's exact vocabulary for component names (C-02) and state primitives (C-03). A generic "frontend developer" prompt defaults to React even when the topic uses Vue; explicit detection eliminates the mismatch.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

---

### Step 1 -- Detect Framework

Read the topic context and identify the frontend framework: React, Vue, Svelte, Angular, or other. State your detection and the evidence (import pattern, file extension, hook usage, etc.). If no framework is detectable, default to React and note the assumption.

> Framework detected: ___

---

### Step 2 -- Activate Expert Role

Assign yourself the role of a senior engineer who has shipped production code in the detected framework. Use the mental model of that expert for every term in this trace:

- **React**: hooks, fiber reconciler, scheduler, synthetic events, render tree
- **Vue 3**: reactive proxy, watchEffect, template compiler, vnode patch, composable
- **Svelte**: compiled output, store subscriber, derived contract, $: reactive block
- **Angular**: zone.js, ChangeDetectionStrategy, ViewChild, DI injector, async pipe

> Expert role active: [Framework] Senior Engineer

Do not use generic language where framework-specific terms exist. If you say "state update," name the exact hook, store method, or reactive primitive.

---

### Step 3 -- Trace as That Expert

Produce the full trace artifact using your expert role's vocabulary.

**Event Chain**
List every event handler that fires in response to `{{signal}}`, in the exact order they fire. For each:
- Handler name (exact function name, not "click handler")
- Component that owns it (exact component name)
- Event type (synthetic vs native, name)
- Propagation path (capture phase? target? bubble? stopped?)

No gaps. If a handler is in the call chain, it has an entry. If event delegation is used, name the delegate owner.

**Component Tree Traversal**
Starting from the component that receives the event, trace the prop/callback path until the action is fully resolved. For each component in the path:
- Component name (exact, as it appears in source)
- What it receives: prop name and type, or callback name
- What it passes down or calls up: name the prop or callback explicitly
- Direction: `DOWN` (prop drilling) or `UP` (callback invocation)

Show the full path. If a component re-renders a child via context rather than props, name the context provider and consumer.

**State Delta**
For each state update triggered by `{{signal}}`:
- State key or slice name (exact: `useState` variable, `ref`, Vuex module + key, Svelte store variable)
- Value before the action
- Value after the action

Then identify any derived state that depends on the changed key: selectors, computed properties, memoized values -- before and after.

**Re-render List**
List every component that re-renders as a result of the state delta. For each:
- Component name
- Reason: `prop change` / `context change` / `selector subscription` -- be specific about which prop or which context value changed

Then list every component that did NOT re-render, with the reason:
- `memo equality` (React.memo / Vue `v-once` / etc.)
- `selector equality` (reselect / Pinia getter / etc.)
- `no subscription` (not connected to the changed state)

Neither list can be empty if the action produces any state change.

**Side Effects**
List every side effect triggered: API calls, subscription updates, timers, storage writes. For each:
- Name or endpoint
- Owner component or middleware (thunk, saga, composable, service)
- Fires: `sync` (in event handler) or `deferred` (useEffect, watchEffect, setTimeout, etc.)

For each async effect, name three states:
- Loading state set when the effect starts
- Success state set on completion
- Error state set on failure

All three must be named. "No error state" is a finding for the Issue Audit, not a valid omission here.

**Issue Audit**
Evaluate all four issue categories. For each, state your finding explicitly:

1. **Unnecessary re-renders** -- Which components in the re-render list re-rendered but produced no observable UI change? Could React.memo, useMemo, a selector, or a smaller render scope have prevented it?
2. **Missing loading states** -- For each async effect in Side Effects: is a loading state set at the start? If not, name the gap.
3. **Error state gaps** -- For each async effect: is an error state set on failure? If not, name the gap. If the error is swallowed silently, name that.
4. **Accessibility failures** -- Does the event chain handle keyboard input (Enter/Space for interactive elements)? Is focus managed after the action (modal open/close, route change)? Are screen reader announcements triggered for dynamic content?

For each category: issue found (component name, nature of gap, one-line remediation) OR no issue found (with supporting evidence from the trace). A "no issues" conclusion with no evidence citation fails this criterion.

**Final UI State**
After the full trace settles, describe the observable UI state:
- Which elements are visible or hidden
- What text or data is displayed
- What interactive state components are in: disabled, focused, selected, loading, error

Derive this directly from the State Delta above. Do not add state not established there.

**Optimization Notes** _(optional -- aspirational)_
If the trace revealed re-renders that could be eliminated or batched: name the component, the specific optimization (React.memo, useMemo with dependency array, reselect selector, batch dispatch, render-scope reduction), and the expected render reduction (e.g., "eliminates 3 re-renders on every keystroke in SearchInput").

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-02 -- Output Format

**Axis**: Output format (structured tables)
**Hypothesis**: Requiring each phase as a mandatory table with typed columns prevents the omission of individual handlers (C-01) and re-render reasons (C-04) that prose narrative allows. Each row is a unit of coverage; a missing row is visually obvious.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

**Role**: Frontend domain expert. Detect the framework from the topic context (React, Vue, Svelte, Angular) and use that framework's vocabulary throughout.

---

Produce the trace as structured tables. Each table is mandatory. Do not merge rows, skip rows, or replace a table with prose. After the tables, prose blocks cover side effects, issue audit, and final UI state.

---

### Table 1 -- Event Chain

Every handler that fires in response to `{{signal}}`, in the order they fire. One row per handler. No handler in the call chain may be omitted.

| # | Handler Name | Owner Component | Event Type | Sync/Async | Propagation |
|---|---|---|---|---|---|
| 1 | | | | | |

_Propagation_: `capture` / `target` / `bubble` / `stopped` / `delegated:{owner}`.
_Sync/Async_: `sync` if the handler completes inline; `async` if it dispatches, schedules, or awaits.

---

### Table 2 -- Component Tree Path

The component path from the event receiver to the deepest component affected. One row per handoff. Show both DOWN (prop drilling) and UP (callback invocation) moves.

| # | From Component | To Component | Direction | Payload Name | Payload Type |
|---|---|---|---|---|---|
| 1 | | | | | |

_Direction_: `DOWN` = prop passed to child; `UP` = callback invoked by child; `CONTEXT` = value read from context provider.

---

### Table 3 -- State Delta

Every state update triggered by `{{signal}}`. One row per state key or slice. If derived state depends on a changed key, add a row for the derived value.

| State Key / Slice | Kind | Before | After | Derived From? |
|---|---|---|---|---|
| | | | | |

_Kind_: `local` (useState/ref/data) / `global` (Redux/Pinia/Zustand/store) / `derived` (selector/computed/memoized).
_Derived From?_: name the parent key if this row is derived state; leave blank for primary state.

---

### Table 4 -- Re-render List

Every component touched by the state delta. One row per component. Include both re-rendered and not-re-rendered components.

| Component Name | Re-rendered? | Reason | Memoization in Place? | Memo Type |
|---|---|---|---|---|
| | | | | |

_Re-rendered?_: `YES` or `NO`.
_Reason (YES)_: `prop change:{prop}` / `context:{context name}` / `selector:{selector name}`.
_Reason (NO)_: `memo equality` / `selector equality` / `no subscription` / `not in subtree`.
_Memo Type_: `React.memo` / `useMemo` / `PureComponent` / `reselect` / `v-memo` / etc. Empty if no memo.

---

### Side Effects

Prose block. For each side effect triggered (API call, subscription, timer, storage write):
- Name or endpoint
- Owner: component name or middleware name
- Timing: `sync` (runs in handler body) or `deferred` (useEffect, watchEffect, nextTick, setTimeout, etc.)
- On start: state key set to indicate loading (name the key and value)
- On success: state key and value set on completion
- On failure: state key and value set on error

If no loading state or error state is set, note it explicitly -- that is a finding for the Issue Audit.

---

### Issue Audit

Evaluate all four categories. Base each evaluation on the tables above -- cite specific rows.

**1. Unnecessary re-renders**
Cross-reference Table 4. For each YES row: was the re-render necessary (did a visible prop change)? Flag any component that re-rendered without an observable UI change. Cite the Table 4 row number.

**2. Missing loading states**
Cross-reference Side Effects. For each async effect: is a loading state set at start? If not, name the effect and the gap.

**3. Error state gaps**
Cross-reference Side Effects. For each async effect: is an error state set on failure? If not, name the effect and the gap. Silent catch blocks count as error state gaps.

**4. Accessibility failures**
Evaluate Table 1 for keyboard path coverage: does the event chain fire on keydown/keyup/Enter/Space as well as click? Evaluate Table 2 for focus management: after the action, is focus placed correctly? Evaluate Table 3 for screen reader state: does any state change trigger an aria-live or role update?

For each category: one or more findings (component, gap, remediation) OR "No issues found" with a specific Table row citation as evidence.

---

### Final UI State

Prose. Observable end state after the trace settles. Derive directly from Table 3:
- Visible / hidden elements (keyed to state changes in Table 3)
- Text or data displayed (values from Table 3 After column)
- Interactive states: disabled, focused, selected, loading, error (keyed to state changes)

Do not describe state not established in Table 3.

---

### Optimization Notes _(optional -- aspirational)_

If Table 4 contains YES rows that appear unnecessary, or if Table 3 shows high-frequency state churn: name the component, the specific optimization (React.memo, useMemo dependency array, reselect selector, batch dispatch), and the expected render reduction.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-03 -- Lifecycle Emphasis

**Axis**: Lifecycle emphasis (hard phase gates with per-phase completion criteria)
**Hypothesis**: Naming each phase explicitly with a stated completion criterion forces the model to populate C-01 and C-03 in separate, non-overlapping sections. Without phase gates, event-chain and state-delta information bleed together, making both criteria harder to score and easier to partially omit.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

**Role**: Frontend domain expert. Detect the framework from the topic context. Use framework vocabulary throughout.

---

Complete each phase in order. Do not begin the next phase until the current phase's completion criterion is fully satisfied. Each phase is a mandatory section in the output artifact.

---

### PHASE 1 -- Event Chain Reconstruction

**Completion criterion**: Every event handler in the call chain is named, in the exact firing order, with its owner component. No handler may be inferred or omitted. If you cannot name a handler precisely, flag it as UNKNOWN rather than skip it.

Produce:
- An ordered list of every handler that fires when the user performs `{{signal}}`
- For each: handler name (exact), owner component (exact), event type (native DOM vs framework synthetic), propagation state (capture / target / bubble / stopped)

> Phase 1 complete when: ordered list exists, each entry has handler name + component + event type + propagation. Zero blanks.

---

### PHASE 2 -- Component Tree Traversal

**Completion criterion**: A continuous path exists from the event-receiving component to the deepest component affected. Every intermediate component is named. Every prop and callback passed along the path is named with direction (DOWN/UP). No gaps in the path.

Produce:
- Starting point: the component that first receives the event from Phase 1
- For each handoff: from component → to component, direction (DOWN = prop / UP = callback), payload name, payload type
- Ending point: the deepest component whose visible output changes
- Note any context consumers in the path (context name, provider, consumer)

> Phase 2 complete when: unbroken path from event receiver to leaf, every handoff named, no "and then it updates the component" shortcuts.

---

### PHASE 3 -- State Delta Mapping

**Completion criterion**: Every state key or slice updated by the action appears with its before value and after value. Derived state (selectors, computed properties, memoized values, getters) that depends on a changed key appears with its own before/after. Zero state changes may be implied without being named.

Produce:
- For each primary state update: key/slice name, before, after
- For each derived value that depends on a changed key: derived value name, before, after, which key it derives from

> Phase 3 complete when: every state change from the action is enumerated, derived state is included, before/after values present for all.

---

### PHASE 4 -- Re-render Analysis

**Completion criterion**: Every component that re-renders is listed with the specific reason. Every component that does NOT re-render (due to memoization, selector equality, or absence of subscription) is listed with the reason. Neither list may be empty if the action produces any state change.

Produce:
- **Re-rendered**: component name, reason (prop change:{which prop} / context:{which context} / selector:{which selector})
- **Not re-rendered**: component name, reason (memo equality / selector equality / no subscription / not in subtree)

> Phase 4 complete when: both lists present (or a documented "action produces no state change" if Phase 3 found none), every re-render has a named reason, every skipped component has a named reason.

---

### PHASE 5 -- Side Effects and Async Paths

**Completion criterion**: Every side effect triggered by the action is named with its owner and timing. For every async effect, three states are named: loading (at start), success (on completion), error (on failure). A missing loading state or missing error state is not an omission -- it is a finding that must be surfaced in Phase 6.

Produce:
- For each side effect: name/endpoint, owner (component or middleware), sync or deferred
- For each async effect: loading state (key + value), success state (key + value), error state (key + value)
- If loading state is absent: note "no loading state -- Phase 6 finding"
- If error state is absent: note "no error state -- Phase 6 finding"

> Phase 5 complete when: all side effects listed, all async paths have three-state accounting (or a named finding if one is absent).

---

### PHASE 6 -- Issue Audit

**Completion criterion**: All four issue categories are evaluated with explicit reasoning anchored to prior phases. A "no issues found" conclusion must cite the specific Phase evidence that supports it. Unsubstantiated "no issues" fails this phase.

Evaluate each category:

**Unnecessary re-renders**: Review Phase 4 re-render list. For each YES: did a visible change occur? If a component re-rendered but its output did not change observably, that is an unnecessary re-render. Name the component, describe what triggered it, suggest a remedy.

**Missing loading states**: Review Phase 5 findings. For each "no loading state" note, describe the user-visible gap (spinner absent, button stays enabled, etc.) and suggest the missing state.

**Error state gaps**: Review Phase 5 findings. For each "no error state" note, describe the user-visible gap (silent failure, stale data displayed, etc.) and suggest the missing state.

**Accessibility failures**: Review Phase 1 for keyboard path. Does the event chain fire on keyboard events as well as pointer events? Review Phase 2 for focus management. After the action, is focus placed on the new content? Review Phase 3 for aria-live updates triggered by state changes to dynamic content.

> Phase 6 complete when: all four categories have an explicit finding or explicit "no issues" with Phase citation.

---

### PHASE 7 -- Final UI State Snapshot

**Completion criterion**: Observable UI state after the trace is described, derived entirely from Phase 3 state delta. No state may appear here that was not established in Phase 3.

Produce:
- Visible / hidden elements (derived from which Phase 3 keys changed)
- Text or data displayed (from Phase 3 after-values)
- Interactive states: disabled, focused, selected, loading, error (from Phase 3 after-values)

> Phase 7 complete when: every statement in this section maps back to a Phase 3 row.

---

### PHASE 8 -- Optimization Notes _(optional -- aspirational)_

**Completion criterion** _(optional)_: If Phase 4 identified re-renders that appear unnecessary or Phase 3 shows high-frequency state churn, name at least one concrete optimization candidate.

Produce (if warranted):
- Component name
- Optimization: React.memo / useMemo with dependency array / reselect selector / batch dispatch / render-scope reduction
- Expected effect: quantify the render reduction ("eliminates re-render on every keystroke in SearchBox")

> Skip this phase if no candidates exist.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-04 -- Combined: Role Sequence + Phrasing Register

**Axes**: Role sequence + Phrasing register
**Hypothesis**: An expert-identity framing combined with conversational walkthrough register ("follow the call into...") elicits more specific component and handler names (C-02) than formal imperative. The conversational voice also surfaces accessibility observations (C-06d) and framework-portable patterns (C-09) more naturally because the expert explains their reasoning rather than just listing outputs.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

---

### Who You Are

Look at the topic and identify the frontend framework. Then step fully into the role of a senior engineer who has shipped production apps in that framework -- not a generic frontend developer, but someone whose instincts are shaped by that specific runtime.

- **React developer**: You think about fiber, the reconciler, which hooks fire and when, the scheduler's priority queue, and what React.memo actually buys you in practice.
- **Vue 3 developer**: You think about the reactive proxy, when watchers are lazy vs eager, how the template compiler transforms `v-model`, and what `shallowReactive` trades off.
- **Svelte developer**: You think about what the compiler emits, when `$:` blocks invalidate, what the store contract guarantees, and how `derived` is different from a computed memo.
- **Angular developer**: You think about zones, which change detection strategy is active, how the injector resolves services, and when `async` pipe unsubscribes.

No framework detectable? Default to React and say so.

Open with: *"I am a [Framework] Senior Engineer. I'll walk through what happens when {{signal}} is triggered in {{topic}}."*

---

### Walk Through the Action

Now tell the story of this user action from first event to final paint. Think out loud. Be specific and named throughout. If you would naturally say "a handler fires" -- stop and name the handler. If you would say "state updates" -- stop and name the key and the values.

---

**What fires first?**

Walk through every event handler that responds to `{{signal}}`, in the order they fire. Think about propagation: does the event travel up? Does something in a parent catch it first? Is there delegation happening? Name each handler, who owns it, and what kind of event it is.

---

**Where does the call go in the component tree?**

Follow the signal from the component that first handles it. Which component gets it? What does it do -- does it call a prop callback upward? Does it set local state? Does it dispatch to a global store? Follow every handoff. Name every component you pass through, name every prop and callback you see. Mark each move: are you going DOWN into children, or UP toward a parent?

Don't shortcut. "The data flows up to the parent" is not enough -- name the parent, name the callback.

---

**What state actually changes?**

When the dust settles, what state is different? Walk through each change. For each: what is the exact key or slice, what did it hold before, what does it hold now? Are there selectors, computed values, or memoized results that derive from any of those keys? If so, they changed too -- name them.

---

**Who notices the change -- and who doesn't?**

Think about who's subscribed. Which components re-render because of those state changes? For each one: why exactly -- new prop, new context value, subscribed selector? Be specific about which prop or which context.

Now think about who has insulation. Which components are wrapped in memo, or whose selectors held equality? Name them too, and say what kept them from re-rendering.

---

**What's happening in the background?**

Is there anything async in motion? An API call, a subscription update, a timer, a storage write? Name each one and say who owns it. Does it fire immediately in the handler, or does it schedule for later?

For each async effect: what state does it set when it starts (the loading signal)? What does it set when it comes back (success path)? What does it set when it fails (error path)? Walk all three branches.

---

**Anything feel off?**

Step back and audit the trace with your senior-engineer instincts. Walk through each issue type and tell me honestly what you see:

*Unnecessary re-renders* -- Any component in that re-render list that really didn't need to re-render? Could a memo, a selector, or a smaller component boundary have prevented it? Name it.

*Missing loading states* -- Every async path you named -- is there a loading state covering it? If a user clicks the button and nothing in the UI changes until the response arrives, that's a gap. Name it.

*Error state gaps* -- If the async call fails, does the UI show something? Or does it silently return to where it was? A silent error is a gap. Name it.

*Accessibility* -- When the user performs `{{signal}}` with a keyboard instead of a mouse, does the event chain still fire? After the action, where does focus go? Is there a screen reader announcement for the content that just changed? Any gaps here?

Be honest. If everything looks correct, explain why the trace supports that -- don't just say "no issues."

---

**What does the user see at the end?**

After everything settles -- what is the actual visible UI state? What's on screen, what's hidden, what does the data say? What interactive states are components in -- disabled, loading, focused, selected?

Derive this from the state changes you named above. Don't describe state you didn't trace.

---

**Any quick wins you spotted?** _(optional -- aspirational)_

If you noticed a re-render that could be memoized out, or a state update that could be batched, name the component and the fix. Estimate the render reduction if you can.

---

**Framework Notes** _(optional -- aspirational)_

After the trace, add a brief "Framework Notes" section: where did the framework's specific mechanics (scheduler, reactive proxy, zone, etc.) shape the trace in ways that would look different in another framework? This keeps the core trace readable for someone unfamiliar with `{{framework}}`.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-05 -- Combined: Output Format + Lifecycle Emphasis + Inertia Framing

**Axes**: Output format + Lifecycle emphasis + Inertia framing
**Hypothesis**: A naive-DOM baseline column in the re-render table makes unnecessary re-renders visually explicit -- any component that re-renders for a reason the naive path would not require is a flagged row, which feeds C-06 (unnecessary re-renders) with concrete evidence rather than editorial judgment. Tables plus phase gates maintain C-01/C-04 coverage; inertia framing distinguishes necessary from unnecessary state machinery.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

**Role**: Frontend domain expert. Detect framework from topic context. Use framework vocabulary throughout.

---

### Inertia Baseline

Before the trace, establish the naive DOM path: what would happen if there were no framework, no state management, no reactive graph -- just a plain event listener and direct DOM mutation.

**Naive DOM path for `{{signal}}`:**
> [Describe: event fires → handler runs → DOM nodes mutated directly → browser repaints. No virtual DOM, no state diffing, no subscriptions. One event, one mutation, one paint.]

Every departure from this path in the actual implementation is deliberate. If a component re-renders but the naive path would have achieved the same visible result with a direct mutation, that departure is a candidate for C-06 (unnecessary re-render). Track each departure in the tables below.

---

### Phase 1 -- Event Chain

_Complete before Phase 2._

Every handler that fires in response to `{{signal}}`, in firing order. One row per handler.

| # | Handler Name | Owner Component | Event Type | Propagation | Departs from Naive? | Departure Reason |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

_Departs from Naive?_: YES if this handler does something that the naive path would not need (e.g., dispatches to a store instead of mutating the DOM directly). NO if it maps 1:1 to a naive DOM operation.
_Departure Reason_: only if YES -- what does this handler do that the naive path does not (e.g., "dispatches action to Redux instead of direct DOM write")?

_Phase 1 complete when_: all handlers listed, ordering verified, every YES row has a departure reason.

---

### Phase 2 -- Component Tree Traversal

_Complete before Phase 3._

Component path from event receiver to deepest affected component.

| # | From Component | To Component | Direction | Payload Name | Payload Type | Naive Equivalent |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

_Direction_: `DOWN` (prop to child) / `UP` (callback to parent) / `CONTEXT` (context consumer reads value).
_Naive Equivalent_: the direct DOM operation this handoff replaces. If there is no naive equivalent (the component represents UI logic with no direct DOM counterpart), write `UI-LOGIC`.

_Phase 2 complete when_: unbroken path from event receiver to leaf, every handoff has a naive equivalent or explicit UI-LOGIC designation.

---

### Phase 3 -- State Delta

_Complete before Phase 4._

Every state update triggered by `{{signal}}`. One row per key or slice. Derived state gets its own row.

| State Key / Slice | Kind | Before | After | Naive Equivalent | Derived From |
|---|---|---|---|---|---|
| | | | | | |

_Kind_: `local` / `global` / `derived`.
_Naive Equivalent_: the direct DOM property or attribute this state update replaces (e.g., `input.disabled = true`). Write `NO-NAIVE` if this state has no direct DOM counterpart (pure UI orchestration logic).
_Derived From_: parent key if this row is derived state; blank for primary state.

_Phase 3 complete when_: all state changes enumerated with before/after, derived state included, every row has a naive equivalent or NO-NAIVE.

---

### Phase 4 -- Re-render Analysis

_Complete before Phase 5._

Every component in the component tree evaluated for re-render. One row per component.

| Component | Re-rendered? | Reason | Memo in Place? | Naive Assessment | Flag |
|---|---|---|---|---|---|
| | | | | | |

_Re-rendered?_: `YES` or `NO`.
_Reason (YES)_: `prop:{prop name}` / `context:{context name}` / `selector:{selector name}`.
_Reason (NO)_: `memo equality` / `selector equality` / `no subscription`.
_Naive Assessment_: `NEEDED` (the naive path would also update this element) / `UNNECESSARY` (the naive path would not need to update this element -- direct mutation would suffice) / `MEMOIZED-SKIP` (no re-render, memo held).
_Flag_: `C-06` if Naive Assessment is UNNECESSARY and no optimization is already in place; blank otherwise.

_Phase 4 complete when_: every component in the affected subtree has a row, every UNNECESSARY row has a C-06 flag.

---

### Phase 5 -- Side Effects

_Complete before Phase 6._

Every side effect triggered. Prose section.

For each side effect: name or endpoint, owner (component or middleware), timing (sync / deferred).

For each async effect, name all three states:
- **Loading state** (key + value set when effect starts) -- if absent, write `MISSING-LOADING`
- **Success state** (key + value set on completion)
- **Error state** (key + value set on failure) -- if absent, write `MISSING-ERROR`

`MISSING-*` entries are Phase 6 findings; do not omit them.

_Phase 5 complete when_: all side effects listed, all async paths have three-state accounting.

---

### Phase 6 -- Issue Audit

_Complete before Phase 7._

**Completion criterion**: All four categories evaluated with explicit phase citations. Unsubstantiated "no issues" fails this phase.

**1. Unnecessary re-renders**
List all Phase 4 rows with Flag = `C-06`. For each: component name, why it re-rendered, why the naive path shows this was unnecessary, one-line remediation (React.memo / useMemo / smaller component boundary / selector / batch).
If no C-06 flags: cite the Phase 4 rows that confirm all re-renders were NEEDED.

**2. Missing loading states**
List all Phase 5 `MISSING-LOADING` entries. For each: effect name, what the user sees during the async wait without a loading state, suggested loading state (state key and value).
If none: cite the Phase 5 async effects that confirm loading states are present.

**3. Error state gaps**
List all Phase 5 `MISSING-ERROR` entries. For each: effect name, failure mode visible to the user, suggested error state (state key and value).
If none: cite the Phase 5 async effects that confirm error states are present.

**4. Accessibility failures**
Review Phase 1: does the event chain include keyboard events (keydown / keyup / Enter / Space) in addition to pointer events? If not, name the missing handler.
Review Phase 2: after the action, is focus placed correctly (modal, route change, dynamic content)?
Review Phase 3: does any state change trigger an aria-live region update or role change?
Name all gaps, or cite the phase evidence that confirms accessibility is covered.

_Phase 6 complete when_: all four categories have explicit findings or explicit no-issue with phase citation.

---

### Phase 7 -- Final UI State

_Complete before Phase 8._

Observable UI state after the trace settles. Derive entirely from Phase 3.

- Visible / hidden elements: cite the Phase 3 key that controls each
- Text or data displayed: cite the Phase 3 after-value that populates each
- Interactive states (disabled, focused, selected, loading, error): cite the Phase 3 after-value

No state may appear here that is not established in Phase 3.

_Phase 7 complete when_: every statement maps to a Phase 3 row.

---

### Phase 8 -- Optimization Notes _(optional -- aspirational)_

If Phase 4 contains UNNECESSARY rows or Phase 3 shows high-frequency state churn (key updated on every keystroke, every scroll, etc.):

- Component name
- Optimization: `React.memo` / `useMemo:{dependencies}` / `reselect selector` / `batch dispatch` / `render-scope reduction`
- Expected effect: render reduction estimate ("eliminates 3 re-renders per keystroke in TagInput")

Skip if no candidates.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`
