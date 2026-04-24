Scorecard written to `simulations/quest/scorecards/scout-market-scorecard-R4-2026-03-14.md`.

---

## Round 4 Results

| Rank | V | Score | Asp | Key result |
|------|---|-------|-----|------------|
| 1 | V-01 | **100** | 9/9 | C-15 PASS via post-card summary table |
| 1 | V-02 | **100** | 9/9 | C-15 PASS via pure wide-table primary view |
| 1 | V-04 | **100** | 9/9 | Path B complete: C-15+C-16+C-17 all PASS on wide-table |
| 1 | V-05 | **100** | 9/9 | Golden candidate: V-01 architecture + condensed instructions |
| 5 | V-03 | **98.9** | 8/9 | C-16 PASS (column header confirmed), C-17 FAIL (no chain) |

All five predictions confirmed. V-04 resolves to 100 rather than 98.9.

**R4 resolved the one structural question:** C-16 passes via table column header. `Inertia-break condition:` as a column header is an explicitly-labeled field — the label string is identical, the foreclosure effect is identical. Two C-16 mechanisms now confirmed.

**Two complete 100-scoring production paths exist:**
- **Path A** (per-card + summary table): V-05 is the golden candidate
- **Path B** (pure wide-table): V-04 is complete

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table column header Inertia-break condition satisfies C-16 -- column header is an explicitly-labeled field equivalent to per-block key-value field; two C-16 mechanisms confirmed (per-block field and table column header)", "post-card cross-segment summary table satisfies C-15 -- summary table need not be the primary scoring view; appending a wide table after per-cards passes C-15 independently; three C-15 mechanisms confirmed (wide-table primary, post-card summary, pure wide-table swap)", "Path B pure wide-table is complete at 100 -- V-04 achieves 9/9 on wide-table architecture; two full 100-scoring production paths confirmed: Path A per-card plus summary table V-01 and V-05 and Path B pure wide-table V-02 and V-04"]}
```
anisms now confirmed: per-block key-value field and table column header. Both use the
same label string; the mechanism (block vs. column) is architecturally equivalent.

**Path B (pure wide-table) complete -- CONFIRMED 100.**
V-04 achieves 9/9 on the pure wide-table architecture. Two complete paths to 100 confirmed:
- Path A (per-card + summary table): V-01, V-05
- Path B (pure wide-table): V-02, V-04

**V-01 vs. V-05 scoring parity -- CONFIRMED EQUAL.**
Instruction wording is neutral once structural scaffolding is identical. V-05 becomes the golden
candidate for production deployment by concision advantage.

## Excellence Signals

**ES-07 (V-03 / V-04): Table column header is structurally equivalent to per-block field for C-16.**
"Inertia-break condition:" as a sequencing table column header forecloses "Year 2+" entries at
the column level. The mechanism differs (column vs. block) but the label string and foreclosure
effect are identical. Template operators can choose either sequencing architecture without
sacrificing C-16 coverage.

**ES-08 (V-01 / V-05): Post-card summary table is a valid C-15 path -- does not require replacing per-cards.**
C-15 is satisfied when the summary table is self-contained. The per-cards remain as supporting
depth; the summary table independently meets the criterion. Operators who prefer per-card depth
can add a summary table without architectural surgery to achieve C-15.

**Golden candidate: V-05.** Per-card + explicit C-16 label + C-17 quantification chain +
post-card summary table (C-15) + condensed instructions. Cleanest 100-scoring production template.
V-01 scores identically -- V-05 preferred by concision.

---

## Predicted vs. Actual

| V | Predicted | Actual | Match |
|---|-----------|--------|-------|
| V-01 | 100 | 100 | YES |
| V-02 | 100 | 100 | YES |
| V-03 | 98.9 | 98.9 | YES |
| V-04 | 100 or 98.9 | 100 | YES (C-16 column PASS) |
| V-05 | 100 | 100 | YES |

---

## Detailed Scoring

### V-01: Per-Card + Cross-Segment Summary Table

**Base:** R3-V-05 | **Axis:** Add cross-segment summary table after per-segment cards

#### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | IDs in SEGMENT IDENTIFICATION, TAM/SAM/SOM, per-card headers, COMPOSITE RANK. |
| C-02 | PASS | STRATEGY: TAM/SAM/SOM table, one row per segment. |
| C-03 | PASS | Per-card pre-prints all three dimensions + arithmetic line. |
| C-04 | PASS | Cards: Rank score formula. COMPOSITE RANK copies and sorts. |
| C-05 | PASS | BEACHHEAD section with fit, GTM, rank, rationale covering inertia, highest-WTP, revenue model fit. |

**Essential: 5/5 -> 60 pts**

#### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | UNIT RULE: tooling = devs, platform/enterprise = $M, no mixing. |
| C-07 | PASS | GTM: SEQUENCING PATH with Y1, Y2+, Defer structure. |
| C-08 | PASS | AMENDMENTS section. |

**Recommended: 3/3 -> 30 pts**

#### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Per-card WTP adjacent to Revenue model and Price point. Summary table makes rank reversal visible across segments simultaneously. STATUS QUO + beachhead inertia present. |
| C-10 | PASS | Per-card Revenue model and Price point fields. Concrete price point required in at least one card. |
| C-11 | PASS | STATUS QUO with named inertia anchor required verbatim. Do-nothing cost quantified. |
| C-12 | PASS | Beachhead "Not building this means:" full chain to STATUS QUO cost. Do not omit, do not write generic statement. |
| C-13 | PASS | Per-card vertical adjacency: WTP immediately above Revenue model and Price point in every block. |
| C-14 | PASS | Per-block "Inertia-break condition:" field. Must cite anchor by name, not calendar date. |
| C-15 | PASS | CROSS-SEGMENT SCORING SUMMARY table: Pain, WTP, Revenue Model, Price Point, Access, Fit Score, GTM, Inertia Anchor, Rank Score as adjacent columns. Instruction: "enables direct cross-segment comparison in a single view without cross-referencing cards." Wide-table format; all dimensions adjacent. |
| C-16 | PASS | Per-block "Inertia-break condition:" field inherited from R3-V-05 (confirmed PASS). |
| C-17 | PASS | (1) STATUS QUO: "Required in Not building this means: below -- do not write a vague estimate." Forward-reference at source. (2) Beachhead: "costing approximately ($ or hrs from STATUS QUO do-nothing cost)." Format-chain at consumption. Both conditions met. |

**Aspirational: 9/9 -> 10 pts**

**Composite: 60 + 30 + 10 = 100 | Prediction: 100 | Match: YES | Golden: YES | Exemplary**

---

### V-02: Architecture Swap to Pure Wide-Table

**Base:** R3-V-05 elements | **Axis:** Replace per-segment cards with UNIFIED SCORING TABLE;
STATUS QUO, beachhead, sequencing carried unchanged

#### Essential: 5/5 -> 60 pts | Recommended: 3/3 -> 30 pts (same structural guarantees)

#### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | UNIFIED SCORING TABLE: WTP, Revenue Model, Price Point as adjacent columns. Rank reversal visible in single row. STATUS QUO + beachhead present. R3 confirmed wide-table passes C-09. |
| C-10 | PASS | Revenue Model and Price Point columns. At least one concrete price point required. |
| C-11 | PASS | STATUS QUO with forward-reference: "Required in Not building this means: below -- do not write a vague estimate." Named inertia anchors required verbatim. |
| C-12 | PASS | Beachhead: "costing approximately ($ or hrs from STATUS QUO do-nothing cost). Every (quarter/year) of delay..." |
| C-13 | PASS | Wide-table column adjacency: WTP, Revenue Model, Price Point as adjacent columns. Confirmed equivalent in R3. |
| C-14 | PASS | Per-block "Inertia-break condition:" field with anchor-name requirement. Carried from R3-V-05. |
| C-15 | PASS | UNIFIED SCORING TABLE is the primary scoring view. All dimensions present as adjacent columns. No separate section required for any dimension. |
| C-16 | PASS | Per-block "Inertia-break condition:" field with explicit anchor-name and foreclosure. Inherited from R3-V-05. |
| C-17 | PASS | (1) STATUS QUO forward-reference instruction. (2) Beachhead cites "from STATUS QUO do-nothing cost." Both chain ends enforced. |

**Aspirational: 9/9 -> 10 pts**

**Composite: 60 + 30 + 10 = 100 | Prediction: 100 | Match: YES | Golden: YES | Exemplary**

---

### V-03: C-16 via Sequencing Sub-Table Column

**Base:** R3-V-01 | **Axis:** Sequencing replaced with structured table; column header
"Inertia-break condition: (Y2+ required -- must name STATUS QUO anchor; Year 2+ is not valid)"

#### Essential: 5/5 -> 60 pts | Recommended: 3/3 -> 30 pts

#### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Wide-table column adjacency for WTP-vs-revenue-model. STATUS QUO and beachhead inertia present. Same as R3-V-01 confirmed PASS. |
| C-10 | PASS | Revenue Model and Price Point in UNIFIED SCORING TABLE. Concrete price point required. |
| C-11 | PASS | STATUS QUO section with named inertia anchor. Do-nothing cost quantified. Cost stated before scoring; pain/WTP anchored to STATUS QUO. |
| C-12 | PASS | Beachhead: "Reference STATUS QUO do-nothing cost. Do not omit this line." Tied to STATUS QUO at consumption. |
| C-13 | PASS | Wide-table column adjacency: WTP, Revenue Model, Price Point as adjacent columns. |
| C-14 | PASS | Sequencing table entry rationale references inertia anchor. STATUS QUO anchor named. |
| C-15 | PASS | UNIFIED SCORING TABLE as primary scoring view. Identical to R3-V-01. |
| C-16 | PASS | Sequencing table column header: "Inertia-break condition: (Y2+ required -- must name STATUS QUO anchor; Year 2+ is not valid)". Ruling: table column IS an explicitly-labeled field. Label string "Inertia-break condition:" matches per-block field exactly; parenthetical forecloses time-based entries at column level. C-16 pass condition satisfied. Column header mechanism confirmed equivalent to per-block key-value field. |
| C-17 | FAIL | STATUS QUO "Do-nothing cost": "Estimate: hrs/wk per user, $ per year, or qualitative friction level." No forward-reference instruction. Beachhead: "Reference STATUS QUO do-nothing cost. Do not omit this line." Reminder at consumption only -- no citation-by-value requirement, no source-format chain. C-17 requires both ends: source pre-commitment AND beachhead cites by value and source. Neither fully met. |

**Aspirational: 8/9 -> 8.89 pts**

**Composite: 60 + 30 + 8.89 = 98.9 | Prediction: 98.9 | Match: YES | Golden: YES**

---

### V-04: V-03 + C-17 Chain (Combined: Wide-Table Path B Complete)

**Base:** V-03 | **Axes:** C-16 via sequencing table column + C-17 STATUS QUO quantification chain

#### Essential: 5/5 -> 60 pts | Recommended: 3/3 -> 30 pts

#### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Wide-table adjacency + STATUS QUO + beachhead inertia. Same as V-03. |
| C-10 | PASS | Revenue Model and Price Point columns with concrete value requirement. |
| C-11 | PASS | STATUS QUO with named inertia anchor. Do-nothing cost quantified. |
| C-12 | PASS | Beachhead "Not building this means:" cites STATUS QUO cost. |
| C-13 | PASS | Wide-table column adjacency. |
| C-14 | PASS | Sequencing table inertia-break column forecloses time-based entries. STATUS QUO anchor available. |
| C-15 | PASS | UNIFIED SCORING TABLE as primary scoring view. |
| C-16 | PASS | Same sequencing table column header mechanism as V-03. Confirmed PASS per V-03 ruling. |
| C-17 | PASS | (1) STATUS QUO: "Required in Not building this means: below -- do not write a vague estimate. This value will be cited by amount and source at the beachhead." Forward-reference with explicit pre-commitment. (2) Beachhead: "costing approximately ($ or hrs from STATUS QUO do-nothing cost -- cite the value from STATUS QUO, do not re-estimate)." Format-chain citation by value and source. Both C-17 conditions met. |

**Aspirational: 9/9 -> 10 pts**

**Composite: 60 + 30 + 10 = 100 | Prediction: 100 (C-16 column PASS) | Match: YES | Golden: YES | Exemplary**

---

### V-05: Golden Candidate R4 (Per-Card + Summary Table, Consolidated)

**Base:** R3-V-05 | **Axes:** C-15 via cross-segment summary table + all R3-V-05 passes preserved
+ full instruction tightening

#### Essential: 5/5 -> 60 pts | Recommended: 3/3 -> 30 pts

#### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Per-card WTP adjacent to Revenue model and Price point. Summary table surfaces rank reversal across segments simultaneously. STATUS QUO + beachhead inertia. Maximum structural scaffolding with minimum verbosity. |
| C-10 | PASS | Revenue model and Price point per-card fields. "At least one card must show a concrete price point, not TBD." |
| C-11 | PASS | STATUS QUO with named inertia anchor: "Required verbatim in scoring cards and sequencing transitions." Do-nothing cost with forward-reference: "This value is required in Not building this means: below." |
| C-12 | PASS | Beachhead: "($ or hrs from STATUS QUO do-nothing cost). Every (quarter/year) of delay = (estimated ongoing waste or lost capture). Do not omit. Do not write a generic statement." |
| C-13 | PASS | Per-card vertical adjacency. |
| C-14 | PASS | Per-block "Inertia-break condition:" field with anchor-name requirement. Carried from R3-V-05. |
| C-15 | PASS | CROSS-SEGMENT SCORING SUMMARY explicitly marked "Required." Instruction: "presents Pain, WTP, Revenue Model, Price Point, Accessibility, Fit Score, GTM Difficulty, Inertia Anchor, and Rank Score as adjacent columns with one row per segment. Enables direct cross-segment comparison in one view without card lookup. No column may be blank." Preamble also names summary table as required output. |
| C-16 | PASS | Per-block "Inertia-break condition:" field inherited from R3-V-05. |
| C-17 | PASS | (1) STATUS QUO: "This value is required in Not building this means: below -- do not write a vague estimate." (2) Beachhead: "costing approximately ($ or hrs from STATUS QUO do-nothing cost)." Both chain ends enforced. Identical coverage to V-01. |

**Aspirational: 9/9 -> 10 pts**

**Composite: 60 + 30 + 10 = 100 | Prediction: 100 | Match: YES | Golden: YES | Exemplary**

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table column header Inertia-break condition satisfies C-16 -- column header is an explicitly-labeled field equivalent to per-block key-value field; two C-16 mechanisms confirmed (per-block field and table column header)", "post-card cross-segment summary table satisfies C-15 -- summary table need not be the primary scoring view; appending a wide table after per-cards passes C-15 independently; three C-15 mechanisms confirmed (wide-table primary, post-card summary, pure wide-table swap)", "Path B pure wide-table is complete at 100 -- V-04 achieves 9/9 on wide-table architecture; two full 100-scoring production paths confirmed: Path A per-card plus summary table V-01 and V-05 and Path B pure wide-table V-02 and V-04"]}
```
