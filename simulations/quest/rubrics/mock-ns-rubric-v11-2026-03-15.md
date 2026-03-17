**v11 written** to `simulations/quest/rubrics/quest-rubric-mock-ns-v11-2026-03-15.md`.

---

**Two new criteria extracted from Round 11:**

**C-32 — Pre-computation preamble positioning** (depends on C-31)
V-01's advancement: preamble moved to the very top of S-3, before the FLAG computation cases — not just before the prohibition rows. An executor gets the cross-reference map before encountering any FLAG logic, scaffolding both the computation and the prohibition rows rather than only the latter. Variants still positioned between computation and prohibition rows (R10 V-05, R11 V-02) pass C-31 but fail C-32.

**C-33 — Structured token resolution table** (depends on C-32)
V-02's advancement: prose preamble replaced by (a) an abbreviation key defining `:CS` / `:FC` suffix codes and (b) a structured table with Token / Step / Row type / Paired token / Direction columns. Enables O(1) lookup by token name vs. prose parsing. The encoding scheme is self-documenting at the preamble rather than implicit at the use site.

**Scoring**: aspirational denominator 23 → 25 (`pass/25 * 10`).
