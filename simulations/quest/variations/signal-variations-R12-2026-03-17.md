Written to `simulations/quest/golden/signal-variate-R12-2026-03-17.md`.

---

## Quest Variate -- /signal (Round 12)

**5 variations generated.** Sole R12 target: **C-36** (COMPLIANCE GATE COVERAGE MATRIX).

### Axis summary

| V | C-36 matrix | C-37 Check 4 | C-38 Check 3 BARE | Predicted |
|---|-------------|--------------|-------------------|-----------|
| V-01 (R) | PRESENT | name-ref | name-list | **99.33** |
| V-02 (S) | absent | verbatim embed | name-list | **99.33** |
| V-03 (T) | absent | name-ref | line-range | **99.33** |
| V-04 (R+S) | PRESENT | verbatim embed | name-list | **99.67** |
| V-05 (R+T) | PRESENT | name-ref | line-range | **99.67** |

### What each variation tests

**V-01 (R only)** — Adds the named COMPLIANCE GATE COVERAGE MATRIX (5-row table: scope, completeness, count, order, format x FULL/BARE/FILTER). Check 4 in FULL references SECTION FORMAT by name ("conform to the SECTION FORMAT template above") — C-37 absent. BARE Check 3 lists namespace groups by name — C-38 absent.

**V-02 (S only)** — No matrix. FULL Check 4 embeds all three SECTION FORMAT sub-elements verbatim (header pattern, `->` separator, footer pattern) — C-37 satisfied. BARE Check 3 uses name-list — C-38 absent.

**V-03 (T only)** — No matrix. FULL Check 4 name-ref — C-37 absent. BARE Check 3 uses full positional line-range notation ("first 8 lines are scout-* names, next 4...") — C-38 satisfied.

**V-04 (R+S)** — Matrix + verbatim Check 4. No line-range in BARE. Tests that R and S stack without interaction.

**V-05 (R+T)** — Matrix + line-range BARE Check 3. Name-ref Check 4. Tests that R and T stack without interaction.

### Coverage matrix design (C-36)

The matrix placed just before the individual gate sections:

```
  Dimension                         | FULL     | BARE     | FILTER
  ----------------------------------|----------|----------|--------
  No cross-namespace contamination  | N/A      | N/A      | Check 1
  All required namespaces present   | Check 1  | Check 2  | Check 2
  Canonical sub-skill count         | Check 2  | Check 2  | Check 2
  Canonical emit order              | Check 3  | Check 3  | N/A
  Section format compliance         | Check 4  | Check 1  | Check 3
```

If V-01=V-02=V-03=99.33, V-04=V-05=99.67, then V-06 (R+S+T, not generated) saturates v12 at **100.00**.
