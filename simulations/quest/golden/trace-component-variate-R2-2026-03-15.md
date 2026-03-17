# trace-component -- R2 Variations (v2 rubric)

**Round**: 2
**Rubric ceiling**: 110 pts (C-01 through C-11)
**Rubric file**: `simulations/quest/rubrics/trace-component-rubric-v2-2026-03-15.md`

**R1 baseline summary:**
- V-01 (Role Sequence): Prose format. Essential criteria covered (C-01/C-02/C-03/C-04 PASS). C-06/C-07 PARTIAL -- prose hid gaps. C-08/C-09 neutral. C-10/C-11 not in v1 rubric. ~Acceptable.
- V-02 (Output Format / Tables): Tables for event chain + re-render list. C-01/C-04 strong. C-06/C-07 improved. Reached Golden because tabular format made omissions structurally visible. ~Golden.
- V-03 (Lifecycle Phase Gates): Hard phase gates + MISSING-token protocol. C-03/C-04/C-05/C-07 strong via token-passing. Reached Golden because downstream phases consumed upstream tokens by reference. ~Golden.
- V-04 (Role Seq + Phrasing Register): Conversational expert voice. C-02/C-06/C-09 natural. Less structural enforcement. ~Acceptable.
- V-05 (Format + Lifecycle + Inertia): Naive-DOM baseline column in re-render table. C-06 strongest of all R1 variations. ~Golden.

**R2 variation axes chosen (3 single-axis + 2 combined):**
1. Role sequence -- Citation Auditor second role enforces C-11 by requiring all conclusions to cite upstream by identifier
2. Output format -- Tables ONLY for C-01 (event chain) and C-04 (re-render list), with mandatory row-citation protocol in downstream prose sections (C-10 + C-11 targeted together)
3. Lifecycle emphasis -- Phase registry pattern: each phase emits a named registry of identifiers (keys, component names, handler names) that downstream phases must open with explicit consumption citations (C-11 structural enforcement)
4. Combined: Output format + Lifecycle -- Tables (C-10) + phase registry + MISSING-token protocol (C-11)
5. Combined: Role sequence + Phrasing register -- Conversational expert with explicit citation rule: every downstream observation must name the upstream finding by its exact identifier or table row

**R2 variation map:**

| Variation | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Hypothesis |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Role sequence (Citation Auditor) | + | + | + | + | ~ | + | ~ | ~ | ~ | ~ | + | Second-role Citation Auditor required to cite upstream findings by exact identifier enforces C-11 without changing first-role output format |
| V-02 | Output format (targeted tables + row citation) | + | ~ | ~ | + | ~ | + | + | ~ | ~ | + | + | Tables only for C-01/C-04 (C-10 targeted); downstream prose required to cite table row numbers (C-11 targeted) |
| V-03 | Lifecycle emphasis (phase registry + consume protocol) | + | + | + | + | + | ~ | + | ~ | ~ | ~ | + | Each phase emits a named registry; downstream phases must open with explicit consumption citations from upstream registries (C-11 structural enforcement) |
| V-04 | Combined: Output format + Lifecycle | + | + | + | + | + | + | + | ~ | ~ | + | + | Tables for C-01/C-04 handle C-10; registry + consume protocol handle C-11; both new v2 criteria addressed by orthogonal mechanisms |
| V-05 | Combined: Role seq + Phrasing register | + | + | + | ~ | + | + | + | + | + | ~ | + | Conversational expert with mandatory citation-by-identifier rule; register elicits C-08/C-09 naturally; citation rule enforces C-11 |

Legend: + = axis targets this criterion, ~ = neutral

---

## V-01 -- Role Sequence: Citation Auditor

**Axis**: Role sequence
**Hypothesis**: A two-role structure where the first role (Domain Expert) produces the raw trace and the second role (Citation Auditor) is explicitly required to re-state every downstream conclusion by citing the upstream finding by its exact identifier -- state key name, component name, handler name -- enforces C-11 cross-section evidence chaining without imposing table format on the primary trace.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

---

### ROLE 1 -- Domain Expert Trace

Detect the frontend framework from the topic context (React, Vue, Svelte, Angular). Use that framework's exact vocabulary throughout. State your detection before beginning.

> Framework detected: ___

Produce the full trace in this order. Be exact: every handler, component, state key, and side effect must be named as it appears in the codebase, not described generically.

**Event Chain**
List every event handler that fires in response to `{{signal}}`, in causal order. For each handler: exact function name, exact owner component name, event type, propagation state (capture / target / bubble / stopped). If handler A dispatches to handler B, both must appear with the dispatch shown between them. No handler in the call chain may be omitted.

**Component Tree Traversal**
Trace the prop and callback path from the event-receiving component to the deepest component affected. For each handoff: from-component name, to-component name, direction (DOWN = prop to child / UP = callback to parent / CONTEXT = context consumer reads value), and the exact prop or callback name carrying the signal. No gaps in the path.

**State Delta**
Every state update triggered by `{{signal}}`: exact state key or slice name, value before, value after. Then identify any selectors, computed values, or memoized results that derive from a changed key -- list them with their own before/after values.

**Re-render List**
Every component that re-renders as a result of the state delta: component name, reason (prop change: which prop / context change: which context / selector subscription: which selector). Then every component that did NOT re-render: component name, reason (memo equality / selector equality / no subscription / not in subtree).

**Side Effects**
Every side effect triggered: name or endpoint, owner (component or middleware), timing (sync / deferred). For each async effect: state key set to loading at start, state key and value set on success, state key and value set on failure. If a loading state or error state is absent, note it -- mark it `MISSING-LOADING` or `MISSING-ERROR`.

**Issue Audit**
Evaluate all four categories:
1. Unnecessary re-renders: which re-rendered components produced no observable UI change?
2. Missing loading states: which async effects have no loading state coverage?
3. Error state gaps: which async effects have no error branch?
4. Accessibility failures: does the event chain cover keyboard input? Is focus managed after the action?

For each category: findings with component name + gap + remediation, or "no issues" with evidence from the trace.

**Optimization Notes** _(optional)_
Concrete optimization candidate: component name, optimization type (React.memo / useMemo / reselect / batch dispatch / render-scope reduction), expected render reduction.

**Final UI State**
Observable UI state after the trace settles: visible/hidden elements, displayed text or data, interactive states (disabled, focused, selected, loading, error). Derive directly from the State Delta.

---

### ROLE 2 -- Citation Auditor

Switch roles. You are now a Citation Auditor. Your job is not to re-run the trace -- it is to verify that the trace is internally consistent by requiring every downstream claim to be backed by an upstream identifier.

Work through each section of the Domain Expert trace and apply the following rule:

> **Citation rule**: Every finding in Side Effects, Issue Audit, and Final UI State must name at least one upstream identifier (a state key from State Delta, a component name from Re-render List or Component Tree, a handler name from Event Chain) as the source of that finding. Restating the same information without naming the upstream source is a gap -- flag it.

**Audit the Side Effects section:**
- For each loading state noted: which State Delta key does it correspond to? Name it.
- For each error state noted: which State Delta key does it correspond to? Name it.
- For each MISSING-LOADING or MISSING-ERROR: which async effect owns it? Name it.

**Audit the Issue Audit section:**
- Unnecessary re-renders: for each flagged component, cite its row in the Re-render List and the State Delta key that drove it.
- Missing loading states: cite the Side Effects entry that lacks the loading state.
- Error state gaps: cite the Side Effects entry that lacks the error branch.
- Accessibility failures: cite the Event Chain handler (or gap) that the finding derives from.
- "No issues" conclusions: cite the specific upstream section and identifier that supports the clean finding.

**Audit the Final UI State section:**
- For each element described in the Final UI State: name the exact State Delta key (from the State Delta section) whose after-value controls it.
- Any UI state element without a State Delta citation is unverifiable -- flag it.

**Derivation chain check:**
Confirm that the derivation chain is traceable: event handler (Event Chain) → state key change (State Delta) → component re-render (Re-render List) → observable UI element (Final UI State). Name the specific identifier at each link for at least one full chain end-to-end.

If all citations are present and the derivation chain is traceable, conclude:
> Audit passed. Full chain: [event handler] -> [state key] -> [re-rendering component] -> [UI element].

If citations are missing, list each gap:
> Citation gap: [section name] -- "[claim]" does not cite an upstream identifier.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-02 -- Output Format: Targeted Tables + Row Citation Protocol

**Axis**: Output format (tables for C-01 and C-04 only, with downstream row-citation protocol)
**Hypothesis**: Mandating table format specifically and only for the event chain (C-01) and re-render list (C-04) isolates the C-10 gap-visible requirement at the two sections with the highest omission risk. Prose sections (C-05 through C-07) are required to cite upstream tables by row number, enforcing C-11 cross-section evidence chaining without imposing tabular format everywhere.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

**Role**: Frontend domain expert. Detect the framework from the topic context. State your detection. Use framework vocabulary throughout.

> Framework detected: ___

---

### Event Chain Table

Mandatory table. One row per handler. Every handler in the call chain must have a row -- no handler may be described in prose and omitted from this table. If you do not know a handler's exact name, write `UNKNOWN` in that cell rather than skipping the row.

| Row | Handler Name | Owner Component | Event Type | Sync/Async | Propagation | Dispatches To |
|-----|-------------|----------------|-----------|-----------|-------------|--------------|
| EC-1 | | | | | | |
| EC-2 | | | | | | |

_Propagation_: `capture` / `target` / `bubble` / `stopped` / `delegated:{owner}`
_Dispatches To_: next handler row (e.g., `EC-2`) or `TERMINAL` if the chain ends here

Complete this table before writing any other section.

---

### Component Tree Traversal

Prose. Starting from the component in EC-1 that owns the first handler, trace the prop/callback path to the deepest component affected.

For each handoff: from-component name, to-component name, direction (DOWN / UP / CONTEXT), and the exact prop or callback name. No gaps in the path.

---

### State Delta

Prose with inline enumeration. For each state update:
- Exact state key or slice name
- Value before
- Value after

Then list any derived state (selectors, computed values, memoized results) that depend on a changed key, with their own before/after values.

---

### Re-render List Table

Mandatory table. Every component in the affected subtree gets a row -- both components that re-rendered and components that did not. A component omitted from this table is a structural gap.

| Row | Component Name | Re-rendered? | Reason | Memo in Place? | Memo Type |
|-----|---------------|-------------|--------|---------------|-----------|
| RR-1 | | YES/NO | | YES/NO | |
| RR-2 | | YES/NO | | YES/NO | |

_Reason (YES)_: `prop:{prop name}` / `context:{context name}` / `selector:{selector name}`
_Reason (NO)_: `memo equality` / `selector equality` / `no subscription` / `not in subtree`

Complete this table before writing Side Effects.

---

### Side Effects

Prose. For each side effect triggered:
- Name or endpoint
- Owner: component name or middleware name
- Timing: `sync` (runs in handler body) or `deferred` (useEffect, watchEffect, nextTick, etc.)
- Loading state: state key and value set when the effect starts -- or write `MISSING-LOADING` if absent
- Success state: state key and value set on completion
- Error state: state key and value set on failure -- or write `MISSING-ERROR` if absent

**Citation requirement**: When naming the owner component, cite its row in the Re-render List Table (e.g., "owned by `CheckoutButton` [RR-3]"). When naming a state key that corresponds to a row in the State Delta, reference it by name.

---

### Issue Audit

Prose. Evaluate all four categories.

**Citation requirement**: Every finding must cite at least one upstream table row by its row identifier (EC-n or RR-n) or a named State Delta key. A finding without a citation is unverifiable.

**1. Unnecessary re-renders**
For each YES row in the Re-render List Table: did the re-render produce an observable UI change? If not, cite the row (RR-n), explain why it was unnecessary, suggest a remedy.

**2. Missing loading states**
For each `MISSING-LOADING` in Side Effects: name the effect, describe the user-visible gap, suggest the loading state. If none: cite the Side Effects entry that confirms coverage.

**3. Error state gaps**
For each `MISSING-ERROR` in Side Effects: name the effect, describe the failure mode, suggest the error state. If none: cite the Side Effects entry.

**4. Accessibility failures**
Review the Event Chain Table. Does any EC row cover keyboard events (keydown / Enter / Space) as well as pointer events? If not, name the missing row. Check focus management and screen reader state. Cite specific EC or RR rows in each finding or clean conclusion.

---

### Final UI State

Prose. Observable end state after the trace settles.

**Citation requirement**: Every element described here must be derived from a named State Delta key. State the key by name in parentheses after each element (e.g., "The submit button is disabled (`isSubmitting: true`)"). UI state not traceable to a State Delta key must not appear here.

---

### Optimization Notes _(optional -- aspirational)_

If the Re-render List Table contains YES rows that appear unnecessary (component re-rendered but no observable output change), name the component (cite RR-n), the optimization, and the expected render reduction.

---

### Framework Notes _(optional -- aspirational)_

Framework-specific mechanics that shaped this trace. Core trace above uses framework-neutral vocabulary; this section isolates framework idioms.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-03 -- Lifecycle Emphasis: Phase Registry + Consume Protocol

**Axis**: Lifecycle emphasis (phase registry pattern with mandatory consumption citations)
**Hypothesis**: Each phase emits a named "registry" section -- a compact list of the identifiers it produced (handler names, component names, state keys) -- and each downstream phase must open with an explicit "Consuming from Phase N" section that cites the upstream identifiers by name. This registry-and-consume pattern enforces C-11 cross-section evidence chaining structurally, without imposing table format, by making the citation requirement a phase entry condition rather than an audit concern.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

**Role**: Frontend domain expert. Detect framework from topic context. State your detection. Use framework vocabulary throughout.

> Framework detected: ___

---

Complete each phase in order. Each phase has three parts: **Body** (the trace content), **Registry** (identifiers this phase produced), and where indicated, **Consuming from Phase N** (identifiers this phase receives from upstream). Do not begin the next phase until the current phase's completion criterion is met.

---

### PHASE 1 -- Event Chain Reconstruction

**Completion criterion**: Every handler in the call chain is listed in causal order with name, owner, and event type. Zero entries may be implicit. UNKNOWN is permitted; omission is not.

**Body**:
List every event handler that fires in response to `{{signal}}`, in the exact order they fire. For each: exact handler name, exact owner component name, event type (synthetic vs native), propagation state (capture / target / bubble / stopped). If handler A dispatches to handler B, show the dispatch explicitly between the two entries.

**Phase 1 Registry** (emit before proceeding to Phase 2):
```
Handlers: [list handler names]
Owner components: [list component names that own handlers]
Event types: [list event types observed]
```

---

### PHASE 2 -- Component Tree Traversal

**Consuming from Phase 1**:
```
Starting component: [first owner component from Phase 1 Registry]
```

**Completion criterion**: Unbroken path from the Phase 1 starting component to the deepest affected component. Every intermediate component named. Every prop and callback named with direction.

**Body**:
Starting from the component identified in "Consuming from Phase 1", trace the prop/callback path. For each handoff: from-component, to-component, direction (DOWN = prop to child / UP = callback to parent / CONTEXT = context read), exact prop or callback name. Note any context provider/consumer pairs.

**Phase 2 Registry** (emit before proceeding to Phase 3):
```
Component path: [ordered list of all component names in the traversal]
Props/callbacks: [list of prop and callback names that carried signals]
Leaf component: [deepest affected component]
```

---

### PHASE 3 -- State Delta Mapping

**Consuming from Phase 2**:
```
State-owning components: [subset of Phase 2 component path that own state]
```

**Completion criterion**: Every state key or slice updated by the action has a named before and after value. Every derived value (selector, computed, memoized) that depends on a changed key has its own row.

**Body**:
For each primary state update: exact state key or slice name, value before, value after.
For each derived value that depends on a changed key: derived name, before, after, which primary key it derives from.

**Phase 3 Registry** (emit before proceeding to Phase 4):
```
State keys changed: [list all primary state key names]
Derived values changed: [list all derived value names, each with parent key]
State-owning components: [components from Phase 2 that own these keys]
```

---

### PHASE 4 -- Re-render Analysis

**Consuming from Phase 3**:
```
Keys that changed: [from Phase 3 Registry: state keys changed]
Components in traversal: [from Phase 2 Registry: component path]
```

**Completion criterion**: Every component in the Phase 2 component path appears in the re-render list (either re-rendered or explicitly not). Every re-render has a named reason citing a Phase 3 key or a Phase 2 prop. Every non-re-render has a named reason.

**Body**:
For each component in the Phase 2 component path:

**Re-rendered** components: component name, reason -- `prop change: [prop name from Phase 2 Registry]` or `context change: [context name]` or `selector subscription: [selector name from Phase 3 Registry]`.

**Not re-rendered** components: component name, reason -- `memo equality` / `selector equality` / `no subscription`. If selector equality: name the selector from Phase 3 Registry and confirm its output did not change.

**Phase 4 Registry** (emit before proceeding to Phase 5):
```
Re-rendered components: [list]
Skipped components (with reason): [list]
Props that triggered re-renders: [list from Phase 2 Registry]
Keys that triggered re-renders: [list from Phase 3 Registry]
```

---

### PHASE 5 -- Side Effects and Async Paths

**Consuming from Phase 4**:
```
Components that re-rendered: [from Phase 4 Registry: re-rendered components]
```

**Completion criterion**: Every side effect triggered by the action is named with owner and timing. Every async effect has three-state accounting. Missing states are named as MISSING-LOADING or MISSING-ERROR tokens -- they are findings for Phase 6, not omissions.

**Body**:
For each side effect triggered:
- Name or endpoint
- Owner: component name (cite from Phase 4 Registry if it re-rendered) or middleware name
- Timing: sync (in handler body) or deferred (useEffect, watchEffect, nextTick, etc.)
- Loading state: `[state key from Phase 3 Registry]: [value]` -- or `MISSING-LOADING`
- Success state: `[state key from Phase 3 Registry]: [value]`
- Error state: `[state key from Phase 3 Registry]: [value]` -- or `MISSING-ERROR`

**Phase 5 Registry** (emit before proceeding to Phase 6):
```
Side effects: [list effect names/endpoints]
Effect owners: [component or middleware names]
MISSING-LOADING tokens: [effect names with absent loading state, or NONE]
MISSING-ERROR tokens: [effect names with absent error state, or NONE]
```

---

### PHASE 6 -- Issue Audit

**Consuming from Phase 4 + Phase 5**:
```
Unnecessary re-render candidates: [Phase 4 Registry re-rendered components -- assess each]
MISSING-LOADING: [from Phase 5 Registry]
MISSING-ERROR: [from Phase 5 Registry]
```

**Completion criterion**: All four issue categories evaluated with explicit upstream citations. Every "no issues" conclusion cites the specific Phase registry entry that supports it.

**Body**:

**1. Unnecessary re-renders**
For each component in "Consuming from Phase 4 -- re-rendered components": did it produce an observable UI change? If a component re-rendered but its output did not change, name it, cite the Phase 4 Registry entry, explain why the re-render was triggered, suggest a remedy (React.memo / useMemo / smaller component boundary / selector / batch).
No issues: cite the Phase 4 Registry entries that confirm all re-renders were necessary.

**2. Missing loading states**
For each `MISSING-LOADING` token from Phase 5 Registry: describe the user-visible gap, suggest the missing state key and value.
No issues: cite Phase 5 Registry "MISSING-LOADING tokens: NONE" and the effect entry that confirms coverage.

**3. Error state gaps**
For each `MISSING-ERROR` token from Phase 5 Registry: describe the failure mode, suggest the missing state key and value.
No issues: cite Phase 5 Registry "MISSING-ERROR tokens: NONE".

**4. Accessibility failures**
Consuming from Phase 1: does the handler list include keyboard event handlers (keydown / Enter / Space) as well as pointer events? If not, name the missing handler.
Consuming from Phase 2: after the action, does the component path include any focus management operation?
Consuming from Phase 3: does any changed state key correspond to an aria-live region or role attribute?
For each gap: name the missing handler, component, or state key. For "no issues": cite the Phase 1/2/3 Registry entries.

**Phase 6 Registry** (emit before proceeding to Phase 7):
```
Issues found: [list of issue type + component name pairs, or NONE]
Accessibility gaps: [list, or NONE]
```

---

### PHASE 7 -- Final UI State Snapshot

**Consuming from Phase 3 + Phase 6**:
```
State keys changed (after values): [from Phase 3 Registry: state keys changed]
Issues found: [from Phase 6 Registry]
```

**Completion criterion**: Every UI element described here derives from a Phase 3 state key. No UI state may appear that was not established in Phase 3.

**Body**:
Describe the observable UI state after the trace settles:
- Visible / hidden elements: derive from which Phase 3 key controls visibility -- cite the key by name
- Text or data displayed: cite the Phase 3 after-value that populates the element
- Interactive states (disabled, focused, selected, loading, error): cite the Phase 3 after-value
- Any unresolved issues from Phase 6 that affect visible state: name the issue and the affected element

For each statement: "The [element] is [state] because [Phase 3 key] changed from [before] to [after]."

---

### PHASE 8 -- Optimization Notes _(optional -- aspirational)_

**Consuming from Phase 4**:
```
Re-rendered components: [Phase 4 Registry -- assess for avoidable renders]
```

If Phase 4 identified re-rendered components where the output did not change:
- Component name (cite Phase 4 Registry)
- Optimization: `React.memo` / `useMemo:{dependencies}` / `reselect selector` / `batch dispatch` / `render-scope reduction`
- Expected effect: quantify the render reduction

Skip if Phase 4 Registry shows no unnecessary renders.

---

### Framework Notes _(optional -- aspirational)_

Framework-specific mechanics that shaped the trace. Core trace uses framework-neutral vocabulary; this section isolates framework idioms.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-04 -- Combined: Output Format + Lifecycle Emphasis

**Axes**: Output format (targeted tables for C-10) + Lifecycle emphasis (phase registry + consume protocol for C-11)
**Hypothesis**: Tables for C-01 (event chain) and C-04 (re-render list) satisfy C-10 by making gaps structurally visible. Phase registry + consume protocol satisfies C-11 by making citation a structural entry requirement for each downstream phase. The two mechanisms address the two new v2 criteria through orthogonal structural devices -- neither mechanism depends on the other, so both can pass or fail independently.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

**Role**: Frontend domain expert. Detect framework from topic context. State your detection. Use framework vocabulary throughout.

> Framework detected: ___

---

Complete each phase in order. Phases 1 and 4 use mandatory tables; other phases use prose with explicit registry and consume headers. Do not begin a phase until the previous phase's completion criterion is met.

---

### PHASE 1 -- Event Chain Table

**Completion criterion**: Every handler in the call chain occupies a table row. No handler is described in prose and omitted from this table. UNKNOWN is acceptable; omission is not.

Mandatory table:

| Row | Handler Name | Owner Component | Event Type | Sync/Async | Propagation | Dispatches To |
|-----|-------------|----------------|-----------|-----------|-------------|--------------|
| EC-1 | | | | | | |

_Dispatches To_: next row identifier (EC-n) or `TERMINAL`

**Phase 1 Registry** (emit before proceeding to Phase 2):
```
Handler rows: [EC-1 through EC-n, with handler name]
Owner components: [list]
```

---

### PHASE 2 -- Component Tree Traversal

**Consuming from Phase 1**:
```
Starting component: [EC-1 owner from Phase 1 Registry]
```

Prose. Trace from the Phase 1 starting component to the deepest component affected. For each handoff: from-component, to-component, direction (DOWN / UP / CONTEXT), exact prop or callback name. No gaps.

**Phase 2 Registry** (emit before proceeding to Phase 3):
```
Component path: [ordered list]
Signal carriers: [prop and callback names]
Leaf component: [deepest affected]
```

---

### PHASE 3 -- State Delta

**Consuming from Phase 2**:
```
State-owning components: [from Phase 2 component path that own state]
```

Prose with enumeration. For each primary state update: exact key or slice, before, after. For each derived value: name, before, after, parent key.

**Phase 3 Registry** (emit before proceeding to Phase 4):
```
Primary keys changed: [list with before/after]
Derived values changed: [list with parent key]
```

---

### PHASE 4 -- Re-render List Table

**Consuming from Phase 3**:
```
Keys that changed: [from Phase 3 Registry: primary keys changed]
Components to evaluate: [from Phase 2 Registry: component path]
```

**Completion criterion**: Every component in the Phase 2 component path has a table row -- both re-rendered and not-re-rendered components. Every YES row cites the Phase 3 key or Phase 2 signal carrier that triggered it. Every NO row names the memoization or non-subscription reason.

Mandatory table:

| Row | Component Name | Re-rendered? | Reason (cite Phase 2/3 identifier) | Memo in Place? | Memo Type |
|-----|---------------|-------------|-------------------------------------|---------------|-----------|
| RR-1 | | YES/NO | | YES/NO | |

_Reason (YES)_: `prop:[name from Phase 2 Registry]` / `context:[name]` / `selector:[name from Phase 3 Registry]`
_Reason (NO)_: `memo equality` / `selector equality (key: [Phase 3 key])` / `no subscription`

**Phase 4 Registry** (emit before proceeding to Phase 5):
```
Re-rendered: [RR-n rows with component name]
Skipped: [RR-n rows with component name and reason]
Keys that drove re-renders: [Phase 3 keys referenced in YES rows]
```

---

### PHASE 5 -- Side Effects

**Consuming from Phase 4**:
```
Re-rendered components: [from Phase 4 Registry]
```

Prose. For each side effect: name/endpoint, owner (cite RR-n if in table, or middleware name), timing (sync / deferred).

For each async effect:
- Loading: `[Phase 3 key]: [value]` or `MISSING-LOADING`
- Success: `[Phase 3 key]: [value]`
- Error: `[Phase 3 key]: [value]` or `MISSING-ERROR`

**Phase 5 Registry**:
```
Effects: [list]
MISSING-LOADING: [effect names, or NONE]
MISSING-ERROR: [effect names, or NONE]
```

---

### PHASE 6 -- Issue Audit

**Consuming from Phase 4 + Phase 5**:
```
Re-rendered components (for unnecessary re-render check): [Phase 4 Registry: re-rendered]
MISSING-LOADING: [Phase 5 Registry]
MISSING-ERROR: [Phase 5 Registry]
```

Prose. Evaluate all four categories. Every finding cites an upstream row identifier (EC-n, RR-n) or a Phase 3 state key. Every "no issues" conclusion cites the specific registry entry that supports it.

**1. Unnecessary re-renders**: For each YES row in Phase 4 table -- did the re-render produce an observable UI change? Flag and remediate if not. Cite the RR-n row.

**2. Missing loading states**: For each MISSING-LOADING in Phase 5 Registry -- describe the user-visible gap, suggest the state. If NONE: cite Phase 5 Registry.

**3. Error state gaps**: For each MISSING-ERROR in Phase 5 Registry -- describe the failure mode. If NONE: cite Phase 5 Registry.

**4. Accessibility failures**: Consuming Phase 1 handler rows -- keyboard events covered? Consuming Phase 2 path -- focus management? Consuming Phase 3 keys -- aria-live triggered? Cite EC-n or RR-n rows.

---

### PHASE 7 -- Final UI State

**Consuming from Phase 3**:
```
Primary keys after-values: [from Phase 3 Registry]
```

Prose. For each UI element described: cite the Phase 3 state key by name that controls it. Format: "The [element] is [state] because `[Phase 3 key]` is now `[after value]`." No UI state may appear that is not established in Phase 3 Registry.

---

### PHASE 8 -- Optimization Notes _(optional -- aspirational)_

**Consuming from Phase 4**:
```
YES rows in re-render table: [Phase 4 Registry: re-rendered]
```

If any Phase 4 YES row appears unnecessary: component name (cite RR-n), optimization, expected render reduction. Skip if none.

---

### Framework Notes _(optional -- aspirational)_

Framework-specific mechanics in isolation. Core trace uses framework-neutral vocabulary.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`

---

## V-05 -- Combined: Role Sequence + Phrasing Register

**Axes**: Role sequence + Phrasing register (conversational expert with mandatory citation-by-identifier rule)
**Hypothesis**: A conversational expert walkthrough elicits C-08 (optimization notes) and C-09 (framework-portable annotations) more naturally than formal imperative -- experts explain their reasoning rather than just listing outputs. Adding an explicit "citation rule" that the expert must follow throughout -- every downstream observation must name an upstream identifier by its exact term -- enforces C-11 evidence chaining within the conversational register. This tests whether natural-language citation constraint is sufficient for C-11, or whether structural mechanisms (tables, phase gates) are required.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- User action (signal): `{{signal}}`

---

### Who You Are

Look at the topic context and identify the frontend framework. Then step into the role of a senior engineer who has shipped production apps in that specific framework -- not a generic "frontend developer" but someone whose instincts run deep in that runtime.

- **React developer**: You think about fiber, the reconciler, which hooks fire in which commit phase, what React.memo actually saves in this case, and why batching matters here.
- **Vue 3 developer**: You think about the reactive proxy, when watchers flush, how the template compiler transforms this particular template, and what a shallow vs deep reactive buys you.
- **Svelte developer**: You think about what the compiler emits for this component, when `$:` blocks invalidate, what the store contract guarantees, and how derived differs from a memoized function.
- **Angular developer**: You think about zones, which change detection strategy is active on which component, how the injector resolves this specific service, and when async pipe unsubscribes.

If no framework is detectable, default to React and say so.

Open with: *"I am a [Framework] Senior Engineer. Let me walk through what happens when `{{signal}}` fires in `{{topic}}`."*

---

### Citation Rule

This is the most important constraint in this prompt. Follow it throughout the walkthrough:

> **Every time you make a claim in a downstream section that depends on an upstream finding, you must name the upstream finding by its exact identifier -- the exact state key name, the exact component name, or the exact handler name you established earlier.**

Concretely:
- When you say a component re-renders, name the state key (established in your State Delta section) that triggered it.
- When you say the final UI shows some state, name the state key (established in your State Delta section) whose after-value controls it.
- When you say an issue exists, name the upstream handler or component (established in your Event Chain or Re-render section) where the gap lives.
- "It updates the state" fails the citation rule. "`isLoading` changes from `false` to `true`" passes.

If at any point you catch yourself making a claim without naming an upstream identifier, stop and add the citation before continuing.

---

### Walk Through the Action

**What fires first?**

Walk through every event handler that responds to `{{signal}}`, in order. Think about event propagation -- does anything catch it in a parent first? Is there delegation? Name each handler by its exact function name and say which component owns it. Name the event type (is it a React synthetic event, a native DOM event, a Vue emit?).

Think out loud about the propagation path. Where does the event start, where does it bubble, where does it stop?

---

**Where does the call travel?**

Follow the signal from the first handler into the component tree. Which component does it reach first? What does that component do with it -- does it call a prop callback upward? Set local state? Dispatch to a store? Where does the call go next?

Name every component you pass through. Name every prop and every callback. Say whether you're going DOWN into a child (via a prop) or UP toward a parent (via a callback). "The data flows up" is not enough -- say the parent name and the callback name.

---

**What state actually changes?**

When the action is processed, what state is different? Walk through each change:
- Exact state key or slice name
- The value it held before
- The value it holds now

Are there selectors, computed values, or memoized results that derive from any of those keys? They changed too -- name them with their own before/after.

---

**Who re-renders -- and who doesn't?**

Think through who is subscribed to the state you named. Which components re-render because of the changes you just described? For each one, name the exact state key or prop name that drove the re-render -- cite it by the identifier you established in your State Delta.

Now think about who has insulation. Which components have React.memo, a Pinia getter, a reselect selector, v-memo? Name them and say what kept them from re-rendering. If a selector held equality, name the selector and say its output stayed the same.

---

**What's happening in the background?**

Any side effects? An API call, a subscription update, a timer, a storage write? Name each one and say who owns it. Does it fire immediately in the handler, or does it schedule for later?

For each async effect, walk all three branches:
- What state key does it set when it starts (the loading signal)?
- What state key does it set when it comes back (success)?
- What does it set when it fails (error)?

**Citation rule applies here**: name the state keys from your State Delta section. If the loading state or error state key does not appear in your State Delta, that is a gap -- note it.

---

**Anything feel off?**

Step back and audit with your senior-engineer instincts. For each category, tell me what you see:

*Unnecessary re-renders* -- Look at the components you said re-rendered. Any of them re-render without producing an observable UI change? Name the component (use the exact name you established in the re-render section), describe what triggered it (cite the state key), and suggest a fix.

*Missing loading states* -- Every async effect you named -- is there a loading state covering it? If not, name the effect and the missing state key.

*Error state gaps* -- If the async call fails, does the UI show something? Name the effect and the missing state key if not.

*Accessibility* -- When the user does `{{signal}}` with a keyboard, does the event chain still fire? After the action, where does focus go? Is there a screen reader announcement for any dynamic content that changed? Cite the specific handler names or component names where gaps exist.

For "no issues": cite the exact handler name, component name, or state key that confirms the category is covered. An uncited "no issues" is not a valid conclusion.

---

**What does the user see at the end?**

After everything settles, describe the actual visible UI state. What's on screen, what's hidden, what does the data say?

**Citation rule applies here especially strongly**: for every UI element you describe, name the state key from your State Delta whose after-value controls it. Format it naturally: "The submit button is disabled because `isSubmitting` is now `true`." Do not describe a UI state that you haven't traced to a state key.

---

**Any quick wins?** _(optional -- aspirational)_

If you noticed a component re-rendering unnecessarily, or a state update that could be batched, name it. Use your expert knowledge: what specific optimization applies here (React.memo, useMemo with these specific dependencies, a reselect selector, a batch dispatch)? How many re-renders would that eliminate per action?

---

**Framework Notes** _(optional -- aspirational)_

After the trace, a brief "Framework Notes" section: where did the framework's specific mechanics (fiber scheduler, reactive proxy, zone.js, compiler output) shape the trace in ways that would look different in another framework? This keeps the core trace readable for someone who knows components but doesn't know `{{framework}}` internals.

---

Write the completed artifact to: `simulations/trace/component/{{topic}}-component-{{date}}.md`
