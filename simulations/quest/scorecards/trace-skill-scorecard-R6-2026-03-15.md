# trace-skill — Quest Score Round 6

## Scoring: V-01 through V-05 against Rubric v5

---

### V-01 — Output format: dedicated Anti-pattern row (C-21 axis)

V-01's full prompt body is visible. Built on R5 V-04/V-05 foundation (C-22 PASS, C-23 PASS) + adds dedicated `Binding (Anti-pattern)` row.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Gather / Bind / Execute / Verdict present in sequence |
| C-02 | PASS | Gather Tier 1 table enumerates all inputs with Spec Source Type |
| C-03 | PASS | Bind resolution table maps every input to single Resolved Value |
| C-04 | PASS | Execute phase with relay schema present; artifact production enabled |
| C-05 | PASS | Verdict phase declared; compliance ledger structure carried from R5 base |
| C-06 | PASS | Phase Label Schema (IMMUTABLE) preamble declares exact headers |
| C-07 | PASS | Verdict compliance ledger cites criterion IDs (C-15 structure) |
| C-08 | PASS | Artifact complete by instruction from R5 base |
| C-09 | PASS | Coverage Matrix with closed-world preamble present |
| C-10 | PASS | Relay Schema has Role / Signal / Binding / Status; Verdict reads evidence fields |
| C-11 | PASS | Gather Tier 1 (spec) precedes Tier 2 (invocation) |
| C-12 | PASS | Coverage Matrix BLOCKED gate section with explicit halt instruction |
| C-13 | PASS | Delimiter markers carried from R5 base |
| C-14 | PASS | Phase Label Schema (IMMUTABLE) table at document top, before all trace content |
| C-15 | PASS | Verdict compliance ledger table from R5 base |
| C-16 | PASS | Bind Part 1 Status Enum declares RESOLVED / UNRESOLVED / BLOCKED |
| C-17 | PASS | Bind Part 2 Conflict Precedence Rule explicitly stated |
| C-18 | PASS | Relay Schema `Binding (Format)` row: `` `InputName = "ResolvedValue"` `` with verbatim example |
| C-19 | PASS | Bind resolution table carries `Precedence applied` column with per-row values |
| C-20 | PASS | CLOSED ASSERTION block names each Required=YES input one line per input |
| **C-21** | **PASS** | Dedicated `Binding (Anti-pattern)` row with `VIOLATION` in Required column; "DO NOT write `InputName` alone" as structurally independent row — independently citable without parsing Format cell |
| **C-22** | **PASS** | Part 3 declares closed three-value vocabulary `override / default / BLOCKED`; "Do NOT use free-form phrases" closes the annotation space |
| **C-23** | **PASS** | "Coverage Matrix is CLOSED for this invocation. Proceed to Gather." as instructed terminus line — required by prompt, not emergent from model depth |

**Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

### V-02 — Lifecycle emphasis: PrecedenceVocabulary type declaration (C-22 axis)

Built on R5 V-02 base (C-21 FAIL, C-22 PARTIAL, C-23 PASS). R6 adds named type `PrecedenceVocabulary` with closed vocab declaration.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-08 | PASS | All essential + recommended from R5 base |
| C-09–C-20 | PASS | Carried from R5 base |
| C-21 | **FAIL** | No dedicated Anti-pattern row; prohibition remains embedded in Format cell description — not independently citable |
| C-22 | **PASS** | Named type `PrecedenceVocabulary`; column header cites type; self-validating annotation column |
| C-23 | PASS | Terminus line carried from R5 V-02 |

Aspirational: 14/15 × 10 = **9.33**

**Composite: 60 + 30 + 9.33 = 99.3/100** ✓ All essential PASS

---

### V-03 — Phrasing register: instructed labeled terminus (C-23 axis)

Built on R5 V-03 base (C-21 FAIL, C-22 FAIL, C-23 PARTIAL). R6 adds explicit closure declaration line as instructed prompt element.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-08 | PASS | All essential + recommended from R5 base |
| C-09–C-20 | PASS | Carried from R5 base |
| C-21 | **FAIL** | No dedicated Anti-pattern row |
| C-22 | **FAIL** | No closed three-value vocabulary declaration in Precedence applied column |
| C-23 | **PASS** | "Coverage Matrix is CLOSED for this invocation." placed as labeled structural terminus in prompt — reproduced by model, not inferred |

Aspirational: 13/15 × 10 = **8.67**

**Composite: 60 + 30 + 8.67 = 98.7/100** ✓ All essential PASS

---

### V-04 — Combined: Output format + Lifecycle emphasis (C-21 + C-22)

C-23 PASS carried from R5 base. Both dedicated Anti-pattern row and named PrecedenceVocabulary type added.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-20 | PASS | All from R5 base |
| C-21 | **PASS** | Dedicated Anti-pattern row (V-01 axis applied) |
| C-22 | **PASS** | Named type PrecedenceVocabulary (V-02 axis applied) |
| C-23 | PASS | Carried from R5 base |

Aspirational: 15/15 × 10 = **10**

**Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

### V-05 — Combined golden: all three axes (C-21 + C-22 + C-23)

All three R6 improvements applied simultaneously.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-20 | PASS | All from R5 base |
| C-21 | **PASS** | Dedicated Anti-pattern row |
| C-22 | **PASS** | Named type PrecedenceVocabulary; closed vocabulary |
| C-23 | **PASS** | Instructed terminus line |

Aspirational: 15/15 × 10 = **10**

**Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

## Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 (tie) | V-01 | 100/100 | YES | C-21 + C-22 + C-23 all PASS; built on R5 V-04/V-05 foundation |
| 1 (tie) | V-04 | 100/100 | YES | C-21 + C-22 axis; C-23 from R5 |
| 1 (tie) | V-05 | 100/100 | YES | All three axes |
| 4 | V-02 | 99.3/100 | YES | C-21 still FAIL |
| 5 | V-03 | 98.7/100 | YES | C-21 + C-22 still FAIL |

---

## Excellence Signals from Top-Scoring Variations

### Signal 1: `VIOLATION` as Required column value — prohibition marked at cell level, not prose level

V-01's Relay Schema uses `VIOLATION` in the Required column for the Anti-pattern row (instead of YES/NO). This makes the row's mandatory character visible at column-scan granularity — an evaluator checking Required=YES rows hits `VIOLATION` as a structural distinct marker. The prohibition is not just declared; it is classified at the same schema layer as the data columns.

### Signal 2: Explicit row-count mandate with "do not skip" instruction names the Anti-pattern row

"All five rows are active requirements — do not skip the Anti-pattern row." The mandate names the specific row the model might omit and prohibits the omission by name. This is anticipatory override: instead of relying on the model to infer that all rows apply, the prompt forecloses the skip by naming it.

### Signal 3: Relay table preamble cross-references both Relay Schema rows by label at instantiation site

V-01's relay table preamble: "(Binding column carries `InputName = "ResolvedValue"` pairs **per Relay Schema Format**; no name-only values **per Relay Schema Anti-pattern**)". The constraint is visible at the point of table instantiation, citing both row labels. This is a closed-loop cross-reference: the table's own header names its two governing schema rows. An evaluator checking the relay table sees both constraints without scrolling back to the schema. This pattern — schema-to-instantiation cross-reference at the header site — is not yet captured by any rubric criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Relay Schema prohibition row uses VIOLATION in Required column — makes the row structurally distinct from YES/NO data rows; prohibition is classified at schema-column granularity rather than embedded in cell prose", "Relay table preamble cross-references both Format and Anti-pattern Relay Schema rows by their row labels ('per Relay Schema Format; no name-only values per Relay Schema Anti-pattern') — closed-loop enforcement at instantiation site, not only at schema declaration site", "Explicit row-count mandate names the specific row the model might skip ('do not skip the Anti-pattern row') — anticipatory override forecloses omission by naming it rather than relying on model inference"]}
```
