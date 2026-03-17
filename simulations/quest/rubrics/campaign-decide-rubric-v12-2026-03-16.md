Written to `simulations/quest/rubrics/campaign-decide-rubric-v12-2026-03-17.md`.

---

**One new criterion extracted from R12:**

| ID | Source | Pattern |
|----|--------|---------|
| C-34 | R12 V-05 Excellence Signal 1 | Confidence threshold propagated via top-level schema definition: thresholds encoded in the Confidence column header of the pre-Phase-0 schema preamble, causing one-definition/unlimited-propagation rather than per-table repetition. Distinct from C-33 (which allows thresholds anywhere). C-34 implies C-33; C-33 does not imply C-34. |

**Scoring model update:**

| Tier | v11 | v12 |
|------|-----|-----|
| Aspirational denominator | /25 | /26 |
| Aspirational total pts | 12.5 | 13.0 |
| Max composite | 102.5 | 103.0 |

The R12 scorecard had only one documented excellence signal, so only one criterion is added. The V-05 column-header passes on C-33 (V-03 also passes C-33 via column header) don't yield a new criterion — C-34 captures the stricter architectural pattern: the schema definition lives *before* Phase 0, not inside a Phase 5 output table.
