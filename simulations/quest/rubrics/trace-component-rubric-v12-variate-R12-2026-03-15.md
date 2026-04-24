# trace-component — Round 12 Variations

**Variation axes used:**
- Single-axis: Lifecycle emphasis / C-38 target (V-01), Role sequence / C-39 target (V-02), Inertia framing / C-36 reinforced (V-03)
- Combined: Role sequence + Lifecycle emphasis / C-38 + C-39 (V-04), Role sequence + Inertia framing + Lifecycle emphasis / all three axes (V-05)

**R12 context:** Two new criteria from R11 excellence signals:

- **C-38 (Manifest-Close Adjacency Marker)** — the `down-arrow TABLE-N begins immediately below. No content may appear between this line and the TABLE-N header.` prohibition must be the LAST CONTENT LINE of each MANIFEST-N block. Not in the manifest's opening annotation. Not in a document-level charter preamble. At the manifest's closing position — the exact point where violation would occur. R11 V-02 scored highest on C-37 by using this pattern (five manifest pairs, all with close-line markers). C-38 formalizes it as a distinct criterion because V-01 and V-04 of R11 also achieved C-37 via other mechanisms (header annotations, charter preambles) that carry non-zero risk of decoupling.

- **C-39 (Self-Authored Schema Constraint)** — the model must PRODUCE the schema artifact (SCHEMA CHARTER, TRAVERSAL-SCHEMA, or equivalent named document) itself, declaring both the inert-default rule (C-36) and the adjacency rule (C-37), before the analysis begins. A schema provided as a pre-filled template — even one with blank fields — fails because the rules are authored by the prompt writer, not the model. R11 V-03 (SCHEMA CHARTER) and V-05 (TRAVERSAL-SCHEMA) were prototypes; both pre-authored the schema's principles in the prompt and had the model fill in framework/state-management details. C-39 requires the model to author the principles themselves from a requirements list.

**C-38 / C-39 orthogonality:**
- C-38 can pass without C-39: prompt provides manifest template with close-line already in it; no model-authored schema
- C-39 can pass without C-38: model authors schema declaring adjacency rule, but the per-manifest close-line lives in a charter preamble rather than the manifest's closing position
- Full enforcement requires both: model-authored schema that declares the close-line rule + per-manifest implementation with the close-line as the manifest's last content

R11 top score: V-02 (close-line high-water mark on C-37); V-03 (schema charter on C-36). New ceiling: 152 pts (C-38 + C-39 at 2 pts each).

**R12 hypothesis for each variation:**
- V-01: C-38 pure form — close-line is the manifest's absolute last line; no schema charter; C-39 expected to fail. Tests whether close-line enforcement alone reaches ~150/152.
- V-02: C-39 pure form — model produces TRAVERSAL-SCHEMA from requirements (not template); schema declares both rules; manifests follow schema with close-lines. Tests whether authorship constraint produces stronger compliance than template-following.
- V-03: Inertia-as-null-hypothesis framing — "every hop begins as inert; departure is the claim requiring justification." Phrasing register shift that reinforces C-36 at conceptual level.
- V-04: C-38 + C-39 combined — model authors schema from requirements (C-39); each manifest ends with close-line (C-38); schema declares the close-line rule (linking macro and micro enforcement). Maximum R12 coverage.
- V-05: All three axes — schema authorship (C-39) + close-line enforcement (C-38) + inertia-as-null-hypothesis framing (C-36). The schema the model authors frames inertia as the governing null hypothesis, then enforces it structurally through close-line markers.

---

## V-01 · Lifecycle Emphasis — Manifest-Close Prohibition Line (C-38 Target)

**Axis**: Lifecycle emphasis
**Hypothesis**: R11 V-02 proved that the `down-arrow TABLE-N begins immediately below` line as the manifest's closing line is the structural high-water mark for C-37 enforcement. C-38 formalizes this as requiring the prohibition to be the manifest's LAST CONTENT — not an opening annotation, not a charter preamble. V-01 enforces C-38 by keeping the manifest body as pure data fields (three code-block lines) and making the prohibition line the final item before the table header. No header-level adjacency annotation, no document-level charter. The close-line is the only mechanism. Five manifest-table pairs exceed C-37's minimum of three. C-39 is not targeted — no model-authored schema. Expected score: ~148-150/152 (C-38 pass, C-39 fail).

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding. All output uses that framework's exact terminology. Every traversal hop is documented — inert hops prove trace completeness, not redundancy.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

Do not begin MANIFEST-1 until this header is complete.

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

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all components in the traversal path — include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-2 begins immediately below. No content may appear between this line and the TABLE-2 header.

**TABLE-2 · Component Tree Traversal**

Direction column permitted values, in priority order. `<-> inert` is the default. All other codes are explicit departures that replace it:

1. `<-> inert` — receives event or prop; produces no mutation; fires no side effect *(default — present unless a departure code applies)*
2. `prop-pass` — passes props downward to a child
3. `event-propagate` — propagates event upward to a parent
4. `dispatch` — dispatches a store action
5. `effect-trigger` — triggers a side effect
6. `context-provide` — provides or updates context value

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | `<-> inert` *(or departure code if active)* | Acted: [desc] / Inert: [reason] | |
| 2 | T-02 | | | | |
| ... | | | | | |

Rules: Direction required per hop. Role required per hop ("Acted: [desc]" or "Inert: [reason]"). Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, a blank Role cell, or "inert" noted only in Notes column.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [components that own or dispatch mutations]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-3 begins immediately below. No content may appear between this line and the TABLE-3 header.

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION (required before table body):**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct — state writes the event handler or synchronous code produces immediately.
- Inherited — state writes triggered transitively through useEffect, watch, computed cascades, store middleware, or subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, computed properties, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```
Silence on zero-mutation case does not pass.

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store slice)* | *(local / context / store)* | *(direct / inherited)* | *(shape)* | *(shape)* | *(setState / dispatch / useEffect / watch / etc.)* |

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or a row count that does not match the pre-declaration total.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2 — every traversal component receives a verdict]
State keys may be touched: ___
Side effects may fire: ___
```
↓ TABLE-4 begins immediately below. No content may appear between this line and the TABLE-4 header.

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops, which may still re-render from prop or context changes.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | *(owns state / receives new props / subscribes to changed context / no state owned / no props changed / not subscribed)* | Yes — [reason] / No — [memoization missing / selector too broad / etc.] | *(UR-ID or "—")* |

Notes:
- `Re-renders? [Yes (N) / No]` — N is the render count; verdict and count in same cell, co-located.
- Every T-ID from TABLE-2 required. No silent drops.
- Unnecessary re-renders receive UR-IDs (UR-01, UR-02, ...).

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", a blank Necessary cell, or a missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [any mutations from async resolution]
Side effects may fire: [cleanup or completion effects]
```
↓ TABLE-5 begins immediately below. No content may appear between this line and the TABLE-5 header.

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / DOM mutation / none)* | | | *(synchronous / microtask / macrotask)* | |

If no side effects: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |` Silence does not pass.

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

**TABLE-7 · Findings** N/A prohibited in any cell.

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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID column + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · "none" row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | Framework Declaration + declared terms in TABLE-2 through TABLE-7 | |

Pass condition: all C-01 through C-05 PASS; at least five total PASS across C-01 through C-08.

---

**STRUCTURAL RULE**: Direction defaults to `<-> inert`. Active hops declare departure codes. Every MANIFEST-N closes with `down-arrow TABLE-N begins immediately below` as its final line; that line was already written above each table.

---

## V-02 · Role Sequence — Schema Architect Produces TRAVERSAL-SCHEMA from Requirements (C-39 Target)

**Axis**: Role sequence
**Hypothesis**: C-39 requires the model to author the schema principles, not fill in a pre-written template. R11 V-05 was the closest prototype — it had a TRAVERSAL-SCHEMA artifact — but the schema's principles were pre-written in the prompt (the model only filled in Framework/State management fields). V-02 inverts this: the model receives REQUIREMENTS for the schema, then writes the schema content including the inert-default rule and adjacency rule from scratch. A model that then violates a rule it wrote is contradicting its own output, not disobeying an external constraint. Role 2 implements the schema the model produced; manifests end with close-line markers (the model instantiates the adjacency rule it declared). Expected score: ~150-152/152.

---

You have two roles in this trace. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are a schema architect designing the output schema for a frontend component trace. Your task is to produce a TRAVERSAL-SCHEMA document — a named artifact that specifies how the trace will be structured. This document is part of the output; it is not an internal planning note.

Your TRAVERSAL-SCHEMA must address the following requirements:

**Requirement A — Framework identification**: Declare the framework, state management layer, and component model you are tracing.

**Requirement B — Direction column contract**: Specify the default value of the Direction column in the traversal table. Explain what an unlabeled cell means under your schema. List the active departure codes available and define when each applies.

**Requirement C — Manifest-analysis pairing rule**: Specify the structural relationship between a MANIFEST-N block and its TABLE-N block. Include: (a) what appears in the manifest, (b) how the manifest closes, and (c) what may or may not appear between the manifest's closing line and the table's header row. Write the exact text of the closing marker that will appear at the end of every manifest in this trace.

**Requirement D — Table inventory**: List every table this trace will produce by name and purpose.

Write the TRAVERSAL-SCHEMA as a legible, named document. A reader must be able to verify your compliance by referencing it.

```
TRAVERSAL-SCHEMA
----------------
[Author this document now. Address Requirements A through D completely.
Write the schema's rules in your own words — do not reproduce instruction text.
This is the governing artifact for the trace that follows.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace using the TRAVERSAL-SCHEMA you authored above. Every rule you declared is in effect. Violating the schema contradicts your own prior output.

---

**MANIFEST-1 · Event Phase**
```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Close this manifest with the exact closing marker declared in your TRAVERSAL-SCHEMA before TABLE-1.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**
```
Components in scope: [all traversal hops — include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Close this manifest with the exact closing marker declared in your TRAVERSAL-SCHEMA before TABLE-2.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Direction contract — apply the default value and departure codes you declared.

| Step | T-ID | Component | Direction [per your TRAVERSAL-SCHEMA] | Role [Acted: desc / Inert: reason] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | *(your default value or departure code)* | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**
```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Close this manifest with the exact closing marker declared in your TRAVERSAL-SCHEMA before TABLE-3.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| | | *(local / context / store)* | *(direct / inherited)* | | | |

[GATE-3: TABLE-3 does not close on "state updates", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**
```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Close this manifest with the exact closing marker declared in your TRAVERSAL-SCHEMA before TABLE-4.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | | Yes (1) / No | | Yes — [reason] / No — [reason] | |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**
```
Components in scope: [components in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Close this manifest with the exact closing marker declared in your TRAVERSAL-SCHEMA before TABLE-5.]*

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

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", or collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · "none" row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA framework declaration + declared terms throughout | |

---

## V-03 · Inertia Framing — Inertia as Null Hypothesis (C-36 Reinforced)

**Axis**: Inertia framing
**Hypothesis**: R11 variations encoded inertia as a default value in a column header — a syntactic mechanism. V-03 tests whether framing inertia as the null hypothesis — the epistemic baseline that must be disproved — produces stronger C-36 compliance. The phrasing shifts from "inertia is the default code" to "inertia is the claim: unless you actively assert departure, you are claiming this hop did nothing." This inverts the burden: a departure code is a falsifying claim; an inert annotation is the null. Models that internalize the null-hypothesis framing may be more resistant to treating missing annotations as "probably active" — they are claims of inactivity, not omissions. C-38 not targeted (no close-line as primary mechanism, uses header annotation instead). C-39 not targeted (no schema authoring). Expected score: ~146-150/152 depending on C-38/C-39 coverage.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding. All output uses that framework's exact terminology.

**EPISTEMIC PRINCIPLE**: In this trace, inertia is the null hypothesis. Every traversal hop is presumed inert — producing no mutation, triggering no side effect — until departure is actively asserted. A departure code is a claim; an inert annotation is the null. A hop with a departure code that cannot be substantiated is a false claim. A hop with no departure code is a verified null. Treat undocumented inert hops as incomplete traces, not clean traces.

---

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

---

**MANIFEST-1 · Event Phase** *(fill completely before writing TABLE-1 — TABLE-1 begins immediately below this block)*

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase** *(fill completely before writing TABLE-2 — TABLE-2 begins immediately below this block)*

```
Components in scope: [all traversal hops — include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-2 · Component Tree Traversal — Null-Hypothesis Direction Schema**

Inertia is the null hypothesis. The Direction column encodes this: `<-> inert` is not one option among equals — it is the default claim that a hop does nothing. Falsify it by declaring a departure code. Active codes are falsifying claims that require support; absence of a code is the null claim of inertia.

Null: `<-> inert` — hop receives event or prop; produces no mutation; fires no side effect.
Falsifying departures (replace null to assert activity):
- `prop-pass` — asserts downward prop transmission
- `event-propagate` — asserts upward event propagation
- `dispatch` — asserts store dispatch
- `effect-trigger` — asserts side effect activation
- `context-provide` — asserts context provision or update

| Step | T-ID | Component | Direction [<-> inert (null hypothesis) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role [Null: inertia confirmed / Active: departure code + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | `<-> inert` *(or departure code — asserting activity)* | Null: [inertia reason] / Active: [departure + evidence] | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4. A departure code without supporting evidence in Role column is an unsupported claim.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
Null-hypothesis confirmed: [brief basis for each, or "all hops asserted active — see departure codes"]
[If count = 0]: No inert hops — all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, a blank Role cell, or a departure code without Role evidence.]

---

**MANIFEST-3 · Mutation Phase** *(fill completely before writing TABLE-3 — TABLE-3 begins immediately below this block)*

```
Components in scope: [components that own or dispatch mutations]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct — state writes the event handler or synchronous code produces immediately.
- Inherited — state writes triggered transitively through useEffect, watch, computed cascades, store middleware, or subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| *(exact key)* | *(component or store slice)* | *(local / context / store)* | *(direct / inherited)* | *(shape)* | *(shape)* | *(mechanism)* |

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase** *(fill completely before writing TABLE-4 — TABLE-4 begins immediately below this block)*

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including null-hypothesis (inert) hops, which may still re-render from prop or context changes.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | *(owns state / receives new props / subscribes to changed context / no state owned / not subscribed)* | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase** *(fill completely before writing TABLE-5 — TABLE-5 begins immediately below this block)*

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

If no side effects: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", or collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a — no issue")* | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · "none" row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | Framework Declaration + declared terms in TABLE-2 through TABLE-7 | |

---

**CLOSING MANDATE**: The null hypothesis is inertia. Every active departure is an asserted claim. Undocumented inert hops are incomplete traces, not clean ones.

---

## V-04 · Combined: Manifest-Close Marker + Schema Architect Role (C-38 + C-39)

**Axis**: Role sequence + Lifecycle emphasis (combined)
**Hypothesis**: V-01 targets C-38 (close-line as manifest's last content) and V-02 targets C-39 (model-authored schema from requirements). V-04 combines them with a structural link: Role 1 (Schema Architect) authors the TRAVERSAL-SCHEMA, and the schema's Requirement C explicitly declares the text of the close-line marker that will appear at the end of every manifest in Role 2. When Role 2 produces manifests ending with that close-line, it is implementing its own prior-role artifact — satisfying C-38 (close-line as last manifest content) and C-39 (self-authored schema) via a single causal chain. Violation in Role 2 is self-contradiction at two levels: it contradicts the close-line just written AND contradicts the schema authored in Role 1. Expected score: ~150-152/152.

---

You have two roles in this trace. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are a schema architect. Produce a TRAVERSAL-SCHEMA artifact — a named document that will govern the trace in Role 2. This is an output, not a planning note. A reader must be able to reference it to verify Role 2's compliance.

Your TRAVERSAL-SCHEMA must address each requirement below. Write the rules in your own words — do not reproduce instruction text.

**Requirement A — Framework context**: Identify the framework, state management library, and component model.

**Requirement B — Direction default contract**: Specify the default value of the traversal table's Direction column. Explain what it means when no departure code is declared for a hop. List all active departure codes and define when each applies.

**Requirement C — Manifest-to-table adjacency rule**: Specify that each MANIFEST-N block in the trace is immediately followed by TABLE-N with no content between them. Declare the exact text of the closing marker that must appear as the final line of every manifest block. This marker is what makes adjacency verifiable at point-of-production — a model that adds content after it must contradict the last line it wrote.

**Requirement D — Table inventory**: List every table this trace will produce by name and purpose, including the Criteria Audit table.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Address Requirements A through D.
The closing marker text you declare in Requirement C will appear verbatim
at the end of each manifest in Role 2.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Requirement C names the closing marker text.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace using the TRAVERSAL-SCHEMA you authored above. Apply the Direction default you declared. End every manifest with the closing marker you specified in Requirement C — verbatim, as the manifest's last content line.

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops — include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Direction contract — apply the default value and departure codes you declared.

| Step | T-ID | Component | Direction [your declared default \| your declared departure codes] | Role [Acted: desc / Inert: reason] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | *(your default or departure code)* | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops — all traversal components contribute to state or effects.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct — immediate state writes from the event handler or synchronous code.
- Inherited — transitive state writes via useEffect, watch, computed cascades, middleware, subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| | | *(local / context / store)* | *(direct / inherited)* | | | |

[GATE-3: TABLE-3 does not close on "state updates", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | | Yes (1) / No | | Yes — [reason] / No — [reason] | |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*

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

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", or collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [finding or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · "none" row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA declaration + declared terms throughout | |

---

## V-05 · Combined: Schema Architect + Null-Hypothesis Inertia + Close-Line Enforcement (All Three Axes)

**Axis**: Role sequence + Inertia framing + Lifecycle emphasis (combined)
**Hypothesis**: V-02 adds schema authorship (C-39); V-03 adds null-hypothesis inertia framing (C-36); V-01 adds close-line enforcement (C-38). V-05 integrates all three via a single mechanism: the model authors a TRAVERSAL-SCHEMA in Role 1 that (a) frames inertia-as-null-hypothesis as the governing epistemology — every departure is a claim requiring falsification evidence — and (b) explicitly declares the close-line marker text that must appear at each manifest's end. Role 2 then implements both: each manifest ends with the close-line (C-38), each Direction cell defaults to `<-> inert` as the null (C-36, C-39), and the schema artifact was authored by the model (C-39). The inertia-as-null framing propagates from the schema through the traversal table through the findings: an unnecessary re-render is a "false active departure" (the render claimed necessity that cannot be supported). Expected score: ~150-152/152.

---

You have two roles in this trace. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are a schema architect. Design the epistemological framework and structural schema for this trace. Produce a TRAVERSAL-SCHEMA artifact — a named, legible document. This is an output, not a planning note.

Your schema must address these requirements. Write the principles yourself — do not reproduce instruction text.

**Requirement A — Framework**: Declare the framework, state management library, and component model.

**Requirement B — Inertia as null hypothesis**: Define the epistemic status of inertia in this trace. Specify: what does it mean for a traversal hop to be inert? Why is inertia treated as the null hypothesis rather than a special case? What constitutes a departure claim, and what makes a departure claim valid vs. unsupported? How does this principle manifest in the Direction column's default value?

**Requirement C — Manifest close-line marker**: Declare the exact text that will appear as the last content line of every MANIFEST-N block in Role 2. Explain why the marker must be the manifest's final line (not in a header annotation or document preamble) and what structural violation it produces if content appears after it.

**Requirement D — Table inventory**: List every table by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Requirements A through D addressed in full.
The text you declare for Requirement C will appear verbatim at the end of
each manifest in Role 2. The epistemic framework from Requirement B will
govern Direction cell choices throughout TABLE-2.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace using the TRAVERSAL-SCHEMA you authored. Apply the null-hypothesis epistemic framework from Requirement B: every Direction cell defaults to the inert null; departure codes are active claims requiring evidence. End every manifest with the Requirement C close-line — verbatim, as the manifest's last content.

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Requirement C close-line — verbatim, last line of this manifest.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops — pass-through hops included; null-hypothesis applies to all]
State keys may be touched: ___
Side effects may fire: ___
```
*[Requirement C close-line — verbatim, last line of this manifest.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA: apply the null-hypothesis Direction default you declared. Every departure code is an active claim backed by Role evidence. An undocumented inert hop is a confirmed null, not an omission.

| Step | T-ID | Component | Direction [null hypothesis: your declared default \| active claims: your declared departure codes] | Role [Null confirmed: reason / Active claim: departure + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | *(your default, or departure code if active claim is supported)* | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
Null confirmed: [brief basis per inert T-ID, or "none — all departure claims supported"]
[If count = 0]: No inert hops — all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or a departure code without Role evidence.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Requirement C close-line — verbatim, last line of this manifest.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct — state writes the event handler or synchronous code produces immediately.
- Inherited — transitive state writes via useEffect, watch, computed cascades, middleware, subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none — no effects, subscriptions, or watchers triggered.
Reason: [read-only / display-only / event consumed without dispatch / other]
```

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|
| | | *(local / context / store)* | *(direct / inherited)* | | | |

[GATE-3: TABLE-3 does not close on "state updates", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Requirement C close-line — verbatim, last line of this manifest.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — inert null-hypothesis hops included; they may still re-render from external prop or context changes.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — unsupported re-render claim] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | | Yes (1) / No | | Yes — [reason] / No — [unsupported necessity: memoization missing / selector too broad / etc.] | |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Requirement C close-line — verbatim, last line of this manifest.]*

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

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", or collapsed rows 3+4.]

---

**TABLE-7 · Findings** N/A prohibited.

The null-hypothesis lens applies: an unnecessary re-render is a re-render whose necessity claim cannot be supported. Findings are confirmed claims — not observations, not concerns.

| ID | Category | Component / State Path | Finding [confirmed issue or "none detected — [basis for null]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unsupported re-render claims")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · "none" row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA declaration + declared terms throughout | |

---

**CLOSING MANDATE**: Inertia is the null hypothesis. Departure is a claim. Evidence is required. The close-line you declared in Requirement C appears as the last content of every manifest; content appearing after it contradicts the last line you wrote.

---

## Variation Axis Summary

| Variation | Primary axis | C-38 mechanism | C-39 mechanism | Expected delta |
|-----------|-------------|----------------|----------------|----------------|
| V-01 | Lifecycle emphasis | Close-line as manifest's absolute last content | None — no model-authored schema | C-38 +2, C-39 0 |
| V-02 | Role sequence | Close-line instantiated from model-authored schema | Model produces schema from requirements (not template) | C-38 +2, C-39 +2 |
| V-03 | Inertia framing | Header annotation (C-38 partial risk) | None | C-38 partial, C-39 0 |
| V-04 | Role sequence + Lifecycle | Close-line verbatim from Requirement C (causal chain) | Model authors schema; Req C declares close-line text | C-38 +2, C-39 +2 |
| V-05 | All three axes | Close-line verbatim from Requirement C | Model authors schema including null-hypothesis framing | C-38 +2, C-39 +2 |

**Key C-38 distinction**: V-01 uses the close-line directly in the prompt manifest template (prompt-provided but positionally correct). V-02/V-04/V-05 have the model declare the close-line text in the schema artifact and then instantiate it in each manifest — a stronger causal chain where the model is the author of both the rule and its implementation.

**Key C-39 distinction**: V-02/V-04/V-05 ask the model to write the schema's principles from requirements. V-03 provides the principles as a preamble narrative (the prompt author wrote them) — C-39 would likely fail V-03 because the epistemic framing is in the prompt, not authored by the model.
