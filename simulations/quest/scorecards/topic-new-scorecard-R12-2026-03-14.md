---

## topic-new Round 12 — Scorecard

### Scoring Summary

All five variations score **identically** on the v11 rubric — this is the expected outcome when variation axes operate above the rubric ceiling.

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 (ES-1) | 5/5 | 3/3 | 28/30 | **99.33** |
| V-02 (ES-2) | 5/5 | 3/3 | 28/30 | **99.33** |
| V-03 (ES-3) | 5/5 | 3/3 | 28/30 | **99.33** |
| V-04 (ES-1+ES-2) | 5/5 | 3/3 | 28/30 | **99.33** |
| V-05 (ES-1+ES-2+ES-3) | 5/5 | 3/3 | 28/30 | **99.33** |

### Failures (shared by all)

- **C-18 FAIL** — No COVERAGE SCHEMA. Coverage constraints embedded inline in phase gates.
- **C-20 FAIL** — FIELD SCHEMA consequence column is single-tier. Recovery Cost column (V-03/V-05) is in pipeline overview, not FIELD SCHEMA — doesn't satisfy C-20's schema-level requirement.

### Top Variation

**V-05** — ranks first by excellence signal coverage (ES-1 + ES-2 + ES-3). Three independent failure axes closed: vocabulary-tier collapse, consumer improvisation at fill time, and skip-cost underestimation.

### Excellence Signals

**ES-1 (C-39 candidate)** — Full vocabulary anchoring: all three priority levels carry decision-state anchors in a dedicated Decision-State Anchor column. Closes recommended/optional collapse vector — substitution fails at all three tiers simultaneously, not just for "essential."

**ES-2 (C-40 candidate)** — Consumer-to-decision-table traceability: F-05 Consumer must appear verbatim as a Decision-Maker Role in the Phase 1 decision table. Phase 2 exit gate adds an explicit third checkpoint. Closes the orphaned-consumer failure mode where F-05 is formatted correctly but points to no actual decision.

**ES-3 (C-41 candidate)** — Recovery cost column: pipeline overview carries a third consequence column naming the concrete rework chain when a skip is caught late. Closes the skip-cost underestimation axis — "Re-run Phase 2, re-run Phase 3, re-write both output files" is a concrete operational cost, not an abstract failure state.

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Full priority-level vocabulary anchoring — all three levels carry decision-state anchors closing recommended/optional collapse alongside essential", "Consumer-to-decision-table traceability — F-05 Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table; Phase 2 exit gate verifies this as an explicit third independent checkpoint", "Recovery cost column — pipeline overview carries a third consequence column naming the concrete rework chain when a phase skip is caught late, making skip cost actionable rather than abstract"]}
```
