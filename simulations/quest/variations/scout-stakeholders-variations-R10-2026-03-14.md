File written. Here are the five Round 10 variations:

---

## Round 10 — scout-stakeholders — V-01 through V-05

**Rubric**: v10 (max 195 pts) | **Target**: First 195/195

---

### Variation axis map

| Variation | Axis | Predicted Score | Key hypothesis |
|-----------|------|----------------|---------------|
| **V-01** | All 29 combined | 195/195 | C-27+C-28 (R9 V-01) + C-29 (R9 V-03) are non-interfering; merging them in one prompt reaches the ceiling |
| **V-02** | C-29 deliberately absent | 190/195 | Isolates C-29 contribution; confirms it is the sole gap in the R9 V-01 configuration |
| **V-03** | C-27+C-28 deliberately absent | 185/195 | Isolates the champion chain; confirms their removal does not disturb C-29 |
| **V-04** | All 29 + engagement window | 195/195 | New derivation step (Step 5a: per-quadrant window) before Frame Type prefill; FAIL_WINDOW_MISMATCH at Step 6b; C-30a candidate |
| **V-05** | All 29 + gatekeeper trajectory | 195/195 | New trajectory table at Step 7 (Trending Engaged / Stalling / Trending Opposed + last observed signal); amendment-eligible; C-30b candidate |

---

### Structural changes from R9 baseline

**V-01** merges two R9 perfect-score patterns:
- Step 1a: adds resolution pathway table (Resolution Authority / Decision Required / Deadline) + `FAIL_NO_RESOLUTION_PATHWAY`
- Phase 1→2 gate checklist: adds "resolution pathway present for each conflict"
- Step 5b: champion depth scoring table (Authority/Proximity/Commitment 1–5, composite ≥ 9)
- Step 5c: champion durability (succession path + deterioration signals, `FAIL_NO_DURABILITY`)
- Amendment mandate: enumerates conflict resolution pathway entries alongside Step 6a prefill

**V-04** adds a pre-comms temporal constraint layer:
- Phase 3 grid gains `Engagement Window` column with per-quadrant rules (gatekeeper window ≤ lead time; inertia window opens pre-announcement)
- New Step 5a: quadrant window derivation table before champion assessment (champion renumbers to 5b/5c/5d)
- Step 6b timing must fall within derived window → `FAIL_WINDOW_MISMATCH`
- Amendment mandate extends to "Step 5a engagement window summaries"

**V-05** adds a directional commitment tracking layer at Step 7:
- Per-gatekeeper trajectory rating (Trending Engaged / Stalling / Trending Opposed)
- Last Observed Signal must be a concrete observable event with a date
- `FAIL_NO_TRAJECTORY` at Step 7
- Amendment mandate extends to "Step 7 gatekeeper trajectory entries"
- Amendment correct-form example shows trajectory entry revision

---

Written to: `simulations/quest/rubrics/scout-stakeholders-rubric-v10-R10-variate-2026-03-14.md`
