# trace-component — R8 Variations (v7 rubric)

**Round**: 8
**Rubric ceiling**: 160 pts (C-01 through C-21)
**Rubric file**: `simulations/quest/rubrics/trace-component-rubric-v7-2026-03-15.md`

**R7 baseline summary:**
- All R6 patterns (C-01 through C-19) established in full; R6 V-05 introduced the TRACE ARCHITECTURE fusion artifact (schemas + vocabulary contract + embedded GATE-VOCAB) with a single TRACE ARCHITECTURE: SEALED completion token. V-05 also introduced the EVIDENCE CHAIN CONTRACT block inside TRACE ARCHITECTURE, making it the first variation to exhibit both C-20 and C-21 patterns before they were criteria.
- C-20 (pre-declared evidence chain contract): The ECC must be a named block declared before trace content, specifying every required derivation pair, so the generating role fills against declared obligations rather than incidentally producing citations, and the audit role checks compliance against the declared contract rather than constructing its own checklist.
- C-21 (unified pre-trace architecture seal): All pre-trace artifacts (schemas, vocabulary contract, enforcement gate — plus by extension the ECC) unified into ONE named architecture artifact with ONE completion token. Separate artifacts with separate blocking conditions do not satisfy this criterion even if all artifacts are present.

**New v7 criteria:**
- **C-20**: Evidence chain contract declared as named block before any trace content. Specifies every upstream→downstream derivation pair. Audit role checks compliance against the declared contract. Generating role fills against declared obligations.
- **C-21**: Single named architecture artifact that unifies all pre-trace artifacts (C-19 schemas + C-14 vocabulary contract + C-18 gate). Emits ONE completion token. All trace-generating roles blocked by that single token.

**R8 variation axes chosen (3 single-axis + 2 combined):**
1. **Role sequence** — ECC as dedicated first artifact; Schema Architect embeds ECC obligation IDs in fill rules, creating bidirectional binding between contract and schema structure.
2. **Output format** — ECC as a formal obligation table with named columns (OBL-ID, Downstream, Must Cite, Source Section); obligation IDs appear in schema fill rules and section instructions so the audit role fills a compliance column against pre-declared rows.
3. **Phrasing register** — ECC as imperative contract clauses with named violation types (CITATION-GAP, DERIVATION-BREAK, UNSUPPORTED-CONCLUSION); less role machinery, more atomic enforcement language; TRACE ARCHITECTURE: SEALED emitted by a flat pre-trace phase rather than a dedicated role.
4. **Role sequence + Output format** (combined) — ECC-first role ordering combined with the formal obligation table format; obligation IDs appear in schema columns, enabling mechanical audit compliance.
5. **All three axes** (combined) — ECC-first ordering + formal obligation table + imperative violation typing + explicit sub-artifact inventory in the seal token.

**R8 variation map:**

| Variation | Axis | C-20 | C-21 | C-18 | C-19 | C-14 | C-16 | C-17 | Hypothesis |
|-----------|------|------|------|------|------|------|------|------|------------|
| V-01 | Role sequence (ECC-first) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ECC produced before schemas; schema fill rules embed ECC obligation IDs; bidirectional binding ensures generating role and audit role share the same obligation reference frame |
| V-02 | Output format (compliance table) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ECC as formal obligation table with OBL-IDs; audit role fills compliance columns against pre-declared rows; section instructions reference OBL-IDs by number |
| V-03 | Phrasing register (imperative + violation types) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Imperative contract clauses with CITATION-GAP / DERIVATION-BREAK violation types; flat pre-trace phase; TRACE ARCHITECTURE: SEALED emitted after inline checklist, not by a role boundary |
| V-04 | Role sequence + Output format | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ECC-first ordering + compliance table: ECC rows exist as named artifacts before schemas reference them; audit compliance is mechanical checkbox completion |
| V-05 | All three axes | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Full synthesis: ECC-first role + obligation table with violation types + explicit sub-artifact inventory in seal token; maximum binding density for C-20 and C-21 |

---

## V-01 — Role Sequence: Evidence Chain Contract First

**Axis**: Role sequence — a dedicated Evidence Architect role produces the Evidence Chain Contract as the first and only pre-trace artifact before any schema or vocabulary work begins. The Schema + Contract Author role embeds ECC obligation IDs in the schema fill rules. The Gate role emits TRACE ARCHITECTURE: SEALED only after all four pre-trace artifacts are confirmed present.

**Hypothesis**: In R6 V-05, the EVIDENCE CHAIN CONTRACT was the last sub-artifact inside TRACE ARCHITECTURE — declared after schemas and vocabulary contract. As a consequence, the schema fill rules could not reference ECC obligations, and the generating role received two parallel binding sets (schema fill rules + ECC obligations) with no structural cross-link. V-01 inverts this: the Evidence Architect produces the ECC first, and the Schema + Contract Author role explicitly references ECC obligation IDs in each schema's fill rules (e.g., "Upstream Ref — satisfies OBL-02, OBL-03"). The result is a single binding frame: each schema column is annotated with the ECC obligation it covers, and the audit role checks compliance by column, not by cross-referencing two separate artifacts. Expected ceiling: 155–160/160.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. No role may produce trace content, downstream artifacts, or structural hints. Role output is visible to all subsequent roles.

---

### ROLE 1 — Evidence Architect

Your sole output is the EVIDENCE CHAIN CONTRACT artifact. No schemas, no vocabulary contract, no trace content.

#### EVIDENCE CHAIN CONTRACT

This contract declares every required upstream-to-downstream derivation pair for this trace. The generating role (Role 3) fills against these obligations. The audit role (Role 5) checks compliance against this contract — not by constructing its own checklist.

| OBL-ID | Downstream Section | Required Citation | Source Section | Violation if Missing |
|--------|--------------------|-------------------|----------------|---------------------|
| OBL-01 | §4 Re-render List — every row | Upstream Ref: §2 hop number OR §3 state key | §2 Component Tree / §3 State Delta | CITATION-GAP: §4 row without §2 or §3 reference |
| OBL-02 | §5 Side Effects — every row | Upstream Ref: §1 step number OR §2 hop number | §1 Event Chain / §2 Component Tree | CITATION-GAP: §5 row without §1 or §2 reference |
| OBL-03 | §7 Final UI State — every item | Named §3 state key — format: `"§3 row '[key]'"` | §3 State Delta | DERIVATION-BREAK: §7 item without §3 derivation citation |
| OBL-04 | §7 Final UI State — derivation chain | §4 row traceable from each §7 item | §4 Re-render List | DERIVATION-BREAK: §7 → §4 chain gap |
| OBL-05 | §6 Issue Flags — every "none detected" | Cited §4 or §5 rows supporting the conclusion | §4 Re-render List / §5 Side Effects | UNSUPPORTED-CONCLUSION: "none detected" without row citation |
| OBL-06 | §6 Issue Flags — every named issue | Named §2 component | §2 Component Tree | CITATION-GAP: issue without §2 component reference |

`EVIDENCE CHAIN CONTRACT: DECLARED`

**Do not produce any schema, vocabulary contract, gate output, or trace content. The EVIDENCE CHAIN CONTRACT is the complete output of Role 1.**

---

### ROLE 2 — Schema Architect

You receive the EVIDENCE CHAIN CONTRACT from Role 1. Produce two named schema blocks. Embed relevant OBL-IDs in schema fill rules to create bidirectional binding between contract obligations and schema structure. No vocabulary contract, no trace content.

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns:
  Step       — Sequential integer. Required for every row.
  Handler    — Exact codebase name. UNKNOWN: [name] — [reason] if undetermined.
  Trigger    — The user action {{signal}} (step 1) or upstream step/dispatch that caused this handler.
  Owner      — Exact codebase component name. UNKNOWN: [component] — [reason] if undetermined.
  Timing     — "sync" | "deferred"

Required tokens:
  UNKNOWN: [name] — [reason]   (handler or owner that cannot be determined)

Fill rules:
  1. Every causal hop from user action to final UI effect occupies one row.
  2. If Handler A dispatches to Handler B, both rows are present; Handler A's step appears in Handler B's Trigger.
  3. An implicit jump between steps is a schema violation.
  4. Step numbers must appear in §5 Upstream Ref per OBL-02.
  5. Step numbers must appear in §4 Upstream Ref where the handler owns a state change (OBL-01 cross-ref).
```

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns:
  Component      — Exact codebase name. Required. (PASS-THROUGH name from §0 PART B)
  Re-renders?    — "YES" | "NO" | "UNKNOWN"
  Reason         — Prop change (name), context change (key), selector subscription (name).
                   MISSING-LOADING if loading-branch re-render unconfirmed.
                   Blank only for NO rows.
  Skip Mechanism — Memoization mechanism for NO rows. Blank for YES rows.
  Upstream Ref   — §2 hop number OR §3 state key [satisfies OBL-01]

Required tokens:
  UNKNOWN          (Re-renders? column — re-render status undetermined)
  MISSING-LOADING  (Reason column — loading branch re-render unconfirmed)

Fill rules:
  1. Every component named in §2 must appear. Silent omission is a schema violation.
  2. Memoized/skipped components appear as NO rows — not absent.
  3. Upstream Ref is required for every row including NO rows [OBL-01].
  4. Row content must support or be cited by §7 items per OBL-04.
```

`TABLE SCHEMAS: DECLARED`

**Do not produce any vocabulary contract, gate output, or trace content.**

---

### ROLE 3 — Contract Author

You receive the EVIDENCE CHAIN CONTRACT and TABLE SCHEMAS from Roles 1–2. Produce §0 Vocabulary Contract. No trace content.

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Map every framework-specific API, directive, decorator, or reactive primitive present in the codebase context. Neutral Equivalent is used in §1–§7 core sections. Framework Term appears only in §8.

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Notes |
|------------------|------|-------|

Every codebase identifier that must appear unchanged in §1–§7 for source navigability. Required entries:
- Every name expected in TABLE-01's Handler and Owner columns
- Every name expected in TABLE-04's Component column
- Every selector name, store slice key, context key

Type: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`

No PASS-THROUGH name may be neutralized or aliased. Framework primitives are MAP by default; codebase identifiers are PASS-THROUGH by default.

**Binding declaration**: §1–§7 bound to Neutral Equivalents (PART A) and exact PASS-THROUGH names (PART B). MAP terms appear only in §8.

`VOCABULARY CONTRACT: DECLARED`

**Do not produce any gate output or trace content.**

---

### ROLE 4 — Architecture Gate

You receive EVIDENCE CHAIN CONTRACT, TABLE SCHEMAS, and VOCABULARY CONTRACT from Roles 1–3. Perform two checks and emit the unified seal.

**Check 1 — GATE-VOCAB**

For every MAP term in §0 PART A: verify it does not appear as a planned column value in TABLE-01 columns (Handler, Owner) or TABLE-04 columns (Component, Reason).

```
GATE-VOCAB inspection:
  MAP terms reviewed: [list from PART A]
  Column value space reviewed: TABLE-01 Handler/Owner | TABLE-04 Component/Reason
  Violations: [MAP term | planned column | cell context] OR "none detected"

GATE-VOCAB result: PASS | FAIL
```

If FAIL: correct §0 PART A. Document correction: `"Correction: [term] reclassified MAP→PASS-THROUGH / cell value [old] → [new]."` Re-run until PASS.

**Check 2 — ARCHITECTURE INVENTORY**

Verify all four pre-trace artifacts are present and complete:
- EVIDENCE CHAIN CONTRACT: DECLARED ✓
- TABLE SCHEMAS: DECLARED ✓
- VOCABULARY CONTRACT: DECLARED ✓
- GATE-VOCAB: PASS ✓

If all four pass:

`TRACE ARCHITECTURE: SEALED — artifacts: ECC (6 obligations), TABLE-01 SCHEMA, TABLE-04 SCHEMA, §0 PART A (N terms), §0 PART B (M names), GATE-VOCAB: PASS`

**Role 5 may not begin until TRACE ARCHITECTURE: SEALED is output.**

---

### ROLE 5 — Trace Author

You receive `TRACE ARCHITECTURE: SEALED`. Produce §1–§9 in full.

**Active bindings**:
- Vocabulary: Neutral Equivalents from §0 PART A replace MAP terms in §1–§7. PASS-THROUGH names from §0 PART B appear exactly as declared. MAP terms appear only in §8.
- Evidence chain: The EVIDENCE CHAIN CONTRACT is a structural obligation. OBL-01 through OBL-06 are fill requirements equivalent to schema column rules — not optional enhancements.

**Pre-output gate check**: Before generating §1, confirm no MAP term from §0 PART A will appear in §1–§7 cell values. State: `GATE CHECK: PASS — no MAP terms in §1–§7 column value space.`

#### §1 Event Chain

Fill TABLE-01 SCHEMA exactly. No columns added or removed. Every causal hop present. UNKNOWN tokens at gaps.

#### §2 Component Tree Traversal

| Hop | From | To | Direction | Carrier Name | Signal Type |
|-----|------|----|-----------|--------------|-------------|

Every component from §1 present. Carrier Name required (prop, callback, state key). Direction: `parent→child` | `child→parent` | `sibling`. Signal Type: `props` | `callback` | `shared state` | `context`.

#### §3 State Delta

| State Key / Slice | Before | After | Derived Selectors Affected |
|------------------|--------|-------|---------------------------|

Every state mutation has a row. Keys named as PASS-THROUGH. Undetermined: `UNKNOWN: [key] — [reason]`.

#### §4 Re-render List

Fill TABLE-04 SCHEMA exactly. Every §2 component has a row. Upstream Ref populated per OBL-01.

#### §5 Side Effects and Async

| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref [OBL-02] |
|--------|-------|-------|----------------|-------------|----------------------|

Both branches declared per async effect. Unconfirmed: `MISSING-LOADING: [reason]` / `MISSING-ERROR: [reason]`. Upstream Ref: §1 step or §2 hop per OBL-02.

#### §6 Issue Analysis

All four categories — no omissions.

**Unnecessary re-renders:** Finding [Component — §4 row — nature — remediation] or `"None detected — §4 rows [cite rows]"` [OBL-05]
**Missing loading states:** Finding or `"None detected — §5 rows [cite rows]"` [OBL-05]
**Error state gaps:** Finding or `"None detected — §5 rows [cite rows]"` [OBL-05]
**Accessibility failures:** Finding [Element — nature — remediation] or `"None detected"`

Named issues cite §2 component per OBL-06. "None detected" conclusions cite specific §4 or §5 rows per OBL-05.

#### §7 Final UI State

Observable state after `{{signal}}` fully resolves. Per item:

`"[Element] shows [state] — derived from §3 row '[state key]' [OBL-03], traceable via §4 row '[component]' [OBL-04]."`

Both derivation citations required per OBL-03 and OBL-04.

#### §8 Framework Notes

| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
|---------------|-------------------|----------------------|--------------------------|

Every PART A MAP entry. Only section where MAP terms appear.

#### §9 Optimization Opportunities

| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
|-----------------|------|-----------------|--------------------------|-------------|

Types: `memoization candidate` | `batching opportunity` | `render-scope reduction`
At least one entry. If none: `"No optimization opportunities — §4 NO rows: [list]."` Citing zero rows when NO rows exist is a failure.

---

### ROLE 6 — Auditor

You receive the full output of Roles 1–5. Produce §10–§12.

#### §10 Completeness Stamp

```
UNKNOWN:         [N] — locations: [§ ref and row/step identifier for each]
MISSING-LOADING: [N] — locations: [§ ref and row/step identifier for each]
MISSING-ERROR:   [N] — locations: [§ ref and row/step identifier for each]
Issues flagged:  [N] — named §6 findings (exclude "none detected")
```

Active correction protocol:
1. Re-scan §1–§9 token-by-token; verify each count.
2. Discrepancy: `"Corrected: [CATEGORY] [old]→[new]; found at [§N — row/step identifier]."`
3. Match: `"Cross-checked: counts match body; no corrections required."`
Cross-check record required regardless of outcome.

#### §11 Vocabulary Audit

Scan §1–§7 for §0 PART A MAP term leaks or PART B alias violations.
- Leak: `LEAK: "[term]" at §N [row/step — column]`
- Alias violation: `ALIAS-VIOLATION: "[name]" aliased to "[alias]" at §N`
- Clean: `"No vocabulary leaks. No alias violations."`

#### §12 Evidence Chain Compliance

Check each EVIDENCE CHAIN CONTRACT obligation:

| OBL-ID | Obligation | Result | Evidence / Violation location |
|--------|-----------|--------|-------------------------------|
| OBL-01 | §4 Upstream Ref per row | PASS / FAIL | Cite compliant rows or list gaps |
| OBL-02 | §5 Upstream Ref per row | PASS / FAIL | Cite compliant rows or list gaps |
| OBL-03 | §7 cites §3 key per item | PASS / FAIL | Cite compliant items or list gaps |
| OBL-04 | §7 traces to §4 row per item | PASS / FAIL | Cite compliant items or list gaps |
| OBL-05 | §6 "none detected" cites §4/§5 | PASS / FAIL | Cite compliant conclusions or list gaps |
| OBL-06 | §6 named issues cite §2 component | PASS / FAIL | Cite compliant issues or list gaps |

**Verdict**: PASS (≥4 of 6 obligations satisfied) / FAIL — list unsatisfied obligations.

---

## V-02 — Output Format: ECC as Two-Column Compliance Table

**Axis**: Output format — the Evidence Chain Contract uses a formal obligation table with an explicit OBL-ID column and a COMPLIANCE column that is blank at declaration time. The trace-generating role receives the obligation table with its compliance column empty and is instructed to populate each section in a way that fills those obligations. The audit role receives the same table and fills the COMPLIANCE column — transforming evidence chain audit from interpretive assessment into mechanical row-by-row verification. All pre-trace artifacts remain unified in one TRACE ARCHITECTURE artifact (satisfying C-21); the ECC table format is the distinguishing feature.

**Hypothesis**: V-01's ECC is a narrative table that the audit role must interpret — it reads the obligations and then decides whether the trace body satisfies them. V-02 makes the ECC a two-pass artifact: the generating role and audit role share the same table structure, with the generating role filling evidence and the audit role filling compliance. This eliminates interpretive variance: an obligation is either satisfied (PASS) or not (FAIL — location cited). Combined with a flat 3-role structure (TRACE ARCHITECTURE role → Trace Author → Auditor), the prompt is shorter while the audit mechanism is tighter. Expected ceiling: 153–158/160.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. Role output is visible to all subsequent roles.

---

### ROLE 1 — Trace Architect

Your sole output is the named `TRACE ARCHITECTURE` artifact. No trace content.

The TRACE ARCHITECTURE artifact contains five parts in this order: EVIDENCE CHAIN CONTRACT, TABLE-01 SCHEMA, TABLE-04 SCHEMA, §0 Vocabulary Contract, and GATE-VOCAB result. The artifact ends with `TRACE ARCHITECTURE: SEALED` after GATE-VOCAB: PASS.

#### EVIDENCE CHAIN CONTRACT

The following obligation table is a pre-declared contract. The generating role (Role 2) fills against these obligations. The audit role (Role 3) fills the COMPLIANCE column against this table.

| OBL-ID | Downstream Section | Required Citation | Source | Violation Type if Missing |
|--------|--------------------|-------------------|--------|--------------------------|
| OBL-01 | §4 — every row | Upstream Ref: §2 hop OR §3 key | §2 / §3 | CITATION-GAP |
| OBL-02 | §5 — every row | Upstream Ref: §1 step OR §2 hop | §1 / §2 | CITATION-GAP |
| OBL-03 | §7 — every item | Cites named §3 key: `"§3 row '[key]'"` | §3 | DERIVATION-BREAK |
| OBL-04 | §7 — every item | Traceable to §4 row | §4 | DERIVATION-BREAK |
| OBL-05 | §6 — every "none detected" | Cites specific §4 or §5 rows | §4 / §5 | UNSUPPORTED-CONCLUSION |
| OBL-06 | §6 — every named issue | Names §2 component | §2 | CITATION-GAP |

`EVIDENCE CHAIN CONTRACT: DECLARED`

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns: Step | Handler | Trigger | Owner | Timing
Handler: exact codebase name, or UNKNOWN: [name] — [reason]
Owner: exact codebase component name, or UNKNOWN: [component] — [reason]
Timing: "sync" | "deferred"
Required token: UNKNOWN: [name] — [reason]
Fill rule: every causal hop present; dispatch chains show source and target rows; no implicit jumps;
           step numbers cited in §5 Upstream Ref (OBL-02)
```

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns: Component | Re-renders? | Reason | Skip Mechanism | Upstream Ref
Component: exact codebase name (PASS-THROUGH)
Re-renders?: "YES" | "NO" | "UNKNOWN"
Reason: prop change (name) | context change (key) | selector (name) | MISSING-LOADING | blank (NO)
Skip Mechanism: memoization mechanism name (NO rows); blank otherwise
Upstream Ref: §2 hop number OR §3 state key — required every row including NO [satisfies OBL-01]
Required tokens: UNKNOWN | MISSING-LOADING
Fill rule: every §2 component appears; evaluated-and-skipped = NO row, not absent
```

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Map every framework-specific API, directive, primitive, reactive mechanism. Neutral Equivalent used in §1–§7.

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Notes |
|------------------|------|-------|

Every codebase identifier appearing unchanged in §1–§7. Required: all TABLE-01 Handler/Owner values, all TABLE-04 Component values, all selector names, store slice keys, context keys.
Type: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`
No PASS-THROUGH name is neutralized. No MAP alias invented for a codebase identifier.

**Binding**: §1–§7 bound to Neutral Equivalents (PART A) and exact PASS-THROUGH names (PART B). MAP terms appear only in §8.

#### GATE-VOCAB

Inspect §0 PART A MAP terms against planned column values in TABLE-01 (Handler, Owner) and TABLE-04 (Component, Reason).

```
MAP terms reviewed: [list]
Planned column value space reviewed: [list Handler/Owner/Component/Reason values]
Violations: [MAP term | column | cell context] OR "none detected"
GATE-VOCAB result: PASS | FAIL
```

If FAIL: correct §0 PART A; document correction; re-run gate. Iterate until PASS.

`TRACE ARCHITECTURE: SEALED` (emitted after GATE-VOCAB: PASS)

**Role 2 may not begin until TRACE ARCHITECTURE: SEALED is output.**

---

### ROLE 2 — Trace Author

You receive `TRACE ARCHITECTURE: SEALED`. Produce §1–§9.

**Active bindings**: Neutral Equivalents from PART A replace MAP terms in §1–§7. PASS-THROUGH names from PART B appear exactly as declared. MAP terms appear only in §8.

**Evidence chain binding**: The EVIDENCE CHAIN CONTRACT is a fill obligation. OBL-01 through OBL-06 are structural requirements. Non-compliance is a CITATION-GAP, DERIVATION-BREAK, or UNSUPPORTED-CONCLUSION — not a formatting choice.

**Pre-output gate**: Before §1, state: `GATE CHECK: PASS — no MAP terms in §1–§7 planned column values.`

#### §1 Event Chain
Fill TABLE-01 SCHEMA exactly. UNKNOWN tokens at gaps.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Carrier Name required. Direction: `parent→child` | `child→parent` | `sibling`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every state mutation has a row. UNKNOWN for undetermined.

#### §4 Re-render List
Fill TABLE-04 SCHEMA exactly. Every §2 component present. Upstream Ref per OBL-01.

#### §5 Side Effects and Async
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref [OBL-02] |
Both branches per async effect. MISSING-LOADING / MISSING-ERROR for unconfirmed. Upstream Ref per OBL-02.

#### §6 Issue Analysis
All four categories — no omissions.
- **Unnecessary re-renders**: Finding [Component — §4 row — nature — remediation] or `"None detected — §4 rows [N, N]"` [OBL-05; OBL-06 if issue found]
- **Missing loading states**: Finding or `"None detected — §5 rows [N, N]"` [OBL-05]
- **Error state gaps**: Finding or `"None detected — §5 rows [N, N]"` [OBL-05]
- **Accessibility failures**: Finding or `"None detected"`

#### §7 Final UI State
Per item: `"[Element] shows [state] — derived from §3 row '[key]' [OBL-03]; traceable via §4 row '[component]' [OBL-04]."`

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
Every PART A MAP entry. Only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
Types: `memoization candidate` | `batching opportunity` | `render-scope reduction`
At least one entry or explicit "None — §4 NO rows: [list]."

---

### ROLE 3 — Auditor

You receive the full output of Roles 1–2. Produce §10–§12.

#### §10 Completeness Stamp

```
UNKNOWN:         [N] — locations: [list]
MISSING-LOADING: [N] — locations: [list]
MISSING-ERROR:   [N] — locations: [list]
Issues flagged:  [N] — named §6 findings only
```

Active correction: re-scan §1–§9; verify counts. Discrepancy: `"Corrected: [CATEGORY] [old]→[new]; at [§N location]."` Match: `"Cross-checked: no corrections required."` Record required regardless.

#### §11 Vocabulary Audit

Scan §1–§7 for PART A MAP leaks or PART B alias violations. Report each or: `"No leaks. No alias violations."`

#### §12 Evidence Chain Compliance

Fill the COMPLIANCE column for each ECC obligation:

| OBL-ID | Obligation (from EVIDENCE CHAIN CONTRACT) | COMPLIANCE | Evidence or Violation Location |
|--------|------------------------------------------|------------|-------------------------------|
| OBL-01 | §4 Upstream Ref per row | PASS / FAIL | |
| OBL-02 | §5 Upstream Ref per row | PASS / FAIL | |
| OBL-03 | §7 cites §3 key per item | PASS / FAIL | |
| OBL-04 | §7 traces to §4 row per item | PASS / FAIL | |
| OBL-05 | §6 "none detected" cites rows | PASS / FAIL | |
| OBL-06 | §6 named issues cite §2 component | PASS / FAIL | |

**Verdict**: PASS (≥4 PASS) / FAIL — list FAIL obligations.

---

## V-03 — Phrasing Register: Imperative Contract Clauses with Violation Types

**Axis**: Phrasing register — the pre-trace phase is a flat sequence of named blocks (no role machinery; no role-level blocking tokens between blocks). The Evidence Chain Contract uses SHALL/MUST imperative language with named violation types. The TRACE ARCHITECTURE: SEALED token is emitted by an inline architecture checklist after all blocks are complete, not by a role transition.

**Hypothesis**: V-01 and V-02 use multi-role pipelines (5 and 3 roles respectively). Role boundary machinery requires the model to maintain role identity and blocking conditions across transitions — which can introduce summarization or context loss at role boundaries. V-03 tests whether a flat prompt with the same structural completeness (ECC pre-declared, schemas named, vocabulary contract with PASS-THROUGH, GATE-VOCAB, unified seal) can achieve equivalent or higher criteria coverage through imperative language density rather than role-boundary enforcement. The SHALL/MUST/VIOLATION framing activates precision language in the generating pass. Expected ceiling: 148–155/160 (slight risk on C-18 if "role-level gate" is read strictly as requiring a role boundary, not just a named blocking step).

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

---

### PRE-TRACE PHASE

Complete all blocks in this phase in order. No trace content of any kind may appear until `TRACE ARCHITECTURE: SEALED` is emitted at the end of this phase.

---

**BLOCK 1 — EVIDENCE CHAIN CONTRACT**

Declare the following obligations before any trace content. This contract is binding on all trace sections.

| OBL-ID | Downstream | SHALL | Source | Violation if Absent |
|--------|-----------|-------|--------|---------------------|
| OBL-01 | §4 every row | carry Upstream Ref: §2 hop OR §3 key | §2 / §3 | CITATION-GAP |
| OBL-02 | §5 every row | carry Upstream Ref: §1 step OR §2 hop | §1 / §2 | CITATION-GAP |
| OBL-03 | §7 every item | name §3 state key: `"§3 row '[key]'"` | §3 | DERIVATION-BREAK |
| OBL-04 | §7 every item | trace to §4 row | §4 | DERIVATION-BREAK |
| OBL-05 | §6 "none detected" | cite §4 or §5 rows | §4 / §5 | UNSUPPORTED-CONCLUSION |
| OBL-06 | §6 named issues | name §2 component | §2 | CITATION-GAP |

`EVIDENCE CHAIN CONTRACT: DECLARED`

---

**BLOCK 2 — TABLE-01 SCHEMA: Event Chain (§1)**

```
Columns: Step | Handler | Trigger | Owner | Timing
Handler: exact codebase name SHALL be used. UNKNOWN: [name] — [reason] MUST occupy the row if undetermined.
Owner: exact codebase component name. UNKNOWN: [component] — [reason] if undetermined.
Timing: "sync" | "deferred". MUST appear for every row.
Required token: UNKNOWN: [name] — [reason]
Fill rules:
  1. Every causal hop SHALL occupy one row. Dispatch chains MUST show both source and target rows.
  2. An implicit jump between consecutive steps is a SCHEMA-VIOLATION.
  3. Step numbers SHALL be cited in §5 Upstream Ref (per OBL-02).
```

`TABLE-01 SCHEMA: DECLARED`

---

**BLOCK 3 — TABLE-04 SCHEMA: Re-render List (§4)**

```
Columns: Component | Re-renders? | Reason | Skip Mechanism | Upstream Ref
Component: exact codebase name (PASS-THROUGH). MUST match §2 name exactly.
Re-renders?: "YES" | "NO" | "UNKNOWN". MUST be explicit — no implicit absence.
Reason: prop change (name the prop) | context change (name the key) | selector (name the selector)
        MISSING-LOADING if loading-branch re-render unconfirmed. Blank only for NO rows.
Skip Mechanism: memoization mechanism name for NO rows. Blank for YES/UNKNOWN rows.
Upstream Ref: §2 hop number OR §3 state key. MUST appear for every row including NO rows [OBL-01].
Required tokens: UNKNOWN | MISSING-LOADING
Fill rules:
  1. Every §2 component SHALL appear. Silent omission is a SCHEMA-VIOLATION.
  2. An evaluated-but-memoized component MUST appear as a NO row — not absent.
```

`TABLE-04 SCHEMA: DECLARED`

---

**BLOCK 4 — §0 VOCABULARY CONTRACT**

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Map every framework API, directive, decorator, reactive primitive. Neutral Equivalent SHALL be used in §1–§7. Framework Term MUST NOT appear in §1–§7 outside §8. MAP terms violating this rule are VOCABULARY-LEAKs.

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Notes |
|------------------|------|-------|

Every codebase identifier that SHALL appear unchanged in §1–§7. MUST include all TABLE-01 Handler/Owner values, all TABLE-04 Component values, all selector names, store slice keys, context keys. Types: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`. A PASS-THROUGH name MUST NOT be neutralized or aliased (violation: ALIAS-VIOLATION).

**Binding**: §1–§7 bound to Neutral Equivalents and exact PASS-THROUGH names. MAP terms confined to §8.

`VOCABULARY CONTRACT: DECLARED`

---

**BLOCK 5 — GATE-VOCAB**

Before proceeding: verify no MAP term from §0 PART A will appear in TABLE-01 Handler/Owner column values or TABLE-04 Component/Reason column values.

```
MAP terms reviewed: [list]
Planned cell values reviewed: [list Handler/Owner/Component/Reason values]
Violations detected: [MAP term | column | context] OR "none"
GATE-VOCAB: PASS | FAIL
```

If FAIL: correct §0 PART A; document correction; re-run. Iterate until PASS.

---

**ARCHITECTURE CHECKLIST**

Before emitting the seal, verify:
- [ ] EVIDENCE CHAIN CONTRACT: DECLARED — 6 obligations present
- [ ] TABLE-01 SCHEMA: DECLARED
- [ ] TABLE-04 SCHEMA: DECLARED
- [ ] VOCABULARY CONTRACT: DECLARED — PART A and PART B complete
- [ ] GATE-VOCAB: PASS

All checks pass:

`TRACE ARCHITECTURE: SEALED`

**No trace content of any kind may appear before this token.**

---

### TRACE GENERATION PHASE

You receive `TRACE ARCHITECTURE: SEALED`. Produce §1–§9.

**Active constraints**:
- Vocabulary: Neutral Equivalents from §0 PART A in §1–§7. PASS-THROUGH names from §0 PART B exact. MAP terms only in §8. Any MAP term in §1–§7 cell values is a VOCABULARY-LEAK.
- Evidence chain: OBL-01 through OBL-06 SHALL be satisfied. Missing citations are CITATION-GAPs, DERIVATION-BREAKs, or UNSUPPORTED-CONCLUSIONs — not stylistic gaps.

**Pre-output verification**: `GATE CHECK: PASS — no MAP terms in §1–§7 planned column values.`

#### §1 Event Chain
Fill TABLE-01 SCHEMA exactly. UNKNOWN at gaps.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Carrier Name required. Direction: `parent→child` | `child→parent` | `sibling`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every mutation present. UNKNOWN for undetermined.

#### §4 Re-render List
Fill TABLE-04 SCHEMA exactly. Every §2 component present. Upstream Ref per OBL-01.

#### §5 Side Effects and Async
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref [OBL-02] |
Both branches per async effect. MISSING-LOADING / MISSING-ERROR for unconfirmed. Upstream Ref per OBL-02.

#### §6 Issue Analysis
All four categories — no omissions:
- **Unnecessary re-renders**: Named finding [Component — §4 row — nature — remediation] or `"None detected — §4 rows [cite]"` [OBL-05; OBL-06 if issue found]
- **Missing loading states**: Named finding or `"None detected — §5 rows [cite]"` [OBL-05]
- **Error state gaps**: Named finding or `"None detected — §5 rows [cite]"` [OBL-05]
- **Accessibility failures**: Named finding or `"None detected"`

#### §7 Final UI State
Per item: `"[Element] shows [state] — §3 row '[key]' [OBL-03]; §4 row '[component]' [OBL-04]."`

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
Every MAP entry. Only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
At least one entry or explicit `"None — §4 NO rows: [list]."` Citing zero rows when NO rows exist is a SCHEMA-VIOLATION.

---

### AUDIT PHASE

Produce §10–§12.

#### §10 Completeness Stamp

```
UNKNOWN:         [N] — locations: [list]
MISSING-LOADING: [N] — locations: [list]
MISSING-ERROR:   [N] — locations: [list]
Issues flagged:  [N] — named §6 findings only
```

Active correction: re-scan §1–§9; verify counts. Discrepancy: `"Corrected: [CATEGORY] [old]→[new]; at [§N location]."` Match: `"Cross-checked: no corrections required."` Record required.

#### §11 Vocabulary Audit

Scan §1–§7 for MAP leaks or alias violations. Report: `VOCABULARY-LEAK: "[term]" at §N [location — column]` / `ALIAS-VIOLATION: "[name]" aliased at §N` / `"No leaks. No violations."`

#### §12 Evidence Chain Compliance

Fill compliance against EVIDENCE CHAIN CONTRACT:

| OBL-ID | SHALL | COMPLIANCE | Location / Gap |
|--------|-------|------------|---------------|
| OBL-01 | §4 Upstream Ref per row | PASS / FAIL | |
| OBL-02 | §5 Upstream Ref per row | PASS / FAIL | |
| OBL-03 | §7 §3 key per item | PASS / FAIL | |
| OBL-04 | §7 §4 trace per item | PASS / FAIL | |
| OBL-05 | §6 "none detected" cites rows | PASS / FAIL | |
| OBL-06 | §6 issues cite §2 component | PASS / FAIL | |

**Verdict**: PASS (≥4 of 6) / FAIL — list failures.

---

## V-04 — Combined: Role Sequence + Output Format

**Axis**: Combined — ECC-first dedicated role (V-01 axis) combined with the two-column compliance table format (V-02 axis). The ECC is produced first as a standalone artifact. All subsequent pre-trace roles explicitly reference OBL-IDs. The Trace Author's section instructions embed OBL-IDs directly in column headers. The Audit role fills a compliance table drawn from the pre-declared ECC rows.

**Hypothesis**: V-01 embeds OBL-IDs in schema fill rules but the ECC table itself is not the direct input to the audit — the audit role reconstructs a compliance checklist from memory. V-02 uses a compliance table but the ECC is embedded inside the unified TRACE ARCHITECTURE artifact alongside schemas and vocabulary contract, which slightly blurs the "first and foundational" character of the ECC. V-04 combines both: ECC is produced first by a dedicated role (so it exists as a standalone artifact before any other pre-trace work), and it is formatted as a compliance table (so the audit role fills it directly). The Trace Author section headers embed OBL-ID brackets, making the evidence chain obligation visible at the point of generation. Expected ceiling: 156–160/160.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. No role may produce trace content or pre-populate downstream roles' outputs. Role output is visible to all subsequent roles.

---

### ROLE 1 — Evidence Architect

Your sole output is the EVIDENCE CHAIN CONTRACT. No schemas, no vocabulary contract, no trace content.

#### EVIDENCE CHAIN CONTRACT

| OBL-ID | Downstream Section | MUST Carry | Source | Violation Type |
|--------|--------------------|-----------|--------|----------------|
| OBL-01 | §4 — every row | Upstream Ref: §2 hop OR §3 state key | §2 / §3 | CITATION-GAP |
| OBL-02 | §5 — every row | Upstream Ref: §1 step OR §2 hop | §1 / §2 | CITATION-GAP |
| OBL-03 | §7 — every item | Named §3 key: `"§3 row '[key]'"` | §3 | DERIVATION-BREAK |
| OBL-04 | §7 — every item | Traceable §4 row | §4 | DERIVATION-BREAK |
| OBL-05 | §6 — "none detected" | Cited §4 or §5 rows | §4 / §5 | UNSUPPORTED-CONCLUSION |
| OBL-06 | §6 — named issues | Named §2 component | §2 | CITATION-GAP |

`EVIDENCE CHAIN CONTRACT: DECLARED — 6 obligations.`

**Complete output of Role 1.**

---

### ROLE 2 — Schema Architect

You receive EVIDENCE CHAIN CONTRACT from Role 1. Produce two named schema blocks. Reference OBL-IDs in fill rules. No vocabulary contract, no trace content.

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns: Step | Handler | Trigger | Owner | Timing
Handler: exact codebase name, or UNKNOWN: [name] — [reason]
Owner: exact codebase component name, or UNKNOWN: [component] — [reason]
Timing: "sync" | "deferred"
Required token: UNKNOWN: [name] — [reason]
Fill rules:
  1. Every causal hop present. Dispatch chains show source and target rows.
  2. No implicit jumps.
  3. Step values appear in §5 Upstream Ref per OBL-02.
  4. Step values appear in §4 Upstream Ref where relevant per OBL-01.
```

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns: Component | Re-renders? | Reason | Skip Mechanism | Upstream Ref [OBL-01]
Component: exact codebase name (PASS-THROUGH from §0 PART B)
Re-renders?: "YES" | "NO" | "UNKNOWN"
Reason: prop change (name) | context change (key) | selector (name) | MISSING-LOADING | blank (NO only)
Skip Mechanism: memoization mechanism (NO rows); blank otherwise
Upstream Ref [OBL-01]: §2 hop OR §3 state key — required every row, OBL-01 violation if absent
Required tokens: UNKNOWN | MISSING-LOADING
Fill rules:
  1. Every §2 component appears. Silent omission is a SCHEMA-VIOLATION.
  2. Evaluated-and-skipped = NO row, not absent.
  3. Upstream Ref column header carries [OBL-01] to make obligation visible at point of generation.
```

`TABLE SCHEMAS: DECLARED — OBL-IDs embedded.`

---

### ROLE 3 — Contract Author

You receive EVIDENCE CHAIN CONTRACT and TABLE SCHEMAS from Roles 1–2. Produce §0 Vocabulary Contract. No trace content.

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Map every framework API, directive, decorator, reactive primitive. Neutral Equivalent used in §1–§7.

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Notes |
|------------------|------|-------|

Every codebase identifier unchanged in §1–§7. Required: all TABLE-01 Handler/Owner values, all TABLE-04 Component values, all selector/store-slice/context names.
Type: `component` | `handler` | `selector` | `store-slice` | `event-name` | `context`
No neutralization. No aliasing. PASS-THROUGH is exact.

**Binding**: §1–§7 bound to Neutral Equivalents (PART A) and exact PASS-THROUGH names (PART B). MAP terms only in §8.

`VOCABULARY CONTRACT: DECLARED`

---

### ROLE 4 — Architecture Gate

You receive EVIDENCE CHAIN CONTRACT, TABLE SCHEMAS, and VOCABULARY CONTRACT from Roles 1–3.

**GATE-VOCAB**: For every MAP term in §0 PART A: verify it does not appear as a planned column value in TABLE-01 (Handler, Owner) or TABLE-04 (Component, Reason).

```
MAP terms reviewed: [list]
Column value space reviewed: [Handler / Owner / Component / Reason planned values]
Violations: [MAP term | column | cell context] OR "none"
GATE-VOCAB: PASS | FAIL
```

If FAIL: correct §0 PART A; document; re-run.

**Architecture inventory**: EVIDENCE CHAIN CONTRACT: DECLARED ✓ | TABLE SCHEMAS: DECLARED ✓ | VOCABULARY CONTRACT: DECLARED ✓ | GATE-VOCAB: PASS ✓

`TRACE ARCHITECTURE: SEALED — ECC (6 obligations), TABLE-01 SCHEMA, TABLE-04 SCHEMA, §0 PART A/B, GATE-VOCAB: PASS`

**Role 5 may not begin until TRACE ARCHITECTURE: SEALED is output.**

---

### ROLE 5 — Trace Author

You receive `TRACE ARCHITECTURE: SEALED`. Produce §1–§9.

**Active bindings**: Neutral Equivalents (§0 PART A) in §1–§7. PASS-THROUGH names (§0 PART B) exact. MAP terms only in §8. OBL-01 through OBL-06 are fill obligations — non-compliance is a named violation type, not a style gap.

**Pre-output gate**: `GATE CHECK: PASS — no MAP terms in §1–§7 planned column values.`

#### §1 Event Chain
Fill TABLE-01 SCHEMA exactly. UNKNOWN at gaps.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Carrier Name required. Direction: `parent→child` | `child→parent` | `sibling`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every mutation present. UNKNOWN for undetermined.

#### §4 Re-render List [OBL-01]
Fill TABLE-04 SCHEMA exactly. Every §2 component present. Upstream Ref per OBL-01.

#### §5 Side Effects and Async [OBL-02]
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref [OBL-02] |
Both branches per async effect. MISSING-LOADING / MISSING-ERROR for unconfirmed. Upstream Ref per OBL-02.

#### §6 Issue Analysis [OBL-05, OBL-06]
All four categories — no omissions.
- **Unnecessary re-renders**: [Component — §4 row — nature — remediation] or `"None detected — §4 rows [cite]"` [OBL-05; OBL-06]
- **Missing loading states**: [Component — §5 row — nature — remediation] or `"None detected — §5 rows [cite]"` [OBL-05]
- **Error state gaps**: [Component — §5 row — nature — remediation] or `"None detected — §5 rows [cite]"` [OBL-05]
- **Accessibility failures**: [Element — nature — remediation] or `"None detected"`

#### §7 Final UI State [OBL-03, OBL-04]
Per item: `"[Element] shows [state] — §3 row '[key]' [OBL-03]; §4 row '[component]' [OBL-04]."`

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) | Framework mechanics note |
Every MAP entry. Only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
At least one entry or explicit `"None — §4 NO rows: [list]."` Citing zero rows when NO rows exist is a SCHEMA-VIOLATION.

---

### ROLE 6 — Auditor

You receive the full output of Roles 1–5. Produce §10–§12.

#### §10 Completeness Stamp

```
UNKNOWN:         [N] — locations: [list]
MISSING-LOADING: [N] — locations: [list]
MISSING-ERROR:   [N] — locations: [list]
Issues flagged:  [N] — named §6 findings only
```

Active correction: re-scan §1–§9; verify counts. Record: discrepancy correction or "Cross-checked: no corrections required."

#### §11 Vocabulary Audit

Scan §1–§7 for MAP leaks or PASS-THROUGH alias violations. Report or: `"No leaks. No violations."`

#### §12 Evidence Chain Compliance

Fill compliance column against EVIDENCE CHAIN CONTRACT from Role 1:

| OBL-ID | MUST Carry (from ECC) | COMPLIANCE | Evidence or Violation Location |
|--------|-----------------------|------------|-------------------------------|
| OBL-01 | §4 Upstream Ref per row | PASS / FAIL | |
| OBL-02 | §5 Upstream Ref per row | PASS / FAIL | |
| OBL-03 | §7 §3 key per item | PASS / FAIL | |
| OBL-04 | §7 §4 trace per item | PASS / FAIL | |
| OBL-05 | §6 "none detected" cites rows | PASS / FAIL | |
| OBL-06 | §6 issues name §2 component | PASS / FAIL | |

**Verdict**: PASS (≥4 PASS) / FAIL — list failures.

---

## V-05 — Combined: Role Sequence + Output Format + Phrasing Register

**Axis**: Combined — (a) ECC-first dedicated role (role sequence); (b) formal obligation table with violation types and OBL-ID columns embedded in section headers (output format); (c) imperative SHALL/MUST phrasing with explicit violation naming throughout pre-trace and trace phases (phrasing register); (d) TRACE ARCHITECTURE: SEALED token explicitly inventories all sub-artifacts including ECC, binding all trace-generating work to a single named seal.

**Hypothesis**: V-01 achieves C-20 through role separation and bidirectional OBL-ID embedding in schemas. V-02 achieves it through the compliance table format. V-03 achieves it through imperative language density without role machinery. V-04 combines V-01 and V-02 but maintains role machinery for all three. V-05 combines all three and additionally: (1) adds imperative violation naming in the Trace Author's section instructions so that gap avoidance is motivated by named violation types rather than schema fill rules; (2) makes the TRACE ARCHITECTURE: SEALED token explicitly enumerate its constituent artifacts (ECC obligation count, schema column count, MAP term count, PASS-THROUGH name count) so the seal is a falsifiable claim, not a declarative marker. Expected ceiling: 158–160/160.

---

You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. Role output is visible to all subsequent roles. No role may produce trace content or pre-populate downstream artifacts.

---

### ROLE 1 — Evidence Architect

Your sole output is the EVIDENCE CHAIN CONTRACT. No schemas, no vocabulary terms, no trace content. This contract is the foundational artifact: all subsequent pre-trace roles reference its OBL-IDs; the trace-generating role fills against its obligations; the audit role checks compliance against its rows.

#### EVIDENCE CHAIN CONTRACT

| OBL-ID | Downstream Section | SHALL | Source | Violation Type if Absent |
|--------|--------------------|-------|--------|--------------------------|
| OBL-01 | §4 Re-render List — every row | carry Upstream Ref: §2 hop OR §3 key | §2 Component Tree / §3 State Delta | CITATION-GAP |
| OBL-02 | §5 Side Effects — every row | carry Upstream Ref: §1 step OR §2 hop | §1 Event Chain / §2 Component Tree | CITATION-GAP |
| OBL-03 | §7 Final UI State — every item | name §3 state key: `"§3 row '[key]'"` | §3 State Delta | DERIVATION-BREAK |
| OBL-04 | §7 Final UI State — every item | trace to §4 row | §4 Re-render List | DERIVATION-BREAK |
| OBL-05 | §6 Issue Flags — every "none detected" | cite specific §4 or §5 rows | §4 / §5 | UNSUPPORTED-CONCLUSION |
| OBL-06 | §6 Issue Flags — every named issue | name §2 component | §2 Component Tree | CITATION-GAP |

`EVIDENCE CHAIN CONTRACT: DECLARED — 6 obligations. OBL-01 through OBL-06 binding on Role 3.`

---

### ROLE 2 — Schema Architect

You receive the EVIDENCE CHAIN CONTRACT from Role 1. Produce two named schema blocks. Each schema's column definition SHALL reference the OBL-ID it satisfies. No vocabulary terms, no trace content.

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns:
  Step       — Sequential integer. Required for every row.
  Handler    — Exact codebase name. MUST be exact. UNKNOWN: [name] — [reason] if undetermined.
  Trigger    — User action {{signal}} (row 1) or upstream Step number that dispatched this handler.
  Owner      — Exact codebase component name. UNKNOWN: [component] — [reason] if undetermined.
  Timing     — "sync" | "deferred". Required for every row.

Required tokens:
  UNKNOWN: [name] — [reason]   — MUST occupy the row; absent rows are SCHEMA-VIOLATIONs

Fill rules:
  1. Every causal hop SHALL occupy one row.
  2. Dispatch chains MUST show source and target rows.
  3. An implicit jump is a SCHEMA-VIOLATION.
  4. Step values MUST appear in §5 Upstream Ref [OBL-02 coverage].
  5. Step values MUST appear in §4 Upstream Ref where the handler triggers a state change [OBL-01 coverage].
```

`TABLE-01 SCHEMA: DECLARED — columns carry OBL-01, OBL-02 coverage annotations.`

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns:
  Component         — Exact codebase name (PASS-THROUGH from §0 PART B). MUST match §2 exactly.
  Re-renders?       — "YES" | "NO" | "UNKNOWN". Absent value is a SCHEMA-VIOLATION.
  Reason            — Prop change (name the prop) | context change (name the key) | selector (name it)
                      MISSING-LOADING if loading-branch re-render unconfirmed
                      Blank ONLY for NO rows
  Skip Mechanism    — Memoization mechanism for NO rows. Blank for YES/UNKNOWN.
  Upstream Ref      — §2 hop OR §3 key. MUST appear for every row including NO rows. [OBL-01]
                      Absent = CITATION-GAP (OBL-01 violation)

Required tokens:
  UNKNOWN          — Re-renders? = undetermined
  MISSING-LOADING  — Reason column = loading-branch existence unconfirmed

Fill rules:
  1. Every §2 component SHALL appear.
  2. Evaluated-and-memoized MUST appear as NO row — not absent.
  3. Upstream Ref carries [OBL-01] to mark the obligation at point of generation.
```

`TABLE-04 SCHEMA: DECLARED — Upstream Ref column annotated with OBL-01.`

`TABLE SCHEMAS: DECLARED.`

---

### ROLE 3 — Contract Author

You receive EVIDENCE CHAIN CONTRACT and TABLE SCHEMAS from Roles 1–2. Produce §0 Vocabulary Contract. Bind PART B PASS-THROUGH entries to TABLE-01 Handler/Owner columns and TABLE-04 Component column by reference. No trace content.

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Every framework API, directive, decorator, reactive primitive. Neutral Equivalent SHALL be used in §1–§7. MAP terms appearing in §1–§7 cell values are VOCABULARY-LEAKs.

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Binds To | Notes |
|------------------|------|----------|-------|

Every codebase identifier that SHALL appear unchanged in §1–§7. Required entries:
- All expected TABLE-01 Handler values → Type: `handler` — Binds To: TABLE-01.Handler
- All expected TABLE-01 Owner values → Type: `component` — Binds To: TABLE-01.Owner
- All expected TABLE-04 Component values → Type: `component` — Binds To: TABLE-04.Component
- All selector names, store slice keys, context keys → appropriate type

No PASS-THROUGH name SHALL be neutralized or aliased. Aliasing = ALIAS-VIOLATION.

**Binding declaration**: §1–§7 bound to Neutral Equivalents (PART A) and exact PASS-THROUGH names (PART B). MAP terms confined to §8.

`VOCABULARY CONTRACT: DECLARED — PART A (N terms), PART B (M names), PASS-THROUGH bindings to TABLE-01/TABLE-04 declared.`

---

### ROLE 4 — Architecture Gate

You receive EVIDENCE CHAIN CONTRACT, TABLE SCHEMAS, and VOCABULARY CONTRACT from Roles 1–3. Perform GATE-VOCAB check and emit the unified seal.

**GATE-VOCAB**: For every MAP term in §0 PART A, verify it does not appear as a planned cell value in TABLE-01 columns Handler and Owner, or TABLE-04 columns Component and Reason.

```
MAP terms reviewed: [list from PART A — N terms]
Planned cell values reviewed: TABLE-01 Handler [list] / Owner [list] | TABLE-04 Component [list] / Reason [list]
Violations: [MAP term | column | cell context] OR "none detected"
GATE-VOCAB: PASS | FAIL
```

If FAIL: correct §0 PART A; document: `"Correction: [term] reclassified or cell value changed: [old]→[new]."` Re-run. Iterate until PASS.

**Architecture inventory — all four artifacts SHALL be complete before the seal is emitted:**
- EVIDENCE CHAIN CONTRACT: DECLARED — [N] obligations ✓
- TABLE-01 SCHEMA: DECLARED — [N] columns ✓
- TABLE-04 SCHEMA: DECLARED — [N] columns ✓
- VOCABULARY CONTRACT: DECLARED — PART A [N terms], PART B [M names] ✓
- GATE-VOCAB: PASS ✓

`TRACE ARCHITECTURE: SEALED — constituent artifacts: ECC (6 obligations: OBL-01–OBL-06), TABLE-01 SCHEMA (5 cols), TABLE-04 SCHEMA (5 cols), §0 PART A ([N] MAP terms), §0 PART B ([M] PASS-THROUGH names), GATE-VOCAB: PASS. All trace-generating roles unlocked.`

**Role 5 may not begin until TRACE ARCHITECTURE: SEALED is output.**

---

### ROLE 5 — Trace Author

You receive `TRACE ARCHITECTURE: SEALED`. Produce §1–§9.

**Active constraints**:
- Vocabulary: Neutral Equivalents from §0 PART A replace MAP terms in §1–§7. PASS-THROUGH names from §0 PART B appear exactly as declared. Any MAP term in §1–§7 cell values is a VOCABULARY-LEAK.
- Evidence chain: OBL-01 through OBL-06 from the EVIDENCE CHAIN CONTRACT are structural fill obligations. Missing citations are CITATION-GAPs, DERIVATION-BREAKs, or UNSUPPORTED-CONCLUSIONs — not style choices.
- Schema compliance: TABLE-01 and TABLE-04 column structures are locked. Column additions or omissions are SCHEMA-VIOLATIONs.

**Pre-output gate**: `GATE CHECK: PASS — no MAP terms in §1–§7 planned column values.`

#### §1 Event Chain
Fill TABLE-01 SCHEMA exactly. Every causal hop present. UNKNOWN: [name] — [reason] MUST occupy any row with an undetermined handler.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Carrier Name (prop, callback, state key) required for every hop. Direction: `parent→child` | `child→parent` | `sibling`. Signal Type: `props` | `callback` | `shared state` | `context`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every state mutation present with before/after values. Selectors named. UNKNOWN: [key] — [reason] for undetermined.

#### §4 Re-render List [OBL-01]
Fill TABLE-04 SCHEMA exactly. Every §2 component present. Upstream Ref SHALL be populated for every row — absent = CITATION-GAP [OBL-01].

#### §5 Side Effects and Async [OBL-02]
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref [OBL-02] |
Both branches declared per async effect. MISSING-LOADING: [reason] / MISSING-ERROR: [reason] for unconfirmed. Upstream Ref: §1 step or §2 hop — absent = CITATION-GAP [OBL-02].

#### §6 Issue Analysis [OBL-05, OBL-06]
All four categories — no omissions. An unlabeled category is a SCHEMA-VIOLATION.

**Unnecessary re-renders**: Named finding [Component [OBL-06] — §4 row — nature — remediation] or `"None detected — §4 rows [cite rows]"` [OBL-05]. Unsupported "none detected" = UNSUPPORTED-CONCLUSION.
**Missing loading states**: Named finding or `"None detected — §5 rows [cite rows]"` [OBL-05].
**Error state gaps**: Named finding or `"None detected — §5 rows [cite rows]"` [OBL-05].
**Accessibility failures**: Named finding or `"None detected"`.

#### §7 Final UI State [OBL-03, OBL-04]
Observable state after `{{signal}}` fully resolves. Per item:
`"[Element] shows [state] — §3 row '[key]' [OBL-03]; §4 row '[component]' [OBL-04]."`
Both citations required per item. Missing = DERIVATION-BREAK.

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
Every §0 PART A MAP entry. MUST appear. This is the only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
Types: `memoization candidate` | `batching opportunity` | `render-scope reduction`.
At least one entry or explicit: `"No optimization opportunities — §4 NO rows: [list all NO rows]."` Citing zero rows when NO rows exist is a SCHEMA-VIOLATION.

---

### ROLE 6 — Auditor

You receive the full output of Roles 1–5. Produce §10–§12.

#### §10 Completeness Stamp

Scan §1–§9 for all incompleteness tokens:

```
UNKNOWN:         [N] — locations: [§ ref — row/step identifier for each instance]
MISSING-LOADING: [N] — locations: [§ ref — row/step identifier for each instance]
MISSING-ERROR:   [N] — locations: [§ ref — row/step identifier for each instance]
Issues flagged:  [N] — named §6 findings (exclude "none detected" conclusions)
```

Active correction protocol — required:
1. Re-scan §1–§9 token-by-token; verify each count against the body.
2. Discrepancy: `"Corrected: [CATEGORY] count [old]→[new]; found additional [TOKEN] at [§N — row/step identifier]."`
3. Match: `"Cross-checked: counts match body; no corrections required."`
Cross-check record required regardless of outcome. A stamp without it is a completeness failure.

#### §11 Vocabulary Audit

Scan §1–§7 for §0 PART A MAP term leaks or PART B alias violations:
- Leak: `VOCABULARY-LEAK: "[term]" at §N [row/step — column]`
- Alias violation: `ALIAS-VIOLATION: "[name]" aliased to "[alias]" at §N [identifier]`
- Clean: `"No vocabulary leaks. No alias violations."`

#### §12 Evidence Chain Compliance

Fill compliance column against EVIDENCE CHAIN CONTRACT from Role 1 — do not reconstruct obligations from the body:

| OBL-ID | SHALL (from ECC Role 1) | COMPLIANCE | Evidence or Violation Location |
|--------|------------------------|------------|-------------------------------|
| OBL-01 | §4 Upstream Ref every row | PASS / FAIL | Cite passing rows or list CITATION-GAP locations |
| OBL-02 | §5 Upstream Ref every row | PASS / FAIL | Cite passing rows or list CITATION-GAP locations |
| OBL-03 | §7 §3 key every item | PASS / FAIL | Cite passing items or list DERIVATION-BREAK locations |
| OBL-04 | §7 §4 row every item | PASS / FAIL | Cite passing items or list DERIVATION-BREAK locations |
| OBL-05 | §6 "none detected" cites §4/§5 | PASS / FAIL | Cite passing conclusions or list UNSUPPORTED-CONCLUSION locations |
| OBL-06 | §6 named issues name §2 component | PASS / FAIL | Cite passing issues or list CITATION-GAP locations |

**Verdict**: PASS (≥4 obligations satisfied) / FAIL — list unsatisfied obligations with violation type.

---

## Variation Map Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event chain complete | PASS | PASS | PASS | PASS | PASS |
| C-02 Component tree traversal | PASS | PASS | PASS | PASS | PASS |
| C-03 State delta shown | PASS | PASS | PASS | PASS | PASS |
| C-04 Re-render list complete | PASS | PASS | PASS | PASS | PASS |
| C-05 Side effects identified | PASS | PASS | PASS | PASS | PASS |
| C-06 Issue flags present | PASS | PASS | PASS | PASS | PASS |
| C-07 Final UI state described | PASS | PASS | PASS | PASS | PASS |
| C-08 Optimization opportunities | PASS | PASS | PASS | PASS | PASS |
| C-09 Framework-portable annotations | PASS | PASS | PASS | PASS | PASS |
| C-10 Gap-visible format | PASS | PASS | PASS | PASS | PASS |
| C-11 Cross-section evidence chaining | PASS | PASS | PASS | PASS | PASS |
| C-12 Incompleteness tokens | PASS | PASS | PASS | PASS | PASS |
| C-13 Framework-neutral core enforcement | PASS | PASS | PASS | PASS | PASS |
| C-14 Vocabulary contract artifact | PASS | PASS | PASS | PASS | PASS |
| C-15 Machine-readable completeness inventory | PASS | PASS | PASS | PASS | PASS |
| C-16 PASS-THROUGH designation | PASS | PASS | PASS | PASS | PASS |
| C-17 Stamp with active correction | PASS | PASS | PASS | PASS | PASS |
| C-18 Role-level enforcement gate | PASS | PASS | PASS* | PASS | PASS |
| C-19 Pre-declared named column schemas | PASS | PASS | PASS | PASS | PASS |
| C-20 Pre-declared evidence chain contract | PASS | PASS | PASS | PASS | PASS |
| C-21 Unified pre-trace architecture seal | PASS | PASS | PASS | PASS | PASS |

*V-03 C-18 risk: criterion requires "role-level gate" — V-03 uses a flat prompt with an inline GATE-VOCAB block rather than a role transition. If the criterion is read strictly as requiring a role boundary, V-03 may score partial on C-18.

**Key differentiators for C-20 and C-21 across variations:**

| | C-20 mechanism | C-21 mechanism |
|--|----------------|----------------|
| V-01 | Dedicated Role 1 produces ECC before schemas exist; schemas embed OBL-IDs in fill rules | Role 4 (Architecture Gate) emits TRACE ARCHITECTURE: SEALED after explicit 4-artifact inventory check |
| V-02 | ECC as compliance table inside TRACE ARCHITECTURE (first sub-artifact); audit role fills COMPLIANCE column against pre-declared rows | Role 1 (Trace Architect) produces entire TRACE ARCHITECTURE artifact; SEALED token after GATE-VOCAB: PASS |
| V-03 | BLOCK 1 of flat pre-trace phase is the ECC table; all subsequent blocks reference it; audit fills compliance column | Inline ARCHITECTURE CHECKLIST ticks off 5 conditions before emitting TRACE ARCHITECTURE: SEALED |
| V-04 | Dedicated Role 1 (Evidence Architect) produces ECC first; Role 2 (Schema Architect) references OBL-IDs in column annotations; Role 6 fills compliance table against Role 1 ECC | Role 4 (Architecture Gate) emits TRACE ARCHITECTURE: SEALED with explicit inventory of ECC obligations + schema columns + contract terms |
| V-05 | Role 1 (Evidence Architect) produces ECC first with violation types; Role 2 embeds OBL-IDs in column headers; Role 5 section headers carry OBL-ID brackets; Role 6 fills against Role 1 ECC | Role 4 emits TRACE ARCHITECTURE: SEALED with falsifiable count inventory: `"ECC (6 obligations: OBL-01–OBL-06), TABLE-01 SCHEMA (5 cols), TABLE-04 SCHEMA (5 cols), §0 PART A (N terms), §0 PART B (M names), GATE-VOCAB: PASS"` |
