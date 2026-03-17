# trace-component — Round 11 Variations

**Variation axes used:**
- Single-axis: Inertia framing (V-01), Lifecycle emphasis (V-02), Output format (V-03)
- Combined: Inertia framing + Lifecycle emphasis (V-04), Role sequence + Inertia framing (V-05)

**R11 context:** Two new criteria from R10 excellence signals: C-36 (Inert-as-Default Direction Schema — Direction column lists `<-> inert` as first and default permitted value; active codes are named departures requiring explicit selection; active-codes-first or inert-as-trailing-exception fails) and C-37 (Manifest-Analysis Paired Block Structure — each phase appears as consecutive MANIFEST-N / TABLE-N blocks with matching N and no intervening content; at least 3 pairs required; header-manifest pattern fails). New ceiling: 148 pts.

R10 excellence signals carried forward:
1. **Default-inert ordering changes the cognitive contract** — an unlabeled hop in a default-inert schema means "probably missed," not "probably active." C-36 extends this from annotation to schema structure.
2. **Compact manifests score higher than verbose ones** — completeness (three fields) beats verbosity; coherence cost of 7-phase manifests outweighs coverage gain.
3. **Mandatory inert-hop declaration even at zero count** — the Declaration footer is a schema field, not a conditional note; zero inert hops becomes an explicit claim.
4. **Adjacent pairing makes manifest-to-analysis gating verifiable by inspection** — MANIFEST-N/TABLE-N adjacency closes the gap C-37 targets: a document-header manifest satisfies C-33 but silently decouples from specific phases.

R10 top score: V-03 143/144. New ceiling: 148 (C-36 + C-37, 2 pts each).

---

## V-01 · Inertia Framing — Direction Column Header as Default-Inert Schema (C-36 Native via C-14)

**Axis**: Inertia framing
**Hypothesis**: R10 V-03 listed `<-> inert` first among Direction values; C-36 requires it to be the *syntactic default*, not just first in a list. V-01 encodes this structurally by embedding inertia in the column header itself: `Direction [<-> inert (default) | departure: prop-pass · event-propagate · dispatch · effect-trigger · context-provide]`. Every active hop must replace the default value; a cell that is never filled is structurally inert. This satisfies C-36 at schema-structure level and simultaneously satisfies C-14 (column header embeds fill constraint) and C-17 (triple structural lock). C-37 absorbed via MANIFEST-N/TABLE-N adjacency carried from R10 V-04. Expected score: 146–148/148.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding. All output uses that framework's exact terminology — no generic substitutions. **Every traversal hop is documented — inert hops are expected output proving trace completeness, not redundant observations.**

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

Do not begin phase analysis until this header is complete.

---

**MANIFEST-1 · Event Phase** *(required gate — fill completely before writing TABLE-1; TABLE-1 begins immediately below this block with no intervening content)*

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-1 · Event Anchor**

Required columns: Event Type · Component Name · Handler Function · Event Payload · File Location

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / object shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase** *(required gate — fill completely before writing TABLE-2; TABLE-2 begins immediately below this block with no intervening content)*

```
Components in scope: [all components in the traversal path — include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-2 · Component Tree Traversal — Default-Inert Schema**

The Direction column's default value is `<-> inert`. Every hop begins as inert. An active hop replaces `<-> inert` with exactly one departure code. A cell containing only a departure code means the hop is active. An unlabeled cell is structurally inert by position — the schema, not an annotation, carries this meaning.

Required columns: Step · T-ID · Component · Direction [<-> inert (default) | prop-pass | event-propagate | dispatch | effect-trigger | context-provide] · Role · Notes

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | `<-> inert` *(replace only if hop is active)* | **Acted**: [description] / **Inert**: [reason — prop forwarded / event not consumed / not subscribed] | |
| 2 | T-02 | | | | |
| … | | | | | |

Rules:
- Direction default: `<-> inert`. Departure codes replace it — they do not accompany it. A departure code without `<-> inert` means active; `<-> inert` without a departure code means inert.
- Role column: "Acted: [description]" or "Inert: [reason]". Blank fails — an unlabeled Role cell does not distinguish acted from inert.
- Minimum two rows. T-IDs (T-01, T-02, …) must all appear in TABLE-4.

**INERT-HOP DECLARATION (mandatory footer — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, inert noted only in Notes column, or a Role cell that is blank. Stating "inert" anywhere except the Direction cell does not satisfy the direction schema.]

---

**MANIFEST-3 · Mutation Phase** *(required gate — fill completely before writing TABLE-3; TABLE-3 begins immediately below this block with no intervening content)*

```
Components in scope: [components that own or dispatch mutations]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION (required before table body):**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- **Direct** — state writes the event handler or synchronous code produces immediately.
- **Inherited** — state writes triggered transitively through `useEffect`, `watch`, computed cascades, store middleware, or subscriptions reacting to direct mutations.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```
Silence on zero-mutation case does not pass.

If total > 0, complete the table. Row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store slice)* | *(local / context / store)* | *(direct / inherited)* | *(shape)* | *(shape)* | *(setState / dispatch / useEffect / watch / etc.)* |

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "updated value", "N/A", or a row count that does not match the pre-declaration total.]

---

**MANIFEST-4 · Re-render Phase** *(required gate — fill completely before writing TABLE-4; TABLE-4 begins immediately below this block with no intervening content)*

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops, which may still re-render from prop or context changes.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | *(owns state / receives new props / subscribes to changed context / no state owned / no props changed / not subscribed)* | Yes — [reason] / No — [memoization missing / selector too broad / etc.] | *(UR-ID or "—")* |

Notes:
- `Re-renders? [Yes (N) / No]` — N is the render count; verdict and count in same cell, co-located.
- Every T-ID required. No silent drops.
- Unnecessary re-renders receive UR-IDs.

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", a blank Necessary cell, or a missing PROMOTION BLOCK.]

---

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / DOM mutation / none)* | | | *(synchronous / microtask / macrotask)* | |

If no side effects: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`. Silence does not pass.

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

All four rows required. Rows 3 and 4 not collapsed.

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings**

N/A prohibited in any cell.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a — no issue")* | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(each UR-ID from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found", or a findings section that addresses only discovered issues without clearing unchecked categories.]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

Read verdicts from the tables produced above — do not re-derive.

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (blank-blocked) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID column + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Mutation Count pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four required Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · "none" row present if no effects | |
| C-07 Issue Detection | TABLE-7 · five required rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | Framework Declaration + declared terms used in TABLE-2 through TABLE-7 | |

Pass condition: at least five PASS verdicts. Any C-01–C-05 FAIL is an essential failure.

---

**CLOSING MANDATE**: Direction cells default to `<-> inert`. Active hops declare departure codes. Undocumented inert hops are incomplete traces.

---

## V-02 · Lifecycle Emphasis — MANIFEST-N/TABLE-N Strict Adjacency via Embedded Structural Marker (C-37 Native)

**Axis**: Lifecycle emphasis
**Hypothesis**: C-37 requires MANIFEST-N/TABLE-N pairs to be positionally adjacent with no intervening content. V-01 achieves this through positioning alone; V-02 makes the adjacency constraint explicit as a point-of-production rule embedded in each MANIFEST block's close. The closing line of every MANIFEST block is: `↓ TABLE-N begins immediately below. No content may appear between this line and the TABLE-N header.` A model that introduces content between a MANIFEST and its TABLE violates a rule it just wrote — the constraint is present at point of violation, not only in preamble instructions. C-36 absorbed by listing `<-> inert` as the first and default permitted value in a numbered Direction schema. Five MANIFEST-TABLE pairs exceed C-37's minimum of three. Expected score: 146–148/148.

---

You are a frontend domain expert. Identify the framework and state management library before proceeding. All output uses that framework's exact terminology.

**STRUCTURAL SCHEMA RULE (read before writing any output):** This trace uses paired MANIFEST-N / TABLE-N blocks. Each MANIFEST block closes with the marker `↓ TABLE-N begins immediately below.` No content may appear between that marker and the TABLE-N header row. Pairing is verifiable by inspection: MANIFEST-1 is followed by TABLE-1, MANIFEST-2 by TABLE-2, and so on. At least five pairs must appear. A manifest at the document header separated from analysis tables by other content violates this rule.

---

**FRAMEWORK DECLARATION**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-1 begins immediately below. No content may appear between this line and the TABLE-1 header.

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

Invalid: "the button", "a click", "the handler", "N/A", blank.

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all components in the traversal path — include pass-through hops]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-2 begins immediately below. No content may appear between this line and the TABLE-2 header.

**TABLE-2 · Component Tree Traversal**

Direction column permitted values — in priority order; `<-> inert` is the default; all other codes are explicit departures:

1. `<-> inert` — hop receives event or prop but produces no mutation and fires no side effect *(default — used unless a departure code applies)*
2. `prop-pass` — hop passes props downward to a child
3. `event-propagate` — hop propagates event upward to a parent
4. `dispatch` — hop dispatches a store action
5. `effect-trigger` — hop triggers a side effect
6. `context-provide` — hop provides or updates context value

| Step | T-ID | Component | Direction | Role | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | `<-> inert` *(or a departure code)* | Acted: [desc] / Inert: [reason] | |
| 2 | T-02 | | | | |
| … | | | | | |

Rules: Direction required per row. Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION:**
```
Inert hops: ___ (T-IDs: ___)
[If 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [components that own or dispatch mutations]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-3 begins immediately below. No content may appear between this line and the TABLE-3 header.

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION (required):**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: ___
```

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store)* | *(local / context / store)* | *(direct / inherited)* | *(shape)* | *(shape)* | *(mechanism)* |

[GATE-3: Does not close on "state updates", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-4 begins immediately below. No content may appear between this line and the TABLE-4 header.

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | *(owns state / receives new props / subscribes to changed context / no state owned / not subscribed)* | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK:**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [any final-state mutations from async resolution]
Side effects may fire: [any cleanup or completion effects]
```
↓ TABLE-5 begins immediately below. No content may appear between this line and the TABLE-5 header.

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / DOM mutation / none)* | | | *(synchronous / microtask / macrotask)* | |

If no effects: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

All four rows required. Rows 3 and 4 not collapsed.

---

**TABLE-7 · Findings** *(no manifest — follows TABLE-6 directly)*

N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: Does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 | TABLE-2 · T-ID + Direction per row + min-2-rows | |
| C-03 | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 | TABLE-5 · "none" row if no effects | |
| C-07 | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 | Framework Declaration + declared terms throughout | |

---

**CLOSING MANDATE**: Each MANIFEST-N is immediately followed by TABLE-N with no intervening content. Direction defaults to `<-> inert`. Active hops declare departure codes.

---

## V-03 · Output Format — Schema Charter: Both C-36/C-37 as Organizational DNA

**Axis**: Output format
**Hypothesis**: V-01 and V-02 add C-36/C-37 as constraints layered onto an existing schema. V-03 tests whether promoting them to the schema's organizing DNA — declared in a SCHEMA CHARTER before any tables — produces stronger compliance. When a principle is declared as the *reason the schema is structured this way*, a model violating it must contradict its own prior output, not merely miss a rule. The SCHEMA CHARTER (a required produced artifact) names both principles: (1) MANIFEST-N/TABLE-N adjacency is the schema's phase-gating mechanism — tables cannot begin before their manifest closes, (2) Direction defaults to `<-> inert` — this is the schema's departure-declaration model, not an annotation option. Compact 3-line manifests (R10 ES-2 lesson: verbosity adds coherence cost). Expected score: 146–148/148.

---

You are a frontend domain expert. Identify the framework and state management library before proceeding. All output uses that framework's exact terminology.

**STEP 1 — SCHEMA CHARTER (required produced artifact, precedes all analysis)**

Before writing any trace table, produce this schema charter. It is part of the output, not an internal planning step.

```
SCHEMA CHARTER
--------------
Framework: ___
State management: ___
Component model: ___

Organizational principle 1 — Phase Gating:
This trace uses MANIFEST-N / TABLE-N adjacent pairs. Each manifest immediately precedes
its analysis table. No content appears between MANIFEST-N and TABLE-N. Pairing is
verifiable by inspection (MANIFEST-1 → TABLE-1, MANIFEST-2 → TABLE-2, ...).
At least 4 pairs required by this trace.

Organizational principle 2 — Departure Declaration:
The traversal schema's Direction column defaults to <-> inert. Every hop is inert unless
an active departure code is declared. Active codes (prop-pass / event-propagate / dispatch /
effect-trigger / context-provide) are replacements for the default, not additions to it.
An unlabeled Direction cell is structurally inert.

Implication: a missing inert annotation is a schema violation (the cell defaults to inert,
making absence detectable); a missing departure annotation on an active hop is also a schema
violation (the default inert label contradicts observed behavior).
```

Do not begin TABLE-1 until the SCHEMA CHARTER is complete.

---

**MANIFEST-1 · Event Phase**
```
In scope: ___  |  State keys: ___  |  Side effects: ___
```

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(type)* | *(exact name)* | *(exact name)* | *(shape / "none")* | *(path:line)* |

[GATE-1: Does not close on "the button", "a click", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**
```
In scope: [all traversal hops]  |  State keys: ___  |  Side effects: ___
```

**TABLE-2 · Component Tree Traversal**

Per SCHEMA CHARTER principle 2: Direction defaults to `<-> inert`. Active hops replace the default with a departure code.

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role [Acted: desc / Inert: reason] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | | `<-> inert` *(or departure code)* | | |
| 2 | T-02 | | | | |
| … | | | | | |

Minimum two rows. Every T-ID appears in TABLE-4.

**INERT-HOP DECLARATION:**
```
Inert hops: ___ (T-IDs: ___)
[If 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: Does not close on a blank Direction cell, Role cell that is blank, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**
```
In scope: [mutation owners]  |  State keys: [expected mutation targets]  |  Side effects: ___
```

**TABLE-3 · State Mutation Map**

**Pre-declaration:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

Zero-mutation case:
```
ZERO MUTATION DECLARATION
Direct: none  |  Inherited: none
Reason: [read-only / display-only / event consumed without dispatch / other]
```

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| | | *(local / context / store)* | *(direct / inherited)* | | | |

Row count = N + M.

[GATE-3: Does not close on "state updates", "previous value", "N/A", row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**
```
In scope: [all T-IDs from TABLE-2]  |  State keys: ___  |  Side effects: ___
```

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear. Inert pass-through hops still require a verdict.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | | Yes (1) / No | | Yes — [reason] / No — [reason] | |

**PROMOTION BLOCK:**
```
Unnecessary re-renders: ___  |  UR-IDs: ___
```

---

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(type / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: Does not close on "UI updates accordingly", "reflects state changes", collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs)* | | *(React.memo / createSelector / computed / useMemo)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: Does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 | TABLE-5 · zero-effects row if no effects | |
| C-07 | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 | SCHEMA CHARTER framework declaration + declared terms in TABLE-2 through TABLE-7 | |

---

**CLOSING MANDATE**: The SCHEMA CHARTER is a produced artifact. Per Charter principle 1, MANIFEST-N is followed immediately by TABLE-N. Per Charter principle 2, Direction defaults to `<-> inert`.

---

## V-04 · Combined: C-36 + C-37 Maximum Enforcement — Direction Header + Adjacency Marker

**Axis**: Inertia framing + Lifecycle emphasis (combined)
**Hypothesis**: V-01 enforces C-36 via column header embedding; V-02 enforces C-37 via the `↓ TABLE-N begins immediately below` marker. Both mechanisms are independent — one targets the cell level, the other targets the block-boundary level. V-04 combines them: every MANIFEST block closes with the adjacency marker AND the Direction column header embeds the inert-as-default constraint. The two mechanisms are non-redundant: the header embedding prevents inert escapes within the table; the adjacency marker prevents structural decoupling between the manifest and its table. C-36 and C-37 are structurally unavoidable in combination. Expected score: 147–148/148.

---

You are a frontend domain expert. Identify the framework and state management library before proceeding. All output uses that framework's exact terminology. **Inert components are not omitted — their documentation proves trace completeness.**

**FRAMEWORK DECLARATION (required)**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

---

**MANIFEST-1 · Event Phase** *(fill all three fields before proceeding)*

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-1 begins immediately below. No content may appear between this line and the TABLE-1 header.

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: Does not close on "the button", "the handler", "N/A", or blank.]

---

**MANIFEST-2 · Traversal Phase** *(fill all three fields before proceeding)*

```
Components in scope: [all traversal hops — include pass-through components]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-2 begins immediately below. No content may appear between this line and the TABLE-2 header.

**TABLE-2 · Component Tree Traversal — Default-Inert Direction Schema**

The Direction column's default value is `<-> inert`. Active hops replace it with a departure code. `<-> inert` is listed first because it is the syntactic default — not because inertia is a special case of activity.

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role [Acted: desc / Inert: reason] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | `<-> inert` *(or departure code if active)* | | |
| 2 | T-02 | | | | |
| … | | | | | |

Rules:
- Direction header lists `<-> inert` first — this is the default, not an option. Departure codes are replacements.
- Role: "Acted: [description]" or "Inert: [reason]". Blank fails.
- Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: Does not close on a blank Direction cell, Role cell that is blank, or inert noted only in Notes.]

---

**MANIFEST-3 · Mutation Phase** *(fill all three fields before proceeding)*

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-3 begins immediately below. No content may appear between this line and the TABLE-3 header.

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

Zero-mutation case:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store)* | *(local / context / store)* | *(direct / inherited)* | *(shape)* | *(shape)* | *(mechanism)* |

Row count must equal N + M.

[GATE-3: Does not close on "state updates", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase** *(fill all three fields before proceeding)*

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-4 begins immediately below. No content may appear between this line and the TABLE-4 header.

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | *(owns state / receives new props / subscribes / no state owned / not subscribed)* | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: Does not close on omitting any T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(type / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row required: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

All four rows required. Rows 3 and 4 not collapsed.

[GATE-6: Does not close on "UI updates accordingly", "reflects state changes", or collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a — no issue")* | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(each UR-ID)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: Does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 | TABLE-5 · zero-effects row if no effects | |
| C-07 | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 | Framework Declaration + declared terms in TABLE-2 through TABLE-7 | |

---

**CLOSING MANDATE**: Each MANIFEST-N closes with `↓ TABLE-N begins immediately below` and is followed by TABLE-N with no intervening content. Direction defaults to `<-> inert`; active hops declare departure codes.

---

## V-05 · Combined: Role Sequence + Inertia Framing — Schema Architect Declares Traversal Schema

**Axis**: Role sequence + Inertia framing (combined)
**Hypothesis**: V-01 through V-04 all instruct the analyst to follow a pre-defined schema. V-05 tests whether having the model act as *schema architect* first — producing a TRAVERSAL-SCHEMA artifact that explicitly designs the Direction column with inert-as-default — produces stronger C-36 compliance. When the model declares `<-> inert` as a design decision in role 1, it becomes an author of that decision rather than a follower of a rule. A model that then violates the inert-as-default in role 2 contradicts its own artifact, creating a stronger structural signal than a missed instruction. The TRAVERSAL-SCHEMA artifact also declares the paired-block structure (C-37), anchoring both new criteria as design outputs. Role 2 then acts as analyst using the declared schema. Expected score: 145–148/148.

---

**ROLE 1 — SCHEMA ARCHITECT (produces TRAVERSAL-SCHEMA artifact)**

You are a schema architect. Your task is to design the output schema this trace will use. Produce the TRAVERSAL-SCHEMA artifact below — it is an output, not a planning note. After producing it, you will switch to the analyst role and execute the trace using the schema you designed.

**TRAVERSAL-SCHEMA (required output artifact)**

```
TRAVERSAL-SCHEMA
----------------
Framework: ___
State management: ___
Component model: ___

Phase-gating design:
  Method: MANIFEST-N / TABLE-N adjacent pairs
  Rule: Each MANIFEST block immediately precedes its TABLE (same N).
        No content may appear between MANIFEST-N and TABLE-N.
        Pairing is verifiable by block label inspection.
  Pairs in this trace: MANIFEST-1/TABLE-1, MANIFEST-2/TABLE-2,
                       MANIFEST-3/TABLE-3, MANIFEST-4/TABLE-4 (minimum)

Direction column design (TABLE-2):
  Default value: <-> inert
  Rationale: Every traversal hop is inert until a departure is declared.
             This inverts the annotation burden — active hops must justify
             departure; inert hops require no justification beyond the default.
  Departure codes (replacements for default, not additions):
    - prop-pass         (hop passes props downward)
    - event-propagate   (hop propagates event upward)
    - dispatch          (hop dispatches a store action)
    - effect-trigger    (hop triggers a side effect)
    - context-provide   (hop provides or updates context)
  Enforcement: Column header embeds default — blank cells are structurally inert.

Table inventory:
  TABLE-1 · Event Anchor
  TABLE-2 · Component Tree Traversal (default-inert Direction schema)
  TABLE-3 · State Mutation Map (pre-declaration + dual-track count)
  TABLE-4 · Re-render Inventory (T-ID completeness + UR-IDs)
  TABLE-5 · Side Effects
  TABLE-6 · Final UI State (four-phase progression)
  TABLE-7 · Findings (five required rows, N/A prohibited)
  TABLE-8 · Criteria Audit (C-01 through C-08)
```

Do not begin TABLE-1 until the TRAVERSAL-SCHEMA artifact is complete.

---

**ROLE 2 — ANALYST (executes trace using the TRAVERSAL-SCHEMA declared above)**

You are now a frontend domain expert. Execute the trace using the schema you declared as architect. Every schema decision above is in effect. Violations contradict your own artifact.

---

**MANIFEST-1 · Event Phase**
```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-1 · Event Anchor**

*(per TRAVERSAL-SCHEMA — TABLE-1 follows MANIFEST-1 immediately)*

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: Does not close on "the button", "the handler", "N/A", or blank.]

---

**MANIFEST-2 · Traversal Phase**
```
Components in scope: [all traversal hops — include pass-through hops]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-2 · Component Tree Traversal**

*(per TRAVERSAL-SCHEMA — Direction defaults to `<-> inert`; departure codes replace the default)*

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role [Acted: desc / Inert: reason] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | | `<-> inert` *(or departure code)* | | |
| 2 | T-02 | | | | |
| … | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION:**
```
Inert hops: ___ (T-IDs: ___)
[If 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: Does not close on blank Direction cell, blank Role cell, or inert noted only in Notes column.]

---

**MANIFEST-3 · Mutation Phase**
```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-3 · State Mutation Map**

**Pre-declaration:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

Zero-mutation:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: ___
```

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| | | *(local / context / store)* | *(direct / inherited)* | | | |

Row count = N + M.

[GATE-3: Does not close on "state updates", "previous value", "N/A", row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**
```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear, including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | | Yes (1) / No | | Yes — [reason] / No — [reason] | |

**PROMOTION BLOCK:**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

---

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(type / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: Does not close on "UI updates accordingly", "reflects state changes", collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs)* | | *(React.memo / createSelector / computed / useMemo)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: Does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

*(per TRAVERSAL-SCHEMA — audit reads verdicts from TABLE-1 through TABLE-7)*

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 | TABLE-5 · zero-effects row if no effects | |
| C-07 | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 | TRAVERSAL-SCHEMA framework declaration + declared terms in TABLE-2 through TABLE-7 | |

---

**CLOSING MANDATE**: The TRAVERSAL-SCHEMA is a produced artifact. Per that artifact: MANIFEST-N is followed immediately by TABLE-N; Direction defaults to `<-> inert`; departures are declared, not implied.

---

## Variation Summary

| Variation | Axis | C-36 Mechanism | C-37 Mechanism | Key Risk |
|-----------|------|---------------|---------------|----------|
| V-01 | Inertia framing | Column header: `Direction [<-> inert (default) \| ...]` — inert is the header's first token; active codes are replacements | MANIFEST-N/TABLE-N adjacency via "immediately below" prose | Possible header truncation in output; column header may be shortened |
| V-02 | Lifecycle emphasis | Direction permitted values in numbered list; `<-> inert` listed first with "(default)" label | `↓ TABLE-N begins immediately below` marker closes each MANIFEST block | Adjacency marker may be omitted when model skips structural formatting |
| V-03 | Output format | SCHEMA CHARTER declares `<-> inert` as default in a produced artifact; violation contradicts prior output | SCHEMA CHARTER declares MANIFEST-N/TABLE-N adjacency as organizational principle 1 | SCHEMA CHARTER may be treated as prose preamble rather than schema definition; less mechanical than header embedding |
| V-04 | Inertia + Lifecycle (combined) | Column header embedding (V-01 mechanism) | `↓ TABLE-N begins immediately below` marker (V-02 mechanism) | Two independent mechanisms; neither reinforces the other — they address different escape paths |
| V-05 | Role sequence + Inertia (combined) | TRAVERSAL-SCHEMA artifact declares `<-> inert` as a design decision in role 1; violation in role 2 contradicts role-1 output | TRAVERSAL-SCHEMA declares paired-block structure by design in role 1 | Role handoff adds coherence cost; model may not maintain schema artifact through role 2; TRAVERSAL-SCHEMA may drift from execution |

**Predicted ranking**: V-04 >= V-01 > V-02 >= V-03 > V-05

- V-04 combines both direct enforcement mechanisms with no coherence overhead — column header + adjacency marker are non-redundant and each closes a distinct escape path.
- V-01 has the strongest single-mechanism C-36 enforcement (header embedding) but C-37 relies on positioning alone without the explicit marker.
- V-02's adjacency marker is strong for C-37 but the numbered-list Direction schema is weaker than header embedding for C-36.
- V-03's SCHEMA CHARTER produces C-36/C-37 as artifacts but is one abstraction layer removed from the enforcement point; document-level declarations carry less structural weight than column-level declarations.
- V-05 introduces role-handoff coherence cost; the TRAVERSAL-SCHEMA artifact adds a novel enforcement mode but the two-role structure risks drift between declared schema and executed schema.
