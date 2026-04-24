## Signal Quest Scorecard — `review-design` Round 2

---

### Summary

| Var | Score | Outcome | Key Driver |
|-----|-------|---------|------------|
| V-01 | **100** | Golden | Phase 3 gate + Sev/Section/three-field baseline |
| V-02 | **98.75** | Golden | Conversational framing → C-08 PARTIAL (softer "feel right?" vs. formal halt) |
| V-03 | **100** | Golden | F-06/F-07 halt conditions close C-08 and C-11 gaps |
| V-04 | **100** | Golden | Expert trace table + pyramid gate table — strongest structural form without F-IDs |
| V-05 | **100** | Golden | Full defense-in-depth: tables + F-IDs — maximum enforcement |

**Ranking (tiebreaker: enforcement depth):** V-05 > V-04 > V-03 > V-01 >> V-02

---

### Key Findings

**R2 baseline worked.** Adding `Sev`+`Section` table columns and the three-field expert trace as structural requirements eliminated the R1 PARTIALs on C-02, C-03, C-07. C-08's universal R1 FAIL was resolved in 4 of 5 variations.

**C-08 design bet resolved.** Conversational calibration (V-02) is insufficient — PARTIAL. Formal phase gate (V-01), F-ID halt (V-03), and table+Status column (V-04, V-05) all achieve PASS. V-02 demonstrates that informal register erodes enforcement even when the requirement is stated.

**Expert trace as table columns** (V-04, V-05) extends the Sev+Section structural pattern to expert selection — the same mechanism that fixed C-02/C-07 in R1 now applies to C-11.

**Score ceiling reached.** Four variations score 100 against the v2 rubric. To differentiate in R3, the rubric needs a new aspirational criterion or an enforcement-depth sub-score within PASS.

---

### Design Bet Resolution

| Bet | Result |
|-----|--------|
| Phase gate vs F-ID halt for C-08 | Tie — both PASS; F-IDs add drift protection |
| Conversational vs formal for C-08 | Formal wins — PARTIAL vs PASS |
| Expert table vs labeled prose for C-11 | Table wins qualitatively (structural enforcement) |
| F-IDs on top of table (V-05 vs V-04) | No rubric score difference; qualitative advantage only |

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["severity pyramid gate as dedicated block between findings and consensus eliminates C-08 skip — lifecycle position is more reliable than a prose instruction", "expert trace in table column form (Signal detected | Expert added | Reason) extends Sev+Section structural enforcement from findings to expert selection", "F-06 halt at pyramid block closes last universal R1 failure — halt-pattern from C-02/C-04 applied to C-08 inverted pyramid"]}
```
03 were PARTIAL in R1 (prose-only). R2 baseline adds `Sev` column to all variations — universal PASS.

---

#### C-03 | Domain Expert Auto-Selection Justified

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Three labeled fields in code block: `Signal detected:` / `Expert added:` / `Reason:` — all required |
| V-02 | PASS | Same three fields; code block format enforces distinct labels |
| V-03 | PASS | Three fields + F-03 (Signal detected empty → halt) + F-07 (Expert added or Reason empty → halt) |
| V-04 | PASS | Domain expert table with `Signal detected | Expert added | Reason` columns; "every row must have all three cells populated" |
| V-05 | PASS | Domain expert table + F-03 + F-07 halt on any empty cell |

**Pattern change from R1**: V-01 was PARTIAL in R1. R2 baseline three-field requirement eliminates partial trace — universal PASS.

---

#### C-04 | Consensus Block Present

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Phase 4 required; "Do not omit this phase even if the review is unanimous" |
| V-02 | PASS | Block 3 required; "Don't skip this block even if the review is unanimous" |
| V-03 | PASS | F-04 halt on omission; "F-04 fires on omission regardless of review content" |
| V-04 | PASS | "Never omit this block" — explicit |
| V-05 | PASS | F-04 + "Never omit this block — F-04 fires on omission" |

All PASS — unchanged from R1.

---

#### C-05 | Unique Catches Surfaced

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Phase 5 required; "If none: write `No unique catches.`" |
| V-02 | PASS | Block 4 required; "If none: write `No unique catches.`" |
| V-03 | PASS | Block 4 required; "If none: write `No unique catches.`" |
| V-04 | PASS | Block 4 as table with `UNIQUE | none | —` fallback row |
| V-05 | PASS | Block 4 table with `UNIQUE | none | —` fallback row |

All PASS — unchanged from R1.

---

#### C-06 | Amend Pathway — Targeted Re-run

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Phase 6: "Re-run: [reviewer name(s)] on [section scope only — never 'full review']" |
| V-02 | PASS | Block 5: "Re-run: [reviewer name(s)] on [section scope only — not a full re-review]" |
| V-03 | PASS | F-05 halt: "An amend scoped to 'full review' fires F-05 — halt and re-scope" |
| V-04 | PASS | "Re-run: [reviewer name(s)] on [section scope only — never 'full review']" |
| V-05 | PASS | F-05 halt + "An amend scoped to 'full review' fires F-05 — halt and re-scope" |

All PASS — unchanged from R1.

---

#### C-07 | Finding Traceability to Design Section

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | `Section` column + "Every P1 row: Section is required. P2 rows: Section required for at least 50% of rows." |
| V-02 | PASS | `Section` column + "All P1 rows have a section. At least half of P2 rows have a section." |
| V-03 | PASS | `Section` column + "P1 rows: Section always required. P2 rows: Section required for >= 50% of rows." |
| V-04 | PASS | `Section` column contracts explicitly state P1 + 50% P2 rules |
| V-05 | PASS | `Section` column + F-02 structural enforcement — strongest traceability anchor |

**Pattern change from R1**: V-01, V-03, V-04 were PARTIAL in R1 (prose-only). R2 baseline adds `Section` column to all — universal PASS.

---

#### C-08 | Severity Distribution Sanity

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Phase 3 (dedicated): explicit P1/P2/P3 count, pyramid check, mandatory `Pyramid inverted...Rationale:` paragraph if not nominal — structural gate between Phase 2 and Phase 4 |
| V-02 | PARTIAL | Block 2.5 "Calibration Check": P1/P2/P3 count present; "does this feel right?" framing is invitational, not mandatory. "Don't skip this" stated but no formal halt or restructure instruction — softer than V-01/V-03/V-04/V-05 |
| V-03 | PASS | F-06 halt: "Pyramid inverted, silent — Block 2.5 shows P1 > P2 or P2 > P3 with no rationale written before Block 3" — explicit halt-and-restructure |
| V-04 | PASS | Severity distribution table with `Status` column; "Do not proceed to Block 3 without completing the Status column" + Rationale row if inverted |
| V-05 | PASS | F-06 halt + Status column + Rationale row — strongest C-08 enforcement |

**Pattern change from R1**: Universal FAIL in R1. R2: 4 PASS, 1 PARTIAL (V-02 conversational framing trades enforcement strength for naturalness).

---

#### C-09 | Expert Disagreement Analysis (Split Synthesis)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "SPLIT: [decision]...Synthesis: [1-3 sentences explaining the underlying design tension this reveals]" |
| V-02 | PASS | "SPLIT:...Synthesis: [1-3 sentences on the design trade-off this split reveals]" |
| V-03 | PASS | "Synthesis: [1-3 sentences on the design tension this split reveals]" in Block 3 |
| V-04 | PASS | Table format: "A: [pos] / B: [pos] | Synthesis: [1-3 sent.]" — structured synthesis field |
| V-05 | PASS | Same table format — structured synthesis field |

All PASS — unchanged from R1.

---

#### C-10 | Structural Column Enforcement in Finding Tables

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | `| Sev | Section | Finding |` table in Phase 2 — both required columns present |
| V-02 | PASS | `| Sev | Section | Finding |` table in Block 2 |
| V-03 | PASS | `| Sev | Section | Finding |` table with F-02 on Sev cell |
| V-04 | PASS | `| Sev | Section | Finding |` table + "no finding may appear as prose-only" stated explicitly |
| V-05 | PASS | Table + F-02 halt + "no finding may appear as prose-only" |

All PASS — R2 baseline requirement, targeted from R1 excellence signal.

---

#### C-11 | Three-Field Expert Trace

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Code block: `Signal detected:` / `Expert added:` / `Reason:` — all three labeled, all required |
| V-02 | PASS | Same three-field code block format |
| V-03 | PASS | Three-field code block + F-03 (Signal detected empty) + F-07 (Expert added or Reason empty) — labeled prose with halt enforcement |
| V-04 | PASS | Domain expert table with `Signal detected | Expert added | Reason` columns — table-enforced, "every row must have all three cells populated" |
| V-05 | PASS | Domain expert table + F-03 + F-07 — strongest C-11 enforcement (table + halt) |

All PASS — R2 baseline requirement, targeted from R1 excellence signal. V-04/V-05 elevate from labeled prose (V-01/V-02/V-03) to table-column form.

---

### Composite Scores

Formula: `essential_pass/4 × 60 + recommended_pass/3 × 30 + aspirational_pass/4 × 10`
PARTIAL = 0.5 for scoring.

| Var | C-01 | C-02 | C-03 | C-04 | Essential (×60) | C-05 | C-06 | C-07 | Recommended (×30) | C-08 | C-09 | C-10 | C-11 | Aspirational (×10) | **Composite** | All Essential? | Outcome |
|-----|------|------|------|------|-----------------|------|------|------|-------------------|------|------|------|------|--------------------|---------------|----------------|---------|
| V-01 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | 4/4 → 10 | **100** | Yes | **Golden** |
| V-02 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | PR | P | P | P | 3.5/4 → 8.75 | **98.75** | Yes | **Golden** |
| V-03 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | 4/4 → 10 | **100** | Yes | **Golden** |
| V-04 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | 4/4 → 10 | **100** | Yes | **Golden** |
| V-05 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | 4/4 → 10 | **100** | Yes | **Golden** |

`P = PASS, PR = PARTIAL`

---

### Ranking

V-01, V-03, V-04, V-05 all score 100. Tiebreaker: structural enforcement strength.

| Rank | Variation | Score | Outcome | Tiebreaker |
|------|-----------|-------|---------|------------|
| 1 | V-05 (all-axes combined) | 100 | Golden | Maximum enforcement: expert table + F-IDs + pyramid gate table + F-06/F-07 — all four aspirational criteria targeted structurally |
| 2 | V-04 (output-format + lifecycle) | 100 | Golden | Expert table + pyramid gate table — structural enforcement without F-ID overhead; cleanest structural form |
| 3 | V-03 (inertia + F-IDs) | 100 | Golden | F-06/F-07 halt conditions close C-08 and C-11 gaps; three-field labeled prose (not table) for expert trace |
| 4 | V-01 (lifecycle baseline) | 100 | Golden | Phase 3 gate is clean and explicit; no F-IDs; code-block fields for expert trace |
| 5 | V-02 (phrasing register) | 98.75 | Golden | Conversational "calibration check" framing reduces C-08 enforcement reliability; PARTIAL on aspirational C-08 |

---

### Design Bet Resolution

| Bet | Winner | Finding |
|-----|--------|---------|
| V-01 (phase gate) vs V-03 (F-ID halt) for C-08 | **Tie** — both PASS | Phase gate and F-ID halt are equally effective at the rubric level; F-IDs add defense against mid-output drift |
| V-02 (conversational) vs V-01 (formal gate) for C-08 | **V-01 wins** | Conversational framing ("does this feel right?") is insufficient to guarantee pyramid compliance — PARTIAL vs PASS |
| V-04 (expert table) vs V-03 (labeled prose + F-IDs) for C-11 | **V-04 wins qualitatively** | Table columns make incomplete expert rows visually obvious; labeled prose requires active field inspection |
| V-05 (F-IDs + tables) vs V-04 (tables only) | **V-05 wins qualitatively** | F-IDs add halt enforcement on top of table structure; no score difference at rubric level |

---

### Excellence Signals

**From V-04 and V-05 (structural top performers):**

1. **Expert trace as table columns closes C-11 via the same structural mechanism that closed C-02 and C-07** — `Signal detected | Expert added | Reason` as three required table columns makes an incomplete expert entry visually impossible to miss. Labeled prose fields (V-01, V-02, V-03) require active inspection; empty table cells are self-evident. This extends the R1 `Sev | Section` column pattern from findings to expert selection.

2. **Dedicated severity distribution block positioned between findings and consensus** — All four passing variations insert a named block (Phase 3, Block 2.5) before consensus analysis. This lifecycle position is the critical insight: computing the pyramid *after* all findings are written but *before* summarization forces the model to surface distribution data at the moment it matters, not as an afterthought. The block cannot be elided without also eliding the consensus analysis.

3. **F-06 halt at the pyramid block closes the last universal R1 FAIL** — R1's C-08 failure was systemic (no prompt mentioned distribution at all). R2's F-06 encodes "Pyramid inverted, silent" as an explicit halt condition at the block where the gap fires. The halt-at-block pattern from R1 (F-02 for C-02, F-04 for C-04) is now applied to C-08 — consistent pattern across all failure types.

**Observation — R2 score ceiling:**
Four of five variations reach 100. The rubric's aspirational ceiling (10 points) is now fully achievable in prompt design when all four criteria are structurally enforced. The remaining scoring variation is in the C-08 enforcement strength dimension (V-02 PARTIAL). To differentiate further in R3, the rubric will need a new aspirational criterion or the scoring will need to track enforcement-depth as a sub-score within PASS.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["severity pyramid gate as dedicated block between findings and consensus eliminates C-08 skip — lifecycle position is more reliable than a prose instruction", "expert trace in table column form (Signal detected | Expert added | Reason) extends Sev+Section structural enforcement from findings to expert selection", "F-06 halt at pyramid block closes last universal R1 failure — halt-pattern from C-02/C-04 applied to C-08 inverted pyramid"]}
```
