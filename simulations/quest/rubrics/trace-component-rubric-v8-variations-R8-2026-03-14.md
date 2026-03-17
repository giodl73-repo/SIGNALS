# trace-component — Round 8 Variations

**Variation axes used:**
- Single-axis: Output format (V-01), Lifecycle emphasis (V-02), Phrasing register (V-03)
- Combined: Output format + Role sequence (V-04), Inertia framing + Output format (V-05)

**R8 context:** Three new criteria (C-27 Mutation Count Pre-Declaration, C-28 Per-Hop Direction Annotation, C-29 Re-render Inventory Completeness by Traversal) were promoted from R7 V-01 excellence signals. All five variations must now address these as first-class structural requirements. The challenge is closing the remaining C-09–C-23 aspirational gap (V-01 scored ~26/30 there in R7).

---

## V-01 · Output Format — Schema-Enforced Tables with Explicit Gate Fields

**Axis**: Output format (schema-enforced tables)
**Hypothesis**: Making C-27, C-28, and C-29 into mandatory schema *fields* — not instructions — prevents elision by table shape rather than instruction memory. A model cannot leave a required column blank without a visible gap. Combined with the R7 mutation-count pre-declaration and UR-ID cross-reference chain, this should push aspirational coverage to 29+/34 on C-09–C-26 and 6/6 on C-27–C-29.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding. All output uses that framework's exact terminology — no generic substitutions.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

Do not begin phase analysis until this header is complete.

---

**TABLE 1 · Event Anchor**

Required columns: Event Type · Component Name · Handler Function · Event Payload · File Location

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|---------------|-----------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact component name — not "the button")* | *(exact function name — not "the handler")* | *(value / object shape / "none")* | *(path:line)* |

Invalid cell values: "the button", "a click", "the handler", "N/A", blank. If the handler is an inline arrow function, name the prop and describe the function body in one line.

---

**TABLE 2 · Component Tree Traversal**

Required columns: Step · Component · Direction · Mechanism · Notes

| Step | Component | Direction | Mechanism | Notes |
|------|-----------|-----------|-----------|-------|
| 1 | *(leaf component receiving event)* | ↑ upward propagation | *(event handler call / callback prop)* | *(any relevant detail)* |
| 2 | *(next component in path)* | ↓ downward prop-passing \| ↑ upward \| context injection \| event delegation | *(prop name / context hook / HOC wrapper)* | |
| … | | | | |

Rules:
- Minimum two rows. A single-row traversal does not satisfy this table.
- Direction column is **required per row** — not once as a summary statement. Permitted values: `↑ upward propagation`, `↓ downward prop-passing`, `context injection`, `event delegation`. Blank direction cells do not pass.
- Assign each component a Traversal ID (T-01, T-02, …) used in TABLE 4.

---

**TABLE 3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION (required, appears before table body):**

```
Mutation count: N = ___
```

Fill N before completing the table. If N = 0, skip the table body and write instead:

```
ZERO MUTATION DECLARATION
Reason: [read-only operation / display-only component / event consumed without dispatch / other]
Confirmation: No local useState, no context write, no store dispatch triggered by this action.
```

Silence on the N = 0 case is not acceptable. "State updates" as a section header without this declaration is not acceptable.

If N > 0, complete the table. The row count must match the declared N.

Required columns: State Key · Owner · Layer · Old Value Shape · New Value Shape · Mechanism

| State Key | Owner | Layer | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|-----------------|-----------------|-----------|
| *(exact key name — not "the state")* | *(component name or store slice)* | *(local / context / store)* | *(type or shape — not "previous")* | *(type or shape — not "updated")* | *(setState call / dispatch / store.set / etc.)* |

Invalid cell values: "state updates", "previous value", "new value", "N/A", "updates accordingly", blank.

---

**TABLE 4 · Re-render Inventory**

Required columns: T-ID · Component · Re-renders? · Reason · Necessary? · UR-ID

| T-ID | Component | Re-renders? | Reason | Necessary? | UR-ID |
|------|-----------|-------------|--------|------------|-------|
| T-01 | *(component from TABLE 2)* | Yes / No | *(owns state / receives new props / subscribes to changed context / no state owned / no props changed)* | Yes — [reason] / No — [reason] | *(UR-01, UR-02, … if unnecessary; "—" if necessary or no re-render)* |

Rules:
- **Every component assigned a T-ID in TABLE 2 must appear in this table.** No T-ID may be silently dropped. If a traversal component does not re-render, it still requires a row with Re-renders? = No and the reason.
- "Several components re-render" does not satisfy any row.
- Components annotated as unnecessary get a UR-ID. These IDs must appear in TABLE 7 F-02 with a named fix.

**PROMOTION BLOCK (mandatory regardless of outcome):**

```
Unnecessary re-renders: [count]
UR-IDs requiring findings entry: [list, or "none"]
```

---

**TABLE 5 · Side Effects**

Required columns: Type · Trigger · Mechanism · Timing · Cleanup

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / DOM mutation / none)* | *(handler or hook that initiates it)* | *(fetch / setTimeout / addEventListener / router.push / etc.)* | *(synchronous / microtask / macrotask)* | *(yes — how / no / N/A)* |

If no side effects, the table must contain exactly one row:

```
| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |
```

Silence is not acceptable.

---

**TABLE 6 · Final UI State — Four-Phase Progression**

Required columns: Phase · UI State · Visible Elements · Disabled/Enabled · User Perception

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | *(what the user saw before the event)* | | | |
| 2 · Synchronous / optimistic | *(immediate UI change after event fires)* | | | |
| 3 · Async success | *(UI after async resolves successfully)* | | | |
| 4 · Async error | *(UI after async rejects or times out)* | | | |

Invalid cell values: "UI updates accordingly", "reflects state changes", "success and error handled", blank.
All four rows are required. A three-phase section that collapses rows 3 and 4 does not pass.

---

**TABLE 7 · Findings**

Required rows (all five are mandatory — N/A is prohibited in any cell):

| ID | Category | Component / State Path | Finding | Fix — API or Pattern |
|----|----------|----------------------|---------|---------------------|
| F-01 | Render performance / unnecessary re-renders | | *(finding or "none detected — [reason]")* | *(named API or "n/a — no issue")* |
| F-02 | Unnecessary re-renders — UR cross-reference | *(list each UR-ID from TABLE 4 PROMOTION BLOCK)* | *(finding per UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* |
| F-03 | Accessibility | | *(finding or "none detected — [reason]")* | |
| F-04 | Async error handling | | *(finding or "none detected — [reason]")* | |
| F-05 | Memory leaks | | *(finding or "none detected — [reason]")* | |

Every UR-ID from the PROMOTION BLOCK in TABLE 4 must appear in F-02 with a named API or pattern fix. If the PROMOTION BLOCK lists "none", F-02 states "none — no unnecessary re-renders detected" in the Finding column.

---

**CLOSING MANDATE**: Replace every generic term with its framework-specific equivalent. "State management layer" → Redux store / Pinia store / Zustand store / NgRx store (as declared). "Component lifecycle" → `useEffect` / `mounted` / `ngOnInit` (as declared). Generic vocabulary after declaration fails this output.

---

## V-02 · Lifecycle Emphasis — Phase-Gated with Blocking Exit Conditions

**Axis**: Lifecycle emphasis (explicit phase gates)
**Hypothesis**: Blocking exit conditions that require C-27, C-28, and C-29 compliance before phase advance turn these into enforced gates rather than aspirational guidelines. A phase cannot close until its exit condition is satisfied — making elision structurally visible.

---

You are a frontend domain expert. Identify the framework and state management library before proceeding.

**Phase 0 — Framework Declaration**

Declare before any analysis:
- Framework name (React, Vue, Angular, Svelte, or other — exact)
- State management library (Redux, Zustand, Pinia, NgRx, Context API, none — exact)
- Component model (functional hooks, class components, Options API, Composition API, other)

*Phase 0 exit condition*: Framework, state management, and component model are all named. Analysis cannot begin until this phase is complete.

---

**Phase 1 — Event Anchor**

Name the exact event that triggered the trace:
1. Event type (click, submit, input, change, etc.)
2. Exact component name that fired it — not "the button" or "the input"
3. Handler function name — not "the handler"
4. Event payload or input value (if relevant)
5. File and line where the handler is defined

*Phase 1 exit condition*: Event type, component name, and handler function are all explicitly named. Proceeding without these three fields fails Phase 1.

---

**Phase 2 — Component Tree Traversal**

Trace the path of the action through the component hierarchy. For each hop:
1. Name the component
2. Annotate the direction at that specific hop: `↑ upward propagation`, `↓ downward prop-passing`, `context injection`, or `event delegation`
3. Name the mechanism (callback prop, context hook, HOC wrapper, etc.)

The direction annotation is required **per hop** — not once as a summary. A traversal that names components but assigns direction only to the overall path does not close this phase. Minimum two named components with individual direction annotations.

Assign each component a Traversal ID (T-01, T-02, …) for use in Phase 4.

*Phase 2 exit condition*: At least two hops listed, each with its own direction annotation. No T-ID may be left unassigned.

---

**Phase 3 — State Update Map**

Open with the mutation count pre-declaration:

```
Mutation count: N = ___
```

If N = 0:

```
ZERO MUTATION DECLARATION
Reason: [name the reason — read-only, display-only, consumed without dispatch]
Confirmation: No local useState, no context write, no store dispatch triggered.
```

Do not proceed to the mutation table if N = 0. Silence on the zero-mutation case is not acceptable.

If N > 0, list each mutation with: state key, owner (component or store slice), layer (local / context / store), old value shape, new value shape, mechanism. The row count must equal the declared N.

Invalid descriptions: "state updates", "previous value", "updates accordingly", "the store is modified".

*Phase 3 exit condition*: Mutation count pre-declaration present. Either zero-mutation declaration complete or mutation table with N rows matching declared count. Generic terms absent.

---

**Phase 4 — Re-render Inventory**

For every component assigned a T-ID in Phase 2, give a verdict:
- Re-renders: Yes — reason (owns state / receives new props / subscribes to changed context)
- Re-renders: No — reason (no state owned / no props changed / not subscribed to changed context)

No T-ID from Phase 2 may be silently dropped. A re-render list that names fewer components than the traversal without explicit non-render verdicts for the missing ones does not close this phase.

For each re-render, annotate necessity: necessary (reason) or unnecessary (reason). Assign a UR-ID (UR-01, UR-02, …) to each unnecessary re-render.

Close with a mandatory PROMOTION BLOCK:

```
Unnecessary re-renders: [count]
UR-IDs requiring findings entry: [list or "none"]
```

*Phase 4 exit condition*: Every T-ID has a verdict. Every unnecessary re-render has a UR-ID. PROMOTION BLOCK present.

---

**Phase 5 — Side Effects**

Identify every side effect triggered by the action: API calls, timers, subscriptions, navigation, DOM mutations.

For each: name the type, the trigger mechanism, timing (synchronous / microtask / macrotask), and cleanup path if any.

If none: write explicitly — "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation triggered by this action." Silence is not acceptable.

*Phase 5 exit condition*: Either at least one side effect documented with mechanism, or an explicit no-side-effects declaration.

---

**Phase 6 — Final UI State**

Describe the observable UI across four phases in order:

1. **Pre-action baseline** — what the user saw before the event
2. **Synchronous / optimistic update** — immediate UI change after event fires
3. **Async success** — UI after async resolves
4. **Async error** — UI after async rejects or times out

For each phase: visible elements, disabled/enabled states, user perception. "UI updates accordingly", "reflects state changes", and "success and error handled" are not acceptable — name what the user sees.

*Phase 6 exit condition*: All four phases present. Each phase contains at least one concrete visible element description. Phases 3 and 4 are not collapsed.

---

**Phase 7 — Findings**

Run a five-category sweep. Each category must appear with either a concrete finding or an explicit "none detected — [brief reason]" confirmation. Silence on any category is not acceptable.

Categories:
1. **Render performance / unnecessary re-renders** — connect to Phase 4 UR-IDs
2. **UR cross-reference** — for each UR-ID from the PROMOTION BLOCK, name the fix: specific API or pattern (`React.memo`, `createSelector`, `computed` with stable deps, `useMemo`, etc.)
3. **Accessibility** — ARIA roles, keyboard navigation, focus management
4. **Async error handling** — loading states, error boundaries, timeout handling
5. **Memory leaks** — subscription cleanup, timer cancellation, event listener removal

Every UR-ID from Phase 4's PROMOTION BLOCK must appear here with a named fix. If "none" was declared, state "no unnecessary re-renders detected" in the UR cross-reference row.

*Phase 7 exit condition*: All five categories addressed. Every UR-ID cross-referenced with a named fix.

---

**Closing**: Use framework-specific vocabulary throughout. After the Phase 0 declaration, replace all generic terms: "state management layer" → the declared library name, "component lifecycle" → the framework's specific hooks or methods.

---

## V-03 · Phrasing Register — Formal/Technical Vocabulary, Instruction-Driven

**Axis**: Phrasing register (formal/technical, imperative instructions without structural schemas)
**Hypothesis**: Technical precision and framework-specific vocabulary improve output quality on straightforward cases, but lack of structural enforcement creates reliability gaps on edge cases (zero-mutation, per-hop annotations, traversal completeness). Expected to score lower on C-27/C-28/C-29 than schema-driven variations.

---

You are a senior frontend engineer conducting a component trace analysis. Apply rigorous technical vocabulary throughout this analysis — use framework-specific terms wherever a generic alternative would be imprecise.

Begin by declaring the framework and state management library. Name them exactly: React with Redux Toolkit, Vue 3 with Pinia, Angular with NgRx, etc. Do not use generic terms after this declaration.

**Event Analysis**

Identify the initiating event with precision. Name the DOM event type, the React component (or Vue component, or Angular component) that owns the event binding, the exact event handler function, and the payload or synthetic event properties that drive the subsequent behavior. Do not describe "the button" — name the component. Do not describe "the handler" — name the function.

**Component Hierarchy Traversal**

Trace the event's path through the component hierarchy. At each step, name the component and describe the mechanism by which control flows — upward via callback props, downward via prop drilling, through a context provider, via event delegation, or through a Higher-Order Component wrapper. Annotate the direction at each step individually; a single direction summary for the whole traversal is insufficient.

The traversal must cover at minimum two named components. Document each hop in sequence, preserving the structural parent→child or leaf→provider relationship.

**State Mutation Analysis**

Declare upfront the total number of state mutations this action produces. Then document each mutation: the state key or slice name, the component or store that owns it, whether it is local component state (`useState`, `this.setState`, `ref`), context state, or store state (Redux slice, Pinia store, Zustand store, NgRx action), the shape of the old value, and the shape of the new value.

If the action produces zero mutations, state this explicitly: name the reason (read-only operation, display-only component, event consumed without store dispatch) and confirm that no `useState`, context write, or store dispatch was triggered. Do not leave this case undocumented.

Prohibited phrases: "state updates", "the state changes", "the store is modified without naming the key", "updates accordingly".

**Re-render Analysis**

For each component in the traversal, determine whether it re-renders as a result of the state changes. Provide a verdict for every component named in the traversal — including components that do not re-render. A re-render analysis that accounts for fewer components than the traversal leaves unexplained gaps.

For each re-render: name the component, state whether the re-render is necessary or unnecessary, and give the reason (owns changed state, receives new props, subscribes to changed context — or for unnecessary: missing memoization, selector too broad, context subscription too coarse).

Assign a short identifier to each unnecessary re-render (UR-01, UR-02, etc.) and note that these require remediation recommendations.

**Side Effect Analysis**

Document every side effect triggered by this action: API calls (named endpoint and HTTP method), timer scheduling (`setTimeout`, `setInterval`), subscription creation, navigation events, or DOM mutations outside the component tree. For each, name the mechanism and note whether cleanup is performed.

If no side effects occur, state this explicitly: "No side effects — this action is synchronous and produces no API calls, timers, subscriptions, or navigation."

**Final UI State**

Describe the observable UI across four temporal stages:
1. The baseline state before the action
2. The immediate synchronous change visible to the user
3. The state after asynchronous resolution (success path)
4. The state after asynchronous rejection or timeout (error path)

For each stage, describe the visible elements, any disabled or enabled controls, and what the user perceives. Prohibited closings: "UI updates accordingly", "the UI reflects the state changes", "success and error states are handled".

**Findings**

Conduct a structured review across five issue categories. For each category, name any issues found. If no issues are found in a category, state "none detected" and give a brief reason rather than leaving the category unaddressed.

Categories:
1. Unnecessary re-renders — for each UR-ID identified above, recommend a specific fix using a named API or pattern (`React.memo`, `useMemo`, `useCallback`, `createSelector`, `Pinia computed`, `NgRx createSelector`, etc.)
2. Missing loading states
3. Error state gaps
4. Accessibility failures (ARIA, keyboard navigation, focus management)
5. Memory leaks (unremoved subscriptions, uncancelled timers)

Use framework-specific API names in all recommendations.

---

## V-04 · Role Sequence — Developer Role then Auditor Role

**Axis**: Role sequence (developer produces trace, auditor verifies completeness against C-27/C-28/C-29 requirements)
**Hypothesis**: A dedicated auditor role that explicitly checks mutation-count pre-declaration, per-hop direction annotations, and traversal completeness catches gaps the developer role produces under time pressure. Role handoff creates a second-pass verification that structured tables achieve through schema shape. Expected to match V-01 on essentials and recommended; may close aspirational gaps via deliberate multi-perspective coverage.

---

You will complete this trace in two roles executed sequentially. Do not blend the roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — Frontend Developer**

You are a frontend developer who built this feature. Produce the trace from your implementation knowledge.

Declare your framework and state management library before beginning. Name them exactly.

**1.1 Event**

Name the event that triggered this trace: event type, exact component name, exact handler function name, event payload, file location. "The button" and "the handler" are not valid component or function names.

**1.2 Component Traversal**

Trace the path through the component hierarchy. For each hop, name the component and the direction of flow at that specific hop:
- `↑ upward propagation` — event bubbles up or callback is invoked
- `↓ downward prop-passing` — parent passes updated props to child
- `context injection` — component reads from context provider
- `event delegation` — event handled by parent on behalf of child

Direction must be stated per hop, not once for the whole path. Assign each component a Traversal ID: T-01, T-02, etc.

**1.3 State Mutations**

Before listing mutations, write:

```
Mutation count: N = ___
```

If N = 0, write the zero-mutation declaration:

```
ZERO MUTATION DECLARATION
Reason: [read-only / display-only / event consumed without dispatch]
Confirmation: No useState, no context write, no store dispatch.
```

If N > 0, list each mutation: state key, owner, layer (local / context / store), old value shape, new value shape, dispatch mechanism. Row count must match N.

**1.4 Re-renders**

For every T-ID from section 1.2, give a verdict: re-renders (yes/no), reason, and necessity annotation (necessary — reason / unnecessary — reason). Assign UR-IDs to unnecessary re-renders.

No T-ID may be omitted.

**1.5 Side Effects**

List every side effect: type, trigger, mechanism, timing, cleanup. If none, state: "No side effects — synchronous only."

**1.6 Final UI State**

Describe four phases: pre-action, synchronous update, async success, async error. For each: visible elements, control states, user perception.

---

**ROLE 2 — Performance Auditor**

You are a performance-focused frontend auditor. Your job is to verify the developer's trace is complete and correct, identify issues the developer may have missed, and produce the findings section.

Begin with a compliance check:

**2.0 Trace Completeness Audit**

| Check | Result | Notes |
|-------|--------|-------|
| Mutation count pre-declaration present? | Pass / Fail | *(section 1.3)* |
| Every traversal hop has its own direction annotation? | Pass / Fail | *(section 1.2)* |
| Every T-ID appears in re-render section with verdict? | Pass / Fail | *(sections 1.2 + 1.4)* |
| Zero-mutation declaration present when N = 0? | Pass / Fail / N/A | |
| Side effect section present (including "none" declaration)? | Pass / Fail | |
| Final UI state covers all four phases? | Pass / Fail | |

If any check fails, note the gap. Do not alter the developer's output — flag the deficiency for the record.

**2.1 Findings Table**

Required rows — N/A prohibited:

| ID | Category | Component / Path | Finding | Fix — Named API or Pattern |
|----|----------|-----------------|---------|---------------------------|
| F-01 | Render performance | | *(finding or "none detected — reason")* | |
| F-02 | Unnecessary re-renders | *(list each UR-ID)* | *(per-UR-ID finding or "none")* | *(React.memo / createSelector / computed / useMemo — named)* |
| F-03 | Accessibility | | *(finding or "none detected — reason")* | |
| F-04 | Async error handling | | *(finding or "none detected — reason")* | |
| F-05 | Memory leaks | | *(finding or "none detected — reason")* | |

Every UR-ID from section 1.4 must appear in F-02 with a named fix.

**2.2 Framework Vocabulary Check**

List any generic terms found in the developer's output that should be replaced by framework-specific equivalents. If none, state: "No generic term substitutions required — developer output uses framework-specific vocabulary throughout."

---

## V-05 · Inertia Framing + Output Format — Change/No-Change Symmetry with Tables

**Axis**: Inertia framing (stable components and state documented symmetrically alongside mutations) combined with schema-enforced tables
**Hypothesis**: Documenting what did NOT change (inertia) symmetrically with what did change makes the zero-mutation case first-class, makes traversal completeness visible (T-IDs without re-renders explicitly documented as "held inert"), and makes per-hop annotations natural (direction = "inert" is a valid direction when a component passes through without acting). Expected to match V-01 on C-27/C-28/C-29 through a different structural mechanism while adding coverage for the "what didn't change" dimension that helps several C-09–C-23 aspirational criteria.

---

You are a frontend domain expert. This trace documents both **what changed** and **what held inert** as a result of the user action. Both sides carry equal analytical weight — the inertia map is not a gap; it is a required output.

**FRAMEWORK DECLARATION**

| Field | Value |
|-------|-------|
| Framework | `[exact name]` |
| State management | `[exact name]` |
| Component model | `[exact model]` |

---

**TABLE 1 · Event Anchor**

| Event Type | Component Name | Handler Function | Payload | File Location |
|------------|---------------|-----------------|---------|---------------|
| | *(exact — not "the button")* | *(exact — not "the handler")* | | |

---

**TABLE 2 · Component Tree Traversal — Change/Inertia Map**

Every component in the traversal path must be listed. For each component, annotate whether it **acted** (handled, transformed, or propagated the event) or **held inert** (was traversed but took no action).

Required columns: Step · T-ID · Component · Direction · Role · Notes

| Step | T-ID | Component | Direction | Role | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | | `↑ upward propagation` \| `↓ downward prop-passing` \| `context injection` \| `event delegation` \| `↔ inert pass-through` | **Acted**: [what it did] \| **Inert**: [why no action] | |

Rules:
- Direction is required **per row**. `↔ inert pass-through` is the correct direction for components that transmit without acting.
- Role column must contain either "Acted: [description]" or "Inert: [reason]" — not blank, not "N/A".
- Assign T-IDs to all rows. T-IDs feed TABLE 4.

---

**TABLE 3 · State Mutation Map — Change Side**

**MUTATION COUNT PRE-DECLARATION:**

```
State change count: N = ___     [count of mutated keys]
State inertia count: M = ___    [count of state keys that could have changed but did not]
```

Declare both N and M before the tables. N = 0 requires a ZERO MUTATION DECLARATION:

```
ZERO MUTATION DECLARATION
Reason: [name the reason]
Confirmation: No local state, no context, no store state was written.
```

If N > 0, list mutations (row count must equal N):

| State Key | Owner | Layer | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|-----------------|-----------------|-----------|

---

**TABLE 3b · State Inertia Map — Inertia Side**

Document state that was read but not written, or state that was evaluated as a dispatch guard but remained unchanged. M = 0 is acceptable; write "No state was evaluated and left unchanged."

| State Key | Owner | Layer | Reason Held Inert |
|-----------|-------|-------|-------------------|

---

**TABLE 4 · Re-render Inventory — Change/Inertia Completeness**

Every T-ID from TABLE 2 must appear. Components that held inert in TABLE 2 are still expected here — they may re-render due to props or context even if they took no action.

Required columns: T-ID · Component · Re-renders? · Reason · Necessary? · UR-ID

| T-ID | Component | Re-renders? | Reason | Necessary? | UR-ID |
|------|-----------|-------------|--------|------------|-------|
| T-01 | | Yes / No | *(owns state / receives new props / subscribes to context / no state / no props changed)* | Yes — [reason] / No — [reason] | *(UR-ID or —)* |

No T-ID may be dropped. Inert components with no re-render require a row with Re-renders? = No.

**PROMOTION BLOCK:**

```
Unnecessary re-renders: [count]
UR-IDs requiring findings entry: [list or "none"]
```

---

**TABLE 5 · Side Effects — Change/Inertia Declaration**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|

If none: one row — `| none | — | No side effects. | — | — |`. Silence not acceptable.

---

**TABLE 6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Control States | User Perception |
|-------|----------|-----------------|---------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

All four rows required. Invalid cells: "UI updates accordingly", "reflects state changes", blank.

---

**TABLE 7 · Findings**

| ID | Category | Component / Path | Finding | Fix |
|----|----------|-----------------|---------|-----|
| F-01 | Render performance | | *(finding or "none detected — reason")* | |
| F-02 | Unnecessary re-renders — UR cross-reference | *(each UR-ID from PROMOTION BLOCK)* | *(per-UR-ID or "none")* | *(named API/pattern)* |
| F-03 | Accessibility | | *(finding or "none detected — reason")* | |
| F-04 | Async error handling | | *(finding or "none detected — reason")* | |
| F-05 | Memory leaks | | *(finding or "none detected — reason")* | |

N/A prohibited in any cell. Every UR-ID must appear in F-02 with a named fix.

---

**CLOSING MANDATE**: After the Framework Declaration, all generic terms are replaced by their declared equivalents. The inertia map is not optional — undocumented inertia is an incomplete trace, not a shorter one.

---

## Variation Summary

| V# | Axis | Primary Mechanism for C-27/C-28/C-29 | Expected Strength | Expected Gap |
|----|------|--------------------------------------|-------------------|--------------|
| V-01 | Output format (schema tables) | Schema field shape — mutation count field, direction column, T-ID completeness rule | Structural elision prevention; highest aspiraional floor | Minor gaps in lifecycle hook specificity |
| V-02 | Lifecycle emphasis (phase gates) | Blocking exit conditions per phase | Clear progression; direction-per-hop is a Phase 2 exit condition | Exit conditions softer than schema fields; model may satisfy in prose with less specificity |
| V-03 | Phrasing register (formal/technical) | Instruction-driven; no schema enforcement | Framework vocabulary strongest here | Zero-mutation silence not blocked; per-hop direction not enforced; traversal completeness not enforced |
| V-04 | Role sequence (developer + auditor) | Auditor TABLE 2.0 compliance check explicitly verifies C-27/C-28/C-29 | Second-pass verification catches gaps; auditor role adds deliberate coverage | Compliance check is after-the-fact — gaps are flagged but not prevented |
| V-05 | Inertia framing + output format | Inertia columns make T-ID completeness first-class; `↔ inert pass-through` makes per-hop annotation natural; N+M count makes zero-mutation explicit | Symmetric change/inertia framing adds structural dimension for zero-mutation and traversal completeness | Extra complexity may distract from core requirements on simple traces |
