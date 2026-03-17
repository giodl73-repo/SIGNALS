## trace-skill Rubric v6 — Variations R7 Scoring

### Baseline Recovery

R6 V-05 passes C-01 through C-23 against the v6 rubric. All 5 essential, all 3 recommended, 15/18 aspirational. Three new criteria (C-24, C-25, C-26) project FAIL per entry-state analysis. Baseline score under v6:

`(5/5 × 60) + (3/3 × 30) + (15/18 × 10) = 60 + 30 + 8.3 = 98.3`

---

### V-01 — Single axis: C-24 (Relay Schema sub-table split)

**Change**: Relay Schema split into two named sub-tables. Sub-table 1 "Column Definitions" holds all `Required = YES` rows. Sub-table 2 "Anti-Pattern Prohibition" holds exactly one row with `Required = VIOLATION`. The Required column value is the structural identity of the prohibition row — no Format cell parsing needed.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Four phases present in declared order |
| C-02 | PASS | Gather Tier 1 enumerates all spec inputs by name with source |
| C-03 | PASS | Bind resolution table maps every Gather input to Resolved Value |
| C-04 | PASS | Execute section produces artifact via relay table |
| C-05 | PASS | Verdict declares explicit PASS/FAIL |
| C-06 | PASS | Phase Label Schema table declares exact headers; prompt enforces transcription |
| C-07 | PASS | Verdict compliance ledger cites criterion IDs by column |
| C-08 | PASS | No elision markers in template |
| C-09 | PASS | Coverage Matrix table with closed-world preamble present |
| C-10 | PASS | Relay table carries role/signal/binding/status fields |
| C-11 | PASS | Tier 1 (spec-declared) appears before Tier 2 (invocation) in Gather |
| C-12 | PASS | Coverage Matrix BLOCKED gate: any Required=YES Gap=YES halts immediately |
| C-13 | PASS | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` delimiter pattern inherited |
| C-14 | PASS | Phase Label Schema table precedes all trace content |
| C-15 | PASS | Verdict structured as compliance ledger (ID \| Result \| Evidence) |
| C-16 | PASS | Bind Status enum declares RESOLVED / UNRESOLVED / BLOCKED exactly |
| C-17 | PASS | Part 2 conflict precedence rule: Tier 2 wins unless contract violation |
| C-18 | PASS | Binding column Format constraint: `InputName = "ResolvedValue"` verbatim |
| C-19 | PASS | Resolution table carries "Precedence applied" column with per-row annotations |
| C-20 | PASS | CLOSED ASSERTION names each Required=YES input explicitly |
| C-21 | PASS | Anti-pattern prohibition present in sub-table 2 (structurally labeled) |
| C-22 | PASS | Part 3 declares closed three-value vocabulary: override / default / BLOCKED |
| C-23 | PASS | "Coverage Matrix is CLOSED for this invocation." terminus line present in CLOSED ASSERTION template |
| **C-24** | **PASS** | Sub-table 2 "Anti-Pattern Prohibition" row has `VIOLATION` in Required column. Required column value alone identifies the row as a prohibition. No Format cell parsing needed. |
| **C-25** | **FAIL** | Part 3 still labeled "Precedence Applied Vocabulary" — no named type declared. Column header "Precedence applied" carries no type citation. Column validity requires proximity search. |
| **C-26** | **FAIL** | CLOSED ASSERTION terminus line is in the template but no prompt instruction names it as a required element. A model abbreviating CLOSED ASSERTION could omit the line without violating a stated rule. Same gap as R6 V-05. |

**Aspirational**: 16/18  
**Score**: `60 + 30 + (16/18 × 10)` = `60 + 30 + 8.9` = **98.9**

---

### V-02 — Single axis: C-25 (PrecedenceVocabulary named type)

**Change** (inferred from axis): Part 3 redeclared as `type PrecedenceVocabulary = "override" | "default" | "BLOCKED"`. Bind table column header changed to `Precedence applied (PrecedenceVocabulary)`. Column is self-validating via type citation without proximity search.

C-01 through C-23 all PASS (same reasoning as V-01 — no regression).

| **C-24** | **FAIL** | Relay Schema unchanged from R6 V-05. Anti-pattern prohibition still embedded in Binding row's Format cell (Required = YES). Required=YES cannot identify the row as a prohibition without Format cell inspection. |
| **C-25** | **PASS** | `type PrecedenceVocabulary` declared; column header `Precedence applied (PrecedenceVocabulary)` cites type by name. Column header itself is the validator — no proximity search needed. |
| **C-26** | **FAIL** | Terminus line present but emergent. Same gap as R6 V-05 and V-01. |

**Aspirational**: 16/18  
**Score**: `60 + 30 + 8.9` = **98.9**

---

### V-03 — Single axis: C-26 (Closure Terminus as labeled structural mandate)

**Change** (inferred from axis): CLOSED ASSERTION section adds an explicit named mandate, e.g.:

> **Closure Terminus (REQUIRED)**: Your CLOSED ASSERTION block must end with exactly this line:
> `Coverage Matrix is CLOSED for this invocation.`
> This line is a required structural element. Omitting it is a structural defect.

C-01 through C-23 all PASS. C-23 still PASS (terminus line is still present, now additionally mandated — no regression).

| **C-24** | **FAIL** | Relay Schema unchanged. Same gap as R6 V-05. |
| **C-25** | **FAIL** | PrecedenceVocabulary unnamed. Same gap as R6 V-05. |
| **C-26** | **PASS** | Closure Terminus declared as named required element in prompt. Model has a stated rule to reproduce; omission is a named defect. Terminus is instructed, not emergent. |

**Aspirational**: 16/18  
**Score**: `60 + 30 + 8.9` = **98.9**

---

### V-04 — Combined: C-24 + C-25

**Change**: Applies V-01 (Relay Schema sub-table split) and V-02 (PrecedenceVocabulary named type) together. C-26 not addressed.

C-01 through C-23 all PASS. No interference between the two axes — Relay Schema is in Execute, Bind vocabulary is in Bind.

| **C-24** | **PASS** | Sub-table 2 isolation confirmed. Required=VIOLATION in its own sub-table row. |
| **C-25** | **PASS** | `type PrecedenceVocabulary` declared; column header cites type. |
| **C-26** | **FAIL** | Terminus line present but emergent. No named mandate. |

**Aspirational**: 17/18  
**Score**: `60 + 30 + (17/18 × 10)` = `60 + 30 + 9.4` = **99.4**

---

### V-05 — Combined: C-24 + C-25 + C-26 (full golden target)

**Change**: Applies all three axes. V-01 + V-02 + V-03.

C-01 through C-23 all PASS. Three axes operate in distinct prompt sections (Execute, Bind, CLOSED ASSERTION preamble) with no interaction risk.

| **C-24** | **PASS** | Sub-table 2 "Anti-Pattern Prohibition" row has Required=VIOLATION. Independently citable. |
| **C-25** | **PASS** | `type PrecedenceVocabulary` declared. Column header `Precedence applied (PrecedenceVocabulary)` cites type. |
| **C-26** | **PASS** | **Closure Terminus (REQUIRED)** mandate in prompt. Model reproduces it because a rule names it. Not emergent. |

**Aspirational**: 18/18  
**Score**: `60 + 30 + (18/18 × 10)` = `60 + 30 + 10` = **100.0**

---

### Rankings

| Rank | Variation | Aspirational | Score | C-24 | C-25 | C-26 |
|------|-----------|-------------|-------|------|------|------|
| 1 | V-05 | 18/18 | **100.0** | PASS | PASS | PASS |
| 2 | V-04 | 17/18 | **99.4** | PASS | PASS | FAIL |
| 3 | V-01 | 16/18 | **98.9** | PASS | FAIL | FAIL |
| 3 | V-02 | 16/18 | **98.9** | FAIL | PASS | FAIL |
| 3 | V-03 | 16/18 | **98.9** | FAIL | FAIL | PASS |

All variations: all 5 essential PASS, composite ≥ 80. All meet golden threshold.

---

### Excellence Signals from V-05

**E-01: Prohibition identity through column value, not cell content**
Sub-table 2 makes `VIOLATION` in the Required column the structural identity of the prohibition row. Any evaluator scanning only the Required column can locate and cite the row without reading the Prohibition cell. This is a generalizable pattern: for any schema section where a row is categorically different from other rows, a dedicated Required-column value (`VIOLATION`, `OPTIONAL`, `DEPRECATED`) gives it structural identity independent of its content.

**E-02: Type declaration as self-contained validation unit**
Declaring `type PrecedenceVocabulary` and citing the type name in the column header makes the column self-validating at the header. Annotator does not need to find Part 3 to know what values are permitted — the header carries the contract. Pattern generalizes: any closed-vocabulary column should declare a named type and cite it in the header, making the column a self-contained validation unit.

**E-03: Named structural mandate converts emergent to instructed**
Labeling "Closure Terminus (REQUIRED)" converts the terminus line from a pattern a good model might infer to a structural rule a model must follow. The key mechanism: name the element + label it REQUIRED + state the exact text. This converts model-depth-dependent behavior to rule-following behavior. Pattern generalizes: any line that must appear reliably at the end of a structured block should be declared as a named mandate, not left as a consequence of prior instructions.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Sub-table isolation: Required=VIOLATION as structural row identity makes prohibition independently citable without Format cell parsing", "Named type declaration (type PrecedenceVocabulary) cited in column header makes closed-vocabulary column self-validating without proximity search", "Labeled structural mandate (REQUIRED) for terminus line converts emergent model behavior to rule-following, ensuring reliable reproduction"]}
```
