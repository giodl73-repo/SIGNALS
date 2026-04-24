# trace-component — Round 15 Variations

**Variation axes used:**
- Single-axis: Role sequence / structural phase boundary for C-47 (V-01), Phrasing register / epistemic question framing for C-46 (V-02), Inertia framing / two-register question structure for C-48 (V-03)
- Combined: Role sequence + Phrasing register / phase boundary + epistemic questions (V-04), All three axes + Lifecycle emphasis / maximum C-46+C-47+C-48 (V-05)

**R15 context:** Three new criteria from R14 excellence signals:

- **C-46 (Epistemic-Register Question Framing)** — Every causal question in the C-41 question set must be phrased at the epistemic or logical-necessity level, not the structural level. R14 V-04 used structural-register questions: "Why must the block open with an explicit count label — e.g., `N=2 OBLIGATIONS`?" — the question names the schema artifact, enabling copy-by-substitution. R14 V-05 achieved epistemic register in Area 2 but Area 3 three-property questions remained structural-register. The test: if replacing the question's answer with the question's vocabulary produces the schema field, the question is structural-register. Epistemic-register questions require the model to derive the structural form from the underlying concept.

- **C-47 (Causal-Completion Gate Before Schema Authorship)** — The causal question block and the schema authorship slot must be structurally separated phases — causal questions close, then schema production begins as a distinct subsequent section. R14 V-05 had null-hypothesis questions and three-property placeholder questions within Area 3 of the same schema section, followed by "design the placeholder" — the questions and the authorship slot were interleaved in the same structural context. A structural phase boundary requires the causal section to close and the schema section to open as a subsequent distinct section; an advisory instruction ("answer before beginning") without structural separation does not pass.

- **C-48 (Null-Hypothesis Register in Causal Question Set)** — The causal question set must contain two sequentially ordered registers: (1) a null-hypothesis register addressing the epistemic status of the default/null case, (2) a departure-property register addressing structural properties of the departure cases. The null register must appear as a prior block before the departure register. R14 V-05 had null-hypothesis questions first in Area 3 but they were not explicitly labeled as registers and were mixed with area setup framing. The null-hypothesis register establishes the epistemic baseline for the unmarked case before departure conditions can be evaluated as departures from it.

**C-46 / C-47 / C-48 orthogonality:**
- C-46 can be satisfied without C-47 (questions phrased epistemically but in an interleaved block with schema production)
- C-46 can be satisfied without C-48 (epistemic questions in a single register, no null/departure decomposition)
- C-47 can be satisfied without C-46 (causal questions sequenced before schema authorship but questions are structural-register)
- C-48 can be satisfied without C-46 (null register present, questions structural-register, phases not separated)
- Full expression requires all three: C-48 establishes the null baseline as a prior register, C-46 ensures questions require derivation rather than copy, C-47 enforces that the complete causal case precedes schema authorship

**R15 hypothesis for each variation:**
- V-01: Role sequence — split the schema architect role into CAUSAL PHASE (questions only, explicit close gate) and SCHEMA PHASE (blank authorship slot, subsequent distinct section). Tests whether a structural phase boundary in the prompt document achieves C-47 without C-46 (questions remain mixed register) or C-48 (no explicit null/departure register labels). Expected: ~164–166/170.
- V-02: Phrasing register — replace all Area 2 and Area 3 causal questions with epistemic-register questions that do not name any schema artifact in their vocabulary. Tests whether purely epistemic framing achieves C-46 without C-47 (questions and schema in same Area 3 section) or C-48 (single-register question block). Expected: ~162–166/170.
- V-03: Inertia framing — explicitly label Area 3's question block with two sequential registers: NULL REGISTER first (epistemic status of the null/default case), DEPARTURE REGISTER second (structural properties of departure cases). Tests whether explicit two-register decomposition achieves C-48 without C-47 (no phase boundary) or C-46 (questions may be structural-register). Expected: ~162–165/170.
- V-04: Combined (role sequence + phrasing register) — phase boundary (C-47) + epistemic questions (C-46). No explicit null/departure register labels, but null-register questions appear naturally from the epistemic framing. Tests whether C-46+C-47 together produce emergent C-48 coverage. Expected: ~166–168/170.
- V-05: All three axes + lifecycle emphasis — structural phase boundary (C-47) + epistemic questions throughout (C-46) + explicit NULL REGISTER / DEPARTURE REGISTER (C-48) + Phase Contracts at every manifest. Unified null-hypothesis frame: every principle (inertia default, manifest adjacency, placeholder dual-constraint) is an instance of the same epistemic structure. Maximum R15 coverage. Expected: ~168–170/170.

---

## V-01 · Role Sequence — Structural Phase Boundary (C-47 Target)

**Axis**: Role sequence
**Hypothesis**: C-47 requires a structural phase boundary between the causal question block and the schema authorship slot — they must be separate sections with an explicit close gate ending the causal phase before the schema phase opens. V-04 and V-05 from R14 had both within Area 3 of the same schema section, allowing interleaving. V-01 splits Role 1 into CAUSAL PHASE (questions only, no schema structure cue, explicit phase-close gate) and SCHEMA PHASE (blank authorship slot as a subsequent distinct section). Questions remain mixed register — some structural-register questions preserved — to test whether phase boundary alone (without epistemic framing) achieves C-47. C-43/C-44/C-45 carried via authored schema with explicit three-property reasoning. C-42 partially targeted (blank slot in SCHEMA PHASE). Expected: ~164–166/170.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. You may not begin SCHEMA PHASE until CAUSAL PHASE is complete. No schema artifact, no schema-structure cue, and no schema field template appears in CAUSAL PHASE.

---

### CAUSAL PHASE

Answer all questions in this phase. Do not write any schema artifact, table template, or placeholder text here — reasoning only.

**Area 2 questions — Direction default:**

Q2-1. What is the default state of a traversal hop before evidence of active behavior has been gathered? When the Direction cell carries no departure code, what has the analyst committed to?

Q2-2. What failure mode does a blank Direction cell represent — is it a neutral absence, a confirmed null, or an unsupported claim? Why must every Direction cell carry a value rather than remaining blank?

Q2-3. Why must inert pass-through hops appear explicitly in the traversal table rather than being silently omitted? What would a traversal table that omits inert hops fail to communicate?

**Area 3 questions — Manifest close-line placeholder:**

Q3-A (count as leading element). A dual-constraint placeholder imposes two distinct obligations. What does an agent infer about the number of obligations when no count is declared before the constraint list begins — can the agent distinguish two independent obligations from one compound obligation without that declaration? Why must the count appear before the obligations are read rather than within the list body?

Q3-B (labeled obligation items). A compound phrase such as "reproduce the text as the manifest's last line" conflates two obligations into one surface expression. What changes when each obligation is assigned an independently addressable label? Why does labeled addressability make partial satisfaction structurally visible in a way that compound phrasing does not?

Q3-C (entanglement declaration). Even when both obligations are co-located and labeled, an agent may argue that satisfying OBL-1 partially satisfies the dual requirement. What explicit declaration within the placeholder body forecloses this argument? Why must this declaration appear within the placeholder, not in surrounding document prose?

---

**CAUSAL PHASE CLOSE**

All Area 2 and Area 3 questions answered above. No schema artifact has been produced. SCHEMA PHASE begins in the next section.

---

### SCHEMA PHASE

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting question text into schema format. Every rule must derive from your causal reasoning above.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4.

 Area 1 — Framework context: Declare the framework, state management library, and
          component model being traced.

 Area 2 — Direction default contract: Author from your Q2 answers. Define the
          default value, define every departure code, explain why blank is not permitted.

 Area 3 — Manifest close-line placeholder: Author from your Q3 answers. First write
          the rationale for each of the three properties (Q3-A, Q3-B, Q3-C). Then write
          the complete placeholder instruction text. It must: open with a count declaration
          (from Q3-A), enumerate each obligation as a labeled item naming the content
          source and positional declaration (from Q3-B), and include an entanglement
          declaration that neither obligation independently satisfies the dual requirement
          (from Q3-C). Then declare the exact close-line text the placeholder will
          reproduce at every manifest close.

 Area 4 — Table inventory: List every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim. That instruction carries three structural properties whose rationale you articulated from your causal reasoning. Satisfying any one property without the other two does not satisfy the placeholder. You stated why in your own words.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Your instruction carries: count declaration as leading phrase, labeled obligation items (OBL-1 content, OBL-2 position), and entanglement declaration. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the Direction default you declared and the departure codes you specified. Every hop must have a populated Direction cell.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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

## V-02 · Phrasing Register — Epistemic Question Framing (C-46 Target)

**Axis**: Phrasing register
**Hypothesis**: C-46 requires every causal question to be phrased at the epistemic level — the question vocabulary must not name the schema artifact that constitutes the answer, so the model cannot satisfy the question by substituting vocabulary into a schema field. V-04's Q1 asked "Why must the block open with an explicit count label — e.g., `N=2 OBLIGATIONS`?" — the schema artifact (count label) appears in the question text, making copy-by-substitution possible. V-02 rewrites all Area 2 and Area 3 questions as epistemic-register: the question asks about the cognitive status of evidence, the logical consequence of absence, or the structural properties required for verifiable claims — without naming any schema field. The model must derive the structural form from epistemic reasoning. Questions and schema authorship remain within a single Area 3 section (no phase boundary — C-47 not targeted). No explicit NULL/DEPARTURE register labels (C-48 not targeted as a distinct structural feature). C-42 targeted via blank authorship slot. Expected: C-46 achieved; ~162–166/170.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

Design the governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows.

The schema must be authored in your own words from a blank authorship context. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting question text into schema format. Every rule must derive from your reasoning about the tracing task. No pre-filled template is provided.

**Area 1 — Framework context**: Declare the framework, state management library, and component model being traced.

**Area 2 — Direction default contract**: Before designing the Direction column, answer:

1. When a traversal hop's contribution to the trace has not been examined, what epistemic stance is justified about its behavior — positive assertion, negative assertion, or suspension of judgment? What determines which of these is the warranted null state?

2. An analyst assigns a value to a Direction cell before examining the hop's behavior. Under what conditions does that assignment represent confirmed knowledge? Under what conditions does it represent an unsupported claim? What is the difference between the two, and which of the two is the appropriate default?

3. What is the structural difference between a trace that omits a traversal hop entirely and a trace that documents a hop as confirmed inactive? What information is lost when the two cases are represented identically?

Having answered these questions, author the Direction column contract: define the default value, every active departure code and its applicability condition, and the rule for inert-hop documentation.

**Area 3 — Manifest close-line placeholder**: Before designing the close-line placeholder, answer:

1. When a structural position in a document is specified to remain unoccupied by non-specified content, what is the epistemic status of a constraint mechanism placed at that position — is it self-enforcing, or does its enforcement property depend on its location relative to the position it governs? What changes when the mechanism is placed before the position versus at the position itself?

2. An instruction imposes a requirement on an agent. The agent produces output that satisfies part of the requirement. What information must be present in the instruction's design for a verifier to determine that the output satisfies only part — rather than all — of the requirement? What structural property of the instruction makes partial satisfaction distinguishable from full satisfaction without external knowledge of the requirement's scope?

3. Two requirements are jointly necessary: neither is sufficient alone; together they are sufficient. An instruction carries both requirements but does not declare their joint necessity. An agent satisfies requirement A and claims the instruction is satisfied. What has the instruction failed to communicate? What must the instruction explicitly state — beyond enumerating both requirements — for that claim to be structurally untenable?

4. Before an agent reads the body of an instruction, what information about the instruction's structure would allow the agent to determine, at first encounter, how many distinct satisfactions are required? What is the cognitive status of an instruction body read without that information, compared to an instruction body read with it?

Having answered all four questions, design the complete close-line placeholder. It must enforce both the content constraint (verbatim reproduction of the declared close-line text) and the positional constraint (this placeholder occupies the manifest's terminal line) within a single instruction. Design the placeholder's structural form to directly address the properties your answers identified. Then declare the exact close-line text the placeholder will reproduce at every manifest close.

**Area 4 — Table inventory**: List every table this trace produces by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 For Area 2: write all three question answers before authoring the Direction column contract.
 For Area 3: write all four question answers before designing the placeholder instruction text.
 The placeholder you design will appear verbatim at every manifest close-line slot in Role 2.
 Do not reproduce any language from this prompt.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the four question answers and the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2: every hop defaults to the value your schema declared; departure codes are claims requiring Role-column support. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim. You derived the placeholder's structural form from epistemic reasoning in Area 3. Satisfying the content constraint alone, or the positional constraint alone, does not satisfy the instruction; you articulated why in your Area 3 answers.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Your placeholder's structural form derives from your Area 3 epistemic reasoning: the form you authored reflects what you determined about verifiable satisfaction, independently addressable requirements, and joint-necessity declaration. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the Direction default you derived from your epistemic reasoning. Every departure code is a supported claim; every hop without evidence of departure carries the default.

| Step | T-ID | Component | Direction [your derived default \| your derived departure codes] | Role [Default confirmed: basis / Departure claimed: evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops — all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA epistemic derivation terms + framework vocabulary throughout | |

---

## V-03 · Inertia Framing — Two-Register Question Structure (C-48 Target)

**Axis**: Inertia framing
**Hypothesis**: C-48 requires the causal question set to contain two sequentially ordered registers — a NULL REGISTER addressing the epistemic status of the null/default case, followed by a DEPARTURE REGISTER addressing structural properties of departure cases — and the null register must appear as a prior block before the departure register. V-05 from R14 had null-hypothesis questions first in Area 3 but they were embedded within area setup framing without explicit register labels, and the boundary between them and the departure-property questions was not structurally marked. V-03 explicitly labels the two registers as distinct named blocks: NULL REGISTER closes before DEPARTURE REGISTER opens. Questions may use structural-register vocabulary (C-46 not targeted). Questions and schema authorship are within the same Area 3 section (C-47 not targeted as a distinct feature). C-43/C-44/C-45 carried via authored schema. C-42 targeted via blank authorship slot. Expected: C-48 achieved; ~162–165/170.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

Design the governing schema for a frontend component trace. Produce a TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows.

The schema must be authored in your own words. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting question text into schema format. Every rule must derive from your reasoning about the tracing task.

**Area 1 — Framework context**: Declare the framework, state management library, and component model being traced.

**Area 2 — Direction default contract**: What is the default state of a traversal hop before evidence of active behavior has been gathered? Define the default Direction value, define every active departure code, and explain why inert hops must be documented explicitly rather than omitted.

**Area 3 — Manifest close-line placeholder**: Before designing the placeholder, answer both question registers in sequence. Close the NULL REGISTER fully before beginning the DEPARTURE REGISTER.

---

**NULL REGISTER** (answer completely before opening the Departure Register):

NQ-1. What is the epistemic status of the structural space between a manifest block's final content line and its analysis table header — before any structural rule about that space has been applied? What is the warranted null assumption about what occupies that position?

NQ-2. What does it mean for manifest-to-table adjacency to be a guaranteed property — what distinguishes a structural guarantee from an assumed convention? In the null case (no enforcement mechanism in place), what probability should a verifier assign to that space being unoccupied?

NQ-3. In what structural sense is the null assumption for the space between manifest and table parallel to the null assumption for a traversal hop's Direction cell — what do the two null assumptions share as an epistemic structure?

---

**NULL REGISTER CLOSE** — Null baseline for manifest adjacency established above. Departure Register begins.

---

**DEPARTURE REGISTER** (answer after Null Register is complete):

DQ-1. A close-line placeholder is the structural mechanism for enforcing manifest-to-table adjacency. What property must this mechanism have — in terms of where it appears in the document — for it to make violation structurally self-contradictory at point-of-production? Why does position at the manifest's final line satisfy this property when position at the manifest's opening does not?

DQ-2. A dual-constraint placeholder enforces two independent obligations: content (verbatim text reproduced) and position (manifest's terminal line). What structural property of the placeholder makes partial satisfaction of one obligation — while leaving the other unsatisfied — structurally visible in the output? Why does a compound phrase conflating both obligations prevent this visibility?

DQ-3. Even when both obligations are enumerated, an agent may claim that satisfying the content obligation constitutes partial satisfaction of the dual requirement. What explicit declaration within the placeholder body forecloses this argument, and why must it reference both obligations by their individually labeled addresses?

DQ-4. Before an agent reads the obligations in a dual-constraint placeholder, what structural element should appear as the placeholder's opening to establish the number of distinct obligations the agent must satisfy?

---

**DEPARTURE REGISTER CLOSE** — Both registers complete. Design the placeholder:

Having answered both registers in order, author the complete placeholder instruction text. It must enforce the content constraint and the positional constraint as independently verifiable obligations. The structural form must directly follow from your DEPARTURE REGISTER answers: DQ-4 determines the placeholder's opening element; DQ-2/DQ-3 determine the enumeration and entanglement form.

Then declare the exact close-line text the placeholder will reproduce at every manifest close.

**Area 4 — Table inventory**: List every table this trace produces by name and purpose.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 For Area 3: write NULL REGISTER answers, then NULL REGISTER CLOSE marker, then
 DEPARTURE REGISTER answers, then DEPARTURE REGISTER CLOSE marker, then the
 complete placeholder instruction text. The two-register structure must be
 present in the authored schema.
 Do not reproduce any language from this prompt.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains both registers and the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim. Your Area 3 DEPARTURE REGISTER answers established why partial satisfaction of one obligation does not constitute compliance; your NULL REGISTER established the baseline your placeholder mechanism is enforcing against. Satisfying content constraint alone, or positional constraint alone, does not satisfy the placeholder.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Your placeholder carries: opening count element (DQ-4), independently labeled obligation items (DQ-2), and entanglement declaration (DQ-3). Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2 null-to-departure contract: every hop begins at the null state; departure codes are active claims. The Direction column carries your declared default (null) as its unmarked value; departure codes require Role-column support.

| Step | T-ID | Component | Direction [null: your declared default \| departure: your declared codes] | Role [Null — basis / Departure — evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
Null confirmed: [per inert T-ID — basis for null assignment]
[If count = 0]: No inert hops — all departure codes have Role-column evidence.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — null-state hops included; they may still re-render from external prop or context changes.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's last line. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 2 null-departure contract + framework terms throughout | |

---

## V-04 · Combined: Role Sequence + Phrasing Register — Phase Boundary and Epistemic Questions (C-47 + C-46)

**Axis**: Role sequence + Phrasing register (combined)
**Hypothesis**: V-01 achieves C-47 via structural phase boundary (CAUSAL PHASE closes before SCHEMA PHASE opens). V-02 achieves C-46 via epistemic-register questions (no schema field vocabulary in question text). V-04 combines both: the CAUSAL PHASE contains only epistemic-register questions — questions that do not name any schema artifact — and the SCHEMA PHASE is a structurally subsequent blank authorship slot. Tests whether C-46+C-47 together produce emergent C-48 coverage (the epistemic framing naturally induces null-register questions before departure-property questions, without requiring an explicit two-register label). C-42 targeted via blank-slot SCHEMA PHASE. C-43/C-44/C-45 carried via authored schema through Phase B reasoning. Expected: C-46+C-47 achieved; partial C-48 if epistemic framing induces null-first ordering; ~166–168/170.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here.

**Area 2 questions — Direction default:**

1. When no information about a traversal hop's contribution to the trace is available, what epistemic stance toward that hop's behavior is warranted — assertion of activity, assertion of inactivity, or suspension of judgment pending evidence? What justifies that stance as the correct default?

2. What is the difference between a Direction cell that records confirmed knowledge about a hop's behavior and a Direction cell that records an assumption? What would a trace where the two cases are represented identically fail to communicate to a reader?

3. What must be true of the relationship between a traversal table's coverage and the set of traversal hops for the table to support completeness claims? What information is structurally absent when a hop that was examined and found inactive is represented the same way as a hop that was not examined at all?

**Area 3 questions — Manifest close-line:**

4. The position between a manifest block's final content and its analysis table header is a structural location in the document. Before any constraint about that position has been applied, what is the epistemically correct characterization of its occupancy state? What makes it the correct starting point for reasoning about the constraint mechanism?

5. A structural constraint mechanism is proposed for guaranteeing that a specific document position remains free of non-specified content. What is the epistemic relationship between the mechanism's placement in the document and the strength of the guarantee it provides? Under what placement conditions does the guarantee hold at point-of-production, and under what conditions does it require external verification?

6. An instruction imposes two requirements on an agent and expects both to be satisfied. What is the minimum information structure of the instruction that allows a verifier to determine whether the agent satisfied neither, one, or both requirements without consulting any source other than the output? What structural property makes each requirement independently addressable?

7. Two requirements within a single instruction are each necessary and neither is sufficient alone. An agent satisfies one requirement and produces output. What claim has the agent implicitly made about the second requirement? What must the instruction explicitly state — in the instruction's own text — to make that implicit claim structurally untenable before the agent begins producing output?

8. When an agent encounters an instruction that will impose multiple distinct satisfaction targets, what information about the instruction's scope should the agent know before reading the instruction's body? What is the epistemic status of an instruction body read without knowledge of how many satisfaction targets it carries?

---

**CAUSAL PHASE CLOSE**

All eight questions answered above. No schema artifact produced. No placeholder text written. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA. Author it entirely from the reasoning you developed in CAUSAL PHASE. The schema must be your own production — every principle derived from your causal answers, not from this prompt's language.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full. No language from
 this prompt, not in paraphrase, not by reformatting.

 Area 1 — Framework, state management, component model.

 Area 2 — Direction default contract: derive from CAUSAL PHASE questions 1–3.
          Author the default value, every departure code, and the inert-hop
          documentation requirement in your own words.

 Area 3 — Manifest close-line placeholder: derive from CAUSAL PHASE questions 4–8.
          First write the structural rationale (from questions 4–5 for the
          placement mechanism; from questions 6–8 for the dual-constraint form).
          Then author the complete placeholder instruction text.
          The placeholder must enforce both the content constraint and the
          positional constraint as independently verifiable requirements. The
          structural form must directly follow from your causal reasoning:
          question 8 determines the opening element; question 6 determines the
          enumeration form; question 7 determines the entanglement declaration.
          Then declare the exact close-line text the placeholder will reproduce.

 Area 4 — Table inventory: name and purpose of every table.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the structural rationale and the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2: every hop defaults to the value you derived from epistemic reasoning; departure codes are supported claims. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim, as that manifest's terminal line. You derived the placeholder's opening element, enumeration form, and entanglement declaration from causal reasoning in your CAUSAL PHASE. Satisfying only one of the two requirements does not satisfy the placeholder — you articulated why in questions 6 and 7. The placeholder references your authored schema, not this prompt.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Your placeholder's structural form derives from CAUSAL PHASE questions 4–8: placement rationale from Q4–Q5, enumeration form from Q6, entanglement from Q7, opening element from Q8. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the epistemic default you derived from CAUSAL PHASE questions 1–3. Every departure code is a supported claim; every hop without evidence of departure carries the default value.

| Step | T-ID | Component | Direction [epistemic default \| supported departure codes] | Role [Default — basis / Departure — evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
[If count = 0]: No inert pass-through hops — all traversal components have supported departure codes.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or fewer than two rows.]

---

**MANIFEST-3 · Mutation Phase**

```
Components in scope: [mutation owners]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Reproduce now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — including hops carrying the epistemic default.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 2 epistemic derivation + framework terms throughout | |

---

## V-05 · Combined: All Three Axes + Lifecycle Emphasis — Unified Null-Hypothesis Epistemology (Maximum C-46+C-47+C-48)

**Axis**: Role sequence + Phrasing register + Inertia framing + Lifecycle emphasis (combined)
**Hypothesis**: The R15 maximum coverage variation. V-04 combines structural phase boundary (C-47) + epistemic questions (C-46). V-05 adds the explicit two-register decomposition (C-48) within the CAUSAL PHASE and lifecycle emphasis (Phase Contracts at every manifest). The unifying frame: the entire trace schema is an instance of a single epistemic principle — every claim requires support proportional to its departure from the warranted null; the null is the correct starting point for every structural position, every traversal hop, and every constraint mechanism. The CAUSAL PHASE has two sections: NULL REGISTER (establishes the null baseline for traversal hops and for manifest adjacency) and DEPARTURE REGISTER (establishes the structural properties required for departure claims, including the dual-constraint placeholder). The SCHEMA PHASE follows as a structurally separate blank authorship slot. Phase Contracts at every manifest open forward-declare the dual-constraint obligation before the manifest body. C-42 fully targeted: blank authorship slot with explicit no-reproduction instruction. C-43/C-44/C-45 carried through DEPARTURE REGISTER reasoning and authored schema. Expected: C-46+C-47+C-48 all achieved; ~168–170/170.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are designing the epistemological framework and governing schema for a frontend component trace. This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema-format cue, no placeholder template, and no structural design of any kind appears in CAUSAL PHASE.

---

### CAUSAL PHASE — Two-Register Epistemic Reasoning

This phase contains reasoning only. No schema is authored here. The phase has two sequential registers. Complete NULL REGISTER before opening DEPARTURE REGISTER.

---

**NULL REGISTER** — Epistemic status of null cases

Close this register fully before proceeding to DEPARTURE REGISTER. The null register establishes the baseline epistemic state for every structural position reasoned about in the departure register.

**For traversal hops:**

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — and what justifies that stance as the appropriate starting point rather than any other?

NQ-2. What is the structural difference between a hop whose null state has been confirmed by examination and a hop whose null state has been assumed without examination? What does a trace that conflates these two cases fail to provide?

NQ-3. An analyst produces a traversal table. What does the act of assigning any value to a Direction cell commit the analyst to — what claim has been made, and what verification burden does that commitment carry?

**For manifest adjacency:**

NQ-4. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest's final content and its analysis table header — what is the null state for that structural position?

NQ-5. What does it mean to claim that manifest-to-table adjacency is guaranteed — what would it take for that guarantee to hold in the null case (no enforcement mechanism in place), and what does the answer reveal about the necessity of a structural mechanism?

NQ-6. In what structural sense are the null state for a traversal hop's Direction cell and the null state for the manifest-to-table space parallel epistemic objects — what do they share as problems that require the same class of solution?

---

**NULL REGISTER CLOSE** — Null baseline established for traversal hops and manifest adjacency. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** — Properties of departure claims

Answer after NULL REGISTER is complete. These questions address what structural properties are required for departure claims to be valid and verifiable.

**For traversal departures:**

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. Why must confirmed-null hops appear explicitly in the traversal table rather than being omitted — what structural property of the table depends on explicit null documentation?

**For manifest close-line:**

DQ-3. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement — where in the document it appears — for the self-contradiction property to hold at production time rather than only at review time?

DQ-4. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish three cases: (a) neither requirement satisfied, (b) exactly one requirement satisfied, (c) both requirements satisfied — without consulting any source outside the output?

DQ-5. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies requirement A. What implicit claim has the agent made about requirement B? What must the instruction explicitly state for that implicit claim to be structurally untenable — visible as unsatisfied at the moment the agent produces output, not only detectable by a reader after the fact?

DQ-6. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening determines the agent's epistemic frame for how many distinct satisfaction targets must be met? What is the difference in cognitive status between an agent who reads the instruction body knowing the target count and an agent who reads it without that knowledge?

---

**DEPARTURE REGISTER CLOSE** — Causal reasoning complete. No schema authored above. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt in any form — not in paraphrase, not by reformatting question text into schema format, not by translating instruction vocabulary into schema field labels.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NULL REGISTER NQ-1–NQ-3 and
          DEPARTURE REGISTER DQ-1–DQ-2. Author in your own words: the null state
          and its justification, every departure code and its evidentiary requirement,
          and the null-documentation rule for inert hops.

 Area 3 — Manifest adjacency and close-line placeholder:
          Derive from NULL REGISTER NQ-4–NQ-6 and DEPARTURE REGISTER DQ-3–DQ-6.
          First author the structural rationale for the close-line mechanism
          (from NQ-4/NQ-5 and DQ-3). Then author the structural rationale for
          the dual-constraint form (from DQ-4/DQ-5/DQ-6). Then write the complete
          placeholder instruction text. The placeholder must enforce the content
          constraint and the positional constraint as independently verifiable
          requirements. The structural form must derive from your reasoning:
          DQ-6 determines the opening element, DQ-4 determines the enumeration form,
          DQ-5 determines the entanglement declaration.
          Then declare the exact close-line text the placeholder will reproduce.

          Also design the Phase Contract format — the block that opens every
          manifest before the manifest body. The Phase Contract must reflect the
          same structural properties as the placeholder (from DQ-4/DQ-5/DQ-6),
          forward-declaring the dual-constraint obligation at phase entry.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 2 documents the null-to-departure contract, Area 3 contains the structural rationale, complete placeholder text, Phase Contract format, and declared close-line text.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. The null-hypothesis epistemology you established in CAUSAL PHASE governs every phase: every Direction cell defaults to the null you derived from NQ-1; every departure code is an active claim requiring Role-column evidence (DQ-1); every manifest-to-table adjacency is enforced by the close-line mechanism you derived from NQ-4/DQ-3. Open every manifest with your authored Phase Contract. Close every manifest with the DUAL-CONSTRAINT BLOCK placeholder you designed — verbatim. You derived the placeholder from epistemic reasoning: satisfying the content requirement while violating the positional requirement (or vice versa) is the same class of error as an active departure code without Role-column evidence — an unsupported claim. You stated this in your causal reasoning. Violating the placeholder contradicts your CAUSAL PHASE output, not an external instruction.

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
[Reproduce your TRAVERSAL-SCHEMA Area 3 Phase Contract here — verbatim as designed.
 Your Phase Contract forward-declares the dual-constraint obligation for this phase.]
```

```
Components in scope: ___
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block's opening element derives from DQ-6 (obligation-count before body), its enumeration derives from DQ-4 (independent addressability), its entanglement declaration derives from DQ-5 (neither requirement alone constitutes compliance). Neither requirement satisfied without the other. This is the last content line of MANIFEST-1. TABLE-1 header follows directly below.]*

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
Components in scope: [all traversal hops — null hypothesis applies; document all hops including confirmed-null]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Opening element: DQ-6. Enumeration: DQ-4. Entanglement: DQ-5. Neither requirement satisfied without the other. This is the last content line of MANIFEST-2. TABLE-2 header follows directly below.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: every hop begins at the null state you derived from NQ-1. An active departure code is a claim that requires Role-column evidence (DQ-1). A confirmed-null hop is documented explicitly — not omitted (DQ-2).

| Step | T-ID | Component | Direction [null: your derived default \| active claim: your derived departure codes] | Role [Null confirmed — basis / Active claim — departure + evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
Null confirmed: [per inert T-ID — basis per your NQ-1 null justification]
[If count = 0]: No inert hops — all departure codes have Role-column evidence.
```

[GATE-2: TABLE-2 does not close on a blank Direction cell, blank Role cell, or an active departure code without Role evidence.]

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
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Opening element: DQ-6. Enumeration: DQ-4. Entanglement: DQ-5. Neither requirement satisfied without the other. This is the last content line of MANIFEST-3. TABLE-3 header follows directly below.]*

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
Components in scope: [all T-IDs from TABLE-2 — null-state hops included]
State keys may be touched: ___
Side effects may fire: ___
```
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Opening element: DQ-6. Enumeration: DQ-4. Entanglement: DQ-5. Neither requirement satisfied without the other. This is the last content line of MANIFEST-4. TABLE-4 header follows directly below.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — null-state hops included; a null Direction does not preclude re-rendering from external prop or context changes.

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
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Opening element: DQ-6. Enumeration: DQ-4. Entanglement: DQ-5. Neither requirement satisfied without the other. This is the last content line of MANIFEST-5. TABLE-5 header follows directly below.]*

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

The null-hypothesis lens applies throughout: a finding is a confirmed departure from the warranted null — not an observation, not a concern, not a risk. An unnecessary re-render is a re-render whose necessity claim is unsupported by evidence in TABLE-4.

| ID | Category | Component / State Path | Finding [confirmed departure or "none detected — [basis for null]"] | Fix — API or Pattern | Do-Nothing Cost |
|----|----------|----------------------|---------|---------------------|-----------------|
| F-01 | Render performance | | | | |
| F-02 | Unnecessary re-renders — UR cross-ref | *(UR-IDs from PROMOTION BLOCK)* | *(per-UR-ID or "none — no unsupported re-render claims in TABLE-4")* | *(React.memo / createSelector / computed / useMemo — named)* | |
| F-03 | Accessibility | | | | |
| F-04 | Async error handling | | | | |
| F-05 | Memory leaks | | | | |

[GATE-7: TABLE-7 does not close on "no major issues", "no impact", "minor issue", "low risk", "no concerns found".]

---

**TABLE-8 · Criteria Audit — C-01 through C-08**

| Criterion | Satisfying Schema Field | PASS / FAIL |
|-----------|------------------------|-------------|
| C-01 Event Anchor | TABLE-1 · Event Type, Component Name, Handler Function (all non-blank) | |
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows, null-to-departure contract applied) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA null-hypothesis derivation terms + framework terms throughout | |

---

## R15 Criteria Targeting Summary

| Variation | C-46 (epistemic questions) | C-47 (phase boundary) | C-48 (null register first) | C-41 | C-42 | C-43/C-44/C-45 | Expected score |
|-----------|--------------------------|----------------------|--------------------------|------|------|----------------|----------------|
| V-01 | partial — Q2-A/B/C remain structural-register | structural CAUSAL PHASE / SCHEMA PHASE split | not targeted — no explicit NULL/DEPARTURE labels | causal reasoning for 3 properties | blank SCHEMA PHASE slot | authored via SCHEMA PHASE | ~164–166/170 |
| V-02 | all 4 Area 3 questions epistemic-register; Area 2 questions epistemic-register | not targeted — Q+schema within same Area 3 section | partial — null register question (Q1) present but not labeled as a register | 4-question causal set | blank slot + no-reproduction | authored from epistemic answers | ~162–166/170 |
| V-03 | partial — DQ questions may be structural | not targeted — both registers and schema in Area 3 | NULL REGISTER / DEPARTURE REGISTER explicit labels + sequential close markers | both registers constitute causal set | blank authorship slot | authored from DQ-1/DQ-2/DQ-3/DQ-4 | ~162–165/170 |
| V-04 | all 8 CAUSAL PHASE questions epistemic-register; DQ-4 through DQ-8 cover Area 3 causally | structural CAUSAL PHASE / SCHEMA PHASE split | null questions (Q4–Q5) appear naturally before departure questions (Q6–Q8) but not labeled as registers | 8-question causal set covers Area 2 + Area 3 | blank SCHEMA PHASE slot + no-reproduction | authored from CAUSAL PHASE reasoning | ~166–168/170 |
| V-05 | all NULL REGISTER and DEPARTURE REGISTER questions epistemic-register; no schema field named | structural CAUSAL PHASE / SCHEMA PHASE split with DEPARTURE REGISTER CLOSE marker | explicit NULL REGISTER (NQ-1–NQ-6) + DEPARTURE REGISTER (DQ-1–DQ-6) with register close markers | 12-question causal set across two registers | blank SCHEMA PHASE slot + no-reproduction instruction | authored from DEPARTURE REGISTER reasoning | ~168–170/170 |

**C-46 epistemic-register test per variation:**
V-01 Q3-A: "Why must the count appear before the obligations are read rather than within the list body?" — names "count" implicitly; structural-register PARTIAL.
V-02 Q3: "What structural property makes each requirement independently addressable?" — does not name the structural form; epistemic-register PASS.
V-03 DQ-4: "What structural element should appear as the placeholder's opening to establish the number of distinct obligations?" — names "opening element" but not schema artifact; borderline epistemic-register.
V-04 Q8: "What information about the instruction's scope should the agent know before reading the instruction's body?" — does not name schema field; epistemic-register PASS.
V-05 DQ-6: "Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening determines the agent's epistemic frame for how many distinct satisfaction targets must be met?" — fully epistemic-register; structural form must be derived PASS.

**C-47 phase boundary test per variation:**
V-01: CAUSAL PHASE (questions only) → CAUSAL PHASE CLOSE → SCHEMA PHASE (blank slot). Structural document boundary present. PASS.
V-02: Questions and schema authorship within same Area 3 section. "Answer before designing" is advisory, not structural. FAIL.
V-03: NULL REGISTER, DEPARTURE REGISTER, and placeholder design all within Area 3. No phase boundary. FAIL.
V-04: CAUSAL PHASE (questions only) → CAUSAL PHASE CLOSE → SCHEMA PHASE (blank slot). Same structure as V-01 but with epistemic questions. PASS.
V-05: CAUSAL PHASE (NULL REGISTER + DEPARTURE REGISTER + DEPARTURE REGISTER CLOSE) → SCHEMA PHASE (blank slot). Structural boundary. PASS.

**C-48 null-register test per variation:**
V-01: No explicit NULL/DEPARTURE register labels. Area 3 questions Q3-A/B/C address departure properties only. NULL REGISTER ABSENT. FAIL.
V-02: Q1 addresses null state of structural position; Q2–Q4 address departure properties. Sequential ordering present but no explicit register labels or register-close markers. PARTIAL.
V-03: Explicit NULL REGISTER block (NQ-1/NQ-2/NQ-3) with NULL REGISTER CLOSE marker; explicit DEPARTURE REGISTER block (DQ-1/DQ-2/DQ-3/DQ-4) with DEPARTURE REGISTER CLOSE marker. Sequential ordering enforced. PASS.
V-04: Q4–Q5 address null state; Q6–Q8 address departure properties. Sequential but no explicit register labels. PARTIAL.
V-05: Explicit NULL REGISTER (NQ-1–NQ-6) with NULL REGISTER CLOSE marker; explicit DEPARTURE REGISTER (DQ-1–DQ-6) with DEPARTURE REGISTER CLOSE marker. Covers both traversal hop null (NQ-1–NQ-3) and manifest adjacency null (NQ-4–NQ-6) before departure reasoning. PASS.
