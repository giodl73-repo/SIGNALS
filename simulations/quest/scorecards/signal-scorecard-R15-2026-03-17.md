---

## Round 15 Scorecard -- /signal (v14 rubric)

### Score Summary

| Variation | Axes  | Ess | Rec | Asp (36) | Composite  |
|-----------|-------|-----|-----|----------|------------|
| **V-04**  | X+Y   | 5/5 | 3/3 | 35/36    | **99.72**  |
| **V-05**  | X+Z   | 5/5 | 3/3 | 35/36    | **99.72**  |
| V-01      | X     | 5/5 | 3/3 | 34/36    | 99.44      |
| V-02      | Y     | 5/5 | 3/3 | 34/36    | 99.44      |
| V-03      | Z     | 5/5 | 3/3 | 34/36    | 99.44      |

### Independence Confirmation

| V | C-42 | C-43 | C-44 | Delta |
|---|------|------|------|-------|
| V-01 (X) | PASS | FAIL | FAIL | +0.278 |
| V-02 (Y) | PARTIAL | PASS | FAIL | +0.278 |
| V-03 (Z) | PARTIAL | FAIL | PASS | +0.278 |
| V-04 (X+Y) | PASS | PASS | FAIL | +0.556 |
| V-05 (X+Z) | PASS | FAIL | PASS | +0.556 |

**X, Y, Z confirmed independent.** Predicted scores match observed exactly. No interaction effects.

### Key findings

**C-42 for V-02/V-03**: FILTER Check 3 has verbatim strings but positional `(1)(2)(3)` labels. C-40 (FULL gate) explicitly accepts `(1)(2)(3)`, but C-42 (FILTER gate) requires named labels equivalent to `Header:/Separator:/Footer:`. Empirical R14 retroactive scoring (base = C-42 FAIL) confirms positional labels fail C-42 at FILTER gate. Scores PARTIAL = 0 pts.

**V-05 FILTER Format matrix cell**: Reads `Ch3 (C-42)` not `Ch3 (C-29)` — first appearance of axis-dependent matrix cell content. When X elevates the FILTER format check, the matrix cell should reference C-42, not the baseline C-29.

### Excellence signals from top variations

1. **FILTER/FULL gate symmetry** (V-04/V-05): `Header:/Separator:/Footer:` at FILTER Check 3 closes the last gate-format asymmetry.
2. **BARE GROUP OFFSET TABLE** (V-04): Fourth named formal table. Pattern confirmed: any per-namespace gate value should become a named table with first/last anchors per row.
3. **Axis-dependent matrix cells** (V-05): Matrix content tracks the highest active criterion per cell. When an axis elevates a gate check, the cell must reference the elevating criterion.

**R16 plan**: V-01 = X+Y+Z convergence, predicted **100.00**. v14 saturation.

```json
{"top_score": 99.72, "all_essential_pass": true, "new_patterns": ["X/Y/Z independence confirmed: each axis +0.278 independently, dual-axis +0.556, R16 V-01 (X+Y+Z) predicted at 100.00", "FILTER gate format check requires named labels (Header:/Separator:/Footer:) not positional (1)(2)(3) to satisfy C-42 -- positional scores partial not full", "axis-dependent matrix cells: when X is present FILTER Format cell references C-42 not C-29 -- matrix content tracks the highest active criterion per cell", "BARE GROUP OFFSET TABLE is the fourth named formal table -- any per-namespace gate value should become a named table with first/last self-documenting anchors per row"]}
```
 | PASS | DOMAIN NOUN TABLE present; all 12 footers use distinct nouns. |
| C-12 | PASS | PASS | PASS | PASS | PASS | ALIGNMENT WIDTH TABLE + rule; -> aligned within each section. |
| C-13 | PASS | PASS | PASS | PASS | PASS | Catalog format matches output spec; IS the output framing. |
| C-14 | PASS | PASS | PASS | PASS | PASS | BARE gate and FILTER gate both present with restart triggers. |
| C-15 | PASS | PASS | PASS | PASS | PASS | ALIGNMENT WIDTH TABLE: 12 rows with precomputed widths. |
| C-16 | PASS | PASS | PASS | PASS | PASS | Width table includes "example pad" column (char count + spaces) per row. |
| C-17 | PASS | PASS | PASS | PASS | PASS | NAMESPACE CATALOG first; PARSE MODE and gates follow. |
| C-18 | PASS | PASS | PASS | PASS | PASS | BARE gate Check 2: 61-line count with labeled per-namespace breakdown. |
| C-19 | PASS | PASS | PASS | PASS | PASS | PARSE MODE lists all 12 canonical names; unknown -> FULL fallback. |
| C-20 | PASS | PASS | PASS | PASS | PASS | FILTER gate Check 2: per-namespace canonical count with restart. |
| C-21 | PASS | PASS | PASS | PASS | PASS | BARE MODE: "Begin with scout-competitors. End with org-committee." |
| C-22 | PASS | PASS | PASS | PASS | PASS | Transcription gate: confirm 61 entries, emit character-for-character. |
| C-23 | PASS | PASS | PASS | PASS | PASS | "The catalog below IS the output for FULL and FILTER modes." |
| C-24 | PASS | PASS | PASS | PASS | PASS | All 3 modes verified: FULL (transcription), BARE (count), FILTER (count). |
| C-25 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 1 (all 12 present) + Check 2 (counts) with restart. |
| C-26 | PASS | PASS | PASS | PASS | PASS | Transcription gate: (8 scout + 4 draft + ... + 4 org = 61) -- labeled. |
| C-27 | PASS | PASS | PASS | PASS | PASS | Per-section count self-check vs canonical AND vs header N; restart. |
| C-28 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 3: "Canonical order: scout, draft... org. First: scout. Last: org." |
| C-29 | PASS | PASS | PASS | PASS | PASS | FILTER gate Check 3: section-format check with restart (any form). |
| C-30 | PASS | PASS | PASS | PASS | PASS | BARE MODE: slash-strip rule + worked examples for first and last entries. |
| C-31 | PASS | PASS | PASS | PASS | PASS | Both transcription gate and BARE gate Check 2 use "N namespace" labeled form. |
| C-32 | PASS | PASS | PASS | PASS | PASS | DOMAIN NOUN TABLE: named formal section, 12 rows. |
| C-33 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 3: all 12 canonical namespaces in canonical sequence. |
| C-34 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 4 (format): header/sep/footer with restart. |
| C-35 | PASS | PASS | PASS | PASS | PASS | BARE gate Check 3: order check with restart trigger. |
| C-36 | PASS | PASS | PASS | PASS | PASS | COMPLIANCE GATE COVERAGE MATRIX: named, 4 check types x 3 modes. |
| C-37 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 4: Header/Separator/Footer verbatim inline. |
| C-38 | PASS | PASS | PASS | PASS | PASS | BARE gate: positional line-range notation all 12 groups (inline or TABLE ref). |
| C-39 | PASS | PASS | PASS | PASS | PASS | Matrix cells carry check numbers all 11 cells. V-03/V-05 add criterion IDs (elevation). |
| C-40 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 4: "Header:", "Separator:", "Footer:" labels with verbatim strings. |
| C-41 | PASS | PASS | PASS | PASS | PASS | BARE gate: absolute offsets inline (V-01/V-03/V-05) or TABLE ref (V-02/V-04). |
| **C-42** | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** | V-01/V-04/V-05: "Header:/Separator:/Footer:" with verbatim strings at FILTER Check 3. V-02/V-03: verbatim strings present but labeled "(1)(2)(3)" only -- positional labels insufficient for C-42 (PARTIAL, not full pass). |
| **C-43** | FAIL | **PASS** | FAIL | **PASS** | FAIL | V-02/V-04: named BARE GROUP OFFSET TABLE with absolute ranges + first/last anchors; gate references table. V-01/V-03/V-05: inline absolute offsets, no named table. |
| **C-44** | FAIL | FAIL | **PASS** | FAIL | **PASS** | V-03/V-05: matrix cells carry "Ch1 (C-25)", "Ch3 (C-41)", etc. V-05 FILTER Format = "Ch3 (C-42)" -- axis-consistent. V-01/V-02/V-04: check numbers only. |

---

### Key Scoring Decisions

**C-42 for V-02/V-03 (no X-axis)**: FILTER gate Check 3 embeds verbatim strings with
positional "(1)", "(2)", "(3)" labels. C-42 requires explicit designators equivalent to
"Header:", "Separator:", "Footer:". Positional labels are accepted by C-40 for the FULL gate
(which explicitly lists "(1)(2)(3)" as acceptable), but C-42's pass condition for the FILTER
gate does not -- and the empirical R14 retroactive scoring (base V-01 = C-42 FAIL) establishes
that positional labels at FILTER Check 3 fail C-42. Verbatim strings earn PARTIAL (not full
pass). PARTIAL = 0 pts in aspirational tier.

**C-41 for V-02/V-04 (Y-axis)**: BARE gate Check 3 says "Consult BARE GROUP OFFSET TABLE
(precomputed)." Table contains all 12 groups with absolute line ranges. Absolute offsets exist
in the prompt as a named artifact; gate references rather than re-embeds. C-41 satisfied. PASS.

**C-39 for V-03/V-05 (Z-axis)**: Matrix cells carry "Ch1 (C-25)", "Ch2 (C-31)", etc.
C-39 requires check numbers only; criterion IDs are an elevation. C-39 PASS; C-44 also PASS.

**V-05 FILTER Format cell in matrix**: Reads "Ch3 (C-42)" rather than "Ch3 (C-29)". Matrix
is self-consistent: since X is present in V-05, FILTER Format references the elevating
criterion C-42, not the baseline C-29. First appearance of axis-dependent matrix cell content.

---

### Excellence Signals

**From V-04 (X+Y -- dual top scorer)**:

1. **FILTER/FULL format gate symmetry achieved**: "Header:", "Separator:", "Footer:" labeled
   verbatim embeds at FILTER Check 3 (C-42) mirror FULL gate Check 4 (C-40). Both gates carry
   self-contained format verification -- no cross-prompt recall at gate evaluation time.

2. **BARE GROUP OFFSET TABLE as fourth named formal table**: Inline absolute offsets -> named
   formal table with first/last entry anchors per row. Same elevation that C-15 applied to
   alignment widths, C-32 to domain nouns, C-36 to gate-check coverage. Pattern confirmed:
   any per-namespace value verified at gate time should become a named table with
   self-documenting rows.

**From V-05 (X+Z -- dual top scorer)**:

3. **Axis-dependent matrix cells**: FILTER Format cell reads "Ch3 (C-42)" not "Ch3 (C-29)"
   when X is present. Matrix content tracks which criterion is actually active at each cell,
   not a static baseline. When an axis elevates a gate check, the matrix cell must reference
   the elevating criterion. Pattern: *matrix cells should reflect the highest criterion
   satisfied at that gate/check-type intersection for the given variation.*

4. **Bidirectional navigation confirmed**: Check numbers navigate forward (matrix -> gate);
   criterion IDs navigate backward (gate -> matrix). Both directions verified. Matrix is a
   full navigable index.

---

### R16 Plan

**V-01 = X+Y+Z** (convergence). All three axes applied simultaneously:
- FILTER Check 3: "Header:", "Separator:", "Footer:" with verbatim strings (X = C-42)
- BARE GROUP OFFSET TABLE: named formal table + gate references table (Y = C-43)
- Coverage matrix: dual-index "Ch# (C-##)" all 11 cells; FILTER Format = "Ch3 (C-42)" (Z = C-44)

**Predicted**: 36/36 asp -> 10.00 -> composite **100.00**. v14 saturation confirmed if
independence holds (confirmed here at single-axis and dual-axis levels).

```json
{"top_score": 99.72, "all_essential_pass": true, "new_patterns": ["X/Y/Z independence confirmed: each axis +0.278 independently, dual-axis +0.556, R16 V-01 (X+Y+Z) predicted at 100.00", "FILTER gate format check requires named labels (Header:/Separator:/Footer:) not positional (1)(2)(3) to satisfy C-42 -- positional scores partial not full", "axis-dependent matrix cells: when X is present FILTER Format cell references C-42 not C-29 -- matrix content tracks the highest active criterion per cell", "BARE GROUP OFFSET TABLE is the fourth named formal table -- any per-namespace gate value should become a named table with first/last self-documenting anchors per row"]}
```
