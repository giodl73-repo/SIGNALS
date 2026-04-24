unit, e.g., 'Invoice value > $10,000'; category-only is a fail; example-only is a fail" — both mechanisms with concrete instantiation |
| V-03 | **PARTIAL** | Column header: "Condition (threshold type + quoted example)" — abbreviated; category list and anti-pattern rules appear in prose instruction block before table ("dollar amount, day count, retry count, or unit quantity"), not in column header; no concrete quoted example (e.g., "Invoice value > $10,000") provided anywhere; mechanism 1 present in prose, mechanism 2 described but not instantiated; C-31 requires both mechanisms in same column header or point-of-use definition with concrete example closing format ambiguity |
| V-04 | **PARTIAL** | Column header: "(BOTH required: (1) threshold-type category — dollar amount, day count, retry count, unit quantity — AND (2) quoted example with operator and unit; category-only is a fail; example-only is a fail)" — category list present ✓; quoted example described by format but no concrete instantiation (no `"Invoice value > $10,000"` in header); mechanism 2 named but not exemplified; format ambiguity not closed |
| V-05 | **PARTIAL** | Column header: "Condition (threshold type + quoted example; both required simultaneously)" — abbreviated; category list in prose ("dollar amount, day count, retry count, unit quantity") but not in header; no concrete quoted example provided; identical structural gap as V-03 |

---

**C-32 through C-45:** ALL PASS — all 5 variations. R13 floor covers all. Bidirectional exception-catalog gates, scan partitioning, STEP 0A/0B labeling, LT-ID cascade, typed escape codes, certified handler gate language — all present.

---

**C-46 — Pre-Schema Incumbent-Process Anchoring**

| Var | Status | Evidence |
|-----|--------|----------|
| V-01 | **PASS** | Full inline-enforcement table before STEP 0A; per-field anti-pattern rules: Incumbent Process ("'manual process' or 'spreadsheet' without qualification does not count"), FM-01/FM-02 with identifiers and specificity rules, Inertia Driver ("'familiarity' or 'it works well enough' without specificity does not count"); Phase Index Status-Quo Gap column header mandates FM-ID inline with "structurally unanchored and is a fail" language; AC-21 in Coverage Scan Group A verifies block; D-09/D-10 in defect taxonomy; Production Gate names "missing SQ Declaration" and "FM-ID-free failure mode" as causal defects |
| V-02 | **PASS** | Key-value table before STEP 0A; FM-01/FM-02 as field names (identifiers present); Inertia Driver field present; post-table statement: "FM-IDs defined in this block are required fields in the Phase Index Status-Quo Gap column. A Phase Index row with a Status-Quo Gap cell that names no FM-ID from this block is structurally unanchored." Phase Index column header enforces FM-ID inline; AC-21 present; D-09/D-10 in taxonomy; Production Gate names causal defects. Weaker per-field anti-pattern rules in declaration table vs V-01 (Inertia Driver field carries no "does not count" inline), but C-46 minimum satisfied |
| V-03 | **PASS** | Prose instructions + key-value table before STEP 0A; FM-01/FM-02 identifiers assigned by prose instruction ("Assign the identifier FM-01 in the cell"); Inertia Driver field; post-table: "The FM-01 and FM-02 identifiers from this block are required in the Phase Index Status-Quo Gap column"; Phase Index Status-Quo Gap column enforces FM-ID; D-09/D-10 present |
| V-04 | **PASS** | Two-part structure: Part A (failure modes with FM-IDs, inertia driver with "must reference at least one named incumbent role" enforcement) + Part B (Incumbent Role Scope with SQR-IDs); Gate A updated to include C-46 in Blocked-by; SQ-Scope field in Role Registry traces roles to IN/NEW/SECONDARY against SQR-IDs; Phase Index Status-Quo Gap enforces FM-IDs; most comprehensive C-46 implementation; D-09/D-10 present |
| V-05 | **PASS** | Prose + inline-enforcement table before STEP 0A; FM-01/FM-02 with identifiers and per-field anti-pattern ("generic 'error-prone' is a fail"); Inertia Driver with "'familiarity' alone does not count"; post-table: "These FM-IDs are required fields in Step 2 phase blocks"; each phase block carries Status-Quo Gap field requiring FM-ID; D-09/D-10 present |

---

**C-47 — Dual-Column Escape-Code Structural Pressure**

| Var | Status | Evidence |
|-----|--------|----------|
| V-01 | **PASS** | Phase Index is table format; Entry Trigger column carries DERIVED:rationale escape code; Status-Quo Gap column adjacent (immediately after Entry Trigger in column order); Status-Quo Gap column header: "names which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID reference is structurally unanchored and is a fail"; Gate B blocked by C-47; AC-22 in Coverage Scan Group B verifies both columns and adjacency; D-11/D-12/D-13 in taxonomy |
| V-02 | **PASS** | Phase Index table; Entry Trigger column has DERIVED:rationale; Status-Quo Gap column adjacent with explicit "these two columns audit each other: a cell with no FM-ID is structurally unanchored and is a fail" language in column header — strongest naming of the mutual-verification relationship; Gate B blocked by C-47; AC-22 verifies adjacency and FM-ID per row |
| V-03 | **PASS** | Phase Index table; Entry Trigger column has DERIVED:rationale; Status-Quo Gap column adjacent with "prose without FM-ID is a fail" inline; prose instruction at Step 2 level: "Write FM-01 or FM-02 -- do not write a prose description without an FM-ID reference"; Gate B blocked by C-47; imperative point-of-use enforcement at authoring time |
| V-04 | **PASS** | Phase Index table; Entry Trigger column has DERIVED:rationale; Status-Quo Gap column adjacent with "cell with no FM-ID is structurally unanchored and is a fail"; Gate B blocked by C-47; no explicit "audit each other" language but structural co-location and FM-ID mandate satisfy criterion |
| V-05 | **PASS** | Phase Index uses block format (not table); Entry Trigger and Status-Quo Gap are adjacent sequential named fields within each phase block; block instruction: "a generic DERIVED:rationale will simultaneously produce a vague Status-Quo Gap with no FM-ID, making the incompleteness visible within the block without a separate scan" — explicitly names the auditing principle via block architecture; Gate B blocked by C-47; AC-22 adapted for block format: "Every phase block in Step 2 carries a Status-Quo Gap field adjacent to the Entry Trigger field" |

---

### Composite Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 to C-30 | P | P | P | P | P |
| **C-31** | **P** | **P** | **½** | **½** | **½** |
| C-32 to C-45 | P | P | P | P | P |
| **C-46** | **P** | **P** | **P** | **P** | **P** |
| **C-47** | **P** | **P** | **P** | **P** | **P** |
| **Points** | **47.0** | **47.0** | **46.5** | **46.5** | **46.5** |
| **Score** | **100** | **100** | **99** | **99** | **99** |

*P = PASS (1.0), ½ = PARTIAL (0.5), F = FAIL (0); composite = (points / 47) × 100*

---

### Ranking

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| 1 | **V-01** | **100** | Inertia Framing — inline per-field FM-ID enforcement in SQ Declaration table |
| 1 | **V-02** | **100** | Output Format — "these two columns audit each other" mutual-auditing language |
| 3 | V-03 | 99 | Phrasing Register — C-31 regressed to prose-only for decision threshold operationalization |
| 3 | V-04 | 99 | Role Sequence + Inertia — C-31 column header omits concrete quoted decision example |
| 3 | V-05 | 99 | Lifecycle Emphasis — C-31 abbreviated to prose; block-format C-47 is strongest structural mechanism |

---

### Excellence Signals (from V-01 and V-02)

**Pattern 1 — Per-field anti-pattern in the SQ Declaration table:** V-01 places "'familiarity' or 'it works well enough' without specificity does not count" directly in the Inertia Driver field definition and equivalent rules in each FM field. This makes the declaration a structurally uncompletable document using decorative commentary — the anti-pattern fail is encountered at the cell level, before any downstream column header is reached. Future criteria building on incumbent-process anchoring should embed anti-pattern vocabulary inside the declaration itself, not only in the downstream columns that consume the FM-IDs.

**Pattern 2 — Naming the auditing relationship explicitly:** V-02 closes C-47's mutual-verification pressure by naming it as a design principle ("these two columns audit each other") rather than only enforcing the columns structurally. When the label appears in the column header at the exact point of use, authors encounter the reason for co-location before they fill either column — the structural dependency becomes a named relationship that cannot be satisfied by filling one column while ignoring the other. V-05's block format achieves the same principle via sequential field authoring; both are valid implementations.

**Pattern 3 — Maintaining full C-31 dual-mechanism operationalization when adopting imperative phrasing:** V-03 and V-05 (the imperative-phrasing variations) traded column-header verbosity for prose clarity. This caused C-31 regression: the concrete quoted example ("Invoice value > $10,000") disappeared from the column header into the prose, leaving format ambiguity unresolved at the column definition level. Future phrasing-register variations must preserve the concrete instantiation in the column header even when simplifying prose.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Per-field anti-pattern rules in the STATUS-QUO PROCESS DECLARATION table itself (not only in downstream column headers) make FM-IDs a live traceability anchor — each field definition names what does not count, preventing decorative-commentary completion at the source", "Explicit 'these two columns audit each other' language in the Status-Quo Gap column header names the C-47 mutual-verification pressure as a design principle at point of use, making the structural dependency visible to authors filling either column rather than discoverable only on scan"]}
```
