Written to `simulations/quest/golden/campaign-decide-variate-R20-2026-03-17.md`.

---

## Summary

**R20 variations** — all inherit R19 V-05 baseline (C-01..C-49):

| Var | Axis | New element | Candidate |
|-----|------|-------------|-----------|
| V-01 | Lifecycle emphasis | Phase gate pre-flight checklists — `[min met? Y/N] [FINDING REGISTER closed? Y/N] [density written? Y/N]` after each evidence phase | C-50 |
| V-02 | Output format | Recommendation calibration delta sentence after Phase 5 recommendation record table — `Confidence moved from {prior} to {final} because {FIDs}` | C-51 |
| V-03 | Inertia framing | Phase 3 segment table gains `Inertia Lock-in (H/M/L)` column, bridging Phase 1a Switching Cost to Phase 3 per-segment resistance | C-52 |
| V-04 | Combined V-01 + V-02 | Gate checklists + recommendation delta sentence | C-50 + C-51 |
| V-05 | Full integration | All three axes over R19 V-05 base, targeting 110.5/110.5 | C-50 + C-51 + C-52 |

**Key design decisions:**
- V-01 gate check is structurally distinct from C-46 density annotation — it consolidates three conditions into one binary line rather than counting one
- V-02 recommendation delta sentence is structurally parallel to the BECAUSE block but operates on the recommendation chain (C-47) rather than phase contributions
- V-03 inertia lock-in column creates a Phase 1a→Phase 3→Phase 5 inertia through-line that was previously only present at Phase 1a
