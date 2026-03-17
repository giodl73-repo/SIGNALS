Written to `simulations/quest/rubrics/campaign-decide-rubric-v11-2026-03-17.md`.

---

**Three new patterns extracted from R11:**

| ID | Source | Pattern |
|----|--------|---------|
| C-31 | V-03 | Phase 1a FINDING REGISTER `Switching Cost` column (4-column schema: `FID / Finding Summary / Primary Competitor / Switching Cost`, H/M/L). Independent of C-29 — that's the dual-signal flag; C-31 is the column that explains *why* inertia wins. |
| C-32 | V-04, V-05 | Phase 5 **Counter Block** distinct schema: `FID / Counter Claim / Rebuttal`. Gap Block is risks; Counter Block is the best argument *against* the recommendation with an inline rebuttal. C-30 requires 4 sub-tables; C-32 hardens the schema of the counter sub-table. |
| C-33 | V-05 | Confidence calibration with quantified thresholds: H = 80%+, M = 50–79%, L < 50%. A bare H/M/L label fails. Independent of C-09 (which requires FID citations in a Confidence Rationale column). |

**Scoring model update:**

| Tier | Before (v10) | After (v11) |
|------|-------------|-------------|
| Aspirational denominator | /22 | /25 |
| Aspirational total pts | 11.0 | 12.5 |
| Max composite | 101.0 | 102.5 |
