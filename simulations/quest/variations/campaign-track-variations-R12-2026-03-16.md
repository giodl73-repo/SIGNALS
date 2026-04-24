Written to `simulations/quest/golden/campaign-track-variate-R12-2026-03-17.md`.

---

## campaign-track / Round 12 — Variations

**What's new in R12**: R10 V-05 produced two PASS+ signals that become C-36 and C-37 in rubric v11. Both follow the `assertion -> causal-explanation` pattern established by C-31/C-32, applied at new declaration sites.

---

### Variation Summary

| ID | Axis | New Criteria | Key Move |
|----|------|-------------|----------|
| **V-01** | C-36 only | C-36 | Phase 4 header names the stale-value consequence: `verdict_after` in `delta.md` becomes stale if Phase 4 exits without writing `story.md`; cascade rule is bare (no WHY) |
| **V-02** | C-37 only | C-37 | Cascade rule explains WHY non-cascade fields are excluded: they were finalized at Phase 3 Step B and Phase 4 cannot change them — per-field justification, not just scope listing |
| **V-03** | Phrasing register | none new | Replaces imperative phrasing with SHALL declarations throughout — all obligation sites, gates, forbidden actions, terminal checklist; tests whether formal register is a hidden scoring axis |
| **V-04** | C-36 + C-37 | C-36 + C-37 | Both causal framing patterns at the Phase 3/4 boundary; Post-Phase-4 section cross-references the Cascade Rule instead of repeating it |
| **V-05** | C-36 + C-37 + SHALL + lifecycle boundary | C-36 + C-37 + new? | Adds a **Phase Boundary Summary** section naming what each phase receives and what it cannot receive — creates three scoring surfaces each for C-36 and C-37; Phase 4 boundary entry names the stale consequence, Phase 3->4 boundary names the finalization constraint |

**Predicted leaderboard**: V-05 > V-04 > V-01 = V-02 > V-03

The core question for quest-score: does the Phase Boundary Summary in V-05 activate a new criterion around explicit input/output declaration (first R13 candidate), or does it only add scoring density for the existing C-36/C-37? V-03's SHALL experiment will reveal whether phrasing register surfaces as a rubric axis in a future round.
