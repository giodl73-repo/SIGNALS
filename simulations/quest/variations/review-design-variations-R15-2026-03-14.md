Written to `simulations/quest/rubrics/review-design-variate-R15-2026-03-15.md`.

---

## review-design — Round 15 Variations

**Baseline**: R14 V-02 (BLOCK 2.7 registry carrying all 42 prior criteria)
**New criteria**: C-43 (BLOCK 2.7 position lock) + C-44 (dual-path mismatch halt)

---

### Single-axis variations

**V-01 | Axis: C-44 Dual-Path Resolution Labeling**
Hypothesis: the R14 "either...or" single-sentence F-28 puts directional ambiguity at the exact halt moment. Splitting into two labeled sentences — **Downstream fix** (correct the Section value) and **Upstream fix** (add the missing P1 finding to BLOCK 2 and update BLOCK 2.7) — removes that ambiguity. BLOCK 2.7 structure is carried unchanged from R14 V-02.

**V-02 | Axis: C-43 BLOCK 2.7 Position Lock**
Hypothesis: agents may defer registry construction to BLOCK 5 or omit the dedicated block entirely. Adding a **POSITION CONSTRAINT** paragraph to the BLOCK 2.7 header — naming the conformant lifecycle order (`BLOCK 2 → BLOCK 2.5 → BLOCK 2.7 → BLOCK 3`), stating inline-at-BLOCK-5 is non-conformant, and having F-30 name the correct position in its repair instruction — enforces C-43 at the declaration site.

**V-03 | Axis: Phrasing Register — Operational-Directive**
Hypothesis: formal-modal register (SHALL/MUST/fires/halt/F-ID) places enforcement at formal distance. Rewriting in numbered Steps with `Required:` constraints and `fix (1)/fix (2)` repair options (no F-IDs) collapses that distance. Step 2.7 = "Section Map" with `build-before` instruction rather than a position constraint paragraph. Tests whether operational register achieves comparable C-43/C-44 compliance.

---

### Combination variations

**V-04 | Axes: C-43 position lock + C-44 labeled dual-path + lifecycle seals + C-37 anaphoric completeness**
Combines V-01 (labeled F-28) + V-02 (BLOCK 2.7 position constraint) + adds `BLOCK N SEALED` statements after each block + all F-IDs use referentially-complete halt clauses ("Populate the [named cell] before continuing. Halt." — not bare "Populate. Halt.").

**V-05 | Axes: declarative register + expanded C-44 + C-43 + Elevation Record**
Carries R14 V-05's `CONSTRAINT VIOLATED:` prefix and "This block produces..." framing. Adds BLOCK 2.7 position constraint. Expands C-44 dual-path coverage beyond F-28 to **all cross-block reference mismatch halts**: F-03, F-10, F-15, F-16, F-17, and F-28 each now specify both a downstream correction and an upstream addition path. BLOCK 3 carries an Elevation Record feeding a consensus-elevation ordering rule in BLOCK 5.

---

Key R15 encoding decisions:
- C-43 inline-pre-check (V-03 from R14) **fails** — V-03 in R15 uses a different axis (register) while keeping BLOCK 2.7 as a dedicated step
- C-44 exempt classes (F-01, F-04 structural absence; F-09, F-12 count-parity) are not given dual-path treatment in any variation
- C-37 anaphoric completeness isolated to V-04 to test its independent contribution
