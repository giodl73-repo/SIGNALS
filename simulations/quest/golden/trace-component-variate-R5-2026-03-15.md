# trace-component — R5 Variations (v5 rubric)

**Round**: 5
**Rubric ceiling**: 140 pts (C-01 through C-17)
**Rubric file**: `simulations/quest/rubrics/trace-component-rubric-v5-2026-03-15.md`

**R4 baseline summary:**
- V-01 (Role Sequence / Vocabulary Contract blocking gate): 123/130 GOLDEN. Gaps: C-08 absent (no optimization section); C-11 partial (only §7→§3 citation mandated; §4/§5/§6 upstream citations not required).
- V-02 (Output Format / Format Contract): 83/130 MARGINAL. Gaps: C-05 partial (no token protocol); C-06 partial; C-07 partial; C-08/C-11/C-12/C-13/C-14/C-15 all absent.
- V-03–V-05: not defined in R4.

**New v5 criteria:**
- C-16: Vocabulary contract PASS-THROUGH designation (depends on C-14)
- C-17: Completeness stamp with active mismatch correction (depends on C-15)

**R5 variation axes chosen (3 single-axis + 2 combined):**
1. Role sequence — extend R4 V-01 with PASS-THROUGH column (C-16), explicit optimization section (C-08), full §4/§5/§6 citation requirements (C-11), and active correction protocol in stamp (C-17)
2. Output format — extend R4 V-02 with prepended vocabulary contract block (C-14/C-16), token rows in all tables (C-12), citation column in §4–§7 (C-11), optimization table (C-08), completeness stamp with correction (C-15/C-17)
3. Lifecycle emphasis — phase-gated trace with dedicated Optimization Phase (C-08) and registry-consume opening protocol per phase (C-11); vocabulary contract absent
4. Phrasing register — imperative per-criterion checklist; each v5 criterion's pass condition stated as a direct instruction; no role machinery
5. Combined: Role sequence + Lifecycle emphasis — three-role pipeline: Contract Author (PASS-THROUGH vocabulary contract) → Phase-gated Trace Author (7 phases, registry-consume, optimization phase) → Active Auditor (correction protocol + leak scan + evidence chain audit)

**R5 variation map:**

| Variation | Axis | C-08 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | Hypothesis |
|-----------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Role sequence | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Targeted additions to R4 V-01 close both known gaps without restructuring the blocking-gate pattern |
| V-02 | Output format | PASS | PASS | PASS | PARTIAL | PASS | PASS | PASS | PASS | Vocabulary contract prepended to format contract elevates R4 V-02 from Marginal; C-13 partial because format-contract mechanism cannot fully enforce neutral vocabulary in all cells |
| V-03 | Lifecycle emphasis | PASS | PASS | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | Phase gates + optimization phase target C-08/C-11/C-12; vocabulary/stamp criteria absent without contract block |
| V-04 | Phrasing register | PASS | PASS | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | Imperative instructions can enforce C-08/C-11/C-12 by direct mandate; C-14/C-16/C-17 require structural artifacts that a flat prompt cannot produce |
| V-05 | Combined: Role seq + Lifecycle | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | All three structural mechanisms in one pipeline: vocabulary integrity (C-13/C-14/C-16), phase completeness (C-08/C-11/C-12), and active audit (C-15/C-17) |

Legend: PASS = mechanism directly targets and likely satisfies the criterion, PARTIAL = partially satisfied, FAIL = criterion not addressed

---

## V-01 — Role Sequence: PASS-THROUGH Vocabulary Contract + Targeted Gap Fixes

**Axis**: Role sequence
**Hypothesis**: R4 V-01 scored 123/130 with two identified gaps: C-08 absent (no optimization section existed) and C-11 partial (only §7→§3 citation was mandated; §4/§5/§6 were not required to cite upstream). Three targeted additions close both gaps without restructuring the successful blocking-gate pattern: (a) PASS-THROUGH column added to the vocabulary contract table (C-16 — declares codebase proper names explicitly rather than implying them through presence); (b) a mandatory §8 Optimizations section added to Role 2 with a quantified render-reduction requirement (C-08); (c) §4, §5, and §6 each given an explicit citation requirement to name the upstream §1–§3 row they derive from (C-11 fully satisfied across ≥ 3 downstream sections). Role 3 extends the completeness stamp with active mismatch correction notation (C-17). Expected ceiling: 138–140/140.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role in full before beginning the next. No role may produce trace content, schema drafts, or structural scaffolding for a downstream role. Role output is visible to subsequent roles.

---

### ROLE 1 — Contract Author

Your sole output is the Vocabulary Contract. No trace content, section outlines, or structural hints appear in this role.

#### §0 Vocabulary Contract

Produce a four-column table mapping every framework-specific term that will appear in this trace:

| Framework Term | Neutral Equivalent | Disposition | Notes |
|---------------|-------------------|-------------|-------|

**Column definitions:**

**Framework Term** — The term as it appears in the framework (e.g., `useState`, `useEffect`, `v-model`, `watchEffect`, `@Input()`, `ChangeDetectionStrategy`, `$store`).

**Neutral Equivalent** — The framework-neutral term used in §1–§7 core sections (e.g., `local state hook` for `useState`, `side-effect hook` for `useEffect`, `two-way binding directive` for `v-model`). For PASS-THROUGH entries, repeat the codebase name unchanged.

**Disposition** — One of two values:
- **MAP** — Framework primitive. Use the Neutral Equivalent in §1–§7. The Framework Term appears only in §9 (Framework Notes).
- **PASS-THROUGH** — Codebase proper name: a component name, handler function name, selector name, store slice name, or any identifier that must appear unchanged in the trace to remain navigable in the source. Use the name exactly as declared in this column across §1–§7. Do not invent a neutral alias.

**Notes** — Optional. State why a codebase identifier is PASS-THROUGH (e.g., "component name in source", "store slice key", "event handler exported from module").

**Rules:**
1. Every framework-specific term that will appear in §1–§7 must have a row.
2. The PASS-THROUGH designation is a mandatory named column — omitting it is a contract failure. A vocabulary contract without a declared PASS-THROUGH section does not satisfy C-16.
3. Framework primitives (`useState`, `useEffect`, `v-model`, `@Input()`, etc.) are MAP by default.
4. Codebase identifiers (component names, handler names, store slices) are PASS-THROUGH by default.
5. If a term is both a framework primitive and a codebase-defined name (e.g., a custom hook named after a framework API), default to PASS-THROUGH and note the conflict.

**Do not produce any §1–§9 content until this table is complete.**

---

### ROLE 2 — Trace Author

You receive the §0 Vocabulary Contract from Role 1. Produce §1–§9 in full, in order.

**Binding constraint**: In §1–§7, use only the Neutral Equivalent for every MAP term and the exact codebase name for every PASS-THROUGH term. Any MAP term appearing in §1–§7 outside §9 is a vocabulary violation. Any PASS-THROUGH term appearing as a neutral alias (e.g., aliasing `useProductStore` to `StateManager`) is a contract violation.

#### §1 Event Chain

| Step | Handler (exact PASS-THROUGH name) | Trigger / Dispatched From | Owner Component | Timing |
|------|----------------------------------|--------------------------|-----------------|--------|
| 1 | [handler name] | [user action `{{signal}}`] | [component name] | sync |
| 2 | [handler name] | dispatched by step 1 | [component name] | sync |
| N | UNKNOWN: [handler name] — [reason] | step N-1 | [component or unknown] | undetermined |

No gap is permitted between steps. If a handler dispatches to another handler, both appear as consecutive rows with the dispatch shown in the Trigger column. Mark any handler whose behavior cannot be determined: `UNKNOWN: [name] — [reason]`.

#### §2 Component Tree Traversal

| Hop | From Component | To Component | Direction | Carrier Name | Signal Type |
|-----|---------------|-------------|-----------|--------------|-------------|
| 1 | [name] | [name] | parent→child | [prop name] | props |
| 2 | [name] | [name] | child→parent | [callback name] | callback |
| 3 | [name] | [name] | sibling | [state key / context] | shared state |

Every component named in §1 must appear in at least one row. The Carrier Name (prop name, callback name, or context/state key) is required for each hop. No component is described generically.

#### §3 State Delta

| State Key / Slice | Before | After | Derived Selectors Affected |
|------------------|--------|-------|---------------------------|
| [key] | [value] | [value] | [selector names, or "none"] |
| UNKNOWN: [key] — [reason] | — | — | — |

Every state update triggered by the action has a row. Selectors or derived state that depend on the changed key are named.

#### §4 Re-render List

| Component | Re-renders? | Reason | Skip Mechanism | Upstream Reference |
|-----------|------------|--------|----------------|-------------------|
| [name] | YES | prop change: [prop name] | — | §2 hop N |
| [name] | YES | context change: [context name] | — | §3 row "[key]" |
| [name] | NO | — | React.memo / selector equality / [mechanism] | §3 row "[key]" — value unchanged |
| [name] | UNKNOWN | — [reason] | — | §2 hop N |

Every component named in §2 must appear. The **Upstream Reference** column is required for every row — cite the §2 hop or §3 row that explains the re-render or skip. This citation is not optional.

#### §5 Side Effects and Async

| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Reference |
|--------|-------|-------|----------------|-------------|-------------------|
| [API call / subscription / timer / storage write] | [component or middleware] | sync / deferred | [state key updated on load] | [state key updated on error] | §1 step N |
| | | | MISSING-LOADING: [reason] | MISSING-ERROR: [reason] | |

For every async effect, name both branches. Mark absent branches with `MISSING-LOADING` or `MISSING-ERROR`. The **Upstream Reference** column must cite the §1 step or §2 hop that owns this effect.

#### §6 Issue Analysis

Evaluate all four categories explicitly. Do not omit any category.

**Unnecessary re-renders:** [component name — §4 row — nature — remediation] / `"None detected — see §4 rows [N, M]"`

**Missing loading states:** [component name — §5 row — nature — remediation] / `"None detected — see §5 rows [N, M]"`

**Error state gaps:** [component name — §5 row — nature — remediation] / `"None detected — see §5 rows [N, M]"`

**Accessibility failures:** [element — nature — remediation] / `"None detected"`

Every "none detected" conclusion must cite the specific §4 or §5 rows that support it. An unsupported "none detected" is not passing.

#### §7 Final UI State

Describe the observable final state after `{{signal}}` fully resolves. For each changed element:
- What is visible / hidden
- What text or data is displayed
- What interactive state (disabled, focused, selected, loading) the component is in

**Every item must derive from a named row in §3.** Format: `"[Element] shows [state] — derived from §3 row '[state key]'."` Derivation citation is required for every item.

#### §8 Optimizations

Identify at least one concrete optimization. If no optimization opportunities exist, state this explicitly and cite the §4 rows that support the conclusion.

| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
|-----------------|------|-----------------|--------------------------|-------------|
| [name] | useMemo / React.memo / reselect selector / render-scope reduction / batching | [what happens now — N renders per action] | [expected outcome — M renders, or "eliminates prop recalc"] | §4 row [N] |

If no optimization: `"No optimization opportunities identified — component tree is correctly memoized or scope-minimal per §4 rows [list all NO rows]."` Citing zero §4 rows when NO rows exist is a failure of this section.

#### §9 Framework Notes

For every MAP entry in §0, list:
- Framework term → Neutral equivalent (as used in §1–§7)
- Which section(s) it appears in
- Framework-specific mechanics (lifecycle order, reactivity model, compiler behavior, etc.)

---

### ROLE 3 — Auditor

You receive the full output from Roles 1 and 2. Produce §10–§12. Nothing else.

#### §10 Completeness Stamp

Scan §1–§8 and count every incompleteness token:

```
UNKNOWN:         [N] — locations: [§1 step N; §3 row "key"; etc.]
MISSING-LOADING: [N] — locations: [§5 row N; etc.]
MISSING-ERROR:   [N] — locations: [§5 row N; etc.]
Issues flagged:  [N] — §6 categories with named findings (not "none detected")
```

**Active correction protocol (mandatory):**
1. After producing the initial count, re-scan §1–§8 and verify each count against the body token-by-token.
2. For any discrepancy: correct the count in the stamp and record: `"Corrected: [category] count [old] → [new]; found additional [TOKEN] at [§N location and row/step identifier]."`
3. If no discrepancy: record: `"Cross-checked: counts match body; no corrections required."`

The cross-check record is required. A stamp without it is incomplete regardless of whether corrections were needed.

#### §11 Vocabulary Audit

Scan §1–§7 for any MAP entry from §0 appearing outside §9.

- For any leak: `LEAK: "[term]" found at §N [row/step identifier]`
- If none: `"No vocabulary leaks detected."`
- For any PASS-THROUGH name appearing aliased to a neutral term: `ALIAS-VIOLATION: "[codebase name]" aliased to "[alias]" at §N [identifier]`

#### §12 Evidence Chain Audit

Verify cross-section citation coverage:

1. Does §7 cite at least one named §3 row? [YES — cite / NO]
2. Does §4 cite at least one §2 or §3 upstream reference per row? [YES — cite / NO — list rows missing citations]
3. Does §5 cite at least one §1 or §2 upstream reference per row? [YES — cite / NO — list rows missing citations]
4. Does §6 cite §4 or §5 rows for "none detected" conclusions? [YES — cite / NO — list unsupported conclusions]

**Evidence chain verdict**: PASS if ≥ 2 downstream sections satisfy their citation requirements; FAIL otherwise — list the missing links.

---

## V-02 — Output Format: Format Contract + Vocabulary Block + Token Rows + Citation Column

**Axis**: Output format
**Hypothesis**: R4 V-02 scored 83/130 because the Format Contract covered only C-01–C-04 and C-10, leaving C-11/C-12/C-13/C-14/C-15 entirely unaddressed. R5 V-02 extends the format contract with four additions: (a) a Vocabulary Contract block prepended before the table schemas (C-14/C-16), (b) a mandatory incompleteness token row in every table (C-12), (c) a "Derived From / Upstream Ref" column in §4–§7 tables forcing cross-section citations (C-11), and (d) an optimization table (C-08) and completeness stamp block (C-15/C-17). C-13 is partial: the format contract can enforce column structure but cannot fully prevent framework jargon from appearing in cell values without vocabulary-contract binding. Expected ceiling: ~115–125/140.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

---

### Pre-Trace: Vocabulary Contract

Before writing any trace content, produce this table:

| Framework Term | Neutral Equivalent | Disposition |
|---------------|-------------------|-------------|
| [term] | [neutral] | MAP |
| [component / handler / selector name] | [same name] | PASS-THROUGH |

**MAP**: Framework primitive — use Neutral Equivalent in §1–§7; Framework Term in §9 only.
**PASS-THROUGH**: Codebase identifier — use exact name in §1–§7; do not alias.

The PASS-THROUGH column is required. Omitting it is a contract failure.

---

### Format Contract

The following table schemas are declared before any trace section is written. Every section must match its declared schema. A column not in the schema does not exist. A required column left blank for a row must contain a gap token, not an empty cell.

**TABLE-01: Event Chain (§1)**

| Step | Handler | Trigger / Dispatch From | Owner Component | Timing | Gap Token |
|------|---------|------------------------|-----------------|--------|-----------|
| Required | Required | Required | Required | sync/deferred | UNKNOWN if undetermined |

**TABLE-02: Component Tree Traversal (§2)**

| Hop | From | To | Direction | Carrier Name | Signal Type | Gap Token |
|-----|------|----|-----------|--------------|-------------|-----------|
| Required | Required | Required | parent→child / child→parent / sibling | prop/callback/state key | props/callback/shared state | UNKNOWN if undetermined |

**TABLE-03: State Delta (§3)**

| State Key / Slice | Before | After | Derived Selectors | Gap Token |
|------------------|--------|-------|------------------|-----------|
| Required | Required | Required | Required or "none" | UNKNOWN if undetermined |

**TABLE-04: Re-render List (§4)**

| Component | Re-renders? | Reason | Skip Mechanism | Upstream Ref | Gap Token |
|-----------|------------|--------|----------------|-------------|-----------|
| Required | YES/NO/UNKNOWN | Required if YES | Required if NO | §2 hopN / §3 row"key" | UNKNOWN if undetermined |

**TABLE-05: Side Effects and Async (§5)**

| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref | Gap Token |
|--------|-------|-------|----------------|-------------|-------------|-----------|
| Required | Required | sync/deferred | State key, or MISSING-LOADING | State key, or MISSING-ERROR | §1 stepN or §2 hopN | UNKNOWN if undetermined |

**TABLE-06: Optimizations (§8)**

| Target Component | Type | Current Behavior | Expected Reduction | §4 Ref |
|-----------------|------|-----------------|-------------------|--------|
| Required | useMemo/React.memo/reselect/scope-reduction/batching | Required | Required | Required |

---

### Trace Sections

Produce §1–§9 in order, using the declared table schemas. For sections using prose (§6, §7, §9), follow the instructions below.

**§1 Event Chain** — TABLE-01. No prose. No rows omitted. Missing rows are Gap Token rows.

**§2 Component Tree Traversal** — TABLE-02. No prose. Every component from §1 has at least one row.

**§3 State Delta** — TABLE-03. No prose. Every state update has a row.

**§4 Re-render List** — TABLE-04. No prose. Every component from §2 has a row (YES, NO, or UNKNOWN). Upstream Ref column required for every row.

**§5 Side Effects and Async** — TABLE-05. No prose. Both loading and error branches declared per async row. Upstream Ref column required.

**§6 Issue Analysis** — Prose. Evaluate all four categories (unnecessary re-renders, missing loading states, error state gaps, accessibility failures). Do not omit any. Each "none detected" must cite specific TABLE-04 or TABLE-05 rows.

**§7 Final UI State** — Prose. Describe observable final state. Every item must name the §3 state key it derives from: `"[Element] shows [state] — §3 row '[key]'."` Derivation citation required for every item.

**§8 Optimizations** — TABLE-06. If no optimizations exist: single row stating `"No optimization opportunities"` with §4 rows cited in the §4 Ref column.

**§9 Framework Notes** — Prose. One paragraph per MAP entry from the Vocabulary Contract. Framework Term → Neutral equivalent used; which sections it appeared in; framework-specific mechanics.

---

### Post-Trace: Completeness Stamp

After §9, produce:

```
UNKNOWN:         [N] — §N locations: [list]
MISSING-LOADING: [N] — §N locations: [list]
MISSING-ERROR:   [N] — §N locations: [list]
Issues flagged:  [N] — §6 findings
```

**Active correction protocol**: After producing the initial count, re-scan Gap Token cells in §1–§8 and verify each count. For any discrepancy: `"Corrected: [category] [old] → [new]; additional [TOKEN] at [§N column/row]."` If no discrepancy: `"Cross-checked: counts match body; no corrections required."`

---

## V-03 — Lifecycle Emphasis: Phase-Gated Trace with Optimization Phase and Registry-Consume Protocol

**Axis**: Lifecycle emphasis
**Hypothesis**: Organizing the trace as seven named phases with hard gates between them enforces two R4 gaps simultaneously: (a) Phase 7 is a dedicated Optimization Phase that cannot be skipped (C-08 — mandatory quantified suggestion or explicit "none" with cited evidence); (b) each phase opens with a Registry-Consume header that names the specific identifiers imported from the prior phase's registry (C-11 — evidence chaining through consumption). Within each phase, incompleteness tokens (UNKNOWN, MISSING-LOADING, MISSING-ERROR) are required at gap points (C-12). Vocabulary contract is absent in this variation — C-13/C-14/C-16 are unaddressed, and C-15/C-17 depend on whether a completeness stamp is included. Expected ceiling: ~100–115/140.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Produce seven phases in order. Each phase must fully complete before the next phase begins.

A phase is complete when:
1. Its Registry is declared at the end of the phase (a named list of identifiers emitted for downstream consumption)
2. All rows or entries in the phase are filled or marked with a gap token

Phases may not be merged. State/render logic stays in its own phase and does not bleed into the event phase.

---

### Phase 1 — Event Phase

**Registry consumed from**: *(none — first phase)*

Enumerate every event handler that fires between `{{signal}}` and the first state mutation.

For each handler: exact function name, owner component, event type, propagation state (capture / target / bubble / stopped), timing (sync / deferred). If handler A dispatches to handler B, both appear in sequence with the dispatch shown. Mark any undetermined handler: `UNKNOWN: [name] — [reason]`.

**Phase 1 Registry** (names emitted to Phase 2):
> Handler names: [list]
> Owner component names: [list]
> Dispatch relationships: [A→B pairs]

---

### Phase 2 — Component Tree Phase

**Registry consumed from Phase 1**: [list the handler names and component names imported from Phase 1 Registry]

For each component named in Phase 1, trace its role in the tree. State direction (parent→child via prop `[name]`, child→parent via callback `[name]`, sibling via shared state `[key]`) for each hop. Every hop names the carrier (prop/callback/state key). No component is described generically.

Mark any component whose tree position cannot be determined: `UNKNOWN: [component] — [reason]`.

**Phase 2 Registry** (names emitted to Phase 3):
> Component names: [list]
> Carrier names (props/callbacks/keys): [list]

---

### Phase 3 — State Phase

**Registry consumed from Phase 2**: [list the component names and carrier names imported from Phase 2 Registry]

For every state mutation triggered by the Phase 1 event chain: state key or slice, value before, value after, selectors or derived state that depend on this key.

Mark any state key whose before/after cannot be determined: `UNKNOWN: [key] — [reason]`.

**Phase 3 Registry** (names emitted to Phase 4):
> State keys mutated: [list]
> Selectors affected: [list]

---

### Phase 4 — Render Phase

**Registry consumed from Phase 3**: [list the state keys and selectors imported from Phase 3 Registry]

For every component in Phase 2: does it re-render? State reason (prop change, context change, selector subscription). For components that do not re-render: name the memoization or equality mechanism. Every component has a row — no silent omissions.

Mark any component whose render behavior cannot be determined: `UNKNOWN: [component] — [reason]`.

**Phase 4 Registry** (names emitted to Phase 5):
> Re-rendered components: [list with reasons]
> Skipped components: [list with mechanisms]

---

### Phase 5 — Effect Phase

**Registry consumed from Phase 4**: [list the re-rendered and skipped components from Phase 4 Registry]

For every side effect triggered (API call, subscription update, timer, storage write): owner component or middleware, when it fires (sync / deferred), what state it updates on success, what state it updates on error.

For any async effect where loading branch cannot be confirmed: `MISSING-LOADING: [effect name] — [reason]`
For any async effect where error branch cannot be confirmed: `MISSING-ERROR: [effect name] — [reason]`

**Phase 5 Registry** (names emitted to Phase 6):
> Effects triggered: [list with owners]
> Loading branches confirmed: [list]
> Error branches confirmed: [list]
> MISSING tokens: [list or "none"]

---

### Phase 6 — Issue Phase

**Registry consumed from Phase 5**: [list effects, loading branches, error branches, and MISSING tokens from Phase 5 Registry]

Also consume Phase 4 Registry for re-render and skip entries.

Evaluate all four issue categories. Do not omit any category.

**Unnecessary re-renders**: [Phase 4 re-rendered component — nature — remediation] / `"None — Phase 4 Registry shows [list of skipped components] as correctly memoized"`

**Missing loading states**: [Phase 5 MISSING-LOADING entry — component — remediation] / `"None — Phase 5 Registry confirms loading branches for all async effects"`

**Error state gaps**: [Phase 5 MISSING-ERROR entry — component — remediation] / `"None — Phase 5 Registry confirms error branches for all async effects"`

**Accessibility failures**: [element — nature — remediation] / `"None detected"`

**Final UI state** (after all phases resolve): Describe observable state. For each changed element, name the Phase 3 state key it derives from.

**Phase 6 Registry** (emitted to Phase 7):
> Unnecessary re-renders identified: [list or "none"]
> Missing loading/error states: [list or "none"]
> Accessibility failures: [list or "none"]

---

### Phase 7 — Optimization Phase

**Registry consumed from Phase 6**: [list the unnecessary re-renders and issue findings from Phase 6 Registry]
**Also consume Phase 4 Registry**: [list the re-rendered components and their reasons]

Identify at least one concrete optimization. If no unnecessary re-renders or structural inefficiencies exist, state this explicitly and cite the Phase 4 Registry entries that confirm it.

For each optimization:
- Target component (from Phase 4 Registry)
- Type: useMemo, React.memo, reselect selector, render-scope reduction, batching
- Current behavior: what renders now and why (Phase 4 reason)
- Expected improvement: N renders → M renders, or specific recalculation eliminated

`"No optimization opportunities — Phase 4 Registry shows all re-renders are necessary per state keys [list] and Phase 6 identifies no unnecessary re-renders."`

---

### Completeness Inventory

After Phase 7, list all incompleteness tokens across all phases:

```
UNKNOWN:         [N] — Phase N, [handler/component/key]
MISSING-LOADING: [N] — Phase 5, [effect names]
MISSING-ERROR:   [N] — Phase 5, [effect names]
Issues flagged:  [N] — Phase 6 categories with findings
```

---

## V-04 — Phrasing Register: Imperative Per-Criterion Checklist

**Axis**: Phrasing register
**Hypothesis**: Translating each v5 criterion's pass condition into a direct imperative instruction creates a self-auditing checklist that reduces interpretation variance. "List EVERY handler in Step order" is harder to partially satisfy than "provide an event chain." Per-criterion instructions target C-08 (explicit optimization mandate) and C-11 (explicit "cite §N row" instruction). Simpler than role machinery; C-14/C-16/C-17 likely fail because those criteria require named pre-trace artifacts that a flat imperative prompt cannot produce. Expected ceiling: ~90–110/140.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Follow each instruction exactly. Complete each section before moving to the next. Use exact names from the codebase — never generic descriptions.

---

**STEP 1 — Detect framework.**
State the frontend framework (React, Vue, Svelte, Angular, other) and the evidence (imports, extensions, hook patterns). Default to React if undetectable. One line.

---

**STEP 2 — Event Chain (§1).**
List EVERY handler that fires between `{{signal}}` and the final UI state. List them in causal order. For each: exact function name, exact owner component name, what triggers it (user action or previous handler dispatch), timing (sync/deferred). If handler A dispatches handler B, list them as consecutive items with the dispatch shown. No handler in the call chain may be omitted. Mark any handler you cannot determine: `UNKNOWN: [name] — [reason]`.

---

**STEP 3 — Component Tree (§2).**
For every component touched by the action, trace the path from the event source to the final state receiver. For each hop state: (a) from component, (b) to component, (c) direction (parent→child / child→parent / sibling), (d) exact carrier name (prop name, callback name, or shared state key). No component is "passed through" without a row. Mark unknowns: `UNKNOWN: [component] — [reason]`.

---

**STEP 4 — State Delta (§3).**
For every state change triggered: (a) exact state key or slice name, (b) value before, (c) value after, (d) any selectors or derived state that depend on this key. Use a table. Mark any state change you cannot confirm: `UNKNOWN: [key] — [reason]`.

---

**STEP 5 — Re-render List (§4).**
For every component in §2, state whether it re-renders. If YES: name the reason (prop change — exact prop; context change — exact context; selector subscription — exact selector) AND cite the §3 row that caused it. If NO: name the exact skip mechanism (React.memo, reselect equality, selector shallow-equal, etc.) AND cite the §3 row showing the value did not change. No component from §2 may be absent from this list.

---

**STEP 6 — Side Effects (§5).**
For every side effect triggered (API call, subscription, timer, storage write): name the effect, its owner, when it fires (sync/deferred), what state key it updates on success, what state key it updates on error. If a loading branch cannot be confirmed: `MISSING-LOADING: [effect] — [reason]`. If an error branch cannot be confirmed: `MISSING-ERROR: [effect] — [reason]`.

---

**STEP 7 — Issues (§6).**
Evaluate all four categories. You MUST address every category — do not skip any.

- **Unnecessary re-renders**: Name any component that re-renders but shouldn't. Name the §4 row. Give a one-line remediation. If none: state "None — §4 rows [N, M] confirm all re-renders are necessary."
- **Missing loading states**: Name any component that fires an async effect but has no loading UI. Name the §5 row. Give a one-line remediation. If none: state "None — §5 rows [N, M] confirm all loading branches."
- **Error state gaps**: Name any component that handles an async effect with no error UI. Name the §5 row. If none: state "None — §5 rows [N, M] confirm all error branches."
- **Accessibility failures**: Name any interactive element missing ARIA role, label, or keyboard handler. Give a one-line remediation. If none: state "None detected."

---

**STEP 8 — Final UI State (§7).**
Describe the observable UI after `{{signal}}` fully resolves. For each changed element: what is visible/hidden, what data is shown, what interactive state (disabled, focused, selected, loading) it is in. For each item, cite the §3 state key it derives from: `"[Element] — §3 row '[key]'."` No item may be listed without a §3 derivation citation.

---

**STEP 9 — Optimizations (§8).**
Name at least one concrete optimization: a specific component, the type (useMemo, React.memo, reselect, batching, scope-reduction), what it prevents, and the expected render reduction (e.g., "eliminates 2 re-renders per action per §4 row N"). If no optimization exists: state "No optimization opportunities — §4 rows [list all NO rows] confirm the tree is correctly memoized or scope-minimal."

---

**STEP 10 — Framework Notes (§9).**
List every framework-specific term used in §1–§8. For each: the framework term, its meaning in framework-neutral language, the section(s) where it appears, and relevant framework mechanics (lifecycle, reactivity model, compiler behavior).

---

**STEP 11 — Completeness Stamp.**
Count every gap token in §1–§8:

```
UNKNOWN:         [N] — §N step/row references
MISSING-LOADING: [N] — §5 row references
MISSING-ERROR:   [N] — §5 row references
Issues flagged:  [N] — §6 categories with named findings
```

After producing this count, re-read §1–§8 and verify each count. If any token was missed: `"Corrected: [category] [old] → [new]; missed [TOKEN] at [§N reference]."` If no corrections: `"Cross-checked: counts match."`

---

## V-05 — Combined: Role Sequence + Lifecycle Emphasis

**Axis**: Combined — Role sequence + Lifecycle emphasis
**Hypothesis**: The two mechanisms that independently achieve high scores in this series are (a) the Vocabulary Contract blocking gate (Role 1 producing the contract before any trace content, enforcing C-14/C-16) and (b) the phase-gated trace with registry-consume protocol (enforcing C-11/C-08 structurally). V-05 combines both in a three-role pipeline: Role 1 produces the vocabulary contract with PASS-THROUGH designation (C-14/C-16); Role 2 runs 7 phase-gated sections with registry-consume openings (C-08/C-11/C-12) bound to the vocabulary contract (C-13); Role 3 produces an active completeness stamp with correction notation (C-15/C-17) plus vocabulary leak and evidence-chain audits. All 17 criteria are directly targeted. Expected ceiling: 138–140/140.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role in full before beginning the next. No role produces content for downstream roles — only output.

---

### ROLE 1 — Contract Author

Produce §0. No trace content, section labels, or structural hints.

#### §0 Vocabulary Contract

| Framework Term | Neutral Equivalent | Disposition | Notes |
|---------------|-------------------|-------------|-------|

**Disposition values:**

**MAP** — Framework primitive (e.g., `useState`, `useEffect`, `v-model`, `watchEffect`, `@Input()`, `ChangeDetectionStrategy`, `$store`). Use Neutral Equivalent in §1–§7. Framework Term in §9 only.

**PASS-THROUGH** — Codebase proper name: component name, handler name, selector, store slice, or identifier that must be unchanged in the trace for source navigability. Use exact codebase name in §1–§7. Inventing a neutral alias for a PASS-THROUGH name is a contract violation.

The PASS-THROUGH designation is a required named column. A contract without it fails C-16.

Rules: include every framework-specific term; framework primitives default to MAP; codebase identifiers default to PASS-THROUGH; conflicts default to PASS-THROUGH with a note.

**Role 1 ends here. Do not produce any §1–§9 content.**

---

### ROLE 2 — Phase-Gated Trace Author

You receive §0. Produce §1–§9 across 7 phases plus Framework Notes.

**Binding constraint**: §1–§7 use only Neutral Equivalents for MAP terms and exact codebase names for PASS-THROUGH terms. Framework primitives outside §9 are vocabulary violations.

Each phase must fully complete before the next begins. Each phase opens with a **Registry Consumed** header and closes with a **Phase Registry** that names the identifiers emitted to the next phase.

---

#### Phase 1 — Event Phase → §1 Event Chain

**Registry Consumed**: *(none — first phase)*

**§1 Event Chain** — For every handler that fires between `{{signal}}` and the first state mutation:

| Step | Handler | Trigger / Dispatch From | Owner Component | Timing |
|------|---------|------------------------|-----------------|--------|
| 1 | [PASS-THROUGH handler name] | `{{signal}}` | [PASS-THROUGH component] | sync |
| N | UNKNOWN: [name] — [reason] | step N-1 | [component or unknown] | undetermined |

**Phase 1 Registry**:
> Handlers: [list]
> Owner components: [list]
> Dispatch pairs: [A→B list]

---

#### Phase 2 — Component Tree Phase → §2 Component Tree Traversal

**Registry Consumed from Phase 1**: [list handler names and component names from Phase 1 Registry — must name each explicitly]

**§2 Component Tree Traversal** — For every component named in Phase 1:

| Hop | From | To | Direction | Carrier Name | Signal Type |
|-----|------|----|-----------|--------------|-------------|
| 1 | [name] | [name] | parent→child | [prop name] | props |
| N | UNKNOWN: [name] — [reason] | — | — | — | — |

**Phase 2 Registry**:
> Components: [list]
> Carrier names: [list]

---

#### Phase 3 — State Phase → §3 State Delta

**Registry Consumed from Phase 2**: [list component names and carrier names from Phase 2 Registry]

**§3 State Delta** — For every state mutation triggered by Phase 1:

| State Key / Slice | Before | After | Derived Selectors | Gap Token |
|------------------|--------|-------|------------------|-----------|
| [key] | [value] | [value] | [names or "none"] | |
| UNKNOWN: [key] — [reason] | — | — | — | UNKNOWN |

**Phase 3 Registry**:
> State keys mutated: [list]
> Selectors affected: [list]

---

#### Phase 4 — Render Phase → §4 Re-render List

**Registry Consumed from Phase 3**: [list state keys and selectors from Phase 3 Registry]

**§4 Re-render List** — For every component in Phase 2:

| Component | Re-renders? | Reason | Skip Mechanism | Phase 3 Key Ref |
|-----------|------------|--------|----------------|-----------------|
| [name] | YES | [prop/context/selector] | — | "[key]" |
| [name] | NO | — | [mechanism] | "[key]" unchanged |
| [name] | UNKNOWN | — [reason] | — | — |

Every Phase 2 component must appear. Phase 3 Key Ref is required.

**Phase 4 Registry**:
> Re-rendered: [list with reasons]
> Skipped: [list with mechanisms]

---

#### Phase 5 — Effect Phase → §5 Side Effects and Async

**Registry Consumed from Phase 4**: [list re-rendered and skipped components from Phase 4 Registry]

**§5 Side Effects and Async**:

| Effect | Owner | Fires | Loading Branch | Error Branch | Phase 1 Ref |
|--------|-------|-------|----------------|-------------|-------------|
| [name] | [component/middleware] | sync/deferred | [key updated] | [key updated] | step N |
| | | | MISSING-LOADING: [reason] | MISSING-ERROR: [reason] | |

Phase 1 Ref must name the Phase 1 step that owns this effect.

**Phase 5 Registry**:
> Effects: [list]
> Loading confirmed: [list]
> Error confirmed: [list]
> MISSING tokens: [list or "none"]

---

#### Phase 6 — Issue and Final State Phase → §6 and §7

**Registry Consumed from Phase 5**: [list effects, loading/error confirmed, MISSING tokens from Phase 5 Registry]
**Also consume Phase 4 Registry**: [list re-rendered and skipped components]

**§6 Issue Analysis** — All four categories required:

- **Unnecessary re-renders**: [Phase 4 component — nature — remediation] / `"None — Phase 4 Registry: [skipped components list]"`
- **Missing loading states**: [Phase 5 MISSING-LOADING — component — remediation] / `"None — Phase 5 Registry confirms all loading branches"`
- **Error state gaps**: [Phase 5 MISSING-ERROR — component — remediation] / `"None — Phase 5 Registry confirms all error branches"`
- **Accessibility failures**: [element — nature — remediation] / `"None detected"`

**§7 Final UI State** — Observable state after `{{signal}}` resolves. Each item derives from Phase 3:
`"[Element] shows [state] — Phase 3 key '[key]'."`

**Phase 6 Registry**:
> Unnecessary re-renders: [list or "none"]
> Missing branches: [list or "none"]
> Accessibility issues: [list or "none"]

---

#### Phase 7 — Optimization Phase → §8 Optimizations

**Registry Consumed from Phase 6**: [list unnecessary re-renders from Phase 6 Registry]
**Also consume Phase 4 Registry**: [list re-rendered components and their reasons]

**§8 Optimizations**:

| Target Component | Type | Current Behavior | Expected Reduction | Phase 4 Ref |
|-----------------|------|-----------------|-------------------|-------------|
| [name] | useMemo/React.memo/reselect/scope-reduction/batching | [N renders per action] | [M renders, or "eliminates recalc"] | re-rendered row |

If no optimization exists: `"No optimization opportunities — Phase 4 Registry shows all re-renders necessary per state keys [list]; Phase 6 identified no unnecessary re-renders."` Cite at least one Phase 4 skipped-component row.

---

#### §9 Framework Notes

For every MAP entry in §0:
- Framework Term → Neutral Equivalent used in §1–§7
- Phases where it appears
- Framework-specific mechanics

---

### ROLE 3 — Active Auditor

You receive the full output from Roles 1 and 2. Produce §10–§12. Nothing else.

#### §10 Completeness Stamp

Scan §1–§8 (all phases) for incompleteness tokens:

```
UNKNOWN:         [N] — Phase N, [handler/component/key identifiers]
MISSING-LOADING: [N] — Phase 5, [effect names]
MISSING-ERROR:   [N] — Phase 5, [effect names]
Issues flagged:  [N] — §6 categories with named findings
```

**Active correction protocol (required):**
1. After initial count, re-scan Phase 1–Phase 7 outputs token-by-token and verify each count.
2. For any discrepancy: `"Corrected: [category] [old] → [new]; found additional [TOKEN] at Phase N, [row/step identifier]."`
3. If no discrepancy: `"Cross-checked: counts match body; no corrections required."`

The cross-check record is required even when no corrections are needed.

#### §11 Vocabulary Audit

Scan §1–§7 for MAP terms from §0 appearing outside §9:
- Found: `LEAK: "[term]" at Phase N, [row/step identifier]`
- Not found: `"No vocabulary leaks detected."`

Scan for PASS-THROUGH names appearing with an invented neutral alias:
- Found: `ALIAS-VIOLATION: "[codebase name]" aliased to "[alias]" at Phase N, [identifier]`
- Not found: `"No alias violations detected."`

#### §12 Evidence Chain Audit

1. Does §7 cite at least one Phase 3 key? [YES — cite / NO]
2. Does §4 cite Phase 3 key refs for every row? [YES / NO — list rows missing refs]
3. Does §5 cite Phase 1 step refs for every row? [YES / NO — list rows missing refs]
4. Do Phase N registries name specific identifiers (not generic counts) from the phase they consume? [YES / NO — list phases with generic or empty consumed-registry headers]

**Evidence chain verdict**: PASS if ≥ 2 downstream-section citation requirements are fully met; FAIL — list missing links.
