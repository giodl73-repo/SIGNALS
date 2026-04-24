Written to `simulations/quest/rubrics/quest-variate-rubric-v13-2026-03-15.md`.

**Changes from v12 → v13:**

**C-37 confirmed** — Phase 2 STOP CONDITION manifest-destination coupling. The Phase 2 gate must read "Do not proceed to the Variation Completion Manifest until..." rather than "Do not begin Phase 3 until...". R13/V-02 cleanly ablated it (manifest and Phase 3 gate retained; only Phase 2 routing changed). Both V-01 and V-02 scored 100.00 under v12 — clean independent ablation.

**Scoring formula:** denominator 29 → 30.

**R13 tier structure under v13:**

| Rank | Variation | Score | Failures |
|------|-----------|-------|---------|
| 1 | V-01 full stack | 100.00 | — |
| 2 | V-02 (C-37 ablation) | 99.67 | C-37 |
| 2 | V-03 (C-36 ablation) | 99.67 | C-36 |
| 4 | V-05 (C-37+C-36 combo) | 99.33 | C-37, C-36 |
| 5 | V-04 (C-35 ablation) | 99.00 | C-35, C-36, C-37 |

Key structural note: V-02 and V-03 are symmetric at 99.67 — C-37 and C-36 are at different gate boundaries and neither entails the other's failure. V-04 sits below V-05 because C-35 ablation pulls both C-36 and C-37 down with it (three failures vs. two). No R13→R14 candidate identified.
