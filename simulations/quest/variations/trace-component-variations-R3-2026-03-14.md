Written to `simulations/quest/variations/trace-component-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — trace-component

**5 variations across 3 single-axis + 2 combined:**

| V | Axis | Core mechanism | Key rubric bet |
|---|------|----------------|----------------|
| **V-01** | Role sequence | Frontend Engineer (Ph 1–2) → Performance Engineer (Ph 3–4) → Accessibility Specialist (Ph 5 + FINDINGS) | C-07/C-09: specialized per-phase roles yield deeper findings, especially Phase 4 re-render diagnosis |
| **V-02** | Phrasing register | Second-person imperative throughout ("Name the component. 'The button' doesn't pass.") vs. V-05 R2's fill-in-the-blank declarative | C-01 through C-05 floor: tests whether rule-statement register enforces as well as slot-shape register |
| **V-03** | Inertia framing | Do-nothing cost is a mandatory N/A-prohibited FINDINGS table column with escape instruction in column definition block | C-15: structural per-row do-nothing cost vs. advisory per-finding field |
| **V-04** | Combined: staged roles + C-14 column header + C-15 do-nothing cost | Column escape instruction embedded in literal Markdown header cell `| What this adds vs. ad-hoc [N/A not allowed...] |`; staged roles; mandatory do-nothing cost column | C-14: header-cell embedding vs. preceding-block embedding; all three new criteria in one template |
| **V-05** | Combined: all three new criteria | V-05 R2 base + FINDINGS gate (C-13 gate family extension) + literal column header embedding (C-14) + mandatory do-nothing cost with its own exact-phrase gate (C-15) | Full ceiling test: C-13+C-14+C-15 stacked on proven C-10+C-11+C-12 |

**Key structural bets in R3:**

- **C-13 (gate family):** R2's gates covered Phases 1–5 only. V-05 extends the family to cover FINDINGS — "no impact," "minor issue," "low risk" do not close the section. A gate family that covers phases but not the closing consolidation section is incomplete.
- **C-14 (column header embedding):** R2 put the escape instruction in a `Column instructions:` block before the table. C-14 targets the Markdown column header cell itself — `| Column Name [instruction] |` — so the constraint is part of the header row the model writes, not preceding advisory text.
- **C-15 (do-nothing cost):** V-02/V-04 in R2 had a "Do-nothing cost" advisory field in FINDINGS. C-15 requires a mandatory column with per-row enforcement — same structural pattern that made the comparison column effective in R2.
- **Role sequence (V-01, V-04):** Not explored in R2. The three-role handoff is the single new axis added for R3 against the V-05 R2 baseline.
it to be structurally enforced — a mandatory column, N/A-prohibited, per-row, not just a per-finding advisory field that can be cleared once.
- **Role sequence (V-01, V-04)**: R2 used "Auto-selected frontend expert" for the entire trace. Staged specialist roles are a new single-axis variation not explored in R2.

---

## V-01: Staged Expertise — Role Sequence

**Axis:** Role sequence — three named specialist roles activate at specific phase windows. The Frontend Engineer handles event and component structure (Phases 1–2). The Performance Engineer handles state mutation and re-render analysis (Phases 3–4). The Accessibility and UX Specialist closes with side effects, final state, and findings (Phase 5 + FINDINGS). Each role is named at the phase header where it activates.

**Hypothesis:** V-05 R2 auto-selects one "frontend expert" role for the entire trace. A single generalist performs adequately across C-01 through C-06 but may not surface the analytical depth that specialized roles bring at phase-specific decision points — particularly Phase 4 (unnecessary re-render diagnosis requires a performance lens) and FINDINGS (accessibility gaps require an a11y frame). Staged role handoffs force the model to shift analytical frames at the exact boundaries where those frames are most productive. Predicted failure mode: role transitions introduce coordination overhead and the model conflates or abbreviates the incoming role's frame rather than switching cleanly. Do-nothing cost is an advisory per-finding field, not a mandatory column.

```
You are running /trace:component. Three specialist roles share this trace.
Each role activates at the phase window declared below.
Complete phases in sequence. Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.

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
- Phases 1–2 → Frontend Engineer: expert in [framework] component architecture and event propagation
- Phases 3–4 → Performance Engineer: expert in [framework] rendering model and state optimization
- Phase 5 + FINDINGS → Accessibility and UX Specialist: expert in ARIA, focus management, and production risk

[PHASE 0 GATE: Framework, vocabulary, surface, action, expected outcome, and all three roles declared.
Mark: PHASE 0 COMPLETE.]

---

## PHASE 1: EVENT ANCHOR
[Role: Frontend Engineer]

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Exact UI component name — not "the button," not "the input field"]
Event payload: [Data carried in the event — e.g., value, id, coordinates. If none: "No payload — void event."]
Handler: [The specific function name or lifecycle hook that receives this event.
  If no handler registered: "No handler on [ComponentName] — event bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler does not close
this phase. Writing "an event fires" without the event type and firing component does not close this
phase. Handler must be a function name or lifecycle hook — not "the event handler."
Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH
[Role: Frontend Engineer]

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch — name which]
[IntermediateComponent] (what it does with this event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

If multiple subtrees affected:
Branch A: [ComponentA] → [ParentA] → [ContextConsumer A]
Branch B: [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a flat list without directional
relationships does not close this phase. Writing "traverses the component tree" without naming hops
does not close this phase. At least two named components with a directional arrow between them
are required. Mark: PHASE 2 COMPLETE.]

---

## PHASE 3: STATE MUTATION MAP
[Role: Performance Engineer — handoff from Frontend Engineer]

For each mutation this action triggers:

Mutation [N]:
  Owner: [Component or store — exact name matching the tree in Phase 2]
  Key: [`stateKey` or `store.slice` — specific field name, not "the state"]
  Old: [Shape or value before — e.g., `false`, `[]`, `{id:null}`]
  New: [Shape or value after — e.g., `true`, `[{id:1}]`, `{id:"abc"}`]
  Mechanism: [useState setter / dispatch(action()) / store.$patch / this.setState]
  Timing: SYNC (completes in the same tick) OR ASYNC (after: [mechanism])

If no mutation: "No mutation — [read-only / presentational]. Justification: [specific reason — not
  'no state in this component' without explaining why this action is presentational]."

[PHASE 3 GATE: Writing "State updates" does not close this phase.
Writing "state changes in response to the action" does not close this phase.
Writing "the store is modified" without naming the key or slice does not close this phase.
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY
[Role: Performance Engineer]

Using mutations from Phase 3, fill this table for every component that re-renders.

| Component | Re-render cause | Count × verdict |
|-----------|-----------------|-----------------|
| [Name] | [owns state X / subscribes to context Y / receives new prop Z from parent] | [1× — justified: owns the toggled boolean; re-render is required to show the updated value] |
| [Name] | [receives full formState prop from parent] | [3× per keystroke — unnecessary: receives full formState instead of the specific field it renders; fix: pass only isValid or wrap in React.memo with custom comparator] |
| [Name] | [reason] | [0× — not in re-render path: selector returns memoized reference; no prop changes reach this component] |
[Minimum one row. Add rows for every re-rendering component.]

Count × verdict format rules:
- Always include the number (or rate) AND the judgment in the same cell.
- "Justified" requires a specific structural reason — not just "re-render is expected."
- "Unnecessary" requires the exact cause AND a specific fix (hook name, API, or boundary).
- Separating count and verdict into two separate columns or a separate subsection does not
  satisfy this section — both must be in the same cell, in the same writing act.

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing "components re-render as expected" without naming them does not close this phase.
Writing count in one place and verdict in a separate subsection does not close this phase —
count × verdict must be in the same cell for every row.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE
[Role: Accessibility and UX Specialist — handoff from Performance Engineer]

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay and callback / route / storage key and value shape]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation
triggered by this action."

**Final UI state:**

Synchronous state (after all SYNC mutations and Phase 4 re-renders complete):
[Name visible elements, disabled states, loading indicators, error messages — specifically.
What element, what state, visible to whom.]

Post-async state (if any side effect exists):
  Success: [What the user sees when the async effect resolves]
  Error: [What the user sees if it fails — or "No error state defined — missing error state, see FINDINGS."]
  If synchronous only: "No async settle point."

[PHASE 5 GATE: Writing "UI updates accordingly" does not close this phase.
Writing "the UI reflects the state changes" does not close this phase.
Writing "success and error states are handled" without describing what the user sees does not close
this phase. A concrete final state names specific visible elements, changed values, or confirmed
no-change. Mark: PHASE 5 COMPLETE.]

---

## FINDINGS
[Role: Accessibility and UX Specialist]

Review all five closed phases. Check for:
- Phase 4 components with "unnecessary" verdict — each needs a finding here
- Phase 5 async effects without a loading state between trigger and settle
- Phase 5 error paths written as "No error state defined"
- Phase 2 components missing ARIA, losing focus after action, or creating keyboard traps
- Framework vocabulary terms declared in Phase 0 that did not appear in any phase

For each finding:
  Severity: P1 (critical) / P2 (degraded) / P3 (cosmetic or a11y debt)
  Source: [Phase number + component or state key]
  Problem: [Specific — "ButtonGroup re-renders on every keystroke because it receives the full
    formState object" not "may have performance issues"]
  Fix: [One concrete, minimal fix — specific hook, attribute, or boundary. Not general advice.]
  Do-nothing cost: [What ships to production without this fix — name the affected user population
    and the exact failure mode, or the specific future engineering consequence.]

If no findings: "No issues across all five phases. Justification: [per-role summary — Frontend
Engineer: Phase 1–2 checks; Performance Engineer: Phase 3–4 checks; Accessibility Specialist:
Phase 5 checks. Name why each role's check came back clean — not just 'implementation looks correct']."

---

## FRAMEWORK VOCABULARY CHECK

Verify that all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here using it correctly and note which phase
should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
roles_used, phases_completed, mutations_count, rerender_count, unnecessary_rerenders, issues_count.
```

---

## V-02: Phrasing Register — Imperative/Conversational

**Axis:** Phrasing register — all constraint instructions are rewritten in direct second-person imperative throughout ("Name the component. 'The button' doesn't pass. 'The input' doesn't pass.") instead of V-05 R2's fill-in-the-blank declarative register (`[Exact UI component name — not "the button"]`). Phase gate text becomes a standalone imperative paragraph rather than a bracketed inline block. Do-nothing cost is an advisory per-finding field.

**Hypothesis:** V-05 R2's declarative fill-in-the-blank register makes the path of least resistance a faithful fill of the template slot — constraints are expressed as slot shapes and negative examples. The imperative register makes the same constraints visible as explicit rules. The question is whether explicit rule-statement ("Name the component. Don't write 'the button.'") is as effective as slot-shape encoding (`[Exact UI component name — not "the button"]`) for constraint enforcement. Predicted failure: without a template slot to fill, output structure may be less consistent; the conversational register may also make the model more likely to skip explicit "No payload — void event" style escape clauses.

```
You are running /trace:component. Work through each step in order.
Mark each step DONE before moving to the next. Do not skip ahead.

---

## STEP 0 — DECLARE YOUR CONTEXT

State the frontend framework. State the state management layer. Declare your role.

Don't guess silently — name everything:
- Framework: React / Vue / Angular / Svelte / other. Include the version if you can infer it.
- State management: useState / Redux / Zustand / Pinia / NgRx / other.
- Rendering model: Virtual DOM / Signals-based / Zone.js / Svelte compiler / other.
- Role: choose the right expert for this framework. Name who you are for this trace.

Declare 3–5 framework-specific terms you'll use. Define each in one clause.
These terms must show up in your trace below — if you don't use a term, the trace is incomplete.
  - [Term 1]: [definition]
  - [Term 2]: [definition]
  - [Term 3]: [definition]

Name the surface and the action:
- Surface: which page or component?
- User action: which UI element, which event type, what does the user do?
- Expected outcome: what does the user expect to happen?

[STEP 0 DONE]

---

## STEP 1 — ANCHOR THE EVENT

Name four things about the event that starts this trace. All four are required.

1. Event type: write the actual event name — onClick, onChange, onSubmit, onDragEnd, or the custom
   event string. "An event fires" doesn't pass. "A click happens" doesn't pass.

2. The component that fired it: write its actual name — not "the button," not "the input field,"
   not "the form element." The component name. If it's unnamed, give it a name from context.

3. Payload: what data rides in the event? If none, say "No payload — void event."

4. Handler: write the function name or lifecycle hook that catches this event.
   "The event handler" doesn't pass. "The handler function" doesn't pass.
   If nothing catches it here, say "No handler on [ComponentName] — bubbles to [ParentComponent]."

Don't move to STEP 2 until all four are named.

[STEP 1 DONE]

---

## STEP 2 — TRACE THE COMPONENT PATH

Draw the chain from the event-receiving component up to the root of the affected subtree.
Name every hop. Show the direction and the relationship at each hop.

Use this structure:
[EventReceivingComponent] (the component from STEP 1)
  ↓ [prop callback / context subscription / store dispatch — which one?]
[IntermediateComponent] (what does it do with this?)
  ↓ [relationship]
[ProviderOrRoot] (top of the affected subtree)

If two subtrees are affected, trace both branches separately — Branch A and Branch B.

Don't write a flat list like "[A, B, C]" without directions — that doesn't pass.
Don't write "traverses the tree upward" without naming the hops — that doesn't pass.
The minimum is two named components with an arrow between them.

[STEP 2 DONE]

---

## STEP 3 — MAP EVERY STATE MUTATION

List every piece of state that changes when this event fires.
For each mutation:
- Owner: which component or store owns this state? Match the name to STEP 2's tree.
- Key: the exact state key or store slice. Not "the state" — the field name. Use backticks.
- Old: what did it look like before? Give the value or shape.
- New: what does it look like after? Give the value or shape.
- Mechanism: how does the change happen? useState setter / dispatch / store.$patch / this.setState.
- Timing: SYNC (same tick) or ASYNC (after: name the mechanism).

If nothing mutates: say "No mutation — [read-only / presentational]. Here's why: [specific reason
  — not 'no state in this component' without explaining why this action is presentational]."
That's a valid finding. But you must say it — silence doesn't pass.

"State updates" doesn't pass.
"State changes in response to the action" doesn't pass.
"The store is modified" without naming the slice doesn't pass.

[STEP 3 DONE]

---

## STEP 4 — INVENTORY THE RE-RENDERS

For every component that re-renders because of STEP 3's mutations, fill one row in this table.

| Component | Re-render cause | Count × verdict |
|-----------|-----------------|-----------------|
| [Name] | [owns state X / subscribes to context Y / receives new prop Z] | [1× — justified: owns the toggled boolean; must re-render to show the updated value] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState when it only renders isValid; fix: pass only isValid or wrap in React.memo with custom comparator] |
| [Name] | [reason] | [0× — not in re-render path: selector returns memoized reference; nothing reaches this component] |

Rules for the Count × verdict cell:
- Write the count and the judgment in the same cell — not in separate columns, not with the
  verdict in a subsection below the table.
- "Justified" needs a structural reason. "Expected behavior" doesn't pass.
- "Unnecessary" needs the exact cause AND a specific fix — a hook name, API, or boundary.
- "0×" needs a confirmed reason why this component is not in the re-render path.

"Several components re-render" without naming them doesn't pass.
"Components re-render as expected" without naming them doesn't pass.
Count and verdict in separate places doesn't pass — same cell, same writing act.

[STEP 4 DONE]

---

## STEP 5 — SIDE EFFECTS AND FINAL STATE

**Side effects.** For each effect triggered by this action:
  Type: API call / timer / navigation / storage write / subscription
  Detail: for API — method + endpoint; for timer — delay + callback; for nav — route;
    for storage — key + value shape.
  Mechanism: useEffect dependency / thunk / saga / Pinia action / router hook.

If none: say it — "No side effects — confirmed synchronous: no API calls, timers, subscriptions,
or navigation." Silence doesn't pass.

**What the user sees.** After all SYNC mutations and re-renders from STEP 3 and STEP 4:
- Name the visible elements. Name the disabled states. Name loading indicators and error messages.
- Be specific: which element, what state, who sees it.

If there are async effects:
  Success: what does the user see when it resolves?
  Error: what does the user see if it fails? Or say "No error state defined — see FINDINGS."
  If synchronous only: say "No async settle point."

"UI updates accordingly" doesn't pass.
"The UI reflects the state changes" doesn't pass.
"Success and error states handled" without describing what the user sees doesn't pass.

[STEP 5 DONE]

---

## FINDINGS

Pull together everything from STEPS 1–5. Check for:
- STEP 4 rows marked "unnecessary" — each is a finding here.
- STEP 5 async effects with no loading state between trigger and settle.
- STEP 5 error paths written "No error state defined."
- STEP 2 components that lose focus, have no ARIA role, or create keyboard traps.
- Framework vocabulary terms from STEP 0 that didn't appear in STEPS 1–5.

For each finding:
  Severity: P1 (blocks users) / P2 (degrades experience) / P3 (polish or a11y debt)
  Source: [which STEP, which component or state key]
  Problem: be specific — "ButtonGroup re-renders 3× per keystroke because it receives the full
    formState object" not "may have performance issues."
  Fix: one concrete fix — name the hook, boundary, or ARIA attribute.
  Do-nothing cost: what ships to production if this finding is not addressed? Name the affected
    user population and the exact failure mode, or the specific engineering consequence.

If no findings: "No issues across all five steps. Here's why each check came back clean:
[per-step summary — name the specific check for each step, not just 'implementation looks correct']."

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
steps_completed, mutations_count, rerender_count, unnecessary_rerenders, issues_count.
```

---

## V-03: Inertia Framing — Do-Nothing Cost as Mandatory Column

**Axis:** Inertia framing (C-15) — the FINDINGS section is restructured as a table with "Do-nothing cost" as a mandatory N/A-prohibited column. The escape instruction appears in the column definition block adjacent to the header, making it visible at cell-fill time. Every finding must declare a specific production consequence or future engineering cost. The rest of the template is the V-05 R2 baseline (exact-phrase gates, merged count×verdict, sequential phases).

**Hypothesis:** V-05 R2 included a per-finding "Fix" field but no mandatory do-nothing cost. Without it, the findings section answers "what broke" and "how to fix it" but not "what ships if we don't." That's the PM-facing question. Making it a mandatory table column with an N/A-prohibited instruction — rather than an advisory field that can be written once or skipped — forces a production-consequence declaration for every finding. Predicted failure: in hypothetical trace scenarios, the model fabricates generic cost claims ("users may experience issues") rather than specific ones; the escape instruction for the exception case may be insufficient to prevent this.

```
You are running /trace:component. Complete each phase in sequence.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.

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
  If no handler registered: "No handler on [ComponentName] — event bubbles to [ParentComponent]."]

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

If multiple subtrees affected:
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

| Component | Re-render cause | Count × verdict |
|-----------|-----------------|-----------------|
| [Name] | [owns state X / subscribes to context Y / receives new prop Z] | [1× — justified: owns the toggled boolean; re-render required to show the updated value] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of specific field; fix: pass only isValid or wrap in React.memo with custom comparator] |
| [Name] | [reason] | [0× — not in re-render path: selector returns memoized reference; nothing reaches this component] |
[Minimum one row. Count × verdict must be in the same cell — count in one column and verdict in
a separate subsection does not satisfy this table.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing count and verdict in separate columns or a separate subsection does not close this phase —
count × verdict must be in the same cell for every row.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay / route / storage key and value shape]
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
A concrete final state names specific visible elements, changed values, or confirmed no-change.
Mark: PHASE 5 COMPLETE.]

---

## FINDINGS

Review all five closed phases. Fill this table for every issue found. Every row is a finding.

Column instructions:

- **Problem**: Name the component and the exact issue. "May have performance issues" does not pass —
  name the component, the cause, and the mechanism.

- **Fix**: One concrete, minimal fix — name the specific hook, boundary, ARIA attribute, or API.
  "Add error handling" does not pass — name the specific handler location or pattern.

- **Do-nothing cost**
  [N/A not allowed — fill every row. Write one of:
  (a) "Ships: [specific user-visible consequence in production — name the user population
       and the exact failure mode — e.g., 'keyboard users cannot resume after this action
       without a mouse click', 'users see a blank panel on save failure with no recovery
       affordance', 'screen readers announce the wrong element after state updates']."
  (b) "Deferred: [specific future engineering cost — e.g., 'this re-render pattern requires
       touching 5 components once the form scales beyond 3 fields; cost grows with data size'].
       Exception — [specific structural reason this issue has zero production consequence —
       e.g., 'this component is behind a disabled feature flag; consequence is zero until the
       flag ships to production']. Exception requires a specific reason — not just asserting
       no consequence."
  A blank cell or "N/A" fails this column. Exception (b) requires justification.]:

| Sev | Type | Source | Problem | Fix | Do-nothing cost |
|-----|------|--------|---------|-----|-----------------|
| [P1/P2/P3] | [Unnecessary re-render / Missing loading state / Error state gap / A11y failure] | [Phase + component] | [specific — component + mechanism + cause] | [concrete fix — hook, boundary, or ARIA attribute] | [Ships: specific user consequence / Deferred: specific cost. Exception — specific reason.] |
[Add one row per finding.]

If no findings, write one row:
| P0 | No issues | All phases | [per-phase summary: name why each gap-check came back clean — Phase 4 count×verdict cells, Phase 5 error paths, Phase 2 ARIA checks] | N/A | No production risk: [per-phase confirmation — name the specific check per phase, not 'implementation looks correct'] |

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, unnecessary_rerenders, issues_count,
do_nothing_costs_present.
```

---

## V-04: Combined — Staged Roles + C-14 Column Header Embedding + C-15 Do-Nothing Cost

**Axis (combined):** Role sequence + output format (C-14 column header embedding) + inertia framing (C-15) — three specialist roles handed off at phase boundaries (V-01 approach), the comparison column escape instruction embedded as part of the literal Markdown column header cell syntax (C-14: the `| Column Name [instruction...] |` cell is where the model encounters the constraint, at the moment of writing the header row itself), and do-nothing cost as a mandatory N/A-prohibited FINDINGS table column (C-15).

**Hypothesis:** R2 embedded the escape instruction in a block before the table (`Column instructions: ... **What this adds vs. ad-hoc** [N/A not allowed...]`). C-14 specifically targets the column header cell itself — the instruction is part of the Markdown table header row syntax. The model writes `| What this adds vs. ad-hoc [N/A not allowed. Invisible: [...] Observable: [...]. Exception — [...]] |` as the header, which means the constraint is encountered at the structural moment of table construction, not in preceding advisory text. Combined with staged roles and a mandatory do-nothing cost column, this tests whether all three new aspirational criteria cohere in one template.

```
You are running /trace:component. Three specialist roles share this trace.
Each role activates at the phase window declared in PHASE 0.
Complete phases in sequence. Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.

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
- Phases 3–4 → Performance Engineer: [framework] rendering and state optimization expert
- Phase 5 + FINDINGS → Accessibility and UX Specialist: ARIA, focus management, production risk

[PHASE 0 GATE: Framework, vocabulary, surface, action, expected outcome, and all three roles declared.
Mark: PHASE 0 COMPLETE.]

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
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY
[Role: Performance Engineer]

Fill this table for every component that re-renders because of Phase 3 mutations.

| Component | Re-render cause | Count × verdict [both in this cell, same writing act — "Nx — justified: [specific structural reason]" or "Nx per action — unnecessary: [exact cause]; fix: [specific hook, API, or boundary]" or "0× — not in re-render path: [confirmed reason]" — count and verdict in separate columns or a subsection does not satisfy this column] | What this adds vs. ad-hoc [N/A not allowed — fill every cell: write "Invisible: [specific thing DevTools cannot show without Profiler or source-stepping — e.g., 'which context subscriber owns this re-render', 'whether selector returned a new reference']" OR "Observable: [specific tab — Network/Console/Elements/Profiler]. Exception — [specific structural reason this row is fully transparent to ad-hoc DevTools without component-level tooling — e.g., 'this is a controlled input; its re-render IS the DOM mutation, visible in Elements']. Exception requires justification — not just asserting it."] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; this re-render is required to show the updated value] | [Invisible: whether this re-render is due to state ownership vs prop propagation is not distinguishable in the DOM without component-level DevTools] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of the specific field it renders; fix: React.memo + pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector contract — DevTools shows a re-render occurred, not whether it was required] |
[Minimum one row. Add rows for every re-rendering component.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing count and verdict in separate columns or a separate subsection does not close this phase.
Leaving a "What this adds vs. ad-hoc" cell blank or writing "N/A" does not close this phase.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE
[Role: Accessibility and UX Specialist — handoff from Performance Engineer]

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay / route / storage key]
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
A concrete final state names specific visible elements, changed values, or confirmed no-change.
Mark: PHASE 5 COMPLETE.]

---

## FINDINGS
[Role: Accessibility and UX Specialist]

Consolidate from Phase 4 "Count × verdict" cells marked "unnecessary," Phase 4 "What this adds
vs. ad-hoc" cells marked "Invisible" that surface a structural problem, Phase 5 error paths
written "No error state defined," and Phase 2 components missing ARIA, losing focus, or creating
keyboard traps.

Fill this table for every issue found.

| Sev | Source | Problem | Fix | Do-nothing cost [N/A not allowed — fill every row: write "Ships: [specific user-visible consequence in production — name the affected user population and exact failure mode, e.g., 'keyboard users cannot resume without a mouse click', 'users see a blank state on network failure with no recovery']" OR "Deferred: [specific future engineering cost, e.g., 'pattern requires refactor touching N components once form scales']. Exception — [specific structural reason this finding has zero production consequence — e.g., 'behind a disabled feature flag; consequence is zero until flag ships']. Exception requires justification — not just asserting no consequence."] |
|-----|--------|---------|-----|-----------------|
| [P1/P2/P3] | [Phase + component] | [specific — component + mechanism + cause, not "may have issues"] | [concrete — hook, boundary, or ARIA attribute] | [Ships: specific consequence / Deferred: specific cost. Exception — specific reason.] |
[Minimum one row per finding.]

If no findings:
| P0 | All phases | No issues — [per-role summary: Frontend Engineer Phase 1–2 checks; Performance Engineer Phase 3–4 checks; Accessibility Specialist Phase 5 checks — name what each role checked and why it came back clean] | N/A | No production risk: [confirm per phase why each gap-check came back clean] |

---

## FRAMEWORK VOCABULARY CHECK

Verify that all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here using it correctly and note which phase
should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
roles_used, phases_completed, mutations_count, rerender_count, unnecessary_rerenders,
issues_count, do_nothing_costs_present.
```

---

## V-05: Combined — Full Gate Family (C-13) + Column Header Embedding (C-14) + Do-Nothing Cost Column (C-15)

**Axis (combined):** All three new aspirational criteria stacked on V-05 R2's proven base — the exact-phrase gate family is extended to cover the FINDINGS section (gates now fire at Phases 1–5 AND in FINDINGS, covering do-nothing cost failure strings — C-13); the comparison column escape instruction is embedded in the literal Markdown column header cell syntax, part of the header row the model writes (C-14); the do-nothing cost is a mandatory N/A-prohibited FINDINGS column with its own exact-phrase gate (C-15).

**Hypothesis:** V-05 R2 achieves 100 on C-01 through C-12. The three new criteria are C-13, C-14, C-15. C-13's key question is whether the gate family is complete: R2's gates covered phases but not FINDINGS — if a model writes "no impact" as a do-nothing cost in FINDINGS, no gate in R2 intercepts it. Extending the gate family to cover FINDINGS gates for do-nothing cost failure strings ("no impact" / "minor issue" / "low risk" do not close FINDINGS) completes the family. C-14: embedding the escape instruction in the literal column header cell — `| What this adds vs. ad-hoc [N/A not allowed...] |` — makes the constraint part of the Markdown syntax the model writes, not preceding advisory text it must recall. C-15: do-nothing cost as a mandatory column with a gate that intercepts generic cost strings. Predicted failure mode: FINDINGS becomes dense enough that Phase 4's complexity (count×verdict + comparison column) causes Phase 1–2 abbreviation — but the phase-gate structure from V-05 R2 prevents this by requiring COMPLETE markers before advancing.

```
You are running /trace:component. Complete each phase in sequence.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.
The FINDINGS section also carries a gate that names the exact strings that do not close it.

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

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a comma-separated list without
directional relationships does not close this phase. Writing "traverses the component tree upward"
without naming hops does not close this phase. At least two named components with a directional
arrow between them are required. Mark: PHASE 2 COMPLETE.]

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

| Component | Re-render cause | Count × verdict [both pieces in this cell, same writing act — co-location required; write "Nx — justified: [specific structural reason]" or "Nx per action — unnecessary: [exact cause]; fix: [specific hook or API]" or "0× — not in re-render path: [confirmed reason]"; count and verdict in separate columns or a separate section does not satisfy this column] | What this adds vs. ad-hoc [N/A not allowed — fill every cell; write "Invisible: [specific thing DevTools cannot show without Profiler or source-stepping — e.g., 'which context subscriber owns this re-render', 'whether the selector returned a new reference vs the same reference']" OR "Observable: [specific tab — Network/Console/Elements/Profiler]. Exception — [specific structural reason this row is fully transparent to ad-hoc DevTools without component-level tooling — e.g., 'this is a controlled input; its re-render IS the DOM mutation, directly visible in Elements tab without component tooling']. Exception requires explanation — not just claiming it."] |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean; this re-render is required to show the updated value] | [Invisible: whether this re-render is due to state ownership vs prop propagation is not distinguishable in the DOM without component-level DevTools] |
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

Fill this table for every finding.

| Sev | Source | Problem | Fix | Do-nothing cost [N/A not allowed — fill every row; write "Ships: [specific user-visible consequence in production — name the affected user population and the exact failure mode, e.g., 'keyboard users cannot resume after this action without a mouse click', 'users see a blank panel on network failure with no recovery affordance', 'screen readers announce stale element state after re-render']" OR "Deferred: [specific future engineering cost, e.g., 'this pattern requires a refactor touching N components once the feature scales to more than 3 items; cost grows with data size']. Exception — [specific structural reason this finding has zero production consequence — e.g., 'this component is behind a disabled feature flag; production consequence is zero until the flag ships']. Exception requires a specific reason — not just asserting no consequence."] |
|-----|--------|---------|-----|-----------------|
| [P1/P2/P3] | [Phase + component] | [specific — component + mechanism + cause, not "may have issues"] | [concrete — hook, boundary, or ARIA attribute] | [Ships: specific consequence / Deferred: specific cost. Exception — specific reason.] |
[Minimum one row per finding.]

[FINDINGS GATE: Writing "no impact" as a do-nothing cost does not close this section.
Writing "minor issue" as a do-nothing cost does not close this section.
Writing "low risk" as a do-nothing cost does not close this section.
Writing "no user-facing consequence" without naming why does not close this section.
A do-nothing cost must name: the specific user population affected AND the exact failure mode
OR the specific future engineering consequence with a scope (number of components, growth factor,
or triggering condition).
If there are no findings, write one row:
  Sev: P0 | Source: All phases | Problem: [per-phase summary — Phase 4: all count×verdict cells are
  justified, cite each; all 'What this adds vs. ad-hoc' cells are Observable exceptions, cite each.
  Phase 5: no async effects without loading states; no missing error paths.
  Phase 2: no ARIA gaps or focus loss detected.] | Fix: N/A |
  Do-nothing cost: No production risk — [confirm per phase why each check came back clean;
  do not write 'implementation looks correct' without per-phase evidence].
Mark: FINDINGS COMPLETE.]

---

## FRAMEWORK VOCABULARY CHECK

Verify that all declared terms from Phase 0 appeared in the trace.
- [Term 1]: Phase [N], [section] — "[exact phrase used]"
- [Term 2]: Phase [N], [section] — "[exact phrase used]"
- [Term 3]: Phase [N], [section] — "[exact phrase used]"

If any term did not appear: write a correction sentence here using it correctly and note which phase
should have used it.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, unnecessary_rerenders, issues_count,
do_nothing_costs_present, findings_gate_fired.
```
