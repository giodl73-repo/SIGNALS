# trace-component — R18 Variations (v18 rubric)

**Round**: 18
**Rubric ceiling**: 188 pts (C-01 through C-57)
**New criteria targeted**: C-55 (header-form causal questions), C-56 (schema-declared compound header template), C-57 (exemplar-grounded compound header template in schema)

**R17 baseline summary:**
- V-01/V-04: NHQ-1/NHQ-2 questions (C-55 ✓) + schema Area 3 declares template (C-56 ✓) but no worked exemplar (C-57 ✗). Ceiling ~178-180/182.
- V-05: NHQ-1/NHQ-2 + schema Area 3b with exemplar (C-55 ✓, C-56 ✓, C-57 ✓). Ceiling ~180-182/182.
- V-02: NCQ questions only -- close-marker form, not header form (C-55 ✗, C-56 ✗, C-57 ✗). ~175-178/182.
- V-03: No NHQ or NCQ questions (C-55 ✗, C-56 ✗, C-57 ✗). ~173-176/182.

**R18 variation axes chosen (3 single-axis + 2 combined):**
1. Role sequence -- what question types appear in the causal phase
2. Output format -- how Schema Area 3 is structured (prose vs table)
3. Lifecycle emphasis -- close-marker questions only (no header-form questions)
4. Role sequence + Output format (combined)
5. All axes + Inertia framing

---

## V-01 · Role Sequence -- NHQ Exemplar-Derivation Question (Single Axis)

**Axis**: Role sequence
**Hypothesis**: R17 V-01 achieved C-55 (NHQ-1/NHQ-2) and C-56 (schema template) but missed C-57 (no exemplar). The minimal addition is NHQ-3 -- an exemplar-derivation question requiring the model to produce one concrete worked compound header line in the causal phase before schema authorship. Schema Area 3 then references NHQ-3 by instruction: "Include the example you authored in NHQ-3 as your first exemplar." The exemplar is a prior cognitive production, not an instruction-following addition. Tests whether exemplar derivation in the causal phase + schema forward-reference achieves C-57 with minimum structural change to V-01. Expected: C-55 ✓, C-56 ✓, C-57 ✓; ~185-186/188.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 -- SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE -- reasoning only.

---

### CAUSAL PHASE -- Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace -- positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. A register section in a structured document can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does a reader have after encountering the compound form that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A document element must both identify itself and characterize its epistemic function. When these two declarations occupy the same parseable header line, what property does that line have that neither the identity claim nor the function claim carries alone? What is the reader's epistemic position after reading the compound header that would require two separate reads to achieve without it?

NHQ-3. Name one register you will use in your CAUSAL PHASE -- not a hypothetical -- and write its complete compound header line in the form `**[LABEL]** -- [epistemic-function descriptor]`. The descriptor must characterize the cognitive work performed in the register, not the topic of its questions. After writing the line, state in one sentence why your descriptor characterizes cognitive work rather than content.

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell -- what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied -- without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above -- NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE -- Schema Authorship

Produce the TRAVERSAL-SCHEMA -- a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt -- not in paraphrase, not by reformatting question text into schema format.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Manifest adjacency and register header format:
           Derive from NQ-3, NHQ-1, NHQ-2, NHQ-3, and DQ-2 through DQ-5.
           First write the structural rationale for the close-line mechanism (NQ-3, DQ-2).
           Then write the structural rationale for the dual-constraint form (DQ-3 through DQ-5).
           Then write the complete close-line placeholder instruction text.
           The placeholder must: open with an obligation count (from DQ-5), enumerate
           both constraints as labeled independent items (from DQ-3), include an
           entanglement declaration that neither alone satisfies the dual requirement
           (from DQ-4), and name the terminal positional claim and the successor artifact.
           Then declare the exact close-line text the placeholder will reproduce.
           Then write the register header format rationale (NHQ-1, NHQ-2).
           Then declare the compound header template: **[LABEL]** -- [epistemic-function descriptor].
           Then include the worked example you authored in NHQ-3 as your first exemplar.
           Then add at least one additional compound header example using a different register.

 Area 4 -- Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3 declares the close-line placeholder, close-line text, register header template, and at least two worked compound header examples (one from NHQ-3, one additional).

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction from Area 3 -- verbatim, naming the successor table. You derived the compound register header template from NHQ-1 and NHQ-2 and demonstrated it in NHQ-3; your TRAVERSAL-SCHEMA Area 3 declares the format and records the worked examples -- apply that standard to every named register you author. Satisfying only one of the two placeholder requirements does not satisfy it -- you articulated why in DQ-3 and DQ-4.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed -- basis / Departure -- evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory -- present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops -- all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct -- state writes the event handler or synchronous code produces immediately.
- Inherited -- transitive state writes via useEffect, watch, computed cascades, middleware, subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none -- no effects, subscriptions, or watchers triggered.
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear -- including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes -- reason / No -- reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes -- [reason] / No -- [reason] | *(UR-ID or "--")* |

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | -- | No API calls, timers, subscriptions, or navigation triggered. | -- | -- |`

---

**TABLE-6 · Final UI State -- Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit -- C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-02 · Output Format -- Schema Area 3 as Boundary Table (Single Axis)

**Axis**: Output format
**Hypothesis**: R17 V-01 declared the compound header template in Area 3 as free-form prose; the model could write a template without an exemplar and the Area 3 instruction structure offered no blank-blocked field forcing an example. Replacing Area 3 prose with a table format -- columns: Boundary Type | Template Pattern | Worked Example | Enforcement Rationale -- makes the "Worked Example" cell blank-blocked. A model filling this table cannot omit the exemplar without leaving a structural gap. NHQ-1/NHQ-2 remain in the causal phase (C-55 ✓). Schema Area 3 as a table row for compound-header template is a schema field (C-56 ✓). The "Worked Example" column enforces C-57 structurally. Tests whether format-level enforcement -- cell that cannot be blank -- achieves C-57 more reliably than prose instruction. Expected: C-55 ✓, C-56 ✓, C-57 ✓; ~185-186/188.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 -- SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE -- reasoning only.

---

### CAUSAL PHASE -- Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace -- positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. A register section in a structured document can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does a reader have after encountering the compound form that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A document element must both identify itself and characterize its epistemic function. When these two declarations occupy the same parseable header line, what property does that line have that neither the identity claim nor the function claim carries alone? What is the reader's epistemic position after reading the compound header that would require two separate reads to achieve without it?

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell -- what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied -- without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above -- NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE -- Schema Authorship

Produce the TRAVERSAL-SCHEMA -- a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Structural boundary declarations.
           Derive from NQ-3, NHQ-1, NHQ-2, and DQ-2 through DQ-5.
           Author the rationale for close-line enforcement (NQ-3, DQ-2).
           Author the rationale for dual-constraint form (DQ-3 through DQ-5).
           Then produce the boundary template table below:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [author from DQ-5/DQ-3/DQ-4 -- two-sentence dual assertion] | [write one complete manifest close-line] | [why dual-sentence form; derive from DQ-3] |
           | Register header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line -- label and descriptor] | [why compound form; derive from NHQ-1 and NHQ-2] |

           No cell in this table may be blank. Worked Example cells require a concrete complete
           line, not a placeholder pattern. Enforcement Rationale cells require a reason derived
           from your CAUSAL PHASE answers, not a restatement of the template.

 Area 4 -- Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3's boundary table has all cells populated (no blank Worked Example cells, no blank Enforcement Rationale cells).

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the dual-assertion close-line form from the boundary table you authored in Area 3 -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2; your boundary table's Worked Example cell demonstrates the standard -- match it in every register header you author. Satisfying only one of the two close-line assertions does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4.

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
*[Apply the manifest close-line form from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming the successor table.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the manifest close-line form from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming the successor table.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without departure evidence carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed -- basis / Departure -- evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops -- all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the manifest close-line form from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming the successor table.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct -- state writes the event handler or synchronous code produces immediately.
- Inherited -- transitive state writes via useEffect, watch, computed cascades, middleware, subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none -- no effects, subscriptions, or watchers triggered.
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
*[Apply the manifest close-line form from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming the successor table.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear -- including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes -- reason / No -- reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes -- [reason] / No -- [reason] | *(UR-ID or "--")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Apply the manifest close-line form from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming the successor table.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | -- | No API calls, timers, subscriptions, or navigation triggered. | -- | -- |`

---

**TABLE-6 · Final UI State -- Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit -- C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-03 · Lifecycle Emphasis -- Close-Marker Questions Only, No Header-Form Questions (Single Axis)

**Axis**: Lifecycle emphasis (how much space per phase, how explicit the phase boundaries are)
**Hypothesis**: A causal phase that emphasizes register close-marker reasoning (NCQ questions -- what the compound close accomplishes that the bare close does not) but omits NHQ questions (header-form causal grounding) cannot achieve C-55, even if schema Area 3 declares a compound header template. C-55 requires questions specifically about why the register section *header* requires co-declaration of label identity and epistemic-function descriptor -- NCQ questions are a different epistemic target (they probe the closing artifact, not the opening artifact). Schema Area 3 is authored from the model's NCQ reasoning, so it derives compound close form but not compound header form. Tests whether NCQ-only causal emphasis + header template in schema (without causal grounding of the header) achieves C-55 and C-56. Expected: C-55 ✗ (NCQ not NHQ), C-56 ✗ (schema derives close template but not header template), C-57 ✗; ~177-180/188.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 -- SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE -- reasoning only.

---

### CAUSAL PHASE -- Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER**

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace -- positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NCQ-1. A named register in a structured document ends. Two close marker forms are possible: (a) a bare named close -- `**NULL REGISTER CLOSE**` -- and (b) a compound close -- `**NULL REGISTER CLOSE** -- Null baseline established`. What does the reader know at the compound close that cannot be derived from the bare close alone? Why is the bare close a boundary position marker but not a closure-assertion marker?

NCQ-2. A register close marker should simultaneously name what terminates and characterize what that termination establishes. When both appear in a single compound line, what structural property does the document boundary gain that it lacks when the close marker is positional only? What reasoning would a reader have to perform externally without the compound close that the compound form performs internally?

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER**

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell -- what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied -- without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above -- NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE -- Schema Authorship

Produce the TRAVERSAL-SCHEMA -- a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Manifest adjacency and register close format:
           Derive from NQ-3, NCQ-1, NCQ-2, and DQ-2 through DQ-5.
           First write the structural rationale for the close-line mechanism (NQ-3, DQ-2).
           Then write the structural rationale for the dual-constraint form (DQ-3 through DQ-5).
           Then write the complete close-line placeholder instruction text.
           The placeholder must: open with an obligation count (from DQ-5), enumerate
           both constraints as labeled independent items (from DQ-3), include an
           entanglement declaration that neither alone satisfies the dual requirement
           (from DQ-4), and name the terminal positional claim and the successor artifact.
           Then declare the exact close-line text the placeholder will reproduce.
           Then write the register close format rationale (NCQ-1, NCQ-2).
           Then declare the compound close template: **[LABEL] CLOSE** -- [accomplishment descriptor].

 Area 4 -- Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3 contains the close-line placeholder, close-line text, and register close template.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction from Area 3 -- verbatim, naming the successor table. You derived the compound register close template from NCQ-1 and NCQ-2; your TRAVERSAL-SCHEMA Area 3 declares the format -- apply it to every named register close you author. Satisfying only one of the two placeholder requirements does not satisfy it -- you articulated why in DQ-3 and DQ-4.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed -- basis / Departure -- evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops -- all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none -- no effects, subscriptions, or watchers triggered.
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes -- reason / No -- reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes -- [reason] / No -- [reason] | *(UR-ID or "--")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | -- | No API calls, timers, subscriptions, or navigation triggered. | -- | -- |`

---

**TABLE-6 · Final UI State -- Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit -- C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-04 · Role Sequence + Output Format -- NHQ Exemplar Derivation + Boundary Table (Two Axes)

**Axes**: Role sequence + Output format
**Hypothesis**: V-01 adds NHQ-3 (exemplar-derivation question) to the causal phase and forwards the produced example into Schema Area 3. V-02 replaces Schema Area 3 prose with a boundary table that blank-blocks the Worked Example cell. V-04 combines both: NHQ-3 in the causal phase (role sequence axis) AND Schema Area 3 as a boundary table with an Example cell that the prompt explicitly binds to the NHQ-3 production (output format axis). The combined structure creates two independent enforcement paths to C-57: the causal phase produces the exemplar via NHQ-3, and the schema table requires that production to populate a blank-blocked cell. If either path alone were insufficient, the combination should close the gap. Tests whether the dual-path structure achieves more reliable C-57 compliance than either axis alone. Expected: C-55 ✓, C-56 ✓, C-57 ✓; ~186-188/188.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 -- SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE -- reasoning only.

---

### CAUSAL PHASE -- Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace -- positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. A register section in a structured document can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does a reader have after encountering the compound form that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A document element must both identify itself and characterize its epistemic function. When these two declarations occupy the same parseable header line, what property does that line have that neither the identity claim nor the function claim carries alone? What is the reader's epistemic position after reading the compound header that would require two separate reads to achieve without it?

NHQ-3. Name one register you will use in your CAUSAL PHASE -- a real register from this trace, not a hypothetical -- and write its complete compound header line in the form `**[LABEL]** -- [epistemic-function descriptor]`. The descriptor must characterize the cognitive work performed (what kind of reasoning the register contains), not the topic or the sequence of the questions. After writing the line, state in one sentence why your descriptor names cognitive work rather than content or position.

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell -- what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied -- without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above -- NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE -- Schema Authorship

Produce the TRAVERSAL-SCHEMA -- a named artifact a reader can reference to verify the trace that follows. Author in your own words from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Structural boundary declarations.
           Author the rationale for the close-line mechanism (NQ-3, DQ-2).
           Author the rationale for the dual-constraint placeholder form (DQ-3 through DQ-5).
           Author the rationale for the compound register header form (NHQ-1, NHQ-2).
           Then produce the boundary declaration table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [Two-req dual-assertion form: obligation count + two independent items + entanglement + position + successor] | [One complete manifest close-line verbatim, for MANIFEST-N / TABLE-N of your choice] | [Derive from DQ-3 and DQ-4 why dual requirement] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [Paste here the compound header line you authored in NHQ-3] | [Derive from NHQ-1 and NHQ-2 why compound form] |

           No cell in this table may be blank.
           The Register section header Worked Example cell must contain the NHQ-3 line verbatim.
           Enforcement Rationale cells must derive from your CAUSAL PHASE answers, not restate the template.

 Area 4 -- Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 boundary table has all cells populated including the NHQ-3 exemplar in the Register section header row.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: reproduce the manifest close-line form from your Area 3 boundary table -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2 and demonstrated it in NHQ-3; your boundary table's Worked Example cell contains the exemplar standard -- all register headers in this trace must match that standard. Satisfying only one of the two close-line assertions does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4.

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming TABLE-1 as successor.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming TABLE-2 as successor.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default derived from NQ-1.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed -- basis / Departure -- evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops -- all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming TABLE-3 as successor.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none
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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming TABLE-4 as successor.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes -- reason / No -- reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes -- [reason] / No -- [reason] | *(UR-ID or "--")* |

**PROMOTION BLOCK (mandatory):**
```
Unnecessary re-renders: ___
UR-IDs requiring findings entry: ___
```

[GATE-4: TABLE-4 does not close on omitting any TABLE-2 T-ID, blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary table -- verbatim, as this manifest's terminal line, naming TABLE-5 as successor.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | -- | No API calls, timers, subscriptions, or navigation triggered. | -- | -- |`

---

**TABLE-6 · Final UI State -- Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or fewer than four distinct phase rows.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit -- C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-05 · All Axes -- Inertia Framing + Full Stack (All Axes Combined)

**Axes**: Role sequence + Output format + Lifecycle emphasis + Phrasing register + Inertia framing
**Hypothesis**: Every structural boundary in a trace document is a departure from a default state. The inertia framing axis makes this principle explicit in every element: NHQ questions name the bare-label competitor and ask what is lost by staying with it; schema Area 3b includes a failure-mode exemplar alongside the passing exemplar (`WRONG: **NULL REGISTER** (bare label only) -- no epistemic function declared / CORRECT: **NULL REGISTER** -- Epistemic status of null cases`); the phrasing register throughout emphasizes that compound form is not decoration but a departure from epistemic inertia. NCQ questions (close form) and NHQ questions (header form) and DSQ questions (two-sentence manifest form) all run together. Schema Area 3 derives all three boundary templates (3a manifest close, 3b register header with passing + failing exemplars, 3c register close). The unifying principle is stated in the schema and applied in Role 2. Tests maximum C-55/C-56/C-57 enforcement via inertia framing + failure-mode exemplar + full causal stack. Expected: C-55 ✓, C-56 ✓, C-57 ✓; ~187-188/188.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 -- SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE -- reasoning only.

---

### CAUSAL PHASE -- Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Each register is a distinct epistemic workspace -- its opening header declares what reasoning occurs within it; its close marker declares what that reasoning established. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace -- positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. Consider two forms of register section header: (a) `**NULL REGISTER**` -- a bare bold label -- and (b) `**NULL REGISTER** -- Epistemic status of null cases` -- a compound label. A reader who encounters (a) knows the register has started. A reader who encounters (b) knows the register has started AND knows the epistemic purpose of the work within it. What is the reader's epistemic position at (b) that is structurally inaccessible at (a)? What must the reader do externally -- reading beyond the header -- to arrive at the same position from (a)?

NHQ-2. Every structural boundary in a trace document represents a departure from a default condition. The default for an unidentified boundary is inertia: it marks position only. The compound header form departs from this inertia by adding an epistemic-function declaration. Name the epistemic state of a register whose header is `**NULL REGISTER**` only: what does a reader know, what does the reader not know, and what work is deferred to the register's content? Now name the epistemic state of a register whose header is `**NULL REGISTER** -- Epistemic status of null cases`: what work is completed before the first question is read? What is the cognitive cost eliminated by the compound form?

NHQ-3. You have now reasoned about why compound register headers exceed bare labels (NHQ-1 and NHQ-2). Write one concrete compound header line for the DEPARTURE REGISTER you will use in this trace. The form is `**[LABEL]** -- [epistemic-function descriptor]`. The descriptor must characterize the cognitive work performed in that register -- the kind of epistemic or logical reasoning that occurs there -- not the topic of the questions, not the sequential position, not generic analytical vocabulary. After writing the line, state in one sentence why your descriptor names cognitive work rather than content or sequence.

NCQ-1. A named register ends. Two close marker forms: (a) `**NULL REGISTER CLOSE**` -- bare -- and (b) `**NULL REGISTER CLOSE** -- Null baseline established`. What does the reader know at (b) that cannot be derived from (a) alone? Why is (a) a departure-point marker but not a closure-assertion marker?

NCQ-2. A register close marker should simultaneously name what terminates and characterize what that termination establishes. When both appear in one compound line, what structural property does the boundary gain that the bare close lacks? What reasoning would a reader perform externally at a bare close that the compound close performs internally?

DSQ-1. A manifest close can assert its terminal position and name its successor in two forms: (a) a single sentence embedding both -- "This is MANIFEST-N's last line before TABLE-N" -- or (b) two structurally independent sentences -- "This is the last content line of MANIFEST-N. TABLE-N header follows directly below." What structural difference between these forms is visible at parse time without reading sentence content? What verification operation is possible with (b) that requires inference with (a)?

DSQ-2. When two independent assertions must be verifiably co-present in a single document element, what is the minimum structural form that allows a verifier to confirm each assertion's presence independently -- without reading the entire element for semantic content? Why does embedding both in a single sentence fail this independent-verifiability requirement?

DSQ-3. An agent is instructed that its manifest close must satisfy two structurally independent assertions. If the close line is one sentence, what parse-time ambiguity arises about whether both are present and distinct? What does making each assertion a grammatically independent sentence resolve at parse time that single-sentence embedding does not?

---

**NULL REGISTER CLOSE** -- Null baseline established: [author an accomplishment descriptor from NCQ-1 and NCQ-2]

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell -- what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied -- without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE** -- Departure baseline established: [author an accomplishment descriptor from NCQ-1 and NCQ-2]

---

**CAUSAL PHASE CLOSE**

All questions answered -- NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE -- Schema Authorship

Produce the TRAVERSAL-SCHEMA -- a named artifact a reader can reference to verify the trace that follows. Author in your own words from your CAUSAL PHASE reasoning. The unifying principle to author: every structural boundary in a trace document is a departure from the default condition of epistemic inertia. No boundary is a bare positional marker; every boundary simultaneously names itself and characterizes what epistemic work it performs or has completed. This principle applies to all three boundary types -- manifest close-lines (departure from spatial inertia), register section headers (departure from identity-only inertia), and register close markers (departure from position-only closure inertia).

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Structural boundary declarations (three templates):

           3a. Manifest adjacency and dual-assertion close-line:
           Derive from NQ-3, DQ-2 through DQ-5, and DSQ-1 through DSQ-3.
           Write the structural rationale for the close-line mechanism.
           Write the structural rationale for two-sentence assertion independence.
           Write the complete close-line placeholder instruction text.
           The placeholder must: open with obligation count (DQ-5), enumerate both
           constraints as labeled independent items (DQ-3), declare entanglement that
           neither alone satisfies (DQ-4), specify two grammatically independent
           sentences (DSQ-1 through DSQ-3), name both assertions.
           Declare the two-sentence close-line text:
           Sentence 1 (identity): "This is the last content line of MANIFEST-N."
           Sentence 2 (successor): "TABLE-N header follows directly below."

           3b. Register header compound template:
           Derive from NHQ-1, NHQ-2, and NHQ-3.
           Write the rationale: why compound form departs from bare-label inertia.
           Declare the template: **[LABEL]** -- [epistemic-function descriptor].
           Include a failure-mode exemplar demonstrating the inertia state that the
           compound form departs from:
             WRONG (bare label -- epistemic inertia): **NULL REGISTER**
             CORRECT (compound -- departure from inertia): **NULL REGISTER** -- Epistemic status of null cases
           Include the compound header line you authored in NHQ-3 as a second passing exemplar.

           3c. Register close compound template:
           Derive from NCQ-1 and NCQ-2.
           Write the rationale: why compound close departs from positional-only closure inertia.
           Declare the template: **[LABEL] CLOSE** -- [accomplishment descriptor].
           Give at least one passing exemplar:
             **NULL REGISTER CLOSE** -- Null baseline established: [epistemic function established]

           Author the unifying principle: the compound form applied to headers (3b) and close
           markers (3c) and the dual-assertion form applied to manifest closes (3a) all share
           the same structural logic -- every boundary names what it is and what epistemic work
           it performs or finalizes. A boundary that names only its position is in epistemic inertia.
           Every authored boundary in this trace departs from that inertia.

 Area 4 -- Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3 declares all three templates -- 3a with two-sentence close-line, 3b with failure-mode exemplar and NHQ-3 passing exemplar, 3c with passing exemplar -- with their rationales.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. Apply all three boundary declaration templates from Area 3 throughout:

- Every named register header: compound form from Area 3b -- identity label AND epistemic-function descriptor in one parseable line. Match the descriptor quality to the passing exemplars, not to the WRONG form. A bare label is a boundary in epistemic inertia; your schema departs from that inertia by design.
- Every named register close marker: compound form from Area 3c -- close label AND accomplishment descriptor in one parseable line.
- Every manifest close-line: dual-assertion two-sentence form from Area 3a -- identity sentence AND successor sentence as grammatically independent co-present sentences.

No boundary in this trace is a bare positional marker. You derived this principle from your CAUSAL PHASE and authored it in your TRAVERSAL-SCHEMA. Satisfying only one assertion at any boundary does not satisfy the boundary requirement -- you articulated why across NHQ-1, NHQ-2, NCQ-1, NCQ-2, and DSQ-1 through DSQ-3.

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
*[Apply the TRAVERSAL-SCHEMA Area 3a close-line placeholder -- verbatim, as two grammatically independent sentences, as this manifest's terminal lines, naming TABLE-1 as successor.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the TRAVERSAL-SCHEMA Area 3a close-line placeholder -- verbatim, as two grammatically independent sentences, as this manifest's terminal lines, naming TABLE-2 as successor.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default. Every departure code is a supported claim; every hop without evidence carries the null default. Active hops have departed from inertia -- their evidence must justify the departure code.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed -- basis / Departure -- evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops -- all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply the TRAVERSAL-SCHEMA Area 3a close-line placeholder -- verbatim, as two grammatically independent sentences, as this manifest's terminal lines, naming TABLE-3 as successor.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```
- Direct -- state writes the event handler or synchronous code produces immediately.
- Inherited -- transitive state writes via useEffect, watch, computed cascades, middleware, subscriptions.

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none -- no effects, subscriptions, or watchers triggered.
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
*[Apply the TRAVERSAL-SCHEMA Area 3a close-line placeholder -- verbatim, as two grammatically independent sentences, as this manifest's terminal lines, naming TABLE-4 as successor.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear -- including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes -- reason / No -- reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|
| T-01 | *(from TABLE-2)* | Yes (1) / No | | Yes -- [reason] / No -- [reason] | *(UR-ID or "--")* |

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
*[Apply the TRAVERSAL-SCHEMA Area 3a close-line placeholder -- verbatim, as two grammatically independent sentences, as this manifest's terminal lines, naming TABLE-5 as successor.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|
| *(API call / timer / subscription / navigation / none)* | | | *(synchronous / microtask / macrotask)* | |

Zero-effects row: `| none | -- | No API calls, timers, subscriptions, or navigation triggered. | -- | -- |`

---

**TABLE-6 · Final UI State -- Four-Phase Progression**

| Phase | UI State | Visible Elements | Disabled/Enabled | User Perception |
|-------|----------|-----------------|-----------------|-----------------|
| 1 · Pre-action baseline | | | | |
| 2 · Synchronous / optimistic | | | | |
| 3 · Async success | | | | |
| 4 · Async error | | | | |

[GATE-6: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit -- C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## R18 Variation Summary

| Variation | Axes | C-55 | C-56 | C-57 | Key mechanism | Expected score |
|-----------|------|------|------|------|---------------|----------------|
| V-01 | Role sequence | ✓ NHQ-1/NHQ-2/NHQ-3 | ✓ Schema Area 3 template | ✓ NHQ-3 exemplar forwarded to schema | Causal exemplar derivation question + schema forward-reference | ~185-186/188 |
| V-02 | Output format | ✓ NHQ-1/NHQ-2 | ✓ Schema boundary table row | ✓ Blank-blocked Worked Example cell in table | Tabular schema format enforces exemplar cell structurally | ~185-186/188 |
| V-03 | Lifecycle emphasis | ✗ NCQ only (close-marker, not header-form) | ✗ Schema Area 3 covers close template only | ✗ No exemplar-derivation path | NCQ-only causal phase omits header-form grounding | ~177-180/188 |
| V-04 | Role sequence + Output format | ✓ NHQ-1/NHQ-2/NHQ-3 | ✓ Schema boundary table row | ✓ Table Example cell bound to NHQ-3 production | Dual-path: causal exemplar + blank-blocked table cell | ~186-188/188 |
| V-05 | All axes + Inertia framing | ✓ NHQ-1/NHQ-2/NHQ-3 | ✓ Schema Area 3b template | ✓ Failure-mode + passing exemplars in schema | Inertia framing names the WRONG form + two passing exemplars | ~187-188/188 |

**C-55 differential**: V-03 uses NCQ questions (close-marker form) -- same gap pattern as R17 V-02. NCQ tests: why the compound close form departs from bare close. NHQ tests: why the compound header form departs from bare label. These are structurally independent epistemic targets. NCQ does not ground the header form; only NHQ does.

**C-56 differential**: V-03's schema derives from NCQ reasoning -- it produces a compound close template in Area 3 but has no path to derive a compound header template (no NHQ reasoning exists). A schema Area 3 that covers close-marker form but omits header template field does not satisfy C-56.

**C-57 differential**: V-01 forwards NHQ-3's produced exemplar into schema Area 3 by instruction. V-02 uses a blank-blocked table cell. V-04 combines both. V-05 adds a failure-mode exemplar alongside the passing exemplar. V-03 has no exemplar-derivation path because no NHQ questions produce one.

**Minimum sufficient condition for C-57 under test**: Does forwarding a causal-phase production into a schema field (V-01) achieve C-57, or does C-57 require a blank-blocked schema field enforcing the exemplar production (V-02)? V-04 resolves ambiguity if both axes together achieve C-57 but either alone does not.
