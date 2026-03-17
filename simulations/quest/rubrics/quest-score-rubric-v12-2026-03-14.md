Written to `simulations/quest/rubrics/quest-score-rubric-v12-2026-03-15.md`.

---

**Three new criteria extracted from R11:**

**C-30 — Multi-variation scoring uses shared baseline evidence table** (structure)
`(for C-02)` — The scorecard's "Shared baseline evidence" table consolidates 29×5=145 rows into a shared head + differentiating overrides. PARTIAL: table present but differentiating cells lack explicit override quotes.

**C-31 — Cascade auto-PASS SETUP block groups primary trigger and dependents** (structure)
`(for C-11)` — "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade" groups the chain visibly in SETUP. PARTIAL: cascade mentioned but primary/dependent distinction implicit. C-31 auto-PASS when C-07 does not fire.

**C-32 — SETUP notes design-time evaluation for template-structure criteria when cascade fires** (continuity)
`(for C-28)` — Explicit note that C-27/C-28 are still validated against the rubric template's static column order even when cascade auto-PASS fires at runtime. Prevents cascade silently bypassing template validation. PARTIAL: note present but specific template element not named. C-32 auto-PASS when C-07 does not fire.

**Cascade updates applied:**
- N_aspirational: 22 → 25 (each criterion: 10/25 = 0.40 pt)
- C-16 required list: added C-21 (v11 omission fix), C-31, C-32 → now 10 declarations
- C-14: 29-row → 32-row
- C-25 "Applied in this rubric": added C-30 (for C-02), C-31 (for C-11), C-32 (for C-28) → 9 entries
- C-03 design note: N_aspirational updated to 25
