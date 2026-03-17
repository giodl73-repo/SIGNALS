Written to `simulations/quest/rubrics/corps-rob-rubric-v14-2026-03-17.md`.

---

**v14 adds 2 criteria from R13 excellence signals:**

**C-43 — Criterion Enumeration Label-Plus-Description Pairing** (C-42 dep)
- Signal: V-01's C-42 pass uses `"C-30 (Run-Level Preamble Schema with Named Post-Stage Reference)"` — both criterion ID and parenthetical functional description. C-42 requires label *or* description; C-43 requires both simultaneously. Label alone is stable but opaque; description alone is readable but fragile under renumbering. Only the paired form is simultaneously stable and self-documenting.

**C-44 — AUDIT RESULT Block Independence Declaration** (C-35 dep)
- Signal: V-02's C-35 pass adds `"mandatory regardless of table presence"`. C-35 establishes ordering (table above, not replacing). C-44 establishes unconditional status (AUDIT RESULT required whether or not the table exists). Without C-44, the additive constraint can be misread as conditional: "keep AUDIT RESULT *when* table is added."

**Scoring impact:**

| | v13 | v14 |
|--|-----|-----|
| Aspirational pool | 34 × 5 = 170 | 36 × 5 = 180 |
| Max composite | 260 | 270 |

**Retroactive R13:** V-01 → 250/270 (gains C-43); V-02 → 250/270 (gains C-44). Both reach 250 via orthogonal paths — same score gap structure as R13 against v13.

**Persistent gap for R14:** C-43 and C-44 are mutually blocked across all R13 runs (V-01 fails C-35 blocking C-44; V-02 fails C-40 blocking C-42→C-43). C-39 remains universally unsatisfied. Ideal R14 combines the full glossary stack (C-40+C-42+C-43) with the full table stack (C-35+C-41+C-44) and a first C-39 attempt, targeting 265/270.
