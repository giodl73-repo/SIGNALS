# trace-component — Round 16 Variations

**Variation axes used:**
- Single-axis: Role sequence / named-register subdivision for C-49 (V-01), Output format / successor-naming in manifest close for C-51 (V-02), Lifecycle emphasis / per-register close chain for C-49+C-50 (V-03)
- Combined: Role sequence + Output format / C-49+C-51 without C-50 (V-04), All three axes + Phrasing register / maximum C-49+C-50+C-51 (V-05)

**R16 context:** Three new criteria from R15 excellence signals:

- **C-49 (Named-Register Subdivision of Causal Phase)** — The causal question block must be subdivided into explicitly labeled named sections — at minimum a NULL REGISTER section and a DEPARTURE REGISTER section — each carrying its own section header as a distinct document element. C-48 requires null questions to precede departure questions (ordering); C-49 requires the two categories to be labeled as structurally distinct named sections. A correctly sequenced but undivided causal block does not satisfy C-49 — the register boundary must be visible as a named section label, not inferred from question ordering.

- **C-50 (Per-Register Close Marker Within Causal Phase)** — Each named register within the causal phase (satisfying C-49) ends with an explicit register-level close marker before the next register or phase begins. Analogous to C-38's manifest-close marker: the per-register close gates each internal register boundary independently of the phase-level gate, preventing content from bleeding from the departure register into the schema authorship block. A causal phase with named registers but a single phase-level close does not satisfy C-50 — the internal register-to-register boundary is ungated. C-50 requires C-49 as a structural precondition.

- **C-51 (Successor-Naming in Manifest-Close Adjacency Marker)** — Every manifest-close adjacency marker explicitly names its phase-keyed successor artifact — "TABLE-N header follows directly below" — in addition to asserting terminal position. C-38 requires the close line to assert that the analysis table begins directly below; C-51 requires that statement to name the specific phase-keyed label rather than asserting terminal position alone. A model writing the close line and then inserting content before TABLE-N must contradict both the terminal-position claim and the named-successor claim simultaneously. C-51 can be satisfied without C-49 or C-50; it extends C-38 without depending on the causal phase structure.

**C-49 / C-50 / C-51 orthogonality:**
- C-49 can be satisfied without C-50 (named sections, single phase-level close)
- C-50 requires C-49 (register-level close requires named registers to close)
- C-51 is independent of C-49 and C-50 (manifest close successor-naming has no dependency on causal phase register structure)
- Full expression requires all three: C-49 makes the null/departure boundary a named document element, C-50 gates each register boundary independently, C-51 binds each manifest close to its specific successor artifact

**R16 hypotheses:**
- V-01: Role sequence — subdivide CAUSAL PHASE into named NULL REGISTER and DEPARTURE REGISTER section headers (no per-register close markers; single CAUSAL PHASE CLOSE). Manifest closes: terminal-position only (no TABLE-N naming). Tests C-49 alone. Expected: ~172-173/176.
- V-02: Output format — manifest close lines name the specific TABLE-N successor in addition to asserting terminal position. No named register subdivision in CAUSAL PHASE. Tests C-51 alone. Expected: ~172-173/176.
- V-03: Lifecycle emphasis — named register sections with explicit per-register close markers (NULL REGISTER CLOSE / DEPARTURE REGISTER CLOSE). No successor-naming in manifest closes. Tests C-49+C-50 combined. Expected: ~173-174/176.
- V-04: Role sequence + Output format — named register sections (C-49, no per-register close) + manifest close successor-naming (C-51). No DEPARTURE REGISTER CLOSE marker. Tests whether C-49+C-51 together produce emergent C-50 tendencies. Expected: ~173-174/176.
- V-05: All three axes + Phrasing register — named registers + per-register close markers + successor-naming in all manifest closes + Phase Contracts at every manifest. Unifying principle: every structural boundary requires both identity assertion and successor commitment. Maximum R16 coverage. Expected: ~174-176/176.

---

## V-01 · Role Sequence — Named-Register Subdivision (C-49 Target)

**Axis**: Role sequence
**Hypothesis**: C-49 requires the causal question block to be explicitly subdivided into named register sections — a NULL REGISTER section and a DEPARTURE REGISTER section — each with its own section header as a distinct document element. R15 V-04 presented all 8 causal questions in a single undivided CAUSAL PHASE block; the null-to-departure boundary was positionally implied but structurally invisible. V-01 reorganizes the same questions under named section headers while making no other structural changes: the NULL-to-DEPARTURE transition is a section heading only (no register close marker — C-50 not targeted). The CAUSAL PHASE closes with a single phase-level `CAUSAL PHASE CLOSE` gate. Manifest close lines assert terminal position without naming TABLE-N (C-51 not targeted). Tests whether named section headers alone satisfy C-49. Expected: C-49 achieved; ~172-173/176.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions in this phase. No schema artifact is written here. The phase contains two named registers. Answer the NULL REGISTER questions completely before proceeding to the DEPARTURE REGISTER.

---

**NULL REGISTER** — Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — positive assertion, negative assertion, or suspension of judgment? What justifies that particular stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and a trace that documents a hop as confirmed inactive? What does the reader lose when the two cases are represented identically?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header? What makes this null characterization the correct starting point for reasoning about an enforcement mechanism?

---

**DEPARTURE REGISTER** — Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement in the document for the self-contradiction property to hold at production time rather than only at review time?

DQ-3. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish: (a) neither requirement satisfied, (b) exactly one satisfied, (c) both satisfied — without consulting any source outside the output?

DQ-4. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies one requirement. What must the instruction explicitly state for the agent's implicit claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening establishes how many distinct satisfaction targets must be met? What is the difference in cognitive status between reading the body with and without that prior knowledge?

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

 Area 3 — Manifest adjacency and close-line placeholder:
          Derive from NQ-3 and DQ-2 through DQ-5.
          First write the structural rationale for the close-line mechanism.
          Then write the structural rationale for the dual-constraint form.
          Then write the complete placeholder instruction text.
          The placeholder must: open with an obligation count (from DQ-5),
          enumerate both constraints as labeled independent items (from DQ-3),
          include an entanglement declaration that neither alone satisfies the
          dual requirement (from DQ-4), and name the terminal positional claim.
          Then declare the exact close-line text the placeholder will reproduce.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the structural rationale and the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim, as that manifest's terminal line. You derived the placeholder from epistemic reasoning in your CAUSAL PHASE. Satisfying only one of the two requirements does not satisfy the placeholder — you articulated why in DQ-3 and DQ-4.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout | |

---

## V-02 · Output Format — Successor-Naming in Manifest Close (C-51 Target)

**Axis**: Output format
**Hypothesis**: C-51 requires every manifest-close adjacency marker to name its phase-keyed successor artifact — "TABLE-N header follows directly below" — in addition to asserting terminal position. R15 V-01 through V-04 established terminal position ("as this manifest's last line" or "as this manifest's terminal line") without naming the specific TABLE-N that must follow. V-02 modifies only the manifest close cue format: every manifest close line asserts identity ("This is the last content line of MANIFEST-N") AND names the successor ("TABLE-N header follows directly below"). The CAUSAL PHASE remains a single undivided block (no register subdivision — C-49 not targeted; no per-register close markers — C-50 not targeted). Tests whether successor-naming in manifest closes alone satisfies C-51 independently of C-49 and C-50. Expected: C-51 achieved; ~172-173/176.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE — reasoning only.

---

### CAUSAL PHASE — Epistemic Reasoning

Answer all questions below. No schema artifact is written here.

**Direction default — traversal null case:**

Q-1. When a traversal hop has not been examined, what epistemic stance toward that hop's behavior is warranted — assertion of activity, assertion of inactivity, or suspension of judgment pending evidence? What justifies that stance as the correct default?

Q-2. What is the difference between a Direction cell that records confirmed knowledge about a hop's behavior and a Direction cell that records an assumption? What would a trace where the two cases are represented identically fail to communicate to a reader?

Q-3. What must be true of the relationship between a traversal table's coverage and the set of traversal hops for the table to support completeness claims? What information is structurally absent when a confirmed-null hop is represented the same way as an unexamined hop?

**Manifest close-line — adjacency and dual-constraint:**

Q-4. The position between a manifest block's final content and its analysis table header is a structural location in the document. Before any constraint about that position has been applied, what is the epistemically correct characterization of its occupancy state?

Q-5. A structural constraint mechanism is proposed for guaranteeing that a specific document position remains free of non-specified content. What is the epistemic relationship between the mechanism's placement in the document and the strength of the guarantee it provides?

Q-6. An instruction imposes two requirements on an agent and expects both to be satisfied. What is the minimum information structure of the instruction that allows a verifier to determine whether the agent satisfied neither, one, or both requirements without consulting any source other than the output?

Q-7. Two requirements within a single instruction are each necessary and neither is sufficient alone. An agent satisfies one requirement and produces output. What must the instruction explicitly state — in the instruction's own text — to make the agent's implicit claim of partial satisfaction structurally untenable before the agent begins producing output?

Q-8. When an agent encounters an instruction that will impose multiple distinct satisfaction targets, what information about the instruction's scope should the agent know before reading the instruction's body?

---

**CAUSAL PHASE CLOSE**

All questions answered above. No schema artifact produced. SCHEMA PHASE begins.

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

 Area 2 — Direction default contract: derive from Q-1 through Q-3.
          Author: the null/default state and its justification, every departure
          code and its evidentiary requirement, and the inert-hop documentation rule.

 Area 3 — Manifest adjacency and close-line placeholder:
          Derive from Q-4 through Q-8.
          First write the structural rationale for the close-line mechanism (Q-4, Q-5).
          Then write the rationale for the dual-constraint form (Q-6, Q-7, Q-8).
          Then write the complete placeholder instruction text.
          The placeholder must: open with obligation count (Q-8), enumerate both
          constraints as independently labeled items (Q-6), include an entanglement
          declaration that neither alone satisfies the dual requirement (Q-7).
          Then declare the exact close-line text the placeholder will reproduce.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the structural rationale and the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2 at every traversal hop. At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim. You derived the placeholder's structural form from Q-4 through Q-8. Satisfying only one of the two requirements does not satisfy the placeholder — you articulated why in Q-6 and Q-7.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-1. TABLE-1 header follows directly below. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-2. TABLE-2 header follows directly below. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: apply the epistemic default you derived from Q-1 through Q-3. Every departure code is a supported claim; every hop without evidence of departure carries the default.

| Step | T-ID | Component | Direction [epistemic default \| departure codes] | Role [Default — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-3. TABLE-3 header follows directly below. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-4. TABLE-4 header follows directly below. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-5. TABLE-5 header follows directly below. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA epistemic derivation terms + framework terms throughout | |

---

## V-03 · Lifecycle Emphasis — Per-Register Close Chain (C-49 + C-50 Target)

**Axis**: Lifecycle emphasis
**Hypothesis**: C-50 requires each named register within the causal phase to end with an explicit register-level close marker before the next register or phase begins — and C-50 requires C-49 as a precondition. V-01 has named register sections (C-49) but uses a single phase-level `CAUSAL PHASE CLOSE` without gating the internal NULL-to-DEPARTURE boundary. V-03 adds per-register close markers: `NULL REGISTER CLOSE` after the null questions and `DEPARTURE REGISTER CLOSE` after the departure questions. The `DEPARTURE REGISTER CLOSE` serves as both the register-level close and the causal-to-schema phase boundary. Manifest close lines remain terminal-position only (C-51 not targeted — no TABLE-N successor naming). Tests whether the full per-register close chain (C-49 + C-50) is achieved when manifest closes do not name successors. Expected: C-49 + C-50 achieved; ~173-174/176.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE.

---

### CAUSAL PHASE — Two-Register Epistemic Reasoning

This phase contains reasoning only. No schema is authored here. The phase has two sequential registers. Complete NULL REGISTER fully and close it before opening DEPARTURE REGISTER.

---

**NULL REGISTER** — Epistemic status of null cases

Close this register completely before proceeding to DEPARTURE REGISTER.

NQ-1. When a traversal hop has not been examined, what epistemic stance toward that hop's behavior is warranted, and what justifies that stance as the appropriate starting point?

NQ-2. What is the structural difference between a trace that omits an unexamined hop and one that documents a confirmed-null hop explicitly? What information is lost when the two cases are represented identically?

NQ-3. An analyst assigns a Direction value to a hop cell. Under what conditions does that assignment represent confirmed knowledge? Under what conditions is it an unsupported claim?

NQ-4. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest's final content line and its analysis table header — what is the null state for that structural position?

---

**NULL REGISTER CLOSE** — Null baseline for traversal hops and manifest adjacency established above. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** — Properties of departure claims

Answer after NULL REGISTER is complete and closed.

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell? What does the departure code assert, and what role does the evidence play?

DQ-2. Why must confirmed-null hops appear explicitly in the traversal table rather than being omitted? What structural property of the table depends on explicit null documentation?

DQ-3. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of the mechanism's placement in the document for the self-contradiction property to hold at production time?

DQ-4. A single instruction imposes two structural requirements. What is the minimum information the instruction must provide for a verifier to independently determine whether each requirement was satisfied?

DQ-5. Two requirements are each necessary; neither is sufficient alone. An agent satisfies one. What must the instruction explicitly state to make the claim of partial satisfaction structurally untenable?

DQ-6. Before an agent reads a multi-requirement instruction's body, what information at the instruction's opening establishes how many distinct satisfaction targets must be met?

---

**DEPARTURE REGISTER CLOSE** — Both registers complete. No schema authored above. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA. The schema must be authored in your own words entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting question text into schema format.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NULL REGISTER NQ-1 through NQ-3
          and DEPARTURE REGISTER DQ-1 through DQ-2.
          Author: the null default and its justification, every departure code and
          its evidentiary requirement, and the explicit null-documentation rule.

 Area 3 — Manifest adjacency and close-line placeholder:
          Derive from NULL REGISTER NQ-4 and DEPARTURE REGISTER DQ-3 through DQ-6.
          First write the structural rationale for the close-line mechanism (NQ-4, DQ-3).
          Then write the rationale for the dual-constraint form (DQ-4, DQ-5, DQ-6).
          Then write the complete placeholder instruction text. It must:
          open with obligation count (DQ-6), enumerate both constraints as independently
          labeled items (DQ-4), include an entanglement declaration (DQ-5), and
          assert terminal positional claim.
          Then declare the exact close-line text the placeholder will reproduce.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the structural rationale and the complete placeholder text, and the close-line text is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2: every hop defaults to the null state you derived from NQ-1; departure codes are active claims requiring Role-column evidence (DQ-1). At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim, as that manifest's terminal line. You derived the placeholder from your DEPARTURE REGISTER reasoning: satisfying the content constraint without the positional constraint (or vice versa) is the same class of error as a departure code without Role-column evidence — an unsupported claim.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Your placeholder carries: obligation-count opening (DQ-6), independently labeled constraints (DQ-4), entanglement declaration (DQ-5). Reproduce now.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops — null hypothesis applies; document all hops including confirmed-null]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim, as this manifest's terminal line. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: every hop begins at the null state (NQ-1). Departure codes are active claims requiring Role-column evidence (DQ-1). Confirmed-null hops are documented explicitly, not omitted (DQ-2).

| Step | T-ID | Component | Direction [null: derived default \| departure: derived codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
|------|------|-----------|-----------|------|-------|
| 1 | T-01 | *(leaf receiving event)* | | | |
| 2 | T-02 | | | | |
| ... | | | | | |

Minimum two rows. T-IDs feed TABLE-4.

**INERT-HOP DECLARATION (mandatory — present regardless of count):**
```
Inert hops: ___ (T-IDs: ___)
Null confirmed: [per inert T-ID — basis per NQ-1 null justification]
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

Every T-ID from TABLE-2 must appear — null-state hops included; a null Direction does not preclude re-rendering from external prop or context changes.

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 2 null-departure contract + framework terms throughout | |

---

## V-04 · Combined: Role Sequence + Output Format (C-49 + C-51, C-50 Not Targeted)

**Axis**: Role sequence + Output format (combined)
**Hypothesis**: V-01 achieves C-49 via named register section headers (no per-register close markers). V-02 achieves C-51 via successor-naming in manifest closes (no register subdivision). V-04 combines both: the CAUSAL PHASE has NULL REGISTER and DEPARTURE REGISTER section headers (C-49), and every manifest close line names its specific TABLE-N successor (C-51). The internal NULL-to-DEPARTURE transition has no close marker — it is governed by the section heading only (C-50 not targeted; single `CAUSAL PHASE CLOSE` at phase boundary). Tests whether C-49+C-51 together create pressure toward C-50 (whether the structural precision of named registers and named successors induces a register-close pattern emergently). Expected: C-49+C-51 achieved; C-50 emergent or absent; ~173-174/176.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema structure, no placeholder template, and no schema-format cue of any kind appears in CAUSAL PHASE.

---

### CAUSAL PHASE — Epistemic Reasoning

This phase contains reasoning only. No schema is authored here. The phase has two named registers. Complete the NULL REGISTER questions before proceeding to the DEPARTURE REGISTER questions.

---

**NULL REGISTER** — Epistemic status of null cases

NQ-1. When a traversal hop has not been examined, what epistemic stance toward its behavior is warranted — positive assertion, negative assertion, or suspension of judgment? What justifies that stance as the correct default over the alternatives?

NQ-2. What is the structural difference between a confirmed-null hop and an unexamined hop represented as absent? What does a traversal table lose when it cannot distinguish the two?

NQ-3. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest block's final content and its analysis table header?

NQ-4. What does it mean to claim that manifest-to-table adjacency holds as a guaranteed structural property? What would it take for that guarantee to hold in the null case — with no enforcement mechanism in place?

---

**DEPARTURE REGISTER** — Properties of departure claims

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell? What does the departure code assert, and what verification burden does that assertion carry?

DQ-2. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of the mechanism's document placement for that property to hold at production time?

DQ-3. A single instruction imposes two structural requirements. What is the minimum information structure for a verifier to independently assess whether each requirement was satisfied without consulting any external source?

DQ-4. Two requirements within a single instruction are jointly necessary; neither alone constitutes even partial compliance. An agent satisfies one. What must the instruction explicitly state for that agent's claim of partial satisfaction to be structurally untenable?

DQ-5. Before an agent reads a multi-requirement instruction's body, what information at the instruction's opening determines the agent's epistemic frame for how many distinct satisfaction targets must be met?

---

**CAUSAL PHASE CLOSE**

All NULL REGISTER and DEPARTURE REGISTER questions answered above. No schema artifact produced. SCHEMA PHASE begins.

---

### SCHEMA PHASE — Schema Authorship

Produce the TRAVERSAL-SCHEMA — a named artifact a reader can reference to verify the trace. Author it entirely from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt — not in paraphrase, not by reformatting question text into schema fields.

```
TRAVERSAL-SCHEMA
----------------
[Author the complete schema here. Areas 1 through 4 in full.
 Every principle must derive from your CAUSAL PHASE answers.
 Do not reproduce any language from this prompt.

 Area 1 — Framework context: framework, state management library, component model.

 Area 2 — Direction default contract: derive from NQ-1, NQ-2, DQ-1.
          Author: the null/default state and its justification, every departure
          code and its evidentiary requirement, and the null-documentation rule
          for confirmed-null hops.

 Area 3 — Manifest adjacency and close-line placeholder:
          Derive from NQ-3, NQ-4, DQ-2, DQ-3, DQ-4, DQ-5.
          First write the structural rationale for the close-line mechanism (NQ-3, NQ-4, DQ-2).
          Then write the rationale for the dual-constraint form (DQ-3, DQ-4, DQ-5).
          Then write the complete placeholder instruction text. It must:
          open with obligation count (DQ-5), enumerate both constraints as independently
          labeled items (DQ-3), include an entanglement declaration (DQ-4), and
          name the terminal positional claim.
          Then declare the exact close-line text the placeholder will reproduce at
          every manifest close. This text must also name the specific phase-keyed
          successor artifact (TABLE-N) so that both a positional claim and a
          successor-identity claim are simultaneously present in the close line.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 3 contains the structural rationale and the complete placeholder text, and the close-line text — including TABLE-N successor naming — is declared.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. Apply the Direction default from Area 2: every hop defaults to the null state you derived from NQ-1; departure codes are claims requiring Role-column evidence (DQ-1). At every manifest close-line slot: apply the placeholder instruction you authored in Area 3 — verbatim. Your close-line text names the specific TABLE-N successor: writing the close line and then inserting content before TABLE-N contradicts both the terminal-position claim and the named-successor claim simultaneously.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-1. TABLE-1 header follows directly below. Reproduce now.]*

**TABLE-1 · Event Anchor**

| Event Type | Component Name | Handler Function | Event Payload | File Location |
|------------|----------------|------------------|---------------|---------------|
| *(click / submit / input / change / other)* | *(exact name)* | *(exact name)* | *(value / shape / "none")* | *(path:line)* |

[GATE-1: TABLE-1 does not close on "the button", "a click", "the handler", "N/A", or any blank cell.]

---

**MANIFEST-2 · Traversal Phase**

```
Components in scope: [all traversal hops — null hypothesis applies; document all hops including confirmed-null]
State keys may be touched: ___
Side effects may fire: ___
```
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-2. TABLE-2 header follows directly below. Reproduce now.]*

**TABLE-2 · Component Tree Traversal**

Per your TRAVERSAL-SCHEMA Area 2: every hop begins at the null state derived from NQ-1. Departure codes are active claims requiring Role-column evidence. Confirmed-null hops are documented explicitly, not omitted.

| Step | T-ID | Component | Direction [null default \| departure codes] | Role [Null confirmed — basis / Departure — evidence] | Notes |
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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-3. TABLE-3 header follows directly below. Reproduce now.]*

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-4. TABLE-4 header follows directly below. Reproduce now.]*

**TABLE-4 · Re-render Inventory**

Every T-ID from TABLE-2 must appear — null-state hops included.

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
*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here — verbatim. This is the last content line of MANIFEST-5. TABLE-5 header follows directly below. Reproduce now.]*

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
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 + NULL REGISTER null-departure derivation throughout | |

---

## V-05 · Combined: All Three Axes + Phrasing Register — Maximum R16 Coverage (C-49 + C-50 + C-51)

**Axis**: Role sequence + Lifecycle emphasis + Output format + Phrasing register (combined)
**Hypothesis**: The R16 maximum coverage variation. V-03 achieves C-49+C-50 (named registers + per-register close markers, no successor naming). V-04 achieves C-49+C-51 (named registers + successor naming, no per-register close). V-05 combines all three: named register sections (C-49) + per-register close markers (C-50) + successor-naming in all manifest close lines (C-51) + Phase Contracts at every manifest (from R15 V-05). The unifying structural principle: every boundary in the document requires two assertions simultaneously — an identity assertion ("this is X") and a successor assertion ("Y follows directly"). The NULL REGISTER CLOSE names what it closes and signals what opens. The DEPARTURE REGISTER CLOSE names what it closes and names the schema phase as successor. Every manifest close names MANIFEST-N (identity) and TABLE-N (successor). The Phase Contract forward-declares the dual-constraint obligation before the manifest body. C-46/C-47/C-48/C-49/C-50/C-51 all present. Expected: C-49+C-50+C-51 all achieved; ~174-176/176.

---

You have two roles. Complete Role 1 fully before beginning Role 2.

---

**ROLE 1 — SCHEMA ARCHITECT**

You are designing the epistemological framework and governing schema for a frontend component trace. This role has two sequential phases. Complete CAUSAL PHASE fully before opening SCHEMA PHASE. No schema artifact, no schema-format cue, no placeholder template, and no structural design of any kind appears in CAUSAL PHASE.

---

### CAUSAL PHASE — Two-Register Epistemic Reasoning

This phase contains reasoning only. No schema is authored here. The phase has two sequential registers. Complete NULL REGISTER fully and close it before opening DEPARTURE REGISTER.

---

**NULL REGISTER** — Epistemic status of null cases

Close this register completely before proceeding to DEPARTURE REGISTER. The null register establishes the baseline epistemic state for every structural position reasoned about in the departure register.

**For traversal hops:**

NQ-1. When a traversal hop has not been examined, what is the warranted epistemic stance about its contribution to the trace — and what justifies that stance as the appropriate starting point rather than any other?

NQ-2. What is the structural difference between a hop whose null state has been confirmed by examination and a hop whose null state has been assumed without examination? What does a trace that conflates these two cases fail to provide?

NQ-3. An analyst produces a traversal table. What does the act of assigning any value to a Direction cell commit the analyst to — what claim has been made, and what verification burden does that commitment carry?

**For manifest adjacency:**

NQ-4. Before any structural rule about manifest-to-table adjacency has been applied, what is the epistemically correct characterization of the space between a manifest's final content and its analysis table header — what is the null state for that structural position?

NQ-5. What does it mean to claim that manifest-to-table adjacency is guaranteed — what would it take for that guarantee to hold in the null case (no enforcement mechanism in place), and what does the answer reveal about the necessity of a structural mechanism?

NQ-6. In what structural sense are the null state for a traversal hop's Direction cell and the null state for the manifest-to-table space parallel epistemic objects — what do they share as problems requiring the same class of solution?

---

**NULL REGISTER CLOSE** — Null baseline established for traversal hops and manifest adjacency. DEPARTURE REGISTER begins.

---

**DEPARTURE REGISTER** — Properties of departure claims

Answer after NULL REGISTER is complete and closed. These questions address the structural properties required for departure claims to be valid and verifiable.

**For traversal departures:**

DQ-1. What is the epistemic relationship between a departure code in a Direction cell and the Role-column evidence for that cell — what does the departure code assert, and what role does the evidence play in making that assertion evaluable?

DQ-2. Why must confirmed-null hops appear explicitly in the traversal table rather than being omitted — what structural property of the table depends on explicit null documentation?

**For manifest close-line:**

DQ-3. A structural mechanism is proposed for making violation of manifest-to-table adjacency self-contradictory at point-of-production. What must be true of that mechanism's placement — where in the document it appears — for the self-contradiction property to hold at production time rather than only at review time?

DQ-4. A single instruction imposes two structural requirements on an agent. What is the minimum information the instruction must provide for a verifier to distinguish three cases: (a) neither requirement satisfied, (b) exactly one requirement satisfied, (c) both requirements satisfied — without consulting any source outside the output?

DQ-5. Two requirements in a single instruction are each necessary for compliance; neither alone constitutes partial compliance. An agent satisfies requirement A. What implicit claim has the agent made about requirement B? What must the instruction explicitly state for that implicit claim to be structurally untenable — visible as unsatisfied at the moment the agent produces output, not only detectable by a reader after the fact?

DQ-6. Before an agent reads the body of a multi-requirement instruction, what information at the instruction's opening determines the agent's epistemic frame for how many distinct satisfaction targets must be met? What is the difference in cognitive status between an agent who reads the instruction body knowing the target count and an agent who reads it without that knowledge?

---

**DEPARTURE REGISTER CLOSE** — Both registers complete. No schema authored above. SCHEMA PHASE begins.

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

 Area 2 — Direction default contract: derive from NULL REGISTER NQ-1 through NQ-3
          and DEPARTURE REGISTER DQ-1 through DQ-2.
          Author in your own words: the null state and its justification, every
          departure code and its evidentiary requirement, and the null-documentation
          rule for confirmed-null hops.

 Area 3 — Manifest adjacency and close-line placeholder:
          Derive from NULL REGISTER NQ-4 through NQ-6 and DEPARTURE REGISTER DQ-3 through DQ-6.
          First author the structural rationale for the close-line mechanism (NQ-4, NQ-5, DQ-3).
          Then author the structural rationale for the dual-constraint form (DQ-4, DQ-5, DQ-6).
          Then write the complete placeholder instruction text. The placeholder must:
          open with obligation count (DQ-6), enumerate both constraints as independently
          labeled items (DQ-4), include an entanglement declaration that neither alone
          satisfies the dual requirement (DQ-5), and assert terminal positional claim.
          Then declare the exact close-line text the placeholder will reproduce.
          This close-line text must carry two assertions: an identity assertion
          ("This is the last content line of MANIFEST-N") and a successor-naming
          assertion ("TABLE-N header follows directly below"). Both assertions must
          appear as distinct co-present sentences in the declared close-line text.

          Also design the Phase Contract format — the block that opens every
          manifest before the manifest body. The Phase Contract must forward-declare
          the dual-constraint obligation at phase entry, consistent with DQ-4 through DQ-6.

 Area 4 — Table inventory: every table by name and purpose.]
```

Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete, Area 2 documents the null-to-departure contract, Area 3 contains the structural rationale, complete placeholder text, Phase Contract format, and the declared close-line text with both identity and successor-naming assertions.

---

**ROLE 2 — TRACE ANALYST**

You are a frontend domain expert. Execute the trace governed by the TRAVERSAL-SCHEMA you authored in Role 1. The null-hypothesis epistemology you established in CAUSAL PHASE governs every phase: every Direction cell defaults to the null you derived from NQ-1; every departure code is an active claim requiring Role-column evidence (DQ-1); every manifest-to-table adjacency is enforced by the close-line mechanism you derived from NQ-4 and DQ-3. Open every manifest with your authored Phase Contract. Close every manifest with the DUAL-CONSTRAINT BLOCK placeholder you designed — verbatim. Your close-line text carries two assertions simultaneously: the identity assertion and the TABLE-N successor-naming assertion. Writing the close line and then inserting content before TABLE-N contradicts both assertions simultaneously — a stronger structural self-contradiction than position alone provides. You derived this property from your DQ-3 reasoning: violation must be self-contradictory at point-of-production, not only detectable by review.

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
*[Reproduce your TRAVERSAL-SCHEMA Area 3 DUAL-CONSTRAINT BLOCK placeholder here — verbatim as designed, as this manifest's terminal line. Your block's opening element derives from DQ-6 (obligation-count before body), its enumeration derives from DQ-4 (independent addressability), its entanglement declaration derives from DQ-5 (neither requirement alone constitutes compliance). This is the last content line of MANIFEST-1. TABLE-1 header follows directly below.]*

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

| Step | T-ID | Component | Direction [null: derived default \| active claim: derived departure codes] | Role [Null confirmed — basis / Active claim — departure + evidence] | Notes |
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
| C-02 Component Tree Traversal | TABLE-2 · T-ID + Direction per row (min 2 rows) | |
| C-03 State Update Map | TABLE-3 · Pre-declaration + row count = N+M | |
| C-04 Re-render Inventory | TABLE-4 · T-ID completeness + PROMOTION BLOCK | |
| C-05 Final UI State | TABLE-6 · four Phase rows, Visible Elements not blank | |
| C-06 Side Effect Coverage | TABLE-5 · none-row if no effects | |
| C-07 Issue Detection | TABLE-7 · five rows, N/A prohibited, F-02 UR cross-ref | |
| C-08 Framework Vocabulary | TRAVERSAL-SCHEMA Area 1 + null-departure derivation terms + framework vocabulary throughout | |
