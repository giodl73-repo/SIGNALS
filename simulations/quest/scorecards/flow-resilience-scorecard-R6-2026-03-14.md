# flow-resilience — Round 6 Scoring

## Results

| Rank | Variation | Composite | New Criteria | Delta |
|------|-----------|-----------|--------------|-------|
| 1 | **V-05** | **94.71** | C-21 + C-23 + C-24 | +1.77 |
| 2 | **V-04** | **94.12** | C-21 + C-24 | +1.18 |
| 3 | V-01 | 93.53 | C-24 | +0.59 |
| 3 | V-02 | 93.53 | C-21 | +0.59 |
| 3 | V-03 | 93.53 | C-23 | +0.59 |

R5 ceiling: 92.94 → R6 ceiling: **94.71** (+1.77)

## Key decisions

**V-01 C-24 PASS**: Two discrete structures — standalone `Column Contract` meta-table followed by a separate blank `Scenario Analysis Table` template. This is what R5 V-02 lacked (one table, not two).

**V-02 C-21 PASS**: `Four-Level Anti-Omission Architecture` section names all four levels (Table / Section / Column / Slot) with Name, Mechanism, and Omission Risk Addressed per row. "No two levels duplicate each other's function" makes it coordinated.

**V-03 C-23 PASS / C-19 FAIL**: Row Descriptors with `**Write this row now.**` + `**Do not advance to Row N until...**` satisfy C-23 (genuine slot-level co-location). C-19 requires imperative inside a per-row *field table schema*, not a prose section — that distinction keeps C-19 open.

**V-05**: Stacks all three. Architecture table's Slot level entry explicitly describes the Row Descriptors mechanism that follows — the architecture anticipates its own artifacts.

## Excellence signals for R7

- **E-10** — Architecture-to-contract forward reference: architecture table names downstream artifacts by section title, creating a closed-loop verifiable chain
- **E-11** — Consequence-enumeration in slot descriptors: Row 3 descriptor names business consequences *per resolution outcome* before the fill (oversell if A wins, double-charge if B wins), elevating fill requirement from content spec to outcome spec

**C-19 remains the R7 ceiling criterion** — closing it requires imperatives inside a per-row field table structure, not prose adjacent to the output table.

```json
{"top_score": 94.71, "all_essential_pass": true, "new_patterns": ["architecture-to-contract forward reference — architecture table Mechanism column names the downstream contract artifact by section title (e.g., 'defined in the Column Contract (below)'), creating a verifiable closed-loop chain between design intent and specification", "consequence-enumeration in slot-level descriptors — Row Descriptors name the business consequence of each possible resolution outcome before the fill happens (oversell if A wins, double-charge if B wins, duplicate fulfillment if merge is naive), making vague fills visibly inadequate against named stakes"]}
```
umn Contract" section is a standalone meta-table (Column / Owner / Fill Requirement) covering all 8 output columns, positioned before the separate blank "Scenario Analysis Table" template — two discrete structures satisfy the pass condition |
| **C-25** Two-Symptom Anti-Boundary Negation (E-9) | PASS | Negation-1 (table splitting) + Negation-2 (horizontal rule / heading / section break) address different boundary mechanisms |

**Aspirational passes**: C-17, C-18, C-20, C-22, C-24, C-25 = 6/17 x 10 = **3.53**
**Composite**: 60 + 30 + 3.53 = **93.53**

---

### V-02 — Anti-Omission Architecture: Explicit Four-Level Stack Naming (C-21 only)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | Class 1 / Class 2 / Class 3 explicitly named |
| **C-02** Four-Field Structure | PASS | State, Capability, Data at Risk, Recovery Path as explicit columns with fill requirements |
| **C-03** Gap Identification | PASS | Three labeled Gap Register findings required |
| **C-04** Distributed Systems Accuracy | PASS | D-owned columns require partition state, service health, named consistency guarantee, named recovery pattern |
| **C-05** Commerce Domain Grounding | PASS | Scenario column requires named commerce operation; Blast Radius anchors to commerce segment |
| **C-06** Severity + Blast Radius | PASS | Severity (D) and Blast Radius (C) as explicit columns |
| **C-17** Unified Table Index | PASS | `#` column + "All eight columns appear in every row of a single unified table" |
| **C-18** Section-Level Phase Gate | PASS | "Produce all three rows before writing the Gap Register." |
| **C-19** Slot-Level In-Row Imperatives | FAIL | No Row Descriptors; no bold imperatives at row granularity |
| **C-20** Column-Level Ownership | PASS | Per-column Owner in column specification table; all 8 columns covered |
| **C-21** Layered Granularity Architecture (E-5) | PASS | "Four-Level Anti-Omission Architecture" section present; names all four levels (Table, Section, Column, Slot) explicitly with Level / Name / Mechanism / Omission Risk Addressed per row; statement "No two levels duplicate each other's function" makes the architecture coordinated rather than incidental |
| **C-22** Anti-Boundary by Structural Symptom | PASS | Two symptom negations: separate-tables + horizontal rule / heading / section break |
| **C-23** In-Row Bold Imperative (E-7) | FAIL | No Row Descriptors; no cell-embedded bold imperatives |
| **C-24** Column-Ownership Meta-Table Pre-Output (E-8) | FAIL | Column spec table present but serves as instruction block only — no separate blank output table template follows it; C-24 requires two discrete structures (meta-table + output template); V-02 has one |
| **C-25** Two-Symptom Anti-Boundary Negation (E-9) | PASS | Negation-1 + Negation-2 address different boundary mechanisms |

**Aspirational passes**: C-17, C-18, C-20, C-21, C-22, C-25 = 6/17 x 10 = **3.53**
**Composite**: 60 + 30 + 3.53 = **93.53**

---

### V-03 — Phrasing Register: Slot-Level Bold Imperatives (C-23 only)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | Class 1 / Class 2 / Class 3 named |
| **C-02** Four-Field Structure | PASS | State, Capability, Data at Risk, Recovery Path as explicit columns |
| **C-03** Gap Identification | PASS | Three labeled findings required in Gap Register; section gate confirms completion before entry |
| **C-04** Distributed Systems Accuracy | PASS | D-owned columns require named partition state, consistency guarantee, recovery pattern |
| **C-05** Commerce Domain Grounding | PASS | Scenario column requires specific commerce operation; Row 2 descriptor names specific downstream services (inventory service, payment gateway, fulfillment orchestrator) |
| **C-06** Severity + Blast Radius | PASS | Dedicated Severity and Blast Radius columns with owners |
| **C-17** Unified Table Index | PASS | `#` column present; anti-split instruction present |
| **C-18** Section-Level Phase Gate | PASS | "Produce all three rows before writing the Gap Register." + section gate in Gap Register preamble |
| **C-19** Slot-Level In-Row Imperatives | FAIL | Row Descriptors appear as a prose section after the column spec table, not as structured field descriptors inside a per-row table schema; C-19 requires the imperative inside a per-row field table structure; prose section adjacent to the output table does not satisfy this criterion |
| **C-20** Column-Level Ownership | PASS | Per-column Owner in column specification table |
| **C-21** Layered Granularity Architecture (E-5) | FAIL | No Four-Level Anti-Omission Architecture section |
| **C-22** Anti-Boundary by Structural Symptom | PASS | Two symptom negations: separate-tables + horizontal rule / heading / section break |
| **C-23** In-Row Bold Imperative (E-7) | PASS | Row Descriptors section contains "**Write this row now.**" followed by per-row fill requirements, followed by "**Do not advance to Row N until all eight columns for Row N contain non-placeholder content.**" for all three rows; imperatives are co-located at row granularity, one per row; explicit framing "the bold imperative in each descriptor is load-bearing — it is not decoration" confirms genuine slot-level intent |
| **C-24** Column-Ownership Meta-Table Pre-Output (E-8) | FAIL | Column spec table in "Scenario Analysis Table" section serves as both contract and instruction block; no separate blank output table template follows — one structure, not two |
| **C-25** Two-Symptom Anti-Boundary Negation (E-9) | PASS | Negation-1 + Negation-2 address different boundary mechanisms |

**Aspirational passes**: C-17, C-18, C-20, C-22, C-23, C-25 = 6/17 x 10 = **3.53**
**Composite**: 60 + 30 + 3.53 = **93.53**

---

### V-04 — Combined: Pre-Output Meta-Table + Four-Level Architecture (C-24 + C-21)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | Class 1 / Class 2 / Class 3 named |
| **C-02** Four-Field Structure | PASS | All four fields as explicit columns with fill requirements |
| **C-03** Gap Identification | PASS | Three labeled Gap Register findings |
| **C-04** Distributed Systems Accuracy | PASS | D-owned columns mandate DS vocabulary |
| **C-05** Commerce Domain Grounding | PASS | Commerce operation required in Scenario column |
| **C-06** Severity + Blast Radius | PASS | Dedicated Severity and Blast Radius columns |
| **C-17** Unified Table Index | PASS | `#` column + anti-split instruction |
| **C-18** Section-Level Phase Gate | PASS | "Produce all three rows before writing the Gap Register." |
| **C-19** Slot-Level In-Row Imperatives | FAIL | No Row Descriptors section |
| **C-20** Column-Level Ownership | PASS | Column Contract assigns Owner per column; architecture table references "Per-column expert-role label defined in the Column Contract" — cross-linking between architecture and contract |
| **C-21** Layered Granularity Architecture (E-5) | PASS | "Four-Level Anti-Omission Architecture" section names all four levels (Table, Section, Column, Slot) with Name, Mechanism, and Omission Risk Addressed per level |
| **C-22** Anti-Boundary by Structural Symptom | PASS | Two symptom negations present |
| **C-23** In-Row Bold Imperative (E-7) | FAIL | No Row Descriptors; no cell-embedded bold imperatives |
| **C-24** Column-Ownership Meta-Table Pre-Output (E-8) | PASS | "Column Contract" standalone meta-table (Column / Owner / Fill Requirement) covering all 8 columns, followed by separate "Scenario Analysis Table" blank template with empty rows — two distinct structures, meta-table before output table |
| **C-25** Two-Symptom Anti-Boundary Negation (E-9) | PASS | Negation-1 + Negation-2 address different boundary mechanisms |

**Aspirational passes**: C-17, C-18, C-20, C-21, C-22, C-24, C-25 = 7/17 x 10 = **4.12**
**Composite**: 60 + 30 + 4.12 = **94.12**

---

### V-05 — Ceiling Attempt: Four-Level Architecture + Slot Imperatives + Pre-Output Meta-Table (C-21 + C-23 + C-24)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | Class 1 / Class 2 / Class 3 named |
| **C-02** Four-Field Structure | PASS | All four fields as explicit columns with fill requirements in Column Contract |
| **C-03** Gap Identification | PASS | Three labeled Gap Register findings; section gate requires confirming all rows complete before advancing |
| **C-04** Distributed Systems Accuracy | PASS | D-owned columns mandate DS vocabulary; Row Descriptors require conflict window duration and named resolution policy |
| **C-05** Commerce Domain Grounding | PASS | Row Descriptors require specific commerce operation per row; Row 3 descriptor names inventory count, cart total, order status, coupon redemption as candidate entities |
| **C-06** Severity + Blast Radius | PASS | Dedicated Severity and Blast Radius columns; Row Descriptors enumerate "degraded / impaired / down" |
| **C-17** Unified Table Index | PASS | `#` column + "All eight columns appear in every row of this single unified table" |
| **C-18** Section-Level Phase Gate | PASS | "Produce all three rows before writing the Gap Register." + section gate: "confirm all three rows are present and all eight columns are filled in every row. If any cell is missing, fill it before continuing." |
| **C-19** Slot-Level In-Row Imperatives | FAIL | Row Descriptors are a prose section positioned after the output table; the structural distinction from C-23 stands — C-19 requires the imperative inside a per-row field descriptor table at cell granularity, not a prose section adjacent to the table |
| **C-20** Column-Level Ownership | PASS | Column Contract assigns Owner per column; architecture table entry for Column level explicitly states "Per-column expert-role label defined in the Column Contract (below)" — forward reference links architecture to contract |
| **C-21** Layered Granularity Architecture (E-5) | PASS | "Four-Level Anti-Omission Architecture" section names all four levels (Table, Section, Column, Slot) with Level / Name / Mechanism / Omission Risk Addressed; Slot level entry describes "Bold 'Write this row now.' / 'Do not advance' embedded in each row's Content descriptor" — the architecture anticipates and names the Row Descriptors mechanism that follows |
| **C-22** Anti-Boundary by Structural Symptom | PASS | Two symptom negations: separate-tables + horizontal rule / heading / section break |
| **C-23** In-Row Bold Imperative (E-7) | PASS | Row Descriptors section contains "**Write this row now.**" + per-row fill requirements + "**Do not advance to Row N until...**" for all three rows; preamble states "Each bold imperative is co-located at the row it governs — it is not a section-level instruction. Read it at the moment you construct that row." — explicit co-location framing distinguishes from section-level or preamble instructions |
| **C-24** Column-Ownership Meta-Table Pre-Output (E-8) | PASS | "Column Contract" standalone meta-table (Column / Owner / Fill Requirement) covering all 8 columns, followed by separate "Scenario Analysis Table" blank template — two discrete structures, meta-table before output table |
| **C-25** Two-Symptom Anti-Boundary Negation (E-9) | PASS | Negation-1 (table splitting) + Negation-2 (horizontal rule / heading / section break) address different boundary mechanisms |

**Aspirational passes**: C-17, C-18, C-20, C-21, C-22, C-23, C-24, C-25 = 8/17 x 10 = **4.71**
**Composite**: 60 + 30 + 4.71 = **94.71**

---

## Ranking

| Rank | Variation | Composite | New Criteria Passed | Delta vs R5 Ceiling |
|------|-----------|-----------|---------------------|---------------------|
| 1 | **V-05** | **94.71** | C-21, C-23, C-24 | +1.77 |
| 2 | **V-04** | **94.12** | C-21, C-24 | +1.18 |
| 3 | V-01 | 93.53 | C-24 | +0.59 |
| 3 | V-02 | 93.53 | C-21 | +0.59 |
| 3 | V-03 | 93.53 | C-23 | +0.59 |

R5 ceiling (V-02, under v6): 92.94
R6 ceiling (V-05): **94.71** (+1.77)

---

## Excellence Signals from V-05

**E-10 — Architecture-to-Contract Forward Reference**
The Four-Level Anti-Omission Architecture table's Column level entry reads "Per-column expert-role label defined in the Column Contract (below)" — a named forward reference from the architecture to the contract artifact. This creates a verifiable design chain: the architecture claims the Column Contract exists and describes its function; the Column Contract that follows must fulfill that claim. A reviewer can check the architecture against the contract without searching. No prior round's top variation made this cross-link explicit. The pattern generalizes: an architecture section that names its downstream artifacts by section title creates a closed-loop specification that cannot be satisfied by removing either component.

**E-11 — Consequence-Enumeration in Slot-Level Descriptors**
V-05's Row 3 descriptor names the business consequence of each possible conflict-resolution outcome before requiring the fill: "state the business consequence of each resolution outcome (oversell if A wins, double-charge if B wins, duplicate fulfillment if merge is naive)." This is a consequence-first slot specification — the descriptor names what is at stake before the model fills the cell, making a vague or generic recovery path answer visibly inadequate against the named stakes. Prior Row Descriptors specified what to fill; this descriptor specifies what the consequences of each fill option are, elevating the fill requirement from content specification to outcome specification.

**Remaining gap entering R7**
C-19 (slot-level imperatives inside a per-row field descriptor table) remains open. The Row Descriptors approach passes C-23 but not C-19. To close C-19, the imperative must appear inside a structured per-row table (e.g., a Field | Content | Imperative table format) at cell granularity, not as prose adjacent to the output table. This is the ceiling criterion for R7.

---

```json
{"top_score": 94.71, "all_essential_pass": true, "new_patterns": ["architecture-to-contract forward reference — architecture table Mechanism column names the downstream contract artifact by section title (e.g., 'defined in the Column Contract (below)'), creating a verifiable closed-loop chain between design intent and specification", "consequence-enumeration in slot-level descriptors — Row Descriptors name the business consequence of each possible resolution outcome before the fill happens (oversell if A wins, double-charge if B wins, duplicate fulfillment if merge is naive), making vague fills visibly inadequate against named stakes"]}
```
