# trace-component — Round 14 Variations

**Variation axes used:**
- Single-axis: Role sequence / C-43+C-44+C-45 authorship target (V-01), Phrasing register / C-45+C-44+C-43 notational isolation (V-02), Lifecycle emphasis / phase-opening constraint contract (V-03)
- Combined: Role sequence + Phrasing register / architect-authored bracket notation (V-04), All three axes + Inertia framing / unified null-hypothesis (V-05)

**R14 context:** Three new criteria from R13 excellence signals:

- **C-43 (Mutual-Constraint Entanglement Declaration)** — Each dual-constraint placeholder must include an explicit statement that neither the content constraint nor the positional constraint can be satisfied without the other. R13 V-03 and V-05 were the sole high-water marks: "Neither constraint is satisfied without the other" / "Neither satisfied without the other" appearing within the placeholder body. C-40 requires co-location of both constraints; C-43 requires the additional entanglement declaration that satisfying one alone does not partially satisfy the dual requirement.

- **C-44 (Numbered Constraint Enumeration in Placeholder)** — Each dual-constraint placeholder must enumerate content and positional constraints as a numbered list — "(1) content — ...; (2) position — ..." or equivalent numbered form — rather than as a compound or conjunctive sentence. R13 V-03: `(1) content — reproduce TRACE CHARTER's close-line exactly; (2) position — absolute last line`. R13 V-05: `(1) content — TRAVERSAL-SCHEMA Area 3 close-line exactly; (2) position — final content of MANIFEST-N`. Numbered items give each constraint a discrete independently-checkable address; compound phrasing allows conflation at point-of-production.

- **C-45 (Dual-Requirement Count Declaration in Placeholder)** — Each dual-constraint placeholder must open with an explicit count declaration as its leading phrase, before constraints are enumerated. R13 V-03: "Two requirements, one instruction:". R13 V-05: "Two simultaneous constraints — one instruction:". The count declaration establishes the N=2 obligation at the placeholder's first token; without it, a model can read two constraints as aspects of a single compound requirement.

**C-43 / C-44 / C-45 orthogonality:**
- C-43 can pass without C-44 (entanglement declared, constraints not numbered)
- C-44 can pass without C-43 (constraints numbered, no entanglement declaration)
- C-45 can pass without C-43 or C-44 (count declared, constraints not numbered and not entangled)
- Full expression requires all three: C-45 establishes obligation count, C-44 makes each constraint independently checkable, C-43 binds them as mutually inseparable

**R14 hypothesis for each variation:**
- V-01: Role sequence — explicitly task the schema architect with deriving and justifying each of the three placeholder properties (C-45, C-44, C-43) from abstract failure-mode reasoning. Tests whether self-authored justification of all three properties produces more robust compliance than receiving the form from a prompt charter. C-41/C-42 partially targeted. Expected: ~160–162/164.
- V-02: Phrasing register — charter-based (no schema architect); clinical bracket notation for the count and enumeration: `[DUAL-CONSTRAINT BLOCK | N=2 OBLIGATIONS: OBL-1...; OBL-2...; Mutual dependency: neither independently satisfies the block.]`. Tests whether a clinical/technical notational register for C-45+C-44+C-43 produces different compliance characteristics than natural language. C-39 not targeted. Expected: ~156–158/164.
- V-03: Lifecycle emphasis — each manifest opens with a PHASE CONTRACT that forward-declares the dual-constraint obligation before the manifest body; the close-line placeholder references the already-declared contract. Tests whether front-loading the entanglement constraint (lifecycle position: opening vs. closing only) strengthens compliance by keeping it active throughout the phase. Charter-based. Expected: ~158–160/164.
- V-04: Role sequence + Phrasing register (combined) — schema architect designs the placeholder in clinical bracket notation from first principles (V-01 reasoning + V-02 notation). Tests whether architect-authored reasoning in formal notation is the strongest combination. Expected: ~160–164/164.
- V-05: All three axes + Inertia framing — unified null-hypothesis epistemology where the inert-default principle (Area 2) and the post-manifest null (Area 3) are both instances of the same epistemic framework; the three placeholder properties (C-45+C-44+C-43) are framed as the mechanism making null-violation structurally visible. Phase contracts (lifecycle emphasis) + clinical notation (phrasing register) + architect authorship. Maximum R14 coverage. Expected: ~162–164/164.

---

## V-01 · Role Sequence — Schema Architect Designs Three-Property Placeholder (C-45+C-44+C-43 Authorship Target)

**Axis**: Role sequence
**Hypothesis**: R13 V-03 provided the C-43+C-44+C-45 form via prompt charter; R13 V-05 embedded it in schema-architect manifests but did not ask the architect to justify each property. V-01 explicitly tasks the architect with deriving each of the three placeholder properties (count opener, numbered enumeration, entanglement declaration) from abstract failure-mode reasoning — not from copyable instruction language. When the model has articulated why C-45 prevents two-constraints-as-one-compound misreading, why C-44 makes each constraint independently checkable, and why C-43 forecloses partial satisfaction, the three properties become logical consequences of the model's own causal output. Manifests carry the full three-property form referencing the authored schema. C-41 partially targeted (causal reasoning required). C-42 not targeted (abstract requirements, not blank-slot). Expected score: ~160–162/164.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

Design the governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows.

The schema must be authored in your own words. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting instruction text into schema format. Every rule must derive from your reasoning about the tracing task.

**Area 1 — Framework context**: Declare the framework, state management library, and component model being traced.

**Area 2 — Direction default contract**: What is the default state of a traversal hop before evidence is considered? Define the default value of the Direction column and explain what a cell means when it carries no departure code. List each active departure code and define when it applies. Why must inert hops be documented explicitly rather than omitted?

**Area 3 — Manifest close-line placeholder design**: Design the placeholder instruction that will appear as the final line of every manifest block in this trace. The placeholder must enforce two constraints simultaneously within a single instruction: (a) the content constraint — the model reproduces the exact close-line text you declare, verbatim, without alteration; (b) the positional constraint — the reproduced text occupies the manifest's last content line, with the analysis table following immediately below.

To make both constraints simultaneously enforceable, your placeholder must carry three structural properties. For each property, reason from the failure mode it prevents:

- **Property A (count declaration as leading phrase)**: A model reading a placeholder that contains two constraints expressed without a preceding count declaration can interpret those constraints as aspects of a single compound requirement. What does a leading count declaration accomplish that constraint enumeration alone does not? Why must the count declaration appear before the constraints are read, not after?

- **Property B (numbered enumeration)**: A compound sentence such as "reproduce the text verbatim as the manifest's last line" conflates two constraints into one surface expression. What does numbered enumeration enable that compound form cannot? Why does each numbered item require independent satisfaction, and why is that not guaranteed by a compound instruction?

- **Property C (entanglement declaration)**: Even when both constraints are co-located and numbered, a model can claim that satisfying the content constraint (reproducing the text correctly, wherever it appears) partially satisfies the dual requirement. What explicit declaration closes this loophole? Why must it appear within the placeholder body, not in a surrounding prose instruction?

Having articulated the rationale for all three properties, write the complete placeholder instruction text. It must: open with a count declaration naming exactly two requirements (Property A), enumerate each constraint as a numbered item with its content source and positional declaration (Property B), and include an entanglement statement declaring that neither constraint independently satisfies the dual requirement (Property C). The placeholder must also name: (i) the content source — where in your TRAVERSAL-SCHEMA to find the exact close-line text to reproduce verbatim; (ii) the positional declaration — that this line is the manifest's last content, the analysis table follows directly.

Then declare the exact close-line text the placeholder will reproduce at every manifest close.

**Area 4 — Table inventory**: List every table this trace produces by name and purpose, including the Criteria Audit table.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 For Area 3: write Property A, B, C rationale BEFORE writing the placeholder instruction text.
 The complete placeholder instruction text you write is what will appear verbatim at every
 manifest close-line slot in Role 2. The close-line text you declare is what the placeholder
 instructs the model to reproduce.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the three-property rationale and the complete placeholder instruction text (with all three properties embedded), and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: use the placeholder instruction you authored in Area 3 — exactly as written, verbatim. That instruction carries three structural properties whose rationale you articulated in Area 3. Satisfying any one property without the other two does not satisfy the placeholder. You stated why in your own words.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[from your TRAVERSAL-SCHEMA Area 1]` |
| State management | `[from your TRAVERSAL-SCHEMA Area 1]` |
| Component model | `[from your TRAVERSAL-SCHEMA Area 1]` |

Do not begin MANIFEST-1 until this header is complete.

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. That instruction carries Property A (count declaration as leading phrase), Property B (numbered enumeration), and Property C (entanglement declaration). Neither property independently satisfies the placeholder. Write the close-line now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. That instruction carries Property A (count declaration as leading phrase), Property B (numbered enumeration), and Property C (entanglement declaration). Neither property independently satisfies the placeholder. Write the close-line now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the Direction default you declared and the departure codes you specified.

| Step | T-ID | Component | Direction [your declared default \| your declared departure codes] | Role [Acted: desc / Inert: reason] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. That instruction carries Property A (count declaration as leading phrase), Property B (numbered enumeration), and Property C (entanglement declaration). Neither property independently satisfies the placeholder. Write the close-line now.]*

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

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. That instruction carries Property A (count declaration as leading phrase), Property B (numbered enumeration), and Property C (entanglement declaration). Neither property independently satisfies the placeholder. Write the close-line now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. That instruction carries Property A (count declaration as leading phrase), Property B (numbered enumeration), and Property C (entanglement declaration). Neither property independently satisfies the placeholder. Write the close-line now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA declaration + framework terms throughout | |

---

## V-02 · Phrasing Register — Clinical Bracket Notation (C-45+C-44+C-43 Notational Isolation)

**Axis**: Phrasing register
**Hypothesis**: R13 V-03 and V-05 used natural-language openers for the count-declaration and enumeration: "Two requirements, one instruction:" and "Two simultaneous constraints — one instruction:". V-02 tests whether a clinical bracket-notation register — where the count appears as a formal label `N=2 OBLIGATIONS` and constraints are labeled `OBL-1`/`OBL-2` — produces different compliance characteristics for C-45/C-44/C-43. The notation shifts from conversational to technical without changing the structural properties: N=2 count opener (C-45), labeled numbered items (C-44), mutual-dependency declaration (C-43). No schema architect role — charter-based, clean phrasing-register isolation. C-39 not targeted. Expected score: ~156–158/164.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding.

---

**TRACE CHARTER**

This trace is governed by the following structural rules.

**Direction schema**: Every traversal hop begins as `<-> inert` — the default null requiring no justification. Active departure codes replace the default only when the hop is demonstrably active:
- `prop-pass` — downward prop transmission to a child
- `event-propagate` — upward event propagation to a parent
- `dispatch` — store dispatch triggering a state write
- `effect-trigger` — activation of a side effect (API call, timer, subscription, navigation)
- `context-provide` — context provision or update

**Manifest close-line** (apply verbatim at every manifest block close):
`▼ Analysis table begins immediately below. No content may appear between this line and the table header.`

---

**FRAMEWORK DECLARATION (required output header)**

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
*[DUAL-CONSTRAINT BLOCK | N=2 OBLIGATIONS — (OBL-1) content: reproduce the TRACE CHARTER manifest close-line text exactly, character for character, no modification permitted; (OBL-2) position: this block is the manifest's terminal content line, the analysis table header follows with no intervening content. Mutual dependency: OBL-1 satisfied alone does not satisfy this block; OBL-2 satisfied alone does not satisfy this block; both must be independently and simultaneously satisfied. Reproduce the close-line now.]*

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
*[DUAL-CONSTRAINT BLOCK | N=2 OBLIGATIONS — (OBL-1) content: reproduce the TRACE CHARTER manifest close-line text exactly, character for character, no modification permitted; (OBL-2) position: this block is the manifest's terminal content line, the analysis table header follows with no intervening content. Mutual dependency: OBL-1 satisfied alone does not satisfy this block; OBL-2 satisfied alone does not satisfy this block; both must be independently and simultaneously satisfied. Reproduce the close-line now.]*

**TABLE-2 · Component Tree Traversal**

Direction default: `<-> inert`. Active departure codes replace the default per the TRACE CHARTER. A departure code without supporting Role-column evidence is an unsupported claim.

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role [Inert: basis confirmed / Acted: departure code + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
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
*[DUAL-CONSTRAINT BLOCK | N=2 OBLIGATIONS — (OBL-1) content: reproduce the TRACE CHARTER manifest close-line text exactly, character for character, no modification permitted; (OBL-2) position: this block is the manifest's terminal content line, the analysis table header follows with no intervening content. Mutual dependency: OBL-1 satisfied alone does not satisfy this block; OBL-2 satisfied alone does not satisfy this block; both must be independently and simultaneously satisfied. Reproduce the close-line now.]*

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

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[DUAL-CONSTRAINT BLOCK | N=2 OBLIGATIONS — (OBL-1) content: reproduce the TRACE CHARTER manifest close-line text exactly, character for character, no modification permitted; (OBL-2) position: this block is the manifest's terminal content line, the analysis table header follows with no intervening content. Mutual dependency: OBL-1 satisfied alone does not satisfy this block; OBL-2 satisfied alone does not satisfy this block; both must be independently and simultaneously satisfied. Reproduce the close-line now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[DUAL-CONSTRAINT BLOCK | N=2 OBLIGATIONS — (OBL-1) content: reproduce the TRACE CHARTER manifest close-line text exactly, character for character, no modification permitted; (OBL-2) position: this block is the manifest's terminal content line, the analysis table header follows with no intervening content. Mutual dependency: OBL-1 satisfied alone does not satisfy this block; OBL-2 satisfied alone does not satisfy this block; both must be independently and simultaneously satisfied. Reproduce the close-line now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRACE CHARTER direction schema + framework terms throughout | |

---

## V-03 · Lifecycle Emphasis — Phase-Opening Constraint Contract (C-45+C-44+C-43 Forward Declaration)

**Axis**: Lifecycle emphasis
**Hypothesis**: In R13 V-03 and V-05, the C-43+C-44+C-45 three-property form appeared only at the manifest's close-line position. V-03 tests whether positioning the entanglement declaration at the manifest's OPENING — as a forward-declared PHASE CONTRACT before the manifest body — and then referencing that contract in the close-line placeholder produces stronger compliance. The mechanism: the model reads the N=2 dual-constraint obligation before filling the manifest body, making both the count (C-45), numbered enumeration (C-44), and entanglement (C-43) active throughout the phase rather than only at the close. The placeholder then references the already-declared contract, providing a structural bridge between opening declaration and closing execution. Charter-based, no schema architect. Tests whether lifecycle position of the entanglement constraint (opening + close vs. close-only) affects compliance. Expected score: ~158–160/164.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding.

---

**TRACE CHARTER**

This trace is governed by the following structural rules.

**Direction schema**: Every traversal hop begins as `<-> inert` — the default null requiring no justification. Active departure codes replace the default only when the hop is demonstrably active:
- `prop-pass` — downward prop transmission
- `event-propagate` — upward event propagation
- `dispatch` — store dispatch
- `effect-trigger` — side effect activation
- `context-provide` — context provision or update

**Manifest close-line** (apply verbatim at every manifest block close):
`▼ Analysis table begins immediately below. No content may appear between this line and the table header.`

**Phase Contract format** (open every manifest with this block before the manifest body):
```
PHASE CONTRACT: Two requirements govern this manifest's close-line —
  (1) content — reproduce the TRACE CHARTER manifest close-line text exactly, verbatim
  (2) position — the close-line is this manifest's terminal content line; analysis table follows directly
Entanglement: neither (1) nor (2) alone satisfies the close-line obligation.
```

---

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[React / Vue / Angular / Svelte / other — name exactly]` |
| State management | `[Redux / Zustand / Pinia / NgRx / Context API / none — name exactly]` |
| Component model | `[functional hooks / class components / Options API / Composition API / other]` |

---

**MANIFEST-1 · Event Phase**

```
PHASE CONTRACT: Two requirements govern this manifest's close-line —
  (1) content — reproduce the TRACE CHARTER manifest close-line text exactly, verbatim
  (2) position — the close-line is this manifest's terminal content line; analysis table follows directly
Entanglement: neither (1) nor (2) alone satisfies the close-line obligation.
```

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Two requirements, one instruction — as declared in this manifest's Phase Contract: (1) content — reproduce the TRACE CHARTER manifest close-line exactly, verbatim; (2) position — this is the terminal content line of MANIFEST-1, TABLE-1 header follows directly. Neither satisfied without the other. Write the close-line now.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
PHASE CONTRACT: Two requirements govern this manifest's close-line —
  (1) content — reproduce the TRACE CHARTER manifest close-line text exactly, verbatim
  (2) position — the close-line is this manifest's terminal content line; analysis table follows directly
Entanglement: neither (1) nor (2) alone satisfies the close-line obligation.
```

```
Components in scope: [all traversal hops — include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Two requirements, one instruction — as declared in this manifest's Phase Contract: (1) content — reproduce the TRACE CHARTER manifest close-line exactly, verbatim; (2) position — this is the terminal content line of MANIFEST-2, TABLE-2 header follows directly. Neither satisfied without the other. Write the close-line now.]*

**TABLE-2 · Component Tree Traversal**

Direction default: `<-> inert`. Active departure codes replace the default per the TRACE CHARTER.

| Step | T-ID | Component | Direction [<-> inert (default) \| prop-pass \| event-propagate \| dispatch \| effect-trigger \| context-provide] | Role [Inert: reason confirmed / Acted: departure + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
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
PHASE CONTRACT: Two requirements govern this manifest's close-line —
  (1) content — reproduce the TRACE CHARTER manifest close-line text exactly, verbatim
  (2) position — the close-line is this manifest's terminal content line; analysis table follows directly
Entanglement: neither (1) nor (2) alone satisfies the close-line obligation.
```

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Two requirements, one instruction — as declared in this manifest's Phase Contract: (1) content — reproduce the TRACE CHARTER manifest close-line exactly, verbatim; (2) position — this is the terminal content line of MANIFEST-3, TABLE-3 header follows directly. Neither satisfied without the other. Write the close-line now.]*

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

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
PHASE CONTRACT: Two requirements govern this manifest's close-line —
  (1) content — reproduce the TRACE CHARTER manifest close-line text exactly, verbatim
  (2) position — the close-line is this manifest's terminal content line; analysis table follows directly
Entanglement: neither (1) nor (2) alone satisfies the close-line obligation.
```

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Two requirements, one instruction — as declared in this manifest's Phase Contract: (1) content — reproduce the TRACE CHARTER manifest close-line exactly, verbatim; (2) position — this is the terminal content line of MANIFEST-4, TABLE-4 header follows directly. Neither satisfied without the other. Write the close-line now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
PHASE CONTRACT: Two requirements govern this manifest's close-line —
  (1) content — reproduce the TRACE CHARTER manifest close-line text exactly, verbatim
  (2) position — the close-line is this manifest's terminal content line; analysis table follows directly
Entanglement: neither (1) nor (2) alone satisfies the close-line obligation.
```

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Two requirements, one instruction — as declared in this manifest's Phase Contract: (1) content — reproduce the TRACE CHARTER manifest close-line exactly, verbatim; (2) position — this is the terminal content line of MANIFEST-5, TABLE-5 header follows directly. Neither satisfied without the other. Write the close-line now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRACE CHARTER direction schema + framework terms throughout | |

---

## V-04 · Combined: Role Sequence + Phrasing Register — Architect-Authored Bracket Notation (C-45+C-44+C-43 + C-41 + C-42)

**Axis**: Role sequence + Phrasing register (combined)
**Hypothesis**: V-01 targets C-43+C-44+C-45 via schema-architect reasoning (role sequence axis). V-02 targets the same criteria via clinical bracket notation (phrasing register axis). V-04 combines them: the schema architect is tasked with designing the three-property placeholder template in clinical OBL-1/OBL-2 bracket-notation form, from abstract failure-mode questions (C-42 partially targeted). Area 3 requires causal reasoning for each property before the placeholder text is written (C-41 targeted). Manifests carry the architect-authored bracket-notation form with full C-43+C-44+C-45 coverage. The combination tests whether the self-authored causal reasoning produces more reliable bracket-notation compliance than a provided-charter bracket form (V-02). Expected score: ~160–164/164.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

Design the governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows.

The schema must be authored in your own words. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting instruction text. Every principle must derive from your reasoning.

**Area 1 — Framework context**: Declare the framework, state management library, and component model being traced.

**Area 2 — Direction default contract**: What does a traversal hop's Direction cell mean when no departure code is assigned? Define the default value. Define every active departure code and when it applies. Explain why a Direction cell must never be blank — what failure mode does a blank Direction cell represent?

**Area 3 — Manifest close-line placeholder**: Design a placeholder instruction that enforces both the content constraint (verbatim reproduction of the declared close-line text) and the positional constraint (this placeholder occupies the manifest's terminal line) within a single instruction. The placeholder must use clinical bracket notation — structured as a labeled block with named obligation items.

Before writing the placeholder, answer these questions in sequence:

- **Question 1 (count declaration as leading label)**: What does a model infer about the number of obligations imposed by an instruction that carries no obligation count at its start? Why must the block open with an explicit count label — e.g., `N=2 OBLIGATIONS` or `OBLIGATION-COUNT: 2` — before the individual obligations are listed, rather than after or embedded in the block's body?

- **Question 2 (labeled obligation items)**: Why does a compound phrase such as "reproduce the close-line text as the manifest's last line" allow partial compliance? How does assigning each obligation a distinct label — OBL-1, OBL-2, or equivalent — give each obligation an independently verifiable address? Why is a labeled item not satisfied by satisfying the other labeled item?

- **Question 3 (mutual-dependency declaration)**: Even with a count label and individually labeled obligations, a model could argue that satisfying OBL-1 implicitly satisfies OBL-2 (or vice versa). What explicit declaration within the placeholder body forecloses this argument? Why must this declaration name both obligations by label and state their mutual dependency, not merely assert the block is "complete only when all obligations are met"?

Having answered all three questions, write the complete DUAL-CONSTRAINT BLOCK placeholder in clinical bracket notation. It must: open with a count label (from your Question 1 answer), enumerate obligations as labeled items naming the content source and the positional declaration (from your Question 2 answer), and include a mutual-dependency declaration referencing both obligation labels (from your Question 3 answer).

Then declare the exact close-line text the placeholder will reproduce at every manifest close.

**Area 4 — Table inventory**: List every table this trace produces by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 For Area 3: write Question 1, 2, 3 answers BEFORE writing the DUAL-CONSTRAINT BLOCK placeholder text.
 The placeholder you design will appear verbatim at every manifest close-line slot in Role 2.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the three-question answers and the complete DUAL-CONSTRAINT BLOCK placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored. Apply the Direction default from Area 2. At every manifest close-line slot: use the DUAL-CONSTRAINT BLOCK placeholder you authored in Area 3 — exactly as designed, verbatim. You explained in Area 3 why the count label, labeled obligations, and mutual-dependency declaration are each necessary. Satisfying any one element without the others does not satisfy the block. You stated the reasons.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[from your TRAVERSAL-SCHEMA Area 1]` |
| State management | `[from your TRAVERSAL-SCHEMA Area 1]` |
| Component model | `[from your TRAVERSAL-SCHEMA Area 1]` |

Do not begin MANIFEST-1 until this header is complete.

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label (OBL-count as leading element), labeled obligation items (OBL-1 content, OBL-2 position), and mutual-dependency declaration referencing both labels. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, labeled obligation items (OBL-1 content, OBL-2 position), and mutual-dependency declaration. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the Direction default you declared and the departure codes you specified.

| Step | T-ID | Component | Direction [your declared default \| your declared departure codes] | Role [Inert: basis / Acted: departure + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, labeled obligation items (OBL-1 content, OBL-2 position), and mutual-dependency declaration. Reproduce now.]*

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

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, labeled obligation items (OBL-1 content, OBL-2 position), and mutual-dependency declaration. Reproduce now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes — [reason] / No — [reason] | *(UR-ID or "—")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Apply your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, labeled obligation items (OBL-1 content, OBL-2 position), and mutual-dependency declaration. Reproduce now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected — [reason]"] | Fix — API or Pattern | Do-Nothing Cost |
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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA declaration + framework terms throughout | |

---

## V-05 · Combined: All Three Axes + Inertia Framing — Unified Null-Hypothesis Epistemology

**Axis**: Role sequence + Lifecycle emphasis + Phrasing register (combined)
**Hypothesis**: V-04 combines schema-architect authorship + clinical bracket notation for C-43+C-44+C-45. V-05 adds lifecycle emphasis (phase contracts from V-03) and extends the null-hypothesis framing from R13 V-05 to the three placeholder properties themselves: just as an undocumented active departure is an unsupported claim (Area 2), an unfulfilled dual-constraint close-line is an unsupported compliance claim. Area 3 asks the model to articulate how the three placeholder properties (count label, labeled obligations, mutual-dependency declaration) are the mechanism that makes a partial-satisfaction claim structurally visible — analogous to the Direction column making an undocumented active hop visible. Each manifest opens with a Phase Contract that forward-declares the N=2 obligation in clinical notation. The close-line placeholder references both the authored schema and the manifest's own Phase Contract. Maximum R14 coverage. Expected score: ~162–164/164.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are designing the epistemological framework and governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows.

The schema must be authored in your own words from a blank authorship context. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting instruction text into schema format. Every principle must derive from your reasoning about the tracing task.

**Area 1 — Framework context**: Declare the framework, state management library, and component model being traced.

**Area 2 — Inertia as epistemic null (Direction column)**: Answer these questions in sequence:
- What is the epistemic status of a traversal hop before any evidence is applied — what must be proved, and by whom?
- Why is inertia the default state rather than a named special case requiring documentation?
- What does it mean to claim activity at a hop, and why does that claim require supporting evidence while the null requires none?
- When a model assigns no departure code, what has it asserted about the hop? When a Direction cell is blank, what has the model failed to assert?
- Why must inert hops be listed explicitly in the INERT-HOP DECLARATION rather than omitted?

**Area 3 — Manifest adjacency as null-hypothesis extension, and the three-property placeholder**: The null-hypothesis principle from Area 2 also governs the structural relationship between a manifest block and its analysis table. Answer these questions in sequence, then design the placeholder:

**Null-hypothesis questions:**
- What is the null (default) state of the position between a manifest's final content line and its analysis table header?
- What unsupported claim does a model make by inserting content into that position?
- Why does placing a prohibition marker at the manifest's last position — rather than at the manifest's opening or in a document preamble — make that claim structurally self-contradictory at point-of-production?
- In what structural sense is this parallel to the inert-hop rule from Area 2?

**Three-property placeholder questions:**
- A model satisfying only the content constraint (correct text, wrong position) has made one half of a dual compliance claim. Why does this partial satisfaction remain structurally visible only if the placeholder carries a mutual-dependency declaration? What does the mutual-dependency declaration add that co-location of both constraints alone does not?
- Why must the placeholder open with a count label before the obligation items are listed — what does the count label signal at the placeholder's first token that prevents misclassification of two obligations as one compound requirement?
- Why does assigning each obligation a labeled item (OBL-1, OBL-2 or equivalent) give each obligation an independently checkable address, and why does this make partial satisfaction structurally visible in a way that compound phrasing does not?

Having answered all questions, design the complete DUAL-CONSTRAINT BLOCK placeholder in clinical bracket notation. It must: open with a count label as the block's first element (from your count-label answer), enumerate OBL-1 (content source + verbatim instruction) and OBL-2 (positional declaration + table-follows instruction) as labeled items (from your labeled-obligation answer), and include a mutual-dependency declaration referencing both OBL labels and stating their entanglement (from your mutual-dependency answer).

Then declare the exact close-line text the placeholder will reproduce at every manifest close.

Also design the **Phase Contract format** — the block that will open every manifest before the manifest body. The Phase Contract must: declare the N=2 obligation count, enumerate the two requirements as labeled items matching your DUAL-CONSTRAINT BLOCK notation, and state the entanglement at the phase opening.

**Area 4 — Table inventory**: List every table this trace produces by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full. Do not reproduce any language
 from this prompt in any form.
 For Area 2: author the null-hypothesis principle from your reasoning.
 For Area 3: write both question sets' answers before designing the DUAL-CONSTRAINT BLOCK
 and Phase Contract. The structural parallel between Area 2 and Area 3 is a key authorship
 commitment — it governs both the Direction column and the manifest close-line slot.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 2 articulates the null-hypothesis principle, Area 3 contains the null-hypothesis extension answers, the three-property placeholder answers, the complete DUAL-CONSTRAINT BLOCK placeholder text (with count label, labeled obligation items, and mutual-dependency declaration), the Phase Contract format, and the declared close-line text.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored. Apply the null-hypothesis epistemology from Area 2: every Direction cell defaults to the inert null; departure codes are active claims requiring Role-column evidence. Apply the adjacency guarantee from Area 3: open every manifest with your authored Phase Contract, and close every manifest with the DUAL-CONSTRAINT BLOCK placeholder you designed — verbatim. You explained the structural parallel between inertia-as-null (Area 2) and the post-manifest-null (Area 3), and you derived the three placeholder properties from null-hypothesis reasoning. Violating the placeholder — satisfying only OBL-1 or only OBL-2 — is the same structural error as an undocumented active hop: an unsupported compliance claim. You stated this in your own words.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[from your TRAVERSAL-SCHEMA Area 1]` |
| State management | `[from your TRAVERSAL-SCHEMA Area 1]` |
| Component model | `[from your TRAVERSAL-SCHEMA Area 1]` |

Do not begin MANIFEST-1 until this header is complete.

---

**MANIFEST-1 · Event Phase**

```
[Reproduce your TRAVERSAL-SCHEMA Area 3 Phase Contract here — verbatim as designed.]
```

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label as first element, OBL-1 (content source: TRAVERSAL-SCHEMA Area 3 close-line text, verbatim), OBL-2 (positional: terminal content of MANIFEST-1, TABLE-1 header follows directly), and mutual-dependency declaration referencing OBL-1 and OBL-2. Neither OBL alone satisfies the block. Apply now.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
[Reproduce your TRAVERSAL-SCHEMA Area 3 Phase Contract here — verbatim as designed.]
```

```
Components in scope: [all traversal hops — null-hypothesis applies; include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, OBL-1 (content source: TRAVERSAL-SCHEMA Area 3 close-line, verbatim), OBL-2 (positional: terminal content of MANIFEST-2, TABLE-2 header follows directly), and mutual-dependency declaration. Neither OBL alone satisfies the block. Apply now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null-hypothesis Direction default. Every departure code is an active claim requiring Role-column evidence. An undocumented inert hop is a confirmed null, not an omission.

| Step | T-ID | Component | Direction [null: your declared default \| active claim: your declared departure codes] | Role [Null confirmed: basis / Active claim: departure + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
Null confirmed: [basis per inert T-ID, or "none — all departure claims have Role evidence"]
[If count = 0]: No inert hops — all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or a departure code without Role evidence.]

---

**MANIFEST-3 · Mutation Phase**

```
[Reproduce your TRAVERSAL-SCHEMA Area 3 Phase Contract here — verbatim as designed.]
```

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, OBL-1 (content source: TRAVERSAL-SCHEMA Area 3 close-line, verbatim), OBL-2 (positional: terminal content of MANIFEST-3, TABLE-3 header follows directly), and mutual-dependency declaration. Neither OBL alone satisfies the block. Apply now.]*

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

[GATE-3: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
[Reproduce your TRAVERSAL-SCHEMA Area 3 Phase Contract here — verbatim as designed.]
```

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, OBL-1 (content source: TRAVERSAL-SCHEMA Area 3 close-line, verbatim), OBL-2 (positional: terminal content of MANIFEST-4, TABLE-4 header follows directly), and mutual-dependency declaration. Neither OBL alone satisfies the block. Apply now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — null-hypothesis hops included; they may still re-render from external prop or context changes.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes — reason / No — unsupported re-render claim] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes — [reason] / No — [unsupported: memoization missing / selector too broad / etc.] | |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
[Reproduce your TRAVERSAL-SCHEMA Area 3 Phase Contract here — verbatim as designed.]
```

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block carries: count label, OBL-1 (content source: TRAVERSAL-SCHEMA Area 3 close-line, verbatim), OBL-2 (positional: terminal content of MANIFEST-5, TABLE-5 header follows directly), and mutual-dependency declaration. Neither OBL alone satisfies the block. Apply now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | — | No API calls, timers, subscriptions, or navigation triggered. | — | — |`

---

**TABLE-6 · Final UI State — Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

The null-hypothesis lens applies: an unnecessary re-render is a re-render whose necessity claim is unsupported. Findings are confirmed claims — not observations, not concerns.

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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA null-hypothesis terms + declaration throughout | |

---

**R14 criteria targeting summary:**

| Variation | C-43 | C-44 | C-45 | C-41 | C-42 | C-36 | Expected score |
|-----------|------|------|------|------|------|------|----------------|
| V-01 | entanglement in authored placeholder (Property C) | numbered enumeration in authored placeholder (Property B) | count declaration as leading phrase (Property A) | causal reasoning for all 3 properties | abstract reqs, no blank-slot | — | ~160–162/164 |
| V-02 | "Mutual dependency: neither independently satisfies the block" | (OBL-1)/(OBL-2) labeled items | "N=2 OBLIGATIONS" leading label | not targeted | not targeted | — | ~156–158/164 |
| V-03 | Phase Contract entanglement + close-line placeholder | Phase Contract items (1)/(2) + placeholder | Phase Contract "Two requirements" + placeholder opener | not targeted | not targeted | — | ~158–160/164 |
| V-04 | mutual-dependency declaration referencing OBL-1/OBL-2 (authored) | labeled OBL-1/OBL-2 items (authored from Question 2) | count label as block first element (authored from Question 1) | 3-question causal reasoning | abstract reqs, no blank-slot | — | ~160–164/164 |
| V-05 | mutual-dependency in authored DUAL-CONSTRAINT BLOCK + Phase Contract | OBL-1/OBL-2 in authored block + Phase Contract | count label in authored block + Phase Contract | 3 null-hypothesis questions + 3 placeholder property questions | blank authorship context + no reproduction | unified null-hypothesis epistemology | ~162–164/164 |

**Placeholder C-43/C-44/C-45 compliance map:**

| Variation | Placeholder form (manifest close-line slot) | C-45 (leading count)? | C-44 (numbered items)? | C-43 (entanglement)? |
|-----------|--------|------|------|------|
| V-01 | `*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction — verbatim... That instruction carries Property A (count), Property B (numbered), Property C (entanglement)...]*` | via authored instruction | via authored instruction | via authored instruction |
| V-02 | `*[DUAL-CONSTRAINT BLOCK \| N=2 OBLIGATIONS — (OBL-1) content: ...; (OBL-2) position: ... Mutual dependency: neither independently satisfies the block.]*` | "N=2 OBLIGATIONS" as leading label | (OBL-1)/(OBL-2) labeled items | "Mutual dependency: neither independently satisfies" |
| V-03 | Phase Contract: "Two requirements: (1)...(2)... Entanglement: neither alone..." + `*[Two requirements, one instruction — as declared in Phase Contract: (1) content...; (2) position... Neither satisfied without the other.]*` | "Two requirements, one instruction" | (1)/(2) items in Phase Contract + placeholder | "Entanglement" in Phase Contract + "Neither satisfied without the other" in placeholder |
| V-04 | `*[Apply your Area 3 DUAL-CONSTRAINT BLOCK — verbatim... count label, OBL-1 content, OBL-2 position, mutual-dependency declaration referencing both OBL labels...]*` | count label as authored first element | OBL-1/OBL-2 authored labeled items | mutual-dependency declaration referencing both OBL labels |
| V-05 | Phase Contract (authored) + `*[Reproduce Area 3 DUAL-CONSTRAINT BLOCK — count label, OBL-1 content source TRAVERSAL-SCHEMA close-line, OBL-2 positional, mutual-dependency declaration. Neither OBL alone satisfies the block.]*` | count label as authored first element | OBL-1/OBL-2 in authored block + Phase Contract | mutual-dependency in authored block + Phase Contract |
