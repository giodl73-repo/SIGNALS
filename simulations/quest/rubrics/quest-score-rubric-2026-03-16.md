Written to `simulations/quest/rubrics/quest-score-rubric-v1-2026-03-16.md`.

---

**Rubric summary:**

| Tier | ID | Criterion | Category |
|------|----|-----------|----------|
| Essential | C-01 | Rubric load verification | correctness |
| Essential | C-02 | Per-criterion verdict matrix | correctness |
| Essential | C-03 | Evidence for every verdict | correctness |
| Essential | C-04 | Composite score per output (with explicit calculation) | correctness |
| Essential | C-05 | Failure patterns section (required even when empty) | coverage |
| Recommended | C-06 | Ranked leaderboard | format |
| Recommended | C-07 | Excellence signals (output-criterion pair + structural mechanism) | depth |
| Recommended | C-08 | Per-output synthesis notes | depth |
| Aspirational | C-09 | Regression signals | behavior |
| Aspirational | C-10 | Score arithmetic verification | correctness |

**Key differences from the 2026-03-15 v1 cycle start:**

- **C-01 (load verification) is now Essential** — the prior cycle showed that skipping/abbreviating load is the leading indicator of downstream errors in verdict counts and formula denominators
- **C-04 now requires explicit calculation**, not just the final number — bare scores were the most common C-04 PARTIAL across Rounds 1-6
- **C-06 (leaderboard) moved to Recommended** — it reorganizes C-04 data and a missing leaderboard degrades but doesn't break a scoring output
- **C-07/C-08 split into excellence signals + per-output notes** — these test different depth properties and were conflated in the prior cycle
- **C-10 (arithmetic verification) added as Aspirational** — emerged as a round 4+ reliability signal in the prior cycle
