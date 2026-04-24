Written to `simulations/quest/scorecards/signal-scorecard-R14-2026-03-17.md` (195 lines).

---

## Round 14 Scorecard -- /signal (v13 rubric)

### Score Summary

| Variation | Axes      | Ess | Rec | Asp (33) | Composite  |
|-----------|-----------|-----|-----|----------|------------|
| V-01      | U+V+W     | 5/5 | 3/3 | 33/33    | **100.00** |
| V-02      | U+V+W+X   | 5/5 | 3/3 | 33/33    | **100.00** |
| V-03      | U+V+W+Y   | 5/5 | 3/3 | 33/33    | **100.00** |
| V-04      | U+V+W+Z   | 5/5 | 3/3 | 33/33    | **100.00** |
| V-05      | U+V+W+X+Y | 5/5 | 3/3 | 33/33    | **100.00** |

**v13 saturation confirmed.** All five score 100.00.

### All-essential pass: YES (5/5 across all variations)

### Key scoring decisions

**C-38/C-41 for V-03/V-05 (Y-axis)**: BARE gate Check 3 says "Consult BARE GROUP OFFSET TABLE (precomputed)." The TABLE contains all 12 groups with absolute line ranges and first/last entry anchors. TABLE reference satisfies C-41's absolute-offset requirement -- the offsets are in the prompt as a named artifact; the gate references rather than re-embeds them. **PASS.**

**C-39 for V-04 (Z-axis)**: Matrix cells carry dual-index "Ch1 (C-25)", "Ch3 (C-41)", etc. C-39 only requires check numbers; criterion IDs are an elevation. **PASS.**

**C-29 for V-01/V-03/V-04 (no X-axis)**: FILTER gate Check 3 uses numbered "(1)(2)(3)" notation for header/separator/footer. C-29 requires the elements be present with restart -- notation style is not tested by v13. **PASS.**

### Excellence Signals

1. **U+V+W convergence** (V-01): Three axes targeting three distinct residual lookup steps each contribute +0.30 independently and jointly saturate v13 at 100.00.

2. **Named precomputed tables as canonical elevation form** (Y-axis, V-03/V-05): BARE GROUP OFFSET TABLE is the fourth named formal table in the prompt. TABLE form adds first/last entry anchors per row (self-documenting) and reduces gate verbosity to a single table reference. Pattern: *any per-namespace value verified at gate time should become a named formal table with self-documenting rows.*

3. **Dual-index matrix for bidirectional navigation** (Z-axis, V-04): Adding criterion IDs alongside check numbers in the matrix closes the reverse-lookup gap -- navigate from check number OR from criterion ID. Pattern: *a coverage matrix mapping in one direction leaves a reverse lookup gap; criterion IDs close it.*

### Post-v13 signals surfaced (deferred to v14)

- **X** (V-02/V-05): FILTER gate Check 3 labeled sub-elements -- FILTER analog of C-40
- **Y** (V-03/V-05): Named BARE GROUP OFFSET TABLE -- table analog of C-41
- **Z** (V-04): Criterion IDs in matrix -- dual-index elevation of C-39

R15 plan: single-axis isolation V-01=X, V-02=Y, V-03=Z; dual V-04=X+Y, V-05=X+Z; convergence V-06=X+Y+Z reserved for R16.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["named precomputed tables with first/last anchors per row are the canonical elevation form for per-group gate values", "dual-index matrix (check number + criterion ID) closes bidirectional navigation gap", "U+V+W convergence confirmed: three independent axes each +0.30 jointly saturate v13"]}
```
mes; explicit fallback. |
| C-20 | PASS | PASS | PASS | PASS | PASS | FILTER gate Check 2: per-namespace count with restart. |
| C-21 | PASS | PASS | PASS | PASS | PASS | BARE MODE: Begin scout-competitors. End org-committee. |
| C-22 | PASS | PASS | PASS | PASS | PASS | Transcription gate: confirm 61 entries; emit character-for-character. |
| C-23 | PASS | PASS | PASS | PASS | PASS | The catalog below IS the output for FULL and FILTER modes. |
| C-24 | PASS | PASS | PASS | PASS | PASS | All 3 modes gated: FULL (transcription), BARE (count), FILTER (count). |
| C-25 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 1 (presence) + Check 2 (counts) with restart. |
| C-26 | PASS | PASS | PASS | PASS | PASS | Transcription gate: (8 scout + 4 draft + ... + 4 org = 61) labeled. |
| C-27 | PASS | PASS | PASS | PASS | PASS | Per-section count self-check vs canonical AND vs header N; restart. |
| C-28 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 3: all 12 canonical names in sequence. |
| C-29 | PASS | PASS | PASS | PASS | PASS | FILTER gate Check 3: header/sep/footer (numbered or labeled); restart. |
| C-30 | PASS | PASS | PASS | PASS | PASS | BARE MODE: slash-strip rule + examples for first and last entries. |
| C-31 | PASS | PASS | PASS | PASS | PASS | Both transcription gate and BARE gate Check 2 use labeled N namespace form. |
| C-32 | PASS | PASS | PASS | PASS | PASS | DOMAIN NOUN TABLE: named section, 12 rows. |
| C-33 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 3: all 12 canonical namespaces in canonical sequence. |
| C-34 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 4 (format): header/sep/footer with restart. |
| C-35 | PASS | PASS | PASS | PASS | PASS | BARE gate Check 3: order check with restart. |
| C-36 | PASS | PASS | PASS | PASS | PASS | COMPLIANCE GATE COVERAGE MATRIX: 4 check types x 3 modes; 11 cells. |
| C-37 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 4: Header:/Separator:/Footer: labels with patterns inline. |
| C-38 | PASS | PASS | PASS | PASS | PASS | BARE gate Check 3: absolute ranges all 12 groups (inline or TABLE ref). |
| C-39 | PASS | PASS | PASS | PASS | PASS | Matrix cells carry check numbers; V-04 adds criterion IDs (Z). |
| C-40 | PASS | PASS | PASS | PASS | PASS | FULL gate Check 4: Header:/Separator:/Footer: labels with inline patterns. |
| C-41 | PASS | PASS | PASS | PASS | PASS | BARE gate Check 3: absolute offsets inline (V-01/V-02/V-04) or TABLE ref (V-03/V-05). |

Note on C-38/C-41 for V-03/V-05: BARE gate Check 3 says 'Consult BARE GROUP OFFSET TABLE
(precomputed).' The TABLE contains all 12 groups with absolute line ranges (1-8 scout,
9-12 draft, ..., 58-61 org) and first/last entry anchors per group. TABLE reference
satisfies the absolute-offset requirement: offsets are in the prompt as a named
precomputed artifact; the gate references rather than re-embeds them.

Note on C-39 for V-04: Matrix cells carry dual index 'Ch1 (C-25)', 'Ch3 (C-41)', etc.
This is an elevation beyond C-39 (which requires check numbers only). C-39 PASS.

---

## Ranking

All five tied at 100.00 under v13. Tiebreaker: post-v13 axis count.

| Rank | Variation | Score  | Post-v13 | Description |
|------|-----------|--------|----------|-------------|
| 1T   | V-05      | 100.00 | X+Y      | Labeled FILTER Check 3 + named BARE GROUP OFFSET TABLE |
| 1T   | V-02      | 100.00 | X        | Labeled FILTER gate Check 3 sub-elements |
| 1T   | V-03      | 100.00 | Y        | Named BARE GROUP OFFSET TABLE |
| 1T   | V-04      | 100.00 | Z        | Dual-index coverage matrix (check number + criterion ID) |
| 1T   | V-01      | 100.00 | --       | Pure U+V+W convergence; v13 saturation baseline |

V-01 is the critical result: U+V+W alone saturates v13 at 100.00.
V-05 is richest for v14 rubric development (X+Y present for dual-axis isolation).

---

## Excellence Signals

### Signal 1: U+V+W convergence confirmed -- v13 saturated at V-01

V-01 (pure U+V+W) scores 100.00. The R13 V-06 plan is realized. Independence of U, V, W
established in R13; joint convergence confirmed in R14.

Pattern: Three axes targeting three distinct residual lookup steps (matrix navigation,
element-name lookup, positional offset arithmetic) independently contribute +0.30 each
and jointly saturate the rubric when combined.

### Signal 2: Named precomputed tables are the canonical elevation form (Y-axis)

V-03/V-05 introduce the BARE GROUP OFFSET TABLE -- the fourth named precomputed table:
- ALIGNMENT WIDTH TABLE (C-15): per-namespace max command widths
- DOMAIN NOUN TABLE (C-32): per-namespace footer nouns
- COMPLIANCE GATE COVERAGE MATRIX (C-36): per-mode x per-check-type gate map
- BARE GROUP OFFSET TABLE (Y): per-namespace absolute line offset ranges with first/last anchors

The TABLE form adds: (1) first/last entry anchors make each row self-documenting;
(2) BARE gate Check 3 becomes a single-line table reference rather than 12-item inline list.

Pattern: Any per-namespace value verified at gate time should become a named formal table
with self-documenting rows (values + worked anchors per row).

### Signal 3: Dual-index matrix enables bidirectional navigation (Z-axis)

V-04 adds criterion IDs to matrix cells ('Ch1 (C-25)', 'Ch3 (C-41)', etc.).
The existing matrix supports gate-forward navigation only (mode x check-type -> check number).
The dual-index adds rubric-backward navigation (criterion ID -> gate and check number).

Pattern: A coverage matrix mapping in one direction (gate -> check) leaves a reverse
lookup gap. Adding criterion IDs makes it bidirectionally complete.

---

## R14 Empirical Findings

| Finding | Result |
|---------|--------|
| U+V+W convergence (V-01) saturates v13 at 100.00 | CONFIRMED |
| X axis (FILTER labeled Check 3) is post-v13 signal | CONFIRMED |
| Y axis (named BARE GROUP OFFSET TABLE) is post-v13 signal | CONFIRMED |
| Z axis (criterion IDs in matrix) is post-v13 signal | CONFIRMED |
| All 5 predicted 100.00 under v13 | CONFIRMED |

---

## R15 Plan

v14 formalizes three new criteria to isolate X, Y, Z independently.

C-42 (X, elevates C-40): FILTER gate Check 3 must label each SECTION FORMAT sub-element
explicitly ('Header:', 'Separator:', 'Footer:'). Closes labeled-embed symmetry gap between
FULL gate Check 4 (C-40) and FILTER gate Check 3.

C-43 (Y, elevates C-41): BARE gate order check must reference a named BARE GROUP OFFSET TABLE
rather than embedding the 12-group offset list inline. Same named-table elevation as
ALIGNMENT WIDTH TABLE (C-15) and DOMAIN NOUN TABLE (C-32).

C-44 (Z, elevates C-39): COMPLIANCE GATE COVERAGE MATRIX cells must carry both the
implementing check number AND the primary criterion ID. Enables matrix navigation from
criterion direction as well as gate direction.

R15 isolation plan (if v14 denominator = 36):

| V     | Axes        | X (C-42) | Y (C-43) | Z (C-44) | Predicted (36) |
|-------|-------------|----------|----------|----------|----------------|
| V-01  | U+V+W+X     | PASS     | FAIL     | FAIL     | 34/36 = 99.44  |
| V-02  | U+V+W+Y     | FAIL     | PASS     | FAIL     | 34/36 = 99.44  |
| V-03  | U+V+W+Z     | FAIL     | FAIL     | PASS     | 34/36 = 99.44  |
| V-04  | U+V+W+X+Y   | PASS     | PASS     | FAIL     | 35/36 = 99.72  |
| V-05  | U+V+W+X+Z   | PASS     | FAIL     | PASS     | 35/36 = 99.72  |
| V-06  | U+V+W+X+Y+Z | PASS     | PASS     | PASS     | 36/36 = 100.00 |

R16 convergence: V-06 saturates v14 at 100.00 if X, Y, Z prove independent.
