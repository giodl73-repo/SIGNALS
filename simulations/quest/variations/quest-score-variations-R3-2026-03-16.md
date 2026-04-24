Written to `simulations/quest/golden/quest-score-variate-R3-2026-03-16.md`.

---

## quest-score Variations -- Round 3 (v3-2026-03-16 rubric)

**What changed from R2 to R3:** Two new Aspirational criteria (C-13, C-14) and N_aspirational bumped 4 -> 6. All R3 variations carry R2's D+E+F base forward (updated F for the new denominator).

---

### Axis selection

| Axis | Label | What it targets |
|------|-------|-----------------|
| **G** | Output-level delta declaration | C-13 PASS: requires the scorer to WRITE a `FORMULA VERSION DELTA` block in their Phase 1 output naming prior=4, current=6. R2's Axis F put the alert in the prompt; C-13 requires it in the output. |
| **H** | In-template Phase 2 entry lock | C-14 PASS: replaces the advisory MODEL CELL instruction with a pre-labeled first row in the verdict table itself. The scorer fills a structurally-locked position at Phase 2 entry rather than following advisory prose. |
| **I** | Per-calculation denominator annotation | C-10/C-13 at the calculation site: every composite score row in Phase 3a carries `A=[n]/6 [N_aspirational=6, v3]`. Stale denominators become visually inconsistent with the template format. Secondary question: does repeated current-value annotation satisfy C-13 (which requires naming the prior value too), or only produce PARTIAL? |

### Variation map

| Variation | Axes | Targets | Key mechanism |
|-----------|------|---------|---------------|
| V-01 | G | C-13 | Required FORMULA VERSION DELTA output block before load summary |
| V-02 | H | C-14 | Pre-labeled `[PHASE 2 ENTRY -- MODEL CELL]` first row in verdict template + PLACEMENT VERIFIED line |
| V-03 | I | C-10/partial C-13 | `A=[n]/6 [N_aspirational=6, v3]` annotation on every composite score row |
| V-04 | G+H | C-13+C-14 | Delta block (Phase 1) + pre-labeled entry cell (Phase 2) -- no overlap, should be fully additive |
| V-05 | G+H+I | C-13+C-14+C-10 | All three: lifecycle-distributed enforcement at Phase 1, Phase 2 entry, and Phase 3 per-row |

### Key design choice

The D+E+F base is included in all variations (not just combinations) because C-11 and C-12 are established rubric criteria. Single-axis R3 variations isolate only the new axis against the validated base -- the same design pattern as R2, which added D, E, and F one at a time against R1's validated base.
