# trace-component — Variate Round 3 (V-01 through V-05)

---

## V-01 — Role Sequence Axis

**Hypothesis:** Running a Vocabulary Police role *before* the Trace Analyst locks the neutral vocabulary contract explicitly. The model cannot later justify framework jargon in core sections by pointing to a Framework Notes annotation — because the contract was written first, not inferred from output.

---

```
You are executing a three-role sequence. Complete each role fully before advancing.
Do not merge roles. Do not begin Role 2 until Role 1 is stamped VOCABULARY LOCKED.

---

### ROLE 1 — Framework Vocabulary Auditor

Your only task: establish the vocabulary contract for this trace.

1. Identify the frontend framework in scope from the user action and codebase context provided.

2. Produce a **Vocabulary Contract** with two columns:

| Framework-Specific Term | Neutral Equivalent |
|-------------------------|--------------------|
| (e.g., useState)        | (e.g., reactive state variable) |
| (e.g., useEffect)       | (e.g., side-effect hook) |
| (e.g., v-model)         | (e.g., two-way binding) |
| (e.g., @Input())        | (e.g., parent-supplied prop) |

   List every framework-specific term you anticipate using in the trace. Map each to a
   neutral equivalent. If a term has no neutral equivalent, mark it FRAMEWORK-ONLY and
   flag it for the Framework Notes section only.

3. Stamp: **VOCABULARY LOCKED — {framework} identified. {N} terms mapped. {M} FRAMEWORK-ONLY.**

Role 1 is complete after the stamp. Advance to Role 2.

---

### ROLE 2 — Trace Analyst

You are writing a component trace for the following user action:

[USER ACTION PLACEHOLDER]

**Constraint from Role 1:** Core trace sections (§1 through §7) must use ONLY the neutral
equivalents from the Vocabulary Contract. Framework-specific terms are confined to
§8 Framework Notes. Violation: framework jargon appearing in §1–§7 prose.

Produce the following eight sections:

---

**§1 Event Chain**

List every handler, middleware, and listener that fires between the triggering user action
and final UI state, in causal order.

Format: numbered list, one row per entry.
- If a handler dispatches to another handler, show the dispatch arrow inline: `HandlerA → dispatch → HandlerB`
- If a handler's behavior cannot be determined from available inputs, mark it: `UNKNOWN: {reason}`
- Omission is not permitted. Every gap must be named and marked.

---

**§2 Component Tree Traversal**

Name every component involved in this action with its exact codebase name.
For each hop, state: direction (parent→child / child→parent / sibling) and the prop name
or callback name carrying the signal.

Format: tree notation or numbered list with direction labels.
- Use neutral vocabulary: "prop" not "prop drilling", "reactive state" not "useState".
- UNKNOWN permitted for components whose participation is unconfirmed.

---

**§3 State Delta**

For every state update triggered by the action, list:
- State key or slice name
- Value before
- Value after
- Derived state or selectors that depend on this key

Format: table.

| State Key | Before | After | Derived Dependents |
|-----------|--------|-------|--------------------|

- Mark unresolvable values: UNKNOWN
- Mark loading states not yet confirmed: MISSING-LOADING
- Mark error states not yet confirmed: MISSING-ERROR

---

**§4 Re-render List**

Enumerate all components that re-render as a result of the state delta.
For each: reason it re-rendered (prop change / context change / subscription).
Components skipped due to memoization or selector equality: list them explicitly as SKIPPED.

Format: table.

| Component | Re-renders? | Reason | Notes |
|-----------|-------------|--------|-------|

---

**§5 Side Effects and Async Calls**

Name every side effect triggered: API call, subscription update, timer, storage write.
For each: when it fires (sync / deferred), which component or middleware owns it,
what UI state it updates on completion.
Loading branch and error branch must both be named.

- Mark unconfirmed loading branches: MISSING-LOADING
- Mark unconfirmed error branches: MISSING-ERROR

---

**§6 Issue Flags**

Evaluate all four categories. Do not skip a category — state "none found" with supporting
evidence from prior sections if applicable.

- (a) Unnecessary re-renders: cite §4 rows
- (b) Missing loading states: cite MISSING-LOADING tokens from §3 or §5
- (c) Error state gaps: cite MISSING-ERROR tokens from §3 or §5
- (d) Accessibility failures: event handlers, focus management, ARIA state changes

Each issue found: component name + nature of gap + one-line remediation hint.
"No issues found" requires citing the specific §4 entries that support the conclusion.

---

**§7 Final UI State**

State the observable final UI state: visible/hidden elements, displayed text or data,
interactive state (disabled, focused, selected).

Cite the §3 state key that produced each UI change. Format: "Because [§3 key] changed
from X to Y, [component] now shows [state]."

---

**§8 Framework Notes**

Translate the trace into framework-specific vocabulary for teams working in {framework}.
This is the only section where framework-specific terms from the Vocabulary Contract appear.
Map each neutral term used in §1–§7 back to its framework equivalent.

---

### ROLE 3 — Completeness Auditor

Verify the completed trace against the following checklist. Output the checklist with
PASS / PARTIAL / FAIL for each item and one sentence of evidence.

- [ ] §1 event chain: every dispatch shown, no silent end-of-list
- [ ] §2 component tree: all hops have direction labels and prop/callback names
- [ ] §3 state delta: all rows present, UNKNOWN/MISSING tokens used where needed
- [ ] §4 re-render list: SKIPPED components explicitly listed
- [ ] §5 async: both loading and error branches named or marked MISSING
- [ ] §6 issues: all four categories evaluated with evidence
- [ ] §7 final state: each UI change cites a §3 key
- [ ] §8 framework notes: no framework jargon leaked into §1–§7

Stamp: **TRACE COMPLETE — {N} UNKNOWN tokens | {M} MISSING tokens | {K} issues flagged**

Role 3 is complete. Trace is ready for use.
```

---

## V-02 — Output Format Axis

**Hypothesis:** A mandatory STATUS column on every row in every structured section prevents silent omission (C-12) and makes incomplete rows structurally visible (C-10) without requiring a separate auditor role. The schema itself enforces the contract.

---

```
You are a Frontend Trace Analyst. Your domain expertise is auto-selected from the framework
context in the provided user action and codebase description. You produce component traces
that are auditable by any frontend engineer regardless of framework familiarity.

Trace the following user action through the UI component tree, state management layer,
and render cycle:

[USER ACTION PLACEHOLDER]

---

## Output Schema

Every structured section uses a table with a mandatory STATUS column.

**STATUS values — use exactly one per row:**
- `CONFIRMED` — derived directly from provided source inputs
- `INFERRED` — logically necessary given confirmed entries; source not directly available
- `UNKNOWN` — cannot be determined from available inputs; reason required
- `MISSING-LOADING` — a loading state exists or should exist; not yet confirmed
- `MISSING-ERROR` — an error state exists or should exist; not yet confirmed

A row without a STATUS value is a schema violation. Do not omit STATUS.
A section that ends without accounting for all expected rows is a schema violation.

---

## Section 1 — Event Chain

Every handler, middleware, and listener that fires between the user action and final UI state.
One row per entry. Causal order. If A dispatches to B, add an explicit DISPATCH row between them.

| Step | Handler / Listener | Dispatches To | STATUS | Notes |
|------|--------------------|---------------|--------|-------|

Rules:
- Do not end the table mid-chain. If you cannot determine the next step, add a row with STATUS=UNKNOWN and explain in Notes.
- DISPATCH rows are required between any two handlers with an indirect relationship.

---

## Section 2 — Component Tree Traversal

Every component involved. One row per hop. Exact codebase name required.

| Hop | From Component | To Component | Direction | Signal Carrier | STATUS | Notes |
|-----|---------------|--------------|-----------|----------------|--------|-------|

Direction values: `parent→child` | `child→parent` | `sibling (shared state)` | `context broadcast`
Signal Carrier: the prop name, callback name, or context key that carries the signal.

---

## Section 3 — State Delta

Every state update triggered by the action.

| State Key / Slice | Before | After | Derived Dependents | STATUS | Notes |
|-------------------|--------|-------|--------------------|--------|-------|

- Value columns: use concrete values or UNKNOWN if indeterminate.
- Derived Dependents: list selectors, computed properties, or memoized values that read this key.

---

## Section 4 — Re-render List

All components that re-render. Components that do NOT re-render must also appear.

| Component | Re-renders? | Reason | Memoization / Guard | STATUS | Notes |
|-----------|-------------|--------|---------------------|--------|-------|

Re-renders? values: `YES` | `NO (memoized)` | `NO (selector equal)` | `NO (condition gate)`
Every component from Section 2 must appear here. A component absent from Section 4 is a gap.

---

## Section 5 — Side Effects and Async

Every side effect triggered by the action.

| Effect | Owner | Fires | On Complete: Updates | Loading Branch | Error Branch | STATUS |
|--------|-------|-------|----------------------|----------------|--------------|--------|

- Fires values: `sync` | `next-tick` | `deferred (ms)` | `on-mount`
- Loading Branch: the UI state shown while the effect is in flight. If unconfirmed: MISSING-LOADING.
- Error Branch: the UI state shown on failure. If unconfirmed: MISSING-ERROR.

---

## Section 6 — Issue Flags

Evaluate all four categories. For each: state findings or explicitly clear with evidence.

**6a — Unnecessary Re-renders**
Cite Section 4 rows. Flag any YES row that could be avoided with memoization or
selector refinement. State the specific component and the optimization.

**6b — Missing Loading States**
List all MISSING-LOADING tokens from Sections 3 and 5. For each: the component that
should show a loading state and the trigger condition.

**6c — Error State Gaps**
List all MISSING-ERROR tokens from Sections 3 and 5. For each: the component that
should handle the error and the expected UI response.

**6d — Accessibility Failures**
Evaluate: keyboard event coverage, focus management after state changes, ARIA attribute
updates that should accompany visible state changes.

If a category has no findings: state "None found" and cite the Section 4 or Section 5 rows
that support this conclusion. Do not leave a category blank.

---

## Section 7 — Final UI State

The observable state of the UI after the full action completes.

| UI Element | Property | Value | Source (§3 key) | STATUS |
|------------|----------|-------|-----------------|--------|

Source column: cite the exact Section 3 state key whose change produced this UI property.
Every row must have a §3 citation. If the derivation cannot be traced: STATUS=UNKNOWN.

---

## Section 8 — Optimization Opportunities

For each unnecessary re-render identified in 6a, state:
- Component name
- Optimization type: `React.memo` | `useMemo` | `reselect selector` | `render-scope split` | equivalent
- Expected render reduction (e.g., "eliminates 2 re-renders per keystroke")

If Section 4 contains no YES rows with avoidable re-renders: state this explicitly and
cite the Section 4 SKIPPED rows that support skipping this section.
Do not leave this section blank or absent without justification.

---

## Section 9 — Framework Notes

Translate the trace into framework-specific vocabulary for engineers working in the
detected framework. Map terms from Sections 1–7 to their framework equivalents.
This is the only section where framework-specific terminology appears.

---

## Trace Summary

After all sections, output:

```
STATUS TOKENS: {N} UNKNOWN | {M} MISSING-LOADING | {P} MISSING-ERROR
RE-RENDERS: {total YES} unnecessary candidate(s) identified
ISSUES: {count} flagged across {categories}
SECTIONS WITH UNKNOWNS: {list section numbers}
```
```

---

## V-03 — Lifecycle Emphasis Axis

**Hypothesis:** Dividing the trace into four explicit lifecycle phases with mandatory completion gates enforces cross-section evidence chaining (C-11) and prevents silent omission (C-12) at phase boundaries — without requiring a table schema or multi-role sequence.

---

```
You are a Frontend Domain Expert conducting a lifecycle-phased component trace.
Your framework expertise is auto-selected from the provided context.

Trace this user action through four lifecycle phases. Complete each phase fully.
Do not advance to the next phase until the current phase's GATE is stamped.

USER ACTION: [USER ACTION PLACEHOLDER]

---

## Phase 1 — Trigger

**Scope:** Everything from the moment the user performs the action until the first component
receives a signal.

Produce:

**1.1 Entry Point**
Name the exact DOM event or gesture that fires. Name the first handler that receives it.
If the entry point is ambiguous: mark `UNKNOWN: {reason}`.

**1.2 Event Chain to First Component**
List every handler, middleware, listener, and interceptor that fires before the first
component's internal logic runs. One entry per step. Show dispatch relationships:
`A → dispatch → B`. Mark any unresolved step `UNKNOWN`.

**1.3 Vocabulary Lock**
Before writing any phase content, list the framework-specific terms you would normally use
(e.g., onClick, useState, $emit) and their neutral equivalents you will use in Phases 1–3.
Commit to the neutral equivalents for all core phase sections.
Framework-specific terms are reserved for Phase 4 Framework Notes only.

**GATE 1:** Stamp one of:
- `PHASE 1 COMPLETE — entry point confirmed, {N} handlers traced, {M} UNKNOWN tokens`
- `PHASE 1 BLOCKED — {reason} — continuing with UNKNOWN tokens as placeholders`

Do not advance to Phase 2 until GATE 1 is stamped.

---

## Phase 2 — Propagation

**Scope:** Signal movement through the component tree.

Reference GATE 1 explicitly: "Building on Phase 1 which ended at [handler name]..."

**2.1 Component Tree Path**
Name every component the signal passes through, in order. For each hop:
- Exact codebase component name
- Direction: `parent→child` | `child→parent` | `sibling (shared state)` | `context broadcast`
- Carrier: the prop name, callback name, or context key
- Mark unresolvable hops: `UNKNOWN`

**2.2 State Management Layer**
Identify where state is owned (local component state, shared store, context). For each:
- State key or slice
- Current value before this action
- Expected value after
- Mark unresolved values: `UNKNOWN` | `MISSING-LOADING` | `MISSING-ERROR`

**GATE 2:** Stamp one of:
- `PHASE 2 COMPLETE — {N} components traversed, {M} state keys updated, {K} UNKNOWN tokens`
- `PHASE 2 BLOCKED — {reason} — continuing with named gaps`

Cite GATE 1 in your stamp: "extends Phase 1's chain from [handler]."

---

## Phase 3 — State Resolution and Side Effects

**Scope:** State deltas finalize; async effects fire.

Reference GATE 2 explicitly: "Following Phase 2's state updates to [keys]..."

**3.1 State Delta Table**
For each state key identified in Phase 2:

| State Key | Before | After | Derived Dependents | Confirmed? |
|-----------|--------|-------|--------------------|------------|

Confirmed? values: YES | INFERRED | UNKNOWN | MISSING-LOADING | MISSING-ERROR

**3.2 Re-render Cascade**
For each state change in 3.1, list components that re-render:
- Component name
- Reason: prop change / context / subscription / forced
- Components skipped (memoized / guard): list explicitly — do not omit skipped components

**3.3 Side Effects**
For each async call or side effect:
- What fires it (cite the state key or event from Phase 2)
- Owner component or middleware
- Timing: sync / next-tick / deferred
- UI state during flight: cite loading branch or mark MISSING-LOADING
- UI state on error: cite error branch or mark MISSING-ERROR

**GATE 3:** Stamp one of:
- `PHASE 3 COMPLETE — {N} state keys resolved, {M} re-renders, {K} side effects, {P} UNKNOWN/MISSING tokens`
- `PHASE 3 BLOCKED — {reason} — named gaps present`

Cite GATE 2 in your stamp.

---

## Phase 4 — Render Output and Analysis

**Scope:** Final UI state; issue analysis; framework translation.

Reference GATE 3 explicitly: "From Phase 3's {M} re-renders and {K} side effects..."

**4.1 Final UI State**
Observable state after the full action. For each change:
- UI element and property
- Value
- Derives from: cite the Phase 3 §3.1 state key by name

Every row must have a derivation citation. UNKNOWN if not traceable.

**4.2 Issue Flags**
Evaluate all four categories, citing prior phase findings:

- **Unnecessary re-renders:** cite Phase 3 §3.2 rows
- **Missing loading states:** list all MISSING-LOADING tokens from Phases 2–3
- **Error state gaps:** list all MISSING-ERROR tokens from Phases 2–3
- **Accessibility failures:** keyboard coverage, focus management, ARIA updates

For each category with no findings: "None found — supported by [cite Phase 3 rows]."

**4.3 Optimization Opportunities**
For each unnecessary re-render in 4.2: name the component, the optimization type,
and the expected render reduction. If no unnecessary re-renders exist: state this
and cite the Phase 3 §3.2 SKIPPED rows.

**4.4 Framework Notes**
Translate the neutral vocabulary used in Phases 1–3 into framework-specific terms.
Map each neutral term to its framework equivalent.
This is the only section where framework-specific terms appear.

**GATE 4 (Final):** Stamp:
`TRACE COMPLETE — 4 phases | UNKNOWN: {N} | MISSING-LOADING: {M} | MISSING-ERROR: {P} | Issues: {K}`

List any open UNKNOWN tokens that require follow-up investigation.
```

---

## V-04 — Combined: Role Sequence + Output Format

**Hypothesis:** The vocabulary lock from V-01 plus the STATUS-column schema from V-02 address C-13 and C-12 simultaneously through different mechanisms — the role contract prevents jargon from entering core sections; the schema catches any that leak through. Together they are mutually reinforcing rather than redundant.

---

```
You are executing a two-role sequence followed by a structured trace output.
Complete Role 1 before producing any trace content.

---

### ROLE 1 — Vocabulary Contract Establishment

Identify the frontend framework from the provided context.

Produce the Vocabulary Contract:

| Framework-Specific Term | Neutral Equivalent | Allowed In Core Sections? |
|-------------------------|--------------------|--------------------------|
| (list all terms you anticipate) | (neutral form) | NO — Framework Notes only |

Rules for the contract:
- Every framework-specific term you expect to use must appear here.
- Terms with no neutral equivalent: mark FRAMEWORK-ONLY in the third column.
- The Allowed In Core Sections column must read NO for every row.

Stamp: **CONTRACT LOCKED — {framework} | {N} terms mapped | {M} FRAMEWORK-ONLY**

Do not begin trace sections until this stamp is written.

---

### ROLE 2 — Trace Analyst (STATUS-Column Schema)

Trace this user action:

[USER ACTION PLACEHOLDER]

**Vocabulary constraint active:** core sections use only neutral equivalents from the Contract.
Framework-specific terms appear only in §8 Framework Notes.

Each section uses a table with a mandatory STATUS column.

**STATUS values:**
- `CONFIRMED` — from direct source inputs
- `INFERRED` — logically necessary; source not directly available
- `UNKNOWN` — cannot be determined; reason required in Notes
- `MISSING-LOADING` — loading branch expected but unconfirmed
- `MISSING-ERROR` — error branch expected but unconfirmed

Every row must have a STATUS. A row without STATUS is a violation.

---

**§1 Event Chain**

| Step | Handler / Listener | Dispatches To | STATUS | Notes |
|------|--------------------|---------------|--------|-------|

Rules: Use neutral vocabulary from Contract. Show DISPATCH rows. Mark gaps UNKNOWN.
Do not end the table until the chain reaches the first component's internal logic.

---

**§2 Component Tree**

| Hop | From | To | Direction | Carrier | STATUS | Notes |
|-----|------|----|-----------|---------|--------|-------|

Direction: `parent→child` | `child→parent` | `sibling` | `context broadcast`
Carrier: the prop or callback name from the Contract's neutral vocabulary.

---

**§3 State Delta**

| State Key | Before | After | Derived Dependents | STATUS | Notes |
|-----------|--------|-------|--------------------|--------|-------|

Mark loading states MISSING-LOADING, error states MISSING-ERROR, unknowns UNKNOWN.

---

**§4 Re-render List**

| Component | Re-renders? | Reason | Guard / Memo | STATUS | Notes |
|-----------|-------------|--------|--------------|--------|-------|

Every component from §2 must appear. SKIPPED components are required entries.
Re-renders? values: `YES` | `NO (memoized)` | `NO (selector equal)` | `NO (gate)`

---

**§5 Side Effects**

| Effect | Owner | Fires | On Complete | Loading Branch | Error Branch | STATUS |
|--------|-------|-------|-------------|----------------|--------------|--------|

Loading Branch / Error Branch: MISSING-LOADING / MISSING-ERROR if unconfirmed.

---

**§6 Issue Flags**

For each category, state findings or clear with evidence:

**6a Unnecessary re-renders** — cite §4 YES rows. Recommend optimization per component.
**6b Missing loading states** — list all MISSING-LOADING tokens from §3 and §5.
**6c Error state gaps** — list all MISSING-ERROR tokens from §3 and §5.
**6d Accessibility** — keyboard coverage, focus, ARIA updates.

"None found" requires citing the §4 or §5 rows that support clearance.

---

**§7 Final UI State**

| UI Element | Property | Value | Source (§3 key) | STATUS |
|------------|----------|-------|-----------------|--------|

Every row must cite a §3 state key. UNKNOWN if derivation cannot be traced.

---

**§8 Optimization Opportunities**

For unnecessary re-renders from §6a: component + optimization type + expected render reduction.
If §4 has no avoidable YES rows: state this and cite the SKIPPED rows.
This section must not be absent without justification.

---

**§9 Framework Notes**

Framework-specific translation of the trace. Only section where Contract terms appear.
Map each neutral term from §1–§7 back to its framework equivalent.

---

**Trace Manifest** (append after §9):

```
VOCABULARY CONTRACT: {N} terms | FRAMEWORK-ONLY: {M}
STATUS TOKENS: UNKNOWN={A} | MISSING-LOADING={B} | MISSING-ERROR={C}
CONTRACT VIOLATIONS IN §1-§7: {count} (list if > 0)
RE-RENDERS: {total YES} | unnecessary candidates: {count}
ISSUES FLAGGED: {count} across {categories}
```
```

---

## V-05 — Combined: Role Sequence + Output Format + Lifecycle Phases

**Hypothesis:** All three axes together produce the highest-fidelity trace by layering: vocabulary lock (prevents C-13 violations), STATUS columns (catches C-12 silent omissions), and phase gates (enforces C-11 cross-section chaining through explicit citations at each boundary).

---

```
You are executing a phased component trace with a vocabulary contract and structured schema.

Three constraints are active simultaneously:

1. **Vocabulary Contract** — framework-specific terms are banned from core sections.
   They appear only in the Framework Notes phase.

2. **STATUS Schema** — every table row has a STATUS column that must be populated.
   STATUS values: CONFIRMED | INFERRED | UNKNOWN | MISSING-LOADING | MISSING-ERROR

3. **Phase Gates** — each phase ends with a stamped gate. Later phases must cite
   earlier gates by name. Cross-section evidence chaining is mandatory, not optional.

---

## Initialization — Vocabulary Contract

Before any trace content, establish the vocabulary contract for this trace.

Identify the framework from provided context. Then:

| Framework Term | Neutral Equivalent | Core Section Usage |
|----------------|--------------------|--------------------|
| (list all anticipated terms) | (neutral form) | PROHIBITED |

Stamp: **CONTRACT LOCKED — {framework} | {N} terms mapped**

USER ACTION TO TRACE: [USER ACTION PLACEHOLDER]

---

## Phase 1 — Trigger Resolution

Using only Contract-approved neutral vocabulary:

**Table 1.1 — Entry Event and First Handler**

| Entry | Handler | Fires Sync? | STATUS | Notes |
|-------|---------|-------------|--------|-------|

**Table 1.2 — Event Chain to Component Boundary**

| Step | Handler | Dispatches To | STATUS | Notes |
|------|---------|---------------|--------|-------|

Rules: No row without STATUS. If the chain reaches an unresolvable step: STATUS=UNKNOWN,
Notes must state the reason. Do not end the table by omission.

**GATE 1:** `PHASE 1 COMPLETE — entry confirmed at [handler name] | chain: {N} steps | UNKNOWN: {M}`
or `PHASE 1 BLOCKED — [reason] — continuing with UNKNOWN placeholders at step {N}`

---

## Phase 2 — Component Propagation

Open with: "Continuing from GATE 1: chain ends at [handler name]."

**Table 2.1 — Component Tree Traversal**

| Hop | From | To | Direction | Carrier (neutral) | STATUS | Notes |
|-----|------|----|-----------|-------------------|--------|-------|

**Table 2.2 — State Keys Encountered**

| State Key | Owner Component | Current Value | STATUS | Notes |
|-----------|----------------|---------------|--------|-------|

Mark: UNKNOWN if value indeterminate | MISSING-LOADING if loading branch unconfirmed |
MISSING-ERROR if error branch unconfirmed.

**GATE 2:** `PHASE 2 COMPLETE — {N} components | {M} state keys | MISSING tokens: {K} | cites GATE 1`

---

## Phase 3 — State and Render Resolution

Open with: "Following GATE 2: {M} state keys identified, {K} MISSING tokens pending."

**Table 3.1 — State Delta**

| State Key | Before | After | Derived Dependents | STATUS | Notes |
|-----------|--------|-------|--------------------|--------|-------|

Every key from Table 2.2 must appear here. A key absent from 3.1 is a gap.

**Table 3.2 — Re-render Cascade**

| Component | Re-renders? | Reason | Guard / Memo | STATUS | Notes |
|-----------|-------------|--------|--------------|--------|-------|

Every component from Table 2.1 must appear here.
SKIPPED components are required entries — not optional.

**Table 3.3 — Side Effects**

| Effect | Owner | Fires | On Complete: Updates | Loading Branch | Error Branch | STATUS |
|--------|-------|-------|----------------------|----------------|--------------|--------|

Loading Branch / Error Branch: populate or mark MISSING-LOADING / MISSING-ERROR.

**GATE 3:** `PHASE 3 COMPLETE — {N} state keys resolved | {M} re-renders | {K} effects | UNKNOWN: {A} | MISSING: {B} | cites GATE 2`

---

## Phase 4 — Output and Analysis

Open with: "From GATE 3: {M} re-renders, {K} side effects, {B} MISSING tokens to resolve."

**Table 4.1 — Final UI State**

| UI Element | Property | Value | Derives From (§3.1 key) | STATUS |
|------------|----------|-------|-------------------------|--------|

Every row must cite a Table 3.1 state key. UNKNOWN if unresolvable.

**4.2 Issue Analysis**

For each category: cite prior-phase tables by table number and row.

- **Unnecessary re-renders:** cite Table 3.2 YES rows. State optimization + expected reduction.
- **Missing loading states:** list all MISSING-LOADING tokens from Tables 3.1 and 3.3.
- **Error state gaps:** list all MISSING-ERROR tokens from Tables 3.1 and 3.3.
- **Accessibility:** evaluate keyboard, focus, ARIA against Tables 2.1 and 3.2.

"None found" requires: table number + row range supporting the clearance.

**4.3 Optimization Opportunities**

For each unnecessary re-render from 4.2: component + optimization type + expected reduction.
If Table 3.2 has no avoidable YES rows: "No optimization opportunities — supported by Table 3.2
rows [list]." This section must not be absent.

**GATE 4 (Final):**
`TRACE COMPLETE — 4 phases | CONTRACT VIOLATIONS: {N} | UNKNOWN: {A} | MISSING-LOADING: {B} | MISSING-ERROR: {C} | ISSUES: {K} | cites GATES 1-3`

**4.4 Framework Notes**

Framework-specific translation of the full trace.
This is the only section where framework-specific vocabulary from the Contract appears.
Map each neutral term used in Tables 1.1–4.1 to its framework equivalent.
```

---

## Round 3 Variation Summary

| Variation | Axis | Primary Hypothesis | Key C-Target |
|-----------|------|--------------------|--------------|
| V-01 | Role sequence | Vocabulary Police role before Trace Analyst locks neutral contract before writing begins | C-13 |
| V-02 | Output format | STATUS column on every table row makes silent omission a schema violation | C-12, C-10 |
| V-03 | Lifecycle emphasis | Phase gates with mandatory GATE stamps force cross-section citation at each boundary | C-11, C-12 |
| V-04 | Role + Format | Contract lock + STATUS schema reinforce each other: prevention + detection | C-13 + C-12 |
| V-05 | Role + Format + Lifecycle | Full combination: prevention (C-13), detection (C-12), chaining (C-11) via layered constraint | C-11 + C-12 + C-13 |
