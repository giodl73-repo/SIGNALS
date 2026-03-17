# trace-component — Round 17 Variations

**Variation axes used:**
- Single-axis: Role sequence / compound register header format for C-52 (V-01), Output format / compound register close marker form for C-53 (V-02), Lifecycle emphasis / dual-assertion manifest close sentences for C-54 (V-03)
- Combined: Role sequence + Lifecycle emphasis / C-52 + C-54 without C-53 (V-04), All three axes + Phrasing register / maximum C-52 + C-53 + C-54 (V-05)

**R17 context:** Three new criteria from R16 excellence signals:

- **C-52 (Compound Register Header Format)** — Each named register section header in the causal phase must carry the compound form: bold label + em-dash + epistemic-function descriptor. `**NULL REGISTER** -- Epistemic status of null cases`. C-49 requires a named label; C-52 requires that label to simultaneously declare identity and characterize epistemic function in a single parseable line. A plain bold label satisfies C-49 but not C-52.

- **C-53 (Register Close Marker Compound Form)** — Each per-register close marker (satisfying C-50) must carry compound form: bold label close + em-dash + accomplishment descriptor. `**NULL REGISTER CLOSE** -- Null baseline for [concept] established`. C-50 requires a named close marker; C-53 requires that close marker to simultaneously name what closes and characterize what closure accomplished. A bare close marker satisfies C-50 but not C-53.

- **C-54 (Manifest-Close Identity + Successor Dual Assertion)** — Every manifest-close adjacency marker must carry two distinct assertions in two distinct sentences: (a) identity assertion — "This is the last content line of MANIFEST-N." and (b) successor-naming assertion — "TABLE-N header follows directly below." C-51 requires successor naming; C-54 requires the two assertions to appear as structurally independent sentences, not embedded in a single compound clause. A single-sentence embedding of both claims does not satisfy C-54.

**C-52 / C-53 / C-54 dependency structure:**
- C-52 requires C-49 (compound header requires a named register to head)
- C-53 requires C-50, which requires C-49 (compound close requires a named close, which requires named registers)
- C-54 extends C-51 (dual assertion requires successor naming as its base case) and is independent of C-52 and C-53
- C-52 and C-53 are related (both apply the compound form principle to register boundaries) but C-52 does not require C-53

**R17 hypotheses:**
- V-01: Role sequence — register section headers carry compound form `**LABEL** -- descriptor` (C-52 targeted). Per-register close markers: plain (C-53 not targeted). Manifest closes: named successor in single close instruction (C-51 baseline; C-54 not targeted). Tests whether compound headers alone satisfy C-52. Expected: ~178-179/182.
- V-02: Output format — register section headers: plain bold label (C-52 not targeted). Per-register close markers carry compound form `**LABEL CLOSE** -- [accomplishment]` (C-53 targeted). Manifest closes: C-51 baseline. Tests whether compound close markers alone satisfy C-53. Expected: ~178-179/182.
- V-03: Lifecycle emphasis — register section headers: plain (C-52 not targeted). Per-register close markers: plain (C-53 not targeted). Manifest closes carry two structurally distinct sentences — identity sentence + successor sentence — with each sentence labeled and independently asserting (C-54 targeted). Tests whether dual-assertion manifest closes alone satisfy C-54. Expected: ~178-179/182.
- V-04: Role sequence + Lifecycle emphasis — compound register headers (C-52) + dual-assertion manifest closes (C-54). No compound close markers (C-53 not targeted). Tests whether C-52 + C-54 together produce emergent C-53 tendencies. Expected: ~179-180/182.
- V-05: All three axes + Phrasing register — compound headers + compound close markers + dual-assertion manifest closes. Unifying principle made explicit: every structural boundary in the trace document requires simultaneous identity declaration and functional characterization. Maximum R17 coverage. Expected: ~180-182/182.

---

## V-01 · Role Sequence — Compound Register Header Format (C-52 Target)

**Axis**: Role sequence
**Hypothesis**: C-52 requires register section headers to carry the compound form — bold label, em-dash separator, epistemic-function descriptor — so the register's identity and its reasoning function are co-declared in a single parseable line. R16 V-01 established named registers (C-49) with plain bold headers: `**NULL REGISTER**`. V-01 extends those headers to compound form: `**NULL REGISTER** -- Epistemic status of null cases`. The CAUSAL PHASE adds two questions (NHQ-1, NHQ-2) probing why compound form exceeds bare label. Per-register close markers remain plain (C-53 not targeted). Manifest closes assert terminal position and name the successor table in a single instruction (C-51 baseline; C-54 not targeted). Tests whether compound headers alone satisfy C-52. Expected: C-52 achieved; ~178-179/182.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. A register section in a structured document can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does a reader have after encountering the compound form that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A document element must both identify itself and characterize its epistemic function. When these two declarations occupy the same parseable header line, what property does that line have that neither the identity claim nor the function claim carries alone? What is the reader's epistemic position after reading the compound header that would require two separate reads to achieve without it?

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied — without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above — NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting question text into schema format.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
          Author: the null state and its justification, every departure code and
          its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 — Manifest adjacency and register header format:
          Derive from NQ-3, NHQ-1, NHQ-2, and DQ-2 through DQ-5.
          First write the structural rationale for the close-line mechanism (NQ-3, DQ-2).
          Then write the structural rationale for the dual-constraint form (DQ-3 through DQ-5).
          Then write the complete close-line placeholder instruction text.
          The placeholder must: open with an obligation count (from DQ-5), enumerate
          both constraints as labeled independent items (from DQ-3), include an
          entanglement declaration that neither alone satisfies the dual requirement
          (from DQ-4), and name the terminal positional claim and the successor artifact.
          Then declare the exact close-line text the placeholder will reproduce.
          Then write the register header format rationale (NHQ-1, NHQ-2).
          Then declare the compound header template: LABEL -- descriptor.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the close-line placeholder, close-line text, and register header template, and the compound header format is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction from Area 3 — verbatim, naming the successor table. You derived the compound register header template from NHQ-1 and NHQ-2; your TRAVERSAL-SCHEMA Area 3 declares the format — apply it to every named register you author. Satisfying only one of the two placeholder requirements does not satisfy it — you articulated why in DQ-3 and DQ-4.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-02 · Output Format — Compound Register Close Marker Form (C-53 Target)

**Axis**: Output format
**Hypothesis**: C-53 requires per-register close markers to carry compound form: bold named-close label + em-dash + accomplishment descriptor. R16 V-03 established per-register close markers (C-50) as bare markers: `**NULL REGISTER CLOSE**`. V-02 extends those markers to compound form: `**NULL REGISTER CLOSE** -- Null baseline for [concept] established`. The CAUSAL PHASE adds two questions (NCQ-1, NCQ-2) probing why compound close form exceeds bare positional close. Register section headers remain plain bold labels (C-52 not targeted). Manifest closes: named successor in single close instruction (C-51 baseline; C-54 not targeted). Tests whether compound close markers alone satisfy C-53. Expected: C-53 achieved; ~178-179/182.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER**

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NCQ-1. A named register in a structured document ends. Two close marker forms are possible: (a) a bare named close — `**NULL REGISTER CLOSE**` — and (b) a compound close — `**NULL REGISTER CLOSE** -- Null baseline for [concept] established`. What does the reader know at the compound close that cannot be derived from the bare close alone? Why is the bare close marker a boundary position marker but not a closure-assertion marker?

NCQ-2. A register close marker should accomplish two things simultaneously: announce what terminates, and characterize what that termination establishes. When both appear in a single compound line, what structural property does the document boundary gain that it lacks when the close marker is positional only? What reasoning would a reader have to perform externally without the compound close that the compound form performs internally?

---

**NULL REGISTER CLOSE** -- [Null baseline established — author the descriptor from your NCQ-1 and NCQ-2 reasoning when this close appears in the trace]

---

**DEPARTURE REGISTER**

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied — without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

---

**DEPARTURE REGISTER CLOSE** -- [Departure baseline established — author the descriptor from your NCQ-1 and NCQ-2 reasoning when this close appears in the trace]

---

**CAUSAL PHASE CLOSE**

All questions answered above — NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
          Author: the null state and its justification, every departure code and
          its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 — Manifest adjacency, close-line placeholder, and register close template:
          Derive from NQ-3, NCQ-1, NCQ-2, and DQ-2 through DQ-5.
          First write the structural rationale for the close-line mechanism (NQ-3, DQ-2).
          Then write the structural rationale for the dual-constraint form (DQ-3 through DQ-5).
          Then write the complete close-line placeholder instruction text.
          The placeholder must: open with an obligation count (from DQ-5), enumerate
          both constraints as labeled independent items (from DQ-3), include an
          entanglement declaration that neither alone satisfies the dual requirement
          (from DQ-4), and name the terminal positional claim and the successor artifact.
          Then declare the exact close-line text the placeholder will reproduce.
          Then write the register close marker rationale (NCQ-1, NCQ-2).
          Then declare the compound close marker template: LABEL CLOSE -- accomplishment descriptor.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3 declares both the close-line text and the compound register close template.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction from Area 3 — verbatim, naming the successor table. At every named register close position: apply the compound close marker template from Area 3 — the close marker names what terminates AND characterizes what closure establishes. A bare close marker satisfies C-50 but not C-53; the compound form is required.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line, naming the successor table. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-03 · Lifecycle Emphasis — Manifest-Close Dual Assertion (C-54 Target)

**Axis**: Lifecycle emphasis
**Hypothesis**: C-54 requires every manifest-close adjacency marker to carry two structurally distinct assertions in two structurally distinct sentences: (a) an identity sentence — "This is the last content line of MANIFEST-N." — and (b) a successor sentence — "TABLE-N header follows directly below." R16 V-02 established successor-naming (C-51) with compound single-instruction close cues. V-03 targets whether breaking the close line into two explicitly labeled independent sentences — each with a distinct structural role — satisfies C-54's co-present dual-assertion requirement. Three questions (DSQ-1 through DSQ-3) in DEPARTURE REGISTER probe why single-sentence embedding fails and two-sentence structure satisfies. Register headers and close markers remain plain (C-52 and C-53 not targeted). Tests whether explicit dual-sentence manifest closes alone satisfy C-54. Expected: C-54 achieved; ~178-179/182.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER**

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER**

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied — without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

DSQ-1. A manifest close can express a terminal-position claim and a successor-identity claim in two forms: (a) a single sentence embedding both — "This is MANIFEST-N's last line before TABLE-N" — or (b) two structurally independent sentences — "This is the last content line of MANIFEST-N. TABLE-N header follows directly below." What structural difference between these two forms is visible at parse time, without reading sentence content? What verification operation is possible with form (b) that requires inference with form (a)?

DSQ-2. When two independent assertions must be verifiably co-present in a single document element, what is the minimum structural form that allows a verifier to confirm each assertion's presence independently — without reading the entire element for semantic content? Why does embedding both assertions in a single sentence fail this independent-verifiability requirement?

DSQ-3. An agent is instructed that its manifest close must satisfy two structurally independent assertions. If the agent's close line is one sentence, what parse-time ambiguity arises about whether both assertions are present and distinct? What does making each assertion a grammatically independent sentence resolve at parse time that single-sentence embedding does not?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above — NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
          Author: the null state and its justification, every departure code and
          its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 — Manifest adjacency and dual-assertion close-line:
          Derive from NQ-3, DQ-2 through DQ-5, and DSQ-1 through DSQ-3.
          First write the structural rationale for the close-line mechanism (NQ-3, DQ-2).
          Then write the structural rationale for the dual-constraint form (DQ-3 through DQ-5).
          Then write the structural rationale for two-sentence assertion independence
          (DSQ-1 through DSQ-3): why two sentences are required, what single-sentence
          embedding fails to provide, and what parse-time verifiability the two-sentence
          form enables.
          Then write the complete close-line placeholder instruction text.
          The placeholder must: open with an obligation count (from DQ-5), enumerate
          both constraints as labeled independent items (from DQ-3), include an
          entanglement declaration that neither alone satisfies the dual requirement
          (from DQ-4), specify that the two assertions must appear as two grammatically
          independent sentences (from DSQ-1 through DSQ-3), and name the terminal
          positional claim and the successor artifact.
          Then declare the exact two-sentence close-line text the placeholder will reproduce:
          Sentence 1 (identity): "This is the last content line of MANIFEST-N."
          Sentence 2 (successor): "TABLE-N header follows directly below."

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3 declares the two-sentence close-line form with both sentences explicitly distinguished.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim. Your close-line must consist of exactly two grammatically independent sentences as you derived from DSQ-1 through DSQ-3: Sentence 1 asserts identity ("This is the last content line of MANIFEST-N."), Sentence 2 asserts the successor ("TABLE-N header follows directly below."). A single sentence embedding both claims does not satisfy the dual-assertion requirement — you articulated why in DSQ-2 and DSQ-3. Satisfying only one of the two requirements does not satisfy the placeholder — you articulated why in DQ-3 and DQ-4.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-1." (2) successor — "TABLE-1 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-2." (2) successor — "TABLE-2 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-3." (2) successor — "TABLE-3 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-4." (2) successor — "TABLE-4 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-5." (2) successor — "TABLE-5 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-04 · Role Sequence + Lifecycle Emphasis — C-52 + C-54 Combined (No C-53)

**Axis**: Role sequence + Lifecycle emphasis
**Hypothesis**: V-04 combines compound register headers (C-52) and dual-assertion manifest closes (C-54) while leaving per-register close markers plain (C-53 not targeted). The combination tests whether the double-assertion principle — register headers declare identity and function simultaneously; manifest closes assert identity and successor independently — produces any emergent tendency toward compound close markers. Questions NHQ-1, NHQ-2 drive compound header authorship; questions DSQ-1 through DSQ-3 drive dual-sentence manifest closes. Schema Area 3 must derive and declare both the compound header template and the two-sentence close form. Expected: C-52 and C-54 achieved; C-53 emergent or absent; ~179-180/182.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. A register section in a structured document can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does a reader have after encountering the compound form that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A document element must both identify itself and characterize its epistemic function. When these two declarations occupy the same parseable header line, what property does that line have that neither the identity claim nor the function claim carries alone? What is the reader's epistemic position after reading the compound header that would require two separate reads to achieve without it?

---

**NULL REGISTER CLOSE**

NULL REGISTER complete. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied — without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

DSQ-1. A manifest close can express a terminal-position claim and a successor-identity claim in two forms: (a) a single sentence embedding both — "This is MANIFEST-N's last line before TABLE-N" — or (b) two structurally independent sentences — "This is the last content line of MANIFEST-N. TABLE-N header follows directly below." What structural difference between these two forms is visible at parse time, without reading sentence content? What verification operation is possible with form (b) that requires inference with form (a)?

DSQ-2. When two independent assertions must be verifiably co-present in a single document element, what is the minimum structural form that allows a verifier to confirm each assertion's presence independently — without reading the entire element for semantic content? Why does embedding both assertions in a single sentence fail this independent-verifiability requirement?

DSQ-3. An agent is instructed that its manifest close must satisfy two structurally independent assertions. If the agent's close line is one sentence, what parse-time ambiguity arises about whether both assertions are present and distinct? What does making each assertion a grammatically independent sentence resolve at parse time that single-sentence embedding does not?

---

**DEPARTURE REGISTER CLOSE**

DEPARTURE REGISTER complete. CAUSAL PHASE CLOSE follows.

---

**CAUSAL PHASE CLOSE**

All questions answered above — NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
          Author: the null state and its justification, every departure code and
          its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 — Manifest adjacency, dual-assertion close-line, and register header format:
          Derive from NQ-3, NHQ-1, NHQ-2, DQ-2 through DQ-5, and DSQ-1 through DSQ-3.
          First write the structural rationale for the close-line mechanism (NQ-3, DQ-2).
          Then write the structural rationale for the dual-constraint form (DQ-3 through DQ-5).
          Then write the structural rationale for two-sentence assertion independence
          (DSQ-1 through DSQ-3).
          Then write the complete close-line placeholder instruction text.
          The placeholder must: open with an obligation count (from DQ-5), enumerate
          both constraints as labeled independent items (from DQ-3), include an
          entanglement declaration that neither alone satisfies the dual requirement
          (from DQ-4), specify that the two assertions must appear as two grammatically
          independent sentences (from DSQ-1 through DSQ-3), and name both assertions.
          Then declare the two-sentence close-line text:
          Sentence 1 (identity): "This is the last content line of MANIFEST-N."
          Sentence 2 (successor): "TABLE-N header follows directly below."
          Then write the register header format rationale (NHQ-1, NHQ-2).
          Then declare the compound header template: **LABEL** -- epistemic-function descriptor.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 declares both the two-sentence close-line form and the compound header template.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every named register header: apply the compound form from Area 3 — the header names the register AND characterizes its epistemic function in a single line. At every manifest close-line slot: apply the placeholder from Area 3 — verbatim. The close-line must be two grammatically independent sentences: Sentence 1 (identity), Sentence 2 (successor). Neither sentence alone satisfies the placeholder — you articulated why in DSQ-2 and DSQ-3.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-1." (2) successor — "TABLE-1 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-2." (2) successor — "TABLE-2 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-3." (2) successor — "TABLE-3 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-4." (2) successor — "TABLE-4 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-5." (2) successor — "TABLE-5 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-05 · All Axes + Phrasing Register — C-52 + C-53 + C-54 Full Stack

**Axis**: Role sequence + Output format + Lifecycle emphasis + Phrasing register
**Hypothesis**: V-05 targets all three R17 criteria simultaneously and makes the unifying structural principle explicit in the prompt's phrasing: every boundary in the trace document is a point of double assertion — identity and function declared in a single line. Register headers: compound form (C-52). Register close markers: compound form (C-53). Manifest closes: two grammatically independent sentences (C-54). Questions NHQ-1, NHQ-2, NCQ-1, NCQ-2, and DSQ-1 through DSQ-3 drive all three structural patterns from causal reasoning. Schema Area 3 derives and declares all three templates. The phrasing register throughout emphasizes the unifying principle — no boundary is a bare positional marker; every boundary is a reasoned commitment. Maximum R17 coverage. Expected: C-52, C-53, C-54 all achieved; ~180-182/182.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Each register is a distinct epistemic workspace — its opening header declares what reasoning occurs within it; its close marker declares what that reasoning established. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** -- Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

NHQ-1. A register section in a structured document can be introduced by a bare bold label (`**NULL REGISTER**`) or by a compound label (`**NULL REGISTER** -- Epistemic status of null cases`). What information does a reader have after encountering the compound form that is structurally absent from the bare label? What cognitive step does the compound form make unnecessary?

NHQ-2. A document element must both identify itself and characterize its epistemic function. When these two declarations occupy the same parseable header line, what property does that line have that neither the identity claim nor the function claim carries alone? What is the reader's epistemic position after reading the compound header that would require two separate reads to achieve without it?

NCQ-1. A named register ends. Two close marker forms are possible: (a) a bare named close — `**NULL REGISTER CLOSE**` — and (b) a compound close — `**NULL REGISTER CLOSE** -- Null baseline for [concept] established`. What does the reader know at the compound close that cannot be derived from the bare close alone? Why is the bare close a boundary position marker but not a closure-assertion marker?

NCQ-2. A register close marker should simultaneously name what terminates and characterize what that termination establishes. When both appear in a single compound line, what structural property does the document boundary gain that it lacks when the close marker is positional only? What reasoning would a reader have to perform externally without the compound close that the compound form performs internally?

---

**NULL REGISTER CLOSE** -- Null baseline established: [author accomplishment descriptor from NCQ-1 and NCQ-2]

---

**DEPARTURE REGISTER** -- Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied — without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

DSQ-1. A manifest close can express a terminal-position claim and a successor-identity claim in two forms: (a) a single sentence embedding both — "This is MANIFEST-N's last line before TABLE-N" — or (b) two structurally independent sentences — "This is the last content line of MANIFEST-N. TABLE-N header follows directly below." What structural difference between these two forms is visible at parse time, without reading sentence content? What verification operation is possible with form (b) that requires inference with form (a)?

DSQ-2. When two independent assertions must be verifiably co-present in a single document element, what is the minimum structural form that allows a verifier to confirm each assertion's presence independently — without reading the entire element for semantic content? Why does embedding both assertions in a single sentence fail this independent-verifiability requirement?

DSQ-3. An agent is instructed that its manifest close must satisfy two structurally independent assertions. If the agent's close line is one sentence, what parse-time ambiguity arises about whether both assertions are present and distinct? What does making each assertion a grammatically independent sentence resolve at parse time that single-sentence embedding does not?

---

**DEPARTURE REGISTER CLOSE** -- Departure baseline established: [author accomplishment descriptor from NCQ-1 and NCQ-2]

---

**CAUSAL PHASE CLOSE**

All questions answered above — NULL REGISTER and DEPARTURE REGISTER complete. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace that follows. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt. The unifying principle to author: every structural boundary in a trace document is a point of double assertion — no boundary is a bare positional marker; every boundary simultaneously declares what it is and what epistemic work it performs or accomplished.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NQ-1 through NQ-2 and DQ-1.
          Author: the null state and its justification, every departure code and
          its evidentiary requirement, and the null-documentation rule for inert hops.

 Area 3 — Structural boundary declarations (three templates):

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
          Derive from NHQ-1 and NHQ-2.
          Write the rationale: why compound form exceeds bare label.
          Declare the template: **LABEL** -- epistemic-function descriptor.
          Give examples: **NULL REGISTER** -- [function], **DEPARTURE REGISTER** -- [function].

          3c. Register close compound template:
          Derive from NCQ-1 and NCQ-2.
          Write the rationale: why compound close exceeds bare close.
          Declare the template: **LABEL CLOSE** -- accomplishment descriptor.
          Give examples: **NULL REGISTER CLOSE** -- [accomplishment],
                         **DEPARTURE REGISTER CLOSE** -- [accomplishment].

          Author the unifying principle: the compound form applied to headers (3b) and
          close markers (3c) and the dual-assertion form applied to manifest closes (3a)
          share the same structural logic — every boundary simultaneously names itself
          and characterizes what it performs or finalizes.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete and Area 3 declares all three templates (close-line dual-assertion, register header compound, register close compound) with their rationales.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. Apply all three boundary declaration templates from Area 3 throughout:

- Every named register header: compound form from Area 3b — identity label AND epistemic-function descriptor in one parseable line.
- Every named register close: compound form from Area 3c — close label AND accomplishment descriptor in one parseable line.
- Every manifest close-line: dual-assertion two-sentence form from Area 3a — identity sentence AND successor sentence as grammatically independent co-present sentences.

No boundary in this trace is a bare positional marker. You derived this principle from your CAUSAL PHASE. Satisfying only one assertion at any boundary does not satisfy the boundary requirement — you articulated why across NHQ-1, NHQ-2, NCQ-1, NCQ-2, and DSQ-1 through DSQ-3.

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
*[Apply your TRAVERSAL-SCHEMA Area 3a placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-1." (2) successor — "TABLE-1 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3a placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-2." (2) successor — "TABLE-2 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the null default you derived from NQ-1. Every departure code is a supported claim; every hop without evidence of departure carries the null default.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3a placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-3." (2) successor — "TABLE-3 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3a placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-4." (2) successor — "TABLE-4 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3a placeholder instruction here — verbatim. Two sentences required: (1) identity — "This is the last content line of MANIFEST-5." (2) successor — "TABLE-5 header follows directly below." Both sentences must appear as grammatically independent co-present sentences. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |
