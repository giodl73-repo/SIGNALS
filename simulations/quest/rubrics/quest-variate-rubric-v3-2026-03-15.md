**v3 written** to `simulations/quest/rubrics/quest-rubric-variate-R3-2026-03-15.md`.

---

## What changed from v2 → v3

**5 new aspirational criteria** (C-14 through C-18), each traceable to a specific Round 2 variation:

| ID | Criterion | Source variation | Signal |
|----|-----------|-----------------|--------|
| C-14 | **Criterion-targeted axis selection** | V-01 | Axis chosen to target C-07 by ID; mechanism stated explicitly |
| C-15 | **Inline generation loop gate** | V-02 | Gate fires after each body, not post-generation; "fix before advancing" while context is active |
| C-16 | **Per-axis pole declaration before generation** | V-03 | Champion table declares current pole per axis — converts "inferable" to "explicitly stated" |
| C-17 | **Pre-generation axis lock** | V-04 | "Do not revise axis assignments after Phase N begins" — enforces C-04 as protocol, not intention |
| C-18 | **Single-axis comparison denominator** | V-04 + V-05 | Combination failure conditions name V-01 / V-03 as comparison baseline, not bare skill |

**Key distinctions added to Evaluator Notes:**
- C-14 vs C-07: passing C-07 (falsifiable) does not imply passing C-14 (criterion-targeted selection)
- C-15 vs C-08: independent — presence of baseline (C-08) doesn't mean the gate is in the loop (C-15)
- C-16 vs C-08: C-08 accepts "inferable"; C-16 requires structured per-axis declaration
- C-17 and C-18: vacuously true for single-axis-only outputs (no combination passes = no scope)

**Scoring formula**: aspirational denominator bumped from `/5` to `/10`. Total weight unchanged.
