## Scout-Risk R9 — Scorecard

### Rubric Summary

**Max composite: 136** (60 essential + 30 recommended + 46 aspirational across 23 criteria)

---

### V-01 — Axis: Inertia Framing (Prose, Decision Window only)

**Essential (60/60)**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "This entry is mandatory. AMEND directives do not remove it. It appears before Phase 2 output in all registers." |
| C-02 | PASS | "at least four of these five dimensions" (4 >= 3) |
| C-03 | PASS | Phase 2 format includes Severity/Likelihood/Mitigation; inertia uses Inertia Condition as qualifying likelihood substitute |
| C-04 | PASS | "Severity: HIGH \| MEDIUM \| LOW (exactly one)" enforced in both phases |
| C-05 | PASS | Typed taxonomy + Phase 2a prohibited-phrase scan |

**Recommended (30/30)**

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "[Dimension] — [Risk title]" header labels every entry |
| C-07 | PASS | IF-THEN form required, "bare labels not permitted" |
| C-08 | PASS | "Order: HIGH entries first, then MEDIUM, then LOW" |

**Aspirational (44/46)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 3 dedicated section, >= 3 pairs |
| C-10 | PASS | AMEND section retains Phase 1 full 5-field anatomy, all repair loops active |
| C-11 | PASS | Phase 2a terminates only when zero instances of 7 prohibited phrases found |
| C-12 | PASS | IF-THEN form required for every row |
| C-13 | PASS | Dedicated "Risk Interdependencies" labeled section, >= 3 pairs |
| C-14 | PASS | IF-THEN syntactic form enforced throughout |
| C-15 | PASS | Phase 0 taxonomy, sub-field key=value pairs required per entry |
| C-16 | PASS | Phase 4 minimum 3 pairs |
| C-17 | PASS | "FROM and TO must each be exactly one of {HIGH, MEDIUM, LOW}" |
| C-18 | PASS | Phase 2b type diversity audit, minimum 3 distinct labels |
| C-19 | PASS | 7 specific forbidden phrases enumerated in Phase 2a |
| C-20 | PASS | Repair Loop C names Phase 2 as upstream step to revise |
| C-21 | PASS | 2 count gates (type diversity, interdependency) × 2 count-gate repair loops (B, C) — row floor is stated as target only, not enforced as a gate, so no mismatch |
| C-22 | PASS | Phase 3: "FROM and TO must each be exactly one of {HIGH, MEDIUM, LOW}" — vocabulary explicitly named |
| C-23 | PASS | Three uniquely labeled loops: Repair Loop A, B, C |
| C-24 | PASS | Phase 0 defines all 6 classes with sub-fields in pre-block |
| C-25 | PASS | Phase 2b labeled "Standalone Step" — "Phase 2b terminates when..." step is independent |
| C-26 | PASS | "sub-field values MUST be rendered inline as key=value pairs" — format spec in Phase 0 |
| C-27 | PASS | "This block precedes all phases and remains in scope for every phase" |
| C-28 | PASS | Phase 1 uses 5-field anatomy; "do NOT apply the Severity/Likelihood/Mitigation structure used for dimensional risks" |
| C-29 | PASS | Decision Window field: "The named deadline, forcing event, or expiry horizon... A concrete calendar marker, external trigger, or compounding milestone — not 'eventually.'" |
| C-30 | PASS | Phase 1 (labeled sub-section, fields: Severity/Status-quo/Inertia Condition/Decision Window/Mitigation) vs Phase 2 (labeled sub-section, fields: Severity/Likelihood/Mitigation) — independent field sets |
| C-31 | **FAIL** | "Target: at least seven dimensional risk entries" stated as goal only; no repair loop for underpopulation |

**V-01 composite: 60 + 30 + 44 = 134/136**

---

### V-02 — Axis: Output Format (Table, Row Floor Repair Loop, No Decision Window)

**Essential (60/60)** — all PASS (inertia mandatory, 5 dimensions, anatomy complete, vocabulary, typed mitigations)

**Recommended (30/30)** — all PASS (dimension column, IF-THEN likelihood, HIGH-first ordering)

**Aspirational (44/46)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-28 | PASS | Matches R8 V-05 baseline; all table-format constraints, 7 prohibited phrases, C-22 vocabulary constraint on From/To columns, C-23 (4 named loops: A/B/C/D) |
| C-29 | **FAIL** | Decision Window deliberately omitted from Phase 1 table schema to isolate axis |
| C-30 | PASS | Phase 1 table (6-column schema: Risk-ID/Dimension/Severity/Status-quo Description/Inertia Condition/Mitigation/Type-Class) vs Phase 2 table (6-column dimensional schema) — separate tables with distinct column layouts |
| C-31 | PASS | "Row-count gate: Table 2 MUST contain at least 7 rows." → "Repair Loop A — Row-count deficit: Return to Phase 2. Add risk entries... Do not proceed to Phase 2a until the row count is confirmed at 7 or greater." |

Note on C-21: 3 count gates (row floor/Loop A, type diversity/Loop C, interdependency count/Loop D) × 3 count-gate loops = 1:1 match → PASS.

**V-02 composite: 60 + 30 + 44 = 134/136**

---

### V-03 — Axis: Phase Structure (Table, Decision Window Column in Table 1, No Row Floor Loop)

**Essential (60/60)** — all PASS

**Recommended (30/30)** — all PASS

**Aspirational (44/46)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-28 | PASS | All baseline criteria pass; 3-loop structure (A/B/C) with quality + type diversity + interdependency count gates |
| C-29 | PASS | Table 1 has explicit Decision Window column: "The named deadline, forcing event, or expiry horizon... must name a specific event, deadline, or milestone — 'soon' or 'eventually' fails" |
| C-30 | PASS | Table 1 (7-column schema including Decision Window) vs Table 2 (6-column dimensional schema) — distinct column layouts, separate tables |
| C-31 | **FAIL** | "Produce a table with at least seven rows" stated; no repair loop for underpopulation. Hypothesis confirms "Row floor is stated at 7 rows but has no dedicated repair loop, so C-31 does not score." |

Note on C-21: 2 count gates (type diversity/Loop B, interdependency count/Loop C) × 2 count-gate loops = 1:1 match → PASS. Row floor stated without repair loop is not an enforced gate.

**V-03 composite: 60 + 30 + 44 = 134/136**

---

### V-04 — Combination: Prose, Decision Window + Row Floor Repair Loop

**Essential (60/60)** — all PASS

**Recommended (30/30)** — all PASS

**Aspirational (46/46)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-28 | PASS | Full prior baseline; prose format with Phase 0 taxonomy pre-block, 7 enumerated forbidden phrases, standalone Phase 2b, vocabulary-constrained IF-THEN likelihood |
| C-29 | PASS | Decision Window field: "The named deadline, forcing event, or expiry horizon after which deferring this decision compounds the inertia risk. Names a concrete calendar marker, milestone trigger, or competitive event — not 'eventually' or 'in the future.'" Decision Window must be populated — "TBD" fails. |
| C-30 | PASS | Phase 1 labeled sub-section (Severity/Status-quo Description/Inertia Condition/Decision Window/Mitigation) vs Phase 2 labeled sub-section (Severity/Likelihood/Mitigation) — independent field sets in separate labeled phases |
| C-31 | PASS | "Row-count gate: Generate at least 7 dimensional risk entries. After completing entries, count them. If Phase 2 has fewer than 7 entries: → Repair Loop A — Row-count deficit: Add risk entries... Do not proceed to Phase 2a until the row count is confirmed at 7 or greater." |

Note on C-21: 3 count gates (row floor/Loop A, type diversity/Loop C, interdependency count/Loop D) × 3 count-gate loops = 1:1 match → PASS. Note on C-23: 4 uniquely named loops (A, B, C, D) → PASS.

**V-04 composite: 60 + 30 + 46 = 136/136**

---

### V-05 — Full Combination: Table Format, All Axes

**Essential (60/60)** — all PASS

**Recommended (30/30)** — all PASS

**Aspirational (46/46)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 3 interdependency table, >= 3 rows |
| C-10 | PASS | AMEND section: Phase 1 retained unchanged with Decision Window column; all 4 repair loops active; all vocabulary constraints in force |
| C-11 | PASS | Phase 2a scan terminates only at zero instances of 7 prohibited phrases |
| C-12 | PASS | "Must use IF-THEN form" in every Likelihood cell, "bare labels ('possible', 'likely', '~30%') are format violations" |
| C-13 | PASS | Dedicated "Risk Interdependencies" table (Table 3), >= 3 rows |
| C-14 | PASS | IF-THEN syntactic form required — format violations called out explicitly |
| C-15 | PASS | Type-Class column plus Mitigation format requiring key=value sub-field pairs |
| C-16 | PASS | Phase 4 minimum 3 named pairs |
| C-17 | PASS | Table 3 From-Severity/To-Severity with explicit FROM/TO severity-transition structure |
| C-18 | PASS | Phase 2b counts distinct Type-Class labels; minimum 3 required |
| C-19 | PASS | 7 specific forbidden phrases enumerated in Phase 2a |
| C-20 | PASS | Repair Loop D: "Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings." Names upstream step. |
| C-21 | PASS | 3 count gates × 3 count-gate repair loops (A for row floor, C for type diversity, D for interdependency) = 1:1 match |
| C-22 | PASS | Table 3 column rules: "From-Severity and To-Severity are vocabulary-constrained at the cell level — prose labels, compound entries, absent values are format violations" with explicit {HIGH, MEDIUM, LOW} |
| C-23 | PASS | 4 uniquely labeled loops: Repair Loop A, Repair Loop B, Repair Loop C, Repair Loop D — each independently addressable by name |
| C-24 | PASS | Phase 0 defines all 6 type classes with sub-field semantics column in a 4-column taxonomy table |
| C-25 | PASS | "Phase 2b — Mitigation Type Diversity Audit (Standalone Step — Do Not Merge with Phase 2 or Phase 2a)" — own step number with explicit merge prohibition |
| C-26 | PASS | "Sub-field values MUST appear as key=value pairs in every Mitigation cell in every table" — output format spec in Phase 0 |
| C-27 | PASS | "This block precedes all phases. Read it before executing Phase 1. It remains in scope for every phase." |
| C-28 | PASS | Table 1 dedicated 7-column schema; "Do not apply Table 2 columns to this entry" |
| C-29 | PASS | Decision Window column in Table 1: "must name a concrete calendar marker, competitive trigger, or compounding milestone; 'eventually' or 'TBD' fails" |
| C-30 | PASS | Table 1 (7-column schema) and Table 2 (6-column schema) are completely separate tables with distinct column definitions — no shared columns |
| C-31 | PASS | "Row-count gate: Table 2 MUST contain at least 7 rows." → "Repair Loop A — Row-count deficit: Return to Phase 2. Add risk entries across additional dimensions or surface additional failure modes within existing dimensions until Table 2 contains at least 7 rows. Do not proceed to Phase 2a until the row count is confirmed at 7 or greater." |

**V-05 composite: 60 + 30 + 46 = 136/136**

---

### Ranking

| Rank | Variation | Score | Delta from Max | Failed Criteria |
|------|-----------|-------|----------------|-----------------|
| **1** | **V-04** | **136/136** | — | None |
| **1** | **V-05** | **136/136** | — | None |
| 3 | V-01 | 134/136 | −2 | C-31 |
| 3 | V-02 | 134/136 | −2 | C-29 |
| 3 | V-03 | 134/136 | −2 | C-31 |

All five variations pass all essential criteria. No variation is blocked from golden territory.

---

### Excellence Signals from V-04 and V-05

**1. The 3-count-gate architecture is the key differentiator.** V-04 and V-05 both reach 136 because they implement all three count gates with dedicated repair loops: row floor (Loop A), type diversity (Loop C), and interdependency count (Loop D). Single-axis variations each miss one gate and pay exactly 2 points.

**2. V-04/V-05 tie confirms format-agnostic schema isolation.** V-04 (prose) and V-05 (table) achieve identical scores. C-30's pass condition of "labeled sub-sections with independent field sets" is satisfied by prose phases as effectively as by typed-column tables. Format choice is not a differentiator when field-set independence is preserved.

**3. Decision Window + Row Floor together are the minimum combination for maximum score.** Neither C-29 alone (V-01, V-03) nor C-31 alone (V-02) reaches 136. The two criteria are strictly additive — there is no interaction penalty or bonus.

**4. The 4-loop naming scheme is structural, not cosmetic.** V-04 and V-05's Repair Loop A/B/C/D naming allows C-21 verification (3 count-gate loops for 3 count gates) to be confirmed by inspection without prose interpretation. V-01/V-02/V-03's 3-loop schemes also satisfy C-21 for their respective gate counts — the naming confirms rather than creates the 1:1 match.

---

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["format-agnostic schema isolation: prose labeled sub-sections with independent field sets achieve C-30 parity with typed-column table schemas — field-set independence is the mechanism, not the output format"]}
```
