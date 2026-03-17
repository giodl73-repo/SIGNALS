Now I have everything I need. Let me evaluate all five variations.

---

# scout-inertia — Quest Score R9

**Rubric**: v9 (ceiling 155 = 100 essential base + 11 advanced criteria × 5 pts)
**A-12 context**: Never passed R5–R8. R9 targets it with explicit Q3/Q4 naming in the template body.

---

## Scoring Framework

- **Essential (C-01–C-05)**: All 5 must pass → 100 base points
- **Advanced (A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18, A-19, A-20)**: 5 pts each → 55 pts max
- **A-08** is in the rubric for reference but subsumed by A-14 (A-14 implies A-08); not scored independently
- Ceiling: 155

---

## V-01 — Output format (tabular + dedicated BRIDGE ARTIFACTS section)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 2 table: "Workaround name (specific: tool / file type / procedure)", "Role performing it", "Ongoing cost (e.g., 2 hours/week)"; rejection rule: "Teams export data fails on all columns" |
| C-02 | Switching cost quantified | **PASS** | Section 3 table with 4 named rows; blockquote rule: "Every estimate must carry a number and a unit. 'Significant' without a number fails C-02" |
| C-03 | Inertia threat score declared | **PASS** | Section 4 table: "Threat score (HIGH / MEDIUM / LOW)"; "Default is HIGH. Deviations require a specific number, threshold, or measurable state" |
| C-04 | Defeat conditions identified | **PASS** | Section 5 DC table: "Minimum 2 rows, each with an FM reference"; falsifiability example embedded |
| C-05 | Failure modes identified | **PASS** | Section 1 FM Inventory: "Minimum 2 rows required. 'Manual is slow' fails — name the specific error, truncation, silent failure, or data loss event" |

**All essential: PASS (100/100)**

### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | "## FAIL-FIRST DECLARATION" as first named section with explicit rationale: "Every defeat condition and switching cost threshold depends on what breaks first. Populate Section 1 before any other section." |
| A-11 | Question per criterion (3+) | **FAIL** | No embedded per-criterion questions anywhere in authoring sections; structural enforcement is via table column schema and section rules only — zero of five criteria have labeled prompts |
| A-12 | BRIDGE dual-closure | **PASS** | Dedicated "## BRIDGE ARTIFACTS" section names Q3 with "(closes C-05 → R-02)" and Q4 with "(closes C-05 → C-04)" as distinct named artifacts in the template body — explicit criterion-chain references present; not column-level closure |
| A-13 | Tabular column schema | **PASS** | All major sections (FM Inventory, Workaround Profile, Switching Cost, Threat Assessment, Defeat Conditions, Bridge Artifact tables, Completeness Check) are tables with named columns |
| A-14 | FM inventory as dedicated named table | **PASS** | "## SECTION 1 — FAILURE MODE INVENTORY" titled table; FM-[N] is first column; positioned before Section 5 DC table |
| A-15 | Trailing completeness checklist | **PASS** | "## COMPLETENESS CHECK" at structural end; one item per essential criterion |
| A-16 | FM Inventory primary key constraint | **PASS** | Blockquote in Section 1 body: "**PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any downstream section of this document unless it has an assigned row in this table." |
| A-17 | Question coverage all 5 | **FAIL** | Same gap as A-11 — no criterion-labeled questions for C-01 through C-05 |
| A-18 | Trailing checklist binary format + full coverage | **PASS** | "| Criterion | Check (Y / N) |" binary format; all five C-01–C-05 criteria listed |
| A-19 | Bidirectional referential integrity | **PASS** | Source end (Section 1): "PRIMARY KEY CONSTRAINT… No FM-[N] identifier may appear in any downstream section." Citation end (Section 5): "**REFERENTIAL INTEGRITY RULE**: Every FM-[N] cited in this table must have a corresponding assigned row in the FM Inventory (Section 1)." Both ends present as separate named rules. |
| A-20 | Inline example in unit-bearing column labels | **PASS** | "Frequency (e.g., 3×/month)" in Section 1; "Ongoing cost (e.g., 2 hours/week)" and "Duration in active use (e.g., 18 months)" in Section 2; "Estimate (e.g., 3 days)" and per-row examples "(e.g., 4 hours/person)", "(e.g., 1 sprint delay)", "(e.g., $8,000)" in Section 3 |

**Advanced subtotal**: A-10(5) + A-12(5) + A-13(5) + A-14(5) + A-15(5) + A-16(5) + A-18(5) + A-19(5) + A-20(5) = **45/55**

**V-01 Total: 145/155**

**A-12 status: PASS** — first pass in nine rounds. Named artifact + chain reference in dedicated BRIDGE ARTIFACTS section satisfies the criterion.

---

## V-02 — Lifecycle emphasis (FAIL-FIRST DECLARATION names Q3/Q4 as stages)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Stage 3 table; "> **C-01 question**: What is the exact name of the workaround — the specific tool, file type, or procedure name? Not 'a manual process.' Who performs it? What is the ongoing cost per week or sprint, with a unit?" |
| C-02 | Switching cost quantified | **PASS** | Stage 4 table; "> **C-02 question**: …Every estimate must carry a number and a unit — 'significant' fails." |
| C-03 | Inertia threat score declared | **PASS** | Stage 5A table; "> **C-03 question**" present; deviation requires "specific quantified condition" |
| C-04 | Defeat conditions identified | **PASS** | Stage 5B DC table; "> **C-04 question**" with falsifiability requirement |
| C-05 | Failure modes identified | **PASS** | Stage 1 FM table; "> **C-05 question**": "Where specifically does the current workaround… fail… produce errors… hit a scale ceiling?" |

**All essential: PASS (100/100)**

### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | "## FAIL-FIRST DECLARATION" is the structural first section; six-stage lifecycle declared with FM Inventory as Stage 1; "This is the structural foundation. Nothing else is authored until Stage 1 has at least two rows." |
| A-11 | Question per criterion (3+) | **PASS** | All 5 criteria have labeled questions: C-05 in Stage 1, C-01 in Stage 3, C-02 in Stage 4, C-03 in Stage 5A, C-04 in Stage 5B |
| A-12 | BRIDGE dual-closure | **PASS** | FAIL-FIRST DECLARATION names "**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02)" and "**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04)" as lifecycle stages with chain references; echoed as named status checks in Stage 2 |
| A-13 | Tabular column schema | **PASS** | FM Inventory (Stage 1), Workaround Profile (Stage 3), Switching Cost (Stage 4), Threat Assessment (Stage 5A), Defeat Conditions (Stage 5B), Completeness Check — all tabular; Stage 2 bridge verification uses checkbox format (not a major output section) |
| A-14 | FM inventory as dedicated named table | **PASS** | "## STAGE 1 — FAILURE MODE INVENTORY" titled table; FM-[N] first column; precedes Stage 5 |
| A-15 | Trailing completeness checklist | **PASS** | "## COMPLETENESS CHECK" at structural end; 5 criterion items |
| A-16 | FM Inventory primary key constraint | **PASS** | Blockquote in Stage 1: "**PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any later section unless it has an assigned row here. Assign identifiers in this table first." |
| A-17 | Question coverage all 5 | **PASS** | C-05 (Stage 1), C-01 (Stage 3), C-02 (Stage 4), C-03 (Stage 5A), C-04 (Stage 5B) — all five present |
| A-18 | Trailing checklist binary format + full coverage | **PASS** | "| Criterion | Check (Y / N) |" binary column; all five C-01–C-05 listed |
| A-19 | Bidirectional referential integrity | **PASS** | Source (Stage 1): "PRIMARY KEY CONSTRAINT… No FM-[N] identifier may appear in any later section." Citation (Stage 5B): "**REFERENTIAL INTEGRITY RULE** (citation point): Every FM-[N] cited here must have a corresponding assigned row in the FM Inventory (Stage 1)." Both ends distinct and separately stated. |
| A-20 | Inline example in unit-bearing column labels | **FAIL** | Stage 1 "Frequency" column lacks inline example (compare V-01: "Frequency (e.g., 3×/month)"); Stage 5B "Measurable threshold" column has no example (compare V-04/V-05: "(e.g., >10MB, >3 failures/week)") |

**Advanced subtotal**: A-10(5) + A-11(5) + A-12(5) + A-13(5) + A-14(5) + A-15(5) + A-16(5) + A-17(5) + A-18(5) + A-19(5) = **50/55**

**V-02 Total: 150/155**

---

## V-03 — Phrasing register (imperative BRIDGE COMMANDs)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | "[C-01 COMMAND]: NAME the specific workaround. Not 'a manual process.'… NAME the role performing it. QUANTIFY the ongoing cost with a number and unit." Table with "Ongoing cost (e.g., 2 hours/week)" column |
| C-02 | Switching cost quantified | **PASS** | "[C-02 COMMAND]: IDENTIFY at least two cost categories. QUANTIFY each with a number and unit."; "> UNIT RULE: EVERY estimate carries a number and unit. 'Significant' is REJECTED." |
| C-03 | Inertia threat score declared | **PASS** | "[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH. IF deviating from HIGH, STATE a specific quantified condition" |
| C-04 | Defeat conditions identified | **PASS** | "[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4 triggers above. CITE the FM-[N] driving each." |
| C-05 | Failure modes identified | **PASS** | "[C-05 COMMAND]: NAME every specific failure mode… ASSIGN an FM-[N] identifier. MINIMUM 2 rows. REJECT any entry where the failure description is generic." |

**All essential: PASS (100/100)**

### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | "**[FAIL-FIRST DECLARATION]**: Start with failure modes. The workaround's failure is the only evidence that inertia can be beaten… ENUMERATE failures first." Label as first structural element with rationale |
| A-11 | Question per criterion (3+) | **PASS** | All 5 criteria have labeled imperative commands: [C-05 COMMAND], [C-01 COMMAND], [C-02 COMMAND], [C-03 COMMAND], [C-04 COMMAND] — imperative commands qualify as "explicitly labeled prompts" |
| A-12 | BRIDGE dual-closure | **PASS** | "**[BRIDGE Q3 COMMAND — closes C-05 → R-02]**" and "**[BRIDGE Q4 COMMAND — closes C-05 → C-04]**" — explicitly named artifacts in template body with criterion-chain references; positioned inline after FM table, before Section 2 |
| A-13 | Tabular column schema | **PASS** | Section 1 FM Inventory, Section 2 Workaround Profile, Section 3 Switching Cost, Section 4 Threat Assessment, Section 5 Defeat Conditions, Completeness Check — all tabular; bridge COMMANDs use checkbox verification (not a major output section) |
| A-14 | FM inventory as dedicated named table | **PASS** | "## 1. FAILURE MODE INVENTORY" titled table; FM-[N] first column; precedes Section 5 |
| A-15 | Trailing completeness checklist | **PASS** | "## COMPLETENESS CHECK" at end; 5 criterion items |
| A-16 | FM Inventory primary key constraint | **PASS** | "**[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers here. NO FM-[N] reference may appear in any later section without a corresponding row in this table." — labeled rule in Section 1 body |
| A-17 | Question coverage all 5 | **PASS** | All five criteria covered by labeled commands |
| A-18 | Trailing checklist binary format + full coverage | **PASS** | "| Criterion | Check (Y / N) |" binary; all 5 criteria listed |
| A-19 | Bidirectional referential integrity | **PASS** | Source (Section 1): "[A-16 PRIMARY KEY RULE]… NO FM-[N] reference may appear in any later section without a corresponding row in this table." Citation (Section 5): "**[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST have an assigned row in the FM Inventory above. DO NOT introduce FM references not assigned in Section 1." Both ends present as labeled rules. |
| A-20 | Inline example in unit-bearing column labels | **FAIL** | Section 1 "How often" column has no inline example; Section 2 "Duration in use" has no example; Section 5 "Measurable threshold" has no example — multiple unit-bearing/unit-adjacent columns without inline examples |

**Note on prediction matrix**: The variation designer predicted A-19 FAIL for V-03, but the actual template includes "[A-19 CITATION INTEGRITY RULE]" labeled in Section 5 and "[A-16 PRIMARY KEY RULE]" in Section 1. A-19 passes; only A-20 fails.

**Advanced subtotal**: A-10(5) + A-11(5) + A-12(5) + A-13(5) + A-14(5) + A-15(5) + A-16(5) + A-17(5) + A-18(5) + A-19(5) = **50/55**

**V-03 Total: 150/155**

---

## V-04 — Output format + lifecycle (dual-position Q3/Q4)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 2 table; "> **C-01 question**: What is the exact name of the workaround… Not 'a manual process.' Who performs it? What is the ongoing cost with a unit?" |
| C-02 | Switching cost quantified | **PASS** | Section 3 table with 4 rows; "> **C-02 question**"; "Every estimate must carry a number and unit. 'Significant' fails C-02." |
| C-03 | Inertia threat score declared | **PASS** | Section 4 table; "> **C-03 question**"; "If not HIGH, state a specific quantified condition — not a qualitative judgment." |
| C-04 | Defeat conditions identified | **PASS** | Section 5B DC table; "> **C-04 question**"; falsifiability requirement explicit |
| C-05 | Failure modes identified | **PASS** | Section 1 FM table; "> **C-05 question**": "Where specifically does the current workaround… fail, produce errors, cause rework, or hit a scale ceiling?" |

**All essential: PASS (100/100)**

### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | "## FAIL-FIRST DECLARATION" first structural section; names Q3/Q4 and states "Populate Section 1 fully. Verify Q3 and Q4. Then proceed in order." |
| A-11 | Question per criterion (3+) | **PASS** | All 5 criteria have labeled criterion questions: C-05 (Section 1), C-01 (Section 2), C-02 (Section 3), C-03 (Section 4), C-04 (Section 5B) |
| A-12 | BRIDGE dual-closure | **PASS** | Dual-position naming: FAIL-FIRST DECLARATION names "**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02)" and "**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04)"; echoed as "## BRIDGE ARTIFACT VERIFICATION" section with dedicated tables after FM Inventory |
| A-13 | Tabular column schema | **PASS** | All major sections tabular: FM Inventory, Bridge Verification tables (Q3 and Q4), Workaround Profile, Switching Cost, Threat Assessment, Defeat Conditions, Completeness Check |
| A-14 | FM inventory as dedicated named table | **PASS** | "## SECTION 1 — FAILURE MODE INVENTORY" titled table; FM-[N] first column; before Section 5 |
| A-15 | Trailing completeness checklist | **PASS** | "## COMPLETENESS CHECK" at end; 5 criterion items |
| A-16 | FM Inventory primary key constraint | **PASS** | Blockquote in Section 1: "**PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any downstream section unless it has an assigned row in this table." |
| A-17 | Question coverage all 5 | **PASS** | All five criteria covered |
| A-18 | Trailing checklist binary format + full coverage | **PASS** | Binary Y/N; all 5 criteria |
| A-19 | Bidirectional referential integrity | **PASS** | Source (Section 1): "PRIMARY KEY CONSTRAINT… No FM-[N] identifier may appear in any downstream section." Citation (Section 5B): "**REFERENTIAL INTEGRITY RULE** (citation point): Every FM-[N] cited in this table must have a corresponding assigned row in the FM Inventory (Section 1). Do not reference FM identifiers not assigned above." |
| A-20 | Inline example in unit-bearing column labels | **FAIL** | Section 1 "Frequency (e.g., 2×/sprint)" ✓; Section 2 "Ongoing cost (e.g., 2 hours/week)" ✓ but "Duration in active use" has no example (V-01/V-05 both include "(e.g., 18 months)"); Section 5B "Threshold (e.g., >10MB, >3 failures/week)" ✓ — one missing inline example fails the "every column label" condition |

**Advanced subtotal**: A-10(5) + A-11(5) + A-12(5) + A-13(5) + A-14(5) + A-15(5) + A-16(5) + A-17(5) + A-18(5) + A-19(5) = **50/55**

**V-04 Total: 150/155**

---

## V-05 — All three axes combined

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | "[C-01 COMMAND]: NAME the specific workaround — tool name, file type, or procedure name. NAME the role performing it. QUANTIFY the ongoing cost with a number and unit." Table with "Ongoing cost (e.g., 2 hours/week)" |
| C-02 | Switching cost quantified | **PASS** | "[C-02 COMMAND]: IDENTIFY at least two cost categories. QUANTIFY each with a number and unit. NAME the role bearing each cost."; "> [UNIT RULE]: EVERY estimate carries a number and unit." |
| C-03 | Inertia threat score declared | **PASS** | "[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH." |
| C-04 | Defeat conditions identified | **PASS** | "[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from Q4 triggers. CITE the FM-[N] driving each." |
| C-05 | Failure modes identified | **PASS** | "[C-05 COMMAND]: NAME every specific failure mode… MINIMUM 2 rows. REJECT generic descriptions" |

**All essential: PASS (100/100)**

### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | "## [FAIL-FIRST DECLARATION]" first structural section; names Q3/Q4 as bridge artifacts; "ENUMERATE failures first." |
| A-11 | Question per criterion (3+) | **PASS** | [C-05 COMMAND], [C-01 COMMAND], [C-02 COMMAND], [C-03 COMMAND], [C-04 COMMAND] — all five labeled |
| A-12 | BRIDGE dual-closure | **PASS** | Triple-position naming: FAIL-FIRST DECLARATION names "**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02)" and "**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04)"; then "[BRIDGE Q3 COMMAND — closes C-05 → R-02]" and "[BRIDGE Q4 COMMAND — closes C-05 → C-04]" inline after FM table with dedicated verification tables |
| A-13 | Tabular column schema | **PASS** | All major sections tabular; FM Inventory, Bridge Q3/Q4 verification tables, Workaround Profile, Switching Cost, Threat Assessment, Defeat Conditions, Completeness Check |
| A-14 | FM inventory as dedicated named table | **PASS** | "## SECTION 1 — FAILURE MODE INVENTORY" titled; FM-[N] first column; before Section 5 |
| A-15 | Trailing completeness checklist | **PASS** | "## COMPLETENESS CHECK" at end; 5 criteria |
| A-16 | FM Inventory primary key constraint | **PASS** | "> **[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers here. NO FM-[N] reference may appear in any later section without a row in this table." — criterion-code labeled rule in Section 1 body |
| A-17 | Question coverage all 5 | **PASS** | All five covered |
| A-18 | Trailing checklist binary format + full coverage | **PASS** | Binary Y/N; all 5 criteria |
| A-19 | Bidirectional referential integrity | **PASS** | Source (Section 1): "[A-16 PRIMARY KEY RULE]… NO FM-[N] reference may appear in any later section without a row in this table." Citation (Section 5): "> **[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST have an assigned row in the FM Inventory (Section 1). DO NOT introduce FM references not assigned above. VERIFY before filling." Both ends labeled with criterion codes. |
| A-20 | Inline example in unit-bearing column labels | **PASS** | Section 1: "Failure description (e.g., CSV export silently truncates at 65,536 rows)", "Actor / role (e.g., data-ops team)", "Trigger (e.g., file > 10MB)", "Frequency (e.g., 2×/sprint)" — every column has an inline example; Section 2: "Ongoing cost (e.g., 2 hours/week)", "Duration in use (e.g., 18 months)"; Section 3: "Estimate (e.g., 3 days)", "Role bearing it (e.g., data-ops team)"; Section 5: "Threshold (e.g., >10MB)" |

**Advanced subtotal**: all 11 × 5 = **55/55**

**V-05 Total: 155/155** — first perfect score in scout-inertia quest series

---

## Composite Scores and Ranking

| Rank | Variation | Axis | Essential | Advanced | Total | All Essential | A-12 |
|------|-----------|------|-----------|----------|-------|---------------|------|
| 1 | **V-05** | All three axes | 100/100 | 55/55 | **155/155** | Yes | **PASS** |
| 2 | V-02 | Lifecycle | 100/100 | 50/55 | **150/155** | Yes | **PASS** |
| 2 | V-03 | Phrasing register | 100/100 | 50/55 | **150/155** | Yes | **PASS** |
| 2 | V-04 | Format + lifecycle | 100/100 | 50/55 | **150/155** | Yes | **PASS** |
| 5 | V-01 | Output format | 100/100 | 45/55 | **145/155** | Yes | **PASS** |

**Ties (V-02, V-03, V-04) broken by axis breadth**: V-04 is architecturally closer to V-05 (dual-position bridge naming + full tabular schema + all criterion questions); V-02 and V-03 each miss A-20 in more columns.

---

## A-12 Status

**A-12 passes in all five R9 variations** — the first round where it has ever passed. The structural move that unlocked it: explicitly naming "Q3" and "Q4" as distinct artifacts in the template body with text "(closes C-05 → R-02)" and "(closes C-05 → C-04)". Column-level FM→actor and FM→trigger closure (as in R8 V-01) was never sufficient; the named-artifact requirement is not met by required columns alone.

---

## Excellence Signals from V-05

**1. All-column concrete example annotation**
V-05 extends inline examples beyond unit-bearing columns to every column in the FM Inventory: "Failure description (e.g., CSV export silently truncates at 65,536 rows)", "Actor / role (e.g., data-ops team)", "Trigger (e.g., file > 10MB)". Prior pattern A-20 captures unit-bearing columns only; V-05 demonstrates that non-unit columns (description, role, trigger) can also carry concrete examples that anchor format expectations at the cell level. Maximum-density format anchoring throughout.

**2. Criterion-code labeling of structural constraint rules**
V-05 (and V-03) label integrity constraint rules with their rubric criterion codes: "[A-16 PRIMARY KEY RULE]" and "[A-19 CITATION INTEGRITY RULE]". Prior templates named rules descriptively ("PRIMARY KEY CONSTRAINT", "REFERENTIAL INTEGRITY RULE") without linking them to the rubric criteria they enforce. Criterion-code labeling creates explicit bidirectional traceability: an author sees both the rule and the rubric criterion it closes, without needing to cross-reference the rubric separately.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["All-column concrete example annotation — V-05 embeds inline examples in every column label including descriptive and format-guided columns (not just unit-bearing ones), creating maximum-density format anchoring; extends A-20 pattern beyond cost/unit columns to failure description, actor, trigger columns", "Criterion-code labeling of structural constraint rules — rules labeled [A-16 PRIMARY KEY RULE] and [A-19 CITATION INTEGRITY RULE] link each rule directly to its rubric criterion, creating explicit bidirectional traceability between template enforcement and rubric criteria without requiring a separate cross-reference"]}
```
