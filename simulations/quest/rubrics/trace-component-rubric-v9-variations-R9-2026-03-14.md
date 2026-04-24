# trace-component — Round 9 Variations

**Variation axes used:**
- Single-axis: Output format (V-01), Lifecycle emphasis (V-02), Inertia framing — targeted extraction (V-03)
- Combined: Output format + Role sequence (V-04), Lifecycle emphasis + Phrasing register (V-05)

**R9 context:** Three new criteria were promoted from R8 excellence signals: C-30 (Mutation Count Dual-Track — direct vs. inherited mutations absorbed into existing TABLE 3 without a sub-table), C-31 (Schema-Field Coverage of Aspirational Criteria — C-20 through C-29 must map to schema-enforced fields, 7+ of 10 to pass), and C-32 (Blank-Blocked Field Primacy — C-01 through C-05 essentials must be backed by blank-blocked fields, 3+ of 5 to pass). The R8 prevention > detection > instruction hierarchy is now a graded first-class criterion. All five variations must address C-30/C-31/C-32.

R8 V-01 scored 128/132; new ceiling is 138. R8 V-01 already implicitly satisfies C-31 (all 10 of C-20–C-29 mapped to schema fields) and C-32 (all 5 essentials backed by blank-blocked columns). The sole new gap is C-30. All R9 variations evolve from R8's strongest patterns.

---

## V-01 · Output Format — Schema Evolution with C-30 Dual Mutation Count

**Axis**: Output format (schema-enforced tables evolved for C-30/C-31/C-32)
**Hypothesis**: R8 V-01 already satisfies C-31 (C-20–C-29 all mapped to schema fields) and C-32 (all five essentials backed by blank-blocked table columns) through its existing structure. The sole gap is C-30. Adding `N=___ direct, M=___ inherited` to the TABLE 3 mutation pre-declaration and a `Type` column to the mutation table body satisfies C-30 at zero proliferation cost — no new table, no TABLE 3b, just one revised pre-declaration line and one new column. The self-reinforcing pipeline should close the remaining 4-point gap from R8 (26→28 on C-09–C-23, plus 6 pts from C-30/C-31/C-32). Expected score: 134–136/138.

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
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact component name — not "the button")* | *(exact function name — not "the handler")* | *(value / object shape / "none")* | *(path:line)* |

Invalid cell values: "the button", "a click", "the handler", "N/A", blank. If the handler is an inline arrow function, name the prop and describe the function body in one line.

---

**TABLE 2 · Component Tree Traversal**

Required columns: Step · T-ID · Component · Direction · Mechanism · Notes

| Step | T-ID | Component | Direction | Mechanism | Notes |
|------|------|-----------|-----------|-----------|-------|
| 1 | T-01 | *(leaf component receiving event)* | `↑ upward propagation` | *(event handler call / callback prop)* | |
| 2 | T-02 | *(next component in path)* | `↑ upward propagation` \| `↓ downward prop-passing` \| `context injection` \| `event delegation` | *(prop name / context hook / HOC wrapper)* | |
| … | | | | | |

Rules:
- Minimum two rows. A single-row traversal does not satisfy this table.
- **Direction is required per row** — not once as a summary statement. Permitted values: `↑ upward propagation`, `↓ downward prop-passing`, `context injection`, `event delegation`. Blank direction cells do not pass.
- T-IDs (T-01, T-02, …) assigned here are the canonical IDs cross-referenced in TABLE 4. Every T-ID from this table must appear in TABLE 4 with a verdict.

---

**TABLE 3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION (required, appears before table body):**

```
Mutations: N=___ direct, M=___ inherited  (total: ___)
```

Definitions:
- **Direct mutations** — state writes produced immediately by the event handler or synchronous code it calls.
- **Inherited mutations** — state writes triggered transitively: `useEffect` reactions, `watch` / `watchEffect` callbacks, `ngOnChanges` lifecycle, computed property cascades, store middleware, or subscription side-effects that fire in response to direct mutations.

If total = 0, skip the table body and write instead:

```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only operation / display-only component / event consumed without dispatch / other]
```

Silence on the zero-mutation case is not acceptable. "State updates" as a section header without this declaration is not acceptable.

If total > 0, complete the table. Row count must match declared total (N + M).

Required columns: State Key · Owner · Layer · Type · Old Value Shape · New Value Shape · Mechanism

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key — not "the state")* | *(component name or store slice)* | *(local / context / store)* | *(direct / inherited)* | *(type or shape — not "previous")* | *(type or shape — not "updated")* | *(setState / dispatch / store.set / useEffect trigger / watcher / etc.)* |

Invalid cell values: "state updates", "previous value", "new value", "N/A", "updates accordingly", blank.

---

**TABLE 4 · Re-render Inventory**

Required columns: T-ID · Component · Re-renders? · Reason · Necessary? · UR-ID

| T-ID | Component | Re-renders? | Reason | Necessary? | UR-ID |
|------|-----------|-------------|--------|------------|-------|
| T-01 | *(component from TABLE 2)* | Yes / No | *(owns state / receives new props / subscribes to changed context / no state owned / no props changed)* | Yes — [reason] / No — [reason] | *(UR-01, UR-02, … if unnecessary; "—" if necessary or no re-render)* |

Rules:
- **Every T-ID from TABLE 2 must appear in this table.** No T-ID may be silently dropped. Traversal components that do not re-render still require a row with Re-renders? = No and the reason.
- "Several components re-render" does not satisfy any row.
- Unnecessary re-renders receive UR-IDs. Every UR-ID must appear in TABLE 7 F-02 with a named fix.

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

If no side effects exist, the table must contain exactly one row:

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

Invalid cell values: "UI updates accordingly", "reflects state changes", "success and error handled", blank. All four rows are required. A three-phase section that collapses rows 3 and 4 does not pass.

---

**TABLE 7 · Findings**

Required rows — N/A is prohibited in any cell:

| ID | Category | Component / State Path | Finding | Fix — API or Pattern |
|----|----------|----------------------|---------|---------------------|
| F-01 | Render performance / unnecessary re-renders | | *(finding or "none detected — [reason]")* | *(named API or "n/a — no issue")* |
| F-02 | Unnecessary re-renders — UR cross-reference | *(list each UR-ID from TABLE 4 PROMOTION BLOCK)* | *(finding per UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* |
| F-03 | Accessibility | | *(finding or "none detected — [reason]")* | |
| F-04 | Async error handling | | *(finding or "none detected — [reason]")* | |
| F-05 | Memory leaks | | *(finding or "none detected — [reason]")* | |

Every UR-ID from the TABLE 4 PROMOTION BLOCK must appear in F-02 with a named API or pattern fix. If the PROMOTION BLOCK lists "none", F-02 states "none — no unnecessary re-renders detected" in the Finding column.

---

**CLOSING MANDATE**: After the Framework Declaration, replace all generic terms with declared equivalents. "State management layer" → Redux store / Pinia store / Zustand store / NgRx store. "Component lifecycle" → `useEffect` / `mounted` / `ngOnInit`. Generic vocabulary after declaration fails this output.

---

## V-02 · Lifecycle Emphasis — Phase-Gated with Per-Phase Schema Field Manifests

**Axis**: Lifecycle emphasis (phase gates with explicit per-phase schema field manifests)
**Hypothesis**: R8 V-02 scored 125/132 — 3 pts below V-01 on aspirational. The gap came from exit conditions being softer than schema columns (prose-stated exits allow more interpretation slack). R9 V-02 adds a per-phase **schema field manifest** — a parenthetical at each phase header listing exactly which table columns that phase enforces and which criteria they satisfy. This makes C-31 and C-32 compliance explicit and visible at each phase boundary, tightening exit condition precision without switching to pure schema tables. The dual mutation count is added to Phase 3's exit condition and declaration. Expected score: 130–133/138.

---

You are a frontend domain expert. Identify the framework and state management library before proceeding.

**Phase 0 — Framework Declaration**
*(Schema fields enforced: Framework, State management, Component model — required header cells, blank not accepted. Satisfies C-20 (Framework Declaration Gate), C-32 (blank-blocked fields for analysis gate).)*

Declare before any analysis:
- Framework name (React, Vue, Angular, Svelte, or other — exact)
- State management library (Redux, Zustand, Pinia, NgRx, Context API, none — exact)
- Component model (functional hooks, class components, Options API, Composition API, other)

*Phase 0 exit condition*: All three fields named. Analysis cannot begin until this phase is complete.

---

**Phase 1 — Event Anchor**
*(Schema fields enforced: Event Type · Component Name · Handler Function · Event Payload · File Location — blank-blocked columns in TABLE 1. Satisfies C-01 (Event Anchor), C-32 (blank-blocked essential field).)*

Name the exact event that triggered the trace:
1. Event type (click, submit, input, change, etc.)
2. Exact component name that fired it — not "the button" or "the input"
3. Handler function name — not "the handler"
4. Event payload or input value (if relevant)
5. File and line where the handler is defined

*Phase 1 exit condition*: Event type, component name, and handler function are all explicitly named. Proceeding without these three fields fails Phase 1.

---

**Phase 2 — Component Tree Traversal**
*(Schema fields enforced: T-ID · Component · Direction · Mechanism — required columns with per-row Direction annotation. Satisfies C-02 (Component Tree Traversal), C-28 (Per-Hop Direction Annotation), C-29 (Re-render Inventory Completeness by Traversal — T-IDs assigned here become required rows in Phase 4), C-32 (blank-blocked essential field).)*

Trace the path of the action through the component hierarchy. For each hop:
1. Name the component
2. Annotate the direction at that specific hop: `↑ upward propagation`, `↓ downward prop-passing`, `context injection`, or `event delegation`
3. Name the mechanism (callback prop, context hook, HOC wrapper, etc.)

**The direction annotation is required per hop** — not once as a summary. A traversal that names components but assigns direction only to the overall path does not close this phase. Minimum two named components with individual direction annotations.

Assign each component a Traversal ID (T-01, T-02, …) for use in Phase 4.

*Phase 2 exit condition*: At least two hops listed, each with its own direction annotation. Every component has a T-ID assigned. No T-ID left unassigned.

---

**Phase 3 — State Update Map**
*(Schema fields enforced: State Key · Owner · Layer · Type · Old Value Shape · New Value Shape · Mechanism — required columns with invalid-value rules. Mutation Count Pre-Declaration is a required field. Type column (direct / inherited) carries C-30. Satisfies C-03 (State Update Map), C-24 (Zero-Mutation Declaration), C-27 (Mutation Count Pre-Declaration), C-30 (Mutation Count Dual-Track), C-31 (schema-field coverage).)*

Open with the mutation count pre-declaration:

```
Mutations: N=___ direct, M=___ inherited  (total: ___)
```

- **Direct mutations**: state writes produced immediately by the event handler or synchronous code it calls.
- **Inherited mutations**: state writes triggered transitively through `useEffect`, `watch`, `watchEffect`, `ngOnChanges`, computed cascades, store middleware, or subscriptions reacting to direct mutations.

If total = 0:

```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch]
```

Do not proceed to the mutation table if total = 0. Silence on the zero-mutation case is not acceptable.

If total > 0, list each mutation with: State Key, Owner (component or store slice), Layer (local / context / store), Type (direct / inherited), Old Value Shape, New Value Shape, Mechanism. Row count must equal declared total (N + M).

Invalid descriptions: "state updates", "previous value", "updates accordingly", "the store is modified".

*Phase 3 exit condition*: Mutation count pre-declaration with N (direct) + M (inherited) present. Either zero-mutation declaration complete, or mutation table with row count = N+M and no generic terms.

---

**Phase 4 — Re-render Inventory**
*(Schema fields enforced: T-ID · Component · Re-renders? · Reason · Necessary? · UR-ID — required columns, every T-ID from Phase 2 must appear. PROMOTION BLOCK is a required closing field. Satisfies C-04 (Re-render Inventory), C-22 (Re-render Necessity Annotation), C-26 (Unnecessary Re-render Promotion), C-29 (Re-render Inventory Completeness by Traversal), C-32 (blank-blocked essential field).)*

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
*(Schema fields enforced: Type · Trigger · Mechanism · Timing · Cleanup — required columns with mandatory "none" row if no side effects. Satisfies C-06 (Side Effect Coverage).)*

Identify every side effect triggered by the action: API calls, timers, subscriptions, navigation, DOM mutations.

For each: name the type, trigger mechanism, timing (synchronous / microtask / macrotask), and cleanup path if any.

If none: write explicitly — "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation triggered by this action." Silence is not acceptable.

*Phase 5 exit condition*: Either at least one side effect documented with mechanism and timing, or an explicit no-side-effects declaration.

---

**Phase 6 — Final UI State**
*(Schema fields enforced: Phase · UI State · Visible Elements · Disabled/Enabled · User Perception — four required rows, collapse of rows 3 and 4 not accepted, invalid-value list enforced. Satisfies C-05 (Final UI State), C-23 (Four-Phase UI Progression), C-32 (blank-blocked essential field).)*

Describe the observable UI across four phases in order:

1. **Pre-action baseline** — what the user saw before the event
2. **Synchronous / optimistic update** — immediate UI change after event fires
3. **Async success** — UI after async resolves
4. **Async error** — UI after async rejects or times out

For each phase: visible elements, disabled/enabled states, user perception. "UI updates accordingly", "reflects state changes", and "success and error handled" are not acceptable — name what the user sees.

*Phase 6 exit condition*: All four phases present. Each phase contains at least one concrete visible element description. Phases 3 and 4 are not collapsed.

---

**Phase 7 — Findings**
*(Schema fields enforced: ID · Category · Component/State Path · Finding · Fix — five required rows, N/A prohibited in any cell, UR-IDs cross-referenced. Satisfies C-07 (Issue Detection), C-09 (Fix Recommendations), C-25 (Issue Category Completeness), C-26 (Unnecessary Re-render Promotion).)*

Run a five-category sweep. Each category must appear with either a concrete finding or an explicit "none detected — [brief reason]" confirmation. Silence on any category is not acceptable.

Categories:
1. **Render performance / unnecessary re-renders** — connect to Phase 4 UR-IDs
2. **UR cross-reference** — for each UR-ID from the PROMOTION BLOCK, name the fix: `React.memo`, `createSelector`, `computed` with stable deps, `useMemo`, `Pinia computed`, `NgRx createSelector`, etc.
3. **Accessibility** — ARIA roles, keyboard navigation, focus management
4. **Async error handling** — loading states, error boundaries, timeout handling
5. **Memory leaks** — subscription cleanup, timer cancellation, event listener removal

Every UR-ID from Phase 4's PROMOTION BLOCK must appear here with a named fix. If "none" was declared, state "no unnecessary re-renders detected" in the UR cross-reference row.

*Phase 7 exit condition*: All five categories addressed. Every UR-ID cross-referenced with a named fix.

---

**Closing**: Use framework-specific vocabulary throughout. After Phase 0, replace all generic terms: "state management layer" → the declared library name, "component lifecycle" → the framework's specific hooks or methods.

---

## V-03 · Inertia Framing — Targeted Extraction (No TABLE 3b)

**Axis**: Inertia framing, reduced to targeted extraction
**Hypothesis**: R8 V-05 scored 126/132 — 2 pts below V-01 — because TABLE 3b (State Inertia Map) introduced complexity that depressed C-09–C-23 aspirational coherence (24 vs. 26 out of 30). The N+M dual count was structurally richer than V-01's single N but the sub-table was the wrong vehicle for it. R9 V-03 extracts only what was valuable: (1) `↔ inert pass-through` direction in TABLE 2 — making traversal of non-acting components structurally expected rather than an edge case, and (2) N+M dual count in the mutation pre-declaration as C-30 now formally requires — but absorbed directly without a separate inertia table. Drop TABLE 3b entirely. The "inertia side" lives only in the Type column (direct / inherited) in TABLE 3 and in the `↔ inert pass-through` option in TABLE 2. Expected score: 132–135/138.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding. All output uses that framework's exact terminology — no generic substitutions. **This trace documents both what changed and what held inert as a result of the user action.** Inert components and unconsumed state paths are expected output, not gaps.

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
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact component name — not "the button")* | *(exact function name — not "the handler")* | *(value / object shape / "none")* | *(path:line)* |

Invalid cell values: "the button", "a click", "the handler", "N/A", blank.

---

**TABLE 2 · Component Tree Traversal — Acted / Inert Map**

Every component in the traversal path must be listed. Components that were traversed but took no action receive `↔ inert pass-through` as their direction — this is not a gap; it is a required annotation.

Required columns: Step · T-ID · Component · Direction · Role · Notes

| Step | T-ID | Component | Direction | Role | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | `↑ upward propagation` | **Acted**: [what it did] | |
| 2 | T-02 | *(next component)* | `↑ upward propagation` \| `↓ downward prop-passing` \| `context injection` \| `event delegation` \| `↔ inert pass-through` | **Acted**: [description] \| **Inert**: [why no action] | |
| … | | | | | |

Rules:
- **Direction is required per row.** `↔ inert pass-through` is the correct direction for components that transmit without acting — its presence is not a failure signal.
- **Role column must contain** either "Acted: [description]" or "Inert: [reason]" — not blank, not "N/A".
- Minimum two rows. T-IDs (T-01, T-02, …) feed TABLE 4. Every T-ID must appear in TABLE 4.

---

**TABLE 3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION (required, appears before table body):**

```
Mutations: N=___ direct, M=___ inherited  (total: ___)
```

- **Direct mutations** — state writes produced immediately by the event handler or synchronous code it calls.
- **Inherited mutations** — state writes triggered transitively through `useEffect`, `watch`, computed cascades, store middleware, or subscriptions reacting to direct mutations.

If total = 0, skip the table body and write:

```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch]
```

Silence on the zero-mutation case is not acceptable.

If total > 0, complete the table. Row count must match declared total (N + M).

Required columns: State Key · Owner · Layer · Type · Old Value Shape · New Value Shape · Mechanism

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store slice)* | *(local / context / store)* | *(direct / inherited)* | *(shape — not "previous")* | *(shape — not "updated")* | *(setState / dispatch / useEffect trigger / watcher / etc.)* |

Invalid cell values: "state updates", "previous value", "new value", "N/A", "updates accordingly", blank.

---

**TABLE 4 · Re-render Inventory**

Required columns: T-ID · Component · Re-renders? · Reason · Necessary? · UR-ID

| T-ID | Component | Re-renders? | Reason | Necessary? | UR-ID |
|------|-----------|-------------|--------|------------|-------|
| T-01 | *(component from TABLE 2)* | Yes / No | *(owns state / receives new props / subscribes to changed context / no state owned / no props changed)* | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

Rules:
- **Every T-ID from TABLE 2 must appear in this table.** Inert-pass-through components still require a row — they may re-render due to prop or context changes even though they did not act on the event.
- No T-ID may be silently dropped. Re-renders? = No still requires a reason.

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
| *(API call / timer / subscription / navigation / DOM mutation / none)* | | | *(synchronous / microtask / macrotask)* | |

If no side effects: one mandatory row — `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`. Silence not acceptable.

---

**TABLE 6 · Final UI State — Four-Phase Progression**

Required columns: Phase · UI State · Visible Elements · Disabled/Enabled · User Perception

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

All four rows required. Invalid cells: "UI updates accordingly", "reflects state changes", blank.

---

**TABLE 7 · Findings**

Required rows — N/A prohibited in any cell:

| ID | Category | Component / State Path | Finding | Fix — API or Pattern |
|----|----------|----------------------|---------|---------------------|
| F-01 | Render performance | | *(finding or "none detected — [reason]")* | |
| F-02 | Unnecessary re-renders — UR cross-reference | *(each UR-ID from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* |
| F-03 | Accessibility | | *(finding or "none detected — [reason]")* | |
| F-04 | Async error handling | | *(finding or "none detected — [reason]")* | |
| F-05 | Memory leaks | | *(finding or "none detected — [reason]")* | |

Every UR-ID from the PROMOTION BLOCK must appear in F-02 with a named fix.

---

**CLOSING MANDATE**: After the Framework Declaration, all generic terms are replaced by declared equivalents. Inert components are not omitted — undocumented inertia is an incomplete trace, not a shorter one.

---

## V-04 · Output Format + Role Sequence — Schema Tables with Targeted C-30/C-31/C-32 Auditor

**Axis**: Output format (V-01 schema tables) + Role sequence (trimmed compliance auditor)
**Hypothesis**: R8 V-04's auditor was full-size — it required the auditor to produce a complete trace independently, which introduced coherence penalties (the auditor's secondary trace added structural noise rather than value). R9 V-04 keeps Role 1 as V-01's full schema trace and reduces Role 2 to a single-purpose compliance table that only checks C-30/C-31/C-32 — three specific cells per check, not a full trace re-run. This targets the new criteria with after-the-fact verification at minimal coherence cost, testing whether a trimmed auditor preserves V-01's 128 baseline while adding verification value for the new criteria. Expected score: 130–134/138.

---

You will complete this trace in two roles executed sequentially. Do not blend the roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — Frontend Developer**

You are a frontend developer who built this feature. Produce the complete trace.

**Framework Declaration (required header)**

| Field | Value |
|-------|-------|
| Framework | `[exact name]` |
| State management | `[exact name]` |
| Component model | `[exact model]` |

Do not begin analysis until this header is complete.

---

**TABLE 1 · Event Anchor**

Required columns: Event Type · Component Name · Handler Function · Event Payload · File Location

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| | *(exact — not "the button")* | *(exact — not "the handler")* | | |

Invalid cell values: "the button", "a click", "the handler", "N/A", blank.

---

**TABLE 2 · Component Tree Traversal**

Required columns: Step · T-ID · Component · Direction · Mechanism · Notes

| Step | T-ID | Component | Direction | Mechanism | Notes |
|------|------|-----------|-----------|-----------|-------|
| 1 | T-01 | | `↑ upward propagation` | | |
| 2 | T-02 | | `↑ upward propagation` \| `↓ downward prop-passing` \| `context injection` \| `event delegation` | | |

Rules: Minimum two rows. Direction required per row — not once as a summary. Assign T-IDs to all rows. Every T-ID must appear in TABLE 4.

---

**TABLE 3 · State Mutation Map**

**Pre-declaration (required):**

```
Mutations: N=___ direct, M=___ inherited  (total: ___)
```

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, or computed properties triggered.
Reason: [name the reason]
```

If total > 0, complete the table. Row count must match N+M.

Required columns: State Key · Owner · Layer · Type · Old Value Shape · New Value Shape · Mechanism

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| | | *(local / context / store)* | *(direct / inherited)* | | | |

Invalid values: "state updates", "previous value", "new value", "N/A", blank.

---

**TABLE 4 · Re-render Inventory**

Required columns: T-ID · Component · Re-renders? · Reason · Necessary? · UR-ID

| T-ID | Component | Re-renders? | Reason | Necessary? | UR-ID |
|------|-----------|-------------|--------|------------|-------|
| T-01 | | Yes / No | | Yes — [reason] / No — [reason] | |

Every T-ID from TABLE 2 must appear. No T-ID may be omitted. Unnecessary re-renders receive UR-IDs.

**PROMOTION BLOCK:**
```
Unnecessary re-renders: [count]
UR-IDs requiring findings entry: [list or "none"]
```

---

**TABLE 5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| | | | *(synchronous / microtask / macrotask)* | |

If none: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`. Silence not acceptable.

---

**TABLE 6 · Final UI State — Four Phases**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

All four rows required. Invalid: "UI updates accordingly", "reflects state changes", blank.

---

**TABLE 7 · Findings**

Required rows — N/A prohibited:

| ID | Category | Component / State Path | Finding | Fix — API or Pattern |
|----|----------|----------------------|---------|---------------------|
| F-01 | Render performance | | *(finding or "none detected — [reason]")* | |
| F-02 | Unnecessary re-renders — UR cross-reference | *(each UR-ID)* | *(per-UR-ID finding or "none")* | *(React.memo / createSelector / useMemo — named)* |
| F-03 | Accessibility | | *(finding or "none detected — [reason]")* | |
| F-04 | Async error handling | | *(finding or "none detected — [reason]")* | |
| F-05 | Memory leaks | | *(finding or "none detected — [reason]")* | |

---

**ROLE 2 — Schema Compliance Auditor (C-30/C-31/C-32 only)**

You are a compliance auditor. Your sole task is to verify the developer's trace satisfies C-30, C-31, and C-32. Do not re-run the trace. Do not add findings. Fill the three tables below.

---

**AUDIT TABLE A · C-30 Dual Mutation Count Compliance**

| Check | Result | Evidence |
|-------|--------|----------|
| Mutation pre-declaration contains "N=___ direct" count? | Pass / Fail | *(quote the declaration line from TABLE 3)* |
| Mutation pre-declaration contains "M=___ inherited" count? | Pass / Fail | *(quote the declaration line)* |
| TABLE 3 row count equals declared N+M total? | Pass / Fail / N/A (total=0) | *(declared total = ___, row count = ___)* |
| Zero-mutation declaration present when total = 0? | Pass / Fail / N/A (total>0) | |
| Type column present with "direct" / "inherited" values? | Pass / Fail / N/A (total=0) | |

---

**AUDIT TABLE B · C-31 Schema-Field Coverage of C-20–C-29**

Required: at least 7 of 10 mapped to schema fields (table column, required row, or required cell). Fewer than 5 fails.

| Criterion | Schema Field in Developer Output | Pass / Fail |
|-----------|----------------------------------|-------------|
| C-20 Framework Declaration Gate | *(name the table/field)* | |
| C-21 Failure Mode Displacement | *(name invalid-value rule in which table)* | |
| C-22 Re-render Necessity Annotation | *(name the column)* | |
| C-23 Four-Phase UI Progression | *(name the required-rows structure)* | |
| C-24 Zero-Mutation Declaration | *(name the required declaration block)* | |
| C-25 Issue Category Completeness | *(name the required-rows structure in TABLE 7)* | |
| C-26 Unnecessary Re-render Promotion | *(name PROMOTION BLOCK + F-02 cross-reference)* | |
| C-27 Mutation Count Pre-Declaration | *(name the pre-declaration field)* | |
| C-28 Per-Hop Direction Annotation | *(name the Direction column rule)* | |
| C-29 Re-render Inventory Completeness | *(name the T-ID completeness rule)* | |

**C-31 verdict**: ___ / 10 criteria mapped to schema fields. Pass (>=7) / Fail (<5) / Borderline (5-6).

---

**AUDIT TABLE C · C-32 Blank-Blocked Field Primacy for C-01–C-05**

Required: at least 3 of 5 essentials backed by blank-blocked schema fields. Fewer than 3 fails.

| Essential Criterion | Blank-Blocked Schema Field Present? | Field Name / Table |
|--------------------|------------------------------------|--------------------|
| C-01 Event Anchor | Yes / No | *(TABLE 1 columns: Event Type, Component Name, Handler Function)* |
| C-02 Component Tree Traversal | Yes / No | *(TABLE 2 minimum two rows + T-ID column)* |
| C-03 State Update Map | Yes / No | *(TABLE 3 pre-declaration + row count constraint)* |
| C-04 Re-render Inventory | Yes / No | *(TABLE 4 T-ID completeness rule)* |
| C-05 Final UI State | Yes / No | *(TABLE 6 four required phases)* |

**C-32 verdict**: ___ / 5 essentials backed by blank-blocked fields. Pass (>=3) / Fail (<3).

---

## V-05 · Lifecycle Emphasis + Phrasing Register — Formal/Technical Phase-Gated with Schema Anchors

**Axis**: Lifecycle emphasis + phrasing register (formal/technical prose sections paired with schema anchor tables)
**Hypothesis**: R8 V-03 (phrasing register only) FAILED on essential C-03 (score 54/60) because instruction-only text provides no structural prevention for the zero-mutation case. The register itself was strong — framework vocabulary, formal precision, imperative completeness instructions. R9 V-05 rescues the formal/technical register by pairing each section with a minimal "anchor table" — a schema-enforced field that satisfies C-32's blank-blocked requirement — while preserving the prose register as the primary channel. Each section has: (1) formal technical prose for reasoning and vocabulary, (2) a required anchor table that makes the key output fields blank-blocked. Phase gates enforce structure without abandoning the prose register. The dual mutation count is introduced as a formal "mutation complexity declaration." Expected score: 122–128/138 — the register overhead may still depress C-21 (failure mode displacement requires specific output text, not prose) and C-31 (some aspirational criteria may still be prose-only rather than schema-field-backed).

---

You are a senior frontend engineer conducting a rigorous component trace analysis. Apply framework-specific vocabulary throughout — use exact API names, hook names, and lifecycle terms from the declared framework. After the framework declaration, generic terms such as "state management layer" and "component lifecycle" are not acceptable; substitute the declared library and hook names.

**Phase 0 — Framework Declaration**

*Anchor table (blank-blocked — Phase 0 exit requires all three rows filled):*

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — exact name]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — exact name]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

Phase 0 exit: All three fields named with exact library/framework names. Analysis cannot proceed until this table is complete.

---

**Phase 1 — Event Analysis**

Identify the initiating event with precision. Name the DOM event type, the component that owns the event binding (not "the button" — name the component), the exact event handler function (not "the handler" — name the function), and the payload or synthetic event properties that drive subsequent behavior.

*Anchor table (blank-blocked — Event Type, Component Name, and Handler Function cannot be left blank):*

| Event Type | Component Name | Handler Function | Payload | File Location |
|------------|----------------|-----------------|---------|---------------|
| | *(exact — not "the button")* | *(exact — not "the handler")* | | |

Phase 1 exit: Event Type, Component Name, and Handler Function are all named in the anchor table.

---

**Phase 2 — Component Hierarchy Traversal**

Trace the event's path through the component hierarchy. At each step, name the component and describe the mechanism by which control flows — upward via callback props, downward via prop drilling, through a context provider, via event delegation, or through a Higher-Order Component wrapper.

The direction must be annotated at each step individually. A single direction summary for the whole traversal is not acceptable. Document each hop in sequence, preserving the structural parent→child or leaf→provider relationship.

*Anchor table (blank-blocked — Direction column and T-ID required per row):*

| Step | T-ID | Component | Direction | Mechanism | Notes |
|------|------|-----------|-----------|-----------|-------|
| 1 | T-01 | *(leaf component)* | `↑ upward propagation` \| `↓ downward prop-passing` \| `context injection` \| `event delegation` | | |
| 2 | T-02 | | *(same direction options)* | | |

Rules: Minimum two rows. Direction required per row. Every T-ID must appear in Phase 4 with a verdict.

Phase 2 exit: At least two hops with individual direction annotations. All components assigned T-IDs.

---

**Phase 3 — State Mutation Analysis**

Declare upfront the mutation complexity of this action:

*Mutation Complexity Declaration (required, appears before mutation table):*

```
Mutations: N=___ direct, M=___ inherited  (total: ___)
```

- **Direct mutations** — state writes the event handler produces immediately or in synchronous code it calls.
- **Inherited mutations** — state writes triggered transitively through `useEffect` reactions, computed cascades, store middleware, `watch` callbacks, or subscriptions responding to direct mutations.

If the action produces zero total mutations, document this explicitly:

```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only operation / display-only / consumed without dispatch]
```

Do not leave zero mutations undocumented. Phrases such as "state updates", "the store is modified" without naming the key, and "updates accordingly" are not acceptable in any mutation description.

If total > 0, complete the mutation anchor table. Row count must match declared N+M.

*Anchor table (blank-blocked — State Key, Owner, and Type cannot be left blank):*

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store slice)* | *(local / context / store)* | *(direct / inherited)* | *(shape)* | *(shape)* | *(mechanism)* |

Phase 3 exit: Mutation Complexity Declaration present with N (direct) + M (inherited) filled. Either zero-mutation declaration complete, or mutation table with N+M rows and Type column filled.

---

**Phase 4 — Re-render Analysis**

For each component in the traversal, determine whether it re-renders as a result of the state changes. Provide a verdict for every component named in Phase 2 — including components that do not re-render. An analysis that accounts for fewer components than the traversal leaves unexplained gaps.

For each re-render, state whether it is necessary or unnecessary and give the reason. Assign a short identifier (UR-01, UR-02, …) to each unnecessary re-render for cross-reference in Phase 7.

*Anchor table (blank-blocked — every T-ID from Phase 2 must appear, Necessary? column required):*

| T-ID | Component | Re-renders? | Reason | Necessary? | UR-ID |
|------|-----------|-------------|--------|------------|-------|
| T-01 | | Yes / No | | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

Every T-ID from Phase 2 must appear. Traversal components with no re-render still require a row with Re-renders? = No and reason.

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: [count]
UR-IDs requiring findings entry: [list or "none"]
```

Phase 4 exit: Every T-ID has a verdict. PROMOTION BLOCK present.

---

**Phase 5 — Side Effect Analysis**

Document every side effect triggered by this action: API calls (named endpoint and HTTP method), timer scheduling (`setTimeout`, `setInterval`), subscription creation, navigation events, or DOM mutations outside the component tree. For each, name the mechanism and note whether cleanup is performed.

*Anchor table (blank-blocked — Type column required; "none" row required if no side effects):*

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

If no side effects: `| none | — | No side effects — synchronous only. | — | — |`. Silence not acceptable.

Phase 5 exit: At least one side effect documented, or "none" row present.

---

**Phase 6 — Final UI State**

Describe the observable UI across four temporal stages. For each stage, describe the visible elements, any disabled or enabled controls, and what the user perceives. Do not use closings such as "UI updates accordingly", "the UI reflects the state changes", or "success and error states are handled."

*Anchor table (blank-blocked — all four Phase rows required, Visible Elements cannot be blank):*

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

Phase 6 exit: All four rows present with concrete visible element descriptions. Phases 3 and 4 not collapsed.

---

**Phase 7 — Findings**

Conduct a structured review across five issue categories. For each category, name any issues found with their component or state path. If no issues are found in a category, state "none detected" and give a brief reason rather than leaving the category unaddressed.

For unnecessary re-renders, recommend a specific fix using a named API or pattern (`React.memo`, `useMemo`, `useCallback`, `createSelector`, `Pinia computed`, `NgRx createSelector`, etc.).

*Anchor table (blank-blocked — five required rows, N/A prohibited):*

| ID | Category | Component / State Path | Finding | Fix — Named API or Pattern |
|----|----------|----------------------|---------|---------------------------|
| F-01 | Render performance / unnecessary re-renders | | *(finding or "none detected — [reason]")* | |
| F-02 | Unnecessary re-renders — UR cross-reference | *(each UR-ID from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(named API)* |
| F-03 | Accessibility | | *(finding or "none detected — [reason]")* | |
| F-04 | Async error handling | | *(finding or "none detected — [reason]")* | |
| F-05 | Memory leaks | | *(finding or "none detected — [reason]")* | |

Every UR-ID from Phase 4's PROMOTION BLOCK must appear in F-02 with a named fix.

Phase 7 exit: All five categories addressed. Every UR-ID cross-referenced with a named fix.

---

**Closing**: Use framework-specific vocabulary throughout — no generic terms after the Phase 0 declaration.

---

## Variation Summary

| V# | Axis | Primary C-30 Mechanism | Primary C-31 Mechanism | Primary C-32 Mechanism | Expected Score |
|----|------|------------------------|------------------------|------------------------|----------------|
| V-01 | Output format (schema evolution) | N=direct, M=inherited pre-declaration + Type column in TABLE 3 | 10/10 criteria already mapped to schema fields via R8 pipeline | All 5 essentials backed by TABLE 1–TABLE 6 columns | 134–136/138 |
| V-02 | Lifecycle emphasis (phase manifests) | Phase 3 manifest + exit condition reference dual count | Per-phase manifests list criteria → field mappings explicitly | Phase 1/2/4/6 exit conditions reference blank-blocked fields | 130–133/138 |
| V-03 | Inertia framing — targeted extraction | N=direct, M=inherited + Type column (TABLE 3b dropped) | TABLE 2 Role column + TABLE 3 Type column extend schema field coverage | TABLE 1–TABLE 6 blank-blocked columns as in V-01 | 132–135/138 |
| V-04 | Output format + Role sequence | AUDIT TABLE A verifies N+M declaration and row count | AUDIT TABLE B maps 10 criteria to schema fields explicitly | AUDIT TABLE C verifies 5/5 essentials are blank-blocked | 130–134/138 |
| V-05 | Lifecycle emphasis + Phrasing register | Mutation Complexity Declaration block (formal register) | Anchor tables per phase provide schema fields; some prose-only gaps possible | Anchor tables per phase give blank-blocked fields for all 5 essentials | 122–128/138 |

**Predicted ranking**: V-01 > V-03 ≥ V-02 > V-04 > V-05

**Key test**: V-03 (inertia targeted extraction) tests whether the `↔ inert pass-through` direction adds aspirational value without V-05's coherence penalty — the sub-table was the cost, not the framing. If V-03 scores within 1–2 of V-01, targeted extraction from V-05 is the right path. If V-03 scores below V-02, the inertia framing itself is the coherence cost.

**Structural hypothesis**: V-01's self-reinforcing pipeline (schema fields → excellence signals → new criteria → schema fields that already existed) should hold for C-30/C-31/C-32 just as it held for C-27/C-28/C-29. The Type column and dual pre-declaration were already the natural extensions of V-01's TABLE 3 structure. C-31 and C-32 should be satisfied at zero revision cost, exactly as C-27/C-28/C-29 were in R8.
