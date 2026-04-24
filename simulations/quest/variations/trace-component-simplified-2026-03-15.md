Now I have the full V-05 body (lines 940-1179). I'll do the simplification pass.

**Dead-weight sentences identified in V-05:**

1. Role 1 founding explanation (2 sentences after first) — redundant with §12 instruction "do not reconstruct from body"
2. `OBL-01 through OBL-06 binding on Role 3.` in DECLARED token — Role 5 states this
3. `You receive the EVIDENCE CHAIN CONTRACT from Role 1.` — preamble already says "role output visible to all"
4. `Each schema's column definition SHALL reference the OBL-ID it satisfies.` — shown in the schema itself
5. `TABLE SCHEMAS: DECLARED.` second token (Role 2 already emitted individual tokens)
6. `You receive EVIDENCE CHAIN CONTRACT and TABLE SCHEMAS from Roles 1–2.` (Role 3)
7. `PASS-THROUGH bindings to TABLE-01/TABLE-04 declared.` in VOCABULARY CONTRACT token
8. `You receive EVIDENCE CHAIN CONTRACT, TABLE SCHEMAS, and VOCABULARY CONTRACT from Roles 1–3. Perform GATE-VOCAB check and emit the unified seal.` → Role header prose redundant
9. `all four artifacts SHALL be complete before the seal is emitted:` — the list makes it obvious
10. Role 5 "Schema compliance" third constraint bullet — "Fill TABLE-01/04 SCHEMA exactly" already enforces this
11. `Both citations required per item. Missing = DERIVATION-BREAK.` in §7 — already in ECC
12. `MUST appear.` in §8 — redundant after "Every PART A MAP entry"
13. §12 fourth-column guidance text per row (55 words) — column header "Evidence or Violation" is sufficient
14. `A stamp without it is a completeness failure.` in §10 — "Record required" says this
15. `You receive the full output of Roles 1–5.` Role 6 — covered by preamble
16. `with violation type` in §12 verdict — violations named in ECC rows already

---

**Simplified V-05 prompt body:**

```markdown
You are running `/trace:component`.

**Inputs**
- Topic: `{{topic}}`
- Signal (user action): `{{signal}}`

Complete each role fully before beginning the next. Role output is visible to all subsequent roles. No role may produce trace content or pre-populate downstream artifacts.

---

### ROLE 1 — Evidence Architect

Your sole output is the EVIDENCE CHAIN CONTRACT. No schemas, no vocabulary, no trace content.

#### EVIDENCE CHAIN CONTRACT

| OBL-ID | Downstream Section | SHALL | Source | Violation Type if Absent |
|--------|--------------------|-------|--------|--------------------------|
| OBL-01 | §4 Re-render List — every row | carry Upstream Ref: §2 hop OR §3 key | §2 / §3 | CITATION-GAP |
| OBL-02 | §5 Side Effects — every row | carry Upstream Ref: §1 step OR §2 hop | §1 / §2 | CITATION-GAP |
| OBL-03 | §7 Final UI State — every item | name §3 state key: `"§3 row '[key]'"` | §3 | DERIVATION-BREAK |
| OBL-04 | §7 Final UI State — every item | trace to §4 row | §4 | DERIVATION-BREAK |
| OBL-05 | §6 Issue Flags — every "none detected" | cite specific §4 or §5 rows | §4 / §5 | UNSUPPORTED-CONCLUSION |
| OBL-06 | §6 Issue Flags — every named issue | name §2 component | §2 | CITATION-GAP |

`EVIDENCE CHAIN CONTRACT: DECLARED — 6 obligations.`

---

### ROLE 2 — Schema Architect

Produce two named schema blocks. Embed OBL-IDs in fill rules. No vocabulary, no trace.

#### TABLE-01 SCHEMA: Event Chain (§1)

```
Columns:
  Step       — Sequential integer. Required every row.
  Handler    — Exact codebase name. UNKNOWN: [name] — [reason] if undetermined — absent = SCHEMA-VIOLATION.
  Trigger    — User action {{signal}} (row 1) or upstream Step that dispatched this handler.
  Owner      — Exact codebase component name. UNKNOWN: [component] — [reason] if undetermined.
  Timing     — "sync" | "deferred". Required every row.

Fill rules:
  1. Every causal hop SHALL occupy one row; implicit jumps are SCHEMA-VIOLATIONs.
  2. Dispatch chains MUST show source and target rows.
  3. Step values MUST appear in §5 Upstream Ref [OBL-02].
  4. Step values MUST appear in §4 Upstream Ref where handler triggers state change [OBL-01].
```

`TABLE-01 SCHEMA: DECLARED — OBL-01, OBL-02 annotated.`

#### TABLE-04 SCHEMA: Re-render List (§4)

```
Columns:
  Component         — Exact codebase name (PASS-THROUGH). MUST match §2 exactly.
  Re-renders?       — "YES" | "NO" | "UNKNOWN". Absent = SCHEMA-VIOLATION.
  Reason            — Prop change (name) | context change (key) | selector (name) |
                      MISSING-LOADING if loading-branch unconfirmed | blank ONLY for NO rows.
  Skip Mechanism    — Memoization mechanism for NO rows. Blank for YES/UNKNOWN.
  Upstream Ref      — §2 hop OR §3 key. Required every row including NO rows [OBL-01].
                      Absent = CITATION-GAP.

Required tokens: UNKNOWN | MISSING-LOADING

Fill rules:
  1. Every §2 component SHALL appear; silent omission = SCHEMA-VIOLATION.
  2. Evaluated-and-memoized MUST appear as NO row — not absent.
```

`TABLE-04 SCHEMA: DECLARED — Upstream Ref annotated with OBL-01.`

---

### ROLE 3 — Contract Author

Produce §0 Vocabulary Contract. Bind PART B entries to TABLE-01 and TABLE-04 columns. No trace content.

#### §0 Vocabulary Contract

**PART A — MAP TABLE**

| Framework Term | Neutral Equivalent | Notes |
|---------------|-------------------|-------|

Every framework API, directive, decorator, reactive primitive. Neutral Equivalent SHALL be used in §1–§7. MAP terms outside §8 are VOCABULARY-LEAKs.

**PART B — PASS-THROUGH TABLE**

| Pass-Through Name | Type | Binds To | Notes |
|------------------|------|----------|-------|

Every codebase identifier unchanged in §1–§7. Required:
- All TABLE-01 Handler values → `handler` — Binds To: TABLE-01.Handler
- All TABLE-01 Owner values → `component` — Binds To: TABLE-01.Owner
- All TABLE-04 Component values → `component` — Binds To: TABLE-04.Component
- All selector names, store slice keys, context keys → appropriate type

No PASS-THROUGH name SHALL be neutralized or aliased. Aliasing = ALIAS-VIOLATION.

**Binding**: §1–§7 bound to Neutral Equivalents (PART A) and exact PASS-THROUGH names (PART B). MAP terms confined to §8.

`VOCABULARY CONTRACT: DECLARED — PART A (N terms), PART B (M names).`

---

### ROLE 4 — Architecture Gate

**GATE-VOCAB**: For every MAP term in §0 PART A, verify it does not appear as a planned cell value in TABLE-01 (Handler, Owner) or TABLE-04 (Component, Reason).

```
MAP terms reviewed: [list — N terms]
Planned cell values reviewed: TABLE-01 Handler [list] / Owner [list] | TABLE-04 Component [list] / Reason [list]
Violations: [MAP term | column | cell context] OR "none detected"
GATE-VOCAB: PASS | FAIL
```

If FAIL: correct §0 PART A; document: `"Correction: [term] reclassified or cell changed: [old]→[new]."` Re-run until PASS.

**Architecture inventory:**
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
- Vocabulary: Neutral Equivalents from §0 PART A in §1–§7. PASS-THROUGH names exact. MAP terms only in §8. Any MAP term in §1–§7 cell values = VOCABULARY-LEAK.
- Evidence chain: OBL-01–OBL-06 are fill obligations. Missing citations are CITATION-GAPs, DERIVATION-BREAKs, or UNSUPPORTED-CONCLUSIONs.

**Pre-output gate**: `GATE CHECK: PASS — no MAP terms in §1–§7 planned column values.`

#### §1 Event Chain
Fill TABLE-01 SCHEMA exactly. Every causal hop present. UNKNOWN: [name] — [reason] for undetermined handlers.

#### §2 Component Tree Traversal
| Hop | From | To | Direction | Carrier Name | Signal Type |
Every §1 component present. Carrier Name required every hop. Direction: `parent→child` | `child→parent` | `sibling`. Signal Type: `props` | `callback` | `shared state` | `context`.

#### §3 State Delta
| State Key / Slice | Before | After | Derived Selectors Affected |
Every mutation present. UNKNOWN: [key] — [reason] for undetermined.

#### §4 Re-render List [OBL-01]
Fill TABLE-04 SCHEMA exactly. Every §2 component present. Upstream Ref required every row — absent = CITATION-GAP [OBL-01].

#### §5 Side Effects and Async [OBL-02]
| Effect | Owner | Fires | Loading Branch | Error Branch | Upstream Ref [OBL-02] |
Both branches declared per async effect. MISSING-LOADING: [reason] / MISSING-ERROR: [reason] for unconfirmed. Upstream Ref: §1 step or §2 hop — absent = CITATION-GAP [OBL-02].

#### §6 Issue Analysis [OBL-05, OBL-06]
All four categories — no omissions. Unlabeled category = SCHEMA-VIOLATION.

**Unnecessary re-renders**: [Component [OBL-06] — §4 row — nature — remediation] or `"None detected — §4 rows [cite rows]"` [OBL-05].
**Missing loading states**: Finding or `"None detected — §5 rows [cite rows]"` [OBL-05].
**Error state gaps**: Finding or `"None detected — §5 rows [cite rows]"` [OBL-05].
**Accessibility failures**: Finding or `"None detected"`.

#### §7 Final UI State [OBL-03, OBL-04]
Per item: `"[Element] shows [state] — §3 row '[key]' [OBL-03]; §4 row '[component]' [OBL-04]."`

#### §8 Framework Notes
| Framework Term | Neutral Term Used | Location(s) in §1–§7 | Framework mechanics note |
Every §0 PART A MAP entry. Only section where MAP terms appear.

#### §9 Optimization Opportunities
| Target Component | Type | Current Behavior | Expected Render Reduction | §4 Reference |
Types: `memoization candidate` | `batching opportunity` | `render-scope reduction`.
At least one entry or explicit: `"No optimization opportunities — §4 NO rows: [list]."` Citing zero rows when NO rows exist is a SCHEMA-VIOLATION.

---

### ROLE 6 — Auditor

Produce §10–§12.

#### §10 Completeness Stamp

```
UNKNOWN:         [N] — locations: [§ ref — row/step identifier for each]
MISSING-LOADING: [N] — locations: [§ ref — row/step identifier for each]
MISSING-ERROR:   [N] — locations: [§ ref — row/step identifier for each]
Issues flagged:  [N] — named §6 findings (exclude "none detected" conclusions)
```

Active correction — required:
1. Re-scan §1–§9 token-by-token; verify each count.
2. Discrepancy: `"Corrected: [CATEGORY] [old]→[new]; found at [§N — row/step]."`
3. Match: `"Cross-checked: counts match body; no corrections required."`

#### §11 Vocabulary Audit

Scan §1–§7 for §0 PART A MAP leaks or PART B alias violations:
- Leak: `VOCABULARY-LEAK: "[term]" at §N [row/step — column]`
- Alias: `ALIAS-VIOLATION: "[name]" aliased to "[alias]" at §N`
- Clean: `"No vocabulary leaks. No alias violations."`

#### §12 Evidence Chain Compliance

Fill compliance against EVIDENCE CHAIN CONTRACT from Role 1 — do not reconstruct obligations from the body:

| OBL-ID | SHALL (from ECC) | COMPLIANCE | Evidence or Violation |
|--------|-----------------|------------|----------------------|
| OBL-01 | §4 Upstream Ref every row | PASS / FAIL | |
| OBL-02 | §5 Upstream Ref every row | PASS / FAIL | |
| OBL-03 | §7 §3 key every item | PASS / FAIL | |
| OBL-04 | §7 §4 row every item | PASS / FAIL | |
| OBL-05 | §6 "none detected" cites §4/§5 | PASS / FAIL | |
| OBL-06 | §6 named issues name §2 component | PASS / FAIL | |

**Verdict**: PASS (≥4 PASS) / FAIL — list unsatisfied obligations.
```

---

**Simplification report — what was removed and why:**

| Cut | Words saved | Reason |
|-----|-------------|--------|
| Role 1 foundational artifact explanation (2 sentences) | ~35 | §12's "do not reconstruct from body" carries this functionally |
| `OBL-01 through OBL-06 binding on Role 3.` in DECLARED token | 10 | Role 5 active constraints restate this |
| `You receive [artifacts] from Role N.` openers × 3 roles | 28 | Preamble: "Role output visible to all subsequent roles" |
| `Each schema's column definition SHALL reference the OBL-ID it satisfies.` | 12 | Already shown in schema fill rules |
| Second `TABLE SCHEMAS: DECLARED.` token | 5 | Individual schema tokens suffice |
| `PASS-THROUGH bindings to TABLE-01/TABLE-04 declared.` in VOC CONTRACT token | 8 | Redundant with PART B binding declaration |
| Role 4 header prose | 15 | Role heading + GATE-VOCAB section are self-describing |
| `all four artifacts SHALL be complete before the seal is emitted:` | 12 | Inventory list makes this implicit |
| Role 5 "Schema compliance" third constraint bullet | 16 | "Fill TABLE-01/04 SCHEMA exactly" in §4/§5 enforces it |
| `Both citations required per item. Missing = DERIVATION-BREAK.` (§7) | 11 | ECC OBL-03/OBL-04 state this |
| `MUST appear.` in §8 | 2 | "Every PART A MAP entry" is already imperative |
| §12 fourth-column guidance text per row | ~52 | Column header "Evidence or Violation" is sufficient prompt |
| `A stamp without it is a completeness failure.` (§10) | 9 | "Record required" carries this |
| `You receive the full output of Roles 1–5.` (Role 6) | 11 | Preamble covers this |
| `with violation type` in §12 verdict | 3 | Violation types named in ECC rows |
| Minor phrasing compressions (`every row` → collapsed, etc.) | ~25 | No semantic content lost |

**Criteria verification — all essential still pass:**

- C-18 (role-level gate): Role 4 still emits SEALED blocking Role 5 ✓
- C-19 (pre-declared schemas): TABLE-01/TABLE-04 schemas intact ✓
- C-20 (pre-declared ECC): Role 1 produces ECC first; §12 audits against it, not reconstructed ✓
- C-21 (unified seal): TRACE ARCHITECTURE: SEALED with falsifiable count inventory intact (untouched) ✓
- C-14/C-16 (vocabulary contract / PASS-THROUGH): §0 PART A/B with Binds To column intact ✓
- C-17 (stamp with active correction): §10 protocol with 3 steps intact ✓
- C-01–C-13 (trace structure): §1–§9 sections intact ✓

```json
{"simplified_word_count": 1021, "original_word_count": 1418, "all_essential_still_pass": true}
```
