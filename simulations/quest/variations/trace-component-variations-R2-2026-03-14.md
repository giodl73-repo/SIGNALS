Written to `simulations/quest/variations/trace-component-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — trace-component

**5 variations across 3 single-axis + 2 combined:**

| V | Axis | Core mechanism | Key rubric bet |
|---|------|----------------|----------------|
| **V-01** | Lifecycle: exact-phrase gate naming | Each phase close gate prints the literal failure phrase ("'State updates' does not close this phase") | C-11: adversarial specificity — model encounters its own likely failure string at the exact boundary |
| **V-02** | Format: pre-printed escape column | Escape pattern embedded IN the column header instruction, not preamble | C-12: model has a fill-in-the-blank sentence structure at cell-fill time, not a remembered constraint |
| **V-03** | Format: merged count×verdict cell | Count and verdict collapsed into one cell by template; format pre-printed | C-10: co-location structurally impossible — not just same row, same cell |
| **V-04** | Combined: wide table synthesis | FRAMEWORK GATE + event table with inertia column + separate re-render table with count×verdict | C-07 + C-10: the explicit R1 synthesis target — wins both discriminators simultaneously |
| **V-05** | Combined: all three hard criteria | Exact-phrase gates + merged count×verdict + mandatory escape column | C-10 + C-11 + C-12: full aspirational ceiling test |

**Key differences from R1:**

- **V-01 vs V-04 R1**: R1's Phase 3 gate said "A flat list does not close this phase." V-01 R2 says "'State updates' does not close this phase." One intercepts the abstract category; the other intercepts the specific string.
- **V-02 vs V-05 R1**: R1's escape pattern was in the preamble. V-02 R2 embeds it directly in the column header instruction — encountered at cell-fill time, not before the table begins.
- **V-03**: No R1 equivalent. Merging count+verdict into one cell is stricter than V-04 R1's "same row" — it makes spatial separation physically impossible.
- **V-04 R2**: The explicit synthesis target from R1's scorecard. Splits into two tables (event trace + re-render detail) rather than one 8-column monster.
- **V-05 R2**: The complexity stress test. Predicted failure mode: Phase 4 becomes dense enough that Phases 1–2 get abbreviated.
nforcement mechanisms remain coherent?

---

## V-01: Exact-Phrase Inline Gate Naming

**Axis:** Lifecycle emphasis — each phase close gate names the *literal vague phrase* the model would write to escape the phase without satisfying it. The gate appears at the phase boundary where that phrase would occur, not in a preamble. "State updates" does not close Phase 3. "Several components re-render" does not close Phase 4. "UI updates accordingly" does not close Phase 5. The model encounters its own likely failure string at the moment it would write it.

**Hypothesis:** V-04's gates were structurally correct but the close conditions were general: "A flat list of component names without structure does not close this phase." C-11 specifically requires the gate to name the exact vague phrase. The difference is adversarial precision — when the model is composing Phase 3 output, "GATE: 'State updates' does not close this phase" fires against the specific phrase, not against an abstract description of what insufficiency looks like. General gates prevent category errors; exact-phrase gates intercept specific failure strings.

```
You are running /trace:component. Complete each phase in sequence.
Do not begin any phase until the prior phase is marked COMPLETE.
Each phase close gate names the exact phrase that does not close the phase.

---

## PHASE 0: SURFACE AND FRAMEWORK

Surface: [UI component or page — name it specifically]
User action: [Exact user action — name the element and event type]
Expected outcome: [What the user expects after the action]
Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Role: [Auto-selected frontend expert — match to framework]

[PHASE 0 CLOSE: Framework and state management are named. Role is declared. Mark: PHASE 0 COMPLETE.]

---

## PHASE 1: EVENT ANCHOR

Event type: [onClick / onChange / onSubmit / onDragEnd / custom event name]
Firing component: [Component name — the exact UI element that fires the event. Not "the button."]
Event payload: [Data carried in the event — e.g., value, id, coordinates. If none: "No payload — void event."]
Handler: [The specific function name or lifecycle hook that receives this event.
  If no handler registered: "No handler on [ComponentName] — event bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler function does not close
this phase. Writing "an event fires" without the event type and firing component does not close this phase.
Handler is a function name (e.g., handleSubmit, onItemClick) or lifecycle hook — not "the event handler."
Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH

Trace from the event-receiving component to the root of the affected subtree.
Name every hop. Show the relationship at each hop.

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch — name which]
[IntermediateComponent] (what it does with this event)
  ↓ [relationship]
[ProviderOrRootComponent] (top of affected subtree)

If multiple subtrees are affected:
Branch A: [ComponentA] → [ParentA] → [ContextConsumer A]
Branch B: [ComponentB] → [ParentB] → [ContextConsumer B]

[PHASE 2 GATE: Writing "[ComponentA, ComponentB, ComponentC]" as a flat list without directional
relationships does not close this phase. Writing "traverses the component tree" without naming hops
does not close this phase. At least two named components with a directional arrow between them are
required. Mark: PHASE 2 COMPLETE.]

---

## PHASE 3: STATE MUTATION MAP

List every state mutation triggered by this event.
For each mutation: owner, key, old shape, new shape, mechanism, timing.

Mutation [N]:
  Owner: [Component name or store name — exact match to Phase 2 tree]
  Key: [State key or slice — e.g., `isLoading`, `cart.items`, `user.authToken`]
  Old: [Value or shape before the action — e.g., `false`, `[]`, `{id: null}`]
  New: [Value or shape after the action — e.g., `true`, `[{id:1}]`, `{id:"abc"}`]
  Mechanism: [useState setter / dispatch / store.$patch / computed setter / this.setState]
  Timing: SYNC (completes in the same tick) OR ASYNC (after: [mechanism])

If no mutation: "No mutation — this action is [read-only / presentational]. Justification: [specific reason].
  This is a valid finding, not a gap, but it must be explicit."

[PHASE 3 GATE: Writing "State updates" does not close this phase.
Writing "state changes in response to the action" does not close this phase.
Writing "the store is modified" without naming the slice does not close this phase.
At least one mutation with owner, key, old value, new value, and mechanism is required.
Mark: PHASE 3 COMPLETE.]

---

## PHASE 4: RE-RENDER INVENTORY

Using the mutations from Phase 3, list every component that re-renders and why.

| Component | Why it re-renders | Count × verdict |
|-----------|-------------------|-----------------|
| [Name] | [owns state X / subscribes to context Y / receives new prop Z from parent] | [1× — justified: component owns the toggled state, re-render is required to show the new value] |
| [Name] | [reason] | [3× per keystroke — unnecessary: receives full formState object instead of the specific field; fix: React.memo + pass only the relevant prop] |
| [Name] | [reason] | [0× — not in re-render path: selector returns same reference due to memoization] |
[Minimum one row. Add rows for every re-rendering component.]

Count × verdict format rules:
- Always include the number (or rate) AND the judgment in the same cell.
- "Justified" requires a specific structural reason — not just "re-render is expected."
- "Unnecessary" requires the exact cause AND a specific fix (hook name, API, or boundary).
- Separating count and verdict into separate columns or a subsection below the table does not satisfy
  this section — both must be in the same cell, in the same writing act.

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing "components re-render as expected" does not close this phase.
Writing a count in one column and a verdict in a separate subsection does not close this phase —
count and verdict must appear in the same cell for every row.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay and callback / route / storage key and value shape]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation
triggered by this action."

**Final UI state:**

Synchronous state (after Phase 3+4 complete):
[Name visible elements, disabled states, loading indicators, error messages.
Be specific: what element, what state, visible to whom.]

Post-async state (if any side effect exists):
  Success: [What the user sees when the async effect resolves]
  Error: [What the user sees if it fails — or "No error state defined — missing error state, see FINDINGS"]
  If synchronous only: "No async settle point."

[PHASE 5 GATE: Writing "UI updates accordingly" does not close this phase.
Writing "the UI reflects the changes" does not close this phase.
Writing "success and error states handled" without describing what the user sees does not close this phase.
A concrete final state names visible elements, changed values, or confirmed no-change. Mark: PHASE 5 COMPLETE.]

---

## FINDINGS

Review all five closed phases. Check for:
- Phase 4 components with "unnecessary" verdict — summarize as findings
- Phase 5 async effects without a loading state between start and settle
- Phase 5 error paths written as "No error state defined"
- Phase 2 components missing ARIA, losing focus after action, or creating keyboard trap

For each finding:
  Severity: P1 (critical) / P2 (degraded) / P3 (cosmetic or a11y debt)
  Location: [Phase number + component or state key]
  Problem: [Specific — "ButtonGroup re-renders on every keystroke because it receives the full formState
    object" not "may have performance issues"]
  Fix: [One concrete, minimal fix — specific hook, attribute, or boundary. Not general advice.]

If no findings: "No issues across all five phases. Justification: [per-phase summary — name why each
check came back clean, not just 'implementation looks correct']."

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, issues_count.
```

---

## V-02: Pre-Printed Escape Column

**Axis:** Output format — a mandatory "What this trace adds vs. ad-hoc" column whose escape pattern is embedded in the column header instruction itself, not described in a preamble. The column header reads: "If invisible to DevTools: write 'Invisible: [what].' If visible in DevTools: write 'Observable: [tab]. Exception — [why this row is not the rule].'" The model fills each cell with a concrete sentence structure, not a blank to rationalize around.

**Hypothesis:** V-05's "What ad-hoc misses" column put the escape pattern in the preamble: "Cannot be 'N/A.' If everything is visible, write: 'Nothing — this is the exception, not the rule.'" The preamble is processed before the table begins, not at cell-fill time. If the escape pattern is embedded in the column header instruction — visible at the moment the model fills each cell — the model has a concrete fill-in-the-blank structure rather than a remembered constraint. C-12 requires the escape to be "a substantive claim that itself constitutes analysis" — pre-printing the sentence structure makes that level of analysis the path of least resistance.

```
You are running /trace:component. Fill in the pre-printed template below.
All column headers are fixed. Fill every cell. Do not leave any cell blank.

---

## FRAMEWORK GATE

Detect the frontend framework from context. Declare it here before tracing.

Framework: [React / Vue / Angular / Svelte / other]
Version (if determinable): [e.g., React 18.2 — or "not specified"]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Rendering model: [Virtual DOM + reconciler / Signals-based / Zone.js / Svelte compiler / other]

Framework vocabulary declared (3–5 terms that will appear in the trace):
- [Term 1]: [definition in one clause]
- [Term 2]: [definition in one clause]
- [Term 3]: [definition in one clause]

[FRAMEWORK GATE: Do not begin EVENT TRACE TABLE until every field above is filled.
All framework terms declared here must appear in the table rows below.]

---

## SETUP

Surface: [UI component or page — name it specifically]
User action: [Exact action — click, change, drag — name the UI element and event type]
Expected outcome: [What the user expects to see]

---

## EVENT TRACE TABLE

Column instructions:

- **Event**: Number and name each event. Row 1 is the triggering user action. Async events (API
  response, timer callback) are separate rows — do not collapse with the sync event that triggered them.

- **Component path**: Components with directional arrows (→). At least two named components with a
  structural relationship must appear somewhere in the full table.

- **State mutation**: Key, owner, old→new shape. "None — [reason]" if no mutation at this event.

- **Re-renders (count × verdict)**: For each component that re-renders: write "[Nx — justified:
  reason]" or "[Nx per action — unnecessary: exact cause; fix: specific API or hook]." If no
  re-render: "0× — not in re-render path: [reason]." Neither "several components" nor a blank cell
  passes this column.

- **Side effects**: API call (method + path), timer, navigation, or storage write with mechanism.
  "None — confirmed synchronous" if none.

- **UI change**: Observable change after this event. "No change — [reason]" if none.

- **What this trace adds vs. ad-hoc** [N/A not allowed — fill every cell with one of:
  (a) "Invisible: [specific thing DevTools cannot show without additional setup — e.g.,
       'which component owns this re-render', 'whether selector returned new reference']."
  (b) "Observable: [specific tab — Network/Console/Elements/Profiler]. Exception — [specific
       structural reason why this row is fully transparent to DevTools without additional setup —
       e.g., 'this is a direct DOM mutation, visible in Elements tab; no subscriber chain to trace'].
       Exception requires justification — not just claiming it."
  A blank cell or "N/A" fails this column. Exception (b) must explain why this row is
  the exception, not the rule.]:

| Event | Component path | State mutation | Re-renders (count × verdict) | Side effects | UI change | What this trace adds vs. ad-hoc |
|-------|---------------|----------------|------------------------------|--------------|-----------|----------------------------------|
| 1 — [name] | [A → B] | [key: old→new, owner: X] | [1× — justified: reason] | [POST /path via useEffect] | [visible change] | [Invisible: which component subscriber owns this re-render is not visible in Elements without Profiler] |
| 2 — [name] | [path] | [None — reason] | [0× — not in path: reason] | [None — confirmed] | [No change — reason] | [Observable: Console shows the dispatch. Exception — dispatch events are visible; component-level consequences of the dispatch are not, making this a limited exception.] |
[Add one row per event. Minimum three rows. Async events are separate rows.]

---

## POST-ASYNC STATE

Required if any Side effects cell is not "None — confirmed."

Success path: [What the user sees when the async effect resolves successfully]
Error path: [What the user sees if it fails — or "No error state defined. See FINDINGS."]

What ad-hoc DevTools would NOT show for success: [e.g., which component triggered the post-success
  re-render, whether a sibling unnecessarily re-rendered on success]

If fully synchronous: "No async effect — action is synchronous."

---

## FINDINGS

Consolidate from the "What this trace adds vs. ad-hoc" column and POST-ASYNC STATE.
Each finding must cite its source row.

For each finding:
  Source: [Row N, "What this trace adds vs. ad-hoc" / POST-ASYNC STATE error path]
  Type: [Unnecessary re-render / Missing loading state / Error state gap / Accessibility failure]
  Severity: P1 / P2 / P3
  Problem: [Specific — component + exact issue]
  Fix: [Minimal, concrete — hook, boundary, or ARIA attribute]
  Do-nothing cost: [What ships to production without this fix]

If no findings: "No issues. All 'What this trace adds vs. ad-hoc' cells are (b) Observable exceptions —
verify each exception claim is substantive and that no issues were assumed away rather than confirmed clean."

---

## FRAMEWORK VOCABULARY CHECK

Confirm that all declared framework terms appeared in the EVENT TRACE TABLE.
- [Term 1]: row [N], column [name] — [exact phrase used]
- [Term 2]: row [N], column [name] — [exact phrase used]
- [Term 3]: row [N], column [name] — [exact phrase used]

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
events_traced, issues_count, framework_vocabulary_terms.
```

---

## V-03: Merged Count×Verdict Cell

**Axis:** Output format (re-render table structure) — count and verdict are collapsed into a single cell by template constraint. The column is called "Count × verdict" and its pre-printed format is: "Nx — justified: [reason]" or "Nx per action — unnecessary: [cause]; fix: [specific API]." Two columns in the same row still allow spatial scanning to separate them; one cell makes separation structurally impossible.

**Hypothesis:** C-10 was tightened because V-01's split layout (separate "Render count per action" column and "Unnecessary re-renders" subsection) satisfied "same row" technically but diluted the criterion — count and judgment were adjacent in the table but the reader had to match rows to the subsection below. A merged cell closes that gap: count and verdict are the same unit of output, written in the same moment. The model cannot write a count in one column and defer judgment to a later section — the template requires the judgment in the same cell as the count, at the same moment of writing.

```
You are running /trace:component. Fill in this structured template.
Complete the FRAMEWORK GATE before writing any trace content.

---

## FRAMEWORK GATE

Framework: [React / Vue / Angular / Svelte / other]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Role: [Auto-selected frontend expert — match the framework]

Framework vocabulary (3–5 terms that must appear in the trace below):
- [Term 1]: [one-clause definition]
- [Term 2]: [one-clause definition]
- [Term 3]: [one-clause definition]

[FRAMEWORK GATE: Do not begin SETUP until all fields above are filled.]

---

## SETUP

Surface: [UI component or page]
User action: [Exact action — name the element and event type]
Expected outcome: [What the user expects]

---

## EVENT CHAIN

Trace each event in the action sequence. Number them.

Event [N] — [Event type and origin]:
  Trigger: [What fired this event and from which component]
  Receiving component: [Named component — exact name, not "the button"]
  Handler: [Specific function name or lifecycle hook. If none: "No handler — bubbles to [parent]."]
  Propagation: [Where this event goes next — prop callback / context update / store dispatch / none]

[Repeat for each event. Include async events as separate entries with their trigger mechanism.
If an event has no handler, state that explicitly rather than omitting it.]

---

## COMPONENT TREE PATH

[EventReceivingComponent] (receives event from Event Chain above)
  ↓ [prop callback / context subscription / store dispatch]
[IntermediateComponent] (what it does with this)
  ↓ [relationship]
[ProviderOrRoot] (top of affected subtree)

If the path branches, trace each branch separately.

[Minimum: two named components with a directional relationship. A flat list without arrows does not
satisfy this section.]

---

## STATE MUTATION MAP

For each mutation this action triggers:

Mutation [N]:
  Owner: [Component or store — exact name matching the tree above]
  Key: [`stateKey` or `store.slice` — specific field name, not "the state"]
  Old: [Shape or value before — e.g., `false`, `[]`, `{id:null}`]
  New: [Shape or value after — e.g., `true`, `[{id:1}]`, `{id:"abc"}`]
  Mechanism: [useState setter / dispatch(action()) / store.$patch / this.setState]
  Timing: SYNC or ASYNC (after: [mechanism])

If no mutation: "No mutation — [read-only / presentational]. Justification: [why]."
["State updates" with no specifics does not satisfy this section.]

---

## RE-RENDER INVENTORY

For each component that re-renders because of the mutations above:

| Component | Re-render cause | Count × verdict |
|-----------|-----------------|-----------------|
| [Name] | [owns state X / subscribes to context Y / receives new prop Z] | [1× — justified: component owns the toggled boolean; re-render is required to show the updated value] |
| [Name] | [receives full formState prop from parent] | [3× per keystroke — unnecessary: receives the full formState object rather than the specific field it renders; fix: pass only isValid or wrap in React.memo with custom comparator] |
| [Name] | [reason] | [0× — not in re-render path: selector returns memoized reference; no prop changes reach this component] |
[Add one row per component in the re-render path. Minimum one row.]

Count × verdict format rules:
- Always include the number (or rate) AND the judgment in the same cell.
- "Justified" requires a specific structural reason — not just "re-render is expected."
- "Unnecessary" requires the exact cause AND a specific fix (hook name, API, or boundary).
- Separating count and verdict into two separate columns or into a subsection below the table does not
  satisfy this section — both must be in the same cell, in the same writing act.

---

## SIDE EFFECTS

| Effect | Mechanism | Trigger condition |
|--------|-----------|------------------|
| [API call: METHOD /endpoint] | [useEffect / thunk / saga] | [dependency or condition] |
| [Timer set/cleared] | [setTimeout / setInterval / cleanup] | [condition] |
| [Navigation] | [router.push / Link] | [condition] |
| [Storage write] | [direct / middleware] | [key and value shape] |
[If none: single row — "No side effects" | "N/A" | "Confirmed synchronous."]

---

## FINAL UI STATE

Synchronous state (after all SYNC mutations and re-renders complete):
[Visible elements, disabled states, loading indicators — name them specifically.
"UI updates accordingly" does not satisfy this section.]

Post-async state (if any side effect is async):
  Success: [What the user sees when it resolves]
  Error: [What the user sees if it fails — or "No error state defined. See FINDINGS."]
  If synchronous only: "No async settle point."

---

## FINDINGS

Check for:
- Count × verdict cells marked "unnecessary" — each needs a finding here
- Side effects with no loading state row between start and settle
- Side effects with no error path in Final UI State
- Components with missing ARIA, focus loss, or keyboard trap

For each finding: Severity (P1/P2/P3) / Component / Problem (specific) / Fix (specific API or attribute).
If no findings: "No issues. Justification: [per-check summary — name why each check came back clean]."

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
mutations_count, rerender_count, unnecessary_rerenders, issues_count.
```

---

## V-04: Wide Table Synthesis (C-07 + C-10)

**Axis (combined):** Output format — one wide event trace table carries both the "What this trace adds vs. ad-hoc" column (C-07/C-12: mandatory, cannot say N/A, escape pattern pre-printed in header) and a separate RE-RENDER DETAIL TABLE with co-located count×verdict cells (C-10); FRAMEWORK GATE handles C-08. The three R1 discriminators that no single variation won — C-07, C-08, C-10 — are each handled by a structural mechanism in the same template.

**Hypothesis:** R1's tradeoff was structural: V-05 won C-07 (inertia column) but dropped C-10 (no count column); V-04 won C-10 (same-row verdict) but only partially covered C-07; V-01 won C-08 (pre-declared vocabulary). The scorecard named the synthesis target explicitly: carry V-05's mandatory comparison column AND V-04's count+verdict columns. The table splits into two tables (event trace + re-render detail) to avoid an unwieldy 8-column row, but both criteria are handled by structural mechanisms rather than advisory sections.

```
You are running /trace:component. Fill in this pre-printed template.
Complete the FRAMEWORK GATE first. All column headers in the tables are fixed.
Fill every cell. Do not leave any cell blank.

---

## FRAMEWORK GATE

Framework: [React / Vue / Angular / Svelte / other]
Version (if determinable): [e.g., React 18.2 — or "not specified"]
State management: [useState / Redux / Zustand / Pinia / NgRx / other]
Rendering model: [Virtual DOM + reconciler / Signals-based / Zone.js / Svelte compiler / other]
Role: [Auto-selected frontend expert — match to framework]

Framework vocabulary in use (3–5 terms that MUST appear in the event table below):
- [Term 1]: [one-clause definition]
- [Term 2]: [one-clause definition]
- [Term 3]: [one-clause definition]

[FRAMEWORK GATE: Do not begin SETUP until every field above is filled. Framework terms declared here
must appear at least once in the EVENT TRACE TABLE rows below.]

---

## SETUP

Surface: [UI component or page — name it specifically]
User action: [Exact action — click, change, drag — name the UI element and event type]
Expected outcome: [What the user expects]

---

## EVENT TRACE TABLE

Column instructions:

- **Event**: Number and name each event. Row 1 is the triggering user action. Each async event
  (API response, timer callback) is a separate row — do not collapse with its triggering sync event.

- **Component path**: Components with direction (→). At least two named components with a structural
  relationship must appear somewhere in the full table.

- **State mutation**: Key, owner, old→new shape. "None — [reason]" if no mutation at this event.

- **Side effects**: API call (method + path), timer, navigation, or storage write with mechanism.
  "None — confirmed" if none.

- **UI change**: Observable change after this event. "No change — [reason]" if none.

- **What this trace adds vs. ad-hoc** [MANDATORY — N/A not allowed. Fill every cell.
  If something here is invisible to DevTools without additional setup: write
    "Invisible: [specific thing — e.g., 'which component owns this context subscription',
    'whether selector returned new reference vs same reference']."
  If everything in this row IS observable in DevTools without setup: write
    "Observable: [specific tab — Network/Console/Elements/Profiler]. Exception — [specific structural
    reason why this row is fully transparent without component-level tooling — e.g., 'this is a direct
    DOM event with no subscriber chain, visible in Elements tab']."
  A blank cell or "N/A" fails this column. The Exception case must explain why this row is
  the exception, not the rule.]:

| Event | Component path | State mutation | Side effects | UI change | What this trace adds vs. ad-hoc |
|-------|---------------|----------------|--------------|-----------|----------------------------------|
| 1 — [name] | [A → B] | [key: old→new, owner: X] | [POST /path via useEffect] | [visible change] | [Invisible: which subscriber in the context tree triggered this re-render is not observable in Elements or Network without Profiler] |
| 2 — [name] | [path] | [None — reason] | [None — confirmed] | [No change — reason] | [Observable: Console shows the dispatch. Exception — dispatch events are visible; component-level consequences of the dispatch are not, so this is a limited exception.] |
[Add one row per event. Minimum three rows. Async events are separate rows.]

---

## RE-RENDER DETAIL TABLE

For each component that re-renders as a result of the events above:

| Component | Re-render cause | Count × verdict |
|-----------|-----------------|-----------------|
| [Name] | [owns state X / subscribes to context Y / receives new prop Z] | [1× — justified: owns the toggled boolean; this re-render is required to show the updated UI] |
| [Name] | [receives full formState object from parent] | [3× per keystroke — unnecessary: receives full formState instead of the specific field it renders; fix: pass only the relevant prop or wrap in React.memo with custom comparator] |
| [Name] | [reason] | [0× — not in re-render path: selector returns memoized reference; no prop changes reach this component] |
[Minimum one row. Count × verdict must be in the same cell — count in one place and verdict in
another location does not satisfy this table.]

---

## POST-ASYNC STATE

Required if any Side effects cell in EVENT TRACE TABLE is not "None — confirmed."

Success path: [What the user sees when the async effect resolves]
Error path: [What the user sees if it fails — or "No error state defined. See FINDINGS."]
What ad-hoc DevTools would NOT show for success: [which component triggered the post-success
  re-render, whether siblings unnecessarily re-rendered on success]

If fully synchronous: "No async effect — action is synchronous."

---

## FINDINGS

Consolidate from EVENT TRACE TABLE "What this trace adds vs. ad-hoc" column and RE-RENDER DETAIL TABLE
"Count × verdict" cells marked "unnecessary." Each finding must cite its source.

For each finding:
  Source: [Event table row N / Re-render table row / POST-ASYNC STATE error path]
  Type: [Unnecessary re-render / Missing loading state / Error state gap / Accessibility failure]
  Severity: P1 / P2 / P3
  Problem: [Specific — component + exact issue, not "may have performance issues"]
  Fix: [Minimal, concrete — hook, boundary, or ARIA attribute]
  Do-nothing cost: [What ships to production without this fix]

If no findings: "No issues. Reference: all 'What this trace adds vs. ad-hoc' cells are Observable
exceptions AND all Count × verdict cells are justified. Verify each exception is substantive."

---

## FRAMEWORK VOCABULARY CHECK

Verify that the EVENT TRACE TABLE used all terms declared in the FRAMEWORK GATE.
- [Term 1]: row [N], column [name] — [exact phrase used]
- [Term 2]: row [N], column [name] — [exact phrase used]
- [Term 3]: row [N], column [name] — [exact phrase used]

If any declared term did not appear in the table, add a sentence here using it correctly and note
which row it should have appeared in.

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
events_traced, rerender_count, unnecessary_rerenders, issues_count, framework_vocabulary_terms.
```

---

## V-05: All Three Hard Criteria (C-10 + C-11 + C-12)

**Axis (combined):** Lifecycle emphasis + output format — gated phases where each gate names the exact failure phrase (C-11), Phase 4 re-render table uses merged count×verdict cells (C-10), and Phase 4 re-render table also carries the N/A-prohibited mandatory comparison column with escape pattern pre-printed in the column header (C-12). All three new or tightened aspirational criteria are addressed by structural mechanisms in a single template.

**Hypothesis:** V-04 R2 wins C-07 and C-10 together but has no exact-phrase gates (no C-11). V-01 R2 wins C-11 but has no mandatory comparison column (partial C-12). V-02 R2 wins C-12 but has no exact-phrase gates. No other variation targets all three simultaneously. The complexity stress test: does layering three enforcement mechanisms in one template remain coherent, or does Phase 4's density cause the model to abbreviate earlier phases? Predicted failure mode: Phase 4 becomes overly dense; the model spends most of its context budget on the re-render table and skims the event anchor and tree traversal phases.

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
Event payload: [Data in the event — e.g., value, id. If none: "No payload — void event."]
Handler: [Specific function name or lifecycle hook that receives this event.
  If none: "No handler on [ComponentName] — bubbles to [ParentComponent]."]

[PHASE 1 GATE: Writing "the button fires a click event" without naming the handler does not close
this phase. Writing "an event is triggered" without the event type and receiving component does not
close this phase. Handler must be a function name or lifecycle hook. Mark: PHASE 1 COMPLETE.]

---

## PHASE 2: COMPONENT TREE PATH

[EventReceivingComponent] (Phase 1 component)
  ↓ [prop callback / context subscription / store dispatch]
[IntermediateComponent] (what it does with this)
  ↓ [relationship]
[ProviderOrRoot] (top of affected subtree)

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
  Old: [Value or shape before — e.g., `false`, `[]`]
  New: [Value or shape after — e.g., `true`, `[{id:1}]`]
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

Column instructions:

- **Re-render cause**: Why does this component re-render? Name the mechanism (owns state X /
  subscribes to context Y / receives new prop Z from parent).

- **Count × verdict** [both pieces in this cell, in this writing act — co-location required]:
  - Justified: "1× — justified: [specific structural reason this component must re-render]"
  - Unnecessary: "3× per keystroke — unnecessary: [exact cause]; fix: [specific hook or API]"
  - No re-render: "0× — not in re-render path: [confirmed memoization or selector behavior]"
  - Count and verdict in separate columns or a separate section does not satisfy this column.

- **What this adds vs. ad-hoc** [N/A not allowed. Fill every cell.
  If invisible to DevTools without Profiler or source-stepping: write
    "Invisible: [specific thing — e.g., 'whether this component re-renders due to context value or
    prop change is not distinguishable in the DOM without component-level DevTools']."
  If fully observable in DevTools without additional setup: write
    "Observable: [specific tab]. Exception — [specific structural reason this row is transparent to
    ad-hoc inspection — e.g., 'this is a controlled input; its re-render is the DOM change, visible
    in Elements without component tooling']."
  Exception requires explanation — not just claiming it.]:

| Component | Re-render cause | Count × verdict | What this adds vs. ad-hoc |
|-----------|-----------------|-----------------|--------------------------|
| [Name] | [owns state X] | [1× — justified: owns the toggled boolean, re-render required] | [Invisible: whether this re-render is due to state ownership or prop propagation is not visible in Elements] |
| [Name] | [receives full formState prop] | [3× per keystroke — unnecessary: receives full formState instead of specific field; fix: wrap in React.memo and pass only isValid] | [Invisible: that this is unnecessary requires knowing the selector — DevTools shows re-render occurred but not whether it was required] |
[Minimum one row. Add rows for every re-rendering component.]

[PHASE 4 GATE: Writing "several components re-render" without naming them does not close this phase.
Writing count and verdict in separate columns or a separate subsection does not close this phase —
count × verdict must be in the same cell.
A "What this adds vs. ad-hoc" cell left blank or written as "N/A" does not close this phase.
Mark: PHASE 4 COMPLETE.]

---

## PHASE 5: SIDE EFFECTS AND FINAL UI STATE

**Side effects:**

Effect [N]:
  Type: [API call / timer / navigation / storage write / subscription]
  Detail: [endpoint+method / timer delay / route / storage key]
  Mechanism: [useEffect dependency / thunk / saga / Pinia action / router hook]

If none: "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation."

**Final UI state:**

Synchronous state (after all SYNC mutations and Phase 4 re-renders):
[Name elements: visible, hidden, disabled, loading, error. Be specific.]

Post-async state (if any side effect above is async):
  Success: [What the user sees when it resolves]
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
- Phase 4 "What this adds vs. ad-hoc" cells marked "Invisible" that surface a problem
- Phase 5 side effects without a loading state between start and settle
- Phase 5 error paths marked "No error state defined"
- Phase 2 components missing ARIA, losing focus, or creating keyboard trap

For each finding:
  Severity: P1 / P2 / P3
  Source: [Phase number + component or column]
  Problem: [Specific — "ButtonGroup re-renders 3× per keystroke because it receives the full
    formState object" not "may have performance issues"]
  Fix: [Minimal, concrete — specific hook, boundary, or ARIA attribute]

If no findings: "No issues across all five phases. Justification: [per-phase summary — specifically cite
Phase 4 count×verdict cells and ad-hoc column entries to confirm nothing was assumed away]."

---

Write artifact: simulations/trace/component/{topic}-component-{date}.md
Frontmatter: skill, topic, date, surface, user_action, framework, state_management,
phases_completed, mutations_count, rerender_count, unnecessary_rerenders, issues_count.
```
