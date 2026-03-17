Written to `simulations/quest/golden/topic-plan-golden-2026-03-15.md`.

**Summary:**

- **Prompt body**: simplified (PASS, 1601 words from 2008 — 20% reduction, all 10 essential criteria preserved)
- **Score**: 365/370 (rubric v20) — highest in the topic:plan series
- **One miss**: C-67 (null-labeling extended to all structured sections) is in the rubric but the simplified prompt's Rule 3 captures the failure condition without the explicit per-section extension sub-clauses; promoted to Round 21

**What made V-05 golden** (5 patterns):
1. INERTIA-GATE block self-enumerates its 4 reproduction sites (C-62) — auditable at definition time
2. Rule 3 carries an explicit failure condition inline, not just a positive constraint (C-66)
3. Split tables (4a Additions / 4b Removals+Reprioritizations) with symmetric "Inertia Rejected Because [REQUIRED]" columns (C-64)
4. Merge + rename prohibitions close both structural escapes from C-64 compliance (C-65)
5. "[REQUIRED]" in the column header as part of the enforcement contract — not a prose reminder
