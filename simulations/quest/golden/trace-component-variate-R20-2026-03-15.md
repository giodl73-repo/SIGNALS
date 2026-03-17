# trace-component -- R20 Variations (v20 rubric)

**Round**: 20
**Rubric ceiling**: 196 pts (C-01 through C-61)
**New criteria targeted**: C-59 (Schema-Artifact Comparison Column Independence), C-60 (Gate-Block Semantic Type Annotation), C-61 (Per-Phase Vocabulary Declaration in Manifest)

**R19 baseline summary:**
- V-01: NHQ-1/2/3 (exemplar derivation) + Area 3 prose + exemplar (C-58 ✗). ~185-186/190.
- V-02: NHQ-1/2 + Area 3 boundary enforcement table (C-58 ✓). ~188-190/190.
- V-03: Phase register (PQ-1/PQ-2) + Area 3 prose, no NHQ-3 (C-55 ✓, C-58 ✗). ~183-185/190.
- V-04: NHQ-3 exemplar derivation + Area 3 table with cell binding, dual enforcement (C-58 ✓). DIRECTIVE/REQUIREMENT gate labels (C-60 signal). ~188-190/190.
- V-05: NHQ-1/2/3 + boundary table + failure-mode exemplar + per-phase vocabulary (C-58 ✓). Per-phase vocab in manifests (C-61 signal). ~188-190/190.

**R20 variation axes chosen (3 single-axis + 2 combined):**
1. Role sequence -- add NHQ-3 grounding schema-artifact comparison column independence (C-59 target)
2. Output format -- add gate semantic type vocabulary to schema (Area 5) and annotate gate blocks (C-60 target)
3. Lifecycle emphasis -- add per-phase vocabulary declarations to each manifest block (C-61 target)
4. Combined: role sequence + output format -- NHQ-3 + gate semantic type vocabulary (C-59 + C-60)
5. Combined: all axes -- NHQ-3 + gate semantic type vocabulary + per-phase vocabulary in manifests (C-59 + C-60 + C-61)

**R20 variation map:**

| Variation | Axis | C-58 | C-59 | C-60 | C-61 | Notes |
|-----------|------|------|------|------|------|-------|
| V-01 | Role sequence | PASS | PASS | FAIL | FAIL | NHQ-3 grounds schema comparison independence; Area 3 requires named alternatives per row; no gate types, no per-phase vocab |
| V-02 | Output format | PASS | FAIL | PASS | FAIL | Area 5 gate semantic type vocabulary; DIRECTIVE/REQUIREMENT gate blocks; no NHQ-3, no per-phase vocab |
| V-03 | Lifecycle emphasis | PASS | FAIL | FAIL | PASS | PHASE VOCABULARY field in all manifests; no NHQ-3, no gate types |
| V-04 | Role sequence + Output format | PASS | PASS | PASS | FAIL | NHQ-3 + Area 5 gate types; no per-phase vocab |
| V-05 | All axes | PASS | PASS | PASS | PASS | All three new criteria activated |

---

## V-01 · Role Sequence -- Schema Comparison Column Independence (Single Axis)

**Axis**: Role sequence
**Hypothesis**: NHQ-3 forces the model to reason about what makes an Enforcement Rationale column an *independent* comparison-column source vs. merely co-present comparison evidence. The answer -- that cells must name specific simpler alternatives and their failure modes, not generic affirmation language -- binds the Area 3 schema instruction to require named alternatives per row. A verifier reading only the schema artifact (without TABLE-7 or TABLE-8) can confirm comparison-column coverage from the schema's Enforcement Rationale column alone. C-59 ✓. No gate type annotation (C-60 ✗). No per-phase vocabulary (C-61 ✗). Expected: ~192-194/196.

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

NHQ-3. A table embedded in a schema artifact carries a column labeled Enforcement Rationale. Two versions of this column exist: Version A populates each cell with a named simpler alternative (e.g., "plain label", "prose sub-section", "ad-hoc header") and the failure mode that alternative produces when used in place of the required form; Version B populates each cell with general affirmation language ("ensures the required form is used", "satisfies the enforcement requirement"). Both versions satisfy the structural requirement that the column be present and non-blank. A verifier is given only the schema artifact -- no other tables in the output are available -- and must determine whether the schema artifact independently satisfies the comparison-column requirement: at least one table with a comparison column populated for every row. Which version permits that determination, and why? What specific property of Version A's cell content, absent from Version B, enables independent verification of comparison-column compliance?

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
           Derive from NQ-3, NHQ-1, NHQ-2, NHQ-3, and DQ-2 through DQ-5.
           Author the rationale for close-line enforcement (NQ-3, DQ-2).
           Author the rationale for dual-constraint form (DQ-3 through DQ-5).
           Author the rationale for compound register header form (NHQ-1, NHQ-2).
           Then produce the boundary enforcement table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [two-req dual-assertion form: obligation count + two independent constraints + entanglement declaration + positional claim + successor name] | [write one complete manifest close-line verbatim] | [name the specific simpler alternative (e.g., single-requirement form, positional claim alone, obligation count omitted) and the failure mode it produces when used in place of the dual-requirement form -- derive from DQ-3 and DQ-4] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line: a real register label and a concrete descriptor] | [name the specific simpler alternative (e.g., bare bold label, label followed by colon, separate descriptor sentence) and the failure mode it produces when used in place of the compound form -- derive from NHQ-1, NHQ-2, and NHQ-3] |

           Enforcement rules for this table:
           - No cell may be blank.
           - Worked Example cells require a complete concrete line, not a placeholder pattern.
           - Enforcement Rationale cells must name a specific simpler alternative and state
             the failure mode it produces -- generic affirmation language ("ensures the
             required form", "satisfies compliance", "enforces the standard") does not
             satisfy this requirement. A verifier reading only this schema must be able to
             determine what the simpler alternative is and why it fails.

 Area 4 -- Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3's boundary enforcement table has all cells populated -- no blank Worked Example cells, no blank Enforcement Rationale cells, no generic affirmation language in Enforcement Rationale cells.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: reproduce the manifest close-line form from your Area 3 boundary enforcement table -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2; your boundary table's Worked Example cell demonstrates the standard -- all register headers in this trace must match that standard. Satisfying only one of the two close-line constraints does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4. Your Area 3 Enforcement Rationale column names specific simpler alternatives and failure modes; a verifier reading only your schema must be able to confirm the comparison-column requirement is met without consulting TABLE-7 or TABLE-8 -- verify your NHQ-3 reasoning holds.

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-1 as successor.]*

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-2 as successor.]*

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-3 as successor.]*

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-4 as successor.]*

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-5 as successor.]*

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

## V-02 · Output Format -- Gate-Block Semantic Type Annotation (Single Axis)

**Axis**: Output format
**Hypothesis**: Adding a Gate Semantic Type Vocabulary as Schema Area 5 -- defining DIRECTIVE (structural form requirement) and REQUIREMENT (mandatory content presence) -- and instructing the model to annotate every gate block with the schema-defined type label produces the `[GATE-N: TYPE: ...]` form required by C-60. The type annotation is bound to the self-authored schema (not coined ad hoc from the prompt), making violation of the annotation requirement a self-contradiction. No NHQ-3 is added (C-59 ✗). No per-phase vocabulary (C-61 ✗). C-58 ✓ from baseline Area 3 enforcement table. Expected: ~192-194/196.

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
[Author the complete schema here. Areas 1 through 5 in full.
 Every principle must derive from your CAUSAL PHASE answers.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Structural boundary declarations.
           Derive from NQ-3, NHQ-1, NHQ-2, and DQ-2 through DQ-5.
           Author the rationale for close-line enforcement (NQ-3, DQ-2).
           Author the rationale for dual-constraint form (DQ-3 through DQ-5).
           Author the rationale for compound register header form (NHQ-1, NHQ-2).
           Then produce the boundary enforcement table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [two-req dual-assertion form: obligation count + two independent constraints + entanglement declaration + positional claim + successor name] | [write one complete manifest close-line verbatim] | [derive from DQ-3 and DQ-4: state why dual-requirement form prevents one-of-two partial satisfaction] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line: a real register label and a concrete descriptor] | [derive from NHQ-1 and NHQ-2: state why compound form eliminates the two-read requirement] |

           Enforcement rules for this table:
           - No cell may be blank.
           - Worked Example cells require a complete concrete line, not a placeholder pattern.
           - Enforcement Rationale cells must state the reasoning derived from your CAUSAL
             PHASE answers -- not a restatement of the template pattern itself.

 Area 4 -- Table inventory: every table by name and purpose.

 Area 5 -- Gate semantic type vocabulary.
           Define the semantic type categories used to annotate gate blocks in this trace.
           Author the type definitions in your own words.

           | Type | Scope | Definition |
           |------|-------|------------|
           | DIRECTIVE | Structural form requirement | [author: when to apply -- gates that enforce a mandatory structural or syntactic form; the output must use a specific format, table structure, column arrangement, or row count pattern] |
           | REQUIREMENT | Mandatory content presence | [author: when to apply -- gates that enforce mandatory content elements; a specific field value, declared count, cross-reference, or enumerated entry must be present in the output] |

           Additional semantic types may be defined here rather than coined ad hoc in the
           trace body. All gate blocks in this trace must carry one of the above labels
           (or a label defined in this area) as the first component after the gate ordinal,
           before the excluded strings -- format: [GATE-N: TYPE: excluded-string(s)].]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3's boundary enforcement table has all cells populated, and Area 5's gate semantic type vocabulary defines at minimum DIRECTIVE and REQUIREMENT with authored definitions.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: reproduce the manifest close-line form from your Area 3 boundary enforcement table -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2; your boundary table's Worked Example cell demonstrates the standard -- all register headers in this trace must match that standard. Satisfying only one of the two close-line constraints does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4. Every gate block in this trace must carry the semantic type annotation from your Area 5 vocabulary -- format: `[GATE-N: TYPE: excluded-strings]` -- using only the types defined in your schema.

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-1 as successor.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: REQUIREMENT: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-2 as successor.]*

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

[GATE-2: REQUIREMENT: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-3 as successor.]*

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

[GATE-3: REQUIREMENT: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-4 as successor.]*

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

[GATE-4: REQUIREMENT: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-5 as successor.]*

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

[GATE-6: DIRECTIVE: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: REQUIREMENT: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

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

## V-03 · Lifecycle Emphasis -- Per-Phase Vocabulary Declaration in Manifest (Single Axis)

**Axis**: Lifecycle emphasis
**Hypothesis**: Adding a PHASE VOCABULARY field to every phase manifest -- requiring at minimum two framework-specific terms scoped to that phase's analysis table -- produces the per-phase vocabulary declaration required by C-61. The field is a lifecycle change: it makes the vocabulary question locally answerable at each manifest without consulting the global FRAMEWORK DECLARATION. No NHQ-3 (C-59 ✗). No gate type annotation (C-60 ✗). C-58 ✓ from baseline Area 3 enforcement table. Expected: ~192-194/196.

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
           Author the rationale for compound register header form (NHQ-1, NHQ-2).
           Then produce the boundary enforcement table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [two-req dual-assertion form: obligation count + two independent constraints + entanglement declaration + positional claim + successor name] | [write one complete manifest close-line verbatim] | [derive from DQ-3 and DQ-4: state why dual-requirement form prevents one-of-two partial satisfaction] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line: a real register label and a concrete descriptor] | [derive from NHQ-1 and NHQ-2: state why compound form eliminates the two-read requirement] |

           Enforcement rules for this table:
           - No cell may be blank.
           - Worked Example cells require a complete concrete line, not a placeholder pattern.
           - Enforcement Rationale cells must state the reasoning derived from your CAUSAL
             PHASE answers -- not a restatement of the template pattern itself.

 Area 4 -- Table inventory: every table by name and purpose.
           Include the PHASE VOCABULARY field in the manifest structure description:
           each phase manifest declares four fields -- Components in scope, State keys
           may be touched, Side effects may fire, and PHASE VOCABULARY. The PHASE
           VOCABULARY field enumerates the framework-specific terms valid for that
           phase's analysis table, scoped to the phase's analytical content. Minimum
           two terms per manifest.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3's boundary enforcement table has all cells populated -- no blank Worked Example cells, no blank Enforcement Rationale cells.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: reproduce the manifest close-line form from your Area 3 boundary enforcement table -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2; your boundary table's Worked Example cell demonstrates the standard -- all register headers in this trace must match that standard. Satisfying only one of the two close-line constraints does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4. Every phase manifest must include a PHASE VOCABULARY field listing at minimum two framework-specific terms valid for that phase's analysis table; the terms must be scoped to the phase's analytical content, not copied from the global FRAMEWORK DECLARATION.

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
PHASE VOCABULARY: [framework-specific terms valid for event-anchor analysis -- e.g., SyntheticEvent, addEventListener, dispatchEvent, event.target; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-1 as successor.]*

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
PHASE VOCABULARY: [framework-specific terms valid for traversal analysis -- e.g., props, context, HOC, React.Children, forwardRef; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-2 as successor.]*

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
PHASE VOCABULARY: [framework-specific terms valid for state mutation analysis -- e.g., useState, useReducer, dispatch, setState, computed; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-3 as successor.]*

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
PHASE VOCABULARY: [framework-specific terms valid for re-render analysis -- e.g., React.memo, shouldComponentUpdate, PureComponent, useMemo, useCallback; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-4 as successor.]*

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
PHASE VOCABULARY: [framework-specific terms valid for side effect and UI settle analysis -- e.g., useEffect, cleanup, AbortController, Promise, microtask; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-5 as successor.]*

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

## V-04 · Combined: Role Sequence + Output Format -- Schema Independence + Gate Annotation (Two Axes)

**Axis**: Role sequence + Output format
**Hypothesis**: NHQ-3 forces the schema's Enforcement Rationale column to carry specific named alternatives (C-59 target); Area 5 gate semantic type vocabulary forces DIRECTIVE/REQUIREMENT annotation on all gate blocks (C-60 target). The two mechanisms are structurally independent: NHQ-3 works at the schema-artifact layer (what the comparison column's cells must contain), while Area 5 works at the gate-block layer (what label each gate must carry). Combined, they activate C-59 and C-60 without per-phase vocabulary (C-61 ✗). Expected: ~194-196/196.

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

NHQ-3. A table embedded in a schema artifact carries a column labeled Enforcement Rationale. Two versions of this column exist: Version A populates each cell with a named simpler alternative (e.g., "plain label", "prose sub-section", "ad-hoc header") and the failure mode that alternative produces when used in place of the required form; Version B populates each cell with general affirmation language ("ensures the required form is used", "satisfies the enforcement requirement"). Both versions satisfy the structural requirement that the column be present and non-blank. A verifier is given only the schema artifact -- no other tables in the output are available -- and must determine whether the schema artifact independently satisfies the comparison-column requirement: at least one table with a comparison column populated for every row. Which version permits that determination, and why? What specific property of Version A's cell content, absent from Version B, enables independent verification of comparison-column compliance?

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
[Author the complete schema here. Areas 1 through 5 in full.
 Every principle must derive from your CAUSAL PHASE answers.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Structural boundary declarations.
           Derive from NQ-3, NHQ-1, NHQ-2, NHQ-3, and DQ-2 through DQ-5.
           Author the rationale for close-line enforcement (NQ-3, DQ-2).
           Author the rationale for dual-constraint form (DQ-3 through DQ-5).
           Author the rationale for compound register header form (NHQ-1, NHQ-2).
           Then produce the boundary enforcement table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [two-req dual-assertion form: obligation count + two independent constraints + entanglement declaration + positional claim + successor name] | [write one complete manifest close-line verbatim] | [name the specific simpler alternative (e.g., single-requirement form, positional claim alone, obligation count omitted) and the failure mode it produces -- derive from DQ-3 and DQ-4] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line: a real register label and a concrete descriptor] | [name the specific simpler alternative (e.g., bare bold label, label followed by colon, separate descriptor sentence) and the failure mode it produces -- derive from NHQ-1, NHQ-2, and NHQ-3] |

           Enforcement rules for this table:
           - No cell may be blank.
           - Worked Example cells require a complete concrete line, not a placeholder pattern.
           - Enforcement Rationale cells must name a specific simpler alternative and state
             the failure mode it produces -- generic affirmation language ("ensures the
             required form", "satisfies compliance", "enforces the standard") does not
             satisfy this requirement. A verifier reading only this schema must be able to
             determine what the simpler alternative is and why it fails.

 Area 4 -- Table inventory: every table by name and purpose.

 Area 5 -- Gate semantic type vocabulary.
           Define the semantic type categories used to annotate gate blocks in this trace.
           Author the type definitions in your own words.

           | Type | Scope | Definition |
           |------|-------|------------|
           | DIRECTIVE | Structural form requirement | [author: when to apply -- gates that enforce a mandatory structural or syntactic form; the output must use a specific format, table structure, column arrangement, or row count pattern] |
           | REQUIREMENT | Mandatory content presence | [author: when to apply -- gates that enforce mandatory content elements; a specific field value, declared count, cross-reference, or enumerated entry must be present in the output] |

           Additional semantic types may be defined here rather than coined ad hoc in the
           trace body. All gate blocks in this trace must carry one of the above labels
           (or a label defined in this area) as the first component after the gate ordinal,
           before the excluded strings -- format: [GATE-N: TYPE: excluded-string(s)].]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3's boundary enforcement table has all cells populated with specific named alternatives (no generic affirmation language), and Area 5's gate semantic type vocabulary defines at minimum DIRECTIVE and REQUIREMENT with authored definitions.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: reproduce the manifest close-line form from your Area 3 boundary enforcement table -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2; your boundary table's Worked Example cell demonstrates the standard -- all register headers in this trace must match that standard. Satisfying only one of the two close-line constraints does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4. Your Area 3 Enforcement Rationale column names specific simpler alternatives and failure modes; a verifier reading only your schema must be able to confirm the comparison-column requirement is met without consulting TABLE-7 or TABLE-8 -- verify your NHQ-3 reasoning holds. Every gate block in this trace must carry the semantic type annotation from your Area 5 vocabulary -- format: `[GATE-N: TYPE: excluded-strings]` -- using only the types defined in your schema.

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
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-1 as successor.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: REQUIREMENT: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-2 as successor.]*

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

[GATE-2: REQUIREMENT: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-3 as successor.]*

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

[GATE-3: REQUIREMENT: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-4 as successor.]*

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

[GATE-4: REQUIREMENT: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-5 as successor.]*

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

[GATE-6: DIRECTIVE: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: REQUIREMENT: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

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

## V-05 · Combined: All Axes -- Schema Independence + Gate Annotation + Per-Phase Vocabulary (Three Axes)

**Axis**: Role sequence + Output format + Lifecycle emphasis
**Hypothesis**: NHQ-3 (C-59) + Area 5 gate semantic type vocabulary (C-60) + PHASE VOCABULARY in all manifests (C-61). The three mechanisms are structurally independent and non-interfering: NHQ-3 works at the schema artifact's comparison column; gate types work at gate-block bracket syntax; per-phase vocabulary works at manifest field content. All three R19 differentials activated simultaneously. Expected: ~196/196 (ceiling).

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

NHQ-3. A table embedded in a schema artifact carries a column labeled Enforcement Rationale. Two versions of this column exist: Version A populates each cell with a named simpler alternative (e.g., "plain label", "prose sub-section", "ad-hoc header") and the failure mode that alternative produces when used in place of the required form; Version B populates each cell with general affirmation language ("ensures the required form is used", "satisfies the enforcement requirement"). Both versions satisfy the structural requirement that the column be present and non-blank. A verifier is given only the schema artifact -- no other tables in the output are available -- and must determine whether the schema artifact independently satisfies the comparison-column requirement: at least one table with a comparison column populated for every row. Which version permits that determination, and why? What specific property of Version A's cell content, absent from Version B, enables independent verification of comparison-column compliance?

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
[Author the complete schema here. Areas 1 through 5 in full.
 Every principle must derive from your CAUSAL PHASE answers.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
           Author: the null state and its justification, every departure code and
           its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 -- Structural boundary declarations.
           Derive from NQ-3, NHQ-1, NHQ-2, NHQ-3, and DQ-2 through DQ-5.
           Author the rationale for close-line enforcement (NQ-3, DQ-2).
           Author the rationale for dual-constraint form (DQ-3 through DQ-5).
           Author the rationale for compound register header form (NHQ-1, NHQ-2).
           Then produce the boundary enforcement table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [two-req dual-assertion form: obligation count + two independent constraints + entanglement declaration + positional claim + successor name] | [write one complete manifest close-line verbatim] | [name the specific simpler alternative (e.g., single-requirement form, positional claim alone, obligation count omitted) and the failure mode it produces -- derive from DQ-3 and DQ-4] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line: a real register label and a concrete descriptor] | [name the specific simpler alternative (e.g., bare bold label, label followed by colon, separate descriptor sentence) and the failure mode it produces -- derive from NHQ-1, NHQ-2, and NHQ-3] |

           Enforcement rules for this table:
           - No cell may be blank.
           - Worked Example cells require a complete concrete line, not a placeholder pattern.
           - Enforcement Rationale cells must name a specific simpler alternative and state
             the failure mode it produces -- generic affirmation language ("ensures the
             required form", "satisfies compliance", "enforces the standard") does not
             satisfy this requirement. A verifier reading only this schema must be able to
             determine what the simpler alternative is and why it fails.

 Area 4 -- Table inventory and manifest structure.
           List every table by name and purpose.
           Manifest structure: each phase manifest declares four fields --
             Components in scope, State keys may be touched, Side effects may fire,
             and PHASE VOCABULARY. The PHASE VOCABULARY field enumerates the
             framework-specific terms valid for that phase's analysis table, scoped to
             the phase's analytical content. Minimum two terms per manifest.

 Area 5 -- Gate semantic type vocabulary.
           Define the semantic type categories used to annotate gate blocks in this trace.
           Author the type definitions in your own words.

           | Type | Scope | Definition |
           |------|-------|------------|
           | DIRECTIVE | Structural form requirement | [author: when to apply -- gates that enforce a mandatory structural or syntactic form; the output must use a specific format, table structure, column arrangement, or row count pattern] |
           | REQUIREMENT | Mandatory content presence | [author: when to apply -- gates that enforce mandatory content elements; a specific field value, declared count, cross-reference, or enumerated entry must be present in the output] |

           Additional semantic types may be defined here rather than coined ad hoc in the
           trace body. All gate blocks in this trace must carry one of the above labels
           (or a label defined in this area) as the first component after the gate ordinal,
           before the excluded strings -- format: [GATE-N: TYPE: excluded-string(s)].]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3's boundary enforcement table has all cells populated with specific named alternatives (no generic affirmation language), and Area 5's gate semantic type vocabulary defines at minimum DIRECTIVE and REQUIREMENT with authored definitions.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: reproduce the manifest close-line form from your Area 3 boundary enforcement table -- verbatim, naming the successor table. You derived the compound register header form from NHQ-1 and NHQ-2; your boundary table's Worked Example cell demonstrates the standard -- all register headers in this trace must match that standard. Satisfying only one of the two close-line constraints does not satisfy the placeholder -- you articulated why in DQ-3 and DQ-4. Your Area 3 Enforcement Rationale column names specific simpler alternatives and failure modes; a verifier reading only your schema must be able to confirm the comparison-column requirement is met without consulting TABLE-7 or TABLE-8 -- verify your NHQ-3 reasoning holds. Every gate block in this trace must carry the semantic type annotation from your Area 5 vocabulary -- format: `[GATE-N: TYPE: excluded-strings]` -- using only the types defined in your schema. Every phase manifest must include a PHASE VOCABULARY field listing at minimum two framework-specific terms valid for that phase's analysis table, scoped to the phase's analytical content.

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
PHASE VOCABULARY: [framework-specific terms valid for event-anchor analysis -- e.g., SyntheticEvent, addEventListener, dispatchEvent, event.target; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-1 as successor.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: REQUIREMENT: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [framework-specific terms valid for traversal analysis -- e.g., props, context, HOC, React.Children, forwardRef; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-2 as successor.]*

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

[GATE-2: REQUIREMENT: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [framework-specific terms valid for state mutation analysis -- e.g., useState, useReducer, dispatch, setState, computed; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-3 as successor.]*

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

[GATE-3: REQUIREMENT: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [framework-specific terms valid for re-render analysis -- e.g., React.memo, shouldComponentUpdate, PureComponent, useMemo, useCallback; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-4 as successor.]*

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

[GATE-4: REQUIREMENT: TABLE-4 does not close on omitting any TABLE-2 T-ID, "several components re-render", blank Necessary cell, or missing PROMOTION BLOCK.]

---

**MANIFEST-5 · UI Settle Phase**

```
Components in scope: [components visible in final UI state]
State keys may be touched: [async resolution mutations]
Side effects may fire: [cleanup or completion effects]
PHASE VOCABULARY: [framework-specific terms valid for side effect and UI settle analysis -- e.g., useEffect, cleanup, AbortController, Promise, microtask; minimum two terms]
```
*[Reproduce the manifest close-line from your TRAVERSAL-SCHEMA Area 3 boundary enforcement table -- verbatim, as this manifest's terminal line, naming TABLE-5 as successor.]*

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

[GATE-6: DIRECTIVE: TABLE-6 does not close on "UI updates accordingly", "reflects state changes", "success and error states are handled", or a three-phase table that collapses rows 3 and 4.]

---

**TABLE-7 · Findings** N/A prohibited.

| ID | Category | Component / State Path | Finding [issue or "none detected -- [reason]"] | Fix -- API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | *(named API or "n/a -- no issue")* | |
| F-02 | Unnecessary re-renders -- UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none -- no unnecessary re-renders detected")* | *(React.memo / createSelector / computed / useMemo -- named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: REQUIREMENT: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

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
