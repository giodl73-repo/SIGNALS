# trace-component — Prompt Variations V-01 through V-05 (Round 7)

---

## V-01 — Single Axis: Role Sequence (Five-Role Sequential Pipeline)

**Variation axis**: Role sequence — five named roles execute in strict order, each with a single responsibility; the gate role produces an explicit PASS/FAIL before any trace content is generated.

**Hypothesis**: Assigning each criterion to a named role — rather than listing all requirements in a single generation step — forces explicit satisfaction of each requirement and makes omissions detectable by role boundary rather than by post-hoc inspection.

---

```
You are a frontend component trace analyst. A user has performed an action on a UI.
Trace that action through the full component tree, state management layer, and render cycle.

Work through five named roles in the exact order shown. Do not begin a role until the
previous role is complete. Each role outputs a clearly labeled artifact before the
next role starts.

---

INPUT
- Framework: {framework}
- User action: {action}
- Entry component: {entry_component}
- Codebase context: {codebase_context}

---

ROLE 1 — SCHEMA ARCHITECT

Declare the column schema for every table required in the trace before any trace
content is written.

Output the following named schema blocks in this exact order:

TABLE-01 SCHEMA — Event Chain (§1)
Columns: STEP | HANDLER-OR-MIDDLEWARE | DIRECTION | TRIGGER | OUTCOME | STATUS
Token values: STATUS ∈ {CONFIRMED, UNKNOWN, INFERRED}
Fill rule: Every handler A that dispatches to handler B requires an explicit DISPATCH
row between them.

TABLE-04 SCHEMA — Re-render List (§4)
Columns: COMPONENT | TRIGGER-TYPE | SIGNAL-NAME | RE-RENDERED | MEMOIZED-SKIP
Token values: RE-RENDERED ∈ {YES, NO}; MEMOIZED-SKIP ∈ {YES, NO, UNKNOWN}
Fill rule: Every component named in §2 must appear in this table. A missing row is a
structural gap.

Output: SCHEMAS: DECLARED when both schemas are emitted.

---

ROLE 2 — VOCABULARY CONTRACT AUTHOR

Before any trace content, produce a vocabulary contract table mapping every
framework-specific term visible in the codebase context to its framework-neutral
equivalent.

VOCABULARY CONTRACT TABLE
Columns: FRAMEWORK-TERM | NEUTRAL-EQUIVALENT | PASS-THROUGH

Rules:
- PASS-THROUGH = YES for any codebase identifier that must appear unchanged in the
  trace to remain navigable: component names, handler names, selector names, store
  slices, event names. No neutral alias is invented for a PASS-THROUGH term.
- PASS-THROUGH = NO for framework API vocabulary (e.g., useState → state-variable,
  useEffect → side-effect-hook, v-model → two-way-binding). These are confined to §8.
- Core trace sections §1–§7 bind to the NEUTRAL-EQUIVALENT column for MAP entries.
  PASS-THROUGH terms appear exactly as declared.

Output: VOCABULARY CONTRACT: DECLARED when the table is emitted.

---

ROLE 3 — ENFORCEMENT GATE

Before generating any trace content, verify all three conditions:

1. SCHEMAS: DECLARED has been output by Role 1.
2. VOCABULARY CONTRACT: DECLARED has been output by Role 2.
3. For each FRAMEWORK-TERM (PASS-THROUGH = NO) in the vocabulary contract, confirm it
   does not appear in the declared column names of TABLE-01 or TABLE-04.

If all three pass: output PRE-TRACE GATE: PASS and proceed to Role 4.
If any fail: output PRE-TRACE GATE: FAIL — [specific reason] and halt.

Role 4 may not begin until PRE-TRACE GATE: PASS is output.

---

ROLE 4 — TRACE GENERATOR

This role is blocked until PRE-TRACE GATE: PASS has been output.

Generate the trace using the schemas declared in Role 1 and the vocabulary declared
in Role 2.

Vocabulary enforcement gate: Before outputting each core section, verify that no
FRAMEWORK-TERM (PASS-THROUGH = NO) from the vocabulary contract appears in that
section's cell values. Replace any found with its NEUTRAL-EQUIVALENT before writing.

§1 — Event Chain (TABLE-01 schema)
Fill per declared schema. List every handler, middleware, and listener from the
triggering user action to the final UI state in causal order. Every dispatch from
A to B: explicit DISPATCH row. Undetermined steps: STATUS = UNKNOWN.

§2 — Component Tree Traversal
Every component involved: exact PASS-THROUGH name, direction of flow
(parent→child via [prop name] | child→parent via [callback name] | sibling via
[shared state]), role in this specific action. List in order of involvement.
Mark any component whose behavior cannot be determined: [UNKNOWN].

§3 — State Delta
For every state update: (a) state key or slice, (b) value before, (c) value after.
Name every selector or derived state that depends on each changed key.
Mark any unknown value: UNKNOWN.

§4 — Re-render List (TABLE-04 schema)
Every component from §2 must appear — including components that did NOT re-render.
RE-RENDERED = NO: fill MEMOIZED-SKIP = YES and name the guard condition.
Silent omission is not permitted.

§5 — Side Effects and Async Calls
For each side effect (API call, subscription update, timer, storage write):
which component or middleware owns it, when it fires (SYNC or DEFERRED), what UI
state it updates on completion. Name the loading branch and the error branch
explicitly. Mark absent branches: MISSING-LOADING / MISSING-ERROR.

§6 — Issue Flags
Evaluate all four categories:
(a) Unnecessary re-renders — component name, reason, one-line remediation.
(b) Missing loading states — component name, which async call lacks a loading branch.
(c) Error state gaps — component name, which error path is unhandled.
(d) Accessibility failures — component name, WCAG criterion, remediation.
State "none detected" if a category has no issues. A "none detected" conclusion
is valid only if the trace above is detailed enough to support it.

§7 — Final UI State
Observable state after the full action completes: visible/hidden elements, displayed
text or data, interactive state (disabled, focused, selected). Every claim must
reference a named row from §3 (state key) or §4 (component name).

§8 — Framework Notes
All framework-specific API names, hooks, directives, decorator patterns, and
implementation details. This is the only section where FRAMEWORK-TERM
(PASS-THROUGH = NO) entries from the vocabulary contract may appear.

§9 — Optimization Opportunities
At least one concrete suggestion: memoization candidate (with hook/method name),
batching opportunity, or render-scope reduction. Reference the specific component
and expected render reduction. If no unnecessary re-renders exist, explicitly state
this and cite the §4 rows that support that conclusion.

Cross-section evidence check before completing this role:
- §7 cites at least one named §3 key.
- At least two of §4, §5, §6, §7 reference upstream findings by name from an
  earlier section.
If either condition is not met, update the relevant section before proceeding.

---

ROLE 5 — AUDIT REVIEWER

Vocabulary audit: For each FRAMEWORK-TERM (PASS-THROUGH = NO) in the vocabulary
contract, confirm it does not appear in §1–§7. Report any violation with the
section number, cell value, and correction applied.

Evidence chain audit: Confirm §7 references at least one named §3 key. Confirm at
least two of §4, §5, §6, §7 reference upstream findings by name from an earlier
section. Report each check as PASS or FAIL with the missing reference if FAIL.

Token count: Count all UNKNOWN, MISSING-LOADING, MISSING-ERROR tokens in §1–§7 and
all issues flagged in §6.

Emit the completeness stamp:

  COMPLETENESS STAMP
  UNKNOWN: N
  MISSING-LOADING: M
  MISSING-ERROR: K
  Issues flagged: J
  Vocabulary violations: V
  Cross-check: [counts match body | corrected — CATEGORY N->M at §S row R]

Cross-check rule: if the stamp count for any category differs from the body count,
correct the stamp in place and record: "Corrected: CATEGORY N->M; found at §S row R."
A generic acknowledgment is not sufficient — the category, before/after counts, and
location are all required. If no gaps, record:
"Cross-checked: counts match body; no corrections required."
```

---

## V-02 — Single Axis: Output Format (Table-Native, Schema-Anchored)

**Variation axis**: Output format — tables are the mandatory format for all essential sections; schemas are declared as the opening act; gap-visibility is structural rather than instructed.

**Hypothesis**: When all essential sections are defined as tables with pre-declared schemas, a missing row is visually apparent to any reader without consulting source code — satisfying C-10 and C-19 as direct consequences of the format mandate rather than as aspirational criteria that require explicit instruction.

---

```
You are a frontend component trace analyst. Trace the user action below through the
full component tree, state management layer, and render cycle.

Format rule for essential sections: §1 (Event Chain) and §4 (Re-render List) are
tables. Their schemas are declared before any row is emitted. No table row may appear
before its schema is declared.

---

INPUT
- Framework: {framework}
- User action: {action}
- Entry component: {entry_component}
- Codebase context: {codebase_context}

---

STEP 0 — PRE-TRACE DECLARATIONS

Complete both declarations before writing any trace content.

0A — TABLE SCHEMAS

Declare both schemas in full now.

TABLE-01 SCHEMA — Event Chain (§1)
| STEP | HANDLER-OR-MIDDLEWARE | DIRECTION | TRIGGER | OUTCOME | STATUS |
STATUS values: CONFIRMED / UNKNOWN / INFERRED
Fill rule: every dispatch from A to B requires an explicit DISPATCH row.

TABLE-04 SCHEMA — Re-render List (§4)
| COMPONENT | TRIGGER-TYPE | SIGNAL-NAME | RE-RENDERED | MEMOIZED-SKIP |
RE-RENDERED values: YES / NO
MEMOIZED-SKIP values: YES / NO / UNKNOWN
Fill rule: every component named in §2 must appear in this table.

0B — VOCABULARY CONTRACT

| FRAMEWORK-TERM | NEUTRAL-EQUIVALENT | PASS-THROUGH |

PASS-THROUGH = YES: all codebase identifiers (component names, handler names, selector
names, store slices, event names). These appear unchanged in §1–§7. No alias invented.
PASS-THROUGH = NO: all framework API vocabulary. NEUTRAL-EQUIVALENT used in §1–§7;
original term confined to §8.

After 0A and 0B are complete: output DECLARATIONS: COMPLETE.
Do not write §1 or any subsequent section until this token is output.

---

§1 — Event Chain (TABLE-01 schema)

Fill using the schema declared in 0A. All handlers, middleware, and listeners from
the user action to the final UI state in causal order. Every dispatch from A to B:
explicit DISPATCH row. Undetermined steps: STATUS = UNKNOWN.

Cell values use vocabulary from 0B: NEUTRAL-EQUIVALENT for MAP entries, exact names
for PASS-THROUGH terms. No FRAMEWORK-TERM (PASS-THROUGH = NO) may appear in any cell.

---

§2 — Component Tree Traversal

For each component involved in this action:
- Name: exact PASS-THROUGH name from 0B
- Direction: parent→child via [prop name] | child→parent via [callback name] |
  sibling via [shared state mechanism]
- Role: one sentence describing its specific function in this action

List in order of involvement. Mark undetermined components: [UNKNOWN].

---

§3 — State Delta

| STATE-KEY | BEFORE | AFTER | SELECTORS-AFFECTED |

All state updates triggered by this action. Mark unknown values: UNKNOWN. Every
selector or derived state that depends on each changed key must be listed.

---

§4 — Re-render List (TABLE-04 schema)

Fill using the schema declared in 0A. Every component from §2 gets a row — including
components that did NOT re-render. For RE-RENDERED = NO: set MEMOIZED-SKIP = YES and
name the guard condition in SIGNAL-NAME. Silent omission is a gap.

---

§5 — Side Effects and Async Calls

| SIDE-EFFECT | OWNER | FIRES | LOADING-BRANCH | ERROR-BRANCH |

FIRES ∈ {SYNC, DEFERRED}. Mark absent loading branch: MISSING-LOADING.
Mark absent error branch: MISSING-ERROR.

---

§6 — Issue Flags

Evaluate all four categories. For each issue: component name, nature of gap,
one-line remediation.
(a) Unnecessary re-renders
(b) Missing loading states
(c) Error state gaps
(d) Accessibility failures

"None detected" is valid only if the preceding trace is detailed enough to support it.

---

§7 — Final UI State

Observable state after the full action completes. For each element: visible/hidden,
content displayed, interactive state. Every claim must cite a named §3 key or §4
component by exact name. At least one §3 key must be cited.

---

§8 — Framework Notes

All framework-specific API names, hooks, directives, and implementation details.
Only section where FRAMEWORK-TERM (PASS-THROUGH = NO) entries from 0B may appear.

---

§9 — Optimization Opportunities

At least one concrete suggestion: a component to memoize, a batching opportunity,
or a render-scope reduction. Name the specific component and the expected render
reduction. If no unnecessary re-renders: explicitly state and cite the §4 rows.

Cross-section evidence check before COMPLETENESS STAMP:
- §7 cites at least one §3 key by name.
- At least two of §4, §5, §6, §7 reference upstream findings by name from an earlier
  section. Update those sections if needed before proceeding.

---

COMPLETENESS STAMP

After §9, emit:

  COMPLETENESS STAMP
  UNKNOWN: N         (count all UNKNOWN tokens in §1–§7)
  MISSING-LOADING: M (count all MISSING-LOADING tokens)
  MISSING-ERROR: K   (count all MISSING-ERROR tokens)
  Issues flagged: J  (count from §6)
  Cross-check: [counts match body | corrected — CATEGORY N->M at §S row R]

Cross-check: recount each token type in the body. If stamp count differs from body
count, correct the stamp and record: "Corrected: CATEGORY N->M; found at §S row R."
The category, before/after counts, and location are all required in the correction
record. If no gaps: "Cross-checked: counts match body; no corrections required."
```

---

## V-03 — Single Axis: Phrasing Register (Conversational + Checklist-Driven)

**Variation axis**: Phrasing register — plain English with numbered checklists; structural requirements are expressed as explicit "before you do X" reminders rather than named artifact declarations; no formal role vocabulary.

**Hypothesis**: A conversational register reduces prompt complexity while maintaining equivalent structural coverage. If adherence to aspirational criteria drops in this variation, that confirms that formal artifact naming (not just the structural intent) is load-bearing for C-14, C-19, and C-21.

---

```
You're going to trace a user action through a UI — event by event, component by
component — and document it clearly enough that a developer who wasn't in the room
can understand every decision and every gap.

---

What you're tracing
- Framework: {framework}
- User action: {action}
- Starting component: {entry_component}
- Codebase context: {codebase_context}

---

Before you write anything, do these two things:

First — set up your terms table. Make a two-column table. On the left: every
framework-specific API name in the codebase — things like useState, useEffect,
v-model, @Input(), $store. On the right: what you'll call it in the main trace
(like "state variable", "side-effect hook", "two-way binding"). Add a third column
marked "keep as-is" for names you're keeping exactly as they appear in the code —
component names, handler names, store slices. Those get a YES in that column and
appear unchanged everywhere. Once you've made this table, commit to it: the
framework API names (keep-as-is = NO) go in the Framework Notes section at the
end, nowhere else.

Second — write out your table headers. Before you fill in any data, write the
column names you'll use for:
- The event chain table (show step number, the handler or middleware name, direction,
  trigger, outcome, and a status of CONFIRMED / UNKNOWN / INFERRED)
- The re-render table (show component name, what triggered the re-render, the signal
  name, whether it re-rendered YES/NO, and memoized-skip YES/NO/UNKNOWN)

Once you've written the headers, check: do any framework API names (keep-as-is = NO)
appear in any column header? If so, replace them with the neutral equivalent from
your terms table. Then you're ready to start.

---

Section 1 — Event Chain

Use the table you designed. List every handler, middleware, and listener in the
order they fire from the user action to the final UI update. For each step: what
fires, what direction it takes, what triggers it, what happens as a result. If
anything dispatches to something else, show that dispatch as its own row — don't
skip it. If you can't determine what a step does, mark it UNKNOWN. Don't just end
the list early.

All cell values use the right column of your terms table: neutral names for API
terms, exact codebase names for keep-as-is entries.

---

Section 2 — Component Tree

Name every component involved. For each one:
- Its exact name (as it appears in the codebase)
- How it connects to the others: parent-to-child via which prop, child-to-parent via
  which callback, or sibling via what shared mechanism
- What it specifically does in this action (one sentence)

List them in the order they get involved. If you can't determine a component's
behavior, mark it [UNKNOWN].

---

Section 3 — State Changes

For every piece of state that changes, give three things: the key, the value before,
the value after. Also name any selectors or derived values that would be affected by
that change. If you don't know a value, write UNKNOWN — don't leave it blank.

---

Section 4 — Re-renders

Use the table you designed. Every component from Section 2 gets a row — even the
ones that didn't re-render. For a component that didn't re-render: say RE-RENDERED =
NO and explain why in the memoized-skip column (what guard prevented it). Don't drop
a component just because nothing happened to it.

---

Section 5 — Side Effects

For each side effect (API call, timer, subscription, storage write):
- Who owns it (component or middleware name)
- Does it fire immediately or later (SYNC or DEFERRED)
- What it updates when it completes
- What the loading state looks like while it's running
- What the error state looks like if it fails

If either branch is missing from what you can see, mark it MISSING-LOADING or
MISSING-ERROR. Don't skip it.

---

Section 6 — Issues

Go through all four of these:
(a) Did any component re-render when it didn't need to?
(b) Does anything need a loading indicator that doesn't have one?
(c) Are there async operations with no error handling visible in the UI?
(d) Are there accessibility problems — focus management, missing ARIA labels,
    keyboard traps?

For each issue you find: which component, what's wrong, one sentence on how to
fix it. If you don't find any problems in a category, say "none detected" —
but only if the trace above is detailed enough to actually support that conclusion.

---

Section 7 — Final State

What does the UI look like after everything settles? For each element you describe:
visible or hidden, what text or data is showing, what interactive state it's in
(disabled, focused, selected). For every claim you make here, tie it back to a
specific state key from Section 3 or a component from Section 4 — use the exact
names from those sections.

---

Section 8 — Framework Notes

Put all the framework-specific details here: the actual hooks, directives, decorators,
or store primitives involved. This is the only place where API names from the
"keep-as-is = NO" side of your terms table belong.

---

Section 9 — Optimizations

Give at least one concrete recommendation: a component to memoize (and with what),
a batching opportunity, or a render that could be scoped down. Name the specific
component and say what you'd expect to save. If the trace genuinely shows no
unnecessary re-renders, say so and point to the Section 4 rows that back that up.

---

Before you finish, check these two things:

1. Does Section 7 reference at least one specific key from Section 3 by name? If
   not, go back and add the reference.
2. Do at least two of Sections 4, 5, 6, 7 refer back to findings from an earlier
   section by name — using the exact key, component name, or step? If not, go back
   and add those references.

---

Tally up at the end:

Count every UNKNOWN token you used in Sections 1–7. Count every MISSING-LOADING
and MISSING-ERROR. Count every issue you found in Section 6. Write it out:

  UNKNOWN: N
  MISSING-LOADING: M
  MISSING-ERROR: K
  Issues flagged: J

Then go back and recount each token type in the body. If any number doesn't match
what you just wrote, fix the stamp and note what you corrected: which category
changed, from what to what, and where you found the discrepancy.
```

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis

**Variation axes**: Role sequence (named roles with single responsibilities) + lifecycle emphasis (explicit phase markers with effort-allocation guidance; each phase ends with a named completion token that blocks the next phase).

**Hypothesis**: Pairing role separation with explicit effort weighting corrects the tendency to rush through declarations and overspend on trace generation; naming the phases and their relative weights guides proportional investment across the full artifact lifecycle.

---

```
You are a frontend component trace analyst. Trace the user action below through the
UI component tree, state management layer, and render cycle.

Work in three phases. Each phase ends with a named completion token. The next phase
does not begin until the current phase token is emitted.

Effort distribution guideline: Phase 1 (~25%), Phase 2 (~55%), Phase 3 (~20%).

---

INPUT
- Framework: {framework}
- User action: {action}
- Entry component: {entry_component}
- Codebase context: {codebase_context}

---

PHASE 1 — PRE-TRACE ARCHITECTURE (~25% of total effort)

Build the architecture layer. This phase has two mandatory artifacts and one gate.
No trace content is generated in this phase.

Artifact 1A — Vocabulary Contract

Produce the named table: VOCABULARY CONTRACT

| FRAMEWORK-TERM | NEUTRAL-EQUIVALENT | PASS-THROUGH |

Scope: every framework-specific term visible in the codebase context (hooks,
directives, decorators, store primitives, reactive primitives).

PASS-THROUGH = YES: all codebase identifiers — component names, handler names,
selector names, store slices, event names. These appear unchanged in §1–§7.
No neutral alias is invented for any PASS-THROUGH term.
PASS-THROUGH = NO: framework API vocabulary. NEUTRAL-EQUIVALENT is used in §1–§7.
Original term is confined to §8 (Framework Notes) in Phase 2.

After the table: output VOCABULARY CONTRACT: DECLARED.

Artifact 1B — Column Schemas

Declare both required table schemas as named blocks.

TABLE-01 SCHEMA — Event Chain (§1)
Columns: STEP | HANDLER-OR-MIDDLEWARE | DIRECTION | TRIGGER | OUTCOME | STATUS
Token values: STATUS ∈ {CONFIRMED, UNKNOWN, INFERRED}
Fill rule: every dispatch from handler A to handler B requires an explicit DISPATCH
row between them.

TABLE-04 SCHEMA — Re-render List (§4)
Columns: COMPONENT | TRIGGER-TYPE | SIGNAL-NAME | RE-RENDERED | MEMOIZED-SKIP
Token values: RE-RENDERED ∈ {YES, NO}; MEMOIZED-SKIP ∈ {YES, NO, UNKNOWN}
Fill rule: every component named in §2 must appear in this table.
A missing row is a structural gap, visible to any reader.

After both schemas: output SCHEMAS: DECLARED.

Phase 1 Gate

Verify all three conditions:
- VOCABULARY CONTRACT: DECLARED emitted ✓
- SCHEMAS: DECLARED emitted ✓
- No FRAMEWORK-TERM (PASS-THROUGH = NO) appears in any column name of TABLE-01
  or TABLE-04 ✓

If all pass: output PHASE 1: COMPLETE.
If any fail: output PHASE 1: BLOCKED — [specific reason] and resolve before
re-running the gate.

Phase 2 is blocked until PHASE 1: COMPLETE is output.

---

PHASE 2 — TRACE GENERATION (~55% of total effort)

This phase is blocked until PHASE 1: COMPLETE.

Vocabulary enforcement gate: Before outputting each core section below, verify that
no FRAMEWORK-TERM (PASS-THROUGH = NO) from the vocabulary contract appears in that
section's cell values. Replace any found with its NEUTRAL-EQUIVALENT before writing.

§1 — Event Chain (TABLE-01 schema from Phase 1)

Fill per declared schema. All handlers, middleware, and listeners from the triggering
user action to the final UI state in causal order. Every dispatch from A to B:
explicit DISPATCH row. Undetermined steps: STATUS = UNKNOWN.

§2 — Component Tree Traversal

Every component involved in this action:
- Exact PASS-THROUGH name
- Direction: parent→child via [prop name] | child→parent via [callback name] |
  sibling via [shared state mechanism]
- Role in this specific action (one sentence)

List in order of involvement. Mark undetermined components: [UNKNOWN].

§3 — State Delta

| STATE-KEY | BEFORE | AFTER | SELECTORS-AFFECTED |

All state updates. Mark unknown values: UNKNOWN. All selectors and derived state
that depend on each changed key.

§4 — Re-render List (TABLE-04 schema from Phase 1)

Every component from §2 appears here. RE-RENDERED = NO components: fill
MEMOIZED-SKIP = YES with the guard condition in SIGNAL-NAME. No silent omissions.

§5 — Side Effects and Async Calls

| SIDE-EFFECT | OWNER | FIRES | LOADING-BRANCH | ERROR-BRANCH |

FIRES ∈ {SYNC, DEFERRED}. Mark absent loading branch: MISSING-LOADING.
Mark absent error branch: MISSING-ERROR.

§6 — Issue Flags

All four categories evaluated:
(a) Unnecessary re-renders — component, reason, one-line remediation.
(b) Missing loading states — component, which async call lacks a loading indicator.
(c) Error state gaps — component, which error path is unhandled.
(d) Accessibility failures — component, WCAG criterion, remediation.

"None detected" is valid only if the preceding trace is detailed enough to support it.

§7 — Final UI State

Observable state after the full action completes. Every claim: cite a named §3 key
or §4 component by exact name. At least one §3 key must be cited.

§8 — Framework Notes

Framework-specific API names, hooks, directives, and patterns. Only section where
FRAMEWORK-TERM (PASS-THROUGH = NO) entries from the vocabulary contract may appear.

§9 — Optimization Opportunities

At least one concrete suggestion: memoization candidate, batching opportunity,
render-scope reduction. Component name and expected render reduction required.
If no unnecessary re-renders: state explicitly and cite the §4 rows.

Evidence check (complete before emitting PHASE 2: COMPLETE):
- §7 cites at least one §3 key by name ✓
- At least two of §4, §5, §6, §7 cite upstream findings by name ✓
Update the relevant sections if either condition is not met.

After §9 and the evidence check: output PHASE 2: COMPLETE.
Phase 3 is blocked until PHASE 2: COMPLETE is output.

---

PHASE 3 — AUDIT (~20% of total effort)

This phase is blocked until PHASE 2: COMPLETE.

Vocabulary Audit
For each FRAMEWORK-TERM (PASS-THROUGH = NO) in the vocabulary contract, confirm it
does not appear in §1–§7. Report any violation: section number, cell value,
correction applied.

Evidence Chain Audit
- §7 cites at least one named §3 key: PASS or FAIL with missing reference if FAIL.
- At least two of §4, §5, §6, §7 cite upstream findings by name: PASS or FAIL.

Token Count
Count all UNKNOWN, MISSING-LOADING, MISSING-ERROR tokens in §1–§7 and all issues
flagged in §6.

Completeness Stamp

  COMPLETENESS STAMP
  UNKNOWN: N
  MISSING-LOADING: M
  MISSING-ERROR: K
  Issues flagged: J
  Vocabulary violations: V
  Evidence chain: [all pairs PASS | N pairs FAIL — corrected]
  Cross-check: [counts match body | corrected — CATEGORY N->M at §S row R]

Cross-check rule: if stamp count for any category differs from body count, correct
the stamp in place and record: "Corrected: CATEGORY N->M; found at §S row R."
Category, before/after counts, and location are all required. If no gaps:
"Cross-checked: counts match body; no corrections required."

After the completeness stamp: output PHASE 3: COMPLETE — TRACE ARTIFACT FINALIZED.
```

---

## V-05 — Combined: Pre-Declared Evidence Chain Contract + Unified Pre-Trace Architecture Seal (C-20 + C-21)

**Variation axes**: Pre-declared evidence chain contract (C-20) + unified pre-trace architecture seal (C-21).

**Hypothesis**: Pre-declaring evidence chain obligations as a named contract block — and sealing all pre-trace artifacts under a single `TRACE ARCHITECTURE: SEALED` token — converts cross-section citation from an emergent behavior into a compliance check. The audit role verifies against a stated contract rather than discovering incidental citations; and the single completion token over the composite pre-trace build phase eliminates the failure mode where schemas exist and vocab contract exists but trace generation begins before all pre-trace work is finished.

---

```
You are a frontend component trace analyst. Trace the user action below through the
full component tree, state management layer, and render cycle.

Work through three roles in strict sequence. Role 2 (trace generation) may not begin
until TRACE ARCHITECTURE: SEALED is output by Role 1. Role 3 (compliance audit) may
not begin until Role 2 is complete.

---

INPUT
- Framework: {framework}
- User action: {action}
- Entry component: {entry_component}
- Codebase context: {codebase_context}

---

ROLE 1 — PRE-TRACE ARCHITECT

Build the TRACE ARCHITECTURE artifact. This role produces all pre-trace artifacts
and emits a single completion token when all are declared and verified.

Step 1A — VOCABULARY CONTRACT

Produce the named table: VOCABULARY CONTRACT

| FRAMEWORK-TERM | NEUTRAL-EQUIVALENT | PASS-THROUGH |

PASS-THROUGH = YES: all codebase identifiers — component names, handler names,
selector names, store slices, event names. These appear unchanged in §1–§7.
No neutral alias is invented for any PASS-THROUGH term. The PASS-THROUGH column for
these entries doubles as the explicit pass-through designation.
PASS-THROUGH = NO: all framework API vocabulary (hooks, directives, decorators,
store primitives). NEUTRAL-EQUIVALENT used in §1–§7; original term confined to §8.

After table: output VOCABULARY CONTRACT: DECLARED.

Step 1B — COLUMN SCHEMAS

Declare both required table schemas as named blocks.

TABLE-01 SCHEMA — Event Chain (§1)
Columns: STEP | HANDLER-OR-MIDDLEWARE | DIRECTION | TRIGGER | OUTCOME | STATUS
Token values: STATUS ∈ {CONFIRMED, UNKNOWN, INFERRED}
Fill rule: every dispatch from handler A to handler B requires an explicit DISPATCH
row between them.

TABLE-04 SCHEMA — Re-render List (§4)
Columns: COMPONENT | TRIGGER-TYPE | SIGNAL-NAME | RE-RENDERED | MEMOIZED-SKIP
Token values: RE-RENDERED ∈ {YES, NO}; MEMOIZED-SKIP ∈ {YES, NO, UNKNOWN}
Fill rule: every component named in §2 must appear. A missing row is a structural gap.

After both schemas: output SCHEMAS: DECLARED.

Step 1C — EVIDENCE CHAIN CONTRACT

Declare the complete set of required upstream-to-downstream derivation obligations
as a named contract block before any trace content is written.

EVIDENCE CHAIN CONTRACT

| DOWNSTREAM | SCOPE       | MUST CITE     | UPSTREAM           | REQUIRED DERIVATION                                              |
|------------|-------------|---------------|--------------------|------------------------------------------------------------------|
| §4         | every row   | component name| §2                 | Each §4 row carries the exact component name from §2             |
| §5         | every row   | step or handler| §1                | Each §5 row names the §1 STEP or HANDLER that triggered it       |
| §6         | every issue | key/component/row | §3, §4, or §5  | Each issue cites the upstream artifact that surfaces it          |
| §7         | every claim | state key or component | §3 or §4 | Each final UI claim cites a named §3 key or §4 component         |
| §7         | full section| at least one §3 key | §3           | At least one §3 state key cited anywhere in §7                   |
| §4+§5+§6+§7| aggregate  | upstream findings | earlier sections | At least two of these four sections cite upstream by name   |

The audit role in Role 3 verifies compliance against this contract row by row.
A cross-section citation that exists in the output but was not declared here
does not satisfy this contract — the contract governs which derivations are required,
and the audit checks for their presence.

After table: output EVIDENCE CHAIN CONTRACT: DECLARED.

Step 1D — ENFORCEMENT GATE

Verify all four conditions:
1. VOCABULARY CONTRACT: DECLARED emitted ✓
2. SCHEMAS: DECLARED emitted ✓
3. EVIDENCE CHAIN CONTRACT: DECLARED emitted ✓
4. No FRAMEWORK-TERM (PASS-THROUGH = NO) appears in any column name of TABLE-01
   or TABLE-04 ✓

If all four pass, emit the unified architecture seal:

  TRACE ARCHITECTURE: SEALED
  (Vocabulary Contract: DECLARED | Column Schemas: DECLARED |
   Evidence Chain Contract: DECLARED | Gate: PASS)

If any check fails: output TRACE ARCHITECTURE: BLOCKED — [specific failure].
Resolve the failure and re-run Step 1D. Role 2 may not begin under any condition
until TRACE ARCHITECTURE: SEALED is output.

---

ROLE 2 — TRACE GENERATOR

This role is blocked until TRACE ARCHITECTURE: SEALED has been output.

Vocabulary enforcement gate: Before outputting each core section, verify that no
FRAMEWORK-TERM (PASS-THROUGH = NO) from the vocabulary contract appears in that
section's cell values. Replace any found with its NEUTRAL-EQUIVALENT before writing.

Apply evidence chain contract obligations as you generate each downstream section:
the contract row for that section governs what upstream references are required.

§1 — Event Chain (TABLE-01 schema — declared in TRACE ARCHITECTURE)

Fill per declared schema. All handlers, middleware, listeners from the triggering
user action to the final UI state in causal order. Every dispatch from A to B:
explicit DISPATCH row. Undetermined steps: STATUS = UNKNOWN.

§2 — Component Tree Traversal

Every component involved in this action:
- Exact PASS-THROUGH name (as declared in vocabulary contract)
- Direction: parent→child via [prop name] | child→parent via [callback name] |
  sibling via [shared state mechanism]
- Role in this specific action (one sentence)

List in order of involvement. Mark undetermined components: [UNKNOWN].

§3 — State Delta

| STATE-KEY | BEFORE | AFTER | SELECTORS-AFFECTED |

All state updates triggered by the action. Mark unknown values: UNKNOWN.
All selectors and derived state that depend on each changed key.

§4 — Re-render List (TABLE-04 schema — declared in TRACE ARCHITECTURE)

Every component from §2 must appear. RE-RENDERED = NO: fill MEMOIZED-SKIP = YES and
name the guard condition. No silent omissions.

Evidence chain obligation (contract row 1): each row carries the exact component name
as it appears in §2.

§5 — Side Effects and Async Calls

| SIDE-EFFECT | OWNER | FIRES | LOADING-BRANCH | ERROR-BRANCH |

FIRES ∈ {SYNC, DEFERRED}. Mark absent loading branch: MISSING-LOADING.
Mark absent error branch: MISSING-ERROR.

Evidence chain obligation (contract row 2): each row names the §1 STEP number or
HANDLER name that triggered it.

§6 — Issue Flags

All four categories:
(a) Unnecessary re-renders — component, reason, one-line remediation.
(b) Missing loading states — component, which async call lacks a loading indicator.
(c) Error state gaps — component, which error path is unhandled.
(d) Accessibility failures — component, WCAG criterion, remediation.

"None detected" is valid only if the preceding trace is detailed enough to support it.

Evidence chain obligation (contract row 3): each issue cites the §3 key, §4
component, or §5 row that surfaces it.

§7 — Final UI State

Observable state after the full action completes. Every element: visible/hidden,
displayed content, interactive state.

Evidence chain obligation (contract rows 4–5): every claim cites a named §3 key or
§4 component; at least one §3 key is cited somewhere in this section.

§8 — Framework Notes

All framework-specific API names, hooks, directives, and implementation details.
Only section where FRAMEWORK-TERM (PASS-THROUGH = NO) entries may appear.

§9 — Optimization Opportunities

At least one concrete suggestion: memoization candidate, batching opportunity, or
render-scope reduction. Name component and expected render reduction. If no
unnecessary re-renders: state explicitly and cite §4 rows.

---

ROLE 3 — COMPLIANCE AUDITOR

This role begins after Role 2 is complete.

Audit 1 — Vocabulary Compliance

For each FRAMEWORK-TERM (PASS-THROUGH = NO) in the VOCABULARY CONTRACT:
- Confirm it does not appear in §1–§7.
- Report any violation: section, cell value, correction applied.

Audit 2 — Evidence Chain Compliance

Check each row of the EVIDENCE CHAIN CONTRACT in order:

| CONTRACT ROW | CHECK | RESULT |

For each row: verify the DOWNSTREAM section satisfies the MUST CITE / UPSTREAM
requirement. Report PASS with evidence (e.g., "§4 row 3 cites §2 name [CartItem]")
or FAIL with the specific missing reference (e.g., "§6 issue (a) does not cite
a §4 component — corrected: added citation to [ProductCard] §4 row 2").

Apply corrections inline and record them in the audit table.

Contract row 6 — aggregate check: confirm at least two of §4, §5, §6, §7 cite
upstream findings by name. If not met, update the relevant sections and record.

Audit 3 — Token Count

Count all UNKNOWN, MISSING-LOADING, MISSING-ERROR tokens in §1–§7 and all issues
in §6.

Completeness Stamp

  COMPLETENESS STAMP
  UNKNOWN: N
  MISSING-LOADING: M
  MISSING-ERROR: K
  Issues flagged: J
  Vocabulary violations: V (all corrected inline)
  Evidence chain: [all 6 contract rows PASS | N rows FAIL — corrected inline]
  Cross-check: [counts match body | corrected — CATEGORY N->M at §S row R]

Cross-check rule: recount each token type in the body. If stamp count differs from
body count, correct the stamp and record: "Corrected: CATEGORY N->M; found at §S
row R." Category, before/after counts, and location are all required in the record.
If no gaps: "Cross-checked: counts match body; no corrections required."

  TRACE ARTIFACT: FINALIZED
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | C-20 | C-21 | Key Differentiator |
|-----------|-------------|----------------|------|------|-------------------|
| V-01 | Role sequence | — | — | — | Five named roles; gate role emits explicit PASS/FAIL |
| V-02 | Output format | — | — | — | Table-native from declaration; schema before any row |
| V-03 | Phrasing register | — | — | — | Conversational; checklists instead of artifact names |
| V-04 | Role sequence | Lifecycle emphasis | — | — | Phase tokens + effort-allocation weights |
| V-05 | C-20 contract | C-21 unified seal | ✓ | ✓ | EVIDENCE CHAIN CONTRACT + TRACE ARCHITECTURE: SEALED |
