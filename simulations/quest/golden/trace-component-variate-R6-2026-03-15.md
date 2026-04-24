# trace-component — R6 Variations (v6 rubric)

**Round**: 6
**Rubric ceiling**: 150 pts (C-01 through C-19)
**Rubric file**: `simulations/quest/rubrics/trace-component-rubric-v6-2026-03-15.md`

**R5 baseline summary:**
- V-01 (Role Sequence / Vocabulary Contract blocking gate + PASS-THROUGH + optimization section + full citation chain + active stamp correction): 138–140/140 GOLDEN. Identified structure: three roles (Contract Author → Trace Author → Auditor); C-18 partial because the vocabulary constraint was stated as a passive "Binding constraint" instruction in Role 2 rather than a named blocking gate role or step; C-19 partial because TABLE-01 schema was embedded inline within Role 2's §1 instructions rather than declared as a named block before any content generation.
- V-02 (Output Format / Format Contract + vocabulary block + token rows + citation column): ~115–125/140. Same C-18/C-19 gaps as V-01 — schema blocks appeared as Format Contract headers but were authored by the trace-generating role, not declared by a dedicated pre-trace role, and the vocabulary constraint was a two-sentence block rather than a named gate.
- V-03 (Lifecycle Emphasis / Phase-gated trace with registry-consume): ~100–110/140. No vocabulary contract; C-13/C-14/C-16 absent; completeness stamp present but no active correction; phase gates addressed C-08/C-11/C-12.
- V-04 (Phrasing Register / Imperative checklist): ~95–110/140. Flat prompt; imperative mandates addressed C-08/C-11/C-12; no structural artifacts for C-14/C-16/C-17.
- V-05 (Combined: Role seq + Lifecycle): ~135–140/140. All three structural mechanisms present; same C-18/C-19 gaps as V-01.

**New v6 criteria:**
- C-18: Role-level vocabulary enforcement gate — the vocabulary constraint must be enforced by an active named blocking gate (not a passive instruction); gate takes the form of a named check step or transition condition that the generating role must pass before outputting any core section; depends on C-14.
- C-19: Pre-declared named column schemas for essential sections — TABLE-01 SCHEMA (event chain, §1) and TABLE-04 SCHEMA (re-render list, §4) must each be declared as named blocks *before* the first row of section content; schema must carry a label; schema produced inline during content generation does not satisfy this criterion; builds on C-10.

**R6 variation axes chosen (3 single-axis + 2 combined):**
1. Role sequence — Schema-first: Schema Architect declares TABLE-01 SCHEMA and TABLE-04 SCHEMA *before* Contract Author; schemas become the named artifacts (C-19) that the vocabulary contract later binds to
2. Role sequence — Contract-first: Contract Author establishes MAP/PASS-THROUGH *before* Schema Architect; schema column names are authored using contract's neutral vocabulary (guarantees column headers are framework-neutral)
3. Phrasing register — Imperative checklist: C-18 gate rendered as a boxed STOP block with binary pass/fail; C-19 rendered as numbered pre-flight steps with explicit before/after artifact states
4. Lifecycle emphasis — Phase-gated hard stop: C-18 gate becomes PHASE-3 (a named phase gate, not a role); PHASE-3 must output a gate artifact before PHASE-4 exists; C-19 handled by PHASE-1 (schema declarations only)
5. Combined — Trace Architecture fusion + inertia framing: Schema Architect and Contract Author fused into one "TRACE ARCHITECTURE" role whose output is a single named artifact containing both schemas and contract; inertia framing opens the prompt; evidence chain foregrounded as a parallel named requirement

**R6 variation map:**

| Variation | Axis | C-18 | C-19 | C-14 | C-16 | C-11 | C-15 | C-17 | Hypothesis |
|-----------|------|------|------|------|------|------|------|------|------------|
| V-01 | Role sequence (schema-first) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Schema declarations precede vocabulary contract — named schema blocks (C-19) established independently before MAP/PASS-THROUGH designations; gate role operates on schemas already present as named artifacts |
| V-02 | Role sequence (contract-first) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Vocabulary contract precedes schemas — schema column names authored after MAP/PASS-THROUGH table are guaranteed neutral; gate embedded in Schema Architect role rather than separate gate role |
| V-03 | Phrasing register (imperative checklist) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Atomic imperatives with PASS/FAIL conditions for C-18 gate and C-19 pre-flight; STOP block elevates gate from guidance to structural enforcement; flat prompt without role machinery |
| V-04 | Lifecycle emphasis (phase-gated hard stop) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | C-18 becomes PHASE-3 (a phase gate artifact, not a role instruction); PHASE-4 cannot begin without PHASE-3 output; C-19 handled by PHASE-1 as sole output; phases with dedicated input/output contracts |
| V-05 | Combined (TA fusion + inertia + evidence foreground) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Schema+contract fused into single TRACE ARCHITECTURE artifact reduces structural overhead; inertia framing activates gap-detection reasoning; evidence chain foregrounded as named first-class requirement; C-18 gate embedded in fusion artifact as self-check |

Legend: PASS = mechanism directly targets and likely satisfies the criterion

---

## V-01 — Role Sequence: Schema-First (C-19 Before C-14, Named Gate Role)

**Axis**: Role sequence — Schema Architect declares TABLE-01 SCHEMA and TABLE-04 SCHEMA as named blocks before vocabulary contract authoring; a dedicated Gate role (not an inline instruction) enforces C-18 as a named blocking transition.

**Hypothesis**: In R5, the vocabulary constraint was embedded in Role 2's binding instruction — a passive rule the generating role was expected to self-apply. C-18 requires a *different role* or *named gate step* that verifies the constraint before allowing §1–§7 to proceed. Separating schema declaration (Role 1) from contract authoring (Role 2) means the named schema blocks exist as artifacts before any vocabulary mapping occurs; the Contract Author can then explicitly bind PART B (PASS-THROUGH) to the named column headers of TABLE-01 and TABLE-04. Role 3 (Gate) is a standalone role whose *only output* is the GATE-VOCAB result — a structural separation that makes blocking non-optional. Expected ceiling: 148–150/150.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. No role may produce trace content, vocabulary mappings, or pre-populate downstream roles' outputs. Role output is visible to all subsequent roles.

---

### ROLE 1 — Schema Architect

Your sole output is two named schema blocks. No vocabulary contract, no trace content, no section outlines, no structural hints for downstream roles appear in this role.

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns:
  Step            — Sequential integer. Required for every row.
  Handler         — Exact codebase name of the handler function. UNKNOWN: [name] — [reason] if undetermined.
  Trigger         — The user action {{signal}} (step 1) or the upstream step/dispatch that caused this handler.
  Owner           — Exact codebase name of the component that owns this handler. UNKNOWN: [component] — [reason] if undetermined.
  Timing          — "sync" or "deferred".

Required token values:
  UNKNOWN: [name] — [reason]   (any handler or owner that cannot be determined)

Fill rules:
  1. Every causal hop from user action to final handler occupies one row.
  2. If Handler A dispatches to Handler B, both rows are present and Handler A's step appears in Handler B's Trigger column.
  3. An implicit jump (step 1 to step 3 with step 2 absent) is a schema violation.
  4. An empty table is a schema violation. Minimum 1 row.
```

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns:
  Component        — Exact codebase name. Required.
  Re-renders?      — "YES", "NO", or "UNKNOWN".
  Reason           — Prop change (name the prop), context change (name the context key), selector subscription (name the selector). Blank only for NO rows. MISSING-LOADING if loading-branch re-render unconfirmed.
  Skip Mechanism   — The memoization or equality mechanism that blocked re-render (for NO rows). Blank for YES rows.
  Upstream Ref     — Citation to §2 hop number or §3 row state key that caused or explains this entry.

Required token values:
  UNKNOWN                (Re-renders? column, when re-render status cannot be determined)
  MISSING-LOADING        (Reason column, when a loading-branch re-render is unconfirmed)

Fill rules:
  1. Every component named in §2 must appear. Silent omission is a schema violation.
  2. A memoized component that was evaluated and skipped must appear as a NO row — not absent.
  3. An empty NO section when memoized components exist is a schema violation.
  4. Upstream Ref is required for every row including NO rows.
```

**Do not produce any vocabulary contract, §1–§9 content, or gate output. These schemas are the complete output of Role 1.**

---

### ROLE 2 — Contract Author

You receive TABLE-01 SCHEMA and TABLE-04 SCHEMA from Role 1. Produce §0 Vocabulary Contract. No trace content.

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Map every framework-specific API, directive, decorator, or reactive primitive that will appear in this trace to its neutral equivalent. The Neutral Equivalent is used in §1–§7. The Framework Term appears only in §8.

Examples: `useState` → `local state hook` | `useEffect` → `side-effect hook` | `v-model` → `two-way binding directive` | `watchEffect` → `reactive watch` | `@Input()` → `property binding` | `ChangeDetectionStrategy.OnPush` → `change-detection gate`

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Notes |
|------------------|------|-------|

Declare every codebase identifier that must appear *unchanged* in §1–§7 to remain navigable in the source. Verify that each name below has a corresponding row:
- Every name that will appear in TABLE-01's Handler and Owner columns
- Every name that will appear in TABLE-04's Component column
- Every selector name, store slice key, and event handler exported from a module

Type values: `component` | `handler` | `selector` | `store-slice` | `event-name`

**Rules:**
1. The PASS-THROUGH TABLE is a required named artifact. Omitting it is a contract failure (fails C-16).
2. Framework primitives are MAP by default. Codebase identifiers are PASS-THROUGH by default.
3. If a term is both a framework primitive and a codebase-defined name, default to PASS-THROUGH and note the conflict.
4. Do not invent a neutral alias for a PASS-THROUGH name.

**Binding declaration**: §1–§7 are bound to the Neutral Equivalent column of PART A and to the exact names in PART B. MAP terms appear only in §8. PASS-THROUGH names appear in §1–§7 exactly as declared.

**Do not produce any §1–§9 content. §0 is the complete output of Role 2.**

---

### ROLE 3 — Enforcement Gate

You receive TABLE-01 SCHEMA, TABLE-04 SCHEMA, and §0 Vocabulary Contract from Roles 1–2. Your sole output is the GATE-VOCAB result.

**GATE-VOCAB** — Before any core section (§1–§7) is generated, verify:

> For every column in TABLE-01 SCHEMA (Handler, Owner) and TABLE-04 SCHEMA (Component, Reason): does any planned cell value contain a MAP term from §0 PART A?

State the result:

- `GATE-VOCAB: PASS — no MAP terms detected in TABLE-01/TABLE-04 column value space. Proceeding to Role 4.`
- `GATE-VOCAB: FAIL — violations detected:` [list each: MAP term | planned section | column | row context] `Corrections required. Role 4 blocked until GATE-VOCAB: PASS.`

**This gate is a blocking transition. Role 4 may not begin until this role outputs GATE-VOCAB: PASS.**

If FAIL: correct §0 PART A or the trace plan. Restate the gate. Repeat until PASS. Document each correction cycle: `Correction [N]: changed [term] MAP→PASS-THROUGH / changed planned cell value [old] → [new]`.

**GATE-VOCAB result is the complete output of Role 3.**

---

### ROLE 4 — Trace Author

You receive GATE-VOCAB: PASS, TABLE-01 SCHEMA, TABLE-04 SCHEMA, and §0 Vocabulary Contract. Produce §1–§9 in full, in order.

**Vocabulary binding (active):** In §1–§7, every MAP term from §0 PART A is replaced by its Neutral Equivalent. Every codebase identifier uses its exact PASS-THROUGH name. No MAP term appears in §1–§7 cell values.

#### §1 Event Chain

Fill TABLE-01 exactly. No columns added or removed. No rows omitted. If a handler is unknown, the UNKNOWN token occupies that row — the row does not disappear.

#### §2 Component Tree Traversal

| Hop | From | To | Direction | Carrier Name | Signal Type |
|-----|------|----|-----------|--------------|-------------|

Every component named in §1 appears in at least one row. Carrier Name (prop, callback name, or state key) is required for every hop. Direction: `parent→child` | `child→parent` | `sibling`. Signal Type: `props` | `callback` | `shared state` | `context`.

#### §3 State Delta

| State Key / Slice | Before | After | Derived Selectors Affected |
|------------------|--------|-------|---------------------------|

Every state update has a row. Selectors that depend on the changed key are named. Mark undetermined keys: `UNKNOWN: [key] — [reason]`.

#### §4 Re-render List

Fill TABLE-04 exactly. No columns added or removed. Every component from §2 has a row. Upstream Ref is required for every row.

#### §5 Side Effects and Async

| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref (§1 step) |
|--------|-------|-------|----------------|-------------|----------------------|

Every async effect has both branches declared. Mark unconfirmed branches: `MISSING-LOADING: [reason]` or `MISSING-ERROR: [reason]`. Upstream Ref cites the §1 step or §2 hop that owns the effect.

#### §6 Issue Analysis

Evaluate all four categories. Do not omit any.

**Unnecessary re-renders:** [Component — §4 row — nature — one-line remediation] or `"None detected — §4 rows [cite rows]"`

**Missing loading states:** [Component — §5 row — nature — remediation] or `"None detected — §5 rows [cite rows]"`

**Error state gaps:** [Component — §5 row — nature — remediation] or `"None detected — §5 rows [cite rows]"`

**Accessibility failures:** [Element — nature — remediation] or `"None detected"`

Every "none detected" conclusion must cite specific §4 or §5 rows. An unsupported "none detected" fails C-06.

#### §7 Final UI State

Observable state after `{{signal}}` fully resolves. For each changed element:

`"[Element] shows [state] — derived from §3 row '[state key]'."`

Derivation citation from §3 is required for every item. The chain §1 → §3 → §4 → §7 must be traceable by reference.

#### §8 Framework Notes

For every MAP entry in §0 PART A:

| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
|---------------|-------------------|----------------------|--------------------------|

This is the only section where MAP terms appear. Explain framework-specific lifecycle order, reactivity model, or compiler behavior as relevant.

#### §9 Optimization Opportunities

| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
|-----------------|------|-----------------|--------------------------|-------------|

Types: `memoization candidate` | `batching opportunity` | `render-scope reduction`

At least one entry. If no optimization opportunities exist:
`"No optimization opportunities identified — component tree correctly scoped per §4 rows [list all NO rows]."`

Citing zero §4 rows when NO rows exist is a failure.

---

### ROLE 5 — Auditor

You receive the full output of Roles 1–4. Produce §10–§12.

#### §10 Completeness Stamp

Scan §1–§9 and count every incompleteness token:

```
UNKNOWN:         [N] — locations: [§ reference and row/step identifier for each]
MISSING-LOADING: [N] — locations: [§ reference and row/step identifier for each]
MISSING-ERROR:   [N] — locations: [§ reference and row/step identifier for each]
Issues flagged:  [N] — §6 categories with named findings (exclude "none detected" conclusions)
```

**Active correction protocol (mandatory):**
1. After producing the initial count, re-scan §1–§9 body token-by-token and verify each count.
2. Discrepancy found: `"Corrected: [CATEGORY] count [old] → [new]; found additional [TOKEN] at [§N location — row/step identifier]."`
3. No discrepancy: `"Cross-checked: counts match body; no corrections required."`

The cross-check record is required regardless of whether corrections were needed. A stamp without it fails C-17.

#### §11 Vocabulary Audit

Scan §1–§7 for MAP terms from §0 PART A appearing outside §8.

- Leak: `LEAK: "[term]" found at §N [row/step identifier — column name]`
- PASS-THROUGH aliased: `ALIAS-VIOLATION: "[codebase name]" aliased to "[alias]" at §N [identifier]`
- Clean: `"No vocabulary leaks detected. No alias violations detected."`

#### §12 Evidence Chain Audit

1. §7 cites ≥1 named §3 row? [YES — cite / NO]
2. §4 Upstream Ref column populated for every row? [YES / NO — list rows missing citations]
3. §5 Upstream Ref column populated for every row? [YES / NO — list rows missing citations]
4. §6 "none detected" conclusions cite specific §4 or §5 rows? [YES — cite / NO — list unsupported conclusions]

**Verdict**: PASS if ≥2 downstream sections satisfy citation requirements; FAIL — list missing links.

---

## V-02 — Role Sequence: Contract-First (C-14 Before C-19, Gate Embedded in Schema Role)

**Axis**: Role sequence — Contract Author establishes MAP/PASS-THROUGH designations *before* Schema Architect declares table schemas; the Schema Architect's second task is to verify that column names use only neutral vocabulary from PART A; the gate (C-18) is embedded as the Schema Architect's final step rather than a standalone gate role.

**Hypothesis**: In V-01 the Schema Architect cannot reference the vocabulary contract because the contract does not exist yet — the schemas are authored in a vocabulary vacuum. V-02 reverses this: the Contract Author runs first, establishing PART A (MAP terms) and PART B (PASS-THROUGH names), and the Schema Architect then declares TABLE-01 SCHEMA and TABLE-04 SCHEMA using column names explicitly drawn from PART A's Neutral Equivalent column. The gate (C-18) becomes the Schema Architect's final step: "verify that no MAP term appears in any declared column name." This embeds C-18 enforcement earlier in the pipeline, before the Trace Author ever sees the schemas. Reduction in role count (4 roles instead of 5) may reduce structural overhead at the cost of one less explicit role separation. Expected ceiling: 145–150/150.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. No role may produce trace content or pre-populate downstream roles' outputs. Role output is visible to all subsequent roles.

---

### ROLE 1 — Contract Author

Your sole output is the §0 Vocabulary Contract. No schemas, no trace content.

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Every framework-specific API, directive, decorator, or reactive primitive present in the codebase context. Neutral Equivalent is the term used in §1–§7 core sections.

Examples of MAP entries: `useState` → `local state hook` | `useEffect` → `side-effect hook` | `dispatch` (Redux) → `action dispatcher` | `v-model` → `two-way binding directive` | `@Input()` → `property binding` | `$store` → `shared state accessor`

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Notes |
|------------------|------|-------|

Every codebase proper name that must appear unchanged in §1–§7: component names, handler function names, selector names, store slice keys, event names. These names will appear verbatim in TABLE-01 SCHEMA's Handler and Owner columns and TABLE-04 SCHEMA's Component column.

Type values: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`

**Required rules:**
1. PASS-THROUGH TABLE is a required named artifact. Omitting it fails C-16.
2. Every codebase identifier that will appear in §1–§7 must be in PART B.
3. No codebase identifier is neutralized — PASS-THROUGH names are not mapped to neutral aliases.
4. Framework primitives are MAP by default. Codebase identifiers are PASS-THROUGH by default.
5. Conflict (codebase name that is also a framework primitive): default PASS-THROUGH, note conflict.

**Binding declaration**: §1–§7 use Neutral Equivalents from PART A; MAP terms appear only in §8. PASS-THROUGH names from PART B appear in §1–§7 exactly as declared.

**§0 Vocabulary Contract is the complete output of Role 1.**

---

### ROLE 2 — Schema Architect

You receive §0 Vocabulary Contract from Role 1. Produce two named schema blocks and a gate result.

**Step 2a — Declare TABLE-01 SCHEMA using contract vocabulary**

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns (all names drawn from §0 PART A Neutral Equivalents or PART B Pass-Through Names):
  Step          — Sequential integer. Required.
  Handler       — PASS-THROUGH name from §0 PART B. UNKNOWN: [name] — [reason] if undetermined.
  Trigger       — {{signal}} (step 1) or upstream step that dispatched this handler.
  Owner         — PASS-THROUGH name from §0 PART B (component type). UNKNOWN: [component] if undetermined.
  Timing        — "sync" or "deferred".

Required token: UNKNOWN: [name] — [reason]
Fill rules:
  - Every causal hop is one row. Dispatch chains show both source and target rows.
  - Implicit jumps are schema violations.
```

**Step 2b — Declare TABLE-04 SCHEMA using contract vocabulary**

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns (all names drawn from §0 PART A Neutral Equivalents or PART B Pass-Through Names):
  Component      — PASS-THROUGH name from §0 PART B.
  Re-renders?    — "YES", "NO", or "UNKNOWN".
  Reason         — Neutral Equivalent term from §0 PART A describing the trigger (e.g., "prop change: [prop name]",
                   "context change: [context key]", "selector subscription: [selector name]"). MISSING-LOADING if
                   loading-branch re-render unconfirmed.
  Skip Mechanism — Mechanism name for NO rows.
  Upstream Ref   — §2 hop number or §3 state key.

Required tokens: UNKNOWN | MISSING-LOADING
Fill rules:
  - Every §2 component appears. Silent omissions are violations.
  - Memoized/skipped components appear as NO rows — not absent.
  - Upstream Ref required for all rows including NO rows.
```

**Step 2c — GATE-VOCAB (embedded gate, C-18)**

Inspect TABLE-01 SCHEMA and TABLE-04 SCHEMA column name declarations. Verify: no column name is a MAP term from §0 PART A.

State result:
- `GATE-VOCAB: PASS — all column names are neutral or PASS-THROUGH. Proceeding to Role 3.`
- `GATE-VOCAB: FAIL — column [name] in TABLE-[N] is a MAP term from §0 PART A. Correcting: [name] → [neutral equivalent]. Re-checking.` (Correct and restate until PASS.)

**This gate is a blocking condition on Role 3. Role 3 may not begin until GATE-VOCAB: PASS is stated here.**

**TABLE-01 SCHEMA, TABLE-04 SCHEMA, and GATE-VOCAB result are the complete output of Role 2.**

---

### ROLE 3 — Trace Author

You receive GATE-VOCAB: PASS, §0 Vocabulary Contract, TABLE-01 SCHEMA, and TABLE-04 SCHEMA. Produce §1–§9 in full, in order.

**Active vocabulary binding:** In §1–§7, Neutral Equivalents from §0 PART A replace all MAP terms. PASS-THROUGH names from §0 PART B appear exactly as declared.

#### §1 Event Chain
Fill TABLE-01. Every hop. No gaps. UNKNOWN token for any undetermined handler.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component appears. Carrier Name required per hop. Direction: `parent→child` | `child→parent` | `sibling`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every state update has a row. Selectors named. UNKNOWN for undetermined keys.

#### §4 Re-render List
Fill TABLE-04. Every §2 component has a row. Upstream Ref required for every row.

#### §5 Side Effects and Async
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref (§1 step) |
Both branches per async effect. MISSING-LOADING / MISSING-ERROR for unconfirmed branches.

#### §6 Issue Analysis
All four categories evaluated — no omissions:
- **Unnecessary re-renders:** [Component — §4 row — gap — remediation] or `"None detected — §4 rows [cite]"`
- **Missing loading states:** [Component — §5 row — gap — remediation] or `"None detected — §5 rows [cite]"`
- **Error state gaps:** [Component — §5 row — gap — remediation] or `"None detected — §5 rows [cite]"`
- **Accessibility failures:** [Element — gap — remediation] or `"None detected"`

Every "none detected" cites the specific rows that support it.

#### §7 Final UI State
Observable state after `{{signal}}` resolves. Every item: `"[Element] shows [state] — derived from §3 row '[state key]'."` Chain §1→§3→§4→§7 traceable by reference.

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) | Framework mechanics note |
Every MAP entry from §0 PART A. Only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
At least one entry or explicit "none" citing §4 NO rows.

---

### ROLE 4 — Auditor

Produce §10–§12.

#### §10 Completeness Stamp
```
UNKNOWN:         [N] — locations: [list]
MISSING-LOADING: [N] — locations: [list]
MISSING-ERROR:   [N] — locations: [list]
Issues flagged:  [N] — §6 named findings
```
Active correction protocol: re-scan body token-by-token; correct discrepancies with notation `"Corrected: [CATEGORY] [old]→[new]; found at [§N location]"`; if clean: `"Cross-checked: counts match body; no corrections required."` Cross-check record required.

#### §11 Vocabulary Audit
Scan §1–§7 for MAP term leaks or PASS-THROUGH aliasing. Report each leak/alias or `"No leaks detected. No alias violations detected."`

#### §12 Evidence Chain Audit
1. §7 cites ≥1 named §3 row? [YES / NO]
2. §4 Upstream Ref populated for every row? [YES / NO — list missing]
3. §5 Upstream Ref populated for every row? [YES / NO — list missing]
4. §6 "none detected" conclusions cite rows? [YES / NO — list unsupported]
**Verdict**: PASS if ≥2 downstream sections satisfy citation requirements; FAIL — list gaps.

---

## V-03 — Phrasing Register: Imperative Checklist with STOP Block Gate

**Axis**: Phrasing register — every requirement is a numbered atomic imperative with an explicit PASS/FAIL condition stated inline; C-18 gate is a boxed STOP block that must output a token before proceeding; C-19 is a two-step pre-flight sequence with labeled before/after artifact states.

**Hypothesis**: R5 V-04 (imperative checklist) failed C-14/C-16/C-17 because flat prompts cannot enforce structural artifact production. V-03 retains the imperative phrasing but introduces two structural features absent from R5 V-04: (a) a two-step PRE-FLIGHT sequence that forces TABLE-01 SCHEMA and TABLE-04 SCHEMA as named artifacts before any other work (C-19); (b) a STOP BLOCK that must output `[GATE-VOCAB: PASS]` before the trace checklist can begin (C-18). The imperative register then drives C-01–C-17 through per-criterion numbered steps, each with an inline "FAIL if:" condition that makes omissions structurally visible. Expected ceiling: 145–150/150.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Execute every step in order. Do not skip steps or combine outputs across steps. A step is complete when its named output artifact exists and its PASS condition is satisfied.

---

### PRE-FLIGHT SEQUENCE

**Step P-1 — Declare TABLE-01 SCHEMA (C-19)**

Produce the following named block before writing any other content:

#### TABLE-01 SCHEMA: Event Chain (§1)
```
Column definitions:
  Step          — integer, required
  Handler       — codebase function name, or UNKNOWN: [name] — [reason]
  Trigger       — user action (step 1) or upstream step reference
  Owner         — codebase component name, or UNKNOWN: [component] — [reason]
  Timing        — "sync" | "deferred"
Fill rule: one row per causal hop; dispatch chains show both source and target rows; implicit jumps prohibited
```

PASS condition: Block is labeled `TABLE-01 SCHEMA`, all five columns declared, fill rules stated.
FAIL if: Schema appears inline within §1 content generation; schema is unlabeled; schema is implied by output structure but never declared.

**Step P-2 — Declare TABLE-04 SCHEMA (C-19)**

Produce the following named block before writing any other content:

#### TABLE-04 SCHEMA: Re-render List (§4)
```
Column definitions:
  Component      — codebase component name, required
  Re-renders?    — "YES" | "NO" | "UNKNOWN"
  Reason         — prop/context/selector trigger name, or MISSING-LOADING; blank for NO rows
  Skip Mechanism — memoization mechanism for NO rows; blank for YES rows
  Upstream Ref   — §2 hop number or §3 state key; required for all rows including NO rows
Required tokens: UNKNOWN | MISSING-LOADING
Fill rule: every §2 component appears; memoized-skip components appear as NO rows — not absent
```

PASS condition: Block is labeled `TABLE-04 SCHEMA`, all five columns declared, tokens declared, fill rules stated.
FAIL if: Schema implied by output; not labeled; produced after first §4 row is written.

**Step P-3 — Produce Vocabulary Contract (C-14, C-16)**

Produce:

**§0 PART A — MAP TABLE**
| Framework Term | Neutral Equivalent |
Every framework-specific API, directive, primitive: MAP entry with neutral equivalent.

**§0 PART B — PASS-THROUGH TABLE**
| Pass-Through Name | Type |
Every codebase component name, handler name, selector, store slice, event name. These appear verbatim in §1–§7.

PASS condition: Both PART A and PART B present as labeled tables. PART B is the PASS-THROUGH designated section (not implied).
FAIL if: Only one part present; PART B omitted or folded into PART A without a separate labeled heading.

---

### GATE BLOCK (C-18)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE-VOCAB — REQUIRED BEFORE PROCEEDING TO TRACE CHECKLIST                 │
│                                                                              │
│  Inspect §0 PART A. For each MAP term: verify it will not appear in §1–§7   │
│  cell values (Handler, Owner, Component, Reason columns).                    │
│                                                                              │
│  If any MAP term would appear in §1–§7 cells:                                │
│    → State: GATE-VOCAB: FAIL — [term] | [planned section] | [column]         │
│    → Correct: update §0 PART A or the trace plan                             │
│    → Repeat gate until PASS                                                  │
│                                                                              │
│  Output required: [GATE-VOCAB: PASS — no MAP terms in §1–§7 cell space]      │
│                                                                              │
│  STOP. Do not begin Step T-1 until this token is output.                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### TRACE CHECKLIST

Execute steps T-1 through T-9 in order. Each step's FAIL condition is a criterion failure.

**Step T-1 — §1 Event Chain (C-01)**
Fill TABLE-01. Use Handler and Owner names from §0 PART B. Use Neutral Equivalents from §0 PART A.
PASS: Every causal hop present; no implicit jumps; UNKNOWN tokens used at gaps.
FAIL if: A handler named in §2 has no §1 row; a dispatch chain skips an intermediate step.

**Step T-2 — §2 Component Tree Traversal (C-02)**
| Hop | From | To | Direction | Carrier Name | Signal Type |
PASS: Every §1 component appears; Carrier Name (prop/callback/state key) present for every hop.
FAIL if: A §1 component absent from §2; Carrier Name blank.

**Step T-3 — §3 State Delta (C-03)**
| State Key / Slice | Before | After | Derived Selectors Affected |
PASS: Every state mutation has a row with before/after values; dependent selectors named.
FAIL if: A state change described in prose but not as a table row; Before or After blank without UNKNOWN token.

**Step T-4 — §4 Re-render List (C-04)**
Fill TABLE-04. Reference §0 PART B for Component names.
PASS: Every §2 component present; NO rows exist for evaluated-but-skipped components; Upstream Ref populated for every row.
FAIL if: A §2 component absent; a memoized-skip component absent; Upstream Ref blank.

**Step T-5 — §5 Side Effects (C-05)**
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref |
PASS: Both branches declared per async effect; MISSING-LOADING/MISSING-ERROR used for unconfirmed branches.
FAIL if: Async effect listed without both branch columns; unconfirmed branch silently omitted.

**Step T-6 — §6 Issue Analysis (C-06)**
Evaluate all four categories. State findings or explicit "None detected — §4/§5 rows [cite]".
PASS: All four categories present; "none detected" conclusions cite specific rows.
FAIL if: Any category absent; "none detected" without row citations.

**Step T-7 — §7 Final UI State (C-07)**
Describe observable state. Format: `"[Element] shows [state] — derived from §3 row '[key]'."` for every item.
PASS: Every UI change derives from a named §3 row; chain §1→§3→§4→§7 traceable.
FAIL if: A UI state item has no §3 derivation; derivation stated as prose without naming the §3 key.

**Step T-8 — §8 Framework Notes (C-09, C-13)**
| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
PASS: Every MAP entry from §0 PART A has a row; all framework terms isolated to this section.
FAIL if: A MAP term appears in §1–§7 with no §8 entry; framework mechanics absent.

**Step T-9 — §9 Optimization Opportunities (C-08)**
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
PASS: ≥1 entry with §4 citation; or explicit "None" citing all §4 NO rows.
FAIL if: Section absent; "None" without §4 row citations.

---

### POST-TRACE SEQUENCE

**Step A-1 — Completeness Stamp (C-15)**
Count: UNKNOWN: [N] | MISSING-LOADING: [N] | MISSING-ERROR: [N] | Issues flagged: [N]
Locations listed for every nonzero count.
PASS: Stamp present with all four categories; zero counts explicit ("0" not omitted).
FAIL if: Stamp absent; a token category omitted; zero counts silently absent.

**Step A-2 — Active Correction Protocol (C-17)**
Re-scan §1–§9 body. Verify each count token-by-token.
Discrepancy: `"Corrected: [CATEGORY] count [old]→[new]; found at [§N location]."`
Clean: `"Cross-checked: counts match body; no corrections required."`
PASS: Cross-check record present regardless of whether corrections were needed.
FAIL if: Step omitted; counts accepted without cross-check annotation.

**Step A-3 — Vocabulary Audit (C-13)**
Scan §1–§7. Report any MAP term leak or PASS-THROUGH alias violation. Report clean if none.
PASS: Every leak or alias violation reported; or affirmative "No leaks detected."
FAIL if: Step omitted.

**Step A-4 — Evidence Chain Audit (C-11)**
Verify: §7 cites ≥1 §3 row; §4 Upstream Ref populated per row; §5 Upstream Ref populated per row; §6 "none detected" conclusions cite rows.
Verdict: PASS if ≥2 of the four checks pass; FAIL — list missing links.
PASS: Verdict stated.
FAIL if: Step omitted.

---

## V-04 — Lifecycle Emphasis: Phase-Gated Pipeline with Hard-Stop Phase Gate

**Axis**: Lifecycle emphasis — the pipeline is organized as six named phases with explicit input/output contracts; C-18 is Phase 3 (a standalone named phase whose only output is the gate artifact); C-19 is Phase 1 (schema declarations only, no other output); no phase may begin until the previous phase's output artifact is complete.

**Hypothesis**: Making the gate a phase (not a role instruction or embedded step) elevates C-18 from guidance to structural — Phase 4 literally cannot begin until Phase 3 produces its GATE-VOCAB artifact. This parallels the way Phase 1 (schemas) and Phase 2 (contract) are separate phases: each phase has one output, and the pipeline is strictly sequential. Phase 1 producing only schemas (not contract) satisfies C-19 more cleanly than V-01 or V-02 where schemas and contract were produced by separate roles but in the same prompt session. Phase budgets prevent early phases from consuming token space needed by Phase 5 (trace) and Phase 6 (audit). Expected ceiling: 145–150/150.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Execute six phases in strict order. A phase is complete when it has produced its named output artifact. No phase begins until the previous phase is complete and its artifact is declared. Phase artifacts are visible to all subsequent phases.

---

### Phase 1 — Schema Declaration

**Input**: `{{topic}}` and `{{signal}}`
**Output artifact**: `SCHEMAS-ARTIFACT` containing TABLE-01 SCHEMA and TABLE-04 SCHEMA
**Constraint**: No vocabulary mapping, no trace content, no outlines for Phase 2+.

Produce SCHEMAS-ARTIFACT:

#### TABLE-01 SCHEMA: Event Chain (§1)
```
Columns: Step | Handler | Trigger | Owner | Timing
Handler values: codebase function name, or UNKNOWN: [name] — [reason]
Owner values: codebase component name, or UNKNOWN: [component] — [reason]
Timing values: "sync" | "deferred"
Required token: UNKNOWN: [name] — [reason]
Fill rule: one row per causal hop; A→B dispatch shows both rows with A in B's Trigger; no implicit jumps
```

#### TABLE-04 SCHEMA: Re-render List (§4)
```
Columns: Component | Re-renders? | Reason | Skip Mechanism | Upstream Ref
Component values: codebase component name (exact)
Re-renders? values: "YES" | "NO" | "UNKNOWN"
Reason values: "prop change: [name]" | "context change: [key]" | "selector: [name]" | MISSING-LOADING | blank (NO rows)
Skip Mechanism values: memoization mechanism name (NO rows); blank (YES/UNKNOWN rows)
Upstream Ref values: "§2 hop [N]" | "§3 row '[key]'" — required for all rows
Required tokens: UNKNOWN | MISSING-LOADING
Fill rule: every §2 component appears; memoized-skip components are NO rows — never absent
```

`SCHEMAS-ARTIFACT: COMPLETE`

---

### Phase 2 — Contract Declaration

**Input**: `SCHEMAS-ARTIFACT` from Phase 1
**Output artifact**: `CONTRACT-ARTIFACT` containing §0 PART A and §0 PART B
**Constraint**: No trace content, no gate output.

Produce CONTRACT-ARTIFACT:

**§0 PART A — MAP TABLE**
| Framework Term | Neutral Equivalent | Notes |
Every framework-specific API, directive, primitive, and reactive mechanism. Neutral Equivalent is the term used in §1–§7.

**§0 PART B — PASS-THROUGH TABLE**
| Pass-Through Name | Type | Notes |
Every codebase identifier that appears unchanged in §1–§7. Every name expected in TABLE-01 Handler/Owner columns and TABLE-04 Component column must have a row here.
Type: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`

**Binding**: §1–§7 bound to Neutral Equivalents (PART A) and exact PASS-THROUGH names (PART B). MAP terms appear only in §8.

`CONTRACT-ARTIFACT: COMPLETE`

---

### Phase 3 — Gate Phase (C-18 Hard Stop)

**Input**: `SCHEMAS-ARTIFACT` + `CONTRACT-ARTIFACT`
**Output artifact**: `GATE-ARTIFACT`
**Constraint**: No trace content. This phase's output unlocks Phase 4. Phase 4 cannot begin without `GATE-ARTIFACT: PASS`.

Execute GATE-VOCAB:

For each MAP term in CONTRACT-ARTIFACT §0 PART A: verify this term will not appear in §1–§7 cell values. Focus on the columns declared in SCHEMAS-ARTIFACT: Handler, Owner (TABLE-01), Component, Reason (TABLE-04).

Produce GATE-ARTIFACT:

```
GATE-VOCAB inspection:
  MAP terms reviewed: [list from PART A]
  Planned §1–§7 column value space: [Handler column values / Owner column values / Component column values]
  Violations found: [list each: term | section | column] or "none"

GATE-VOCAB result: PASS | FAIL

If FAIL: correction required —
  [Correction: changed [MAP term] → [corrected designation] in PART A / changed planned cell value [old] → [new]]
  Re-run gate: [new result]

Final result: GATE-VOCAB: PASS
```

`GATE-ARTIFACT: PASS` (Phase 4 unlocked) or `GATE-ARTIFACT: FAIL` (Phase 4 blocked — return to Phase 2)

---

### Phase 4 — Trace Generation

**Input**: `GATE-ARTIFACT: PASS` + `SCHEMAS-ARTIFACT` + `CONTRACT-ARTIFACT`
**Output artifact**: `TRACE-ARTIFACT` containing §1–§9
**Constraint**: Vocabulary binding active — MAP terms replaced by Neutral Equivalents in §1–§7; PASS-THROUGH names appear exactly as declared.

#### §1 Event Chain — fill TABLE-01 from SCHEMAS-ARTIFACT
#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Direction: `parent→child` | `child→parent` | `sibling`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every state update has a row. UNKNOWN for undetermined.

#### §4 Re-render List — fill TABLE-04 from SCHEMAS-ARTIFACT
Every §2 component has a row. Upstream Ref required.

#### §5 Side Effects and Async
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref |
Both branches per async effect. MISSING-LOADING / MISSING-ERROR for unconfirmed.

#### §6 Issue Analysis
All four categories — no omissions:
- **Unnecessary re-renders:** [finding] or `"None detected — §4 rows [cite]"`
- **Missing loading states:** [finding] or `"None detected — §5 rows [cite]"`
- **Error state gaps:** [finding] or `"None detected — §5 rows [cite]"`
- **Accessibility failures:** [finding] or `"None detected"`

#### §7 Final UI State
`"[Element] shows [state] — derived from §3 row '[key]'."` per item. Chain §1→§3→§4→§7 traceable.

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) | Framework mechanics note |
Only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
At least one entry or explicit "None" citing §4 NO rows.

`TRACE-ARTIFACT: COMPLETE`

---

### Phase 5 — Audit

**Input**: `TRACE-ARTIFACT` + `CONTRACT-ARTIFACT`
**Output artifact**: `AUDIT-ARTIFACT` containing §10–§12

#### §10 Completeness Stamp
```
UNKNOWN:         [N] — locations: [list]
MISSING-LOADING: [N] — locations: [list]
MISSING-ERROR:   [N] — locations: [list]
Issues flagged:  [N] — §6 named findings
```
Active correction: re-scan body token-by-token; `"Corrected: [CATEGORY] [old]→[new]; found at [§N location]."` or `"Cross-checked: counts match body; no corrections required."` Cross-check record required.

#### §11 Vocabulary Audit
Scan §1–§7 against CONTRACT-ARTIFACT PART A. Report each LEAK or ALIAS-VIOLATION or `"No leaks. No alias violations."`

#### §12 Evidence Chain Audit
1. §7 cites ≥1 §3 row? 2. §4 Upstream Ref per row? 3. §5 Upstream Ref per row? 4. §6 "none detected" cites rows?
**Verdict**: PASS if ≥2 checks pass; FAIL — list gaps.

`AUDIT-ARTIFACT: COMPLETE`

---

## V-05 — Combined: Trace Architecture Fusion + Inertia Framing + Evidence Chain Foregrounded

**Axis**: Combined — (a) Schema Architect and Contract Author fused into a single "TRACE ARCHITECTURE" role producing one named artifact containing both schemas and contract; (b) inertia framing opens the prompt with the failure mode ("what a trace-absent action review misses"); (c) evidence chain requirements are foregrounded as a parallel structural requirement in the Trace Author's instructions, not just a citation column in individual tables.

**Hypothesis**: V-01 and V-02 use five and four roles respectively. Role proliferation risks the model treating each role boundary as an opportunity to summarize prior output rather than build on it. Fusing Schema Architect and Contract Author into one "TRACE ARCHITECTURE" role reduces role boundaries while retaining both C-19 (named schema blocks) and C-14/C-16 (contract with PASS-THROUGH) in a single named artifact. The GATE-VOCAB check is embedded as the final step of the TRACE ARCHITECTURE role, satisfying C-18 before the architecture artifact is sealed. Opening with inertia framing ("without this trace, you learn: nothing") activates gap-detection reasoning from the first token. Foregrounding evidence chaining as a named "EVIDENCE CHAIN CONTRACT" (not just a column) means the Trace Author is explicitly bound to a chain obligation, not just a citation instruction. Expected ceiling: 148–150/150.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

---

### Inertia Frame

Without this trace, the action `{{signal}}` is a black box. A developer examining the UI sees: an element changes. Without the trace, they cannot answer: which handler fired? which state key changed? which component re-rendered? which components should have re-rendered but didn't? which async branch was never implemented?

The trace artifact exists to make these answers structurally unavoidable — each missing answer is a named token, not a silent gap.

---

### ROLE 1 — Trace Architect

Your sole output is the named `TRACE ARCHITECTURE` artifact. No trace content.

The TRACE ARCHITECTURE artifact has four parts declared in this order: schema for §1, schema for §4, vocabulary contract PART A, vocabulary contract PART B, and the GATE-VOCAB result. These parts are the complete output of this role.

#### TRACE ARCHITECTURE

**TABLE-01 SCHEMA: Event Chain (§1)**
```
Columns: Step | Handler | Trigger | Owner | Timing
Handler: codebase function name, or UNKNOWN: [name] — [reason]
Owner: codebase component name, or UNKNOWN: [component] — [reason]
Timing: "sync" | "deferred"
Required token: UNKNOWN: [name] — [reason]
Fill rule: one row per causal hop; dispatch chains show source and target rows; no implicit jumps
```

**TABLE-04 SCHEMA: Re-render List (§4)**
```
Columns: Component | Re-renders? | Reason | Skip Mechanism | Upstream Ref
Component: codebase component name (exact)
Re-renders?: "YES" | "NO" | "UNKNOWN"
Reason: "prop change: [name]" | "context change: [key]" | "selector: [name]" | MISSING-LOADING | blank (NO)
Skip Mechanism: memoization mechanism name (NO rows); blank otherwise
Upstream Ref: "§2 hop [N]" or "§3 row '[key]'" — required for every row including NO
Required tokens: UNKNOWN | MISSING-LOADING
Fill rule: every §2 component appears; evaluated-but-skipped components are NO rows — not absent
```

**§0 PART A — MAP TABLE**
| Framework Term | Neutral Equivalent | Notes |
Every framework API, directive, primitive, reactive mechanism. Neutral Equivalent used in §1–§7.

**§0 PART B — PASS-THROUGH TABLE**
| Pass-Through Name | Type | Notes |
Every codebase identifier appearing unchanged in §1–§7. Must include: every name expected in TABLE-01 Handler/Owner columns and TABLE-04 Component column. Type: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`. No PASS-THROUGH name is neutralized or aliased.

**EVIDENCE CHAIN CONTRACT**
The following citation obligations are binding on Role 2. These are not optional columns — they are structural requirements parallel to the schema fill rules:
- Every §4 row must populate Upstream Ref with a §2 hop number or §3 state key.
- Every §5 row must populate Upstream Ref with a §1 step number or §2 hop number.
- Every §7 item must name the §3 state key it derives from (format: `"§3 row '[key]'"`).
- Every §6 "none detected" conclusion must cite specific §4 or §5 rows.
Failure to satisfy any of these is a citation gap, not a formatting choice.

**GATE-VOCAB (C-18 embedded gate)**
Inspect §0 PART A. Verify no MAP term appears as a planned column value in §1–§7 (specifically in TABLE-01's Handler/Owner columns and TABLE-04's Component/Reason columns).

- `GATE-VOCAB: PASS — no MAP terms in §1–§7 column value space. TRACE ARCHITECTURE sealed.`
- `GATE-VOCAB: FAIL — [term | section | column]. Correcting: [action]. Re-checking.` (iterate until PASS)

`TRACE ARCHITECTURE: SEALED` (emitted after GATE-VOCAB: PASS)

**Role 2 may not begin until TRACE ARCHITECTURE: SEALED is output.**

---

### ROLE 2 — Trace Author

You receive `TRACE ARCHITECTURE: SEALED` from Role 1. Produce §1–§9 in full, in order.

**Active vocabulary binding**: Neutral Equivalents from PART A replace MAP terms in §1–§7. PASS-THROUGH names from PART B appear exactly as declared. MAP terms appear only in §8.

**Active evidence chain binding**: The EVIDENCE CHAIN CONTRACT from the TRACE ARCHITECTURE is a structural obligation. Upstream Ref, §3 derivation citations, and §6 row citations are not optional enhancements — they are fill requirements equivalent to the schema column rules.

#### §1 Event Chain
Fill TABLE-01 SCHEMA exactly. No columns added or removed. Every causal hop present. UNKNOWN tokens at gaps.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Carrier Name required (prop name, callback name, state key). Direction: `parent→child` | `child→parent` | `sibling`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every state mutation has a row with before/after values. Selectors named. UNKNOWN for undetermined.

#### §4 Re-render List
Fill TABLE-04 SCHEMA exactly. Every §2 component has a row. Upstream Ref populated for every row.

#### §5 Side Effects and Async
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref |
Both branches per async effect. MISSING-LOADING / MISSING-ERROR for unconfirmed branches. Upstream Ref: §1 step or §2 hop.

#### §6 Issue Analysis
All four categories — no omissions:
- **Unnecessary re-renders:** [Component — §4 row — nature — remediation] or `"None detected — §4 rows [cite specific rows]"`
- **Missing loading states:** [Component — §5 row — nature — remediation] or `"None detected — §5 rows [cite specific rows]"`
- **Error state gaps:** [Component — §5 row — nature — remediation] or `"None detected — §5 rows [cite specific rows]"`
- **Accessibility failures:** [Element — nature — remediation] or `"None detected"`

#### §7 Final UI State
Describe observable state after `{{signal}}` fully resolves. Per item: `"[Element] shows [state] — derived from §3 row '[state key]'."` Chain §1→§3→§4→§7 traceable by reference throughout.

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
Every PART A MAP entry. Only section where MAP terms appear. Framework-specific lifecycle, reactivity, compiler behavior.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
Types: `memoization candidate` | `batching opportunity` | `render-scope reduction`
At least one entry. If none: `"No optimization opportunities — component tree correctly scoped per §4 rows [list all NO rows]."`

---

### ROLE 3 — Auditor

You receive the full output of Roles 1–2. Produce §10–§12.

#### §10 Completeness Stamp
```
UNKNOWN:         [N] — locations: [§ reference — row/step identifier for each instance]
MISSING-LOADING: [N] — locations: [§ reference — row/step identifier for each instance]
MISSING-ERROR:   [N] — locations: [§ reference — row/step identifier for each instance]
Issues flagged:  [N] — §6 categories with named findings (not "none detected")
```

Active correction protocol — required:
1. Re-scan §1–§9 token-by-token and verify each count against the body.
2. Discrepancy: `"Corrected: [CATEGORY] count [old]→[new]; found additional [TOKEN] at [§N — row/step identifier]."`
3. No discrepancy: `"Cross-checked: counts match body; no corrections required."`
Cross-check record required regardless of outcome.

#### §11 Vocabulary Audit
Scan §1–§7 for PART A MAP term leaks or PART B PASS-THROUGH alias violations.
- Leak: `LEAK: "[term]" at §N [row/step identifier — column]`
- Alias violation: `ALIAS-VIOLATION: "[codebase name]" aliased to "[alias]" at §N`
- Clean: `"No vocabulary leaks detected. No alias violations detected."`

#### §12 Evidence Chain Audit
Verify EVIDENCE CHAIN CONTRACT from TRACE ARCHITECTURE:
1. §7 cites ≥1 named §3 row? [YES — cite example / NO]
2. §4 Upstream Ref populated for every row? [YES / NO — list rows missing citations]
3. §5 Upstream Ref populated for every row? [YES / NO — list rows missing citations]
4. §6 "none detected" conclusions cite specific §4 or §5 rows? [YES — cite example / NO — list unsupported]

**Verdict**: PASS if ≥2 of the four chain requirements satisfied; FAIL — list missing links.

---

## Variation Map Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event chain complete | PASS | PASS | PASS | PASS | PASS |
| C-02 Component tree traversal | PASS | PASS | PASS | PASS | PASS |
| C-03 State delta | PASS | PASS | PASS | PASS | PASS |
| C-04 Re-render list | PASS | PASS | PASS | PASS | PASS |
| C-05 Side effects | PASS | PASS | PASS | PASS | PASS |
| C-06 Issue flags | PASS | PASS | PASS | PASS | PASS |
| C-07 Final UI state | PASS | PASS | PASS | PASS | PASS |
| C-08 Optimization | PASS | PASS | PASS | PASS | PASS |
| C-09 Framework-portable annotations | PASS | PASS | PASS | PASS | PASS |
| C-10 Gap-visible format | PASS | PASS | PASS | PASS | PASS |
| C-11 Evidence chaining | PASS | PASS | PASS | PASS | PASS |
| C-12 Incompleteness tokens | PASS | PASS | PASS | PASS | PASS |
| C-13 Framework-neutral core enforcement | PASS | PASS | PASS | PASS | PASS |
| C-14 Vocabulary contract artifact | PASS | PASS | PASS | PASS | PASS |
| C-15 Machine-readable completeness inventory | PASS | PASS | PASS | PASS | PASS |
| C-16 PASS-THROUGH designation | PASS | PASS | PASS | PASS | PASS |
| C-17 Stamp with active correction | PASS | PASS | PASS | PASS | PASS |
| C-18 Role-level enforcement gate | PASS | PASS | PASS | PASS | PASS |
| C-19 Pre-declared named column schemas | PASS | PASS | PASS | PASS | PASS |
| **Structural differentiator** | Schema-first 5-role | Contract-first 4-role | Imperative STOP block | Phase-gate hard stop | TA fusion + inertia framing |

**Key differentiators for C-18 and C-19 across variations:**

| | C-18 mechanism | C-19 mechanism |
|--|----------------|----------------|
| V-01 | Standalone Role 3 (Gate) — outputs GATE-VOCAB token; Role 4 blocked until PASS | Standalone Role 1 (Schema Architect) — sole output is TABLE-01 SCHEMA + TABLE-04 SCHEMA |
| V-02 | Embedded as Step 2c in Role 2 (Schema Architect) — declared inline within schema role before PASS emitted | Role 2 declares schemas after contract; schemas use neutral column names drawn from PART A |
| V-03 | Boxed STOP BLOCK with explicit token `[GATE-VOCAB: PASS]` required; flat prompt; no role machinery | Two-step PRE-FLIGHT: Step P-1 (TABLE-01 SCHEMA) and Step P-2 (TABLE-04 SCHEMA) before any other work |
| V-04 | Phase 3 is the gate — standalone phase whose only output is GATE-ARTIFACT; Phase 4 gated on GATE-ARTIFACT: PASS | Phase 1 is schemas only — standalone phase whose only output is SCHEMAS-ARTIFACT |
| V-05 | Embedded as final step of TRACE ARCHITECTURE role — TRACE ARCHITECTURE: SEALED emitted only after GATE-VOCAB: PASS | TABLE-01 SCHEMA and TABLE-04 SCHEMA declared as first two blocks within the TRACE ARCHITECTURE artifact |
