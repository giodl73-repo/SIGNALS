Written to `simulations/quest/rubrics/trace-state-rubric-v12-2026-03-15.md`.

---

**Two new criteria extracted from Round 12:**

**C-34 — Disqualification-condition fusion in field labels**
Source: V-01 `[C-17: qualitative 'be thorough' does not satisfy]` and `[C-28: naming only the conflict outcome does not qualify]`. The field annotation carries the criterion ID co-located with the **specific negative test** — not a behavioral directive (that's C-30) but the exact pattern that *fails* the criterion. C-30 and C-34 are orthogonal axes of the same label; a single annotation can satisfy both if it carries a directive *and* a disqualification condition. A general prohibition without a named failing pattern does not qualify.

**C-35 — Section-label criterion-consequence fusion**
Source: V-02 `section label repeats "[C-17: if fewer than 5 blocks...]"`. The **section heading itself** carries criterion ID + conditional consequence clause — making enforcement visible at structural navigation level, before any field in the section is read. Distinct from C-23 (invalidation clause anywhere in section prose) and C-19 (artifact-level clause anywhere in hard constraints). A body-level invalidation sentence satisfies C-23 but not C-35.

**Rubric state:** inner v26 → v27 / outer v10 → v11. Pool: 25 → 27 aspirationals. Cap and any-5 threshold unchanged.
