```markdown
# quest-score Rubric — v5

**Version:** v5
**Date:** 2026-03-16
**Prior version:** quest-score-rubric-v4-2026-03-16.md

---

## What changed v4 -> v5

**Two new aspirational criteria, sourced directly from R4 excellence signals:**

**C-17 — Self-referential anti-pattern priming** (from AF-6/AF-7 second-order compliance)
- Root pattern in R4: the top-scoring variation included anti-pattern entries (AF-6, AF-7)
  that primed against mechanical execution of the post-scoring scan itself and against
  misplaced anti-pattern table placement respectively; the failure mode enforcement
  mechanisms primed against their own failure modes, creating a second-order compliance
  guarantee; single-axis variations (scan only, or pre-placement only) did not produce
  this property
- The principle: a rubric or score report that only describes the mechanism without
  guarding against degenerate execution of that mechanism leaves a compliance gap; the
  scan can be present but mechanically executed (ticking boxes without checking content);
  the anti-pattern table can be present but placed in the wrong phase; naming these as
  anti-patterns before execution closes the gap
- Pass condition: the score report (or rubric driving it) contains at least one anti-pattern
  entry that targets the enforcement mechanisms defined in C-15 or C-16 themselves —
  i.e., an anti-pattern that says "do not execute the scan mechanically" or "do not place
  the anti-pattern table post-Phase-1"; the entry must be placed in the pre-execution
  priming section (satisfying C-16 placement) to count; an anti-pattern about the scan
  placed after Phase 1 fails; PARTIAL if a self-referential entry exists but is placed
  outside the pre-execution window

**C-18 — Full-envelope structural coverage** (from H+G combination achieving 8/8 aspirational)
- Root pattern in R4: front-loaded failure mode avoidance (BEFORE YOU BEGIN block satisfying
  C-16) combined with back-end named scan ([SCAN COMPLETE] token satisfying C-15) achieves
  maximum aspirational compliance by closing both ends of the execution window; variations
  with only pre-placement or only post-scan achieved at most 7/8 aspirational; the
  combination is not merely additive — it eliminates the entire class of mid-execution
  compliance drift by bookending structural work with explicit compliance checkpoints
- The principle: neither mechanism alone is sufficient for full-envelope coverage; pre-priming
  without a closing scan allows drift during execution; a closing scan without pre-priming
  arrives after first-structural-token decisions are made; only the H+G combination (Header
  priming + Gate scan) closes both ends
- Pass condition: the score report contains both (a) a pre-Phase-1 failure mode priming block
  that satisfies C-16 and (b) a post-output-block named scan that satisfies C-15, and both
  are present in the same execution unit (same phase sequence, same report); satisfying C-15
  alone or C-16 alone does not satisfy C-18; the criterion is specifically for the combination
  property; PARTIAL if both blocks are nominally present but one fails its own pass condition
  (e.g., scan present but covers only subset of outputs, or priming block placed mid-phase)

**Formula update:** A_count denominator `/8` → `/10` (10 aspirational criteria now:
C-09 through C-18). Max score and golden threshold unchanged.

---

## Criterion Summary

| ID | Criterion | Tier | Category |
|----|-----------|------|----------|
| C-01 | Complete verdict matrix — one block or row per criterion for each output; no cell blank or omitted | essential | completeness |
| C-02 | Evidence per verdict — each verdict cell cites a specific structural reference from the output | essential | correctness |
| C-03 | Formula-correct composite score — formula, weights, tier counts, and arithmetic applied correctly | essential | correctness |
| C-04 | Ranked leaderboard — all N outputs in a single descending list by composite score | essential | format |
| C-05 | Failure patterns identified — criteria failing across ALL outputs surfaced; absence stated if none | essential | coverage |
| C-06 | Excellence signals — outlier-high criterion-output pairs identified with structural mechanism named | recommended | depth |
| C-07 | Regression signals — degraded criterion-output pairs flagged when prior-round data is available | recommended | depth |
| C-08 | Per-output summary note — 1–3 sentence structural differentiator or miss per output | recommended | depth |
| C-09 | Golden threshold declaration per output — explicit YES/NO field in each output block | aspirational | format |
| C-10 | Failure-pattern root-cause diagnosis — "rubric gap" vs "skill design issue" label on each universal failure | aspirational | depth |
| C-11 | Rubric-adaptive formula derivation — tier counts derived from active rubric, not hardcoded literals | aspirational | correctness |
| C-12 | Structured diagnosis template — failure entries follow a fixed labeled template enforcing parallel structure | aspirational | format |
| C-13 | Derivation-complete gate marker — explicit completion marker after derivation block proves derivation preceded scoring | aspirational | correctness |
| C-14 | Required fields in primary output block — Golden and summary note appear as labeled slots inside the per-output verdict block, not deferred to synthesis | aspirational | format |
| C-15 | Post-scoring completeness scan — explicit verification pass after all output blocks confirms required in-block fields are present before the report is sealed | aspirational | correctness |
| C-16 | Pre-execution failure mode priming — anti-patterns placed before Phase 1 so failure mode context loads before any structural work begins | aspirational | format |
| C-17 | Self-referential anti-pattern priming — at least one anti-pattern entry targets the enforcement mechanisms defined in C-15 or C-16 themselves, placed in the pre-execution priming section | aspirational | correctness |
| C-18 | Full-envelope structural coverage — both a pre-Phase-1 failure mode priming block (C-16) and a post-output named scan (C-15) are present in the same execution unit, closing both ends of the structural execution window | aspirational | format |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)`, max 100.
**Golden threshold:** all 5 essentials PASS + composite >= 80.
```
