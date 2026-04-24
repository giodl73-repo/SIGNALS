## trace-component Variations — Round 4 (V-01 through V-05)

---

## V-01 — Axis: Role Sequence (Vocabulary Contract as R1 blocking gate)

**Hypothesis**: Making the Vocabulary Contract the *mandatory first artifact* produced by a dedicated Role 1 — with all downstream roles explicitly bound to its neutral column — closes the escape route where vocabulary intent is stated but trace body sections still drift into framework jargon. The audit in Role 3 cannot be skipped because it exists as a named role, not an instruction buried in a later section.

---

```
Trace a user action through the UI component tree, state management layer, and render cycle.

You will run as three sequential roles. Role 1 must complete its full output before Role 2 begins.
Role 3 audits Role 2's output before the artifact is finalized.

---

ROLE 1 — VOCABULARY ARCHITECT

Your only job is to produce the Vocabulary Contract for this trace. Do not begin tracing yet.

Examine the codebase context provided. Identify every framework-specific term that will appear
in this trace: event primitives, lifecycle hooks, state primitives, component annotations,
binding mechanisms, render triggers. For each term, produce a framework-neutral equivalent.

Output format — a named artifact titled exactly:

  ## Vocabulary Contract

  | Framework Term | Neutral Equivalent | Notes |
  |----------------|--------------------|-------|
  | ...            | ...                | ...   |

Rules:
- Every framework-specific term you expect to use in Sections 1–7 must appear in this table.
- The Neutral Equivalent column is what Sections 1–7 will use. The Framework Term column is
  reserved for Section 8 only.
- If a term has no neutral equivalent (proper name, component name), note it as PASS-THROUGH
  in the Notes column. Pass-through terms may appear in core sections.
- This table is a binding contract. Do not proceed to Role 2 until the table is complete.

---

ROLE 2 — TRACE AUTHOR

You are writing the trace artifact. The Vocabulary Contract produced by Role 1 is your binding
constraint. Before writing any section, re-read the Neutral Equivalent column. Sections 1–7
use neutral vocabulary only.

Produce the following sections in order. Each section header is mandatory even if content
is sparse — mark sparse sections with explicit UNKNOWN or MISSING tokens (never omit them).

---

### §1 — Event Chain

List every handler, middleware, and listener that fires between the user action and final UI
state. Causal order is required. If handler A dispatches to handler B, show the dispatch
step between them as a row.

Table format:

  | Step | Handler / Listener | Trigger | Dispatches To | Owner |
  |------|--------------------|---------|---------------|-------|

Use neutral vocabulary per the Vocabulary Contract. If a step's behavior cannot be determined
from available inputs, insert: UNKNOWN — [reason].

---

### §2 — Component Tree Traversal

Name every component involved in the action flow. Show direction of signal propagation for
each hop: parent→child (via named prop), child→parent (via named callback), sibling (via
named shared-state access). Use exact codebase names.

Table format:

  | From | To | Signal Direction | Carrier Name | Signal Type |
  |------|----|-----------------|--------------|-------------|

---

### §3 — State Delta

For every state update triggered by the action, show the state key or slice, value before,
and value after. List any derived state or selectors that depend on the changed key.

Table format:

  | State Key / Slice | Before | After | Derived Dependents |
  |-------------------|--------|-------|--------------------|

---

### §4 — Re-render List

Enumerate every component that re-renders. For each: reason it re-rendered (prop change,
context change, subscription). Then enumerate every component that did NOT re-render due to
memoization or selector equality, citing which mechanism caused the skip.

Table format:

  | Component | Re-renders? | Reason | Memoization Mechanism (if skipped) |
  |-----------|-------------|--------|-------------------------------------|

---

### §5 — Side Effects and Async Calls

List every side effect triggered: API call, subscription update, timer, storage write.
For each: when it fires (sync / deferred), which component or middleware owns it, what UI
state it targets on completion. Name both the success branch and the error branch.

If a loading branch or error branch cannot be confirmed, mark: MISSING-LOADING or
MISSING-ERROR with reason.

---

### §6 — Issue Analysis

Evaluate all four categories. Do not skip any category, even to report "none found."

(a) Unnecessary re-renders — name any component re-rendering without a changed dependency.
(b) Missing loading states — name any async path without a loading signal to the user.
(c) Error state gaps — name any error path that produces no user-visible state.
(d) Accessibility failures — name any interaction that produces no accessible event or role update.

For each issue found: component name, nature of gap, one-line remediation hint.
For each category with no issues: state "none found" with the C-04 or C-05 row that supports it.

---

### §7 — Final UI State

State the observable final UI state after the full trace completes: which elements are
visible or hidden, what text or data is displayed, what interactive state components are in.
Cite the specific §3 row(s) that produce each element of this state.

---

### §8 — Framework Notes

This is the only section where framework-specific terms from the Vocabulary Contract's
Framework Term column may appear. Annotate mechanics that are framework-specific: lifecycle
hook behavior, rendering batching specifics, framework-owned state primitives.

---

ROLE 3 — VOCABULARY AUDITOR

Audit Role 2's artifact against the Vocabulary Contract. Produce a named section:

  ## Vocabulary Audit

  | Section | Violation Found | Framework Term Used | Expected Neutral Term |
  |---------|-----------------|--------------------|-----------------------|

If no violations are found, state: "No vocabulary leakage detected across §1–§7."

Then produce the Completeness Stamp:

  ## Completeness Stamp

  UNKNOWN: [N]
  MISSING-LOADING: [M]
  MISSING-ERROR: [K]
  Issues flagged in §6: [J]

Count every token in the body. The stamp counts must match the body exactly.
If a mismatch exists, correct the stamp and note the correction.
```

---

## V-02 — Axis: Output Format (Table-first, column-contract mandate)

**Hypothesis**: Pre-declaring explicit column schemas for every essential section before any trace content is written forces completeness at the structural level — a missing column entry is a visible hole, not a prose omission. The column definitions themselves encode the criteria, making C-01/C-04 gaps self-auditing without a separate audit role.

---

```
Trace a user action through the UI component tree, state management layer, and render cycle.

## Format Contract

Before producing any trace content, declare the column schema for each required table.
Every essential section uses a table. Prose narrative is permitted only in §6 (Issue Analysis)
and §8 (Framework Notes). A section that substitutes prose for a required table fails the
format contract.

Declare schemas now:

  TABLE-01 (Event Chain): Step | Handler | Trigger | Dispatches To | Owner
  TABLE-02 (Component Tree): From | To | Direction | Carrier | Signal Type
  TABLE-03 (State Delta): State Key | Before | After | Derived Dependents
  TABLE-04 (Re-renders): Component | Re-renders? | Reason | Memoization Mechanism
  TABLE-05 (Side Effects): Effect | Fires When | Owner | Success Target | Error Target

These schemas are fixed. Do not add or remove columns. A cell may contain UNKNOWN,
MISSING-LOADING, or MISSING-ERROR where information cannot be determined — these tokens
are valid cell values. An empty cell is never valid.

---

## §1 — Event Chain  [TABLE-01]

Populate TABLE-01 starting from the user action through every handler, middleware, and
listener to the final UI state. Causal order is required. If handler A dispatches to
handler B, insert a row for the dispatch as a Step entry. Do not collapse steps.

---

## §2 — Component Tree Traversal  [TABLE-02]

Populate TABLE-02 for every component involved. Each prop or callback that carries a signal
across a component boundary occupies its own row. Direction notation:
  PARENT→CHILD: prop pass-down
  CHILD→PARENT: callback invocation
  SIBLING: shared state read/write (name the state key)

Use exact codebase component names. Use framework-neutral signal type terms.

---

## §3 — State Delta  [TABLE-03]

Populate TABLE-03 for every state key or slice that changes. Every row must have a Before
and After value — if the current value is unknown, use UNKNOWN-BEFORE or UNKNOWN-AFTER as
the cell value, not a blank. Derived state that depends on a changed key belongs in the
Derived Dependents column; list all dependents or mark UNKNOWN.

---

## §4 — Re-render List  [TABLE-04]

Populate TABLE-04 with two groups:
  Group A — components that re-render: set Re-renders? = YES, populate Reason.
  Group B — components that did NOT re-render: set Re-renders? = NO, populate
            Memoization Mechanism with the mechanism that caused the skip.

Group B is required. A TABLE-04 with only Group A entries is incomplete. If no components
were skipped by memoization, add a row with Re-renders? = NO and Memoization Mechanism =
"none — no memoized components on this path."

---

## §5 — Side Effects and Async Calls  [TABLE-05]

Populate TABLE-05 for every side effect. The Error Target column must be populated for
every async row — if no error target exists, write MISSING-ERROR: [component or path].
If a loading state is expected but unconfirmed, write MISSING-LOADING in Success Target.

---

## §6 — Issue Analysis

Evaluate all four categories in order. Use this exact structure for each:

  **Unnecessary re-renders**: [finding or "none — supported by TABLE-04 rows: N"]
  **Missing loading states**: [finding or "none — supported by TABLE-05 rows: N"]
  **Error state gaps**: [finding or "none — confirmed in TABLE-05 Error Target column"]
  **Accessibility failures**: [finding or "none — [basis for conclusion]"]

For each issue found: component name, gap description, one-line remediation.

---

## §7 — Final UI State

State the observable final UI state. For each element of the final state, cite the
TABLE-03 row (by State Key) that produces it. Do not assert a final state element that
has no TABLE-03 row. If an expected final state element has no corresponding TABLE-03 row,
mark it UNKNOWN and explain the gap.

---

## §8 — Framework Notes

Framework-specific annotations here. All framework-specific vocabulary (lifecycle hooks,
framework-owned primitives, framework event names) must appear only in this section.
Core table entries (§1–§7) use framework-neutral terms only. If a framework term appeared
in a core table, it should be moved here and the table entry updated to the neutral term.

---

## Completeness Stamp

Conclude with a structured summary block:

  ---
  COMPLETENESS STAMP
  UNKNOWN cells: [count all TABLE-01 through TABLE-05 UNKNOWN entries]
  MISSING-LOADING: [count]
  MISSING-ERROR: [count]
  Issues flagged in §6: [count of non-"none" findings]
  Tables populated: [N]/5 required tables
  ---

Count every token in the tables above. The stamp numbers must match the table contents.
```

---

## V-03 — Axis: Lifecycle Emphasis (Phase-gate with completion criteria)

**Hypothesis**: Dividing the trace into four named phases — each with explicit completion criteria and a required attestation before the next phase opens — prevents the common failure mode of stopping after the happy-path state delta without completing the analysis and validation phases. The Phase-Complete gate creates a natural audit point at each boundary.

---

```
Trace a user action through the UI component tree, state management layer, and render cycle.

The trace is divided into four phases. Each phase has completion criteria. You must produce
a PHASE-COMPLETE attestation before opening the next phase. A phase cannot be declared
complete unless all criteria are satisfied — missing items must be marked with UNKNOWN or
MISSING tokens, which count as satisfied (gap acknowledged) rather than skipped.

---

## PHASE 1 — VOCABULARY AND SCOPE

Completion criteria for Phase 1:
  [ ] Framework vocabulary table produced (Vocabulary Contract)
  [ ] User action and system boundary named
  [ ] Entry component and entry state identified

### 1.1 — Vocabulary Contract

Produce a table mapping every framework-specific term in this codebase to its
framework-neutral equivalent. Sections in Phase 2 use neutral terms only.

  | Framework Term | Neutral Equivalent |
  |----------------|--------------------|

### 1.2 — Action Scope

State:
  - The exact user action being traced
  - The entry component (first component to receive the event)
  - The system boundary (where the trace ends — final UI state, network call return,
    or explicit scope limit)
  - Known initial state at trace entry

---

PHASE-COMPLETE 1: [ ] Vocabulary Contract produced | [ ] Scope defined | [ ] Entry state named

---

## PHASE 2 — CORE TRACE

Completion criteria for Phase 2:
  [ ] §1 Event chain covers entry to boundary with no unmarked gaps
  [ ] §2 Component tree shows direction and carrier for each hop
  [ ] §3 Every state change has before/after values (UNKNOWN-BEFORE/AFTER accepted)
  [ ] §4 Re-render list includes both YES and NO groups

### §1 — Event Chain

Causal-order list of every handler, middleware, and listener from user action to system
boundary. Each dispatch between handlers is a separate step. Gaps marked UNKNOWN with reason.

### §2 — Component Tree Traversal

Every component on the signal path. For each hop: direction (parent→child / child→parent /
sibling), carrier name (prop, callback, state key), exact codebase component names.

### §3 — State Delta

Every state key that changes. Before value, after value, derived dependents. Unknown values
marked UNKNOWN-BEFORE or UNKNOWN-AFTER, not omitted.

### §4 — Re-render List

Components that re-render: reason (prop change / context change / subscription).
Components that did NOT re-render: memoization mechanism that caused the skip.
Both groups required. If no skipped components: state explicitly with reason.

---

PHASE-COMPLETE 2: [ ] Event chain complete | [ ] Component tree traversal complete |
                  [ ] State delta complete | [ ] Re-render list has both groups

---

## PHASE 3 — DEPTH ANALYSIS

Completion criteria for Phase 3:
  [ ] §5 Every async side effect has both success and error branches named
  [ ] §6 All four issue categories evaluated (none-found findings cite Phase 2 rows)
  [ ] §7 Final UI state elements each cite a §3 row

### §5 — Side Effects and Async Calls

Every side effect: when it fires, owner, success target, error target. Missing branches
marked MISSING-LOADING or MISSING-ERROR with reason. No async row may have a blank
error branch.

### §6 — Issue Analysis

Evaluate in order. Each category requires a finding or a supported "none found":

  (a) Unnecessary re-renders — cite §4 rows
  (b) Missing loading states — cite §5 rows
  (c) Error state gaps — cite §5 error column
  (d) Accessibility failures — cite §2 rows

For each issue: component name, gap description, remediation hint (one line).
For each "none found": cite the specific Phase 2 rows that support the conclusion.

### §7 — Final UI State

Observable final state after trace completes. Each element cites the §3 row that produces it.
Elements without a §3 row are marked UNKNOWN with explanation.

---

PHASE-COMPLETE 3: [ ] All side effects have error branches or MISSING-ERROR |
                  [ ] All four issue categories addressed | [ ] Final state cites §3 rows

---

## PHASE 4 — VALIDATION AND STAMP

Completion criteria for Phase 4:
  [ ] §8 Framework notes present
  [ ] Optimization section present or explicitly waived
  [ ] Completeness Stamp matches body token counts
  [ ] Vocabulary audit confirms no leakage into §1–§7

### §8 — Framework Notes

Framework-specific annotations. All framework vocabulary from the Vocabulary Contract
appears only here. If a framework term appeared in §1–§7, flag it here and note the
correction.

### §9 — Optimization Opportunities

At least one concrete suggestion: memoization candidate (name component + expected
render reduction), batching opportunity, or render-scope reduction. If no unnecessary
re-renders were found in §6(a), state this explicitly and cite the §4 rows.

### Vocabulary Leakage Audit

Review §1–§7. List any framework-specific terms found outside §8. For each: section,
term, correction. If none: "No vocabulary leakage detected."

### Completeness Stamp

  ---
  UNKNOWN: [count all UNKNOWN tokens in body]
  MISSING-LOADING: [count]
  MISSING-ERROR: [count]
  Issues flagged (§6): [count of non-"none" findings]
  ---

Count tokens in the body above. Stamp must match exactly.

---

PHASE-COMPLETE 4: [ ] Framework notes written | [ ] Optimization addressed |
                  [ ] Vocabulary audit complete | [ ] Stamp counts match body
```

---

## V-04 — Combination Axis: Role Sequence + Output Format (Vocabulary Contract gate + pre-declared table schemas)

**Hypothesis**: Pre-committing both the vocabulary binding (Role 1 contract) AND the structural completeness contract (column schemas declared before any content) creates two orthogonal forcing functions: Role 1 makes C-13/C-14 violations detectable at the schema level, and the column declarations make C-10 gaps self-evident before a trace row is written. The combination is stronger than either axis alone because vocabulary drift and structural omission are the two most common independent failure modes.

---

```
Trace a user action through the UI component tree, state management layer, and render cycle.
Three roles run in sequence. Role 1 output is a binding constraint on Role 2 structure.
Role 3 validates both bindings before the artifact is finalized.

---

ROLE 1 — CONTRACT ARCHITECT

Your output is two artifacts: the Vocabulary Contract and the Table Schema Declaration.
Do not begin tracing. Role 2 may not proceed until both artifacts are complete.

### Vocabulary Contract

Identify every framework-specific term that will appear in this trace. Map each to its
framework-neutral equivalent.

  ## Vocabulary Contract

  | Framework Term | Neutral Equivalent | Pass-through? |
  |----------------|--------------------|---------------|

Pass-through = YES means the term is a proper name (component name, API endpoint) with no
neutral substitute. Pass-through terms may appear in core sections. All other framework
terms are banned from §1–§7.

### Table Schema Declaration

Declare the exact column schema for every table Role 2 will produce. These schemas are fixed
and cannot be changed by Role 2.

  TABLE-01 — Event Chain
    Columns: Step | Handler (neutral term) | Trigger | Dispatches To | Owner

  TABLE-02 — Component Tree
    Columns: From | To | Direction | Carrier (neutral term) | Signal Type (neutral term)

  TABLE-03 — State Delta
    Columns: State Key | Before | After | Derived Dependents

  TABLE-04 — Re-render List
    Columns: Component | Re-renders? | Reason (neutral term) | Memoization Mechanism

  TABLE-05 — Side Effects
    Columns: Effect (neutral term) | Fires When | Owner | Success Target | Error Target

Annotate each column that requires neutral vocabulary with "(neutral term)". Role 2 must
use the Vocabulary Contract's Neutral Equivalent column for all cells so annotated.

---

ROLE 2 — TRACE AUTHOR

Constraints inherited from Role 1:
  1. Use Neutral Equivalent terms in all §1–§7 cells marked "(neutral term)" in Table Schema Declaration.
  2. Do not add or remove columns from the declared schemas.
  3. Every cell in every table must contain a value — UNKNOWN, MISSING-LOADING, or MISSING-ERROR
     are valid cell values; blank cells are invalid.

---

### §1 — Event Chain  [TABLE-01]

Populate TABLE-01 in causal order from user action to system boundary.
Each dispatch between handlers is its own row. Do not collapse adjacent steps.

### §2 — Component Tree Traversal  [TABLE-02]

Populate TABLE-02 for every component on the signal path.
Direction values: PARENT→CHILD / CHILD→PARENT / SIBLING.
Carrier column: name the prop, callback, or state key. Use neutral term.

### §3 — State Delta  [TABLE-03]

Populate TABLE-03 for every state key that changes.
Unknown values: UNKNOWN-BEFORE / UNKNOWN-AFTER in the relevant cell.
Derived Dependents: all selectors or computed values that depend on the changed key,
or UNKNOWN if not determinable.

### §4 — Re-render List  [TABLE-04]

Two groups required:
  Group A (Re-renders? = YES): reason column required.
  Group B (Re-renders? = NO): Memoization Mechanism column required.
If Group B is empty: add one row with Re-renders? = NO and Memoization Mechanism =
"none — no memoized components on this signal path."

### §5 — Side Effects  [TABLE-05]

Every async effect requires both Success Target and Error Target populated.
Missing branches: MISSING-LOADING (Success Target) or MISSING-ERROR (Error Target).

### §6 — Issue Analysis

Evaluate all four categories. Use neutral terms. Cite TABLE row numbers for each finding
and for each "none found" conclusion.

  (a) Unnecessary re-renders:
  (b) Missing loading states:
  (c) Error state gaps:
  (d) Accessibility failures:

### §7 — Final UI State

State the observable final UI state. Each element cites its TABLE-03 row by State Key.
Elements without a TABLE-03 row are marked UNKNOWN-FINAL with explanation.

### §8 — Framework Notes

Framework-specific terms from the Vocabulary Contract appear here only.
Annotate framework mechanics not captured by the neutral-vocabulary tables above.

---

ROLE 3 — CONTRACT AUDITOR

Produce two audit sections and the Completeness Stamp.

### Vocabulary Audit

Re-read §1–§7. List any cell or narrative text containing a term from the Vocabulary Contract's
Framework Term column (excluding Pass-through terms).

  | Section | Table | Cell | Framework Term Found | Required Neutral Term |
  |---------|-------|------|---------------------|----------------------|

If no violations: "Vocabulary Contract fully enforced across §1–§7."

### Schema Audit

Confirm that Role 2's tables match the declared schemas:
  - No added columns
  - No removed columns
  - No blank cells

List any deviation. If none: "Table schemas match Role 1 declaration."

### Completeness Stamp

  ---
  UNKNOWN: [count all UNKNOWN tokens across §1–§7 tables and §7 narrative]
  MISSING-LOADING: [count]
  MISSING-ERROR: [count]
  Issues flagged (§6): [count of non-"none" findings]
  Vocabulary violations: [count from Vocabulary Audit]
  Schema deviations: [count from Schema Audit]
  ---
```

---

## V-05 — Combination Axis: Lifecycle Emphasis + Phrasing Register (imperative phase gates)

**Hypothesis**: Imperative register ("You MUST produce X before Y is permitted") combined with phase-gate attestations creates unambiguous failure conditions where a model cannot rationalize partial compliance. The phrasing eliminates hedged constructions ("you may wish to…", "consider…") that models exploit to skip non-trivial criteria. The phase gate is the structural enforcement; the imperative register is the disambiguation of what counts as passing the gate.

---

```
You are tracing a user action through a UI component tree, state management layer, and
render cycle. This trace has four phases. You MUST complete each phase fully before
advancing. Advancing without a gate attestation is a trace failure.

---

## PHASE 1 — VOCABULARY LOCK  [GATE: declare before tracing]

You MUST produce the following before writing any trace content:

**1.1 — Vocabulary Contract**

You MUST identify every framework-specific term this trace will use and map it to a
framework-neutral equivalent. Output a named table:

  | Framework Term | Neutral Equivalent |

Every term you use in Phases 2–3 that appears in the Framework Term column MUST appear
in its Neutral Equivalent form in Sections §1–§7. Framework terms are permitted ONLY in §8.
This is not optional. There is no exception for "well-known" terms.

**1.2 — Entry Scope**

You MUST state:
  - The exact user action (not a paraphrase)
  - The first component that receives the event (exact codebase name)
  - The entry state values relevant to this action
  - The scope boundary (where this trace ends)

**GATE 1 ATTESTATION**: "Vocabulary Contract complete. Scope defined. Phase 2 permitted."

Do not write §1 until you have written GATE 1 ATTESTATION.

---

## PHASE 2 — CORE TRACE  [GATE: all essential sections complete]

You MUST produce all four essential sections. No section may be omitted or compressed into
another section. Every gap MUST be marked with an explicit token (UNKNOWN, MISSING-LOADING,
MISSING-ERROR). A missing section row is not a gap — it is a failure to enumerate.

**§1 — Event Chain**

You MUST list every handler, middleware, and listener that fires between the user action
and the scope boundary, in causal order. If handler A dispatches to handler B, you MUST
show the dispatch as an explicit step. You MUST NOT compress two steps into one.

Produce a table:
  | Step | Handler | Trigger | Dispatches To | Owner |

Use neutral vocabulary per the Vocabulary Contract. Any step whose behavior is unknown
MUST carry an UNKNOWN token in the Handler cell — do not end the table early.

**§2 — Component Tree Traversal**

You MUST name every component involved. For each hop you MUST state:
  - Direction: PARENT→CHILD, CHILD→PARENT, or SIBLING
  - Carrier: the exact prop, callback, or state key that moves the signal
  - Exact codebase component names on both ends

Produce a table:
  | From | To | Direction | Carrier | Signal Type |

**§3 — State Delta**

You MUST list every state key that changes. For each you MUST provide:
  - The state key or slice name
  - The value before (UNKNOWN-BEFORE if not determinable — do NOT omit the row)
  - The value after (UNKNOWN-AFTER if not determinable)
  - Derived state that depends on this key

Produce a table:
  | State Key | Before | After | Derived Dependents |

**§4 — Re-render List**

You MUST list every component that re-renders AND every component that did NOT re-render
due to memoization or selector equality. Omitting the skipped-components group is a
section failure. If no components were skipped, you MUST state this explicitly with reason.

Produce a table:
  | Component | Re-renders? | Reason | Memoization Mechanism |

**GATE 2 ATTESTATION**: "Event chain complete. Component tree complete. State delta complete.
Re-render list includes both groups. All gaps marked. Phase 3 permitted."

Do not write §5 until you have written GATE 2 ATTESTATION.

---

## PHASE 3 — DEPTH AND ANALYSIS  [GATE: every async effect and every issue category addressed]

**§5 — Side Effects and Async Calls**

You MUST list every side effect triggered (API call, subscription, timer, storage write).
For every async effect you MUST name both the success branch and the error branch.
You MUST NOT leave the error branch empty. If no error branch exists: MISSING-ERROR with reason.
If a loading state is expected but unconfirmed: MISSING-LOADING with reason.

Produce a table:
  | Effect | Fires When | Owner | Success Target | Error Target |

**§6 — Issue Analysis**

You MUST evaluate all four categories. You MUST NOT skip a category because you expect it
to be empty — evaluate it and produce a supported conclusion.

(a) Unnecessary re-renders — You MUST cite §4 rows. A conclusion of "none" requires
    naming the §4 rows that confirm no component re-rendered without a changed dependency.

(b) Missing loading states — You MUST cite §5 rows. A "none" conclusion requires naming
    every async §5 row and confirming each has a success target.

(c) Error state gaps — You MUST cite §5 error column. A "none" conclusion requires
    confirming every §5 async row has a non-MISSING error target.

(d) Accessibility failures — You MUST state the basis for your conclusion. "None found"
    without a basis is a failing response.

For each issue found: component name, gap description, one-line remediation.

**§7 — Final UI State**

You MUST describe the observable final UI state. For each element you MUST cite the §3
State Key that produces it. You MUST NOT assert a final state element that has no §3 row.
Elements with no §3 row MUST be marked UNKNOWN-FINAL with explanation.

**GATE 3 ATTESTATION**: "All side effects enumerated with error branches or MISSING tokens.
All four issue categories addressed with cited evidence. Final state cites §3 rows.
Phase 4 permitted."

Do not write §8 until you have written GATE 3 ATTESTATION.

---

## PHASE 4 — FRAMEWORK ANNOTATION AND STAMP  [GATE: audit and stamp complete]

**§8 — Framework Notes**

You MUST annotate framework-specific mechanics here. This is the ONLY section where
terms from the Vocabulary Contract's Framework Term column may appear. You MUST check
§1–§7 for vocabulary leakage and note any violations found here.

**§9 — Optimization Opportunities**

You MUST identify at least one concrete optimization (memoization candidate, batching
opportunity, render-scope reduction) OR explicitly state why none exists by citing the
relevant §4 and §6(a) rows. A silently absent §9 is a section failure.

**Vocabulary Leakage Audit**

You MUST review §1–§7 for framework terms from the Vocabulary Contract. Report:
  | Section | Term Found | Required Neutral Replacement |

If none: "No vocabulary leakage detected in §1–§7."

**Completeness Stamp**

You MUST produce this stamp as the final element of the artifact. Count every token.
The stamp numbers MUST match the body:

  ---
  COMPLETENESS STAMP
  UNKNOWN: [N]
  MISSING-LOADING: [M]
  MISSING-ERROR: [K]
  Issues flagged (§6): [J]
  Vocabulary violations: [V]
  ---

**GATE 4 ATTESTATION**: "Framework notes written. Optimization addressed. Vocabulary audit
complete. Completeness Stamp produced and counts verified against body."
```

---

## Variation Summary

| Variation | Axis | Core Bet | Key C-14/C-15 Mechanism |
|-----------|------|----------|------------------------|
| V-01 | Role sequence | Vocabulary Contract as R1 blocking artifact; Role 3 audits for leakage | C-14: Role 1 produces named table; Role 3 audits. C-15: Role 3 stamp |
| V-02 | Output format | Pre-declared column schemas make gaps structurally visible without an audit role | C-14: implicit via column neutrality annotation. C-15: structured stamp |
| V-03 | Lifecycle emphasis | Four phase gates with explicit completion criteria enforce both trace and validation | C-14: Phase 1 Vocabulary Contract. C-15: Phase 4 stamp with gate |
| V-04 | Role sequence + Output format | Two orthogonal constraints (vocabulary binding + column schemas) close vocabulary drift and structural omission independently | C-14: Role 1 contract + Role 3 audit. C-15: Role 3 counts tables |
| V-05 | Lifecycle + Phrasing register | Imperative register eliminates hedged compliance; gates create unambiguous failure conditions | C-14: GATE 1 blocks Phase 2 until contract produced. C-15: GATE 4 requires stamp with verified counts |
