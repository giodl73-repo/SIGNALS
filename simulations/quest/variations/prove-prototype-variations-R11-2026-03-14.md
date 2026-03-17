Here are the 5 complete variations for `prove-prototype` Round 11 (v11 rubric, 246 pts):

---

## Summary

**Base**: R10 V-05 (C-31 + C-32 + C-30, scores 231 on v11). The v11 ceiling requires adding C-33 and C-34 simultaneously.

**What changed in each variation:**

| # | Axis | Key change | C-33 | C-34 | Predicted |
|---|------|------------|------|------|-----------|
| V-01 | Inertia framing | Numbered CALIBRATE header on R10 V-04 base | ✓ | — | ~218 |
| V-02 | Output format | "Baseline (inertia competitor)" column label on R10 V-05 base | — | ✓ | ~231 |
| V-03 | Lifecycle emphasis | Document-level container manifest + enriched CLOSE COMPLETE on R10 V-04 base | — | — | ~211+ |
| V-04 | Combined: C-33 + C-34 | Both axes on R10 V-05 base — the R11 seed | ✓ | ✓ | **~238** |
| V-05 | Combined: all three | V-04 + manifest + enriched CLOSE COMPLETE | ✓ | ✓ | ~238+ |

---

**Key structural decisions:**

**V-01 vs V-02 use different bases** — V-01 uses R10 V-04 (no three-column table) to isolate C-33 cleanly; V-02 uses R10 V-05 (with C-30) to test whether the column label upgrade from "B-00 Baseline (Phase 4)" to "Baseline (inertia competitor)" is sufficient for C-34, or whether R10 V-05 already passed it.

**V-03 is a gap-signal probe.** The container manifest at the document top is not targeted at any known criterion. If V-03 scores higher than its V-04 base, the manifest is influencing the score through an unidentified mechanism — a potential v12 seed.

**V-04 is the R11 seed.** C-33 fires at CALIBRATE entry (pre-build); C-34 fires at the results table column header (post-build). They are structurally independent at different lifecycle stages — neither implies the other, so the combination requires a joint prompt.

**V-05 adds depth to V-04.** The enriched `CONTAINER: CLOSE COMPLETE` line now carries all five post-build result values (verdict, B-00 delta, counter-evidence disposition, limitation, replication status). If V-05 outscores V-04, the gap between them is the v12 seed.

Saved to `simulations/quest/rubrics/prove-prototype-rubric-v11-variate-R11-2026-03-15.md`.
