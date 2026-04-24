Written to `simulations/quest/variations/trace-component-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — trace-component

**5 variations, targeting C-16 and C-17 (the two new v4 criteria):**

| V | Axis | Mechanism | Ceiling bet |
|---|------|-----------|-------------|
| **V-01** | Lifecycle emphasis | FINDINGS promoted to PHASE 6 with three sub-phases (Problem Survey / Fix Survey / Do-nothing cost Survey), each with its own gate | C-16: dedicated Problem Survey gate intercepts "may have performance issues," "could cause issues" as non-closers |
| **V-02** | Output format | Priority Score column (Impact × Urgency = 1–9); FINDINGS gate covers both Problem AND Do-nothing cost weak strings in a single gate block | C-16: dual-column gate without sub-section decomposition — tests whether one extended gate block can cover two column families |
| **V-03** | Phrasing register | Imperative throughout; Problem column weak strings named explicitly ("'May have performance issues' doesn't pass") but no structural gate syntax | C-16 baseline: imperative prohibition vs. structural gate — tests register enforcement alone |
| **V-04** | Combined: role sequence + triple lock on Do-nothing cost column | Staged roles (Frontend → Performance → A11y) + Do-nothing cost column gets all three lock mechanisms simultaneously: mandatory N/A-prohibited + header-cell instruction + FINDINGS gate | C-17: triple lock on Do-nothing cost as carrier column |
| **V-05** | Combined: R3 V-05 base + C-16 + C-17 | R3 V-05 baseline (104/104) + FINDINGS gate extended to Problem column (C-16) + Problem column gets triple lock: mandatory + header-cell instruction + gate naming weak strings (C-17) | Full ceiling test: 108 pts |

**Key structural bets:**

- **C-16 discrimination axis** is V-01 vs. V-02 vs. V-03: sub-section decomposition (V-01) vs. dual-coverage gate block (V-02) vs. imperative statement alone (V-03) for intercepting Problem column escape strings.
- **C-17** targets the Problem column in V-05 (all three mechanisms co-present: mandatory designation + `| Problem [N/A not allowed — ...] |` header syntax + gate naming "may have performance issues" as non-closers). V-04 targets the Do-nothing cost column.
- R3 V-05's FINDINGS gate intercepted only do-nothing cost strings — **"may have performance issues" could still clear FINDINGS unintercepted**. All five R4 variations attempt to close this gap, with different structural approaches.
ore reliable mechanisms.
- **C-17 (triple lock on a single column):** In R3, the three lock mechanisms were distributed across different columns and phases. C-17 requires all three co-present on the same column simultaneously — mandatory designation, escape instruction in the column header cell itself, and a gate that names weak strings specific to that column. V-04 targets the Do-nothing cost column; V-05 targets the Problem column.
- **Single-axis isolation:** V-01 tests lifecycle emphasis (sub-section decomposition) without adding the header-cell embedding of C-14 or the imperative register of V-02/V-03. V-02 tests output format (scoring scale + dual gate). V-03 tests phrasing register alone — no structural gates on the Problem column.

---

## V-01: Lifecycle Emphasis — FINDINGS Promoted to Phase 6 with Sub-Section Gates

**Axis:** Lifecycle emphasis — the FINDINGS section is promoted from a post-trace appendix to a first-class phase (PHASE 6) with three explicit sub-phases. Each sub-phase carries its own close gate. Problem Survey gates on Problem column weak strings. Do-nothing cost Survey gates on do-nothing cost weak strings. Fix Survey gates on generic fix language. The rest of the template is R3 V-05 baseline (sequential phases, exact-phrase gates, count×verdict column, comparison column with header-cell embedding, mandatory do-nothing cost).

**Hypothesis:** In R3, FINDINGS was a flat table appended after Phase 5. The FINDINGS gate (C-13) intercepted do-nothing cost strings but not Problem column strings. Promoting FINDINGS to PHASE 6 with internal sub-phases creates dedicated gate attachment points for each column type. A Problem Survey sub-phase gate can intercept "may have performance issues" at the Problem-entry moment rather than at section-close time. Predicted failure: sub-phase decomposition of FINDINGS increases structural complexity; the model may correctly execute Problem Survey while abbreviating Do-nothing cost Survey, or confuse sub-phase ordering with the trace phases above.

```
You are running /trace:component. Complete each phase in sequence.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.
PHASE 6 (FINDINGS) carries three sub-phase gates — one per survey column.

---

## PHASE 0: FRAMEWORK

Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Role: [Auto-selected frontend expert — match to framework]

Framework vocabulary declared (3–5 terms that must appear in phases below):
- [Term 1]: [one-clause definition]
- [Term 2]: [one-clause definition]
- [Term 3]: [one-clause definition]

Surface: [UI component or page — name it specifically]
User action: [Exact user action — name the element and event type]
Expected outcome: [What the user expects]

[PHASE 0 COMPLETE]

---

## PHASE 1: EVENT ANCHOR

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Exact UI component name — not "the button," not "the input field"]
Event payload: [Data carried in the event. If none: "No payload — void event."]
Handler: [The specific function name or lifecycle hook that receives this event.
  If no handler: "No handler on [ComponentName] — bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler does not close
this phase. Writing "an event fires" without the event type and firing component does not close
this phase. Handler must be a function name or lifecycle hook — not "the event handler."
Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch — name which]
[IntermediateComponent] (what it does with this event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

Branch if multiple subtrees affected:
Branch A: [ComponentA] → [ParentA] → [ContextConsumer A]
Branch B: [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a flat list without directional
relationships does not close this phase. Writing "traverses the component tree" without naming hops
does not close this phase. At least two named components with a directional arrow between them
are required. Mark: PHASE 2 COMPLETE.]

---

## PHASE 3: STATE MUTATION MAP

Mutation [N]:
  Owner: [Component or store — exact name from Phase 2]
  Key: [`stateKey` — specific field, not "the state"]
  Old: [Value or shape before]
  New: [Value or shape after]
  Mechanism: [useState setter / dispatch / store.$patch / this.setState]
  Timing: SYNC or ASYNC (after: [mechanism])

If no mutation: "No mutation — [read-only / presentational]. Justification: [why]."

[PHASE 3 GATE: Writing "State updates" does not close this phase.
Writing "state changes in response to the action" does not close this phase.
Writing "the store is modified" without naming the key or slice does not close this phase.
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY

Using mutations from Phase 3, fill this table for every component that re-renders.

| Component | Re-render cause | Count × verdict [both in this cell, same writing act — write "Nx — justified: [specific structural reason]" or "Nx per action — unnecessary: [exact cause]; fix: [specific hook or API]" or "0× — not in re-render path: [confirmed reason]"; count and verdict in separate columns or a subsection does not satisfy this column] | What this adds vs. ad-hoc [N/A not allowed — fill every cell: write "Invisible: [specific thing DevTools cannot show without Profiler or source-stepping — e.g., 'which context subscriber owns this re-render', 'whether selector returned a new reference']" OR "Observable: [specific tab]. Exception — [specific structural reason this row is fully transparent to ad-hoc DevTools — e.g., 'this is a controlled input; its re-render IS the DOM mutation, visible in Elements']. Exception requires justification."] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; re-render required to show the updated value] | [Invisible: whether this re-render is due to state ownership vs. prop propagation is not distinguishable without component-level DevTools] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of the specific field it renders; fix: React.memo + pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector contract — DevTools shows a re-render occurred, not whether it was required] |
[Minimum one row.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing "components re-render as expected" without naming them does not close this phase.
Writing count and verdict in separate columns or a subsection does not close this phase —
count × verdict must be in the same cell, same writing act.
Leaving a "What this adds vs. ad-hoc" cell blank or writing "N/A" does not close this phase.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay and callback / route / storage key]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation."

**Final UI state:**

Synchronous state (after all SYNC mutations and Phase 4 re-renders):
[Name visible elements, disabled states, loading indicators, error messages — specifically.]

Post-async state (if any side effect exists):
  Success: [What the user sees when the async effect resolves]
  Error: [What the user sees if it fails — or "No error state defined. See PHASE 6 FINDINGS."]
  If synchronous only: "No async settle point."

[PHASE 5 GATE: Writing "UI updates accordingly" does not close this phase.
Writing "the UI reflects the state changes" does not close this phase.
Writing "success and error states are handled" without describing what the user sees does not close
this phase. A concrete final state names specific visible elements, changed values, or confirmed
no-change. Mark: PHASE 5 COMPLETE.]

---

## PHASE 6: FINDINGS

PHASE 6 has three sub-phases executed in order. Each sub-phase has its own close gate.
Complete PROBLEM SURVEY before starting FIX SURVEY. Complete FIX SURVEY before COST SURVEY.

---

### PHASE 6A — PROBLEM SURVEY

Identify every problem across Phases 1–5:
- Phase 4 "Count × verdict" cells marked "unnecessary"
- Phase 4 "What this adds vs. ad-hoc" cells marked "Invisible" that surface a gap
- Phase 5 async effects without a loading state between trigger and settle
- Phase 5 error paths written "No error state defined"
- Phase 2 components missing ARIA, losing focus, or creating keyboard traps
- Phase 0 vocabulary terms that did not appear in any phase

For each problem, open a finding with:
  Finding-ID: [F-NN]
  Sev: P1 (blocks users) / P2 (degrades experience) / P3 (polish or a11y debt)
  Source: [Phase + component or state key — e.g., "Phase 4, ButtonGroup"]
  Problem: [Component + mechanism + cause — e.g., "ButtonGroup re-renders 3× per keystroke
    because it receives the full formState object rather than the isValid field it renders."]

[PHASE 6A GATE: Writing "may have performance issues" does not close PROBLEM SURVEY.
Writing "could cause issues" does not close PROBLEM SURVEY.
Writing "might affect users" does not close PROBLEM SURVEY.
Writing "has a potential re-render problem" without naming the component and cause does not close
PROBLEM SURVEY. Every finding's Problem field must name: the exact component, the exact cause,
and the mechanism.
If there are no problems: write a single finding F-00 with Sev: P0, Source: All phases, Problem:
"No issues found. Phase survey: [Phase 4 — all count×verdict cells are justified, cite each;
all 'What this adds vs. ad-hoc' cells are Observable exceptions, cite each. Phase 5 — no async
without loading state; no missing error paths. Phase 2 — no ARIA or focus gaps. Phase 0 — all
vocabulary terms appeared in trace, cited above in FRAMEWORK VOCABULARY CHECK.]"
Mark: PHASE 6A COMPLETE.]

---

### PHASE 6B — FIX SURVEY

For each finding from PHASE 6A, add a Fix field:
  Finding-ID: [F-NN — match to PHASE 6A]
  Fix: [One concrete, minimal fix — name the specific hook, attribute, boundary, or API.
    "Add error handling" does not pass — name the location and pattern.
    "Improve performance" does not pass — name the memoization boundary or selector change.
    "Fix accessibility" does not pass — name the ARIA attribute or focus management call.]

[PHASE 6B GATE: Writing "add error handling" without naming the location or pattern does not
close FIX SURVEY. Writing "improve performance" without naming a specific hook, boundary, or API
does not close FIX SURVEY. Writing "use memoization" without naming which component and which
memoization primitive does not close FIX SURVEY. Mark: PHASE 6B COMPLETE.]

---

### PHASE 6C — DO-NOTHING COST SURVEY

For each finding from PHASE 6A, add a Do-nothing cost:
  Finding-ID: [F-NN — match to PHASE 6A]
  Do-nothing cost: [Write one of:
    (a) "Ships: [specific user-visible consequence — name the affected user population and
        the exact failure mode, e.g., 'keyboard users cannot resume after this action without
        a mouse click', 'users see a blank panel on save failure with no recovery affordance',
        'screen readers announce stale element state after re-render']."
    (b) "Deferred: [specific future engineering cost — e.g., 'this re-render pattern requires
        touching 5 components once the form scales beyond 3 fields; cost grows with data size']."
    Exception — [specific structural reason this finding has zero production consequence, e.g.,
    'this component is behind a disabled feature flag; consequence is zero until the flag ships'].
    Exception requires a specific reason — not just asserting no consequence.]

[PHASE 6C GATE: Writing "no impact" does not close DO-NOTHING COST SURVEY.
Writing "minor issue" does not close DO-NOTHING COST SURVEY.
Writing "low risk" does not close DO-NOTHING COST SURVEY.
Writing "no user-facing consequence" without naming why does not close DO-NOTHING COST SURVEY.
A do-nothing cost must name the specific user population AND the exact failure mode,
OR the specific future engineering consequence with scope.
Mark: PHASE 6C COMPLETE. PHASE 6 COMPLETE.]

---

## FRAMEWORK VOCABULARY CHECK

Verify all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here and note which phase should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, unnecessary_rerenders, findings_count,
problem_survey_complete, fix_survey_complete, cost_survey_complete.
```

---

## V-02: Output Format — Priority Scoring Column + Dual-Column FINDINGS Gate

**Axis:** Output format — the FINDINGS table gains a Priority Score column (Impact × Urgency, each 1–3, product = 1–9; scores 7–9 = ship-blocker, 4–6 = address before launch, 1–3 = backlog). The FINDINGS gate covers both the Problem column and the Do-nothing cost column simultaneously, naming weak strings from both in a single gate block. No sub-phase decomposition. The rest of the template is R3 V-05 baseline with the comparison column intact.

**Hypothesis:** The scoring column adds a quantitative framing that forces the model to evaluate severity and urgency as separate dimensions before assigning a priority, which in turn raises the bar for Problem specificity (you cannot accurately score 7/9 for a vague problem description). The dual-column gate covering both "may have performance issues" (Problem) and "no impact" (Do-nothing cost) in a single gate block tests whether gate coverage of two column families is achievable without structural sub-section decomposition. Predicted failure: a single gate block covering two column families is longer than a per-column gate; the model may misread it and intercept only the first family listed.

```
You are running /trace:component. Complete each phase in sequence.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.
The FINDINGS gate covers both Problem and Do-nothing cost weak strings.

---

## PHASE 0: FRAMEWORK

Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Role: [Auto-selected frontend expert — match to framework]

Framework vocabulary declared (3–5 terms that must appear in phases below):
- [Term 1]: [one-clause definition]
- [Term 2]: [one-clause definition]
- [Term 3]: [one-clause definition]

Surface: [UI component or page — name it specifically]
User action: [Exact user action — name the element and event type]
Expected outcome: [What the user expects]

[PHASE 0 COMPLETE]

---

## PHASE 1: EVENT ANCHOR

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Exact UI component name — not "the button," not "the input field"]
Event payload: [Data carried in the event. If none: "No payload — void event."]
Handler: [The specific function name or lifecycle hook that receives this event.
  If no handler: "No handler on [ComponentName] — bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler does not close
this phase. Writing "an event fires" without the event type and firing component does not close
this phase. Handler must be a function name or lifecycle hook — not "the event handler."
Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch — name which]
[IntermediateComponent] (what it does with this event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

Branch if multiple subtrees affected:
Branch A: [ComponentA] → [ParentA] → [ContextConsumer A]
Branch B: [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a flat list without directional
relationships does not close this phase. Writing "traverses the component tree" without naming hops
does not close this phase. At least two named components with a directional arrow between them
are required. Mark: PHASE 2 COMPLETE.]

---

## PHASE 3: STATE MUTATION MAP

Mutation [N]:
  Owner: [Component or store — exact name from Phase 2]
  Key: [`stateKey` — specific field, not "the state"]
  Old: [Value or shape before]
  New: [Value or shape after]
  Mechanism: [useState setter / dispatch / store.$patch / this.setState]
  Timing: SYNC or ASYNC (after: [mechanism])

If no mutation: "No mutation — [read-only / presentational]. Justification: [why]."

[PHASE 3 GATE: Writing "State updates" does not close this phase.
Writing "state changes in response to the action" does not close this phase.
Writing "the store is modified" without naming the key or slice does not close this phase.
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY

Using mutations from Phase 3, fill this table for every component that re-renders.

| Component | Re-render cause | Count × verdict [both in this cell, same writing act — "Nx — justified: [structural reason]" or "Nx per action — unnecessary: [cause]; fix: [specific hook or API]" or "0× — not in re-render path: [confirmed reason]"; count and verdict in separate columns or a subsection does not satisfy this column] | What this adds vs. ad-hoc [N/A not allowed — fill every cell: "Invisible: [specific thing DevTools cannot show without Profiler or source-stepping]" OR "Observable: [specific tab]. Exception — [specific structural reason — e.g., 'this is a controlled input; its re-render IS the DOM mutation']. Exception requires justification."] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; re-render required to show the updated value] | [Invisible: whether this re-render is due to state ownership vs. prop propagation is indistinguishable without component-level DevTools] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of the specific field it renders; fix: React.memo + pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector contract] |
[Minimum one row.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing count and verdict in separate columns or a subsection does not close this phase.
Leaving a "What this adds vs. ad-hoc" cell blank or writing "N/A" does not close this phase.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay and callback / route / storage key]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation."

**Final UI state:**

Synchronous state (after all SYNC mutations and Phase 4 re-renders):
[Name visible elements, disabled states, loading indicators, error messages — specifically.]

Post-async state (if any side effect exists):
  Success: [What the user sees when the async effect resolves]
  Error: [What the user sees if it fails — or "No error state defined. See FINDINGS."]
  If synchronous only: "No async settle point."

[PHASE 5 GATE: Writing "UI updates accordingly" does not close this phase.
Writing "the UI reflects the state changes" does not close this phase.
Writing "success and error states are handled" without describing what the user sees does not close
this phase. Mark: PHASE 5 COMPLETE.]

---

## FINDINGS

Consolidate from:
- Phase 4 "Count × verdict" cells marked "unnecessary"
- Phase 5 async effects without a loading state between trigger and settle
- Phase 5 error paths written "No error state defined"
- Phase 2 components missing ARIA, losing focus, or creating keyboard traps
- Phase 4 "What this adds vs. ad-hoc" cells marked "Invisible" that surface a structural problem

Priority Score = Impact (1–3) × Urgency (1–3) → 7–9 ship-blocker, 4–6 address before launch, 1–3 backlog.
- Impact 3: blocks users or corrupts data. Impact 2: degrades experience, workaround exists. Impact 1: polish, cosmetic, or a11y debt without user flow impact.
- Urgency 3: will regress or spread if not fixed before next merge. Urgency 2: bounded scope now, expands with growth. Urgency 1: stable issue, can defer.

| Score | Sev | Source | Problem | Fix | Do-nothing cost [N/A not allowed — fill every row: "Ships: [specific user-visible consequence — name the affected user population and the exact failure mode]" OR "Deferred: [specific future engineering cost with scope]. Exception — [specific structural reason this finding has zero production consequence]. Exception requires a specific reason."] |
|-------|-----|--------|---------|-----|-----------------|
| [I×U] | [P1/P2/P3] | [Phase + component] | [specific — component + mechanism + cause] | [concrete — hook, boundary, or ARIA attribute] | [Ships: specific consequence / Deferred: specific cost. Exception — specific reason.] |
[Minimum one row per finding.]

[FINDINGS GATE:
Problem column — writing "may have performance issues" without naming the component and cause does
not close this section. Writing "could cause issues" without naming the component and mechanism
does not close this section. Writing "might affect users" without naming the specific failure mode
does not close this section. Writing "potential re-render problem" without naming the component
does not close this section.
Do-nothing cost column — writing "no impact" as a do-nothing cost does not close this section.
Writing "minor issue" does not close this section. Writing "low risk" does not close this section.
Writing "no user-facing consequence" without naming why does not close this section.
If there are no findings, write one row with Score: 0, Sev: P0, Source: All phases, Problem:
[per-phase summary — Phase 4: cite each count×verdict cell and each 'What this adds vs. ad-hoc'
cell; confirm each was justified or an Observable exception. Phase 5: no missing loading states,
no missing error paths. Phase 2: no ARIA or focus gaps.], Fix: N/A, Do-nothing cost: No production
risk — [per-phase evidence; do not write 'implementation looks correct' without citing each check].
Mark: FINDINGS COMPLETE.]

---

## FRAMEWORK VOCABULARY CHECK

Verify all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here using it correctly.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, unnecessary_rerenders, findings_count,
max_priority_score, ship_blockers_count.
```

---

## V-03: Phrasing Register — Imperative Throughout, Problem Column Weak Strings Named

**Axis:** Phrasing register — all constraint instructions are written in second-person imperative throughout. The FINDINGS section Problem column instruction explicitly names weak strings as non-passing in imperative form ("'May have performance issues' doesn't pass. 'Could cause issues' doesn't pass. Name the component, the cause, and the mechanism.") but uses no structural gate syntax for the Problem column. The FINDINGS gate covers only do-nothing cost strings (same as R3 V-05). This is a register test for C-16: imperative prohibition of Problem column weak strings vs. structural gate interception.

**Hypothesis:** R3 V-02 tested imperative register for phase instructions. This variation extends the same register to Problem column enforcement in FINDINGS — explicit "doesn't pass" statements for weak Problem column strings, without the gate block formalism. If the model follows explicit rule statements as reliably as structural gate interception, this should approach C-16. If the gate's exact-phrase interception is materially stronger than the imperative rule statement, this will score partial on C-16. This is the control for V-01 and V-02 — the question is whether register alone is sufficient enforcement for Problem column strings, or whether structural gating is required.

```
You are running /trace:component. Work through each step in order.
Mark each step DONE before moving to the next. Do not skip ahead.

---

## STEP 0 — DECLARE YOUR CONTEXT

Name the framework. Name the state management layer. Name your role.

- Framework: React / Vue / Angular / Svelte / other. Include the version if you can infer it.
- State management: useState / Redux / Zustand / Pinia / NgRx / other.
- Rendering model: Virtual DOM / Signals-based / Zone.js / Svelte compiler / other.
- Role: pick the right expert for this framework. Name who you are for this trace.

Declare 3–5 framework-specific terms you'll use. Define each in one clause.
These terms must appear in your trace below — if you don't use a term, the trace is incomplete.
  - [Term 1]: [definition]
  - [Term 2]: [definition]
  - [Term 3]: [definition]

Name the surface and the action:
- Surface: which page or component?
- User action: which element, which event type, what does the user do?
- Expected outcome: what does the user expect to happen?

[STEP 0 DONE]

---

## STEP 1 — ANCHOR THE EVENT

Name all four. All four are required.

1. Event type: write the actual event name — onClick, onChange, onSubmit, onDragEnd, or the custom
   event string. "An event fires" doesn't pass. "A click happens" doesn't pass.

2. The component that fired it: write its actual name. Not "the button." Not "the input field."
   Not "the form element." The component name. If it's unnamed, give it a name from context.

3. Payload: what data rides in the event? If none, say "No payload — void event."

4. Handler: write the function name or lifecycle hook that catches this event.
   "The event handler" doesn't pass. "The handler function" doesn't pass.
   If nothing catches it here, say "No handler on [ComponentName] — bubbles to [ParentComponent]."

[STEP 1 DONE]

---

## STEP 2 — TRACE THE COMPONENT PATH

Draw the chain from the event-receiving component to the root of the affected subtree.
Name every hop. Show the direction and the relationship at each hop.

[EventReceivingComponent] (the component from STEP 1)
  ↓ [prop callback / context subscription / store dispatch — which?]
[IntermediateComponent] (what it does with this)
  ↓ [relationship]
[ProviderOrRoot] (top of the affected subtree)

If two subtrees are affected, trace both — Branch A and Branch B.

Don't write a flat list like "[A, B, C]" without directions — that doesn't pass.
Don't write "traverses the tree upward" without naming the hops — that doesn't pass.
Two named components with an arrow between them is the minimum.

[STEP 2 DONE]

---

## STEP 3 — MAP EVERY STATE MUTATION

For each piece of state that changes:
- Owner: which component or store? Match the name to STEP 2's tree.
- Key: the exact state key or store slice. Not "the state" — the field name. Use backticks.
- Old: what did it look like before? Give the value or shape.
- New: what does it look like after? Give the value or shape.
- Mechanism: useState setter / dispatch / store.$patch / this.setState.
- Timing: SYNC (same tick) or ASYNC (after: name the mechanism).

If nothing mutates: say "No mutation — [read-only / presentational]. Here's why: [specific reason]."

"State updates" doesn't pass.
"State changes in response to the action" doesn't pass.
"The store is modified" without naming the slice doesn't pass.

[STEP 3 DONE]

---

## STEP 4 — INVENTORY THE RE-RENDERS

For every component that re-renders, fill one row.

| Component | Re-render cause | Count × verdict [both in this cell — "Nx — justified: [structural reason]" or "Nx per action — unnecessary: [cause]; fix: [hook or API]" or "0× — not in re-render path: [confirmed reason]"; count and verdict in separate places doesn't pass] | What this adds vs. ad-hoc [N/A not allowed — "Invisible: [what DevTools can't show]" OR "Observable: [specific tab]. Exception — [specific structural reason]". Exception requires justification.] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; must re-render to show the updated value] | [Invisible: whether this re-render is due to state ownership vs. prop propagation] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState; fix: React.memo + pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector contract] |
[Minimum one row.]

"Several components re-render" without naming them doesn't pass.
"Components re-render as expected" without naming them doesn't pass.
Count and verdict in separate places doesn't pass — same cell, same writing act.

[STEP 4 DONE]

---

## STEP 5 — SIDE EFFECTS AND FINAL STATE

**Side effects.** For each effect triggered by this action:
  Type: API call / timer / navigation / storage write / subscription
  Detail: method + endpoint / timer delay + callback / route / key + value shape.
  Mechanism: useEffect dependency / thunk / saga / Pinia action / router hook.

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation."
Silence doesn't pass.

**What the user sees.** After all SYNC mutations and re-renders:
- Name the visible elements. Name disabled states. Name loading indicators and error messages.
- Be specific: which element, what state, who sees it.

If async effects exist:
  Success: what does the user see when it resolves?
  Error: what does the user see if it fails? Or "No error state defined — see FINDINGS."
  If synchronous only: "No async settle point."

"UI updates accordingly" doesn't pass.
"The UI reflects the state changes" doesn't pass.
"Success and error states handled" without describing what the user sees doesn't pass.

[STEP 5 DONE]

---

## FINDINGS

Pull together everything from STEPS 1–5. For each issue:

Severity: P1 (blocks users) / P2 (degrades experience) / P3 (polish or a11y debt)
Source: which STEP, which component or state key.

Problem: name the component, the cause, and the mechanism.
  "May have performance issues" doesn't pass — name the component and the specific cause.
  "Could cause issues for users" doesn't pass — name the specific user population and failure mode.
  "Might affect performance" doesn't pass — name the component, re-render count, and root cause.
  "Has a potential re-render problem" doesn't pass — name the component and why.
  "Performance could be improved" doesn't pass — name what is re-rendering unnecessarily and why.

Fix: one concrete fix — name the hook, boundary, or ARIA attribute.
  "Add error handling" doesn't pass — name the location and pattern.
  "Improve performance" doesn't pass — name the memoization boundary or selector.

Do-nothing cost: what ships if this is not addressed?
  Name the affected user population and the exact failure mode,
  or the specific future engineering cost with scope.

If no findings: "No issues across all five steps. Here's why each check came back clean:
[STEP 4 — name each count×verdict cell and each 'What this adds vs. ad-hoc' cell; confirm
justified/Observable with evidence. STEP 5 — no async without loading states; no missing error
paths. STEP 2 — no ARIA or focus gaps.]"

---

## FRAMEWORK VOCABULARY CHECK

Did every declared term appear in your trace?
- [Term 1]: STEP [N], [section] — "[exact phrase used]"
- [Term 2]: STEP [N], [section] — "[exact phrase used]"
- [Term 3]: STEP [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here and note which step should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
steps_completed, mutations_count, rerender_count, unnecessary_rerenders, findings_count.
```

---

## V-04: Combined — Staged Roles + Triple Structural Lock on Do-Nothing Cost Column (C-17)

**Axis (combined):** Role sequence (staged specialist roles, R3 V-01 pattern) + triple structural lock on the Do-nothing cost column. The Do-nothing cost column carries all three independent enforcement mechanisms simultaneously: (1) mandatory N/A-prohibited designation in the column setup block, (2) escape instruction embedded in the literal Markdown column header cell — `| Do-nothing cost [N/A not allowed — fill every row...] |` — making it part of the header row syntax the model writes, (3) a FINDINGS gate that names weak do-nothing cost strings ("no impact," "minor issue," "low risk") specifically for the Do-nothing cost column. Tests C-17 with the Do-nothing cost column as the carrier column.

**Hypothesis:** In R3 V-05, the Do-nothing cost column had the column-header instruction (C-14) and the FINDINGS gate (C-13), but these were tested as separate criteria. C-17 requires all three mechanisms present on the same column simultaneously — the mandatory designation, the header-cell instruction, and the per-column gate. Staged roles provide analytical depth for FINDINGS without being the structural discriminator. The triple-lock question is whether the three mechanisms are genuinely independent: mandatory designation prevents omission, header-cell instruction provides the constraint at write-time, and the named gate intercepts the specific strings a model produces when clearing the first two. If any one mechanism fails to fire, one of the other two should catch it. Predicted failure: the staged role handoff to Accessibility and UX Specialist at FINDINGS introduces a framing shift that causes the model to reweight toward a11y findings and underweight performance re-render findings from Phase 4.

```
You are running /trace:component. Three specialist roles share this trace.
Each role activates at the phase window declared in PHASE 0.
Complete phases in sequence. Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.
The FINDINGS section carries its own gate covering do-nothing cost failure strings.

---

## PHASE 0: FRAMEWORK + ROLE ASSIGNMENT

Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Rendering model: [Virtual DOM + reconciler / Signals-based / Zone.js / Svelte compiler / other]

Framework vocabulary declared (3–5 terms that must appear in phases below):
- [Term 1]: [one-clause definition]
- [Term 2]: [one-clause definition]
- [Term 3]: [one-clause definition]

Surface: [UI component or page — name it specifically]
User action: [Exact user action — name the element and event type]
Expected outcome: [What the user expects]

ROLE ASSIGNMENT:
- Phases 1–2 → Frontend Engineer: [framework] component architecture and event propagation expert
- Phases 3–4 → Performance Engineer: [framework] rendering model and state optimization expert
- Phase 5 + FINDINGS → Accessibility and UX Specialist: ARIA, focus management, production risk

[PHASE 0 GATE: Framework, vocabulary, surface, action, expected outcome, and all three roles
declared. Mark: PHASE 0 COMPLETE.]

---

## PHASE 1: EVENT ANCHOR
[Role: Frontend Engineer]

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Exact UI component name — not "the button," not "the input field"]
Event payload: [Data carried in the event. If none: "No payload — void event."]
Handler: [The specific function name or lifecycle hook that receives this event.
  If no handler: "No handler on [ComponentName] — bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler does not close
this phase. Writing "an event fires" without the event type and firing component does not close
this phase. Handler must be a function name or lifecycle hook — not "the event handler."
Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH
[Role: Frontend Engineer]

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch — name which]
[IntermediateComponent] (what it does with this event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

Branch if multiple subtrees affected:
Branch A: [ComponentA] → [ParentA] → [ContextConsumer A]
Branch B: [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a flat list without directional
relationships does not close this phase. Writing "traverses the component tree" without naming hops
does not close this phase. At least two named components with a directional arrow required.
Mark: PHASE 2 COMPLETE.]

---

## PHASE 3: STATE MUTATION MAP
[Role: Performance Engineer — handoff from Frontend Engineer]

Mutation [N]:
  Owner: [Component or store — exact name from Phase 2]
  Key: [`stateKey` — specific field, not "the state"]
  Old: [Value or shape before]
  New: [Value or shape after]
  Mechanism: [useState setter / dispatch / store.$patch / this.setState]
  Timing: SYNC or ASYNC (after: [mechanism])

If no mutation: "No mutation — [read-only / presentational]. Justification: [why]."

[PHASE 3 GATE: Writing "State updates" does not close this phase.
Writing "state changes in response to the action" does not close this phase.
Writing "the store is modified" without naming the key or slice does not close this phase.
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY
[Role: Performance Engineer]

Using mutations from Phase 3, fill this table for every component that re-renders.

| Component | Re-render cause | Count × verdict [both in this cell, same writing act — "Nx — justified: [specific structural reason]" or "Nx per action — unnecessary: [exact cause]; fix: [specific hook, API, or boundary]" or "0× — not in re-render path: [confirmed reason]"; count and verdict in separate columns or a subsection does not satisfy this column] | What this adds vs. ad-hoc [N/A not allowed — fill every cell: "Invisible: [specific thing DevTools cannot show without Profiler or source-stepping — e.g., 'which context subscriber owns this re-render', 'whether selector returned a new reference']" OR "Observable: [specific tab — Network/Console/Elements/Profiler]. Exception — [specific structural reason this row is fully transparent to ad-hoc DevTools — e.g., 'this is a controlled input; its re-render IS the DOM mutation, visible in Elements']. Exception requires justification — not just claiming it."] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; re-render required to show the updated value] | [Invisible: whether this re-render is due to state ownership vs. prop propagation is not distinguishable without component-level DevTools] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of specific field it renders; fix: React.memo + pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector contract — DevTools shows a re-render occurred, not whether it was required] |
[Minimum one row. Add rows for every re-rendering component.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing "components re-render as expected" without naming them does not close this phase.
Writing count and verdict in separate columns or a subsection does not close this phase —
count × verdict must be in the same cell, same writing act.
Leaving a "What this adds vs. ad-hoc" cell blank or writing "N/A" does not close this phase.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE
[Role: Accessibility and UX Specialist — handoff from Performance Engineer]

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay and callback / route / storage key]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation."

**Final UI state:**

Synchronous state (after all SYNC mutations and Phase 4 re-renders):
[Name visible elements, disabled states, loading indicators, error messages — specifically.]

Post-async state (if any side effect exists):
  Success: [What the user sees when the async effect resolves]
  Error: [What the user sees if it fails — or "No error state defined. See FINDINGS."]
  If synchronous only: "No async settle point."

[PHASE 5 GATE: Writing "UI updates accordingly" does not close this phase.
Writing "the UI reflects the state changes" does not close this phase.
Writing "success and error states are handled" without describing what the user sees does not close
this phase. A concrete final state names specific visible elements, changed values, or confirmed
no-change. Mark: PHASE 5 COMPLETE.]

---

## FINDINGS
[Role: Accessibility and UX Specialist]

Consolidate from:
- Phase 4 "Count × verdict" cells marked "unnecessary"
- Phase 4 "What this adds vs. ad-hoc" cells marked "Invisible" that surface a structural gap
- Phase 5 async effects without a loading state between trigger and settle
- Phase 5 error paths written "No error state defined"
- Phase 2 components missing ARIA, losing focus, or creating keyboard traps
- Phase 0 vocabulary terms that did not appear in any phase

MANDATORY — Do-nothing cost column:
Every row must have a Do-nothing cost entry. N/A is not allowed in any row.
Write one of: "Ships: [specific consequence]" or "Deferred: [specific cost]" or an Exception.
Exception requires a specific structural reason — not just asserting no consequence.

| Sev | Source | Problem | Fix | Do-nothing cost [N/A not allowed — fill every row: write "Ships: [specific user-visible consequence — name the affected user population and the exact failure mode, e.g., 'keyboard users cannot resume after this action without a mouse click', 'users see a blank panel on network failure with no recovery affordance', 'screen readers announce stale state after re-render']" OR "Deferred: [specific future engineering cost — e.g., 'this re-render pattern requires touching N components once the form scales beyond M fields; cost grows with data size']. Exception — [specific structural reason this finding has zero production consequence — e.g., 'this component is behind a disabled feature flag; consequence is zero until the flag ships to production']. Exception requires a specific reason — not just asserting no consequence."] |
|-----|--------|---------|-----|-----------------|
| [P1/P2/P3] | [Phase + component] | [specific — component + mechanism + cause, not "may have issues"] | [concrete — hook, boundary, or ARIA attribute] | [Ships: specific consequence / Deferred: specific cost. Exception — specific structural reason.] |
[Add one row per finding.]

[FINDINGS GATE: Writing "no impact" in the Do-nothing cost column does not close this section.
Writing "minor issue" in the Do-nothing cost column does not close this section.
Writing "low risk" in the Do-nothing cost column does not close this section.
Writing "no user-facing consequence" without naming why does not close this section.
Writing "no production risk" without citing per-phase evidence does not close this section.
A Do-nothing cost must name: the specific user population AND the exact failure mode
OR the specific future engineering cost AND the triggering scope condition.
If there are no findings, write one row:
  Sev: P0 | Source: All phases | Problem: [per-role summary — Frontend Engineer: Phase 1–2 checks;
  Performance Engineer: Phase 3–4 checks, cite each count×verdict cell and each 'What this adds
  vs. ad-hoc' cell; Accessibility Specialist: Phase 5 checks.] | Fix: N/A |
  Do-nothing cost: No production risk — [confirm per phase why each check came back clean;
  cite specific checks — do not write 'implementation looks correct'].
Mark: FINDINGS COMPLETE.]

---

## FRAMEWORK VOCABULARY CHECK

Verify all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here and note which phase should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
roles_used, phases_completed, mutations_count, rerender_count, unnecessary_rerenders,
findings_count, do_nothing_costs_present.
```

---

## V-05: Combined — R3 V-05 Base + C-16 (Problem Column Gate) + C-17 (Triple Lock on Problem Column)

**Axis (combined):** All five v3 criteria carried forward from R3 V-05 (proven ceiling at 104/104) + C-16: FINDINGS gate extended to cover Problem column weak strings in addition to do-nothing cost strings + C-17: Problem column gets all three triple structural lock mechanisms simultaneously — (1) mandatory N/A-prohibited designation, (2) escape instruction embedded in the literal Markdown column header cell syntax (`| Problem [N/A not allowed — ...] |`), (3) FINDINGS gate names Problem column weak strings as non-closers.

**Hypothesis:** R3 V-05 passed all 15 v3 criteria. The two new R4 criteria target gaps that remained: C-16 targets the Problem column (FINDINGS gate covered do-nothing cost strings but not Problem strings — "may have performance issues" can still clear FINDINGS in R3 V-05); C-17 requires the triple lock on a single column. The Problem column is the natural carrier for C-17 because it is the gate family's highest-traffic interception point — it is the column a model is most likely to fill with weak escape strings on first pass. Stacking all three mechanisms on the Problem column (mandatory + header instruction + gate) means: the mandatory designation prevents omission; the header-cell instruction provides the constraint at the moment of writing the header row; the gate names the specific strings ("may have performance issues," "could cause issues") that a model produces when clearing the first two. Predicted failure: the Problem column header becomes long enough to degrade table readability — the model may truncate it in practice, which would fail C-17's header-embedded instruction requirement.

```
You are running /trace:component. Complete each phase in sequence.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.
The FINDINGS section carries a gate that covers both the Problem column and the Do-nothing cost
column — both gate families are enforced at FINDINGS COMPLETE.

---

## PHASE 0: FRAMEWORK

Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Role: [Auto-selected frontend expert — match to framework]

Framework vocabulary declared (3–5 terms that must appear in phases below):
- [Term 1]: [one-clause definition]
- [Term 2]: [one-clause definition]
- [Term 3]: [one-clause definition]

Surface: [UI component or page — name it specifically]
User action: [Exact user action — name the element and event type]
Expected outcome: [What the user expects]

[PHASE 0 COMPLETE]

---

## PHASE 1: EVENT ANCHOR

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Exact UI component name — not "the button," not "the input field"]
Event payload: [Data carried in the event. If none: "No payload — void event."]
Handler: [The specific function name or lifecycle hook that receives this event.
  If no handler: "No handler on [ComponentName] — bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler does not close
this phase. Writing "an event fires" without the event type and firing component does not close
this phase. Handler must be a function name or lifecycle hook — not "the event handler."
Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch — name which]
[IntermediateComponent] (what it does with this event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

Branch if multiple subtrees affected:
Branch A: [ComponentA] → [ParentA] → [ContextConsumer A]
Branch B: [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a flat list without directional
relationships does not close this phase. Writing "traverses the component tree" without naming hops
does not close this phase. At least two named components with a directional arrow between them
are required. Mark: PHASE 2 COMPLETE.]

---

## PHASE 3: STATE MUTATION MAP

Mutation [N]:
  Owner: [Component or store — exact name from Phase 2]
  Key: [`stateKey` — specific field, not "the state"]
  Old: [Value or shape before]
  New: [Value or shape after]
  Mechanism: [useState setter / dispatch / store.$patch / this.setState]
  Timing: SYNC or ASYNC (after: [mechanism])

If no mutation: "No mutation — [read-only / presentational]. Justification: [why]."

[PHASE 3 GATE: Writing "State updates" does not close this phase.
Writing "state changes in response to the action" does not close this phase.
Writing "the store is modified" without naming the key or slice does not close this phase.
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY

Using mutations from Phase 3, fill this table for every component that re-renders.

| Component | Re-render cause | Count × verdict [both pieces in this cell, same writing act — co-location required; write "Nx — justified: [specific structural reason]" or "Nx per action — unnecessary: [exact cause]; fix: [specific hook or API]" or "0× — not in re-render path: [confirmed reason]"; count and verdict in separate columns or a separate section does not satisfy this column] | What this adds vs. ad-hoc [N/A not allowed — fill every cell; write "Invisible: [specific thing DevTools cannot show without Profiler or source-stepping — e.g., 'which context subscriber owns this re-render', 'whether the selector returned a new reference vs. the same reference']" OR "Observable: [specific tab — Network/Console/Elements/Profiler]. Exception — [specific structural reason this row is fully transparent to ad-hoc DevTools without component-level tooling — e.g., 'this is a controlled input; its re-render IS the DOM mutation, directly visible in Elements tab without component tooling']. Exception requires explanation — not just claiming it."] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; this re-render is required to show the updated value] | [Invisible: whether this re-render is due to state ownership vs. prop propagation is not distinguishable in the DOM without component-level DevTools] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of the specific field it renders; fix: React.memo + pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector contract — DevTools shows a re-render occurred but cannot determine whether it was required] |
[Minimum one row. Add rows for every re-rendering component.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing "components re-render as expected" without naming them does not close this phase.
Writing count in one column and verdict in a separate subsection does not close this phase —
count × verdict must be in the same cell, in the same writing act.
Leaving a "What this adds vs. ad-hoc" cell blank or writing "N/A" does not close this phase.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay and callback / route / storage key]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation."

**Final UI state:**

Synchronous state (after all SYNC mutations and Phase 4 re-renders):
[Name visible elements, disabled states, loading indicators, error messages — specifically.]

Post-async state (if any side effect exists):
  Success: [What the user sees when the async effect resolves]
  Error: [What the user sees if it fails — or "No error state defined. See FINDINGS."]
  If synchronous only: "No async settle point."

[PHASE 5 GATE: Writing "UI updates accordingly" does not close this phase.
Writing "the UI reflects the state changes" does not close this phase.
Writing "success and error states are handled" without describing what the user sees does not close
this phase. A concrete description names specific visible elements, changed values, or confirmed
no-change. Mark: PHASE 5 COMPLETE.]

---

## FINDINGS

Consolidate from:
- Phase 4 "Count × verdict" cells marked "unnecessary"
- Phase 4 "What this adds vs. ad-hoc" cells marked "Invisible" that surface a structural problem
- Phase 5 side effects without a loading state between trigger and settle
- Phase 5 error paths written "No error state defined"
- Phase 2 components missing ARIA, losing focus, or creating keyboard traps
- Phase 0 vocabulary terms that did not appear in any phase

MANDATORY — Problem column: every row must name the component, the cause, and the mechanism.
N/A is not allowed. Generic descriptions do not satisfy this column.

MANDATORY — Do-nothing cost column: every row must name a specific consequence or cost.
N/A is not allowed. Generic risk statements do not satisfy this column.

| Sev | Source | Problem [N/A not allowed — fill every row; name the exact component, the exact cause, and the mechanism — e.g., "ButtonGroup re-renders 3× per keystroke because it receives the full formState object rather than the isValid field it renders" or "SaveButton has no aria-busy state during the POST request; screen readers receive no in-progress feedback" or "useEffect subscribes without a cleanup return; subscription accumulates across re-mounts"; a blank cell, "N/A", or a generic description fails this column] | Fix | Do-nothing cost [N/A not allowed — fill every row; write "Ships: [specific user-visible consequence — name the affected user population and the exact failure mode, e.g., 'keyboard users cannot resume after this action without a mouse click', 'users see a blank panel on save failure with no recovery affordance', 'screen readers announce stale element state after re-render']" OR "Deferred: [specific future engineering cost — e.g., 'this re-render pattern requires touching N components once the form scales beyond M fields; cost grows with data size']. Exception — [specific structural reason this finding has zero production consequence — e.g., 'this component is behind a disabled feature flag; consequence is zero until the flag ships to production']. Exception requires a specific reason — not just asserting no consequence."] |
|-----|--------|---------|-----|-----------------|
| [P1/P2/P3] | [Phase + component] | [exact component + cause + mechanism] | [concrete — hook, boundary, or ARIA attribute] | [Ships: specific consequence / Deferred: specific cost. Exception — specific structural reason.] |
[Add one row per finding.]

[FINDINGS GATE:
Problem column — writing "may have performance issues" does not close this section.
Writing "could cause issues" does not close this section.
Writing "might affect users" does not close this section.
Writing "has a potential re-render problem" without naming the component and cause does not close
this section. Writing "performance could be improved" without naming what is re-rendering and why
does not close this section. A Problem cell must name: the exact component AND the exact cause
AND the mechanism — all three.
Do-nothing cost column — writing "no impact" does not close this section.
Writing "minor issue" does not close this section.
Writing "low risk" does not close this section.
Writing "no user-facing consequence" without naming why does not close this section.
A Do-nothing cost cell must name: the specific user population AND the exact failure mode,
OR the specific future engineering cost AND the triggering scope condition.
If there are no findings, write one row:
  Sev: P0 | Source: All phases |
  Problem: No issues found. Phase survey: [Phase 4 — cite each count×verdict cell (all justified,
  name structural reason for each) and each 'What this adds vs. ad-hoc' cell (all Observable
  exceptions, name the DevTools tab and why it is sufficient). Phase 5 — no async without loading
  state; no missing error paths, cite each. Phase 2 — no ARIA or focus gaps, name each component
  checked.] | Fix: N/A |
  Do-nothing cost: No production risk — [per-phase confirmation; cite each check; do not write
  'implementation looks correct' without per-phase evidence].
Mark: FINDINGS COMPLETE.]

---

## FRAMEWORK VOCABULARY CHECK

Verify all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here using it correctly and note which phase
should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, unnecessary_rerenders, findings_count,
do_nothing_costs_present, findings_gate_fired, problem_gate_fired.
```
