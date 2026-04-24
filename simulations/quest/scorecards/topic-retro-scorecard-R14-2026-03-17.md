**Round 14 scoring complete.** Here are the results:

---

## topic-retro R14 — Scores (rubric v12, denominator 140)

| Rank | Variation | Score | % |
|------|-----------|-------|---|
| 1 | **V-05** Bidirectional Cross-linking | **120/140** | 85.7% |
| 2 | **V-01** Full Tabular | **117/140** | 83.6% |
| 3 | **V-04** Lifecycle + Inertia | **115/140** | 82.1% |
| 4 | **V-02** Echo-Anchored | **110/140** | 78.6% |
| 5 | **V-03** Conversational | **106/140** | 75.7% |

**All essential: PASS** | **all_essential_pass: true**

---

**V-05 wins** on the strength of two differentiators over V-01 (which also PASS C-34/C-35):
- **C-21 PARTIAL** — Phase 8 SEAL FIELD CROSS-LINK TABLE + Bidirectional Audit Checklist (V-01: FAIL)
- **C-24 PARTIAL** — Echo Table "Why Not a Gap / Why Not a Wrong Prediction" exclusion fields (V-01: FAIL — no prior-belief field at all)
- **C-27 PARTIAL** — Checklist covers all output phases (V-01: FAIL)

**V-04** is the strongest on inertia-adjacent criteria (C-13/C-20/C-26/C-27 all PARTIAL via phase boundary protocol), but trades off all of C-32/C-33/C-34/C-35 by not having a Design Guarantees table.

**Two new patterns** from V-05 for potential Round 15 criteria:
1. **Three-pass architectural isolation** — C-12 compliance as a structural property, not a post-hoc rule
2. **Accuracy reconciliation cross-check** — Forward/Backward pass ratios compared; not yet captured by any criterion

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Three-pass architectural isolation...", "Accuracy reconciliation cross-check..."]}
```
| V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-01 Essential: One Echo named, unexpected, actionable | PASS | PASS | PASS | PASS | PASS | All have Echo section with naming and disqualification rule |
| C-02 Essential: Wrong verdicts identified | PASS | PASS | PASS | PASS | PASS | All have accuracy table with WRONG verdict + paragraph explanations |
| C-03 Essential: Gap analysis present | PASS | PASS | PASS | PASS | PASS | All have dedicated gap section |
| C-04 Essential: One Echo, framed as unexpected | PASS | PASS | PASS | PASS | PASS | All: disqualification rule for wrong-as-Echo; ECHO: NONE option |
| C-05 Essential: Topic/commitment context | PASS | PASS | PASS | PASS | PASS | All: PRE-EXECUTION CONTRACT or Opening establishes topic/commitment |
| C-06 Recommended: Signal coverage summary | PASS | PASS | PASS | PASS | PASS | All have 9-namespace coverage table |
| C-07 Recommended: Recommendation tied to gaps/Echo | PASS | PASS | PASS | PASS | PASS | All have "Addresses: [Gap:] OR [Echo:]" linkage |
| C-08 Recommended: Accuracy ratio stated | PASS | PASS | PASS | PASS | PASS | All have "N_CORRECT / N_TOTAL = X%" or equivalent |
| C-09 Echo linked to systemic pattern | PASS | PASS | PASS | PASS | PASS | All have Systemic Pattern field in Echo section |
| C-10 AMEND scope declared/enforced | N/A | N/A | N/A | N/A | N/A | Non-AMEND run |
| C-11 Systemic Pattern Echo field (named structural) | **PASS** | **PASS** | **PARTIAL** | **PASS** | **PASS** | V-03: prose ("name the systemic pattern"), no labeled structural field |
| C-12 Three-way isolation | PASS | PASS | PASS | PASS | PASS | All have isolation between wrong/gap/echo; V-02/V-04/V-05 have explicit checklists |
| C-13 Inertia framing for gaps | **FAIL** | **FAIL** | **FAIL** | **PARTIAL** | **FAIL** | V-04: "Inertia Impact: WOULD-DISPLACE/CONFIRM" column is closest; others name outcomes only |
| C-14 Verdict label explicit, not prose | PASS | PASS | PASS | PASS | PASS | All have enumerated verdict column (CORRECT/WRONG/PARTIAL/...) |
| C-15 Accuracy ratio not just count | PASS | PASS | PASS | PASS | PASS | All have N/M = X% form |
| C-16 Namespace coverage table (9 rows explicit) | PASS | PASS | PASS | PASS | PASS | All have explicit 9-row table |
| C-17 Recommendation bracket-slot template | **PASS** | **PASS** | **PARTIAL** | **PASS** | **PASS** | V-03: narrative instructions, not a bracket-slot template |
| C-18 Echo systemic pattern named (not blank/restatement) | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | All have the field with description; none constrain against blank or restatement explicitly |
| C-19 Phase completion self-contained | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | Tabular rows self-contained; non-tabular sections lack structural prevention across all variations |
| C-20 Gap inertia assumption named | **FAIL** | **FAIL** | **FAIL** | **PARTIAL** | **FAIL** | V-04: "Inertia Impact" column is dedicated but captures effect, not the assumption itself |
| C-21 Phase seal explicit | **FAIL** | **FAIL** | **FAIL** | **PARTIAL** | **PARTIAL** | V-04: exit conditions enumerate required fields per phase; V-05: Phase 8 SEAL CROSS-LINK TABLE + Bidirectional Audit Checklist |
| C-22 OOS secondary table | N/A | N/A | N/A | N/A | N/A | Non-AMEND run |
| C-23 Phase seal format strings per field | FAIL | FAIL | FAIL | FAIL | FAIL | No variation has per-seal-field format string contracts |
| C-24 Echo why-unexpected explained | **FAIL** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PARTIAL** | V-01: Echo Table has no "prior belief" field; V-02: "Why it wasn't foreseeable" present but prior-belief-contradiction framing incomplete; V-04: Signal Family Blind Spot addresses structural blindness; V-05: "Why Not a Gap/Wrong" are exclusion fields, not prior-belief |
| C-25 Recommendation outcome measurable | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | All have gap/echo linkage + practice change + trigger; none specify measurable outcome |
| C-26 Gap inertia column structurally isolated | **FAIL** | **FAIL** | **FAIL** | **PARTIAL** | **FAIL** | V-04: "Would Have Revealed" (outcome) + "Inertia Impact" (effect) are two separate columns; V-01/V-02/V-05: outcome-only |
| C-27 Phase self-containment extended to all phases | **FAIL** | **FAIL** | **FAIL** | **PARTIAL** | **PARTIAL** | V-04: exit conditions cover all 6 phases; V-05: Bidirectional Audit Checklist covers all output tables |
| C-28 Recommendation slot completeness guard | PARTIAL | PARTIAL | **FAIL** | PARTIAL | PARTIAL | V-03: no bracket-slot template at all; others have template but no SEAL guard for placeholder check |
| C-29 Phase 8 score copy guard | FAIL | FAIL | FAIL | FAIL | FAIL | No variation has "do not recompute" copy instruction for final accuracy score |
| C-30 Phase 8 SEAL copy-verified label + source | FAIL | FAIL | FAIL | FAIL | FAIL | No variation has COPY-VERIFIED label or named copy-source in a Phase 8 SEAL |
| C-31 Design guarantees summary explicit | **PASS** | **PARTIAL** | **FAIL** | **PARTIAL** | **PASS** | V-01: explicit SECTION 5 "Design Guarantees Table"; V-05: Phase 8 SEAL FIELD CROSS-LINK TABLE; V-02: THREE-WAY ISOLATION CHECK partial proxy; V-04: phase boundary protocol partial proxy; V-03: nothing |
| C-32 Phase 8 SEAL fields independent verification | **PASS** | **FAIL** | **FAIL** | **FAIL** | **PASS** | V-01: "Verification Instructions" column per SEAL field row, independent check specified; V-05: CHECK + HOW columns per SEAL field; V-02/V-03/V-04: no per-field verification structure |
| C-33 Design guarantees section mechanism-keyed table | **PARTIAL** | **FAIL** | **FAIL** | **FAIL** | **PARTIAL** | V-01/V-05: tables present but SEAL Field is the row key, not Mechanism; two-column mechanism-as-row-key form not achieved |
| C-34 Phase 8 SEAL items cross-reference contract mechanism | **PASS** | **FAIL** | **FAIL** | **FAIL** | **PASS** | V-01/V-05: explicit Cross-reference column "Cross-reference: PRE-EXECUTION CONTRACT [mechanism]" per SEAL row |
| C-35 Design guarantees table one row per SEAL field | **PASS** | **FAIL** | **FAIL** | **FAIL** | **PASS** | V-01: "one row. Do not collapse SEAL fields into groups"; V-05: "One row per Phase 8 SEAL field. Do not collapse." |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (50 applicable) | Raw | / 140 |
|-----------|---------------|-----------------|------------------------------|-----|-------|
| V-01 | 60 | 30 | 27 | **117** | 83.6% |
| V-02 | 60 | 30 | 20 | **110** | 78.6% |
| V-03 | 60 | 30 | 16 | **106** | 75.7% |
| V-04 | 60 | 30 | 25 | **115** | 82.1% |
| V-05 | 60 | 30 | 30 | **120** | 85.7% |

**Rank**: V-05 (120) > V-01 (117) > V-04 (115) > V-02 (110) > V-03 (106)

**Aspirational breakdown (non-N/A criteria: C-09, C-11–C-21, C-23–C-35 = 25 criteria × 2 = 50 pts applicable):**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 2 | 2 | 2 | 2 | 2 |
| C-11 | 2 | 2 | 1 | 2 | 2 |
| C-12 | 2 | 2 | 2 | 2 | 2 |
| C-13 | 0 | 0 | 0 | 1 | 0 |
| C-14 | 2 | 2 | 2 | 2 | 2 |
| C-15 | 2 | 2 | 2 | 2 | 2 |
| C-16 | 2 | 2 | 2 | 2 | 2 |
| C-17 | 2 | 2 | 1 | 2 | 2 |
| C-18 | 1 | 1 | 1 | 1 | 1 |
| C-19 | 1 | 1 | 1 | 1 | 1 |
| C-20 | 0 | 0 | 0 | 1 | 0 |
| C-21 | 0 | 0 | 0 | 1 | 1 |
| C-23 | 0 | 0 | 0 | 0 | 0 |
| C-24 | 0 | 1 | 1 | 1 | 1 |
| C-25 | 1 | 1 | 1 | 1 | 1 |
| C-26 | 0 | 0 | 0 | 1 | 0 |
| C-27 | 0 | 0 | 0 | 1 | 1 |
| C-28 | 1 | 1 | 0 | 1 | 1 |
| C-29 | 0 | 0 | 0 | 0 | 0 |
| C-30 | 0 | 0 | 0 | 0 | 0 |
| C-31 | 2 | 1 | 0 | 1 | 2 |
| C-32 | 2 | 0 | 0 | 0 | 2 |
| C-33 | 1 | 0 | 0 | 0 | 1 |
| C-34 | 2 | 0 | 0 | 0 | 2 |
| C-35 | 2 | 0 | 0 | 0 | 2 |
| **Total** | **27** | **20** | **16** | **25** | **30** |

---

## Ranking Detail

**Tier 1:**
- **V-05 (120)** — Three-pass bidirectional structure (Forward → Backward → Classification) enforces three-way isolation architecturally: gaps and echoes are separated during Pass 3 by the structural test "was a signal type available?" rather than post-hoc rules. PHASE 8 SEAL FIELD CROSS-LINK TABLE with CHECK/HOW columns achieves C-32 PASS and C-34/C-35 PASS. Mechanism-keyed PRE-EXECUTION CONTRACT table enables per-table Cross-reference column throughout. Bidirectional Audit Checklist adds C-21/C-27 PARTIAL. The three-pass structure uniquely enables C-24 PARTIAL via "Why Not a Gap / Why Not a Wrong Prediction" exclusion analysis in the Echo Table.

- **V-01 (117)** — Full tabular structure achieves C-32/C-34/C-35 PASS through SECTION 5 Design Guarantees Table. Simpler prompt design than V-05. Loses 3 pts vs V-05 on C-21, C-24, C-27 (all FAIL): no phase-level seals, no Echo prior-belief field, no all-phases self-containment coverage.

**Tier 2:**
- **V-04 (115)** — Inertia framing captures inertia-adjacent criteria (C-13/C-20/C-26 all PARTIAL; C-21/C-27 PARTIAL via phase boundary protocol). Best variation for criteria C-13 through C-27 that require gap-level assumption framing. Trades off structural C-32/C-33/C-34/C-35 coverage (all FAIL) for inertia depth. A synthesis with V-05 would be stronger.

**Tier 3:**
- **V-02 (110)** — Echo-first discovery before accuracy scoring produces structural C-12 compliance and C-24 PARTIAL via "Why it wasn't foreseeable" field. Loses heavily on C-32/C-34/C-35 (all FAIL) — no Design Guarantees table or Phase 8 SEAL structure.

- **V-03 (106)** — Conversational register produces readable prose but fails structural criteria: C-11 PARTIAL (systemic pattern not a labeled field), C-17 PARTIAL (no bracket-slot template), C-28 FAIL (no template, no guard). Lowest score because phrasing register cannot substitute for structural encoding.

---

## Excellence Signals from V-05

**V-05 differentiator — Three-pass architectural isolation (Forward → Backward → Classification):**
Pass 3 classifies each UNPREDICTED finding as GAP / ECHO-CANDIDATE / NEITHER using the explicit test "Was a signal type available?" before any Echo is named. This makes C-12 (three-way isolation) an architectural property of the processing order — gaps and echoes are separated during classification, not after naming. V-01 through V-04 achieve C-12 through rules ("A wrong prediction restated as the Echo is disqualified"); V-05 achieves it through structure. Architectural compliance is more robust: the structural test prevents misclassification even if the rule is ignored.

**V-05 differentiator — Accuracy reconciliation cross-check:**
Pass 2 ends with: "Cross-check: Does this ratio match the forward pass accuracy? If not, explain the discrepancy." This makes the accuracy computation auditable against itself — a reviewer can verify the backward-pass ratio equals the forward-pass ratio. No other variation has a cross-check between two independently computed accuracy paths.

---

## JSON Output

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Three-pass architectural isolation (Forward Pass → Backward Pass → Classification Pass): gaps and echoes separated during classification by structural test ('was a signal type available?'), making C-12 three-way isolation an architectural property rather than a rule-enforcement requirement -- architectural compliance is more robust than rule-based prohibition because the structural test prevents misclassification even when the rule is ignored", "Accuracy reconciliation cross-check between Forward Pass and Backward Pass: two independently computed accuracy ratios reconciled against each other ('Cross-check: Does this ratio match the forward pass accuracy? If not, explain the discrepancy') -- no existing criterion captures this; it makes the accuracy computation auditable against itself"]}
```
