Written to `simulations/quest/golden/org-rob-variate-R6-2026-03-16.md`.

---

# org-rob -- Prompt Variations R6

**Rubric:** v5 (max 112). Two new criteria: C-18 (orientation.frame in ROLE: block) and C-19 (Via: as second column, 100% coverage). Gap from best R5 score (108) = 4 pts.

---

## Variation axes and predicted scores

| Variation | Axis | Base | C-18 | C-19 | Expected |
|-----------|------|------|------|------|----------|
| **V-01** | Output format: Frame citation in ROLE: block | V-02 R5 (106) | ++ | ++ (inherited) | **108** |
| **V-02** | Output format: Via: as second column | V-01 R5 (103) | ++ (inherited) | ++ (gains C-14 too) | **107** |
| **V-03** | Phrasing register: prohibition-mode enforcement | V-05 R5 (108) | ++ | ++ | **110** |
| **V-04** | Combination: C-18 + C-19 on gate+ledger base | V-04 R5 (104) | ++ | ++ (+ C-14) | **110** |
| **V-05** | Full unification targeting 112 | V-05 R5 (108) | ++ | ++ | **112** |

---

## Key structural changes per variation

**V-01** — Single addition to V-02 R5 ROLE: block: `Frame: orientation.frame = "{value}"` line. Via: second column was already present. C-18 is the only new structural element.

**V-02** — Single column reorder to V-01 R5 finding schema: `ID | Via | Finding | ...` instead of `ID | Finding | Severity | ...`. V-01 R5 already had orientation.frame in ROLE:. Via: second position earns both C-14 ++ (100% coverage, exceeds 50% floor) and C-19 ++ (second-column structural enforcement). Still lacks C-15 (verdict table) and C-17 (stage ledger) — reaches 107 without them.

**V-03** — Phrasing register applied to V-05 R5 structure. Every structural rule is a named SCHEMA VIOLATION type (`VIOLATION-01` through `VIOLATION-08`). The underlying architecture is V-05 R5's phase-gate + ledger + verdict-table + Via: field, with two structural changes baked in: Frame: line in ROLE: block and Via: moved to second column. Prohibition language is the variation axis; C-18 and C-19 are both targeted. Tests whether named violation types produce tighter structural compliance on C-11 exit conditions than instruction language.

**V-04** — V-04 R5 base (C-11 phase gates + C-17 write-ahead ledger, 104 under v5) gains three criteria in one change set: C-14 ++ and C-19 ++ (Via: second column in finding table) plus C-18 ++ (Frame: in ROLE: block). The Ledger also carries a `Via:` column — enabling cross-stage lens filtering for synthesis without adding a new structural artifact. C-15 (verdict table) remains o — intentionally excluded to test that the 110 path is achievable without it.

**V-05** — Minimal diff from V-05 R5: (1) ROLE: block gains `Frame: orientation.frame = "{value}"` line; (2) finding table column order changes from `ID | Finding | Via | ...` to `ID | Via | Finding | ...`. All C-09–C-17 mechanisms inherited intact. No structural conflict: Frame: is a stage-header property; Via: column position is a finding-row property. Both are additive at their respective layers.

---

## Structural independence verification (C-18 ∩ C-19)

C-18 and C-19 are independent by position: C-18 lives in the ROLE: block (stage header), C-19 lives in the finding table (finding row). A stage can earn C-18 without any Via: field; a finding table can earn C-19 without any Frame: citation. V-01 R6 earns both because it inherits C-19 from V-02 R5 and adds C-18 — same structural independence pattern as V-01/V-02 R5 on the same two criteria. V-05 R6 earns both by targeting each at its correct structural layer.
