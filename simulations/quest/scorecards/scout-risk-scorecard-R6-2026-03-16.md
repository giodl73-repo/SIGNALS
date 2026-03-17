## scout-risk — Quest Score R6

### Per-Variation Criterion Evaluation

---

#### V-01 — Lifecycle Emphasis (Phase 2b standalone diversity audit)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | PASS | "mandatory, first" + "Do not skip it. Do not move it." |
| C-02 | Dimensional coverage enforced | PASS | "at least one risk each from 3 or more of these dimensions" |
| C-03 | Risk anatomy complete | PASS | Severity + IF/THEN likelihood + mitigation type + mitigation all required |
| C-04 | Severity correct scale | PASS | "HIGH, MEDIUM, or LOW — nothing else" on every entry |
| C-05 | Mitigations specific and actionable | PASS | 6-phrase forbidden list; "name what the team should do" |
| C-06 | Dimension-labeled | PASS | "Dimension: which of the five it belongs to" required |
| C-07 | Likelihood qualified beyond binary | PASS | IF [specific condition or scenario], THEN activates; no bare labels |
| C-08 | Ordered by priority | PASS | "Sort dimensional risks from highest to lowest severity" |
| C-09 | Interdependencies noted | PASS | Dedicated ## Risk Interdependencies section, >= 3 pairs |
| C-10 | AMEND behavior | PARTIAL | Phase 4 handles AMEND correctly; no live directive in base prompt |
| C-11 | Zero-generic mitigations | PASS | 6 enumerated forbidden phrases; replace-on-sight instruction |
| C-12 | All likelihoods trigger-qualified | PASS | IF/THEN required; no bare probability labels |
| C-13 | Interdependencies structured section >= 2 | PASS | Dedicated labeled section, >= 3 named pairings |
| C-14 | IF-THEN syntactic form | PASS | "IF [specific condition or scenario that triggers this risk], THEN this risk activates" |
| C-15 | Mitigation type with sub-field contracts | FAIL | Type label required but no sub-field contracts (Spike: Unknown/Time-box, etc.) absent |
| C-16 | Interdependency count >= 3 | PASS | "at least 3 named compound-risk pairings" required |
| C-17 | Severity-transition labels FROM/TO | PASS | "must state both the FROM severity… and the TO severity… stating only 'escalates to HIGH' without the origin severity is incomplete" |
| C-18 | Mitigation type portfolio >= 3 classes | PASS | Phase 2b requires >= 3 distinct type class names; repair loop if < 3 |
| C-19 | Enumerated forbidden-phrase list >= 3 | PASS | 6 named phrases: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options" |
| C-20 | Count failure triggers upstream revision | PASS | Phase 2b: "return to Phase 2 and revise"; Phase 3: "return to Phase 2 and make them more concrete" |
| C-21 | Repair-loop count = gate count | PASS | 2 gates (Phase 2b diversity, Phase 3 pair count) × 2 named repair loops — counts match |
| C-22 | Severity columns type-constrained at cell level | FAIL | Prose format: "escalates from [CURRENT SEVERITY] to [NEW SEVERITY]" — no column vocabulary rule |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 2+1+2+2+2+2+0+2+2+2+2+2+2+0 = 25

**V-01 Composite: 115** — Golden ✓

---

#### V-02 — Output Format (vocabulary-constrained typed columns)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | PASS | "mandatory, first" + "Do not skip it. Do not move it." |
| C-02 | Dimensional coverage enforced | PASS | "at least one risk each from 3 or more of these dimensions" |
| C-03 | Risk anatomy complete | PASS | All fields required in structured format |
| C-04 | Severity correct scale | PASS | "HIGH, MEDIUM, or LOW — nothing else" |
| C-05 | Mitigations specific and actionable | PASS | Forbidden phrase list + type contracts structurally prevent hedges |
| C-06 | Dimension-labeled | PASS | "Dimension: which of the five it belongs to" |
| C-07 | Likelihood qualified beyond binary | PASS | IF [specific condition or scenario], THEN activates |
| C-08 | Ordered by priority | PASS | "Sort dimensional risks from highest to lowest severity" |
| C-09 | Interdependencies noted | PASS | Dedicated ## Risk Interdependencies section, >= 3 pairs |
| C-10 | AMEND behavior | PARTIAL | Step 5 handles AMEND; no live directive in base prompt |
| C-11 | Zero-generic mitigations | PASS | 6 enumerated phrases + type contracts make generic hedges structurally impossible |
| C-12 | All likelihoods trigger-qualified | PASS | IF [specific condition or scenario], THEN activates |
| C-13 | Interdependencies structured section >= 2 | PASS | Table with >= 3 rows required |
| C-14 | IF-THEN syntactic form | PASS | "IF [specific condition or scenario], THEN this risk activates" |
| C-15 | Mitigation type with sub-field contracts | PASS | Full sub-field contracts in Steps 1 and 2: Spike: Unknown/Time-box; Gate: Criterion; Validate: Assumption/Method; Contract: Party/Commitment; Cut: Element/Scope effect; Instrument: Metric/Alert threshold |
| C-16 | Interdependency count >= 3 | PASS | "Minimum 3 rows required" |
| C-17 | Severity-transition labels FROM/TO | PASS | Separate From Severity / To Severity columns in table |
| C-18 | Mitigation type portfolio >= 3 classes | FAIL | No type diversity audit gate present — type contracts exist but no count minimum across entries |
| C-19 | Enumerated forbidden-phrase list >= 3 | PASS | 6 named forbidden phrases |
| C-20 | Count failure triggers upstream revision | PASS | "If fewer than 3 pairs are present, return to Step 2 and add or refine risk entries" |
| C-21 | Repair-loop count = gate count | PASS | 1 gate (pair count >= 3) × 1 repair loop — trivial match |
| C-22 | Severity columns type-constrained at cell level | PASS | "Vocabulary: must contain exactly one of {HIGH, MEDIUM, LOW}. These are the only permitted values. No other text is valid in this column." + "A cell containing 'MEDIUM → HIGH', 'escalates to HIGH', or any prose violates the vocabulary constraint." |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 2+1+2+2+2+2+2+2+2+0+2+2+2+2 = 27

**V-02 Composite: 117** — Golden ✓

---

#### V-03 — Phrasing Register (named Repair Loop A / Repair Loop B labels)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | PASS | "mandatory, first" + "Do not skip it. Do not move it." |
| C-02 | Dimensional coverage enforced | PASS | "Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline" |
| C-03 | Risk anatomy complete | PASS | All fields required: Dimension, Risk, Severity, IF/THEN, Mitigation type, Mitigation |
| C-04 | Severity correct scale | PASS | "HIGH, MEDIUM, or LOW — nothing else" |
| C-05 | Mitigations specific and actionable | PASS | "a concrete action" + 6-phrase forbidden list |
| C-06 | Dimension-labeled | PASS | "Dimension: [Technical / Market / Compliance / Dependency / Timeline]" |
| C-07 | Likelihood qualified beyond binary | PASS | IF [specific triggering condition], THEN activates; "No bare probability labels" |
| C-08 | Ordered by priority | PASS | "Sort entries from highest to lowest severity" |
| C-09 | Interdependencies noted | PASS | Dedicated ## Risk Interdependencies section, >= 3 pairs |
| C-10 | AMEND behavior | PARTIAL | Step 4 handles AMEND; no live directive |
| C-11 | Zero-generic mitigations | PASS | 6 enumerated forbidden phrases, replace-on-sight |
| C-12 | All likelihoods trigger-qualified | PASS | IF/THEN required; "No bare probability labels" |
| C-13 | Interdependencies structured section >= 2 | PASS | Dedicated labeled section, >= 3 named pairings |
| C-14 | IF-THEN syntactic form | PASS | "IF [specific triggering condition], THEN this risk activates" |
| C-15 | Mitigation type with sub-field contracts | FAIL | Type label required; no sub-field contracts |
| C-16 | Interdependency count >= 3 | PASS | "List at least 3 compound-risk pairings" required |
| C-17 | Severity-transition labels FROM/TO | PASS | "Every pairing must state both FROM severity… and TO severity… Stating only the destination ('escalates to HIGH') without the origin is incomplete." |
| C-18 | Mitigation type portfolio >= 3 classes | PASS | Repair Loop A: "Minimum required: 3 distinct type class names"; named repair instruction |
| C-19 | Enumerated forbidden-phrase list >= 3 | PASS | 6 named phrases |
| C-20 | Count failure triggers upstream revision | PASS | Repair Loop A: "return to Step 2 and revise mitigation type assignments"; Repair Loop B: "return to Step 2 and add or refine risk entries" |
| C-21 | Repair-loop count = gate count | PASS | 2 gates (Repair Loop A diversity, Repair Loop B pair count) × 2 named repair loops — explicit labeling makes count unambiguous |
| C-22 | Severity columns type-constrained at cell level | FAIL | Prose format: "escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY]" — no cell-level vocabulary rule |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 2+1+2+2+2+2+0+2+2+2+2+2+2+0 = 25

**V-03 Composite: 115** — Golden ✓

---

#### V-04 — Lifecycle + Output Format (C-21 + C-22 + C-15 combined)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | PASS | "mandatory, first" + "Do not skip it. Do not move it." |
| C-02 | Dimensional coverage enforced | PASS | "Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline" |
| C-03 | Risk anatomy complete | PASS | All fields in structured format |
| C-04 | Severity correct scale | PASS | "HIGH, MEDIUM, or LOW — nothing else" |
| C-05 | Mitigations specific and actionable | PASS | Forbidden phrase list + type contracts |
| C-06 | Dimension-labeled | PASS | "Dimension: [Technical / Market / Compliance / Dependency / Timeline]" |
| C-07 | Likelihood qualified beyond binary | PASS | IF [specific triggering condition], THEN activates |
| C-08 | Ordered by priority | PASS | "Sort entries from highest to lowest severity" |
| C-09 | Interdependencies noted | PASS | Dedicated table section, >= 3 rows required |
| C-10 | AMEND behavior | PARTIAL | Step 4 handles AMEND; no live directive |
| C-11 | Zero-generic mitigations | PASS | 6 forbidden phrases + type contracts |
| C-12 | All likelihoods trigger-qualified | PASS | IF/THEN required |
| C-13 | Interdependencies structured section >= 2 | PASS | Table with >= 3 rows |
| C-14 | IF-THEN syntactic form | PASS | "IF [specific triggering condition], THEN this risk activates" |
| C-15 | Mitigation type with sub-field contracts | PASS | Full sub-field contracts in Step 1 and Step 2: all 6 types defined with required named sub-fields |
| C-16 | Interdependency count >= 3 | PASS | "Minimum 3 rows required" |
| C-17 | Severity-transition labels FROM/TO | PASS | Separate From Severity / To Severity columns |
| C-18 | Mitigation type portfolio >= 3 classes | PASS | Step 2c: "Minimum required: 3 distinct type class names"; repair loop to Step 2 if < 3 |
| C-19 | Enumerated forbidden-phrase list >= 3 | PASS | 6 named phrases |
| C-20 | Count failure triggers upstream revision | PASS | Step 2c: "return to Step 2 and revise"; Step 3: "return to Step 2 and add or refine" |
| C-21 | Repair-loop count = gate count | PASS | 2 gates (Step 2c diversity, Step 3 pair count) × 2 repair loops — counts match |
| C-22 | Severity columns type-constrained at cell level | PASS | "Vocabulary: must contain exactly one of {HIGH, MEDIUM, LOW}. No other values are permitted." + "A prose entry ('escalates to HIGH', 'MEDIUM → HIGH') violates the vocabulary constraint." |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 2+1+2+2+2+2+2+2+2+2+2+2+2+2 = 27

**V-04 Composite: 117** — Golden ✓

---

#### V-05 — Full Integration (R4 V-05 base + STEP 2b + typed-column table)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | PASS | "mandatory, always first"; explicit format with row 0; STEP 4 self-check item |
| C-02 | Dimensional coverage enforced | PASS | "Cover at least 3 of the 5 dimensions" |
| C-03 | Risk anatomy complete | PASS | Full table schema with all fields; STEP 4 self-check verifies |
| C-04 | Severity correct scale | PASS | "HIGH / MEDIUM / LOW"; STEP 4 self-check item |
| C-05 | Mitigations specific and actionable | PASS | Forbidden phrase list + type contract structure makes hedges "structurally impossible" |
| C-06 | Dimension-labeled | PASS | Table column "Dimension" required |
| C-07 | Likelihood qualified beyond binary | PASS | Column header IS the IF-THEN template; bare labels "cannot satisfy a column that begins with 'IF'" |
| C-08 | Ordered by priority | PASS | "sorted by severity descending after inertia"; STEP 4 self-check item |
| C-09 | Interdependencies noted | PASS | Dedicated ## Risk Interdependencies table section; >= 3 rows |
| C-10 | AMEND behavior | PARTIAL | STEP 5 handles AMEND correctly; no live directive in base prompt |
| C-11 | Zero-generic mitigations | PASS | 6 enumerated forbidden phrases + sub-field contracts make generic text impossible; self-check item |
| C-12 | All likelihoods trigger-qualified | PASS | Column header template enforces IF/THEN; self-check: "Every likelihood cell starts with 'IF'" |
| C-13 | Interdependencies structured section >= 2 | PASS | Dedicated table with >= 3 rows; isolation rule ("Do not put interdependency notes inside individual rows") |
| C-14 | IF-THEN syntactic form | PASS | Column header template is "IF [condition], THEN risk activates"; STEP 4 self-check verifies every row |
| C-15 | Mitigation type with sub-field contracts | PASS | Full sub-field contracts for all 6 types; "type contract rule" makes incomplete entries detectable; STEP 4 self-check item |
| C-16 | Interdependency count >= 3 | PASS | "Minimum 3 rows required" in STEP 3 |
| C-17 | Severity-transition labels FROM/TO | PASS | Separate From Severity / To Severity columns; both required fields |
| C-18 | Mitigation type portfolio >= 3 classes | PASS | STEP 2b: "Minimum required: 3 distinct type class names"; repair loop to STEP 2; STEP 4 self-check item |
| C-19 | Enumerated forbidden-phrase list >= 3 | PASS | 6 named phrases in both STEP 2 rules and STEP 4 self-check |
| C-20 | Count failure triggers upstream revision | PASS | STEP 2b: "return to STEP 2 and revise mitigation type assignments"; STEP 3: "return to STEP 2 and add or refine risk entries" |
| C-21 | Repair-loop count = gate count | PASS | 2 gates (STEP 2b diversity, STEP 3 pair count) × 2 repair loops with named back-references — counts match |
| C-22 | Severity columns type-constrained at cell level | PASS | "Vocabulary constraint: must contain exactly one of {HIGH, MEDIUM, LOW}. These are the only permitted values in this column. No other text is valid." + cell-level violation examples + STEP 4 self-check items for both From and To columns |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 2+1+2+2+2+2+2+2+2+2+2+2+2+2 = 27

**V-05 Composite: 117** — Golden ✓

---

### Score Summary

| ID | Essential | Recommended | Aspirational | Composite | Golden |
|----|-----------|-------------|--------------|-----------|--------|
| V-01 | 60 | 30 | 25 | **115** | YES |
| V-02 | 60 | 30 | 27 | **117** | YES |
| V-03 | 60 | 30 | 25 | **115** | YES |
| V-04 | 60 | 30 | 27 | **117** | YES |
| V-05 | 60 | 30 | 27 | **117** | YES |

**Ceiling: 117** (C-10 PARTIAL irreducible on all base prompts; theoretical max 118 requires live AMEND directive)

**Ranking:** V-02 = V-04 = V-05 at 117; V-01 = V-03 at 115.

---

### Excellence Signals (top-scoring variations)

**Signal 1 — Self-check as constraint amplifier (V-05 exclusive)**
V-05 is the only variation whose STEP 4 self-check includes explicit cell-level items: "From Severity column: every cell contains exactly one of {HIGH, MEDIUM, LOW}" and "To Severity column: every cell contains exactly one of {HIGH, MEDIUM, LOW}." This pairs every structural rule with a verification item — the constraint is stated twice (at definition and at audit), doubling the probability that the model enforces it. Pattern: every typed column constraint should have a corresponding self-check item.

**Signal 2 — Column header as schema template eliminates class of error (V-05 exclusive)**
V-05's likelihood column header is literally "IF [condition], THEN risk activates" — not a prose instruction, but the template itself baked into the column name. The model filling the column must complete the template to produce a valid cell. This is stronger than any instruction because the column structure enforces the form at parse time, not at review time.

**Signal 3 — Type sub-field contracts compensate for absent diversity gate (V-02 trade-off)**
V-02 omits C-18 (no diversity gate) but still reaches 117 because C-15 (full type sub-field contracts, +2 pts) and C-22 (typed columns, +2 pts) exactly offset C-18's loss. Implication: type contracts and type diversity gate are partially substitutable — a register where every mitigation fulfills a named sub-field contract is less likely to be type-monoculture than one with only a label. The contracts create natural diversity pressure even without an explicit count gate.

---

```json
{"top_score": 117, "all_essential_pass": true, "new_patterns": ["Self-check as constraint amplifier: pairing every typed column rule with a corresponding self-check item doubles enforcement probability — V-05's STEP 4 includes explicit cell-level items for both From Severity and To Severity columns", "Column header as schema template: using the IF-THEN construct as the literal column header (not an instruction) forces template completion at cell-fill time rather than at review time, eliminating bare probability labels structurally", "Type sub-field contracts as diversity pressure: full named sub-field contracts (Spike: Unknown+Time-box, Gate: Criterion, etc.) create implicit diversity pressure even without an explicit count gate — structurally substitutable for C-18 when combined with C-22"]}
```
