# trace-component -- QU5 Simplified (from V-05, R20)

**Source**: V-05 (all axes: C-59 + C-60 + C-61)
**QU5 goal**: Minimal prompt passing all essential criteria (C-01–C-05) plus V-05 aspirational innovations (C-58–C-64).

---

Complete Role 1 before Role 2.

---

**ROLE 1 -- SCHEMA ARCHITECT**

Complete CAUSAL PHASE before SCHEMA PHASE. No schema structure in CAUSAL PHASE.

---

### CAUSAL PHASE -- Epistemic Reasoning

Complete NULL REGISTER before DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace -- positive assertion, negative assertion, or suspension of judgment?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. What is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header, before any rule has been applied? What makes this the correct starting point for an enforcement mechanism?

NHQ-1. A register section can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does the compound form provide that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A schema artifact's boundary enforcement table has an Enforcement Rationale column. Version A populates each cell with a named simpler alternative (e.g., "plain label", "prose sub-section") and the failure mode that alternative produces. Version B uses general affirmation language ("ensures the required form is used"). Both satisfy the structural requirement that the column be present and non-blank. A verifier with only the schema artifact must determine whether the comparison-column requirement is independently satisfied. Which version permits that determination, and why? What property of Version A's cell content, absent from Version B, enables independent verification?

---

**NULL REGISTER CLOSE**

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell?

DQ-2. What must be true of a manifest-to-table adjacency enforcement mechanism's placement for violations to be self-contradictory at production time, not only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied -- without consulting any source outside the output?

DQ-4. Two requirements are each necessary for compliance; neither alone constitutes partial compliance. What must the instruction state for an agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. What information at a multi-requirement instruction's opening establishes how many satisfaction targets must be met before reading the body?

---

**DEPARTURE REGISTER CLOSE**

---

**CAUSAL PHASE CLOSE**

---

### SCHEMA PHASE -- Schema Authorship

Produce the TRAVERSAL-SCHEMA from your CAUSAL PHASE reasoning.

```
TRAVERSAL-SCHEMA
----------------
[Areas 1 through 5 in full.

 Area 1 -- Framework context: framework, state management library, component model.

 Area 2 -- Direction default contract (from NQ-1–NQ-2, DQ-1):
           Author the null state and justification, each departure code with
           evidentiary requirement, and the inert-hop documentation rule.

 Area 3 -- Structural boundary declarations.
           Derive from NQ-3, NHQ-1, NHQ-2, and DQ-2 through DQ-5.
           Author rationales for: close-line enforcement (NQ-3, DQ-2);
           dual-constraint form (DQ-3–DQ-5); compound register header (NHQ-1, NHQ-2).
           Then produce the boundary enforcement table:

           | Boundary Type | Template Pattern | Worked Example | Enforcement Rationale |
           |---------------|-----------------|----------------|----------------------|
           | Manifest close-line | [dual-req form: obligation count + two independent constraints + entanglement declaration + positional claim + successor name] | [write one complete manifest close-line verbatim] | [name a simpler alternative and its failure mode -- derive from DQ-3 and DQ-4] |
           | Register section header | **[LABEL]** -- [epistemic-function descriptor] | [write one complete compound header line: a real register label and a concrete descriptor] | [name a simpler alternative and its failure mode -- derive from NHQ-1 and NHQ-2] |

           Enforcement rules for this table:
           - No cell may be blank.
           - Worked Example cells require a complete concrete line, not a placeholder pattern.
           - Enforcement Rationale cells must name a specific simpler alternative and its failure mode. Generic affirmation language does not satisfy this requirement -- a verifier with only the schema must be able to identify the alternative and why it fails.

 Area 4 -- Table inventory and manifest structure.
           List every table by name and purpose.
           Each manifest declares four fields: Components in scope, State keys may be
           touched, Side effects may fire, and PHASE VOCABULARY (framework-specific
           terms for that phase's analysis table; minimum two).

 Area 5 -- Gate semantic type vocabulary.
           Author the type definitions in your own words.

           | Type | Scope | Definition |
           |------|-------|------------|
           | DIRECTIVE | Structural form requirement | [author: gates enforcing mandatory structural or syntactic form] |
           | REQUIREMENT | Mandatory content presence | [author: gates enforcing mandatory content presence] |

           All gate blocks carry a type label from this area -- format: [GATE-N: TYPE: excluded-string(s)].]
```

Do not begin MANIFEST-1 until TRAVERSAL-SCHEMA is complete, Area 3 cells have specific named alternatives, and Area 5 defines DIRECTIVE and REQUIREMENT.

---

**ROLE 2 -- TRACE ANALYST**

You are a frontend domain expert. Execute the trace per the TRAVERSAL-SCHEMA. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: use your Area 3 Worked Example verbatim, naming the successor table. All register headers match the compound form in your Area 3 Worked Example. Every gate block carries the semantic type from your Area 5 vocabulary -- format: `[GATE-N: TYPE: excluded-strings]`. Every phase manifest includes PHASE VOCABULARY with at minimum two framework-specific terms for that phase.

**FRAMEWORK DECLARATION (required output header)**

| Field | Value |
|-------|-------|
| Framework | `[Area 1]` |
| State management | `[Area 1]` |
| Component model | `[Area 1]` |

---

**MANIFEST-1 · Event Phase**

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [event-anchor terms; minimum two]
```
*[Area 3 close-line, verbatim -- successor TABLE-1.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|

[GATE-1: REQUIREMENT: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops -- include pass-through hops explicitly]
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [traversal terms; minimum two]
```
*[Area 3 close-line, verbatim -- successor TABLE-2.]*

**TABLE-2 · Component Tree Traversal**

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed -- basis / Departure -- evidence] | Notes |
|------|------|-----------|-----------|------|-------|

T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory):**
```
Inert hops: ___ (T-IDs: ___)
[If 0]: No inert hops detected.
```

[GATE-2: REQUIREMENT: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [mutation terms; minimum two]
```
*[Area 3 close-line, verbatim -- successor TABLE-3.]*

**TABLE-3 · State Mutation Map**

**MUTATION COUNT PRE-DECLARATION:**
```
Mutations: N=___ direct, M=___ inherited (total: ___)
```

If total = 0:
```
ZERO MUTATION DECLARATION
Direct mutations: none
Inherited mutations: none.
Reason: [read-only / display-only / event consumed without dispatch / other]
```

If total > 0, row count must equal N + M.

| State Key | Owner | Layer | Type | Old Value Shape | New Value Shape | Mechanism |
|-----------|-------|-------|------|-----------------|-----------------|-----------|

[GATE-3: REQUIREMENT: TABLE-3 does not close on "state updates", "the store is modified", "previous value", "N/A", or row count mismatch.]

---

**MANIFEST-4 · Re-render Phase**

```
Components in scope: [all T-IDs from TABLE-2]
State keys may be touched: ___
Side effects may fire: ___
PHASE VOCABULARY: [re-render terms; minimum two]
```
*[Area 3 close-line, verbatim -- successor TABLE-4.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear -- including inert pass-through hops.

| T-ID | Component | Re-renders? [Yes (N) / No] | Reason | Necessary? [Yes -- reason / No -- reason] | UR-ID |
|------|-----------|----------|--------|---------|-------|

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
PHASE VOCABULARY: [settle terms; minimum two]
```
*[Area 3 close-line, verbatim -- successor TABLE-5.]*

**TABLE-5 · Side Effects**

| Type | Trigger | Mechanism | Timing | Cleanup |
|------|---------|-----------|--------|---------|

Zero-effects row: `| none | -- | No effects triggered. | -- | -- |`

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
