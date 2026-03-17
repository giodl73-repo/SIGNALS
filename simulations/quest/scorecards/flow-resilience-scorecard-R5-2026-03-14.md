# flow-resilience — Round 5 Scoring (v5 Rubric)

## Variation Evaluation

---

### V-01 — Role Sequence: Commerce-First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | All three classes explicitly named and separated by role pass |
| **C-02** Four-Field Structure | PASS | State, Capability, Data at Risk, Recovery Path all in unified table |
| **C-03** Gap Identification | PASS | Three labeled findings: Offline Experience Gap, Data Consistency Violation, Missing Recovery Flow |
| **C-04** Distributed Systems Accuracy | PASS | DS Expert pass explicitly validates terminology and patterns |
| **C-05** Commerce Domain Grounding | PASS | Commerce Expert anchors each scenario to named operation before DS validation |
| **C-06** Severity + Blast Radius | PASS | DS Expert adds Severity and Blast Radius in explicit instructions |
| **C-17** Unified table index | PARTIAL | `#` column present; no explicit "unified index" framing or prohibition on splitting |
| **C-18** Section-level phase gate | FAIL | No instruction to complete table rows before advancing to Gap Register |
| **C-19** Slot-level in-row imperatives | FAIL | No bold imperatives embedded inside Content descriptors |
| **C-20** Column-level ownership | FAIL | Role ownership implied by section headers, not assigned per column structurally |
| **C-21** Layered Granularity Architecture | FAIL | Uses multiple levels implicitly but never names the four-level stack |
| **C-22** Anti-boundary by structural symptom | FAIL | "Do not split the table by scenario class or by expert role" — positive instruction only, no symptom-level negations naming specific artifacts |
| **C-23** In-row bold imperative | FAIL | No cell-embedded bold imperatives |

**Aspirational**: 1/15 × 10 = 0.67  
**Composite**: 60 + 30 + 0.67 = **90.7**

---

### V-02 — Output Format: Column-Ownership Table

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | Three classes named in scenario table specification |
| **C-02** Four-Field Structure | PASS | State, Capability, Data at Risk, Recovery Path all present as explicit columns |
| **C-03** Gap Identification | PASS | Three labeled gap findings with labeled structure required |
| **C-04** Distributed Systems Accuracy | PASS | D-owned columns mandate precise distributed systems vocabulary per fill requirement |
| **C-05** Commerce Domain Grounding | PASS | C-owned Scenario column requires named commerce operation; C-owned Blast Radius anchors to commerce segment |
| **C-06** Severity + Blast Radius | PASS | Severity and Blast Radius as dedicated columns with explicit owners |
| **C-17** Unified table index | PASS | `#` column present; "All eight columns appear in every row of a single unified table" prohibits split |
| **C-18** Section-level phase gate | PASS | "Produce all three rows before writing the Gap Register." — explicit sequencing gate |
| **C-19** Slot-level in-row imperatives | FAIL | No bold imperatives embedded inside cell Content descriptors |
| **C-20** Column-level ownership | PASS | Explicit meta-table assigning Owner per column — strongest C-20 implementation seen |
| **C-21** Layered Granularity Architecture | FAIL | Uses C-17 (#), C-18 (phase gate), C-20 (column ownership) but does not explicitly name the four-level stack as a coordinated architecture |
| **C-22** Anti-boundary by structural symptom | PASS | Two distinct symptom negations: "Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns" + "Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts" |
| **C-23** In-row bold imperative | FAIL | No cell-embedded bold imperatives |

**Aspirational**: 4/15 × 10 = 2.67  
**Composite**: 60 + 30 + 2.67 = **92.7**

---

### V-03 — Phrasing Register: Imperative Direct

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Scenario Coverage | PASS | Scenarios A, B, C map to the three classes explicitly |
| **C-02** Four-Field Structure | PASS | All four fields in table; fill requirements listed per column |
| **C-03** Gap Identification | PASS | "Write exactly three findings. Use these labels exactly:" — prescriptive structure |
| **C-04** Distributed Systems Accuracy | PASS | "Use distributed systems vocabulary. Name the partition, the consistency guarantee in effect" |
| **C-05** Commerce Domain Grounding | PASS | Step 1 forces naming a specific operation before table construction begins |
| **C-06** Severity + Blast Radius | PASS | Severity and Blast Radius in table with explicit fill requirements |
| **C-17** Unified table index | PARTIAL | `#` column present; "Place all three rows in one table" — correct instruction, no explicit framing as anti-omission mechanism |
| **C-18** Section-level phase gate | PASS | "Fill all three rows before advancing." — explicit phase gate |
| **C-19** Slot-level in-row imperatives | FAIL | No cell-embedded bold imperatives |
| **C-20** Column-level ownership | FAIL | No per-column owner assignment |
| **C-21** Layered Granularity Architecture | FAIL | Phase gate present but no four-level stack naming |
| **C-22** Anti-boundary by structural symptom | PARTIAL | "Do not start a new table for each scenario" — one negation, one structural artifact named. Second symptom absent. |
| **C-23** In-row bold imperative | FAIL | No cell-embedded bold imperatives |

**Aspirational**: 2/15 × 10 = 1.33  
**Composite**: 60 + 30 + 1.33 = **91.3**

---

## Ranking

| Rank | Variation | Composite | Delta vs V-05 (v5) |
|------|-----------|-----------|---------------------|
| 1 | V-02 | 92.7 | −5.3 vs 98.0 |
| 2 | V-03 | 91.3 | −6.7 |
| 3 | V-01 | 90.7 | −7.3 |

---

## Excellence Signals from V-02

**E-8 — Column-ownership meta-table as pre-output specification**  
V-02 introduces a separate meta-table (Name / Owner / Fill Requirement) before the output table itself. This creates structural pre-commitment: the model processes per-column responsibility before constructing any row, making column omission detectable as a contract violation rather than an oversight. This is a stronger form of C-20 than role-section headers or parenthetical labels.

**E-9 — Two-symptom anti-boundary negation pattern**  
V-02 achieves C-22 by naming two distinct structural artifacts that must not appear: (1) "separate tables for Commerce Expert columns and Distributed Systems Expert columns" and (2) "a horizontal rule, heading, or section break between rows when column ownership shifts." The pairing matters: the first negation addresses table splitting, the second addresses invisible boundary insertion. A model that satisfies negation-1 by consolidating tables could still insert a `---` separator; negation-2 closes that escape route. Single-symptom instructions (V-01, V-03) leave one or more escape routes open.

**Remaining gap to ceiling (C-21, C-23)**  
No Round 5 variation explicitly names the four anti-omission levels as a coordinated architecture (C-21), and no variation embeds bold imperatives inside Content descriptor cells (C-23). Both remain open for Round 6.

---

```json
{"top_score": 92.7, "all_essential_pass": true, "new_patterns": ["column-ownership meta-table as pre-output specification — separate Name/Owner/Fill-Requirement table before output table creates per-column responsibility before row construction begins", "two-symptom anti-boundary negation — naming two distinct structural artifacts to avoid (separate table + horizontal rule/heading/section break) closes escape routes that single-symptom or positive-only instructions leave open"]}
```
