Written to `simulations/quest/golden/corps-achievements-variate-R6-2026-03-16.md`.

---

## R6 — corps-achievements Variate Summary

**Variation axes selected**: C-21 (correction loop), C-22 (derivability elimination), C-23 (numbered sub-step gate language)

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | C-21 only | Formula mismatch triggers explicit table correction with numbered sub-steps on the formula gate — turns C-19 from display into closed-loop verification |
| **V-02** | C-22 only | Derivability test runs as a 3-step elimination protocol (Candidate → Topic-by-topic test → Verdict), discarding any insight reachable from a single topic |
| **V-03** | C-23 only | All multi-condition gates use numbered sub-steps throughout — gate language established once in a preamble, applied universally including the insight gate |
| **V-04** | C-21 + C-22 | Correction loop + derivability elimination — the two synthesis outputs (rankings and insight) each have their own closed verification loop |
| **V-05** | C-21 + C-22 + C-23 | All three: numbered sub-steps applied universally (C-23) means the correction loop gate (C-21) and derivability gate (C-22) are structurally consistent with every other gate in the skill |

**Key design choices that differentiate R6 from R5**:
- The Stagnation Pattern Registry is now explicit and shared across all 5 variations (enabling C-14 and C-17 without per-variation reinvention)
- The weighted formula `Score = (Signals×1) + (Topics×3) + (Milestones×5)` is canonicalized in the shared resources section
- C-20 (gate criterion IDs) appears in all 5 variations via `[C-NN]` bracket labels on every gate
- C-15 (gate failure names specific instance) is enforced in all 5 via explicit "cite the topic name / row" instructions in failure paths
- V-05 carries C-21 and C-22 inside C-23's numbered sub-step structure — the correction step and derivability verdict each become a numbered condition in their respective gates
