Written to `simulations/quest/rubrics/topic-plan-rubric-v12-2026-03-15.md`.

---

## Changes from v11 → v12

**Two new aspirational criteria** extracted from Round 12:

**C-40 — Null-case enforcement consolidated in COLUMN CONTRACT rule** (`enforcement`)

The discriminating signal is V-02's Rule 3. V-01/V-03 score PARTIAL on C-23 because their per-site null-case enforcement is inconsistently applied — Step 6 has both C-23 components, but Steps 3a/4/7 have only the verbatim template without the "do not omit" instruction. V-02 adds Rule 3 to CONTRACT ("A missing section is indistinguishable from a section that was skipped entirely") and has every null-case site cite "(Rule 3)" — both C-23 components fire via rule reference at every null site. C-40 applies the same architectural principle as C-36 (which consolidated enumerated-column constraints into a CONTRACT rule) to null-case enforcement.

**C-41 — Schema column definitions carry inline rule-reference annotations** (`enforcement`)

The discriminating signal is V-02's `[Rule 1: ADD / REMOVE / REPRIORITIZE]` annotations in schema columns. V-01/V-03 pass C-36 without inline schema annotations, leaving the governing rule implicit at the column level. C-41 closes the legibility gap by requiring each enumerated-value column to carry a compact annotation naming its governing CONTRACT rule — completing the three-point activation chain: **C-36** (rule above schema) → **C-41** (rule at each column) → **C-39** (rule at extraction step).

**Updated totals**: 41 criteria, 255 pts | Formula: `(essential/5×60) + (recommended/3×30) + (aspirational/33×165)` | Golden threshold bumped to **150**.
