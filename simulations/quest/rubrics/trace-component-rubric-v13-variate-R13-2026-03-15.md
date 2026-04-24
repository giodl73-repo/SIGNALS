# trace-component — Round 13 Variations

**Variation axes used:**
- Single-axis: Role sequence / C-42 target (V-01), Lifecycle emphasis / C-41 target (V-02), Phrasing register / C-40 target (V-03)
- Combined: Role sequence + Lifecycle emphasis / C-42 + C-41 + C-40 (V-04), All three axes / C-40 + C-41 + C-42 + C-36 (V-05)

**R13 context:** Three new criteria from R12 excellence signals:

- **C-40 (Dual-Constraint Position-and-Content Placeholder)** — The close-line placeholder at each manifest must enforce BOTH the content constraint (verbatim reproduction of the exact text declared in the schema artifact) AND the positional constraint (this placeholder is the manifest's last line) within a single instruction string. R12 V-04 and V-05 were the high-water marks: `*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*` and `*[Requirement C close-line — verbatim, last line of this manifest.]*` — both name content-source and position in one instruction. Single-constraint forms leave one failure mode open.

- **C-41 (Schema Causal Explanation Requirement)** — The schema's Requirement C (or equivalent) must ask the model to EXPLAIN WHY the close-line must occupy the manifest's closing position — not merely declare that it must. R12 V-05 was the prototype: "Explain why the marker must be the manifest's final line (not in a header annotation or document preamble) and what structural violation it produces if content appears after it." A model that has articulated the causal mechanism cannot violate the rule without contradicting its own stated reasoning.

- **C-42 (Anti-Reproduction Schema Authorship)** — The schema slot must be blank with an explicit prohibition against reproducing instruction text. R12 V-02 introduced "Author this document now — do not reproduce instruction text." C-42 strengthens C-39: where C-39 requires model authorship by instruction, C-42 requires it by structure — blank slot + anti-copy directive — so the schema cannot be satisfied by transcription or paraphrase.

**C-40 / C-41 / C-42 orthogonality:**
- C-40 can pass without C-41 (dual-constraint placeholder, no causal explanation in schema)
- C-41 can pass without C-42 (causal explanation required, but schema slot has labeled requirements that could be paraphrased)
- C-42 can pass without C-41 (blank-slot authorship, but Requirement C does not ask for causal reasoning)
- Full enforcement requires all three

**R13 hypothesis for each variation:**
- V-01: C-42 pure form — abstract functional requirements (non-copyable language) + blank slot + strong anti-copy. C-41 not targeted. Tests whether removing copyable requirement language produces stronger authorship compliance.
- V-02: C-41 pure form — Requirement C explicitly demands causal explanation of the enforcement mechanism before close-line declaration. Standard labeled requirements (no blank-slot anti-copy). Tests whether causal-reasoning mandate in isolation elevates constraint compliance.
- V-03: C-40 pure form — no schema architect role; close-line declared in prompt charter; placeholder uses maximally explicit procedural dual-constraint phrasing. Tests whether phrasing register of the placeholder drives C-40 compliance independent of schema authorship.
- V-04: C-42 + C-41 + C-40 combined — abstract requirements (C-42) + Requirement 3 causal explanation (C-41) + dual-constraint placeholders (C-40). Three criteria targeted via single causal chain: blank-slot authorship produces schema, schema contains causal reasoning, manifests close with dual-constraint placeholders referencing authored schema.
- V-05: All three + null-hypothesis inertia — V-04 plus C-36 integration. The null-hypothesis principle governs BOTH Direction cells (inertia as default) AND post-manifest positions (empty as default). Area 3 asks the model to explain structural parallelism between these two instances of the same principle. Maximum R13 coverage.

---

## V-01 · Role Sequence — Abstract-Requirements Blank-Slot Authorship (C-42 Target)

**Axis**: Role sequence
**Hypothesis**: R12 V-02 was the strongest C-39/C-42 prototype, but its Requirements A–D described schema content areas in named, prescriptive terms ("Specify the default value of the Direction column... List the active departure codes...") that could be paraphrased into a schema. V-01 replaces labeled requirements with abstract questions — "What does a Direction cell's default state mean?" — that describe the information need without providing copyable rule language. The schema slot is blank with a strong anti-reproduction instruction. Dual-constraint placeholders (C-40) are used at each manifest close. Causal explanation (C-41) is not asked — V-01 isolates C-42. Expected score: ~154–156/158 (C-42 pass, C-41 gap).

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are designing the governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact in your output that a reader can reference to verify the trace that follows.

Your TRAVERSAL-SCHEMA must answer these four questions. Author every answer in your own words. Do not reproduce any language from this prompt — not in paraphrase, not reformatted, not as rule text derived from the instructions below.

1. What framework, state management library, and component model are being traced?
2. For the traversal table's Direction column: what does a cell mean when it carries no departure code? What non-default codes are available, and what does each one assert about the hop's behavior?
3. How does each MANIFEST-N block close? What is the exact text that appears as the manifest's final line? Why does placing that text at the manifest's last position — rather than in the manifest's opening line or a document preamble — make any violation of the MANIFEST-N / TABLE-N adjacency guarantee structurally visible at point-of-production?
4. What tables will this trace produce? List each by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author this schema now. Do not reproduce any language from this prompt — not even
 in paraphrase. Every principle must be in your own words, derived from your
 understanding of the tracing task. Question 3 must name the close-line text.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and question 3 declares the close-line text.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored above. Any rule you declared is binding on this output. Violating it contradicts your own prior production.

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
*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*

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
*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*

**TABLE-2 · Component Tree Traversal**

Apply the Direction default and departure codes you declared in question 2 of your TRAVERSAL-SCHEMA.

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
*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*

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
*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*

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
*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*

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

## V-02 · Lifecycle Emphasis — Schema Causal Explanation Requirement (C-41 Target)

**Axis**: Lifecycle emphasis
**Hypothesis**: R12 V-05 was the closest C-41 prototype — its Requirement C asked the model to "explain why the marker must be the manifest's final line and what structural violation it produces if content appears after it." V-02 isolates and deepens this mechanism: Requirement C is split into two steps — (a) answer three causal questions in sequence, then (b) declare the close-line text. The causal questions force the model to articulate the full enforcement chain before committing to the close-line text. A model that has answered "what prior output does inserting content after the close-line contradict?" cannot then insert content after it without self-contradiction at the reasoning level. Standard labeled requirements are used (not abstract); no anti-copy directive — clean C-41 isolation. Dual-constraint placeholders (C-40) present at each manifest close. Expected score: ~152–156/158 (C-41 pass, C-42 gap).

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are a schema architect. Produce a TRAVERSAL-SCHEMA artifact — a named document that governs the trace in Role 2. A reader must be able to reference this artifact to verify Role 2's compliance.

**Requirement A — Framework context**: Identify the framework, state management library, and component model.

**Requirement B — Direction default contract**: Specify the default value of the traversal table's Direction column. Explain what it means when no departure code is declared for a hop. List all active departure codes and define when each applies.

**Requirement C — Manifest-to-table adjacency rule**: Before declaring the close-line text, answer these three questions in sequence:
- Why does the adjacency prohibition need to occupy the manifest's closing position — rather than the manifest's opening annotation, the table's opening header, or a document-level preamble? What is different about the closing position that makes it structurally effective?
- If a model inserts content between the close-line and the table header, what prior output does that insertion contradict?
- Why does this make non-compliance structurally visible at point-of-production — without requiring a post-hoc auditor to check the document structure?

Having answered these three questions, declare the exact text of the close-line marker that will appear as the final line of every manifest block in this trace.

**Requirement D — Table inventory**: List every table this trace will produce by name and purpose, including the Criteria Audit table.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Address Requirements A through D.
 For Requirement C: write the three mechanism answers before declaring the close-line text.
 The close-line you declare will appear verbatim at the end of each manifest in Role 2.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Requirement C contains both the mechanism reasoning and the declared close-line text.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored above. You answered in Requirement C why the close-line must be the manifest's final position. Apply that reasoning: end every manifest with the close-line you declared — verbatim, as the manifest's last content line. You stated what inserting content after it would contradict. That statement is now part of your output.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[from your TRAVERSAL-SCHEMA]` |
| State management | `[from your TRAVERSAL-SCHEMA]` |
| Component model | `[from your TRAVERSAL-SCHEMA]` |

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*

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
*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Requirement B: apply the Direction default you declared and the departure codes you specified.

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
*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*

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
*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*

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
*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*

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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA declaration + terms throughout | |

---

## V-03 · Phrasing Register — Procedural Dual-Constraint Placeholder (C-40 Target)

**Axis**: Phrasing register
**Hypothesis**: R12's dual-constraint placeholders used compact abbreviation: "verbatim, as this manifest's last line." V-03 tests whether a procedurally-enumerated form — where both constraints are explicitly numbered within the placeholder and the instruction states they cannot be satisfied independently — produces stronger C-40 compliance. No schema architect role (C-39 not targeted; close-line declared in prompt charter). The variation axis is the placeholder phrasing alone. If V-03 scores well on C-40, it confirms the dual-constraint form is the mechanism, not the schema-authorship scaffolding. C-41, C-42 not targeted; expected C-39 fail. Expected score: ~146–150/158.

---

You are a frontend domain expert. Identify the framework and state management library from the provided code or topic description before proceeding.

---

**TRACE CHARTER**

This trace is governed by the following structural rules.

**Direction schema**: Every traversal hop begins as `<-> inert` — the default, requiring no justification. Active departure codes replace the default only when the hop is demonstrably active:
- `prop-pass` — downward prop transmission
- `event-propagate` — upward event propagation
- `dispatch` — store dispatch
- `effect-trigger` — side effect activation
- `context-provide` — context provision or update

**Manifest close-line** (apply verbatim at the close of every manifest block):
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
*[Two requirements, one instruction: (1) content — reproduce the TRACE CHARTER's manifest close-line text exactly, word for word, with no alteration; (2) position — this reproduction is the absolute last line of this manifest block, TABLE-1 header follows directly. Neither constraint is satisfied without the other. Write the close-line now.]*

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
*[Two requirements, one instruction: (1) content — reproduce the TRACE CHARTER's manifest close-line text exactly, word for word, with no alteration; (2) position — this reproduction is the absolute last line of this manifest block, TABLE-2 header follows directly. Neither constraint is satisfied without the other. Write the close-line now.]*

**TABLE-2 · Component Tree Traversal**

Direction default: `<-> inert`. Active departure codes replace the default per the TRACE CHARTER. A departure code without supporting Role evidence is an unsupported claim.

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
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Two requirements, one instruction: (1) content — reproduce the TRACE CHARTER's manifest close-line text exactly, word for word, with no alteration; (2) position — this reproduction is the absolute last line of this manifest block, TABLE-3 header follows directly. Neither constraint is satisfied without the other. Write the close-line now.]*

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
*[Two requirements, one instruction: (1) content — reproduce the TRACE CHARTER's manifest close-line text exactly, word for word, with no alteration; (2) position — this reproduction is the absolute last line of this manifest block, TABLE-4 header follows directly. Neither constraint is satisfied without the other. Write the close-line now.]*

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
*[Two requirements, one instruction: (1) content — reproduce the TRACE CHARTER's manifest close-line text exactly, word for word, with no alteration; (2) position — this reproduction is the absolute last line of this manifest block, TABLE-5 header follows directly. Neither constraint is satisfied without the other. Write the close-line now.]*

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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRACE CHARTER direction schema + terms throughout | |

---

## V-04 · Combined: Role Sequence + Lifecycle Emphasis (C-42 + C-41 + C-40)

**Axis**: Role sequence + Lifecycle emphasis (combined)
**Hypothesis**: V-01 targets C-42 (abstract requirements + blank slot + anti-copy). V-02 targets C-41 (causal explanation in Requirement C). V-04 combines them via a single structural chain: the schema architect role receives abstract questions (C-42) where Requirement 3 is itself a two-part instruction — first answer the causal mechanism questions, then declare the close-line (C-41). Because the requirements are non-copyable and the slot is blank with anti-copy, C-42 is structurally enforced. Because Requirement 3 demands causal reasoning before the declaration, C-41 is enforced at authorship time. Manifests close with dual-constraint placeholders that name the authored schema as content source (C-40). All three criteria targeted. Expected score: ~154–158/158.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are designing the governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact in your output that a reader can reference to verify the trace that follows.

Your TRAVERSAL-SCHEMA must address these four areas. Author every rule in your own words. Do not reproduce any language from this prompt — not in paraphrase, not reformatted, not as rule text derived from the instructions below.

**Area 1 — Framework context**: What framework, state management library, and component model are being traced?

**Area 2 — Direction default contract**: What does a Direction cell mean when it carries no departure code? What non-default codes are available, and what does each assert about the hop?

**Area 3 — Manifest adjacency mechanism**: Answer these questions in sequence, then declare the close-line text:
- Why must the adjacency prohibition occupy the manifest's closing position rather than its opening position or a document preamble? What property of the closing position enables structural enforcement?
- What does a model contradict if it inserts content between the close-line and the table header?
- Why does this make non-compliance visible at point-of-production — without requiring a post-hoc audit?

Having answered these three questions, declare the exact text of the close-line marker that will appear as the final line of every manifest block in this trace.

**Area 4 — Table inventory**: List every table by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author this schema now. Do not reproduce any language from this prompt — not even
 in paraphrase. Every rule must derive from your own reasoning. For Area 3: write
 the mechanism answers before declaring the close-line text.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the mechanism reasoning, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored. Apply the Direction semantics from Area 2. End every manifest with the Area 3 close-line — verbatim, as the manifest's last line. You stated in Area 3 what inserting content after it contradicts. That reasoning is part of your output. Violating the close-line rule contradicts both your stated reasoning and your structural prior output.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[from your TRAVERSAL-SCHEMA Area 1]` |
| State management | `[from your TRAVERSAL-SCHEMA Area 1]` |
| Component model | `[from your TRAVERSAL-SCHEMA Area 1]` |

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Your TRAVERSAL-SCHEMA Area 3 close-line — verbatim, as the last line of this manifest.]*

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
*[Your TRAVERSAL-SCHEMA Area 3 close-line — verbatim, as the last line of this manifest.]*

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
*[Your TRAVERSAL-SCHEMA Area 3 close-line — verbatim, as the last line of this manifest.]*

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
*[Your TRAVERSAL-SCHEMA Area 3 close-line — verbatim, as the last line of this manifest.]*

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
*[Your TRAVERSAL-SCHEMA Area 3 close-line — verbatim, as the last line of this manifest.]*

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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA declaration + terms throughout | |

---

## V-05 · Combined: All Three Axes + Null-Hypothesis Inertia (C-40 + C-41 + C-42 + C-36)

**Axis**: Role sequence + Lifecycle emphasis + Phrasing register (combined)
**Hypothesis**: V-04 combines C-40 + C-41 + C-42 via schema authorship with causal explanation and dual-constraint placeholders. V-05 adds C-36 integration via structural unification: the null-hypothesis principle governs BOTH traversal hop Direction cells (inertia as default) AND post-manifest positions (empty as default). Area 3 asks the model to explain how the close-line mechanism is structurally parallel to the inertia-as-null rule — both are instances of the same epistemological principle. This creates a single causal framework governing two enforcement mechanisms simultaneously; the model cannot violate either without contradicting the unified principle it authored. Procedural dual-constraint placeholders (V-03 phrasing register) are used to maximize C-40 clarity. Expected score: ~156–158/158.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are designing the epistemological framework and governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact in your output that a reader can reference to verify the trace that follows.

The schema must be authored in your own words from a blank context. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting instruction text into a schema format. Every principle must derive from your reasoning about the tracing task.

Address these four areas:

**Area 1 — Framework context**: State the framework, state management library, and component model.

**Area 2 — Inertia as epistemic null**: Answer: What is the epistemic status of a traversal hop before any evidence is applied — what must be proved, and by whom? Why is inertia the default state rather than a special case requiring documentation? What does it mean to claim activity at a hop, and why does that claim require supporting evidence while the null requires none? How does this principle manifest in the Direction column's default value and in the requirement to document inert hops explicitly rather than omit them?

**Area 3 — Manifest adjacency as null-hypothesis extension**: The principle from Area 2 governs traversal hops. It also governs the structural space between a manifest block and its analysis table. Answer these questions in sequence, then declare the close-line text:
- What is the null (default) state of the position between a manifest's final content line and its analysis table's header?
- What claim does a model make by inserting content into that position?
- Why does placing a prohibition marker at the manifest's last position — rather than in the manifest's opening annotation or a document preamble — make that claim structurally self-contradictory at point-of-production?
- In what sense is this structurally parallel to the inert-hop rule from Area 2?

Having answered these questions, declare the exact text of the close-line marker that will appear as the final line of every manifest block in this trace.

**Area 4 — Table inventory**: List every table by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author this schema now. Do not reproduce any language from this prompt — not in
 any form. Areas 1 through 4 addressed in full. For Area 2: author the inertia
 principle from your reasoning, not from instructions. For Area 3: write the
 mechanism answers and structural parallel before declaring the close-line text.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 2 articulates the null-hypothesis principle, Area 3 contains the adjacency mechanism reasoning with the structural parallel to Area 2, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored. Apply the null-hypothesis epistemology from Area 2: every Direction cell defaults to the inert null; departure codes are active claims requiring evidence. Apply the adjacency guarantee from Area 3: end every manifest with the close-line you declared — verbatim, as the manifest's last content line. You explained the causal mechanism and the structural parallel for both principles. Violating either contradicts your authored reasoning.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[from your TRAVERSAL-SCHEMA Area 1]` |
| State management | `[from your TRAVERSAL-SCHEMA Area 1]` |
| Component model | `[from your TRAVERSAL-SCHEMA Area 1]` |

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Two simultaneous constraints — one instruction: (1) content — reproduce the TRAVERSAL-SCHEMA Area 3 close-line text exactly, word for word; (2) position — this line is the final content of MANIFEST-1, TABLE-1 header follows directly. Neither constraint is satisfied without the other. Write the close-line now as this manifest's last line.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops — null-hypothesis applies; include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Two simultaneous constraints — one instruction: (1) content — reproduce the TRAVERSAL-SCHEMA Area 3 close-line text exactly, word for word; (2) position — this line is the final content of MANIFEST-2, TABLE-2 header follows directly. Neither constraint is satisfied without the other. Write the close-line now as this manifest's last line.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null-hypothesis Direction default. Every departure code is an active claim requiring evidence in the Role column. An undocumented inert hop is a confirmed null, not an omission.

| Step | T-ID | Component | Direction [null: your declared default \| active claim: your declared departure codes] | Role [Null confirmed: reason / Active claim: departure + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
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
*[Two simultaneous constraints — one instruction: (1) content — reproduce the TRAVERSAL-SCHEMA Area 3 close-line text exactly, word for word; (2) position — this line is the final content of MANIFEST-3, TABLE-3 header follows directly. Neither constraint is satisfied without the other. Write the close-line now as this manifest's last line.]*

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
*[Two simultaneous constraints — one instruction: (1) content — reproduce the TRAVERSAL-SCHEMA Area 3 close-line text exactly, word for word; (2) position — this line is the final content of MANIFEST-4, TABLE-4 header follows directly. Neither constraint is satisfied without the other. Write the close-line now as this manifest's last line.]*

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
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Two simultaneous constraints — one instruction: (1) content — reproduce the TRAVERSAL-SCHEMA Area 3 close-line text exactly, word for word; (2) position — this line is the final content of MANIFEST-5, TABLE-5 header follows directly. Neither constraint is satisfied without the other. Write the close-line now as this manifest's last line.]*

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
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA null-hypothesis terms + declaration throughout | |

---

**R13 criteria targeting summary:**

| Variation | C-40 | C-41 | C-42 | C-36 | Expected score |
|-----------|------|------|------|------|----------------|
| V-01 | dual-constraint placeholder | not targeted | primary target (abstract reqs + blank + anti-copy) | — | ~154–156/158 |
| V-02 | dual-constraint placeholder | primary target (3-question causal chain) | not targeted | — | ~152–156/158 |
| V-03 | primary target (procedural enumerated form) | not targeted | not targeted | — | ~146–150/158 |
| V-04 | dual-constraint placeholder | causal 3-question + reasoning-bound reminder | abstract reqs + blank + anti-copy | — | ~154–158/158 |
| V-05 | procedural dual-constraint | causal chain + structural parallel | abstract reqs + blank + anti-copy | unified null-hypothesis epistemology | ~156–158/158 |

**Placeholder C-40 compliance map (content source + position in one instruction):**

| Variation | Placeholder form | Content-source named? | Position named? | Single instruction? |
|-----------|-----------------|----------------------|-----------------|---------------------|
| V-01 | `*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*` | yes (TRAVERSAL-SCHEMA question-3) | yes (last line of this manifest) | yes |
| V-02 | `*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*` | yes (TRAVERSAL-SCHEMA Requirement C) | yes (manifest's last line) | yes |
| V-03 | `*[Two requirements, one instruction: (1) content — reproduce TRACE CHARTER's close-line exactly; (2) position — absolute last line of this manifest block. Neither constraint is satisfied without the other.]*` | yes (TRACE CHARTER) | yes (absolute last line) | yes (stated explicitly) |
| V-04 | `*[Your TRAVERSAL-SCHEMA Area 3 close-line — verbatim, as the last line of this manifest.]*` | yes (TRAVERSAL-SCHEMA Area 3) | yes (last line of this manifest) | yes |
| V-05 | `*[Two simultaneous constraints — one instruction: (1) content — reproduce TRAVERSAL-SCHEMA Area 3 close-line exactly; (2) position — final content of MANIFEST-N, TABLE-N follows directly. Neither satisfied without the other.]*` | yes (TRAVERSAL-SCHEMA Area 3) | yes (final content of MANIFEST-N) | yes (stated explicitly) |
